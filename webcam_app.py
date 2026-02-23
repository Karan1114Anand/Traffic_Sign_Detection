"""
Real-time Traffic Sign Detection Web Application
Uses YOLOv8 model for webcam-based detection
"""
from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
import cv2
from ultralytics import YOLO
import numpy as np
import threading

app = Flask(__name__)
CORS(app)

# Load the trained model
MODEL_PATH = r'D:\GuruJI\YOLO\train4\weights\best.pt'
model = YOLO(MODEL_PATH)

# Global variables
camera = None
camera_lock = threading.Lock()
latest_frame = None
latest_detected_frame = None
frame_lock = threading.Lock()
camera_running = True  # Track camera state
capture_thread_obj = None

def get_camera():
    """Initialize and return camera object"""
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow for Windows
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 480)  # Reduced from 640
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)  # Reduced from 480
        camera.set(cv2.CAP_PROP_FPS, 30)
        camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Minimize buffer
    return camera

def capture_frames():
    """Continuously capture frames from camera"""
    global latest_frame, latest_detected_frame, camera_running
    
    cam = get_camera()
    frame_skip = 0  # Skip frames for better performance
    
    while camera_running:
        if not camera_running:
            break
            
        with camera_lock:
            success, frame = cam.read()
        
        if not success:
            continue
        
        # Store original frame
        with frame_lock:
            latest_frame = frame.copy()
        
        # Run detection every other frame to reduce lag
        frame_skip += 1
        if frame_skip % 2 == 0:  # Process every 2nd frame
            try:
                results = model(frame, conf=0.5, verbose=False, imgsz=480)  # Reduced image size
                detected_frame = results[0].plot()
                
                with frame_lock:
                    latest_detected_frame = detected_frame
            except Exception as e:
                print(f"Detection error: {e}")
                with frame_lock:
                    latest_detected_frame = frame.copy()
        
        # Small delay to prevent CPU overload
        cv2.waitKey(1)

# Start frame capture thread
capture_thread_obj = threading.Thread(target=capture_frames, daemon=True)
capture_thread_obj.start()

def generate_frames_original():
    """Generate original camera frames"""
    while True:
        with frame_lock:
            if latest_frame is None:
                continue
            frame = latest_frame.copy()
        
        # Encode frame to JPEG with lower quality for speed
        ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
        if not ret:
            continue
            
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def generate_frames_detected():
    """Generate frames with detection overlay"""
    while True:
        with frame_lock:
            if latest_detected_frame is None:
                continue
            frame = latest_detected_frame.copy()
        
        # Encode frame to JPEG with lower quality for speed
        ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
        if not ret:
            continue
            
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('webcam.html')

@app.route('/video_feed_original')
def video_feed_original():
    """Original video streaming route"""
    return Response(generate_frames_original(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_detected')
def video_feed_detected():
    """Detected video streaming route"""
    return Response(generate_frames_detected(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_camera')
def stop_camera():
    """Stop the camera"""
    global camera, camera_running
    camera_running = False
    if camera is not None:
        camera.release()
        camera = None
    return jsonify({'status': 'stopped'})

@app.route('/start_camera')
def start_camera():
    """Start the camera"""
    global camera, camera_running, capture_thread_obj
    camera_running = True
    
    # Restart capture thread if needed
    if capture_thread_obj is None or not capture_thread_obj.is_alive():
        capture_thread_obj = threading.Thread(target=capture_frames, daemon=True)
        capture_thread_obj.start()
    
    return jsonify({'status': 'started'})

@app.route('/camera_status')
def camera_status():
    """Get camera status"""
    return jsonify({'running': camera_running})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Traffic Sign Detection - Webcam Application")
    print("="*60)
    print(f"Model loaded from: {MODEL_PATH}")
    print("Server starting at: http://localhost:5001")
    print("="*60 + "\n")
    
    try:
        app.run(host='localhost', port=5001, debug=False, threaded=True)
    finally:
        if camera is not None:
            camera.release()
