
url = '/token'


def test_get_token(client):
    data = {'username': 'johndoe', 'password': '@@123456Abc**'}
    r = client.post(url, data)
    assert r.status_code == 200
