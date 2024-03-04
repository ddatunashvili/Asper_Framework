import threading
from flask import Flask
from flask_cors import CORS
from werkzeug.serving import make_server
from PyQt5.QtCore import QObject, pyqtSignal
from .routes import setup_routes

class FlaskThread(threading.Thread):
    def __init__(self, app, host='127.0.0.1', port=8000):
        threading.Thread.__init__(self)
        self.app = app
        self.host = host
        self.port = port
        self.server = make_server(self.host, self.port, self.app)

    def run(self):
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()  # Close the server socket


class App(QObject):
    quit_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.app = Flask(__name__)
        CORS(self.app)  # Enable CORS for all routes
        self.flask_thread = FlaskThread(self.app)
        
        setup_routes(self)
       
    def run(self):
        self.flask_thread.start()

    def stop(self):
        self.flask_thread.stop()
        self.flask_thread.join()  # Wait for Flask thread to finish

    def run_in_main_thread(self):
        self.run()

    def quit(self):
        self.stop()
        self.flask_thread.stop()

if __name__ == "__main__":
    app = App()
    app.run_in_main_thread()
