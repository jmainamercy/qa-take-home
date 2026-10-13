from playwright.sync_api import expect

from tests.data import STANDARD_USER, LOCKED_OUT_USER


def test_standard_user_can_log_in_and_sees_product_list(page, login_page, inventory_page):
    login_page.open()
    login_page.login(*STANDARD_USER)

    expect(page).to_have_url("/inventory.html")
    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.items).not_to_have_count(0)


def test_locked_out_user_sees_error_message(page, login_page):
    login_page.open()
    login_page.login(*LOCKED_OUT_USER)

    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text("Sorry, this user has been locked out.")
    expect(page).not_to_have_url("/inventory.html")


def test_adding_two_products_shows_badge_of_two(logged_in):
    inventory = logged_in
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")

    expect(inventory.cart_badge).to_have_text("2")


def test_checkout_shows_order_confirmation(logged_in, page, cart_page, checkout_page):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.open_cart()
    expect(cart_page.items).to_have_count(1)
    cart_page.checkout()

    checkout_page.fill_details("Test", "Member", "00100")
    checkout_page.finish()

    expect(checkout_page.confirmation_header).to_have_text("Thank you for your order!")
    expect(page).to_have_url("/checkout-complete.html")
