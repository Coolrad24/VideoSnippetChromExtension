from pathlib import Path

import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip
import os.path

def extract_audio(video_file):
    # Get only filename

    final_audio_file = f'{Path(video_file).stem}.mp3'
    if not os.path.exists(final_audio_file):
        # Read the video file
        clip = mp.VideoFileClip(video_file)
        # Save the audio file
        clip.audio.write_audiofile(final_audio_file)
    return final_audio_file


def millisec_2_sec(time):
    return time / 1000


# Start and end are in milliseconds
def cut_video(video_file, start, end):
    # Get only filename
    final_video_file = f'final_{Path(video_file).stem}.mp4'
    # Read the file
    clip = mp.VideoFileClip(video_file)
    # Trim the video
    clip = clip.subclip(millisec_2_sec(start), millisec_2_sec(end))
    # Save Video
    clip.write_videofile(final_video_file)
    return final_video_file

# cut_video('video.mp4', 190, 3114)





#
# def add_subtitle():
#     generator = lambda txt: mp.TextClip(txt, font='Arial', fontsize=24, color='white')
#     subs = [((0, 4), 'subs1'),
#             ((4, 9), 'subs2'),
#             ((9, 12), 'subs3'),
#             ((12, 16), 'subs4')]
#     subtitles = SubtitlesClip(subs, generator)
#
#     video = mp.VideoFileClip("video.mp4")
#     result = mp.CompositeVideoClip([video, subtitles.set_pos(('center', 'bottom'))])
#
#     result.write_videofile("output.mp4", fps=video.fps, temp_audiofile="video.m4a", remove_temp=True,
#                            codec="libx264", audio_codec="aac")
#
#
# add_subtitle()