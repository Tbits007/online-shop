from app.domain.users import Users


def test_users_model():
    """Тестирует инициализацию модели Users."""

    user = Users(
        email="test@example.com",
        hashed_password="hashedpassword",
        is_active=True,
        is_superuser=False,
        is_verified=True
    )

    assert user.email == "test@example.com"
    assert user.hashed_password == "hashedpassword"
    assert user.is_active is True
    assert user.is_superuser is False
    assert user.is_verified is True