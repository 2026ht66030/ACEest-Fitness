"""Simple pytest tests for ACEestFull.py.

Run:
    pytest test_ACEestFull.py -v
"""
import sqlite3
import app as app


def test_default_admin_credentials(tmp_path, monkeypatch):
    # Use a temporary database for this test.
    test_db = tmp_path / "test_aceest.db"
    monkeypatch.setattr(app, "DB_NAME", str(test_db))

    app.init_db()

    with sqlite3.connect(test_db) as conn:
        row = conn.execute(
            "SELECT role FROM users WHERE username=? AND password=?",
            ("admin", "admin"),
        ).fetchone()

    assert row is not None
    assert row[0] == "Admin"


def test_invalid_credentials_are_not_in_database(tmp_path, monkeypatch):
    test_db = tmp_path / "test_aceest.db"
    monkeypatch.setattr(app, "DB_NAME", str(test_db))

    app.init_db()

    with sqlite3.connect(test_db) as conn:
        row = conn.execute(
            "SELECT role FROM users WHERE username=? AND password=?",
            ("wrong_user", "wrong_password"),
        ).fetchone()

    assert row is None
