import cv2

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 


def detect(gray, frame): 
	eye = eye_cascade.detectMultiScale(gray, 1.3, 5) 
	for (x, y, w, h) in eye: 
		cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 127, 255), 2) 
	return frame 


video_capture = cv2.VideoCapture(0) 
while True: 
# Captures video_capture frame by frame 
	_, frame = video_capture.read() 

	# To capture image in monochrome					 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	
	# calls the detect() function	 
	canvas = detect(gray, frame) 

	# Displays the result on camera feed					 
	cv2.imshow('Video', canvas) 

	# The control breaks once q key is pressed						 
	if cv2.waitKey(33)==27:			 
		break

# Release the capture once all the processing is done. 
video_capture.release()								 
cv2.destroyAllWindows() 