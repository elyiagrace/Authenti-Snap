# Welcome to Hack Midwest 2024!
## Getting Started
Ensure you have reviewed the [Rules & FAQ](https://hackmidwest.com/#faq)
- ✅  Clone this repository and rename to the name of your app or idea
- 🚫   Make it **private** - Unable to change the privacy of a fork
- ✅  Add pr@kcitp.com as a user
- ✅ Populate the Team, App & Challenges info below and update as needed
<br /><br />
---
**Made by**: Ellia Morse || ellia@ku.edu || elyiagrace  
---

# Authenti-Snap 🔒💻  
Imagine capturing a screenshot, instantly proving the website it came from, and locking it down as verifiable proof—no hassle, no fuss. That’s exactly what **Authenti-Snap** does! Think of it as a notary for your screenshots. It securely captures the screenshot, date-time stamp, and website metadata, storing everything using the InterPlanetary File System (IPFS) for seamless integration with blockchain tech. It’s secure, accurate, and tamper-proof. Whether you’re sharing paystubs with your bank 🏦, preparing for a tech-risk audit 📊, maintaining compliance records 📑, or protecting intellectual property 💡, **Authenti-Snap** is the ultimate web3 solution for digital proof.

## What challenges are you building for?
*See hackmidwest.com/#prizes for challenge details*
- ✅  Pinata Challenge
- [ ]  Pinata AI Challenge
- ✅  Pinata Enterprise Challenge
- [ ]  AWS Bedrock Challenge
- [ ]  Red Hat | Intel AI Challenge
- [ ]  Zoom Challenge
- [ ]  USDA Challenge
- [ ]  brAIn Rot Challenge
<br /><br />

---
#Instructions - Tested on Windows <br /><br />
1. Confirm Python3 is installed<br /><br />
2. Create a virtual enviroment using: python -m venv testEnv<br /><br />
3. On the same level as your test enviroment: testEnv\Scripts\activate<br /><br />
4. Now that you are in your virtual enviroment: pip install -r requirements.txt<br /><br />
5. Now within Command Prompt: "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_debug"<br /><br />
6. Now go to Pinata and get your API key and Secret key. You'll want to replace the dummy text in screenshot_processor.py<br /><br />
7. From here, run main_app.py!!<br /><br />
8. Select "snip" then drag your mouse over your Chrome window to select your area for screenshot<br /><br />
9. This will automatically capture, hash, and appear in IPFS!<br /><br />
10. (Optional) Give yourself a pat on the back, you deserve it!
<br /><br />

Notes: 
We launch a chrome debug menu because we want to enable external tools (Selenium) to interact with Chrome’s internal APIs. This is done for tasks such as inspecting, automating, or controlling web pages, which would normally require manual interaction through Chrome’s Developer Tools. In our case, we use this to read the URL


