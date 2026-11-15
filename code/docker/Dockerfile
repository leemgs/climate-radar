# Build from the repository root:
#   docker build -t climate-radar -f code/docker/Dockerfile .
#   docker run --rm -v $PWD:/app climate-radar
FROM python:3.11-slim
WORKDIR /app
COPY code/requirements.txt code/requirements.txt
RUN pip install --no-cache-dir -r code/requirements.txt
COPY . .
WORKDIR /app/code
CMD ["make", "reproduce"]
