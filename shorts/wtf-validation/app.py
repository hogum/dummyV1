from flask import Flask, render_template
from form_validate import Contact

app = Flask(__name__)
app.config.update(
    SECRET_KEY='development key')


@app.route('/form', methods=['GET', 'POST'])
def contact():
    name = ''
    form = Contact()
    if form.validate_on_submit():
        name = form.name.data
        # return render_template('form_success.html', form=form, name=name)
    return render_template('user.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)
