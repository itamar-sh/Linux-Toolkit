# from moviepy.editor import VideoFileClip, clips_array

# # Load the video clips
# clip_sound = VideoFileClip("sound.mp4")
# clip_screen = VideoFileClip("screen.mp4")

# # Crop the top half of the screen video
# clip_screen_cropped = clip_screen.crop(y1=0, y2=clip_screen.h / 2)

# # Combine the videos vertically with audio from the first video
# final_clip = clips_array([[clip_sound], [clip_screen_cropped]])

# # Write the result to a file
# final_clip.write_videofile("combined_video.mp4", codec="libx264", audio_codec="aac")


from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def merge_videos(background_path, speaker_path, output_path):
    # Load video clips
    background_clip = VideoFileClip(background_path)
    speaker_clip = VideoFileClip(speaker_path)

    # Resize the speaker video to a larger box
    speaker_clip_resized = speaker_clip.resize(width=background_clip.w // 6)

    # Calculate the position
    # posx = int(speaker_position[1] == 'left') * speaker_clip_resized.size[0]
    # posy = int(speaker_position[0] == 'top') * speaker_clip_resized.size[1]

    # Overlay the speaker video on top of the background video
    final_clip = CompositeVideoClip([background_clip.set_pos('center'), speaker_clip_resized.set_position((0, 0))])

    # Set the audio of the final clip to the audio from the speaker video
    final_clip = final_clip.set_audio(speaker_clip.audio)

    # Write the final video to a file
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp.m4a", remove_temp=True)

# Example usage
background_video_path = "cyber_law2_screen.mp4"
speaker_video_path = "cyber_law2_sound.mp4"
output_video_path = "cyber_law2_combined.mp4"

merge_videos(background_video_path, speaker_video_path, output_video_path)
