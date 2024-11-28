import argparse
from services.producer import start_producer
from services.consumer import start_consumer
from services.collector import collect_results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Distributed Image Recognition System")
    parser.add_argument("--mode", choices=["producer", "consumer", "collector"], required=True,
                        help="Mode to run the program: producer (send images), consumer (process images), collector (collect results)")
    parser.add_argument("--image-dir", help="Directory with images for producer mode")
    parser.add_argument("--output-dir", help="Directory to save results for collector mode")
    args = parser.parse_args()
    
    if args.mode == "producer":
        if not args.image_dir:
            print("Image directory is required for producer mode.")
        else:
            start_producer(args.image_dir)
    elif args.mode == "consumer":
        start_consumer()
    elif args.mode == "collector":
        if not args.output_dir:
            print("Output directory is required for collector mode.")
        else:
            collect_results(args.output_dir)
