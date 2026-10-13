import pytest
import requests

import config


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json", "Accept": "application/json"})
    return s


@pytest.fixture(scope="session")
def token(session):
    r = session.post(f"{config.BASE_URL}/auth",
                     json={"username": config.USERNAME, "password": config.PASSWORD})
    assert r.status_code == 200, f"Could not get a token: {r.status_code} {r.text}"
    tok = r.json().get("token")
    assert tok, f"No token in response: {r.text}"
    return tok


@pytest.fixture
def auth_headers(token):
    return {"Cookie": f"token={token}"}


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Test",
        "lastname": "Member",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def booking_id(session, booking_payload):
    """Creates a booking and passes its ID to the test. Deletes it afterwards so tests stay independent."""
    r = session.post(f"{config.BASE_URL}/booking", json=booking_payload)
    assert r.status_code == 200, r.text
    bid = r.json()["bookingid"]
    yield bid
    try:
        tok = session.post(f"{config.BASE_URL}/auth",
                           json={"username": config.USERNAME, "password": config.PASSWORD}).json().get("token")
        session.delete(f"{config.BASE_URL}/booking/{bid}", headers={"Cookie": f"token={tok}"})
    except Exception:
        pass
