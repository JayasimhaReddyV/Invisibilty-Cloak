# Invisibilty-Cloak

The Invisibility Cloak project is a computer vision-based application that allows users to make objects disappear in real time using color detection and background substitution. Inspired by the invisibility cloak concept from Harry Potter, this project utilizes OpenCV to create a seamless illusion of invisibility.

Features
- Real-Time Cloak Effect – Makes a selected color (e.g., red) disappear by replacing it with the background.
- Background Capture – Captures a static background frame before applying the invisibility effect.
- Color Detection – Detects and masks the chosen cloak color for replacement.
- Smooth Transition – Uses morphological operations to enhance the invisibility effect.

Technologies Used
- Python
- OpenCV (for image processing)
- NumPy

How It Works
- The application captures the background frame before the user appears with the cloak.
- It detects a predefined cloak color (e.g., red) using color segmentation.
- The detected region is replaced with the previously captured background.
- The processed frame is displayed in real time, creating the invisibility effect.
