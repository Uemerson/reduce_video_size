import ffmpeg


def reduce_video_size(input_path, output_path, crf=28, preset="slow"):
    """
    Reduces the size of an MKV video using FFmpeg.

    Parameters:
        input_path (str): Path to the original .mkv video file.
        output_path (str): Path to the output compressed video file.
        crf (int): Constant Rate Factor (quality, from 18 to 35; lower is
                   better quality).
        preset (str): Compression speed (options: ultrafast, superfast,
                      veryfast, faster, fast, medium, slow, slower, veryslow).
    """
    try:
        (
            ffmpeg.input(input_path)
            .output(
                output_path,
                vcodec="libx264",
                crf=crf,
                preset=preset,
                acodec="aac",
                audio_bitrate="128k",
            )
            .run(overwrite_output=True)
        )
        print("Video compressed successfully!")
    except ffmpeg.Error as e:
        print("Error while compressing the video:", e)


reduce_video_size("original_video.mkv", "compressed_video.mkv")
