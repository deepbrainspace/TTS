from TTS.server.server import create_argparser, app
from TTS.api import TTS
import argparse
import os

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", default=True)
    parser.add_argument("--port", type=int, default=5002)
    args = parser.parse_args()
    
    # Initialize TTS with model name
    print("Initializing TTS model...")
    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2",
        gpu=True  # Enable GPU
    )
    print("Model initialized successfully!")
    
    # Start server
    print(f"Starting server on port {args.port}...")
    app.run(debug=args.debug, port=args.port, host="0.0.0.0")

if __name__ == "__main__":
    main() 