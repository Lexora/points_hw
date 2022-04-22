from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db():
    pass
    #return client.application_fake_database




@app.route("/ping")
def ping():
    return "pong"

@app.route("/results", methods=['GET', 'POST'])
def users_route():
    try:
        if request.method == 'GET':
            pass
            # return jsonify({"status": "success", "payload": str(val)}), 200
        elif request.method == 'POST':
            pass
            # return jsonify({"status": "success", "payload": str(val)}), 200
    except Exception:
        return (
            jsonify({"status": "failed", "payload": "Internal server error. Please try again later"}),
            500
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)