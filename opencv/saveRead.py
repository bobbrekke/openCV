import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# uncomment to capture from nanoCam
#cam= cv2.VideoCapture(camSet)

# read video from file, not nanoCam
cam= cv2.VideoCapture('videos/myCam.avi')

# create file object to write video frames with format and frame rate
#outVid=cv2.VideoWriter('videos/myCam.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH))


#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    #qoutVid.write(frame)


#increase wait to get the playback frame rate natural
    if cv2.waitKey(50q)==ord('q'):
        break

cam.release()
outVid.release()  
cv2.destroyAllWindows()