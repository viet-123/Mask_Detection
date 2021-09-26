import cv2
from time import sleep
# creating a video object
cam = cv2.VideoCapture(0)
# named the video object
cv2.namedWindow("Camera")
# variable
img_counter = 0

while True:

    # create a frame object
    check, frame = cam.read()
    
    # show the frame
    cv2.imshow("Camera", frame)
    if not check:
        break
    
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Closing...")
        break
    
    else:
        # auto capture
        img_name = "picture_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        # when img_counter = 20 reset it to save resources 
        if(img_counter == 20): img_counter = 0
        
# shutdown the camera
cam.release()

cv2.destroyAllWindows()
