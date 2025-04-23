import requests


class EmployeeApi:
    USERNAME = "harrypotter"
    PASSWORD = "expelliarmus"

    EMPLOYEE_ENDPOINT = 'employee'
    GET_EMPLOYEE_ENDPOINT = f'{EMPLOYEE_ENDPOINT}/info'
    CREATE_EMPLOYEES_ENDPOINT = f'{EMPLOYEE_ENDPOINT}/create'
    CHANGE_EMPLOYEE_ENDPOINT = f'{EMPLOYEE_ENDPOINT}/change'

    LOGIN_ENDPOINT = f'auth/login'

    def __init__(self, address):
        self._address = address
        self._session = requests.Session()

    def _token(self, user, password):
        creds = {"username": user, "password": password}
        url =  f'http://{self._address}/{self.LOGIN_ENDPOINT}'
        resp = requests.post(url, json=creds)
        return resp.json()["user_token"]

    def get_token(self):
        return self._token(self.USERNAME, self.PASSWORD)

    def info(self, employee_id):
        url = f'http://{self._address}/{self.GET_EMPLOYEE_ENDPOINT}/{employee_id}'
        resp = self._session.get(url)
        resp.raise_for_status()
        return resp.json()

    def create(self, data):
        url = f'http://{self._address}/{self.CREATE_EMPLOYEES_ENDPOINT}'
        resp = self._session.post(url, json=data)
        resp.raise_for_status()
        return resp.json()

    def change(self, user_id, token, update):
        url = f'http://{self._address}/{self.CHANGE_EMPLOYEE_ENDPOINT}/{user_id}?client_token={token}'
        resp = self._session.patch(url, json=update)
        resp.raise_for_status()
        return resp.json()