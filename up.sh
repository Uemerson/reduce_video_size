#!/bin/bash

docker build -t video-compressor .
docker run --name reduce_video_size_container --rm -v "$PWD:/app" video-compressor