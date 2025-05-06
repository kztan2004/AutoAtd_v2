# AutoAtd_v2 – Automated Attendance Taker 👀

AutoAtd_v2 is a lightweight Python tool that automatically detects and scans attendance links on the CLiC platform using computer vision and browser automation.

## ⚠️ Disclaimer
- This tool is meant to help automate attendance **only when you're present.**
- The author **does not encourage skipping class or cheating.**
- **Use at your own risk.**

## 🚀 Features
- Scans screen for attendance QR using OpenCV
- Automatically opens and submits attendance using Selenium
- Keyboard hotkey integration for force stop the services
- Simple configuration via `config.ini`

## 🛠 Requirements

- Python 3.7+
- Google Chrome or compatible browser

## 🧰 Installation

1. **Clone the repository (If you have GitBash)**
```bash
git clone https://github.com/yourusername/autoclic-attendance.git](https://github.com/kztan2004/AutoAtd_v2.git
```

2. **Install all dependencies in your terminal**:
```bash
pip install opencv-python numpy pyautogui keyboard selenium
```

3. **Chrome Driver**:<br>
Download the ChromeDriver version that matches your installed Google Chrome from:
https://developer.chrome.com/docs/chromedriver/downloads/version-selection <br>
(Make sure to include your Chrome Driver path inside the environment variables)

4. **Config.ini**:
```bash
[info]
id = your_id
password = your_password
```
(kindly reminder: Don't forget to **SAVE** the file)

5. **RUN main.py**<br>
![image](https://github.com/user-attachments/assets/aa4a051a-7e1d-4791-818f-6a0089374687)<br>
Sample output from terminal
