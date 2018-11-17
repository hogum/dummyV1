
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form[username],
                       request.form[passsword])
            return log_the_user_in(request.form['username'])

        else:
            error = 'Invalid username/password'

    return render_template('login.html', error=error)


# 11 File Uploads

from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')


# Cookies

from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    

from flask import request

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return  resp
