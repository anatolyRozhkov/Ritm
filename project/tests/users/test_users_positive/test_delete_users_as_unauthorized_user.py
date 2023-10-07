import pytest
import requests


@pytest.mark.skip("BUG #1: This method doesn't seem to work as it doesn't actually delete users")
def test_put_patch_as_unauthorized_user(users_from_db):
    """
    Test delete user by id as an unauthorized user.
    """

    # When
    # Get a user from our improvised DB as if we created it
    first_user_from_db = users_from_db[0]

    endpoint = 'https://reqres.in/api/users/'

    # Then
    response = requests.delete(endpoint + str(first_user_from_db.id))

    # Expected 204 NO CONTENT
    assert response.status_code == 204

    # Step 2
    # Fetch deleted user to check if it was really deleted
    # This step would be normally done using the DB

    # Try fetching deleted user by id
    response = requests.get(endpoint + str(first_user_from_db.id))

    # Expected 404 NOT FOUND
    assert response.status_code == 404
