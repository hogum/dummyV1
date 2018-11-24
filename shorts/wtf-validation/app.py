from flask import Flask, render_template, url_for, redirect, session, flash
from form_validate import Contact
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models import User, Role
from base import Base, Session, engine

Base.metadata.create_all(engine)
dbsession = Session()

app = Flask(__name__)
app.config.update(
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:pass@localhost:5432/dummy')

db = SQLAlchemy(app)

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app,
                db=dbsession,
                User=User,
                Role=Role
                )


@app.route('/form', methods=['GET', 'POST'])
def contact():

    form = Contact()
    if form.validate_on_submit():
        user = dbsession.query(User).filter(
            User.name == form.name.data).first()
        if user is None:
            user_name = form.name.data
            user = User(user_name)
            dbsession.add(user)
            dbsession.commit()
            session['exists'] = False

        else:
            session['exists'] = True
            name_ = user.name
            if name_ != form.name.data:
                flash('Changed your name already?')
        session['name'] = form.name.data

        return redirect(url_for('contact'))
    return render_template('user.html',
                           form=form,
                           name=session.get('name'),
                           exists=session.get('exists', False))


if __name__ == '__main__':
    app.run(debug=True)
