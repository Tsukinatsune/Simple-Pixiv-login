Refresh token gist
https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362

<img src="https://c.tenor.com/qMyieAqYK8MAAAAd/tenor.gif" alt="Dancing chen" width="200" height="200">

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

สำหรับ Bypass reCAPTCHA บน Pixiv วิธีการใช้ **Playwright** เพื่อดึง `PHPSESSID` เป็นแนวทางลดความปวดหัวจากการไปไล่แก้ Reverse Engineering ตัว API โดยตรง และทำให้ระบบมองว่าเราเป็น User จริงๆ ที่ใช้งานผ่าน Browser ครับ
นี่คือคำแนะนำภาษาไทย

---

## 🚀 เริ่มต้นใช้งาน (Getting Started)

### สิ่งที่ต้องเตรียม (Prerequisites)

เครื่องมือนี้พัฒนาและทดสอบบน **Windows 11** จำเป็นต้องติดตั้ง Python ไว้ในเครื่องให้เรียบร้อย

### การติดตั้ง (Installation)

ติดตั้ง Library ที่จำเป็นสำหรับการจำลอง Browser และการจัดการ Network:

```bash
# ติดตั้ง Playwright และ Requests
python -m pip install playwright requests

# ติดตั้ง Chromium browser engine
python -m playwright install chromium

```

---

## 🛠️ การตั้งค่า (Configuration)

เพื่อให้สคริปต์ทำงานได้ ต้องระบุข้อมูลบัญชี Pixiv ลงในสคริปต์ โดยแก้ไขในส่วนของ Placeholder ดังนี้:

1. **Email/Username:**

```python
page.fill(email_selector, 'your_email@example.com')

```

2. **Password:**

```python
page.fill('input[placeholder="Password"]', 'your_secure_password')

```

---

## 💡 หลักการทำงาน (How it Works)

แทนที่จะพยายามถอดรหัส Encryption ของ Pixiv เราใช้แนวทางแบบ "Thick Client" แทน:

1. **Automated Login:** Playwright จะเปิดหน้าต่าง Chromium และนำทางไปยังหน้า Login
2. **Human Simulation:** ระบบจะกรอกข้อมูลและเลียนแบบพฤติกรรมการใช้งานของมนุษย์
3. **Cookie Extraction:** เมื่อ Login สำเร็จ สคริปต์จะดึงค่า `PHPSESSID` ออกมา
4. **API Ready:** นำ Session ID นี้ไปใช้ร่วมกับ Library `requests` เพื่อดึงข้อมูลจาก Private API ของ Pixiv ได้ทันที

---

**ขอให้สนุกใช้งาน Pixiv API!** 🚀


