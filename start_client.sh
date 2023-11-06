#!/bin/sh

# Before running run in terminal sudo chmod +x start_client.sh
docker build -t client:latest -f Dockerfile.client .
docker rm homomorphic_encryption_client
docker run -it --name homomorphic_encryption_client --network=host client:latest
