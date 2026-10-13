-- Setup: run schema.sql first.
-- Plain ANSI SQL: works in SQLite and PostgreSQL.

-- Q1
-- Every claim with member name, provider name, amount and status, newest first.
-- Tie-break on id DESC so claims on the same date have a stable order.
SELECT c.id        AS claim_id,
       m.name      AS member_name,
       p.name      AS provider_name,
       c.amount,
       c.status,
       c.submitted_on
FROM claims c
JOIN members   m ON m.id = c.member_id
JOIN providers p ON p.id = c.provider_id
ORDER BY c.submitted_on DESC, c.id DESC;

-- Q2
-- Total amount of approved claims for each employer.
-- Only status = 'approved' is counted ('paid' is a different status).
-- LEFT JOINs + COALESCE keep an employer with no approved claims (total 0).
SELECT e.name AS employer,
       COALESCE(SUM(c.amount), 0) AS total_approved
FROM employers e
LEFT JOIN members m ON m.employer_id = e.id
LEFT JOIN claims  c ON c.member_id = m.id AND c.status = 'approved'
GROUP BY e.id, e.name
ORDER BY e.name;

-- Q3
-- Members who have never submitted a claim.
SELECT m.id, m.name
FROM members m
WHERE NOT EXISTS (SELECT 1 FROM claims c WHERE c.member_id = m.id);

-- Q4
-- Claims submitted after the member's policy had ended.
SELECT c.id AS claim_id, m.name AS member_name, m.policy_end,
       c.submitted_on, c.amount, c.status
FROM claims c
JOIN members m ON m.id = c.member_id
WHERE c.submitted_on > m.policy_end;

-- Q5
-- Possible duplicate claims: same member, provider, amount and date.
-- Lists every claim in each duplicate group.
SELECT c.id AS claim_id, c.member_id, c.provider_id, c.amount, c.submitted_on, c.status
FROM claims c
JOIN (SELECT member_id, provider_id, amount, submitted_on
      FROM claims
      GROUP BY member_id, provider_id, amount, submitted_on
      HAVING COUNT(*) > 1) d
  ON  d.member_id = c.member_id AND d.provider_id = c.provider_id
  AND d.amount = c.amount       AND d.submitted_on = c.submitted_on
ORDER BY c.member_id, c.submitted_on, c.id;
