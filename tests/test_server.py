from app import main


def test_server_ping():
    response = main.app.test_client().get("/ping")
    res = response.data.decode("utf-8")
    assert res == "pong"
