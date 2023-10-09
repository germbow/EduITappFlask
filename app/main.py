import sys
import socket
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Hola mundo desde Educacion IT con Flask en un contenedor Docker id: {} con uWSGI / Nginx y Python {} (default)".format(
        socket.gethostname(), version
    )
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)