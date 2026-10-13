# Task 2: Bug reports: Sauce Demo (problem_user)

**Environment for all reports:** Chrome Version 145.0.7632.75 , Ubuntu 24.04.4 2026.02.15 LTS (Cubic 2026-02-15 13:07) , screen size 1920 × 1200, URL https://www.saucedemo.com
**Preconditions for all:** Logged in as `problem_user` / `secret_sauce` (shown on the login page); cart empty unless stated.

Severity scale used: **Critical** = blocks purchase or loses data; **High** = major function broken, workaround exists; **Medium** = wrong output, purchase still possible; **Low** = cosmetic.

---

## BUG-01: Product list shows the wrong images

**Steps to reproduce**

1. Log in as `problem_user`.
2. On the product list, look at the image of each product.
3. Repeat as `standard_user` and compare.

**Expected:** Each product shows its own image, as it does for `standard_user`.
**Actual:** For `problem_user` the products show the wrong images. All six products show the same image an image of dog with a ball in its mouth
**Severity / priority:** High / High: users can't tell from the picture what they are buying.
**Evidence:** screenshots/bug-01.png

## BUG-02: Only three of six products can be added to the cart; Remove doesn't work on the product list

**Steps to reproduce**

1. Log in as `problem_user`.
2. Click "Add to cart" on each product, one at a time, and watch the button and the cart badge.
3. Click "Remove" on each product, on the product list and then on the cart page.

**Expected:** Every product's button changes to "Remove" and the cart badge goes up by 1. "Remove" reverses this.
**Actual:** Only three of the six products can be added to the cart. On the product list the "Remove" button can't be clicked; removing only works from the cart page.
**Severity / priority:** Critical / High: some products can't be bought at all.
**Evidence:** screenshots/bug-02.png

## BUG-03: Sort dropdown does not change the order

**Steps to reproduce**

1. Log in as `problem_user`.
2. Choose each sort option in turn (name A→Z, Z→A, price low→high, high→low).

**Expected:** The list reorders as labelled.
**Actual:** Nothing changes.
**Severity / priority:** Medium / Medium: users can still buy without sorting.
**Evidence:** screenshots/bug-03.png

## BUG-04: Checkout: first name is erased when moving to the next field

**Steps to reproduce**

1. Log in as `problem_user`, add one product, open the cart and click Checkout.
2. Type a first name (for example "Test").
3. Click or tab into the last name field and look at the first name field.

**Expected:** Each field keeps what was typed, and Continue takes the user to the overview page.
**Actual:** The first name can be typed, but when focus moves to the next field the first name is deleted. Once you are ablw to click continue you are directed to login page
**Severity / priority:** Critical / High: if the checkout details can't be entered, the user can't complete a purchase.
**Evidence:** screenshots/bug-04.png

---

## Other areas tested

Login, product details page, cart contents: no further bugs were found
