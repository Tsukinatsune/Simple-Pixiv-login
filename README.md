# Simple-Pixiv-login
This uses a GUI to bypass reCAPTCHA, but sometimes, if you send too many requests, reCAPTCHA is forced to appear instead of letting you pass. However, it works well when you have many servers and rotate them one by one, so it doesn’t look like spam coming from the same location.

With this thick, we can obtain the PHPSESSID directly without having to perform difficult reverse engineering.

I only tested on Window 11

Library i used
python -m pip install playwright requests
python -m playwright install chromium


what u have to change?

page.fill(email_selector, '<Email here>')

page.fill('input[placeholder="Password"]', '<Password here>')

Have fun with pixiv api!
