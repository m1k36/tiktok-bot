"""
Created: 09/09/2025
By: M1k36
File Description: Core file to create audio for the video via gTTS
"""
import edge_tts
import asyncio
from moviepy import AudioFileClip
from Bot.config import *

"""
Main function to create all audio part.
It use edge_tts and asynchronously create audio since we do not need to wait for each audio in order and just need to wait
for all audio to be created and saved. 
"""
async def audioContentMaker(text: str, title: str):
    #Make sure the audio folder exist, and if not create the folder to store audio files
    os.makedirs(AUDIO_FOLDER_PATH + f"{title}", exist_ok=True)
    #Split the text to create each audio
    text_parts = splitText(text)

    """
    Asynchronous function to create an audio with provided text part.
    """
    async def gtts_api_async(text_part: str, index: int, is_question: bool):
        #If the text is a questio, we don't remove the blank audio at the end
        if is_question:
            communicate = edge_tts.Communicate(text_part+" ?", voice=EDGE_TTS_VOICE_TYPE, rate=TITLE_SPEED_RATE)
            await communicate.save(AUDIO_FOLDER_PATH + f"{title}/audio_question.mp3")
            print(f"Audio clip Question finished !")
            return
        #If the text is not a question, we remove the blank audio at the end to make the video less boring
        else:
            communicate = edge_tts.Communicate(text_part, voice=EDGE_TTS_VOICE_TYPE, rate=TEXT_SPEED_RATE)
            await communicate.save(AUDIO_FOLDER_PATH + f"{title}/audio_{index}.mp3")

            audio = AudioFileClip(AUDIO_FOLDER_PATH + f"{title}/audio_{index}.mp3")
            audio = audio.subclipped(0, audio.duration - 0.5)
            audio.write_audiofile(AUDIO_FOLDER_PATH + f"{title}/audio_{index}.mp3",  write_logfile=False, logger=None)

            print(f"Audio clip n°{index} finished !")
            return

    #Add all audio task to generate in an array and asynchronously launch them all and wait for every task to be done
    tasks = [gtts_api_async(text_part, i, False) for i, text_part in enumerate(text_parts)]
    tasks.append(gtts_api_async(title, -1, True))
    await asyncio.gather(*tasks)

    print(f"✅ Audio Generated !")
    return text_parts

"""
------------------------------------------------------------
Usefull func to treat audio :]
------------------------------------------------------------
1- Custom split function to have every text part for the audio. Splitting the text is usefull to have a small text to be 
   generate by edge_tts and to have a easy way to create subtitle.
"""
def splitText(text: str):
    segments = [text]
    for separator in SEPARATORS:
        new_segments = []
        for segment in segments:
            for part in segment.split(separator):
                new_segments.append(part)
        segments = new_segments
    return segments
