# Installation Guide

## Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- Webcam
- Git

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/traffic-sign-detection.git
cd traffic-sign-detection
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (Web framework)
- OpenCV (Computer vision)
- Ultralytics (YOLOv8)
- NumPy, Pillow (Image processing)

### 4. Download or Train Model

**Option A: Use Pretrained Model**

The app will automatically download `yolov8n.pt` on first run.

**Option B: Use Custom Trained Model**

1. Train your model using the provided notebook or script
2. Place the trained model at: `train4/weights/best.pt`

### 5. Run the Application

```bash
python webcam_app.py
```

You should see:
```
============================================================
Traffic Sign Detection - Webcam Application
============================================================
Model loaded from: train4/weights/best.pt
Server starting at: http://localhost:5001
============================================================
```

### 6. Access the Web Interface

Open your browser and navigate to:
```
http://localhost:5001
```

## Troubleshooting

### Issue: Module Not Found

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Issue: Camera Not Detected

**Solution:**
- Check camera permissions in your OS
- Try different camera index in `webcam_app.py`:
  ```python
  camera = cv2.VideoCapture(1)  # Try 0, 1, 2, etc.
  ```

### Issue: Port Already in Use

**Solution:**
Change the port in `webcam_app.py`:
```python
app.run(host='localhost', port=5002, debug=False, threaded=True)
```

### Issue: Slow Performance

**Solutions:**
1. Reduce resolution in `webcam_app.py`
2. Use smaller YOLOv8 model (yolov8n instead of yolov8s)
3. Increase frame skip rate
4. Close other applications

## Windows-Specific Setup

### Enable Long Paths (if needed)

1. Press `Win + R`, type `gpedit.msc`
2. Navigate to: Computer Configuration > Administrative Templates > System > Filesystem
3. Enable "Enable Win32 long paths"
4. Restart terminal

### Install Visual C++ Redistributable

Some dependencies may require Visual C++ Redistributable:
- Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe

## Verification

Test your installation:

```bash
python -c "import cv2, flask, ultralytics; print('All dependencies installed successfully!')"
```

## Next Steps

- Read [README.md](README.md) for usage instructions
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Train your own model using the provided notebook

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [GitHub Issues](https://github.com/yourusername/traffic-sign-detection/issues)
3. Create a new issue with details

Happy detecting! 🚦
