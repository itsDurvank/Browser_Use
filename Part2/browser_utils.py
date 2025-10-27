from browser_use import BrowserSession
from config import BRAVE_PATH

def get_browser_session():
    return BrowserSession(
        keep_alive=True, 
        headless=False,
        wait_for_network_idle_page_load_time=3.0,
        allowed_domains=['*.producthunt.com', '*'],
        executable_path=BRAVE_PATH
    )
