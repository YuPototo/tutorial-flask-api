from src.app import app
from src.db import db


if __name__ == '__main__':
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run()
