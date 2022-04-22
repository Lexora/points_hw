from scr import server


def test_server_ping():
    response = server.app.test_client().get("/ping")
    res = response.data.decode("utf-8")
    assert res == "pong"

