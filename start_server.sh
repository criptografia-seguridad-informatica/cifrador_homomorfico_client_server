#!/bin/sh

# Before running run in terminal sudo chmod +x start_server.sh
docker build -t server:latest -f Dockerfile.server .
docker rm homomorphic_encryption_server
docker run -it --name homomorphic_encryption_server -p 5000:5000 server:latest