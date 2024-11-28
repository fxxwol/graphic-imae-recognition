import json
from kafka import KafkaProducer
from pathlib import Path
from configs.kafka_config import KAFKA_BROKER, INPUT_TOPIC

def start_producer(image_dir):
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    
    image_files = list(Path(image_dir).rglob("*.jpg"))
    if not image_files:
        print("No images found in the directory.")
        return
    
    for image_path in image_files:
        image_data = {"path": str(image_path)}
        producer.send(INPUT_TOPIC, value=image_data)
        print(f"Sent image to topic: {image_path}")
    
    print("All images sent.")
