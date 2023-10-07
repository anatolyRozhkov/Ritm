import pytest
import requests

from project.tests.utilities.shared_data import UserData


@pytest.fixture
def users_from_db():
    """
    This will be our improvised DB call.
    Meaning that here we have a list of users
    that we will use to cross-verify responses from tests.

    It's not an ideal solution, but it will ease up our test
    development considerably.
    """

    response = requests.get('https://reqres.in/api/users?per_page=100')

    assert response.status_code == 200

    user_data_list = []
    json_dict = response.json()

    for user in json_dict.get('data', []):
        user_data = UserData(
            id=user['id'],
            email=user['email'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            avatar=user['avatar']
        )
        user_data_list.append(user_data)

    return user_data_list


@pytest.fixture
def user_page_count_from_db():
    """
    Return number of users and the number
    of pages without filters applied.
    """
    response = requests.get('https://reqres.in/api/users')

    assert response.status_code == 200

    json_dict = response.json()

    return {'page_count': json_dict['total_pages'], 'user_count': json_dict['total']}

