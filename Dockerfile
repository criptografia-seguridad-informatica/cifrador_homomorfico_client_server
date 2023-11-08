FROM ubuntu:22.04
RUN apt update && apt install -y git build-essential cmake python3 python3-dev python3-pip
RUN pip3 install numpy pybind11 pytest
RUN mkdir app
RUN git clone https://github.com/Huelse/SEAL-Python.git
WORKDIR /SEAL-Python

RUN git submodule update --init --recursive
RUN cd SEAL && cmake -S . -B build -DSEAL_USE_MSGSL=OFF -DSEAL_USE_ZLIB=OFF && cmake --build build
RUN python3 setup.py build_ext -i

RUN cp seal.*.so ../app

WORKDIR /
RUN rm -r SEAL-Python

WORKDIR /app
COPY . ./

# Hay que copiar este archivo en todos lados donde se use la librería de SEAL
RUN cp seal.*.so ./client/model
RUN cp seal.*.so ./server/model
RUN cp seal.*.so ./examples


ENTRYPOINT ["python3"]