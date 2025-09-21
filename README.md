# TikTok Reddit Video Generator

An automated tool to generate TikTok-style videos in the style of Reddit stories, combining synthesized speech,
background music, images and videos.

## Features

- Asynchronous text-to-speech generation using `edge_tts`
- Automated video assembly with subtitles and background elements
- Configurable via environment variables
- Organized output structure
- Modular and extensible architecture

## Prerequisites

- Python 3.8+
- ffmpeg installed and in PATH
- Required Python packages:
    - edge-tts >= 6.1.7
    - moviepy >= 1.0.3
    - python-dotenv >= 1.0.0
    - numpy >= 1.24.0
    - pydub >= 0.25.1

## Project Structure

```
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── Bot/
│   ├── init.py
│   ├── main.py # Main script to run the bot
│   ├── config.py # Configuration settings
│   └── Scripts/
│           ├── Audio_maker.py # Script to generate audio from text
│           └── Video_Maker.py # Script to create video from audio and media
└── Content/
    ├── Audio/
    │       └── #Folder where audio files will be saved
    ├── Video/
    │       └── #Folder where video files will be saved
    └── Backgrounds/
            ├── font/ #Place your font here
            ├── Images/ #Place your background images here
            ├── Audio/ #Place your background music here
            └── Videos/ #Place your background videos here
```

## Installation

1. **System prerequisite**
    - Install Python 3.8+
    - Install ffmpeg and add it to PATH

2. **Project installation**
    - Clone the repository :
      ```
      git clone
      ```
    - Create the required folders :
      ```
      Content/
      ├── Audio/
      ├── Video/
      └── Background/
          ├── font/
          ├── Image/
          ├── Audio/
          └── Video/
      ```
    - Execute :
      ```
      pip install -r requirements.txt
      ```

3. **Configuration**
    - Paste `.env.example` to `.env`
    - Add your configurations in `.env` and change the parameters as needed
    - Add a background video to `Content/Background/Video/`
    - Add a background music to `Content/Background/Audio/`


4. **Launch**
   - change the tiktok text in `Bot/main.py` line 7 to whatever content you want
   - change the tiktok title in `Bot/main.py` line 8 to whatever question / title you want
   - Run the bot :
       ```
       python Bot/main.py
       ```
   
## Overall opinion

In my opinion, this project is good to create some tiktok reddit story videos. 
The only thing is that, even though the generation of the audio is fast, 
making the actual video is really long. 
As i tested, generating a minute-long video can take up to 10 minutes. 
which is ... questionable.
Perhaps using another library than moviepy could help, and also tweaking my code ??

## Authors

M1k36 \
:>
