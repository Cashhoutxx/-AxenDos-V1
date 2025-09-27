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

🛠️ Usage

✅ Add your allowed targets to allowed_targets.txt, for example:

http://localhost:8000
http://127.0.0.1:5000


🧪 Simulation mode (Dry run):

python safe_load_tester.py --target http://localhost:8000 --count 10 --interval 0.5 --simulate


⚠️ Real test (requires --confirm flag):

python safe_load_tester.py --target http://localhost:8000 --count 100 --interval 0.1 --confirm

⚙️ Command-Line Options
Argument	Description
--target	Target URL (must be in whitelist)
--count	Number of requests
--interval	Time between requests (in seconds)
--method	HTTP method (GET or POST)
--concurrency	Max parallel threads (default: 1, max: 20)
--simulate	Enable simulation mode (no network calls)
--confirm	Required for real tests
🔐 Safety & Legal Notice

🚫 Never run tests on servers you do not own or manage.
✅ Always have written permission for any system you test.
📜 Violating Terms of Service, laws, or regulations may result in legal consequences.

This tool is designed for:

Localhost testing

Internal development/staging environments

Educational purposes

Pentest labs or CTF environments (with permission)

🧰 Recommended Alternatives

For larger scale testing:

🌐 Locust
 – scalable user load simulation

☕ Apache JMeter
 – advanced test plans

🧪 k6
 – modern performance testing for developers

🙌 Contributing

Pull requests are welcome — especially for:

Enhancements that improve safety

CI/CD improvements

Better configuration validation

📄 License

This project is licensed under the MIT License. See LICENSE for details.
