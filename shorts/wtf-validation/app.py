from flask import Flask, render_template, url_for, redirect, session
from form_validate import Contact

app = Flask(__name__)
app.config.update(
    SECRET_KEY='development key')


@app.route('/form', methods=['GET', 'POST'])
def contact():

    form = Contact()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('contact'))
    return render_template('user.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    app.run(debug=True)
