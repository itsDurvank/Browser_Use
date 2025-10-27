"""
this modules has 4 tasks:
1. Gets the intro agent to navigate to Product Hunt
2. Gets the top products agent to extract the first two products
3. Gets the UI review agent to provide a casual comment about the UI
4. Gets the navbar agent to extract the navbar elements"""

from browser_use import Agent, Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from models import Posts, Details
import os

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))
controller1 = Controller(output_model=Posts)
controller2 = Controller(output_model=Details)

def get_intro_agent(session):
    return Agent(
        task="Navigate to https://producthunt.com",
        llm=llm,
        browser_session=session
    )

def get_top_products_agent(session):
    return Agent(
        task="""
From the current Product Hunt homepage, perform the following steps:
1. Click on the first product listed.
2. Extract:
   - The product name
   - The URL behind the "Visit Website" button.

3. Then, go back and repeat the same steps for the second product.
4. Return the final result in the following JSON format:
[
{
                "product_name": "Product A",
                "visit_website_url": "https://..."
            },
            {
                "product_name": "Product B",
                "visit_website_url": "https://..."
            }
            ]
""",
        llm=llm,
        browser_session=session,
        controller=controller1
    )

def get_ui_review_agent(session, url):
    return Agent(
        task="From the current website, which is {url}, give me a quick casual comment about the UI" + UI_REVIEW_PROMPT,
        llm=llm,
        browser_session=session
    )

def get_navbar_agent(session):
    return Agent(
        task="From the Current page , Get the elements on the navbar" + NAVBAR_PROMPT,
        llm=llm,
        browser_session=session,
        controller=controller2
    )
def get_navbar_review_agent(session, label):
    return Agent(
        task=f"Click on the '{label}' section in the navbar and explore it like you're an influencer reviewing the site. Summarize the page’s content in 2–3 sentences, but make it feel personal, insightful, and human — like you're genuinely sharing what stood out to you.",
        llm=llm,
        browser_session=session
    )


UI_REVIEW_PROMPT = """
                    You are a friendly and casual product reviewer. You're currently visiting a product's website.
                        WEBSITE UI REVIEW STYLE:
                                    - Give short, casual opinions like you're showing a friend a cool website
                                    - Use expressions like "Oh wow!", "This looks...", "I love how...", "The design is..."
                                    - Keep it brief - just 2-3 sentences max
                                    - Focus on the value propositions from the users point of view
                                    - Use everyday language, not design jargon
                                    - Be enthusiastic and conversational
                                    - Examples of good responses:
                                    * "Oh look at this UI! It's super clean and modern, really professional looking!"
                                    * "Wow, this website has such a sleek design! The colors are really nice and everything feels organized."
                                    * "This looks pretty cool! The layout is simple but effective, very user-friendly."
                    IMPORTANT:
                        Do not take screenshots or images, just give a quick casual comment about the UI of the website.                        
"""

NAVBAR_PROMPT = """
 OBJECTIVE: Extract the actual navigation bar (navbar) items from the currently open website.
WHAT TO EXTRACT:
- Top-level navbar labels (e.g., "Home", "Features", "Pricing")
- Items inside dropdowns — hover to reveal

DO NOT INCLUDE:
- Sidebar links
- Footer elements
- Elements hidden behind hamburger icons (unless open)
- Generic terms like “Home” unless you actually see them

if Navbar elements are present:
   RETURN THIS EXACT JSON:
     {"titles": [
    { "Features": "https://example.com/features" },
    { "Pricing": "https://example.com/pricing" },
    { "Docs": "https://example.com/docs" }]
    }

else:
    Return This:
	  {"titles": []
	  }
RULES:
- Return ONLY what’s visible on the navbar.
- If no navbar is found or nothing is visible, return:


Return ONLY this JSON structure. No extra text.
JSON FORMAT:
[
  { "Start Free Trial": "https://example.com/start-free-trial" },
  { "Pricing": "https://example.com/pricing" },
  { "Contact": "https://example.com/contact" }
]

STRICT RULES:
- Only return visible elements (what you actually see).
- Don’t guess labels.
- Don’t include footer or sidebar items unless they are clearly navigational.
- No text, explanations, or markdown — just the JSON list.

"""
