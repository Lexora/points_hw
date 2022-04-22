from flask import Blueprint
import requests
from collections import namedtuple


autoroute_api_processor = Blueprint("autoroute_api_processor", __name__)

urls = [
    "localhost:5000/autonomous-car/routes/empty-route",
    "localhost:5000/autonomous-car/routes/success-no-obstacles",
    "localhost:5000/autonomous-car/routes/success-with-obstacles",
    "localhost:5000/autonomous-car/routes/failure-out-of-bounds",
    "localhost:5000/autonomous-car/routes/failure-hits-obstacle",
]


def process_request(endpoint):
    pass


@autoroute_api_processor.route("/autoroute_api_processor")
def process_request(request):
    return process_request()

    # return "Welcome to the autoroute_api_processor"
