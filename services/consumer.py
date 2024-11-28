import json
from kafka import KafkaConsumer, KafkaProducer
from configs.kafka_config import KAFKA_BROKER, INPUT_TOPIC, OUTPUT_TOPIC
from services.image_processor import process_image

def start_consumer():
    consumer = KafkaConsumer(
        INPUT_TOPIC,
        bootstrap_servers=[KAFKA_BROKER],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    
    print("Consumer is running...")
    for message in consumer:
        image_data = message.value
        image_path = image_data["path"]
        
        try:
            detections = process_image(image_path)
            output = {"path": image_path, "detections": detections}
            producer.send(OUTPUT_TOPIC, value=output)
            print(f"Processed image: {image_path}")
        except Exception as e:
            print(f"Error processing image {image_path}: {str(e)}")
