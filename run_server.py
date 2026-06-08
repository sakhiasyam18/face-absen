from flask import (
    Flask,
    render_template
)

from api.attendance_api import (
    attendance_api
)

from api.register_api import (
    register_api
)

from api.recognition_api import (
    recognition_api
)

app = Flask(__name__)

app.register_blueprint(
    attendance_api
)

app.register_blueprint(
    register_api
)

app.register_blueprint(
    recognition_api
)

@app.route("/")
def dashboard():

    return render_template(
        "dashboard.html"
    )


@app.route("/register")
def register_page():

    return render_template(
        "register.html"
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )