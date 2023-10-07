import uuid

import pytest
import requests


@pytest.mark.skip("BUG #2: these methods don't seem to work as they always return 200 status codes")
@pytest.mark.parametrize("http_method", ["put", "patch"])
def test_put_patch_non_existent_user_by_id_as_unauthorized_user(http_method):
    """
    Test update and partially update
    non-existent user by id as an unauthorized user.


    NOTE:
    These methods don't seem to work because they return 200 status codes even on random users.
    It could be viewed as a security feature tho, but I can't verify this without access to
    the DB.
    """
    # When
    endpoint = 'https://reqres.in/api/users/'

    http_client_method = getattr(requests, http_method)

    # Then
    response = http_client_method(endpoint + str(uuid.uuid4()))

    # Expected 404 NOT FOUND
    assert response.status_code == 404
