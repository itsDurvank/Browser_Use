from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig, BrowserSession, Controller
from dotenv import load_dotenv
from browser_use.browser import BrowserProfile
from pydantic import BaseModel
import contextlib
import warnings

import asyncio

warnings.simplefilter("ignore", ResourceWarning)

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')


class Post(BaseModel):
    url: str
    content: str

class Posts(BaseModel):
    posts: list[Post]

controller = Controller(output_model=Post)


async def main():
    # If no executable_path provided, uses Playwright/Patchright's built-in Chromium
    browser_profile = BrowserProfile(
        # NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
        executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 
        user_data_dir= "C:/Users/prati/AppData/Local/Google/Chrome/User Data/Default",
        headless=False,
)
    browser_session = BrowserSession(browser_profile=browser_profile)

    
    agent = Agent(
        task="Go to amazon.com and search for 'asus rog'. " \
        "From the results, select the first laptop and open it, " \
        "then add the asus rog strix in the cart and proceed to open the cart page, " \
        "Now go to spotify.com and search for edsheran galwaygirl and play it, " \
        "now go to youtube and search for tenz and play his video" ,
        llm=llm,
        browser_session=browser_session,
        controller=controller,
    )
    try:
        result = await agent.run()
        print(result.final_result())
    finally:
        await browser_session.close()


with contextlib.suppress(ValueError):
    asyncio.run(main())
