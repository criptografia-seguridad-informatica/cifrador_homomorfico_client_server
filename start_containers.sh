#!/bin/sh

# Before running run in terminal sudo chmod +x start_containers.sh

docker build -t client:latest -f Dockerfile.client .
docker build -t server:latest -f Dockerfile.server .

docker run -d -p 5000:5000 server:latest

docker run -it --network=host client:latest