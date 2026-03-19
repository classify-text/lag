import shutil
import subprocess
import os
import platform
import uuid

src_file = "attack.mov"
base, ext = os.path.splitext(src_file)

is_windows = platform.system() == "Windows"
is_mac = platform.system() == "Darwin"

for i in range(5):
    new_file = f"{uuid.uuid4()}{ext}"
    shutil.copy(src_file, new_file)
    
    if is_windows:
        subprocess.Popen(["cmd", "/c", "start", "", new_file])
    elif is_mac:
        subprocess.Popen(["open", new_file])
    else:
        subprocess.Popen(["xdg-open", new_file])
