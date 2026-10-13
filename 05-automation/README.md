# Task 5: UI automation (Playwright + Python + pytest) for Sauce Demo

## Run (one command after setup)

```bash
cd 05-automation
uv venv env && source env/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest
```

Useful options: `pytest --headed` (watch the browser), `pytest --browser firefox`.

## What is covered

| Test                                                  | What it checks                                                                       |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `test_standard_user_can_log_in_and_sees_product_list` | Lands on `/inventory.html`, title "Products", at least one product shown             |
| `test_locked_out_user_sees_error_message`             | Error is visible, mentions the user is locked out, user stays off the inventory page |
| `test_adding_two_products_shows_badge_of_two`         | Cart badge text is "2"                                                               |
| `test_checkout_shows_order_confirmation`              | Confirmation heading "Thank you for your order!" and the complete page               |

## Structure

- `pages/`: one page object per screen (login, inventory, cart, checkout); locators live here only.
- `tests/`: tests read like user steps; `conftest.py` holds fixtures (a `logged_in` fixture, page-object fixtures).
- `pytest.ini`: base URL, so tests use relative paths.

## Design choices

- Locators use `data-test` attributes via `get_by_test_id`. Sauce Demo uses `data-test` (Playwright's default is `data-testid`), so `tests/conftest.py` sets the attribute name once for the whole session.
- No fixed waits. Playwright's `expect(...)` auto-waits and retries.
- Each test gets a fresh browser context, so tests don't depend on each other and can run in any order.

## Status / known gaps

- GitHub Actions workflow: `.github/workflows/tests.yml` at the repo root. Link to a passing run: https://github.com/jmainamercy/qa-take-home/actions/runs/38356516063
- Status : Success
- WorkFlow Name: UI tests
- Job Name: ui-tests (completed in 33 seconds)
- Total Duration: 38 seconds
- Trigger: Pushed to the main branch by user @jmainamercy
