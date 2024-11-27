import re
from playwright.sync_api import Page, expect

def test_site_title(page: Page):
    page.goto('https://en.wikipedia.org/wiki/Main_Page')
    expect(page).to_have_title(re.compile('Wikipedia'))

def test_search_form(page: Page):
    page.goto('https://en.wikipedia.org/wiki/Main_Page')
    search = page.locator('#p-search')
    expect(search).to_be_visible()

def test_link_help(page: Page):
    page.goto('https://en.wikipedia.org/wiki/Main_Page')
    page.click('#vector-main-menu-dropdown-checkbox')
    page.click('text=Help')
    expect(page).to_have_url(re.compile('Help'))
