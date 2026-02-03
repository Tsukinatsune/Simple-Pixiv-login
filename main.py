from playwright.sync_api import sync_playwright
import re
import sys
import requests

PIXIV_SESSION_RE = re.compile(r"^\d+_[A-Za-z0-9]{20,}")
portalurl = "https://accounts.pixiv.net/portal"

def run():
    final_session_id = None
    
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        def check_cookie(frame):
            nonlocal final_session_id
            if frame == page.main_frame:
                all_cookies = context.cookies()
                php_session = next((c for c in all_cookies if c['name'] == 'PHPSESSID'), None)
                
                if php_session and PIXIV_SESSION_RE.match(php_session['value']):
                    final_session_id = php_session['value']
                    browser.close()

        page.on("framenavigated", check_cookie)
        
        try:
            page.goto("https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2Fen%2F&lang=en&source=pc&view_type=page")
            
            email_selector = 'input[placeholder="E-mail address or pixiv ID"]'
            page.wait_for_selector(email_selector, timeout=10000)
            page.fill(email_selector, '<Email here>')
            page.fill('input[placeholder="Password"]', '<Password here>')
            page.click('button:has-text("Log In")')
            page.wait_for_timeout(60000) 

        except Exception:
            pass

    return final_session_id

if __name__ == "__main__":
    session_id = run()
    if session_id:
        cookies = {
            "PHPSESSID": session_id
        }
        response = requests.get(portalurl ,cookies=cookies)
        rawdata = response.text
        match = re.search(r'pixivId\&quot;\:\&quot;(.*?)\&quot;', rawdata)
        if match:
            name_match = re.search(r'sessionUser\.userName\"\:\"(.*?)\"', rawdata)
            user_name = name_match.group(1) if name_match else "Not found"
            id_match = match.group(1)
            print(user_name + '|' + id_match + '|' + session_id)
        else:
            print("No match found.")
    else:
        print("Failed to capture PHPSESSID.")