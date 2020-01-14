from bddrest import status


def test_querystring(app, story, when):

    @app.route()
    def get(*, baz=None):
        assert app.request.query['foo'] == 'bar'
        assert baz == 'qux'

    with story(app, '/?foo=bar&baz=qux'):
        assert status == 200
