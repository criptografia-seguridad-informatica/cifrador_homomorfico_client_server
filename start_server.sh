#!/bin/sh

# Before running run in terminal sudo chmod +x start_server.sh
docker build -t homomorphic_encryption_server:latest -f Dockerfile .
docker rm homomorphic_encryption_server
docker run -it --name homomorphic_encryption_server -p 5000:5000 homomorphic_encryption_server:latest ./server/main.py