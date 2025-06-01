# Reduce Video Size

This project is a simple tool to compress `.mkv` video files using Python, FFmpeg, and Docker.

## Features

- Reduces the size of `.mkv` videos using the H.264 codec and AAC audio compression.
- Allows you to adjust compression quality and speed.

## Prerequisites

- [Docker](https://www.docker.com/)
- (Optional) Python 3.13+ and [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) for local execution

## How to Use

### 1. Place the Original Video

Put your `original_video.mkv` file in the project root.

### 2. Run the Automation Script

In the terminal, run:

```sh
bash up.sh
```

The script will:
- Activate the virtual environment (if it exists)
- Update `requirements.txt`
- Build the Docker image
- Run the container to compress the video

### 3. Result

The compressed video will be saved as `compressed_video.mkv` in the project root.

## Customization

You can adjust compression parameters by editing `main.py`:

- `crf`: Quality factor (lower is better quality and larger size)
- `preset`: Compression speed (`ultrafast`, `fast`, `medium`, `slow`, etc.)

## Project Structure

```
.
├── Dockerfile
├── main.py
├── original_video.mkv
├── compressed_video.mkv
├── requirements.txt
├── up.sh
└── .gitignore
```

## License

MIT