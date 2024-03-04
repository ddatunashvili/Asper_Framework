import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from src.main import App


class FullScreenWebApp(QMainWindow):
    def __init__(self, url, flask_app):
        super().__init__()
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        self.setWindowTitle("Asper")
        self.setWindowIcon(QIcon("logo.ico"))
        self.showFullScreen()
        # self.show()# is windowed

        self.web_view.load(QUrl(url))

        self.flask_app = flask_app

    def closeEvent(self, event=None):
        self.flask_app.quit()  # Emit the quit signal to stop the Flask server
        QApplication.quit()  # Close the application

        # Remove __pycache__ folders
        self.remove_pycache_folders()

    def remove_pycache_folders(self):
        # Recursively remove __pycache__ folders
        for root, dirs, files in os.walk(".", topdown=False):
            for name in dirs:
                if name == "__pycache__":
                    pycache_path = os.path.join(root, name)
                    print("Removing:", pycache_path)
                    try:
                        shutil.rmtree(pycache_path)
                    except OSError as e:
                        print(f"Error: {pycache_path} : {e.strerror}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    windows_app = App()
    windows_app.run()

    url = "http://127.0.0.1:8000/"
    window = FullScreenWebApp(url, windows_app)

    # Connect the quit_signal to a method that performs the same action as closeEvent
    windows_app.quit_signal.connect(window.closeEvent)

    sys.exit(app.exec_())
