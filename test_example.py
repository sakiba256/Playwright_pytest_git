
import os
import pytest

from datetime import datetime

from playwright.sync_api import Page
from Support.Login import Login


# Ensure Screenshots folder exists
os.makedirs("Screenshots", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d %H-%M")
filename = f"Screenshots/example_screenshot_{timestamp}.png"
filename_playwright  = f"Screenshots/Playwright_screenshot_{timestamp}.png"


@pytest.mark.order(2)
def test_basic_playwright(page: Page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.wait_for_timeout(2000)  # Wait for 1 second
    
    page.screenshot(path=filename)

@pytest.mark.skip(reason="Not ready yet")
def test_not_ready(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    
@pytest.mark.order(1)
@pytest.mark.parametrize("url", ["https://playwright.dev"])
def test_check_title(page: Page, url: str):
    page.goto(url)
    assert page.title() != ""
    page.screenshot(path=filename_playwright)
    page.wait_for_timeout(2000)  # Wait for 1 second

@pytest.mark.order(3)
@pytest.mark.parametrize("username,password", [("student", "Password123")])
def test_login(page: Page, username, password):
    Login.visit(page,username, password)
    Login.validate(page)
    print("Login test completed successfully.")
    page.wait_for_timeout(2000)


