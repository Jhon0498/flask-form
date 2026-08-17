from flask import render_template, session, redirect, url_for, flash
from forms import NameForm


def registrar_rotas(app):

    @app.route('/', methods=['GET', 'POST'])
    def index():

        form = NameForm()

        if form.validate_on_submit():
            #Permite manter o nome entre uma requisção e outra
            old_name = session.get('name')
            #Se o nome for diferente do anterior prossegue com a informação abaixo
            if old_name is not None and old_name != form.name.data:
                flash('Looks like you have changed your name!')

            session['name'] = form.name.data

            return redirect(url_for('index'))

        return render_template(
            'index.html',
            form=form,
            name=session.get('name')
        )