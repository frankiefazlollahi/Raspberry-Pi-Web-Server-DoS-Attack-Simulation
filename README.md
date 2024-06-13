# Raspberry-Pi-Web-Server-DoS-Attack-Simulation
This repository contains scripts and documentation for simulating and mitigating Denial of Service (DoS) attacks on an IoT device, specifically a Raspberry Pi hosting a web server. The project aims to demonstrate the vulnerabilities of IoT devices to DoS attacks and evaluate the effectiveness of countermeasures in mitigating these threats.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)

## Introduction

DoS attacks are a significant threat to IoT devices due to their limited computational resources and often insecure default configurations. This project explores the impact of HTTP flood and SYN flood attacks on a Raspberry Pi web server, and implements countermeasures such as rate limiting and SYN cookies to mitigate these attacks.

## Setup

### Requirements

- Raspberry Pi (Model 3 or higher recommended)
- Camera module compatible with Raspberry Pi
- NGINX web server
- Wireshark for network monitoring
- Python for script execution

### Installation

1. **Setting up Raspberry Pi:**
   - Install and configure NGINX as the web server.
   - Set up the camera module and configure mjpg-streamer for live video streaming.
   - Ensure proper network connectivity
   - Wireshark for monitoring network traffic

2. **Preparing Attack Environment:**
   - Install necessary dependencies on the attacker's machine (e.g., Python for scripts execution).

## Usage

1. **Executing DoS Attacks:**
   - Use Python scripts to simulate HTTP flood and SYN flood attacks from the attacker's machine.
   - Monitor the Raspberry Pi's performance using htop for resource usage and Wireshark for network traffic.

2. **Implementing Countermeasures:**
   - Enable rate limiting, SYN cookies, and TCP Connection Limit on the Raspberry Pi to mitigate the impact of DoS attacks.
   - Edit the Nginx configuration file (/etc/nginx/nginx.conf) to include rate limiting:
   - http {
     limit_req_zone $binary_remote_addr zone=one:10m rate=1r/s;
     server {
       location / {
       limit_req zone=one burst=5;
       proxy_pass http://localhost:8080;
       }
    }
  }
   - Enable SYN cookies in the Linux kernel: sudo sysctl -w net.ipv4.tcp_syncookies=1
   - TCP Connection Limits: sudo iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 10 -j REJECT
   - Repeat attacks to evaluate the effectiveness of these countermeasures.

## Future Work

In future iterations of this project, we plan to:

- Implement a Frames Per Second (FPS) display alongside the video stream to monitor performance more accurately.
- Utilize separate WiFi networks for the attacker and server to assess network isolation's impact on attack success.
- Experiment with downloadable DoS tools like LOIC, HOIC, PyLoris, and DDoSIM to compare against custom scripts used in this project.
