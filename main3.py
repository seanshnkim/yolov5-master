from detect_distance import detect_depth_dist
from detect_custom import run, inference, get_centroid, parse_opt, check_requirements
# from detect_distance import detect_depth_dist
from realsense_depth import *
from pathlib import Path
import sys
import os
import torch
import time

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

opt = parse_opt()
check_requirements(ROOT / 'requirements.txt', exclude=('tensorboard', 'thop'))

# run 함수를 돌리면 뎁스카메라 frame이 들어오지 않는다. URL로 받아온다고 해도.
model, dataset, webcam, save_dir = run(**vars(opt))

# dc = DepthCamera()

centroid = [-1, -1]
# while not torch.is_tensor(centroid[0]):


# print(f"centroid: {centroid}")

# centroid_pix = int(centroid[0].item()), int(centroid[1].item())

while True:
    # _, depth_frame, _ = dc.get_frame()
    centroid, label = inference(model, dataset, webcam, save_dir, **vars(opt))
    if torch.is_tensor(centroid[0]):
        centroid_pix = int(centroid[0].item()), int(centroid[1].item())
    # distance = depth_frame[centroid_pix[1], centroid_pix[0]]
    # print(f"distance: {distance}")
        print(f"Detected: {label}, bbox center: {centroid_pix}")
    time.sleep(0.1)