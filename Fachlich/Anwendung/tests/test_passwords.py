"""P04: direkter Passwortvertrag, ausschliesslich synthetische Testwerte."""

import pytest

from app.auth import hash_password, verify


@pytest.mark.parametrize("password", ["unit-test-password", "Grüezi-音楽-2026"])
def test_password_hash_accepts_only_matching_password(password):
    encoded = hash_password(password)

    assert verify(password, encoded) is True
    assert verify(password + "-wrong", encoded) is False


def test_same_password_has_distinct_verifiable_hashes():
    password = "synthetic-salt-test"
    first = hash_password(password)
    second = hash_password(password)

    assert first != second
    assert verify(password, first) is True
    assert verify(password, second) is True


@pytest.mark.parametrize(
    "encoded",
    [None, "", "missing-separator", "too:many:separators"],
    ids=["missing", "empty", "no-separator", "extra-separator"],
)
def test_malformed_password_hash_is_rejected(encoded):
    assert verify("synthetic-password", encoded) is False
