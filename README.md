

# OpenCV Through OBS Virtual Camera

This repository demonstrates how to access the OBS virtual camera through OpenCV. Many developers face challenges accessing the OBS virtual camera to capture a specific window or video, which is not easily accessed by OpenCV directly. This guide will help resolve those issues.

## Step 1: Open the Desired Window

First, open the window you want to capture using OpenCV in real-time. For instance, if you want to access your shop camera feed via the web, open that in a separate window.

<p align="center">
  <img src="https://github.com/user-attachments/assets/67218998-b9cf-4b84-b7dc-dbeb770f53e1" width="500" alt="Shop camera window">
</p>

## Step 2: Open OBS Studio and Add Your Window

1. Launch OBS Studio.
2. Add the window you opened earlier as a source in OBS Studio.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3664591b-6235-4922-8fd3-dfe0c480bce7" width="400" alt="OBS Studio">
  <img src="https://github.com/user-attachments/assets/820c4b21-5cce-440c-8600-c9fef191ab46" width="400" alt="Add window in OBS">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/95d0a5ae-3d96-4711-98fe-4ca4d6166892" width="400" alt="OBS settings">
  <img src="https://github.com/user-attachments/assets/106750c6-c49c-4fa3-8156-f8ce9b30f30f" width="400" alt="OBS window selection">
</p>

3. Once you've selected your desired window, click **OK**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/01f87247-a69e-46ed-97d7-6454900ef206" width="400" alt="Click OK">
</p>

## Step 3: Run the App

Now, you're ready to run `app.py` and start capturing the window in OpenCV through the OBS virtual camera.

---
