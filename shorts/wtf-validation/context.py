

from models import User, Role
from app import app, dbsession


@app.shell_context_processor
def make_shell_context():
    return dict(app=app,
                db=dbsession,
                User=User,
                Role=Role
                )
