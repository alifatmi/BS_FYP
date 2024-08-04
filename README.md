# Drowsiness Detection and Focus Control System

![flow_diagram](https://github.com/user-attachments/assets/5518f5af-d759-46ea-a51e-cb7ca3195fd0)

## Overview

In today's fast-paced world, the increase in the number of vehicles on the road has led to a rise in transportation-related accidents. One significant factor contributing to these accidents is **Driver Drowsiness**. This project, **Drowsiness Detection and Focus Control System**, aims to mitigate this risk by detecting drowsiness and lack of focus in drivers through eye blinking and head movement monitoring.

The system uses a camera to capture real-time video frames, analyzing them to identify abnormal eye behavior or head movements. If the driver is found to have closed eyes or lost focus for a certain period, the system triggers an alarm to alert the driver, ensuring safety and reducing the chances of accidents.

## Features

- **Real-time Eye Blink Detection:** Continuously monitors eye blinking patterns to detect signs of drowsiness.
- **Head Movement Tracking:** Tracks head orientation to identify if the driver is losing focus or falling asleep.
- **Alarm System:** Alerts the driver immediately when drowsiness or loss of focus is detected.
- **Cost-Effective Solution:** Designed to be accessible and affordable, ensuring wide applicability in various vehicles.
- **User-Friendly Interface:** Simple setup and operation, requiring minimal technical knowledge.

## Goals and Objectives

- **Save Lives:** Reduce the risk of accidents caused by driver drowsiness.
- **Increase Awareness:** Keep drivers alert and aware of their surroundings.
- **Prevent Sleep State:** Actively monitor and prevent drivers from falling asleep.
- **Affordable Solution:** Provide a cost-effective tool for enhancing road safety.

## Usage

1. **Setup the Camera:**  
   Connect a compatible camera to your computer or device.

2. **Start the System:**  
   Run the application using the command mentioned above.

3. **Monitor the Driver:**  
   The system will begin monitoring the driver's eye blinking and head movements in real time.

4. **Receive Alerts:**  
   If the system detects drowsiness or loss of focus, an alarm will sound to alert the driver.

## Technical Details

### Face Landmark Model

For detecting face landmarks, the project utilizes transfer learning and a custom-trained neural network. This network is designed to predict 3D landmark coordinates on synthetic data while accurately detecting 2D semantic contours on real-world data.

The model provides robust predictions of facial landmarks, ensuring precise tracking of eye blinking and head movements.

## Implementation Steps

1. **Data Collection:**  
   Capture video frames from the camera and preprocess them for analysis.

2. **Face Detection:**  
   Use the face landmark model to identify key points on the driver's face.

3. **Blink Detection:**  
   Analyze the eye region to detect blink frequency and duration.

4. **Head Pose Estimation:**  
   Calculate head orientation angles to determine focus levels.

5. **Alert Mechanism:**  
   Trigger an alarm if drowsiness or lack of focus is detected beyond the threshold.


## Installation

To get started with the Drowsiness Detection and Focus Control System, follow these steps:

### Clone the Repository

```
git clone https://github.com/yourusername/drowsiness-detection.git
cd BS_FYP
 ```

### Prerequisites

You need to install required libaries.

#### Installation

To install the required libraries for this project, run the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt

```
## Run the Application

To start the application, use the following command in your terminal or command prompt:

```bash
python main.py
```



