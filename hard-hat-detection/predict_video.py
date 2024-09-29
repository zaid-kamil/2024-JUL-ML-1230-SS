# pip install python-dotenv opencv-contrib-python ultralytics
import cv2
from ultralytics import YOLO
import os, dotenv
dotenv.load_dotenv()
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
# Open the video file

hat_model = YOLO(r"runs\detect\train3\weights\best.pt")
video_path = r"E:\project_24\chandresh\code\data\hardhat.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    if success:
        # Run YOLOv8 inference on the frame
        results = hat_model(frame)
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        if cv2.waitKey(10) == ord('q'):
            break
cv2.destroyAllWindows()
cap.release()