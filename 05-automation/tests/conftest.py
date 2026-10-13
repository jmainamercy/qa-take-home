import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from tests.data import STANDARD_USER

@pytest.fixture(scope="session", autouse=True)
def _use_data_test_attribute(playwright):
    """Sauce Demo uses the attribute data-test; Playwright's default is data-testid."""
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)


@pytest.fixture
def logged_in(page: Page, login_page: LoginPage, inventory_page: InventoryPage):
    """Fresh browser context per test (pytest-playwright default), so tests don't share state."""
    login_page.open()
    login_page.login(*STANDARD_USER)
    expect(inventory_page.title).to_have_text("Products")
    return inventory_page
