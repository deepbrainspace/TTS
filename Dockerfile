FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV COQUI_TOS_AGREED=1

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    espeak-ng \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the TTS code
COPY . /app/TTS/

# Create and activate virtual environment using uv
RUN pip3 install uv
RUN uv venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Install TTS and dependencies with all extras
WORKDIR /app/TTS
RUN uv pip install -e ".[all]"

# Install specific versions that are compatible
RUN uv pip install "numpy>=1.24.3,<2.0.0"
RUN uv pip install "torch==2.1.0"
RUN uv pip install "torchaudio==2.1.0"

# Pre-download the model during build
RUN mkdir -p /root/.local/share/tts && \
    python3 -c "import numpy; print('Numpy version:', numpy.__version__)" && \
    python3 -c "from TTS.utils.manage import ModelManager; ModelManager().download_model('tts_models/multilingual/multi-dataset/xtts_v2')"

EXPOSE 5002

# Add a health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5002/health || exit 1
