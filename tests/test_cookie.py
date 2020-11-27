from http import cookies

from bddrest import status, response


def test_cookie(app, Given):
    @app.route()
    def get(req):
        counter = req.cookies['counter']
        req.cookies['counter'] = str(int(counter.value) + 1)
        req.cookies['counter']['max-age'] = 1
        req.cookies['counter']['path'] = '/a'
        req.cookies['counter']['domain'] = 'example.com'

    headers = {'Cookie': 'counter=1;'}
    with Given(headers=headers):
        assert status == 200
        assert 'Set-cookie' in response.headers
        assert response.headers['Set-cookie'] == \
            'counter=2; Domain=example.com; Max-Age=1; Path=/a'

        cookie = cookies.SimpleCookie(response.headers['Set-cookie'])
        counter = cookie['counter']
        assert counter.value == '2'
        assert counter['path'] == '/a'
        assert counter['domain'] == 'example.com'
        assert counter['max-age'] == '1'
