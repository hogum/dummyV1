from flask import Flask, render_template, url_for, redirect, session
from form_validate import Contact
from flask_migrate import Migrate

from models import User, Role
from base import Base, Session, engine

Base.metadata.create_all(engine)
dbsession = Session()

app = Flask(__name__)
app.config.update(
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:pass@localhost:5432/dummy')


migrate = Migrate(app, dbsession)


@app.route('/form', methods=['GET', 'POST'])
@app.shell_context_processor
def make_shell_context():
    return dict(app=app,
                db=dbsession,
                User=User,
                Role=Role
                )


def contact():

    form = Contact()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data)
        if user is None:
            dbsession.add(user)
            session['exists'] = False
            """
            name_ = session.get('name')
        if name_ != form.name.data:
            flash('Changed your name already?')
        """
        else:
            session['exists'] = True
        session['name'] = form.name.data

        return redirect(url_for('contact'))
    return render_template('user.html',
                           form=form,
                           name=session.get('name'),
                           exists=session.get('exists', False))


if __name__ == '__main__':
    app.run(debug=True)
