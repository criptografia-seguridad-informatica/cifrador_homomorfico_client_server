#!/bin/sh

# Before running run in terminal sudo chmod +x start_client.sh
docker build -t homomorphic_encryption_client:latest -f Dockerfile .
docker rm homomorphic_encryption_client
docker run -it --name homomorphic_encryption_client --network=host homomorphic_encryption_client:latest ./client/main.py