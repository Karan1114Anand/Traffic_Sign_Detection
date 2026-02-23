# 🚦 Traffic Sign Detection System

Real-time traffic sign detection web application powered by YOLOv8 and Flask.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

- **Real-time Detection**: Live webcam feed with instant traffic sign recognition
- **Dual View**: Side-by-side comparison of camera input and AI detection output
- **YOLOv8 Powered**: State-of-the-art object detection model
- **Modern UI**: Dark theme with Tailwind CSS and Material Icons
- **Performance Optimized**: Low latency streaming with frame skipping
- **Interactive Controls**: Start/Stop camera without page reload
- **Live Metrics**: Real-time FPS, inference time, and recording duration

## 📋 Requirements

- Python 3.13+
- Webcam
- Windows OS (optimized for DirectShow)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Karan1114Anand/Traffic_Sign_Detection.git
cd Traffic_Sign_Detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download YOLOv8 Model

Place your trained YOLOv8 model at:
```
train4/weights/best.pt
```

Or download a pretrained model:
```bash
# The app will automatically download yolov8n.pt if no custom model is found
```

### 4. Run the Application

```bash
python webcam_app.py
```

### 5. Open in Browser

Navigate to: `http://localhost:5001`

## 📁 Project Structure

```
traffic-sign-detection/
├── webcam_app.py           # Flask backend server
├── templates/
│   └── webcam.html         # Frontend UI
├── static/                 # Static assets (if any)
├── train4/
│   └── weights/
│       └── best.pt         # Trained YOLOv8 model
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🎯 Usage

1. **Start Camera**: Click the green "START CAMERA" button
2. **View Detection**: See real-time traffic sign detection with bounding boxes
3. **Monitor Performance**: Check FPS and inference time in the top-right
4. **Stop Camera**: Click the red "STOP CAMERA" button to pause
5. **Refresh Feed**: Use "REFRESH FEED" button if stream freezes

## 🛠️ Configuration

### Camera Settings

Edit `webcam_app.py` to adjust camera parameters:

```python
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 480)   # Resolution width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)  # Resolution height
camera.set(cv2.CAP_PROP_FPS, 30)            # Frame rate
```

### Detection Settings

Adjust detection confidence and model size:

```python
results = model(frame, conf=0.5, imgsz=480)  # conf: confidence threshold
```

### Performance Tuning

- **Reduce lag**: Lower resolution or increase frame skip
- **Better quality**: Increase JPEG quality in `cv2.imencode()`
- **Faster inference**: Use smaller YOLOv8 model (yolov8n vs yolov8s)

## 📊 Model Training

To train your own traffic sign detection model:

1. Prepare dataset in YOLO format
2. Create `data.yaml` configuration
3. Train using:

```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data='data.yaml', epochs=30, imgsz=640)
```

4. Copy trained model to `train4/weights/best.pt`

## 🎨 UI Customization

The UI uses Tailwind CSS. Customize colors in `templates/webcam.html`:

```javascript
colors: {
    "primary": "#0df246",           // Green accent
    "background-dark": "#102214",   // Dark background
}
```

## 🐛 Troubleshooting

### Camera Not Working
- Check camera permissions in browser
- Ensure no other application is using the camera
- Try different camera index: `cv2.VideoCapture(1)`

### Lag Issues
- Reduce resolution in camera settings
- Increase frame skip rate
- Lower JPEG quality
- Use smaller YOLOv8 model

### Model Not Found
- Verify model path: `train4/weights/best.pt`
- Check model file is not corrupted
- Ensure model is YOLOv8 format (.pt file)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Karan Anand [LinkedIn](https://www.linkedin.com/in/karan24anand?utm_source=share_via&utm_content=profile&utm_medium=member_android)

Project Link: https://github.com/Karan1114Anand/Traffic_Sign_Detection.git

## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Flask](https://flask.palletsprojects.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Material Icons](https://fonts.google.com/icons)
- [Traffic Signs Detection using YOLOv8 - Kaggle Notebook](https://www.kaggle.com/code/pkdarabi/traffic-signs-detection-using-yolov8/notebook) by pkdarabi

---

Made with ❤️ for safer roads
