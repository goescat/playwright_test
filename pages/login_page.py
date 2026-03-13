class LoginPage:

    def __init__(self, page):
        self.page = page

    def Landing(self):
        self.page.hover("#btn-login")
        self.page.get_by_text("Log in with Old Neopets Account").click()