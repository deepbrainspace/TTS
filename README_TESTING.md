# Local Testing Guide

## Prerequisites
```bash
# Install CUDA toolkit and drivers
apt-get update
apt-get install -y \
    nvidia-cuda-toolkit \
    nvidia-driver-535

# Verify GPU access
nvidia-smi
```

## Environment Setup
```bash
# Install UV (faster than venv)
pip install uv

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate

# Clone repository (if not done)
git clone https://github.com/your-repo/TTS.git
cd TTS

# Install TTS with all dependencies using UV
uv pip install -e ".[all]"

# Install specific compatible versions
uv pip install "numpy>=1.24.3,<2.0.0"
uv pip install "torch==2.1.0"
uv pip install "torchaudio==2.1.0"

# Install testing dependencies
uv pip install requests tqdm

# Download required models
python3 scripts/download_models.py
```

## Testing
```bash
# Verify GPU setup
python3 scripts/test_gpu.py

# Start TTS server
python3 scripts/run_server.py

# Test TTS functionality
python3 scripts/test_tts.py
```

## Troubleshooting
- If GPU issues: Check `nvidia-smi` output
- If space issues: Check `df -h`
- If process hangs: Check `ps aux | grep python`
- If UV issues: Try `uv pip list` to verify packages
- If model download fails: Check space with `df -h` and internet connection 