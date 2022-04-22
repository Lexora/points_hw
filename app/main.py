from flask import Blueprint, Flask, request, jsonify

# from flask_cors import CORS
# from flask_restful import Api, Resource, reqparse
from autoroute_api_processor import autoroute_api_processor
import datetime


app = Flask(__name__)
app.register_blueprint(autoroute_api_processor)


def get_db():
    pass
    # return client.application_fake_database


@app.route("/")
def base_route():
    return "hey there!"


@app.route("/ping")
def ping():
    return f"pong at {str(datetime.datetime.utcnow().isoformat())}"


@app.route("/results", methods=["GET", "POST"])
def users_route():
    try:
        if request.method == "GET":
            pass
            # return jsonify({"status": "success", "payload": str(val)}), 200
        elif request.method == "POST":
            pass
            # return jsonify({"status": "success", "payload": str(val)}), 200
    except Exception:
        return (
            jsonify(
                {
                    "status": "failed",
                    "payload": "Internal server error. Please try again later",
                }
            ),
            500,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
