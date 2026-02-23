"""
Setup script for Traffic Sign Detection System
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="traffic-sign-detection",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Real-time traffic sign detection using YOLOv8 and Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/traffic-sign-detection",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.13",
    install_requires=[
        "Flask>=3.0.0",
        "flask-cors>=4.0.0",
        "opencv-python>=4.12.0",
        "ultralytics>=8.3.0",
        "Pillow>=11.0.0",
        "numpy>=2.2.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "traffic-sign-detection=webcam_app:main",
        ],
    },
)
