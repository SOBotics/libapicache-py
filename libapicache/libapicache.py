from typing import Optional, Union
from datetime import timedelta
import requests


class APICache:
    def __init__(self, host: str):
        self._host = host

    def posts_by_id(self, ids: list, site: str, key: str, page: Optional[int] = 1, pagesize: Optional[int] = 10,
                    max_age: Optional[Union[int, timedelta]] = None):
        uri = '{}/posts/{}?key={}&site={}&page={}&pagesize={}'.format(self._host, ';'.join(ids), key, site, page,
                                                                      pagesize)
        if max_age is not None:
            if isinstance(max_age, timedelta):
                max_age = max_age.total_seconds()

            uri += '&max_age={:.0f}'.format(max_age)

        response = requests.get(uri)
        response.raise_for_status()
        return Response(response.json(), response.status_code)

    def recent_questions(self, site: str, key: str, pagesize: Optional[int] = 10,
                         max_age: Optional[Union[int, timedelta]] = None):
        uri = '{}/questions?key={}&site={}&pagesize={}'.format(self._host, key, site, pagesize)
        if max_age is not None:
            if isinstance(max_age, timedelta):
                max_age = max_age.total_seconds()

            uri += '&max_age={:.0f}'.format(max_age)

        response = requests.get(uri)
        response.raise_for_status()
        return Response(response.json(), response.status_code)


class Response:
    def __init__(self, json_data: dict, response_code: int):
        self.response_code = response_code

        self.has_more = json_data.get('has_more', False)
        self.items = json_data.get('items', [])

        self.error_id = json_data.get('error_id', None)
        self.error_name = json_data.get('error_name', None)
        self.error_message = json_data.get('error_message', None)

    def is_error(self):
        return self.error_id is not None or self.error_name is not None or self.error_message is not None



