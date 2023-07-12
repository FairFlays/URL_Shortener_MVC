from flask import Blueprint

from src.services import health

app = Blueprint("health", __name__)


@app.route("/health")
def healthcheck():
    return health.healthcheck()
