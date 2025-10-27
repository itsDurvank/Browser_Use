# IN this file, it runs the get_ui_review_agent function and the get_navbar_agent function
import json
from agent_tasks import get_ui_review_agent, get_navbar_agent, get_navbar_review_agent
from audio import speak
from browser_use import Agent
from agent_tasks import llm


async def review_product(session, url):
    
    # Navigate to product URL
    await Agent(
        task=f"Navigate to {url}",
        llm=llm,
        browser_session=session
    ).run()

    # UI Review
    ui_agent = get_ui_review_agent(session, url)
    ui_result = await ui_agent.run()
    speak(ui_result.final_result())

    # Navbar Elements
    nav_agent = get_navbar_agent(session)
    nav_result = await nav_agent.run()
    res = nav_result.final_result()
    print("Navbar result:", res , "Type:", type(res))
    try:
        navbar_items = json.loads(res)  # Now it's a dict
        print("Parsed navbar items:", navbar_items, "Type:", type(navbar_items))
        title_list = navbar_items["titles"]
        labels = [item.get("navbar_title") for item in title_list]
        print("Navbar labels:", labels)
        speak("Here are some sections on the website: " + ", ".join(labels))
    except Exception as e:
        print("Navbar parsing error:", e)
    return labels    

async def run_navbar_review(session,url,labels):
    await Agent(
        task=f"Navigate to {url}",
        llm=llm,
        browser_session=session
    ).run()
 
    speak("Now, let's review the navbar items.")
    for label in labels:
        speak(f"Reviewing the {label} section.")
        navbar_review_agent = get_navbar_review_agent(session, label)
        navbar_review_result = await navbar_review_agent.run()
        speak(navbar_review_result.final_result())
        print("Navbar review completed.")
