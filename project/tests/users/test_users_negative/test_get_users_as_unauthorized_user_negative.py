import uuid

import requests


def test_get_non_existent_user_by_id_as_unauthorized_user():
    """
    Test get non-existent user by id as an unauthorized user.
    """
    # When

    endpoint = 'https://reqres.in/api/users/'

    # Then
    response = requests.get(endpoint + str(uuid.uuid4()))

    # Expected 404 NOT FOUND
    assert response.status_code == 404
