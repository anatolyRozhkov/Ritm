import pytest
import requests

"""
For these tests I will be using fixtures 
that mock real DB calls.

Normally I would cross-verify api responses with the DB,
to make sure that the back-end serves data as expected, so,
sine in this case I don't have access to the DB, I'll pretend
that the fixtures provide 'true' data from the DB.
"""


def test_get_users_as_unauthorized_user(users_from_db, user_page_count_from_db):
    """
    Test get users as an unauthorized user.
    """

    # When
    # Our improvised DB data
    first_user_from_db = users_from_db[0]

    # Count of returned users
    if user_page_count_from_db['user_count'] >= 6:
        returned_user_count = 6
    else:
        returned_user_count = user_page_count_from_db['user_count']

    endpoint = 'https://reqres.in/api/users/'

    # Then
    response = requests.get(endpoint)

    response_dict = response.json()

    # Expected 200 OK
    assert response.status_code == 200
    assert len(response_dict) == 6

    # Verify response body
    assert response_dict['page'] == 1
    assert response_dict['per_page'] == 6
    assert response_dict['total'] == user_page_count_from_db['user_count']
    assert response_dict['total_pages'] == user_page_count_from_db['page_count']
    assert len(response_dict['data']) == returned_user_count

    # Verify support
    assert len(response_dict['support']) == 2
    assert response_dict['support']['url'] == 'https://reqres.in/#support-heading'
    assert response_dict['support'][
               'text'] == 'To keep ReqRes free, contributions towards server costs are appreciated!'

    # Verify single user
    first_user = response_dict['data'][0]
    assert len(first_user) == 5

    assert first_user['id'] == first_user_from_db.id
    assert first_user['email'] == first_user_from_db.email
    assert first_user['first_name'] == first_user_from_db.first_name
    assert first_user['last_name'] == first_user_from_db.last_name
    assert first_user['avatar'] == first_user_from_db.avatar


def test_get_user_by_id_as_unauthorized_user(users_from_db):
    """
    Test get user by id as an unauthorized user.
    """
    # When

    endpoint = 'https://reqres.in/api/users/'

    # Get a user from our improvised DB as if we created it
    first_user_from_db = users_from_db[0]

    # Then
    response = requests.get(endpoint + str(first_user_from_db.id))

    response_dict = response.json()

    # Expected 200 OK
    assert response.status_code == 200
    assert len(response_dict) == 2

    # Verify user
    first_user = response_dict['data']
    assert len(first_user) == 5

    assert first_user['id'] == first_user_from_db.id
    assert first_user['email'] == first_user_from_db.email
    assert first_user['first_name'] == first_user_from_db.first_name
    assert first_user['last_name'] == first_user_from_db.last_name
    assert first_user['avatar'] == first_user_from_db.avatar

    # Verify support
    assert len(response_dict['support']) == 2
    assert response_dict['support']['url'] == 'https://reqres.in/#support-heading'
    assert response_dict['support'][
               'text'] == 'To keep ReqRes free, contributions towards server costs are appreciated!'


@pytest.mark.parametrize(
    "query_string, expected_value",
    [
        ('?page=1&per_page=7', 7),
        ('?page=1&per_page=9', 9),
    ],
)
def test_filters_for_get_users_as_unauthorized_user(query_string, expected_value):
    """
    Test filters for get users as an unauthorized user.
    """

    # When
    endpoint = 'https://reqres.in/api/users/'

    # Then
    response = requests.get(endpoint + query_string)

    response_dict = response.json()

    assert response.status_code == 200

    assert response_dict['per_page'] == expected_value
