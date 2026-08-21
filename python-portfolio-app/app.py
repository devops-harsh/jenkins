from flask import Flask, render_template

app = Flask(__name__)

SERVICES = {
    "web": {
        "name": "Web Server",
        "status": "Operational",
        "uptime": "99.99%"
    },
    "database": {
        "name": "Database",
        "status": "Operational",
        "uptime": "99.97%"
    },
    "api": {
        "name": "API Gateway",
        "status": "Operational",
        "uptime": "99.95%"
    },
    "storage": {
        "name": "Object Storage",
        "status": "Operational",
        "uptime": "99.99%"
    }
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/web")
def web():
    service = SERVICES["web"]

    return render_template(
        "playlist.html",
        title=service["name"],
        status=service["status"],
        uptime=service["uptime"]
    )


@app.route("/database")
def database():
    service = SERVICES["database"]

    return render_template(
        "playlist.html",
        title=service["name"],
        status=service["status"],
        uptime=service["uptime"]
    )


@app.route("/api")
def api():
    service = SERVICES["api"]

    return render_template(
        "playlist.html",
        title=service["name"],
        status=service["status"],
        uptime=service["uptime"]
    )


@app.route("/storage")
def storage():
    service = SERVICES["storage"]

    return render_template(
        "playlist.html",
        title=service["name"],
        status=service["status"],
        uptime=service["uptime"]
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

unused_variable = "lint-test"