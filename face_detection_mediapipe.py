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
face_detector = mp.solutions.face_detection
face_drawer   = mp.solutions.drawing_utils

# Detect faces on an image
def detectFromImg(image_path):
	"""Function to detect faces on an image"""
 
	# Load the images
	image = cv2.imread(image_path)

	# Using mediapipe face detector
	with face_detector.FaceDetection(min_detection_confidence=0.5) as face_detection:
    
		# Convert the BGR image to RGB
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image.flags.writeable = False

		# Get faces on the an image (frame)
		faces = face_detection.process(image)

		# Draw the face detection annotations on the image
		image.flags.writeable = True
		image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
		if faces.detections:
			for detection in faces.detections:
				face_drawer.draw_detection(image, detection)
		
		# Show repeted images (Video)
		cv2.imshow('Face Detection', image)
		cv2.waitKey(0)

# Detect faces on video
def detectFromVid(video_path):
	"""Function to detect faces on a video"""

	# Load the video
	video = cv2.VideoCapture(video_path)

	# Using mediapipe face detector
	with face_detector.FaceDetection(min_detection_confidence=0.5) as face_detection:

		# Loop over video frames
	    while True:
         
            # Get every frame on the video
	        success, image = video.read()
	
		    # If there's no more frames, stop 
	        if not success:
		        break
    
	        # Convert the BGR image to RGB
	        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	        image.flags.writeable = False

	        # Get faces on the an image (frame)
	        faces = face_detection.process(image)

	        # Draw the face detection annotations on the image
	        image.flags.writeable = True
	        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
	        if faces.detections:
	          for detection in faces.detections:
	            face_drawer.draw_detection(image, detection)
		  
		    # Show repeted images (Video)
	        cv2.imshow('Face Detection', image)
	        if cv2.waitKey(5) & 0xFF == 27:
	          break
     
    # End 
	video.release()
 
# Detect faces on a cam
def detectFromCam():
	"""Function to detect faces on a web cam"""

	# Load the video
	cam = cv2.VideoCapture(0)

	# Using mediapipe face detector
	with face_detector.FaceDetection(min_detection_confidence=0.5) as face_detection:

		# Loop over video frames
	    while True:
         
            # Get every frame from the cam
	        success, image = cam.read()
	
		    # If there's no frmae exist on the cam 
	        if not success:
		        break
    
	        # Convert the BGR image to RGB
	        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	        image.flags.writeable = False

	        # Get faces on the an image (frame)
	        faces = face_detection.process(image)

	        # Draw the face detection annotations on the image
	        image.flags.writeable = True
	        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
	        if faces.detections:
	          for detection in faces.detections:
	            face_drawer.draw_detection(image, detection)
		  
		    # Show repeted images (Video)
	        cv2.imshow('Face Detection', image)
	        if cv2.waitKey(5) & 0xFF == 27:
	          break
     
    # End 
	cam.release()

# Get flag from cmd (img , vid or cam)
flag = sys.argv[1]   

# Run the function
# NOTE : sys.argv[2] is the path of image or video passed on cmd
if flag == "img":
    detectFromImg(f"{sys.argv[2]}")
elif flag == "vid":
    detectFromVid(f"{sys.argv[2]}")
else:
    detectFromCam()
