from flask import Flask
from router.routes import bp, limiter
import os

app = Flask(__name__)

limiter.init_app(app)
app.register_blueprint(bp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
