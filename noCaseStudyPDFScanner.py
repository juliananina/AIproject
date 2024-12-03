import re
from playwright.sync_api import sync_playwright

def run(playwright):
    with open('links.txt', 'r') as file:
        links = file.readlines()
    count = 1
    # Process each link
    for link in links:
        link = link.strip()  # Remove any extra whitespace/newline characters
        print(link)  # Or process the link as needed
        browser = playwright.firefox.launch(headless=True)
        context = browser.new_context(
            accept_downloads=True,  # Ensures the download happens directly
            bypass_csp=True  # To avoid content security policy issues if any
        )
        page = context.new_page()

        # Open the links.txt file and read each line

        # Navigate to the page
        page.goto(link)
        print("works before download")
        
        # Listen for the download event
        
        # Click the link to trigger the download
        # page.locator('a', has_text="Download Case Study PDF").click(force=True)
        # page.get_by_role("link", name="Download The Case Study PDF").click()
        # page.locator("a").filter(has_text="Download Case Study PDF")
        
        if page.locator("a", has_text="Download The Case Study PDF").is_visible():
            print("has download button")

        elif page.locator("a", has_text="Download Case Study PDF").is_visible():
            print("has download button")
           
        else:
            with open('nodownloadbutton.txt', 'a') as no_download_file:
                print("No download link button on this page : " + link)
                no_download_file.write(link + '\n')
                print("link recorded in the text file")
                
        # Clean up
        context.close()
        browser.close()

# Run the script with Playwright
with sync_playwright() as playwright:
    run(playwright)
