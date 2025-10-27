from browser_use import Agent,BrowserSession
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))



async def main():
    browser= BrowserSession(
        keep_alive=True, 
        headless=False,
        wait_for_network_idle_page_load_time=3.0,
        allowed_domains=['*.producthunt.com', '*'],
        executable_path="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    )
    await browser.start()

    agent = Agent(
        task=f"""
               1. Use Navigate action to go to 'https://www.spotify.com' 
               2. Use wait_for_page_load action to ensure the page is fully loaded
               3. Use click action to open the login page
               4. Use type action to enter email which is {os.getenv('spotify_email')}
               5. Use wait action to wait for user input for OTP
               6. Use search action to find 'blue' song on the search bar
               7. Use click action on the play button to play the first song from the search results

""",
        llm=llm,
        browser_session=browser,
        
    )
    result = await agent.run()
    data = result.final_result()
    print("Final result:", data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())