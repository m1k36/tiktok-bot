import os
from dotenv import load_dotenv

#Load .env variable from the .env file
load_dotenv()

"""
Get env variable and raise an error if a variable doesn't exist or is not found.
"""
def require_env(var_name: str):
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"Missing .env variable : {var_name}")
    return value

# -----------------------------
# FOLDER PATH FOR CONTENT
# -----------------------------
MAIN_FOLDER_PATH = require_env("MAIN_FOLDER_PATH")
AUDIO_FOLDER_PATH = require_env("AUDIO_FOLDER_PATH")
VIDEO_FOLDER_PATH = require_env("VIDEO_FOLDER_PATH")
BACKGROUND_VIDEO_FOLDER_PATH = require_env("BACKGROUND_VIDEO_FOLDER_PATH")
BACKGROUND_AUDIO_FOLDER_PATH = require_env("BACKGROUND_AUDIO_FOLDER_PATH")
BACKGROUND_IMAGE_FOLDER_PATH = require_env("BACKGROUND_IMAGE_FOLDER_PATH")
FONT_FOLDER_PATH = require_env("FONT_FOLDER_PATH")

# -----------------------------
# CONTENT NAMES
# -----------------------------
BACKGROUND_VIDEO_NAME = require_env("BACKGROUND_VIDEO_NAME")
BACKGROUND_AUDIO_NAME = require_env("BACKGROUND_AUDIO_NAME")
BACKGROUND_IMAGE_NAME = require_env("BACKGROUND_IMAGE_NAME")
FONT_NAME = require_env("FONT_NAME")

# -----------------------------
# AUDIO CUSTOM PARAMETER
# -----------------------------
EDGE_TTS_VOICE_TYPE = require_env("EDGE_TTS_VOICE_TYPE")
TITLE_SPEED_RATE = require_env("TITLE_SPEED_RATE")
TEXT_SPEED_RATE = require_env("TEXT_SPEED_RATE")
SEPARATORS = eval(require_env("SEPARATORS"))  # Not the best but hey why not :>

# -----------------------------
# VIDEO CUSTOM PARAMETER
# -----------------------------
VIDEO_FPS = int(require_env("VIDEO_FPS"))
VIDEO_BITRATE = require_env("VIDEO_BITRATE")
VIDEO_AUDIO_BITRATE = require_env("VIDEO_AUDIO_BITRATE")
VIDEO_VOICE_VOLUME_SCALED_FACTOR = float(require_env("VIDEO_VOICE_VOLUME_SCALED_FACTOR"))
VIDEO_MUSIC_VOLUME_SCALED_FACTOR = float(require_env("VIDEO_MUSIC_VOLUME_SCALED_FACTOR"))

SUBTITLE_TEXT_COLOR = require_env("SUBTITLE_TEXT_COLOR")
SUBTITLE_TEXT_STROKE_COLOR = require_env("SUBTITLE_TEXT_STROKE_COLOR")
SUBTITLE_TEXT_FONT_SIZE = int(require_env("SUBTITLE_TEXT_FONT_SIZE"))
SUBTITLE_TEXT_STROKE_WIDTH = float(require_env("SUBTITLE_TEXT_STROKE_WIDTH"))

QUESTION_REDDIT_POST_NAME = require_env("QUESTION_REDDIT_POST_NAME")
QUESTION_REDDIT_POST_NAME_COLOR = require_env("QUESTION_REDDIT_POST_NAME_COLOR")
QUESTION_REDDIT_POST_NAME_FONT_SIZE = int(require_env("QUESTION_REDDIT_POST_NAME_FONT_SIZE"))
QUESTION_REDDIT_POST_NAME_STROKE_WIDTH = float(require_env("QUESTION_REDDIT_POST_NAME_STROKE_WIDTH"))

QUESTION_TEXT_COLOR = require_env("QUESTION_TEXT_COLOR")
QUESTION_TEXT_FONT_SIZE = int(require_env("QUESTION_TEXT_FONT_SIZE"))
QUESTION_TEXT_STROKE_WIDTH = float(require_env("QUESTION_TEXT_STROKE_WIDTH"))
