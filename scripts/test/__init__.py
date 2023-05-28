from pathlib import Path
import sys
import os

# ==================== sys.path BASE_DIR 추가 ====================
BASE_DIR : str = os.path.dirname(Path(__file__).resolve().parent)
sys.path.append(BASE_DIR)
from parsing import get_soup_obj,parser,download_csv
# ====================                        ====================