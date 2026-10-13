FROM python:3.11-slim

WORKDIR /workspace

# Install dependensi sistem dasar
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install pustaka ML dan RL
RUN pip install --no-cache-dir \
    numpy \
    matplotlib \
    torch \
    tqdm

CMD ["/bin/bash"]