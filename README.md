
<!-- PROJECT TITLE -->
<h1 align="center">Face Detection Using Mediapipe</h1>

<!-- PROJECT DESCRIPTION -->
## ➲ Project description
Implement face detection on an image, a video or web cam using mediapipe library on python

<!-- PREREQUISTIES -->
## ➲ Prerequisites
This is list of required packages and modules for the project to be installed :
* Python 3.x

  <https://www.python.org/downloads>
  
* OpenCV 
  ```sh
  pip install opencv-python
  ```
* Mediapipe 
  ```sh
  pip install mediapipe
  ```

<!-- INSTALLATION -->
## ➲ Installation
1. Clone the repo
   ```sh
   git clone https://github.com/omaarelsherif/Face-Detection-Using-Mediapipe.git
   ```
2. Run the code from cmd
   ```sh
   python face_detection_mediapipe.py "FLAG" "IMAGE_PATH"/"VIDEO_PATH"
   ```
   For Image:
   ```sh
   python face_detection_mediapipe.py img Images/img1.jpg
   ```
   For Video:
   ```sh
   python face_detection_mediapipe.py vid Videos/video.mp4
   ```
   For Cam:
   ```sh
   python face_detection_mediapipe.py cam
   ```

<!-- OUTPUT -->
## ➲ Output
Here's the project output where the input is an image containing single or multi faces or a video and the output will be the same image with bounding boxs around all faces or a video with bounding box on faces in every frame as follows:

<h3>Face Detection Image Output - Single face</h3>

![alt text for screen readers](/Outputs/output1.png "Face Detection Image Output - Single face")

<h3>Face Detection Image Output - Multi faces</h3>

![alt text for screen readers](/Outputs/output2.png "Face Detection Image Output - multi face")

<h3>Face Detection Video Output</h3>

![alt text for screen readers](/Outputs/output3.gif "Face Detection Video Output")

<!-- REFERENCES -->
## ➲ References
These links may help you to better understanding of the project idea and techniques used :
1. Mediapipe : https://bit.ly/3AlHJ6f
   
<!-- CONTACT -->
## ➲ Contact
- E-mail :  [omaarelsherif@gmail.com](mailto:omaarelsherif@gmail.com)
- Facebook : https://www.facebook.com/omaarelshereif
