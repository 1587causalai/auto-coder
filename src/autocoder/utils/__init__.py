import os
from typing import Optional
import subprocess
import shutil
from loguru import logger

def get_last_yaml_file(actions_dir:str)->Optional[str]:
    action_files = [
            f for f in os.listdir(actions_dir) if f[:3].isdigit() and "_" in f and f.endswith(".yml")
        ]

    def get_old_seq(name):
        return name.split("_")[0]

    if not action_files:
        max_seq = 0
    else:
        seqs = [int(get_old_seq(f)) for f in action_files]
        max_seq = max(seqs)

    new_seq = str(max_seq + 1).zfill(12)
    prev_files = [f for f in action_files if int(get_old_seq(f)) < int(new_seq)]

    if not prev_files:
        return None
    else:
        prev_file = sorted(prev_files)[-1]  # 取序号最大的文件        
        return prev_file

def open_yaml_file_in_editor(new_file:str):
    try:
        if os.environ.get("TERMINAL_EMULATOR") == "JetBrains-JediTerm":
            subprocess.run(["idea", new_file])
        else:
            if shutil.which("code"):
                subprocess.run(["code", "-r", new_file])
            elif shutil.which("idea"):
                subprocess.run(["idea", new_file])
    except Exception as e:
        logger.info(
            f"Error opening editor, you can manually open the file: {new_file}"
        )