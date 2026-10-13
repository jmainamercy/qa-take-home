# QA Take-Home Assessment

## Contents

| Task            | Where                                                                           | Status                                                                    |
| --------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1. Test cases   | [01-test-cases/01-test-cases.md](01-test-cases/01-test-cases.md)                | Done: 15 test cases and 3 questions for the product manager               |
| 2. Bug reports  | [02-bug-reports/bug-reports.md](02-bug-reports/bug-reports.md)                  | Done: 4 bugs with screenshots                                             |
| 3. API testing  | [03-api/](03-api/) (pytest) and [findings.md](03-api/findings.md)               | Done: 15 tests run, findings recorded                                     |
| 4. SQL          | [04-sql/queries.sql](04-sql/queries.sql), [bug-report.md](04-sql/bug-report.md) | Done; outputs in [results.txt](04-sql/results.txt) from a real SQLite run |
| 5. Automation   | [05-automation/](05-automation/)                                                | Done: 4 Playwright tests, all passing                                     |
| 6. Test summary | [06-test-summary.md](06-test-summary.md)                                        | Done                                                                      |

Bonus k6 load test: not attempted.

## Time spent

1. Task 1: 40 min
2. Task 2: 40 min
3. Task 3: 40 min
4. Taks 4: 30 min
5. Task 5: 70 min

## Where I got stuck

The API tests failed on a 2-second response-time check that moved between requests on different runs; I recorded it in findings.md as intermittent instead of changing the test.
I do not have K6 installed so i was unable to attempt the bonus question
