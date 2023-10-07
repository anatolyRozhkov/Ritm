import uuid

import pytest
import requests


@pytest.mark.skip("BUG #2: This method always returns 200 status codes, can tell if it working properly")
def test_delete_non_existent_user_by_id_as_unauthorized_user():
    """
    Test delete non-existent user by id as an unauthorized user.
    """
    # When

    endpoint = 'https://reqres.in/api/users/'

    # Then
    response = requests.delete(endpoint + str(uuid.uuid4()))

    # Expected 404 NOT FOUND
    assert response.status_code == 404
