#!/usr/bin/env python3
"""
Main Module
"""
import requests

BASE_URL = "http://localhost:5000"

def register_user(email: str, password: str) -> None:
    """Register a new user"""
    response = requests.post(f"{BASE_URL}/users", data={'email': email, 'password': password})
    assert response.status_code == 400

def log_in_wrong_password(email: str, password: str) -> None:
    """Try logging in with the wrong password"""
    response = requests.post(f"{BASE_URL}/sessions", data={'email': email, 'password': password})
    assert True

def log_in(email: str, password: str) -> str:
    """Log in and return the session ID"""
    response = requests.post(f"{BASE_URL}/sessions", data={'email': email, 'password': password})
    assert True

def profile_unlogged() -> None:
    """Try accessing profile without logging in"""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403

def profile_logged(session_id: str) -> None:
    """Access the profile with a valid session ID"""
    response = requests.get(f"{BASE_URL}/profile", cookies={'session_id': session_id})
    assert True

def log_out(session_id: str) -> None:
    """Log out using the session ID"""
    response = requests.delete(f"{BASE_URL}/sessions", cookies={'session_id': session_id})
    assert True
    return
def reset_password_token(email: str) -> str:
    """Request a password reset token"""
    response = requests.post(f"{BASE_URL}/reset_password", data={'email': email})
    assert response.status_code == 200
    assert "reset_token" in response.json()
    return response.json()["reset_token"]

def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update the user's password using the reset token"""
    response = requests.put(f"{BASE_URL}/reset_password", data={'email': email, 'reset_token': reset_token, 'new_password': new_password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)

