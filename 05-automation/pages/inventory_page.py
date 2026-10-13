from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.get_by_test_id("title")
        self.items = page.get_by_test_id("inventory-item")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")
        self.cart_link = page.get_by_test_id("shopping-cart-link")

    def add_to_cart(self, product_slug: str):
        """product_slug is the data-test suffix, e.g. 'sauce-labs-backpack'."""
        self.page.get_by_test_id(f"add-to-cart-{product_slug}").click()

    def open_cart(self):
        self.cart_link.click()
