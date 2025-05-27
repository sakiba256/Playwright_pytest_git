import pytest
from playwright.sync_api import sync_playwright, Page
import platform
from typing import Generator

# Get Google Chrome executable path based on OS
def get_chrome_path() -> str:
    if platform.system() == "Windows":
        return "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    elif platform.system() == "Darwin":
        return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    else:  # Linux
        return "/usr/bin/google-chrome"

@pytest.fixture
def page() -> Generator[Page, None, None]:
    chrome_path = get_chrome_path()
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            executable_path=chrome_path
        )
        page = browser.new_page()
        yield page
        browser.close()
