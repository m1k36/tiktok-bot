"""
Created: 09/09/2025
By: M1k36
File Description: Core file to create the video, add audio and musique
"""
import random
from moviepy import *
from Bot.config import *

"""
Main function to create the overall video with audio, text, image, music, ...
"""
def videoContentMaker(title: str, text_parts):
    #Load all the audio file and the intro question audio in the correct order
    audio_clips = [AudioFileClip(AUDIO_FOLDER_PATH + f"{title}/audio_question.mp3")]
    for i in range(0, len(text_parts)):
        audio_clips.append(AudioFileClip(AUDIO_FOLDER_PATH + f"{title}/audio_{i}.mp3"))

    #Load the background video that is the base to create the video
    background_video = VideoFileClip(BACKGROUND_VIDEO_FOLDER_PATH + BACKGROUND_VIDEO_NAME)
    background_video = background_video.without_audio()
    #Create a random subclip to make so each generated is kind of unique
    #and do not look all the same (need a long background video file)
    stamp_start, stamp_end = getRandomBGVideoStamp(background_video.duration, getAudioLength(audio_clips))
    background_video = background_video.subclipped(stamp_start, stamp_end)

    #Create an array that store each subclip in order
    #It is first initialise with the intro clip
    video_clips = [questionMaker(title, background_video, audio_clips)]

    #Create each subclip with the audio, subtitle, ...
    for index in range(0, len(text_parts)):
        #Get the correct subclip for the correct audio
        slice_stamp_start, slice_stamp_end = getVideoSliceStamp(audio_clips, index + 1)
        video_clip = background_video.subclipped(slice_stamp_start, slice_stamp_end)
        video_clip = video_clip.with_audio(audio_clips[index + 1])

        #Add the subtitle on the video
        text_clip = TextClip(font=FONT_FOLDER_PATH + FONT_NAME, color=SUBTITLE_TEXT_COLOR,
                             stroke_color=SUBTITLE_TEXT_STROKE_COLOR, text_align="center",
                             text=text_parts[index], font_size=SUBTITLE_TEXT_FONT_SIZE,
                             size=[int(background_video.w / 2) + 100, background_video.h - 100],
                             method="caption", stroke_width=SUBTITLE_TEXT_STROKE_WIDTH)
        text_clip = text_clip.with_duration(video_clip.duration)
        text_clip = text_clip.with_position(("center", "center"))

        #Merge all the element for the sub clip and add them to the overall video array
        video_clip_composite = CompositeVideoClip([video_clip, text_clip])
        video_clips.append(video_clip_composite)
        print(f"Stamps clip n°{index} finished !")

    print(f"✅ Stamps clip finished !")

    #Merge all the subclip in one video
    video = concatenate_videoclips(video_clips)

    #Load a music and add it to the video
    background_audio = AudioFileClip(BACKGROUND_AUDIO_FOLDER_PATH + BACKGROUND_AUDIO_NAME).with_duration(video.duration + 2)
    background_audio = background_audio.subclipped(2, video.duration + 2)
    #Merge the video audio with the music and tunes the volume to be goog
    video_audio = CompositeAudioClip([video.audio.with_volume_scaled(factor=VIDEO_VOICE_VOLUME_SCALED_FACTOR),
                                      background_audio.with_volume_scaled(factor=VIDEO_MUSIC_VOLUME_SCALED_FACTOR)
                                      ])

    #Add the new video audio mix with the music, to video and save it
    video = video.with_audio(video_audio)
    video.write_videofile(VIDEO_FOLDER_PATH + f"{title}.mp4", fps=VIDEO_FPS, bitrate=VIDEO_BITRATE, audio_bitrate=VIDEO_AUDIO_BITRATE)

    print(f"✅ Video generated !")

"""
Function to create the intro of the video, wich is a "reddit post" with a question (here "title") and 
return everything created.
"""
def questionMaker(title: str, background_video, audio_clips):
    slice_stamp_start, slice_stamp_end = getVideoSliceStamp(audio_clips, 0)
    video_clip = background_video.subclipped(slice_stamp_start, slice_stamp_end)

    # Audio for the intro clip
    audio = audio_clips[0]
    video_clip = video_clip.with_audio(audio)

    # Load the image reddit post to creat the sub clip intro for the video
    image = ImageClip(BACKGROUND_IMAGE_FOLDER_PATH + BACKGROUND_IMAGE_NAME).with_duration(audio.duration)
    image = image.resized(width=600, height=300)
    image = image.with_position(("center", "center"))

    # Create and place the subforum name on the image
    text_title = TextClip(color=QUESTION_TEXT_COLOR,
                          horizontal_align="left",
                          text_align="left", text=QUESTION_REDDIT_POST_NAME,
                          font_size=QUESTION_REDDIT_POST_NAME_FONT_SIZE,
                          stroke_width=QUESTION_REDDIT_POST_NAME_STROKE_WIDTH,
                          size=[550, 100], method="caption")
    text_title = text_title.with_duration(audio.duration)
    text_title = text_title.with_position(
        ((video_clip.w / 2) - (image.w/2) + (125), (video_clip.h / 2) - (image.h/2) - 15)
    )

    # Create and place the question name on the image
    text_question = TextClip(color=QUESTION_TEXT_COLOR,
                             horizontal_align="left",
                             text_align="left", text=title + " ?",
                             font_size=QUESTION_TEXT_FONT_SIZE,
                             stroke_width=QUESTION_TEXT_STROKE_WIDTH,
                             size=[500, 200], method="caption")
    text_question = text_question.with_duration(audio.duration)
    text_question = text_question.with_position(
        ((video_clip.w / 2) - (image.w/2) + (30), (video_clip.h / 2) - (image.h/2) + (60))
    )

    # return the sub clip
    video_clip_composite = CompositeVideoClip([video_clip, image, text_title, text_question])
    print("Question clip finished !")
    return video_clip_composite


"""
------------------------------------------------------------
Usefull func to treat video audio with the video background :>
------------------------------------------------------------
1- get the overall audio text generated length (in second)
2- get the time stamp to create the subclip according to the audio file placement
3- get an random large subclip of the background video to create the video, so each video is a bit random 
   (the longer is the background video, the more unique each video created are)
"""
def getAudioLength(audio_clips):
    length = 0
    for audio_clip in audio_clips:
        length += audio_clip.duration
    return length

def getVideoSliceStamp(audio_clips, audio_index):
    start_stamp = 0
    for i in range(0, len(audio_clips)):
        if i == audio_index:
            return start_stamp, start_stamp + audio_clips[i].duration
        else:
            start_stamp += audio_clips[i].duration
    #Safe return
    return 0, 0

def getRandomBGVideoStamp(video_duration: int, audio_duration: int):
    stamp_start = random.randint(0, int(video_duration - audio_duration + 1))
    stamp_end = stamp_start + audio_duration

    return stamp_start, stamp_end