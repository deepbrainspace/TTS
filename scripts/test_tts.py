import requests
import json

def test_health():
    response = requests.get("http://localhost:5002/health")
    print("Health check:", response.json())

def test_tts():
    data = {
        "text": "This is a test of the TTS system",
        "language": "en"
    }
    
    response = requests.post(
        "http://localhost:5002/tts",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code == 200:
        with open("test_output.wav", "wb") as f:
            f.write(response.content)
        print("TTS test successful! Output saved to test_output.wav")
    else:
        print("TTS test failed:", response.text)

if __name__ == "__main__":
    test_health()
    test_tts() 