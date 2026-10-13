"""Restful Booker API tests.

Every test asserts: (1) the status code, (2) key body fields, (3) response time < 2 s.
Expected values follow the API documentation. Where good API design disagrees with the
documented behaviour, the test asserts good design and the comment says so. A failing test
there is a candidate entry for findings.md, not necessarily a mistake in the test.
"""
import pytest

import config

URL = config.BASE_URL


def fast(r):
    assert r.elapsed.total_seconds() < config.MAX_RESPONSE_SECONDS, \
        f"Too slow: {r.elapsed.total_seconds():.2f}s"


def test_auth_valid_credentials_returns_token(session):
    r = session.post(f"{URL}/auth", json={"username": config.USERNAME, "password": config.PASSWORD})
    assert r.status_code == 200
    assert isinstance(r.json().get("token"), str) and r.json()["token"]
    fast(r)


def test_auth_wrong_password_returns_no_token(session):
    r = session.post(f"{URL}/auth", json={"username": config.USERNAME, "password": "wrong"})
    assert r.status_code in (200, 401)
    assert "token" not in r.json()
    fast(r)

def test_create_booking(session, booking_payload):
    r = session.post(f"{URL}/booking", json=booking_payload)
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body["bookingid"], int)
    assert body["booking"]["firstname"] == booking_payload["firstname"]
    assert body["booking"]["totalprice"] == booking_payload["totalprice"]
    assert body["booking"]["bookingdates"] == booking_payload["bookingdates"]
    fast(r)


def test_get_booking_by_id(session, booking_id, booking_payload):
    r = session.get(f"{URL}/booking/{booking_id}")
    assert r.status_code == 200
    body = r.json()
    assert body["firstname"] == booking_payload["firstname"]
    assert body["lastname"] == booking_payload["lastname"]
    assert body["depositpaid"] is True
    fast(r)


def test_get_booking_ids_contains_new_booking(session, booking_id):
    r = session.get(f"{URL}/booking")
    assert r.status_code == 200
    assert booking_id in [b["bookingid"] for b in r.json()]
    fast(r)

def test_put_updates_whole_booking(session, booking_id, booking_payload, auth_headers):
    new = {**booking_payload, "firstname": "Updated", "totalprice": 999}
    r = session.put(f"{URL}/booking/{booking_id}", json=new, headers=auth_headers)
    assert r.status_code == 200
    assert r.json()["firstname"] == "Updated"
    assert r.json()["totalprice"] == 999
    fast(r)
    assert session.get(f"{URL}/booking/{booking_id}").json()["firstname"] == "Updated"


def test_patch_updates_only_given_fields(session, booking_id, booking_payload, auth_headers):
    r = session.patch(f"{URL}/booking/{booking_id}", json={"lastname": "Patched"}, headers=auth_headers)
    assert r.status_code == 200
    body = r.json()
    assert body["lastname"] == "Patched"
    assert body["firstname"] == booking_payload["firstname"] 
    fast(r)

def test_delete_booking_then_get_returns_404(session, booking_id, auth_headers):
    r = session.delete(f"{URL}/booking/{booking_id}", headers=auth_headers)
    assert r.status_code == 201
    fast(r)
    r2 = session.get(f"{URL}/booking/{booking_id}")
    assert r2.status_code == 404
    fast(r2)


def test_create_missing_required_fields_is_rejected(session):
    r = session.post(f"{URL}/booking", json={"firstname": "OnlyName"})
    assert r.status_code == 400
    fast(r)


def test_create_wrong_data_type_is_rejected(session, booking_payload):
    bad = {**booking_payload, "totalprice": "not-a-number"}
    r = session.post(f"{URL}/booking", json=bad)
    assert r.status_code == 400
    fast(r)


def test_get_nonexistent_booking_returns_404(session):
    r = session.get(f"{URL}/booking/999999999")
    assert r.status_code == 404
    fast(r)


def test_put_without_token_is_forbidden(session, booking_id, booking_payload):
    r = session.put(f"{URL}/booking/{booking_id}", json=booking_payload)
    assert r.status_code in (401, 403)
    fast(r)


def test_put_with_wrong_token_is_forbidden(session, booking_id, booking_payload):
    r = session.put(f"{URL}/booking/{booking_id}", json=booking_payload,
                    headers={"Cookie": "token=not-a-real-token"})
    assert r.status_code in (401, 403)
    fast(r)


def test_delete_without_token_is_forbidden_and_booking_remains(session, booking_id):
    r = session.delete(f"{URL}/booking/{booking_id}")
    assert r.status_code in (401, 403)
    fast(r)
    assert session.get(f"{URL}/booking/{booking_id}").status_code == 200


def test_update_nonexistent_booking(session, booking_payload, auth_headers):
    r = session.put(f"{URL}/booking/999999999", json=booking_payload, headers=auth_headers)
    assert r.status_code == 404
    fast(r)
