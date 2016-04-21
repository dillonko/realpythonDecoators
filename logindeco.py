from functools import wraps
from flask import g, request, redirect, url_for


def login_requiired(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args,*kwargs)
    return deocrated_function

@app.route('/secret')
@login_required
def secret():
    pass

