from http import HTTPStatus


def test_app(client):
    response = client.get("/admin")

    assert response.status_code == HTTPStatus.MOVED_PERMANENTLY
