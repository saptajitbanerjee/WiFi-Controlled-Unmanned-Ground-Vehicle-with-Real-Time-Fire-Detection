# Internet Controlled Unmanned Ground Vehicle with Real Time Fire Detection

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Unmanned Ground Vehicle](#ugv)
- [Web Interface](#web-interface)
- [Block Diagram](#block-diagram)
- [System Architecture](#system-architecture)
  - [Hardware Components](#hardware-components)
  - [Software Tools](#software-tools)
  - [Raspberry Pi Setup](#raspberry-pi-setup)
  - [Robotic Car Assembly](#robotic-car-assembly)
  - [GPIO Pin Connections](#gpio-pin-connections)
  - [Live Video Feed Streaming](#live-video-feed-streaming)
  - [Environmental Monitoring](#environmental-monitoring)
  - [AWS IoT Core Integration](#aws-iot-core-integration)
  - [MQTT Communication](#mqtt-communication)
  - [Web Application Development](#web-application-development)
  - [PyTorch Integration](#pytorch-integration)
- [Conclusion](#conclusion)

## Introduction

The remotely operated unmanned ground vehicle is a complex system that combines hardware and software to enable remote control and monitoring. It utilizes a Raspberry Pi as its core controller and leverages AWS cloud services for data transmission and processing. The project integrates sensors for environmental data collection, real-time video streaming for visual feedback, and machine learning for fire detection. Additionally, it provides multiple control interfaces, including on-screen, keyboard, and voice commands.

## Project Overview

The project aims to create a versatile remotely operated unmanned ground vehicle system that integrates various technologies such as IoT, machine learning, and real-time data transmission. This system is designed to be highly adaptable and capable of performing tasks such as remote surveillance, environmental monitoring, and rapid response to critical events. It brings together a diverse set of components and software tools to achieve its objectives.

## Unmanned Ground Vehicle

![UGV](https://github.com/saptajitbanerjee/Internet-Controlled-Unmanned-Ground-Vehicle-with-Real-Time-Fire-Detection/blob/8f25b455ebbfa375e9a9c811d8d22bb41ab33587/front_view.png)
![UGV](https://github.com/saptajitbanerjee/Internet-Controlled-Unmanned-Ground-Vehicle-with-Real-Time-Fire-Detection/blob/8f25b455ebbfa375e9a9c811d8d22bb41ab33587/side_view.png)
![UGV](https://github.com/saptajitbanerjee/Internet-Controlled-Unmanned-Ground-Vehicle-with-Real-Time-Fire-Detection/blob/8f25b455ebbfa375e9a9c811d8d22bb41ab33587/top_view.png)

## Web Interface

![Web Interface](https://github.com/saptajitbanerjee/Internet-Controlled-Unmanned-Ground-Vehicle-with-Real-Time-Fire-Detection/blob/8f25b455ebbfa375e9a9c811d8d22bb41ab33587/web_page.png)

## Block Diagram
![Block Diagram](https://github.com/saptajitbanerjee/Internet-Controlled-Unmanned-Ground-Vehicle-with-Real-Time-Fire-Detection/blob/024fd1e830369256dd49567265e80378d6a92c13/block_diagram.png)

## System Architecture
![System Architecture Diagram](https://github.com/saptajitbanerjee/Internet-Controlled-Unmanned-Ground-Vehicle-with-Real-Time-Fire-Detection/blob/024fd1e830369256dd49567265e80378d6a92c13/system_architecture.png)

### Hardware Components
- **Raspberry Pi 4:** The central controller of the robotic car.
- **Logitech C270 Webcam:** Captures live video feed.
- **4WD Four Wheel Drive Kit:** The chassis for the robotic car.
- **Dual Shaft 200 RPM BO Gear Motor:** Drives the wheels.
- **L298N Motor Driver Board:** Controls motor operations.
- **BME280 Sensor Module:** Monitors environmental data.
- **10000mAh 18W Power Bank:** Powers the system.
- **9V Alkaline Battery:** Backup power source.

### Software Tools
- **Raspberry Pi Imager:** Used for OS installation.
- **PuTTy:** Establishes remote connections.
- **VNC Viewer:** Provides a graphical interface.

### Raspberry Pi Setup
- Installation of Raspbian OS.
- OS upgrade and update.
- Installation of required Python packages.
- Integration of Python libraries and Remote.It for remote access.

### Robotic Car Assembly
- Chassis assembly and component integration.
- Wiring connections and component mounting.

### GPIO Pin Connections
- Establishment of GPIO Pin connections.
- Utilization of Thonny Python Editor IDE for Python code development and testing.

### Live Video Feed Streaming
- Development of code for live video feed streaming.
- Creation of an HTTP Server on the Raspberry Pi.
- Secure transmission of live video feed via Remote.It.

### Environmental Monitoring
- Integration of BME280 sensor with Raspberry Pi.
- I2C address identification for the sensor.
- Development of code for sensor data acquisition.
- Setup of a local WiFi access point and connection to AWS IoT Core using MQTT.

### AWS IoT Core Integration
- Registration of Raspberry Pi as a single "Thing."
- Generation of device and root CA certificates for MQTT authentication.

### MQTT Communication
- Integration of Paho MQTT library.
- Development of code for publishing sensor data to AWS IoT Core.
- Secure, lightweight, and reliable data transmission over MQTT.

### Web Application Development
- Utilization of JavaScript, jQuery, Node.js, HTML, and CSS.
- WebSocket API integration for real-time data reception.
- Browserify for cross-browser compatibility.
- Flask application framework for backend.
- Integration of a machine learning model for fire detection using Torch.
- On-screen, keyboard, and voice controls for the robotic car.

### PyTorch Integration
- Loading of a fire detection Convolutional Neural Networks (CNN) model based on YOLOv5.

## Conclusion

In conclusion, this project has successfully achieved its objectives by integrating various technologies to create a highly versatile robotic car system. The project's uniqueness lies in its ability to seamlessly combine elements of IoT, machine learning, and real-time data transmission to build a system that is not only novel but also holds great promise for practical applications.

One of the project's key innovations is the use of MQTT as the primary communication protocol for transmitting sensor data and remote control commands. This choice, over traditional HTTP or other application layer protocols, offers several advantages. MQTT's lightweight nature results in minimal overhead and efficient data transmission, making it well-suited for resource-constrained devices like the Raspberry Pi. The low latency and bidirectional communication capabilities of MQTT ensure real-time interaction between the user and the robotic car, enhancing the user experience.

Furthermore, the incorporation of real-time fire detection using YoloV5 and the live video feed adds a unique dimension to the project. This feature not only makes the robotic car suitable for remote surveillance and safety applications but also showcases its potential for deployment in scenarios where rapid response to critical events is required.

In summary, this project not only delivers a highly functional robotic car system but also serves as a testament to innovation at the intersection of IoT, robotics, and machine learning. Its emphasis on efficient data transmission through MQTT, coupled with its successful integration of diverse technologies, positions it as a pioneering solution with broad applicability.
