"""
Service Package
"""

from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Security headers
Talisman(
    app,
    force_https=False,
    content_security_policy=None
)

# CORS policy
CORS(app)

# This must be imported after the Flask app is created
from service import routes  # noqa: E402, F401
from service.common import log_handlers  # noqa: E402

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("S E R V I C E   R U N N I N G".center(70, "*"))
app.logger.info(70 * "*")
