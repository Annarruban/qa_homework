import pytest
from employee_api import EmployeeApi

@pytest.fixture
def api():
   api = EmployeeApi("5.101.50.27:8000")
   yield api

@pytest.mark.parametrize("user_id, expected_first_name, expected_last_name, expected_email", [
(1, "Иван", "Иванов", "ivan@example.com"), ])
def test_get_existing_user(api, user_id, expected_first_name, expected_last_name, expected_email):
    employee = api.info(user_id)
    assert employee["first_name"] == expected_first_name
    assert employee["last_name"] == expected_last_name
    assert employee["email"] == expected_email
    assert employee["id"] == user_id


def test_non_existing_user(api):
    with pytest.raises(Exception):
        _ = api.info(-1)

@pytest.mark.parametrize("first_name, second_name, email, company_id, phone, birthdate", [
("John", "Doe", "john@example.com", 1, "+38000000", "1970-01-01"), ])
def test_create_user(api, first_name, second_name, email, company_id, phone, birthdate):
    response = api.create({
        "first_name": first_name, "last_name": second_name,
        "email": email, "company_id": company_id,
        "phone": phone, "birthdate": birthdate}
    )
    id = response["id"]
    employee = api.info(id)
    assert employee["first_name"] == first_name
    assert employee["last_name"] == second_name
    assert employee["email"] == email
    assert employee["id"] == id

@pytest.mark.parametrize("user_id, email, new_email", [
(3, "anna@example.com", "anna@yahoo.com"), ])
def test_update_user(api, user_id, email, new_email):
    token = api.get_token()
    _ = api.change(user_id, token,{
        "email": new_email
    })
    response = api.info(user_id)
    assert response["email"] == new_email
    response = api.change(user_id, token, {
        "email": email
    })
    assert response["email"] == email
