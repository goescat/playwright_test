
from pages.login_page import LoginPage
from playwright.sync_api import expect


def test_login_p1(page):
    page.goto("https://www.neopets.com/index.phtml")

    LoginPage(page).Landing()

    expect(page).to_have_url("https://www.neopets.com/home/")