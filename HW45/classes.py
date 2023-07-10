import requests as r
import time


class User:
    def __init__(self, response):
        self.id = response.json()['id']
        self.name = response.json()['name']
        self.email = response.json()['email']
        self.gender = response.json()['gender']
        self.status = response.json()['status']


class Post:
    def __init__(self, response):
        if isinstance(response, r.models.Response):
            self.id = response.json()['id']
            self.user_id = response.json()['user_id']
            self.title = response.json()['title']
            self.body = response.json()['body']
            self.status_code = response.status_code
        else:
            self.id = response[0]['id']
            self.user_id = response[0]['user_id']
            self.title = response[0]['title']
            self.body = response[0]['body']


class HTTPClient:
    BASE_URL = 'https://gorest.co.in/public/v2'
    USERS_ENDPOINT = '/users'
    POSTS_ENDPOINT = '/posts'

    AUTHORIZATION_HEADER = "Bearer 7769aea9f387689d686ee79df61a615e5a6ba36ec16384d450dfc4414434cd5d"
    BASE_HEADER = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": AUTHORIZATION_HEADER}

    def __init__(self, user=None):
        self.user = user

    @staticmethod
    def email_generator():
        return 'test_user' + str(int(time.time())) + '@' + 'mytest.com.ua'

    def create_user(self, name='John Snow', gender='male', status='active', email_user=None):
        if email_user is None:
            email = HTTPClient.email_generator()
        else:
            email = email_user
        body = {
            "name": name,
            "gender": gender,
            "email": email,
            "status": status
        }
        response = r.post(url=HTTPClient.BASE_URL + HTTPClient.USERS_ENDPOINT, headers=HTTPClient.BASE_HEADER,
                          json=body)
        self.user = User(response)
        return self

    def delete_user(self):
        r.delete(url=HTTPClient.BASE_URL + HTTPClient.USERS_ENDPOINT + '/' + str(self.user.id),
                 headers=HTTPClient.BASE_HEADER)
        self.user = None
        return self

    def create_post(self, user_title, user_body):
        body = {"title": user_title,
                "body": user_body}
        response = r.post(
            url=HTTPClient.BASE_URL + HTTPClient.USERS_ENDPOINT + '/' + str(self.user.id) + HTTPClient.POSTS_ENDPOINT,
            headers=HTTPClient.BASE_HEADER, json=body)
        return Post(response)

    @staticmethod
    def get_post_by_id(id_post):
        params = {"id": id_post}
        response = r.get(url=HTTPClient.BASE_URL + HTTPClient.POSTS_ENDPOINT, headers=HTTPClient.BASE_HEADER,
                         params=params)
        return Post(response.json())
