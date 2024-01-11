from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import concatenate_videoclips

def cut_video(input_path, start_time, end_time, output_path):
    # Convert time strings to seconds
    start_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time.split(':')))
    end_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], end_time.split(':')))

    # Load video clip
    video_clip = VideoFileClip(input_path)

    # Clip before the specified range
    clip_before = video_clip.subclip(0, start_time_seconds)

    # Clip after the specified range
    clip_after = video_clip.subclip(end_time_seconds, video_clip.duration)

    # Concatenate the clips
    final_clip = concatenate_videoclips([clip_before, clip_after])

    # Write the new video to a file
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp.m4a", remove_temp=True)
    
def extract_clip_from_video(input_path, start_time, end_time, output_path):
    # Convert time strings to seconds
    start_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time.split(':')))
    end_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], end_time.split(':')))

    # Load video clip
    video_clip = VideoFileClip(input_path)

    # Cut the video using moviepy
    new_clip = video_clip.subclip(start_time_seconds, end_time_seconds)

    # Write the new video to a file
    new_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp.m4a", remove_temp=True)

# Example usage
input_video_path = "screen.mp4"
start_time = "00:46:34"
end_time = "01:01:42"
output_video_path = "cut_screen.mp4"

cut_video(input_video_path, start_time, end_time, output_video_path)
