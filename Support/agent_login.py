class agentLogin:
    def __init__(self, agent_username, agent_password):
        self.agent_username = agent_username
        self.agent_password = agent_password

    def login(self, page):  
        print(f"Agent {self.agent_username} is attempting to log in.")
        page.fill('//input[@id="i0116"]', self.agent_username)
        page.wait_for_timeout(2000)  # Wait for 2 seconds to ensure the page loads
        next_button = page.locator('//input[@id="idSIButton9"]')
        next_button.click()
        page.wait_for_timeout(2000)  # Wait for 2 seconds to ensure the page loads

        page.fill('//input[@id="i0118"]', self.agent_password)
        page.click('//input[@id="idSIButton9"]')
        page.wait_for_timeout(4000)  # Wait for 2 seconds to ensure the page loads


