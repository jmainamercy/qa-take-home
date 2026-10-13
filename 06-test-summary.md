# Test Summary: Sauce Demo release readiness

**Date:** 13/10/2026  **Tester:** Mercy Maina  **Build:** https://www.saucedemo.com (public practice site)

## What was tested

| Area                  | Task  | Scope                                                                                                 |
| --------------------- | ----- | ----------------------------------------------------------------------------------------------------- |
| Manual UI exploration | 2     | Login, product list, product details, cart, checkout as `problem_user`, compared with `standard_user` |
| API (Restful Booker)  | 3     | 15 pytest tests: auth, create/read/update/delete, negative cases                                      |
| UI automation         | 5     | 4 Playwright tests: login, locked-out user, cart badge, checkout                                      |
| Load (k6)             | bonus | Not done                                                                                              |

**Not tested:** load and performance, other browsers and mobile, accessibility, security, and the other demo users (`performance_glitch_user`, `error_user`, `visual_user`).

Task 3 tested Restful Booker, a different system, so its results say nothing about Sauce Demo's readiness.

## Results

| Suite                       | Run       | Passed | Failed           | Notes                                                                                                                      |
| --------------------------- | --------- | ------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Manual exploration (Task 2) | 5 areas   | n/a    | 4 bugs found    | Exploratory, so no pass/fail count. Details in 02-bug-reports. Rated 2 Critical, 1 High, 1 Medium      |
| API tests (Task 3)          | 15        | 12     | 3                | 3 failures are API behaviour (500, 200, 405; see 03-api/findings.md). The 2 s response-time check is intermittent.         |
| UI automation (Task 5)      | 4         | 4      | 0                | All four pass on `standard_user` and `locked_out_user` flows. They don't cover `problem_user`, where the bugs were found. |

## Three biggest risks if released today

1. **Checkout can't be completed.** For `problem_user` the first name is erased when moving to the next field (BUG-04), so the order details can't be entered and the purchase is blocked.
2. **Products can't be added to the cart.** Only three of six products can be added, and Remove doesn't work on the product list (BUG-02), so customers can't buy everything on sale.
3. **Wrong product images.** Products show the wrong images (BUG-01), so customers can't tell what they are buying. This adds to the risk of wrong orders and returns.

## Recommendation

**Hold.** Two bugs rated Critical (BUG-02 and BUG-04) stop a customer from buying, so the shop should not be released until they are fixed and retested. BUG-01 and BUG-03 can follow as known issues.

## What I would test next

- Other users (`performance_glitch_user`, `error_user`, `visual_user`) and the bugs I found, as automated regression tests
- Other browsers and a mobile viewport
- Accessibility (keyboard use, labels, contrast)
- Load and response time under realistic traffic
