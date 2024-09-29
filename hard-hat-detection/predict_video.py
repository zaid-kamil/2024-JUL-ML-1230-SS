import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# pip install opencv-contrib-python
# pip install ultralytics
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO(r'hard-hat-detection\runs\detect\train3\weights\best.pt')

# Open the video file
cap = cv2.VideoCapture(r"E:\project_24\chandresh\code\data\hardhat.mp4")
# video length
current_frame = 0
# 
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    current_frame += 1
    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        # Display the progress bar
        cv2.rectangle(annotated_frame, (0, height-5), (int(width * current_frame / length), height), (0, 200, 255), -1)
        # % of video completed
        per_remaining = round((current_frame / length) * 100, 2)
        # Display the progress percentage
        cv2.putText(annotated_frame, f"{per_remaining}%", (10, height-10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)


        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()