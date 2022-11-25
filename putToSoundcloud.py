

from playwright.sync_api import sync_playwright

def initiate():
    inner = ""
    def run(playwright):
        chromium = playwright.firefox  # or "firefox" or "webkit".
        # browser = chromium.launch(headless=False, slow_mo=50)
        browser = chromium.launch()
        page = browser.new_page()
        page.goto("https://www.ruf.rice.edu/~kemmer/Words04/usage/jargon_medical.html")
        page.locator('i')
        ua = page.query_selector("i")
        return ua.inner_html()




    with sync_playwright() as playwright:
        inner = run(playwright)

    return inner
