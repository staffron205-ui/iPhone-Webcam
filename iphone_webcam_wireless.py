import cv2
import pyvirtualcam

url = "http://192.168.0.131:4747/video"  # Use your actual stream URL
cap = cv2.VideoCapture(url)

# Set desired output size (width, height)
out_width, out_height = 1920, 1080

with pyvirtualcam.Camera(width=out_width, height=out_height, fps=30) as cam:
    print(f"Virtual camera started: {out_width}x{out_height}")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Resize the frame to match the virtual cam size
        frame_resized = cv2.resize(frame, (out_width, out_height), interpolation=cv2.INTER_LINEAR)
        
        # If your stream is BGR and pyvirtualcam expects RGB, convert it:
        # frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

        cam.send(frame_resized)
        cam.sleep_until_next_frame()

        # Show the frame for debugging (optional)
        cv2.imshow('Resized Frame', frame_resized)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()