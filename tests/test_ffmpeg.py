import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

ffmpeg_bin = os.getenv("FFMPEG_BIN")

print("FFMPEG_BIN =", ffmpeg_bin)

os.environ["PATH"] += os.pathsep + ffmpeg_bin

result = subprocess.run(
    ["ffmpeg", "-version"],
    capture_output=True,
    text=True,
)

print(result.returncode)
print(result.stdout)
print(result.stderr)