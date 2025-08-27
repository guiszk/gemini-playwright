import asyncio
from playwright.async_api import async_playwright
import sys 

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <prompt>")
    sys.exit(1)

async def run():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)  # Use Firefox
        page = await browser.new_page()

        await page.goto("https://gemini.google.com/app")

        await page.wait_for_selector(".ql-editor > p:nth-child(1)")

        await page.fill(".ql-editor > p:nth-child(1)", sys.argv[1])

        await page.click(".send-button-icon")

        await page.wait_for_selector(".refresh-icon")

        text = await page.locator('.response-content').last.inner_text()
        print("Assistant response:", text)

asyncio.run(run())
