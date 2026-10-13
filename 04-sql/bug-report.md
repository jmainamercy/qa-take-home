# Bug report: claim approved for a member whose policy had already ended

**Found by:** Q4 in `queries.sql` (output in `results.txt`, run on SQLite)

| Field         | Value                                                                                  |
| ------------- | -------------------------------------------------------------------------------------- |
| Title         | Claim 4 was approved although it was submitted 15 days after the member's policy ended |
| Environment   | Claims dataset from the brief, SQLite (in-memory), schema as given                     |
| Preconditions | Dataset loaded exactly as given in the brief                                           |

## Steps to reproduce

1. Load the script from the brief.
2. Run:
   ```sql
   SELECT c.id, m.name, m.policy_end, c.submitted_on, c.amount, c.status
   FROM claims c JOIN members m ON m.id = c.member_id
   WHERE c.submitted_on > m.policy_end;
   ```

## Expected result

A claim submitted after `policy_end` is not payable. Its status should be `rejected` (or the claim should be blocked at submission), or it should be flagged for manual review.

## Actual result

One row is returned:

| claim_id | member                   | policy_end | submitted_on | amount | status       |
| -------- | ------------------------ | ---------- | ------------ | ------ | ------------ |
| 4        | Wanjiru Kamau (member 3) | 2026-06-30 | 2026-07-15   | 8000   | **approved** |

The 8000 is also counted in Kilima Tech's approved total (Q2), so the employer total is overstated by this amount if the claim is invalid.

## Severity / priority

- **Severity: High.** An approved claim on an expired policy is a wrong payout. Money leaves the company.
- **Priority: High.** Fix and check for other such claims before the next payout run.

## Notes and assumptions

- The data only has `submitted_on`, not the date of treatment. If the policy rules allow late submission for treatment that happened while the policy was active, the claim may be valid. The data should then hold a treatment date so this can be checked. This is worth asking the product owner.
- Suggested follow-ups: add a rule or database check that blocks or flags claims where `submitted_on > policy_end`, and re-run Q4 across production data.

## Evidence

`04-sql/results.txt`

## Related finding (not written up separately)

Q5 shows claims 5 and 6 (member 4, provider 1, 3000, 2026-09-01, both `submitted`) are possible duplicates. This needs confirming with the business, since two identical visits on one day is unusual but possible.
