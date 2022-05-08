import os
import shutil
from os import path
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1].resolve()  # converterApi root directory


def clear_detect_dir():
    target_path = Path(ROOT, 'yolov5/runs/detect/exp')

    if path.exists(target_path):
        shutil.rmtree(target_path)

        print("Directory removed: " + str(target_path))
    else:
        print("Directory does not exists.")


def create_result_template():
    target_path = Path(ROOT, 'result.html')

    if path.exists(target_path):
        os.remove(target_path)

        print("File removed: " + str(target_path))

    src = Path(ROOT, 'default.html')
    dst = Path(ROOT, 'result.html')
    shutil.copy(src, dst)
