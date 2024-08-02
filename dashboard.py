import streamlit as st
import cv2
import numpy as np

def dashboard():
    """Display the webcam feed."""
    # Set page config to wide layout
    st.set_page_config(layout="wide")

    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam opened successfully
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return

    # Create a placeholder for the video feed
    stframe = st.empty()

    # HTML and JavaScript to handle full screen
    full_screen_script = """
    <script>
    function resizeVideo() {
        const videoElement = document.getElementById('video_feed');
        videoElement.style.width = '100%';
        videoElement.style.height = '100vh';
    }
    window.onload = resizeVideo;
    </script>
    """

    st.markdown(full_screen_script, unsafe_allow_html=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image")
            break

        # Convert the frame to RGB (Streamlit uses RGB format)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame with the specified width and height
        stframe.image(frame_rgb, channels="RGB", use_column_width=True)

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    dashboard()
