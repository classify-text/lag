import shutil
import subprocess
import os
import platform

src_file = "attack.mov"
base, ext = os.path.splitext(src_file)


is_windows = platform.system() == "Windows"

for i in range(1, 6):
    new_file = f"{base}_{i}{ext}"
    

    shutil.copy(src_file, new_file)
    

    if is_windows:
        os.startfile(new_file)   # Windows
    else:
        subprocess.Popen(["open", new_file])  # macOS
