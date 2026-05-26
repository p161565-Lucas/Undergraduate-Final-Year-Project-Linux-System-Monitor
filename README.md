## Undergraduate Final Year Project: Linux System Monitor

A real-time Linux system monitoring and remote control application built with Python and PyQt.


---
## 📌 Project Overview

With the rapid development of information technology, the Linux operating system has been widely used in various fields. Therefore, monitoring and managing Linux systems has become particularly important. This project focuses onLinux system performance monitoring and implementation, with the main objectives of achieving real-time remote monitoring of multiple system metrics, visualizing and storing monitoring data, and remotely controlling Linux system processes.

This project adopts modular design methodology. The entire development process is demonstrated through detailed module flowcharts and implementation procedures. Multiple core technologies are applied in this system, including PyQt graphical interface development, SSH remote connection protocol, Linux shell monitoring scripts, PyChart dynamic data visualization, SQL Server remote database interaction, and regular expression-based data filtering and extraction.

The final system realizes remote connection between Windows PyCharm and Ubuntu Linux, real-time collection and visual display of system operating data, dynamic curve chart rendering, user password storage and modification based on SQL Server, and automatic extraction and analysis of massive system log data, completing a comprehensive visualized Linux system monitoring and remote management platform.


---
## ✨ Key Features

- Complete login authentication system: user registration, login verification and password modification based on SQL Server database

- Real-time Linux system monitoring: collect CPU, memory and other system operating indicators

- Dynamic data visualization: display system status through real-time updating line charts

- Remote Linux process control: support remote viewing and closing system processes

- System log analysis: use regular expressions to screen valid data and identify potential system abnormal errors

- Manual monitoring + intelligent judgment: combined artificial observation and preliminary model training for system anomaly detection


---
## 🛠️ Tech Stack

- Programming Language: Python

- GUI Framework: PyQt

- Database: SQL Server

- Remote Communication: SSH protocol

- Data Visualization: PyChart

- System Operation: Linux Shell Script

- Data Processing: Regular Expression


---
## 📁 File Description

- run.py: Main program entry file to launch the entire application

- main.py: Test Linux remote connection and obtain system command return data fields

- homepage.py: Responsible for the main monitoring interface display and function realization


---
## 🚀 Environment Deployment & Configuration Guide

1. Install SSH Service on Ubuntu (VMware Virtual Machine)

Execute the following commands in the Ubuntu terminal:

sudo apt-get update
sudo apt-get install openssh-client
sudo apt-get install openssh-server
sudo service ssh start

Verify whether SSH is installed successfully:

sudo ps -e | grep ssh

2. Configure SSH Password-Free Login

Step 1: Generate SSH key pair on Windows terminal

ssh-keygen -t rsa

Step 2: Transfer the public key to the Ubuntu server

ssh-copy-id zhang@192.168.154.128

Manual permission configuration (if needed):

chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa.pub

Step 3: Test remote connection

ssh zhang@192.168.154.128

3. Create System Monitoring Shell Script

Create and edit the monitoring script in Ubuntu terminal:

nano top_script.sh

Write the following content and save:

top -b -n 1

4. Modify IP Configuration

Check the local IP address of Ubuntu:

ifconfig

Update the IP address parameter in the homepage.py file to complete remote connection matching.


---
## 🎯 Project Summary

This undergraduate graduation project completes the design and implementation of a full-stack Linux system monitoring platform. It integrates GUI interface development, database data storage, remote server connection, real-time data visualization and system abnormal log recognition, realizing automatic monitoring, visual analysis and remote management of Linux system operating status. The project has complete functions, standardized code structure and strong practical application value.
