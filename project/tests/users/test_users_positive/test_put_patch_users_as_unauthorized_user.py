import pytest
import requests

from tests.utilities.get_date import get_time_and_date, current_time_in_gmt_plus_0


@pytest.mark.parametrize("http_method", ["put", "patch"])
def test_put_patch_user_by_id_as_unauthorized_user(
        http_method, users_from_db
):
    """
    Test update and partially update user by id
    as an unauthorized user.

    Compare updated time with the current time in
    GMT+0 since it's the time the servers operate in.
    """

    # When
    # Get a user from our improvised DB as if we created it
    first_user_from_db = users_from_db[0]

    endpoint = 'https://reqres.in/api/users/'

    http_client_method = getattr(requests, http_method)

    # Then
    response = http_client_method(endpoint + str(first_user_from_db.id))

    response_dict = response.json()

    # Expected 200 OK
    assert response.status_code == 200
    assert len(response_dict) == 1

    assert get_time_and_date(response_dict['updatedAt']) == current_time_in_gmt_plus_0()
