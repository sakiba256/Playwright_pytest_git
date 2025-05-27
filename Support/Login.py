class Login:
    def visit (page,username, password):
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.fill("#username", username)
        page.fill("#password", password)
        page.click("#submit")


    def validate(page):
        page.wait_for_timeout(2000)
        page.screenshot(path="Screenshots/login_screenshot.png")
        page.wait_for_timeout(2000)


 