# API findings: Restful Booker

Source: two `pytest -v` runs of `test_restful_booker.py` (15 tests each, Python 3.10.12, pytest 8.3.3). Everything below comes from those runs. Severity is my own judgement.

## Reproducible behaviour (same result in both runs)

| #   | Request                                                                    | Expected                                  | Actual                                | Why it matters                                                                                                            | Severity |
| --- | -------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | `POST /booking` with only `{"firstname": "OnlyName"}`                      | 400 Bad Request with a validation message | **500** (both runs)                   | A client mistake causes a server error. It hides the real problem from the caller and looks like an outage in monitoring. | Medium   |
| 2   | `POST /booking` with `totalprice: "not-a-number"` (all other fields valid) | 400, since a number is expected           | **200**: booking accepted (both runs) | Invalid data is accepted and can reach reports or calculations later. The runs don't show what was stored.                | Medium   |
| 3   | `PUT /booking/999999999` with a valid token                                | 404 Not Found                             | **405** Method Not Allowed            | The status is misleading: the method is allowed, the booking just doesn't exist. Clients can't tell the two cases apart.  | Low      |

## Intermittent: response time over 2 s

| Run | Request                                | Status        | Time   |
| --- | -------------------------------------- | ------------- | ------ |
| 1   | `PUT /booking/{id}` with a wrong token | 403 (correct) | 2.77 s |
| 2   | `POST /auth` with valid credentials    | 200 (correct) | 2.33 s |

## Other notes

- **`DELETE` returns 201.** `test_delete_booking_then_get_returns_404` asserts 201 (as the documentation states) and passed in both runs. REST convention would be 200 or 204. Minor design note, consistent with the documentation.
- **Passed negative cases (both runs):** `GET` of a missing booking returns 404; `PUT` without a token is refused; `DELETE` without a token is refused and the booking remains.
