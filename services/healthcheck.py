from typing import Dict
from sqlalchemy.sql import text
from extensions import db, redis_client


def check_health() -> Dict[str, bool]:
    connection_status = {"health_check_successful": True}
    try:
        query = text("SELECT 1")
        db.session.execute(query).fetchall()
        connection_status["db_reachable"] = True
    except Exception:
        connection_status["db_reachable"] = False
        connection_status["health_check_successful"] = False
    try:
        redis_client.ping()
        connection_status["redis_reachable"] = True
    except Exception:
        connection_status["redis_reachable"] = False
        connection_status["health_check_successful"] = False
    return connection_status
