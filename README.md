# RPA Test Application

A simple Flask web application designed for testing RPA (Robotic Process Automation) workflows. This application provides common web interface elements that can be used to test automated processes, including login functionality, navigation, data display, and file downloads.

## Purpose

This application serves as a test environment for RPA automation workflows, providing:
- Login page with authentication
- Multiple pages with navigation
- User profile management
- Data reporting with export functionality

## Prerequisites

- Python 3.7 or higher
- pip package manager

## Setup Instructions

### 1. Clone or Download the Application

Download the application files to your local machine.

### 2. Create a Python Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### 5. Access the Application

Open your web browser and navigate to `http://localhost:5000`

**Login Credentials:**
- Username: `Admin`
- Password: `Admin123`

## Stopping the Application

To stop the application:
1. Press `Ctrl+C` in the terminal where the app is running
2. Deactivate the virtual environment: `deactivate`
