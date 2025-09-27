📌 Overview

SafeLoadTester is a lightweight Python tool designed for safe and ethical HTTP load testing. It is intentionally built with security features to prevent abuse, such as:

✅ Target whitelisting
✅ Simulation mode (no real network requests)
✅ Rate limiting and concurrency caps
❌ No proxy/anonymization support
✅ Required confirmation before real execution

🚀 Features

🔁 Simulates GET/POST requests to a whitelisted target

🧪 Simulation mode: runs test logic without sending actual requests

📋 Whitelist system to limit allowed targets

🧵 Configurable concurrency (with limits)

🧯 Built-in safety measures to avoid abuse

📦 Installation
git clone https://github.com/yourname/safeloadtester.git
cd safeloadtester
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt


<img width="763" height="339" alt="Capture" src="https://github.com/user-attachments/assets/eff6536f-b84b-4dfb-9f52-6ba52b474691" />
