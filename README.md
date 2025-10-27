🧠 Browser_Use — Automated AI Product Reviewer

An agentic AI system that autonomously browses, analyzes, and reviews trending products on Product Hunt
 — combining LLM intelligence, Playwright automation, and Text-to-Speech narration to deliver an immersive review experience.

🚀 Overview

Browser_Use is a cutting-edge AI agent that:

Uses Playwright for automated browser interaction.

Fetches and evaluates the top 2 products on Product Hunt each day.

Leverages LLM API integration to generate insightful, structured reviews.

Employs TTS (Text-to-Speech) to narrate reviews for a more dynamic presentation.

This project demonstrates agentic reasoning, autonomous browsing, and AI-driven content generation — pushing the limits of what’s possible with modern AI frameworks.

⚙️ Features

✅ Autonomous Web Browsing — Navigates Product Hunt without manual input.
✅ AI-Powered Review Generation — Uses a Large Language Model (LLM) API to summarize and critique products.
✅ Playwright Integration — Handles site interaction and data extraction reliably.
✅ Text-to-Speech Narration — Converts generated reviews into natural-sounding speech.
✅ Fully Automated Flow — From fetching to narrating, the process runs end-to-end.

🧩 Tech Stack
Component	Technology Used
Automation	Playwright

LLM Integration	OpenAI / compatible AI API
Voice Generation (TTS)	gTTS / other supported TTS module
Framework	Python 3.x
Runtime	Browser-Use framework (agent orchestration)
🧠 How It Works

Launch Agent: The AI agent boots using Browser_Use framework.

Navigate Product Hunt: Playwright opens the Product Hunt “Today” page.

Scrape Data: The top 2 products are extracted with titles, descriptions, and links.

Generate Reviews: The LLM analyzes product information and generates structured, human-like reviews.

Voice Narration: The review is spoken aloud using the TTS system.

Output: Both text and audio outputs are saved or displayed.

🛠️ Setup & Installation
Prerequisites

Python 3.10 or later

Node.js (for Playwright)

API key for your chosen LLM provider (e.g., OpenAI)

Steps
# Clone this repository
git clone https://github.com/itsDurvank/Browser_Use.git
cd Browser_Use

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys and configuration in .env

# Run Playwright setup
playwright install

# Launch the AI Reviewer
python main.py

🎧 Example Output

Text Review:
“Product X is a minimalist productivity app that streamlines task management using intuitive gesture controls…”

Audio Output:
The same review narrated in a realistic voice using TTS.

🧭 Vision

Browser_Use isn’t just an automation project — it’s a demonstration of next-gen agentic AI capable of autonomous reasoning, decision-making, and multimedia generation.
This project aims to showcase how AI + Automation + Voice can redefine digital content creation and evaluation.

🧑‍💻 Author

Durvank Kavhale
AI/ML Developer | Agentic AI Enthusiast
GitHub
