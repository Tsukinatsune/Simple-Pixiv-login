Hi i'm Tsukinatsune

A lightweight Python utility to bypass reCAPTCHA using **Playwright**. By automating a real browser instance, this script captures the `PHPSESSID` cookie directly, bypassing the need for complex reverse engineering of Pixiv's authentication API.

**Anti-Spam Strategy:** If you encounter persistent reCAPTCHAs, rotate through multiple proxy servers. This distributes requests across different IPs, making your traffic appear organic rather than automated.

## 🚀 Getting Started

### Prerequisites

This tool was developed and tested on **Windows 11**. You will need Python installed.

### Installation

Install the necessary automation and networking libraries:

```bash
# Install Playwright and Requests
python -m pip install playwright requests

# Install the Chromium browser engine
python -m playwright install chromium

```

---

## 🛠️ Configuration

To get the script running, you need to provide your Pixiv credentials within the automation script. Locate the following lines and update the placeholders:

1. **Email/Username:**
```python
page.fill(email_selector, 'your_email@example.com')

```


2. **Password:**
```python
page.fill('input[placeholder="Password"]', 'your_secure_password')

```



---

## 💡 How it Works

Instead of fighting Pixiv's encryption, we use a "thick client" approach:

1. **Automated Login:** Playwright opens a Chromium instance and navigates to the login page.
2. **Human Simulation:** It fills in the credentials and handles the interaction flow.
3. **Cookie Extraction:** Once logged in, the script extracts the `PHPSESSID`.
4. **API Ready:** You can now use this session ID with the `requests` library to fetch data from Pixiv's private API endpoints.

---

**Happy Coding with the Pixiv API!** 🚀
