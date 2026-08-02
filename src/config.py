import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "dataset"

FFMPEG_BIN = os.getenv("FFMPEG_BIN", "")
FFMPEG_PATH = os.getenv("FFMPEG_PATH", "")

TESSERACT_PATH = os.getenv("TESSERACT_PATH", "")

MESSAGES_FILE = DATASET_DIR / "messages.csv"
USERS_FILE = DATASET_DIR / "users.csv"
GROUPS_FILE = DATASET_DIR / "groups.csv"
GROUP_MEMBERS_FILE = DATASET_DIR / "group_members.csv"
MESSAGE_HISTORY_FILE = DATASET_DIR / "message_history.csv"
MESSAGE_EVENTS_FILE = DATASET_DIR / "message_events.csv"
BUSINESS_ACCOUNTS_FILE = DATASET_DIR / "business_accounts.csv"
USER_BUSINESS_HISTORY_FILE = DATASET_DIR / "user_business_history.csv"
IMAGES_FILE = DATASET_DIR / "images.csv"
VOICE_NOTES_FILE = DATASET_DIR / "voice_notes.csv"
OUTPUT_FILE = DATASET_DIR / "output.csv"