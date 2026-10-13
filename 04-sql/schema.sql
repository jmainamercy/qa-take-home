CREATE TABLE employers (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE members (id INTEGER PRIMARY KEY, name TEXT,
 employer_id INTEGER, policy_end DATE);
CREATE TABLE providers (id INTEGER PRIMARY KEY, name TEXT, type TEXT);
CREATE TABLE claims (id INTEGER PRIMARY KEY, member_id INTEGER,
 provider_id INTEGER, amount INTEGER, status TEXT, submitted_on DATE);
INSERT INTO employers VALUES (1, 'Sunrise Logistics'), (2, 'Kilima Tech');
INSERT INTO members VALUES
 (1, 'Achieng Otieno', 1, '2026-12-31'),
 (2, 'Brian Mwangi', 1, '2026-12-31'),
 (3, 'Wanjiru Kamau', 2, '2026-06-30'),
 (4, 'Hassan Ali', 2, '2027-03-31'),
 (5, 'Njeri Wambui', 1, '2026-12-31');
INSERT INTO providers VALUES
 (1, 'Uhai Clinic', 'Outpatient'),
 (2, 'Mto Pharmacy', 'Pharmacy'),
 (3, 'Baraka Dental', 'Dental');
INSERT INTO claims VALUES
 (1, 1, 1, 4500, 'approved', '2026-08-02'),
 (2, 1, 2, 1200, 'paid', '2026-08-05'),
 (3, 2, 1, 15000, 'rejected', '2026-08-10'),
 (4, 3, 3, 8000, 'approved', '2026-07-15'),
 (5, 4, 1, 3000, 'submitted', '2026-09-01'),
 (6, 4, 1, 3000, 'submitted', '2026-09-01'),
 (7, 2, 2, 2500, 'approved', '2026-09-12'),
 (8, 1, 3, 22000, 'in_review', '2026-09-20');
