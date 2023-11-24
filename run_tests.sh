#!/bin/sh
# Before running run in terminal sudo chmod +x run_tests.sh

docker build -t pytest-image .

if [ -n "$1" ]; then
  ENTRYPOINT="pytest $1"
else
  ENTRYPOINT="pytest"
fi

docker run --entrypoint "$ENTRYPOINT" pytest-image
