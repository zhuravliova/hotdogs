from flask import Flask

from config import DevConfig
from extensions import migrate, db
from views import HotDogView, HotDogsView, IndexView, CreateHotDogView, EditHotDogView, DeleteHotDogView


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    load_models()
    register_urls(app)

    return app


def load_models():
    import models


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)


def register_urls(app: Flask):
    app.add_url_rule('/', view_func=IndexView.as_view('index'))
    app.add_url_rule('/hotdogs/', view_func=HotDogsView.as_view('hotdogs'))
    app.add_url_rule('/hotdog/<pk>/', view_func=HotDogView.as_view('hotdog'))
    app.add_url_rule('/hotdogs/create/', view_func=CreateHotDogView.as_view('create'))
    app.add_url_rule('/hotdog/<pk>/edit/', view_func=EditHotDogView.as_view('edit'))
    app.add_url_rule('/hotdog/<pk>/delete/', view_func=DeleteHotDogView.as_view('delete'))


if __name__ == '__main__':
    create_app().run()
