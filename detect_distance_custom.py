import cv2

def show_depth_distance(point, dc):
    ret, depth_frame, color_frame = dc.get_frame()
    
    # flip the image
    color_frame = cv2.flip(color_frame,1)
    depth_frame = cv2.flip(depth_frame,1)

    # Show distance for a specific point
    cv2.circle(color_frame, point, 5, (0, 200, 255), cv2.FILLED)
    distance = depth_frame[point[1], point[0]]

    cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)
        
