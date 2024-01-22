from flask import Flask

from app import create_app, register_routes
from configs.settings import DEBUG

flask_app: Flask = register_routes(create_app())

if __name__ == "__main__":
    # Run App
    app = create_app()
    register_routes(app)
    app.run(debug=DEBUG)
