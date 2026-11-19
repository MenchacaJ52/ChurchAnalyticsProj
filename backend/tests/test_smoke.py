import pytest
from django.contrib.auth import get_user_model


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.django_db
def test_user_signs_in_with_email():
    User = get_user_model()
    user = User.objects.create_user(email="Pastor@Example.com", password="s3cret-pass!")
    assert user.email == "Pastor@example.com"  # domain part normalized
    assert user.check_password("s3cret-pass!")
    assert User.USERNAME_FIELD == "email"


@pytest.mark.django_db
def test_create_superuser_sets_flags():
    admin = get_user_model().objects.create_superuser(email="admin@example.com", password="x")
    assert admin.is_staff and admin.is_superuser
