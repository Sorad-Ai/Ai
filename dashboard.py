import streamlit as st
import cv2
import numpy as np

def dashboard():
    """Display the webcam feed."""
    # st.title("Webcam Feed")

    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam opened successfully
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return

    # Create a placeholder for the video feed
    stframe = st.empty()

    # Set the desired width for the video output
    video_width = 1280  # Width in pixels

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image")
            break

        # Convert the frame to RGB (Streamlit uses RGB format)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame with the specified width
        stframe.image(frame_rgb, channels="RGB", use_column_width=False, width=video_width)

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    dashboard()
