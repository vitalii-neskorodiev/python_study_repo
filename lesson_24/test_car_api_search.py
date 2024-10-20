import pytest
import requests
from requests.auth import HTTPBasicAuth
from assertpy import assert_that
from requests import Response, Session
import logging

BASE_URL: str = "http://127.0.0.1:8080"

logging.basicConfig(
    filename='test_search.log',
    filemode='a',
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)


@pytest.fixture(scope="class")
def authorized_session() -> Session:
    auth = HTTPBasicAuth('test_user', 'test_pass')
    response: Response = requests.post(f"{BASE_URL}/auth", auth=auth)

    assert_that(response.status_code).is_equal_to(200)
    access_token: str = response.json().get("access_token")

    session = Session()
    session.headers.update({'Authorization': f'Bearer {access_token}'})
    return session


class TestCarAPISearch:

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            (None, 5),
            ("price", 3),
            ("year", 7),
            ("engine_volume", 10),
            ("brand", 2),
            ("price", None),
            (None, None),
        ]
    )
    def test_get_desired_car(self, authorized_session, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        response = authorized_session.get(f"{BASE_URL}/cars", params=params)
        assert_that(response.status_code).is_equal_to(200)
        cars = response.json()
        assert_that(cars).is_instance_of(list)

        log_message = f"Test with sort_by={sort_by} and limit={limit}: Returned {len(cars)} cars."
        logging.info(log_message)
        print(log_message)

        if limit:
            assert_that(len(cars)).is_less_than_or_equal_to(limit)

        if sort_by:
            sorted_cars = sorted(cars, key=lambda x: x.get(sort_by))
            assert_that(cars).is_equal_to(sorted_cars)
