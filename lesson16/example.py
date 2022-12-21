import os
from pathlib import Path
import shutil

WORKING_DERICTORY = Path(__file__).parent.parent
EXCLUDE_FORMATS = [".pyc", '.iml']
RESULT_DIRECTORY = Path(WORKING_DERICTORY, "all_examples")


def foo(num):
    return 12 - num


def replace_example_files(directory):
    if not RESULT_DIRECTORY.exists():
        RESULT_DIRECTORY.mkdir()
    for item in os.listdir(directory):
        item_path = Path(directory, item)
        if item_path.is_dir():
            replace_example_files(item_path)
        else:
            name_file = item_path.name
            if item_path.suffix in EXCLUDE_FORMATS:
                continue
            if name_file.startswith("example"):
                shutil.copy(item_path, RESULT_DIRECTORY)


if __name__ == '__main__':
    replace_example_files(WORKING_DERICTORY)
