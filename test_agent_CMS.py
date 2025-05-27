import os
import pytest

from datetime import datetime

from playwright.sync_api import Page
from Support.agent_login import agentLogin
@pytest.mark.parametrize("username,password", [("sakiba.audacityit@bkash.com", "Sehreen@7654321")])
def test_agent_cms(page, username, password):
    page.goto("https://uat-agent-campaign.bkash.com/")
    page.wait_for_timeout(4000)  # Wait for 2 seconds to ensure the page loads

    # ✅ Create an instance of agentLogin with credentials
    login_agent = agentLogin(username, password)

    # ✅ Now call the login method using the instance
    login_agent.login(page)
