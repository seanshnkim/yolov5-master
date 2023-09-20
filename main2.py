from detect_distance import detect_depth_dist
from detect import run, parse_opt, check_requirements
from pathlib import Path
import sys
import os

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

opt = parse_opt()
check_requirements(ROOT / 'requirements.txt', exclude=('tensorboard', 'thop'))
run(**vars(opt))
