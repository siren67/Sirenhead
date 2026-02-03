 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..78c70cf7306b20fea35cfe60e2db5e0ec2d9554b
--- /dev/null
+++ b/README.md
@@ -0,0 +1,50 @@
+# Google-Backed Chatbot (Minimal)
+
+This repository contains a minimal Python chatbot that answers questions by querying the Google Custom Search JSON API.
+
+## Beginner-friendly overview
+
+Think of this chatbot as a small program that:
+
+1. Takes your question (for example: "What is the tallest mountain?").
+2. Asks Google for search results (via the official API).
+3. Reads the short snippets that Google returns.
+4. Combines those snippets into a short reply.
+
+Because it uses Google's official API, you need:
+
+- A **Google API key** (proves who is calling the API).
+- A **Custom Search Engine (CSE) ID** (tells Google what search engine to use).
+
+## Setup
+
+1. Create a Google Custom Search Engine (CSE) and API key.
+2. Export the following environment variables:
+
+```bash
+export GOOGLE_API_KEY="your_api_key"
+export GOOGLE_CSE_ID="your_cse_id"
+```
+
+3. Install dependencies (this installs the `requests` library used to talk to Google):
+
+```bash
+python -m venv .venv
+source .venv/bin/activate
+pip install -r requirements.txt
+```
+
+## Run
+
+```bash
+python chatbot.py
+```
+
+Type your question at the prompt and the bot will return a short answer based on the top Google result snippets.
+
+## Example
+
+```
+You: What is the tallest mountain?
+Bot: Mount Everest is the tallest mountain on Earth, with an elevation of about 8,848 meters (29,029 feet) above sea level...
+```
 
EOF
)
