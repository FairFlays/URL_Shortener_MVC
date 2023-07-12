from datetime import datetime

from src.models.health_models import HealthResponse


def healthcheck() -> dict[str, datetime]:
    return HealthResponse(status="OK", current_time=datetime.now()).model_dump()
