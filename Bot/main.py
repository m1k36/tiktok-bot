"""
Created: 09/09/2025
By: M1k36
File Description: Core file to launch the bot
"""
import time
import asyncio
from Scripts.Video_Maker import videoContentMaker
from Scripts.Audio_maker import audioContentMaker

"""
tiktok_text: a generated random story, WARNING : no "." at the end
tiktok_title: the title for all the generated content for the video
"""
tiktok_text = "So this happened last month and my friends won’t stop bringing it up. I was at the gym, feeling confident for once, and I decided to try the rowing machine. You know, the one that makes you look like a Viking in training. Anyway, I sit down, put my headphones in, and start going at it like I’m auditioning for the Olympics. After about 3 minutes, I notice people staring. I’m thinking, “Yeah, must be impressed with my technique.” Spoiler: they were not. Turns out, I forgot to actually set the resistance and the chain wasn’t hooked properly. So from the outside, I basically looked like a lunatic flapping my arms back and forth in fast-forward, with zero resistance, like I was paddling for dear life on invisible water. The best part? My headphones had disconnected, and my phone was blasting “Eye of the Tiger” at full volume. I didn’t realize until a trainer walked over, barely holding back laughter, and fixed the machine for me. Now everyone at the gym knows me as “the cardio mime"
tiktok_title = 'What is the craziest and funniest thing that happened to you'

"""
Main routine that:
Firstly, create all the audio based on the text provided.
secondly, create and add all together: the audio, the music, the reddit "post" and the background video.
"""
async def routine():
    text_parts = await audioContentMaker(tiktok_text, tiktok_title)
    videoContentMaker(tiktok_title, text_parts)

"""
Main thing to start the process.
"""
if __name__ == '__main__':
    start = time.time()

    asyncio.run(routine())

    end = time.time()
    print(f"⏳ Elapse time  : {end - start:.2f} sec")
