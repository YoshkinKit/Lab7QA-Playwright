from playwright.sync_api import Page, expect

def test_contact_form(page: Page):
    page.goto('http://localhost:3000')
    page.fill('#name', 'Mykyta')
    page.fill('#message', 'Ваша програма дуже класне!')
    page.click('#sendButton')
    expect(page.locator('#successMessage')).to_be_visible()

def test_page_title(page: Page):
    page.goto('http://localhost:3000')
    expect(page).to_have_title("Форма зворотного зв'язку")

def test_required_fields(page: Page):
    page.goto('http://localhost:3000')
    page.click('#sendButton')
    invalid_element = page.query_selector(':invalid')
    assert invalid_element is not None
