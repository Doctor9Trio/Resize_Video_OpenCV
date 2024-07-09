import cv2

def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

capture = cv2.VideoCapture("C:\\Users\\Doctor9Trio\\OneDrive\\Desktop\\Test.mp4")
frame_no = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    frame_no += 1
    print(frame_no)
    ret, frame = capture.read()
    if not ret:
        break
    new_frame = rescale_frame(frame, 0.25)
    cv2.putText(new_frame, 
                str(frame_no), 
                (50, 50), 
                font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
    
    cv2.imshow("framenew", new_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
