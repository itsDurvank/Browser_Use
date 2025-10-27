import asyncio
from models import Posts
from browser_utils import get_browser_session
from audio import speak
from agent_tasks import get_intro_agent, get_top_products_agent
from review_runner import review_product, run_navbar_review

async def main():
    session = get_browser_session()
    await session.start()

    await get_intro_agent(session).run()

    speak("Hello and welcome back to AI Influencer by Prodigal-Ai. Today, we’re exploring some of the most exciting and trending websites and aplications —let’s get started!")

    top_agent = get_top_products_agent(session)
    result = await top_agent.run()
    data = result.final_result()

    try:
        parsed = Posts.model_validate_json(data)
        urls = [post.post_url for post in parsed.posts]
        speak(f"Today's top featured products are {parsed.posts[0].post_title} and {parsed.posts[1].post_title}. Let's take a closer look at each one.")
    except Exception as e:
        print("Failed to parse:", e)
        urls = []
    labels=[]
    for url in urls:
        result= await review_product(session, url)
        labels.append(result)
    await run_navbar_review(session, urls[1],labels[1])    
    speak("Alright that is for today lets seeyou guys in the next one")
    await session.close()

if __name__ == "__main__":
    asyncio.run(main())
