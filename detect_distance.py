import cv2
import pyrealsense2
from realsense_depth import *

point = (400, 300)

# def detect_depth_dist(point):
    # # Initialize Camera Intel Realsense
dc = DepthCamera()

def show_distance(event, x, y, args, params):
    point = (x, y)

# Create mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)

while True:
    # type(depth_frame) = np.arrayS
    # type(color_frame) = np.array
    # ret == True
    # depth_frame.shape = (480, 640)
    # color_frame.shape = (480, 640, 3)
    ret, depth_frame, color_frame = dc.get_frame()
    
    # flip the image
    color_frame = cv2.flip(color_frame,1)
    depth_frame = cv2.flip(depth_frame,1)

    # point_int = int(point[0].item()), int(point[1].item())
    # Show distance for a specific point
    cv2.circle(color_frame, point, 5, (0, 200, 255), cv2.FILLED)
    distance = depth_frame[point[1], point[0]]

    cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

# point = (400, 300)
# detect_depth_dist(point)