#!/usr/bin/env bash
apt-get update
apt-get install -y cmake g++ build-essential libboost-all-dev libopenblas-dev liblapack-dev
pip install -r requirements.txt
