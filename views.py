from flask import render_template, request, abort
from flask.views import MethodView
from models import HotDog
from extensions import db


class IndexView(MethodView):

    def get(self):
        return render_template('index.html')


class CreateHotDogView(MethodView):
    def get(self):
        return render_template('form.html', the_title='Create a new hot dog')

    def post(self):
        item = HotDog(name=request.form['name'], description=request.form['description'])
        db.session.add(item)
        db.session.commit()
        return render_template('result.html', message=f'created hot dog {item.name} with id {item.pk}')


class HotDogsView(MethodView):

    def get(self):
        hotdogs = HotDog.query.all()
        return render_template('hotdogs.html', the_title='List of hot dogs', hotdogs=hotdogs)


class HotDogView(MethodView):

    def get(self, pk):
        item = HotDog.query.filter_by(pk=pk).first()
        if item is None:
            abort(404)
        return render_template('item.html', the_title=item.name, the_desc=item.description, item=item)


class EditHotDogView(MethodView):

    def get(self, pk):
        item = HotDog.query.filter_by(pk=pk).first()
        if item is None:
            abort(404)
        return render_template('form.html', the_title=item.name, name=item.name, description=item.description, item=item)

    def post(self, pk):
        item = HotDog.query.filter_by(pk=pk).first()
        if item is None:
            abort(404)
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.add(item)
        db.session.commit()
        return render_template('result.html', message=f'updated hot dog {item.name} with id {item.pk}')


class DeleteHotDogView(MethodView):
    def get(self, pk):
        item = HotDog.query.filter_by(pk=pk).first()
        if item is None:
            abort(404)
        return render_template('delete.html', the_title='Deleting hot dog', name=item.name, item=item)

    def post(self, pk):
        item = HotDog.query.filter_by(pk=pk).first()
        if item is None:
            abort(404)
        db.session.delete(item)
        db.session.commit()
        return render_template('result.html', message=f'hot dog deleted successfully')
