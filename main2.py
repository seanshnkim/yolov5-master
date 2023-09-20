from detect_distance import detect_depth_dist
from detect_custom import run, inference, get_centroid, parse_opt, check_requirements
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
model, dataset, webcam, save_dir = run(**vars(opt))

dc = DepthCamera()
start_time = time.time()

while (time.time() - start_time) < 100:
    centroid = inference(model, dataset, webcam, save_dir, **vars(opt))
    
    if torch.is_tensor(centroid[0]):
        # detect_depth_dist(dc, centroid)
        
        ret, depth_frame, color_frame = dc.get_frame()

        point_int = int(centroid[0].item()), int(centroid[1].item())
        # Show distance for a specific point
        # cv2.circle(color_frame, point_int, 5, (0, 200, 255), cv2.FILLED)
        distance = depth_frame[point_int[1], point_int[0]]
        print(f"distance: {distance}")
    time.sleep(0.1)