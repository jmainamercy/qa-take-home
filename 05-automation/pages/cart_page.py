from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.get_by_test_id("inventory-item")
        self.checkout_button = page.get_by_test_id("checkout")

    def checkout(self):
        self.checkout_button.click()
