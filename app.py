from flask import Flask
from extensions import db, redis_client, migrate


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("configs.settings")
    app.config.from_pyfile("settings.py", silent=True)
    init_extensions(app)
    return app


def init_extensions(flask_app: Flask) -> None:
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)
    redis_client.init_app(flask_app)

    with flask_app.app_context():
        db.create_all()


def register_routes(flask_app: Flask) -> Flask:
    from api.routes import router
    flask_app.register_blueprint(router)

    return flask_app
