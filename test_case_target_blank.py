# Test case - Abstract: Using Python and Playwright verify, if a new page was opened in
# a new tab, after a click on the anchor with href="https://www.fiofondy.cz/"

from playwright.sync_api import sync_playwright


def print_open_tabs_count(number, singl_plural):
    '''This function prints the open tabs count of a given number.'''

    print(f"After click on the element with text FIOFONDY {singl_plural} : {number}")


singl_or_plural = ["is open tab", "are open tabs"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo= 300)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.fio.cz')
    page.wait_for_load_state('networkidle')
    accept_all_cookies = page.locator('button#c-p-bn')
    accept_all_cookies.click()
    a_href_text_FIOFONDY = page.locator('a:has-text("FIOFONDY")')
    a_href_text_FIOFONDY.click()
    page.wait_for_load_state('networkidle')
    open_tabs = page.context.pages
    number_of_tabs = len(open_tabs)
    if number_of_tabs < 1:
        print_open_tabs_count(number_of_tabs, singl_or_plural[0])
        page.screenshot(path="./test_case_target_blank.png", full_page=True)
    else:
        print_open_tabs_count(number_of_tabs, singl_or_plural[1])
        new_tab = open_tabs[number_of_tabs - 1]
        new_tab.bring_to_front()
        new_tab.screenshot(path="./test_case_target_blank.png", full_page=True)
    for i in range(number_of_tabs):
        print(page.context.pages[i].url)
    context.close()
    browser.close()

