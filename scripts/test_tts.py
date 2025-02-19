import requests
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", default="Hello, this is a test.")
    parser.add_argument("--language", default="en")
    parser.add_argument("--output", default="test.wav")
    args = parser.parse_args()

    # Proper request format
    payload = {
        "text": args.text,
        "language": args.language
    }

    try:
        response = requests.post(
            "http://localhost:5002/api/tts",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            with open(args.output, "wb") as f:
                f.write(response.content)
            print(f"Audio saved to {args.output}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to server. Is the server running?")
        print("Start server with: python3 -m TTS.server.server --model_path models/... --config_path models/...")

if __name__ == "__main__":
    main() 