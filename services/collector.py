import os
import json
from pathlib import Path
from kafka import KafkaConsumer
from configs.kafka_config import KAFKA_BROKER, OUTPUT_TOPIC

def collect_results(output_dir):
    consumer = KafkaConsumer(
        OUTPUT_TOPIC,
        bootstrap_servers=[KAFKA_BROKER],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    os.makedirs(output_dir, exist_ok=True)
    print("Result collector is running...")
    
    for message in consumer:
        result_data = message.value
        image_path = result_data["path"]
        detections = result_data["detections"]
        
        output_path = Path(output_dir) / (Path(image_path).stem + "_results.json")
        with open(output_path, "w") as f:
            json.dump(detections, f, indent=4)
        
        print(f"Results saved for {image_path} at {output_path}")
