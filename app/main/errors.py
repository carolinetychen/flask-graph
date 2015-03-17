from flask import reder_template
from . import main


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return renter_template('500.html'), 500
