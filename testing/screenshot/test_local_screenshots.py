from playwright.sync_api import Page

def test_page_screenshot(page: Page, assert_snapshot):
    page.goto('http://localhost:3000')
    assert_snapshot(page.screenshot())

def test_element_screenshot(page: Page, assert_snapshot):
    page.goto('http://localhost:3000')
    element = page.locator('h1')
    assert_snapshot(element.screenshot())
