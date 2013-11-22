from flask import Flask, render_template, redirect, g, request, url_for, abort
from flask.ext.babel import Babel


app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Direct babel to use the language defined in the session."""
    return g.get('current_lang', 'en')

@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        if request.view_args['lang_code'] not in ('es', 'en'):
            return abort(404)
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')

@app.route('/')
def root():
    return redirect(url_for('index', lang_code='en'))

@app.route('/<lang_code>')
def index():
    return render_template('index.html')

@app.route('/<lang_code>/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
