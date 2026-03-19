import shutil
import subprocess
import os
import platform
import uuid

src_file = "attack.mov"
base, ext = os.path.splitext(src_file)

system_name = platform.system()

for i in range(5):
    new_file = f"{uuid.uuid4()}{ext}"
    shutil.copy(src_file, new_file)

    if system_name == "Windows":
        subprocess.Popen(["cmd", "/c", "start", "", new_file], shell=True)
    elif system_name == "Darwin":
        subprocess.Popen(["open", new_file])
    else:
        subprocess.Popen(["xdg-open", new_file])
