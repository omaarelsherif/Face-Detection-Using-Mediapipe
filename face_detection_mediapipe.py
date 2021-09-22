### Face detection using mediapipe ###
"""
	Description :
				   Implement face detection on an image, a video or web cam using mediapipe library on python
"""

# Importing modules
import sys
import cv2
import mediapipe as mp

# Initialize mediapipe face detector and drawer
mp_face_detection = mp.solutions.face_detection
mp_face_drawing   = mp.solutions.drawing_utils

# Detect faces on an image
def detectFromImg(image_path):
	"""Function to detect faces on an image"""

	# Using mediapipe face detector
	with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
		
		# Load the images
		img = cv2.imread(image_path)
    
		# Convert the BGR image to RGB
		img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		# Get faces on the an image (frame)
		faces = face_detection.process(img_grey)

		# Convert image back to its colors for displaying
		img_final = cv2.cvtColor(img_grey, cv2.COLOR_RGB2BGR)

		# Draw the face detection annotations on the image
		if faces.detections:
			for detection in faces.detections:
				mp_face_drawing.draw_detection(img_final, detection)
		
		# Show repeted frames (Video)
		cv2.imshow('Face Detection Mediapipe', img_final)
		cv2.waitKey(0)

# Detect faces on video or cam
def detectFromVid(video_path=None, cam=False):
	"""Function to detect faces on a video or cam"""

	# Using mediapipe face detector
	with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
     
		# Load the video or cam based on cam flag
		if cam:
			video = cv2.VideoCapture(0)
		else:
			video = cv2.VideoCapture(video_path)

		# Loop over video frames
		while True:
         
            # Get every frame on the video
			success, frame = video.read()

			# If there's no more frames, stop 
			if not success:
				break

			# Convert the BGR frame to RGB
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			# Get faces on the an image (frame)
			faces = face_detection.process(frame)

			# Convert the frame back to its colors for displaying
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
   
			# Draw the face detection annotations on the image
			if faces.detections:
				for detection in faces.detections:
					mp_face_drawing.draw_detection(frame, detection)
			
			# Show repeted images (Video)
			cv2.imshow('Face Detection Mediapipe', frame)
			if cv2.waitKey(5) & 0xFF == 27:
				break
		
    	# End 
	video.release()

# Get flag from cmd (img , vid or cam)
flag = sys.argv[1]   

# Run the function
# NOTE : sys.argv[2] is the path of image or video passed on cmd
if flag == "img":
    detectFromImg(f"{sys.argv[2]}")
elif flag == "vid":
    detectFromVid(f"{sys.argv[2]}")
else:
    detectFromVid(cam=True)
