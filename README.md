![Asper Logo](https://raw.githubusercontent.com/ddatunashvili/Asper_Framework/master/src/static/images/Asper.png?token=GHSAT0AAAAAACNBZGDJKUQ44GREPSVX4EX6ZPFDLGQ)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ddatunashvili/Asper_Framework/blob/master/license.txt)

[![Discord Chat](https://img.shields.io/discord/448698263508615178.svg)](https://discord.gg/CKhzV7F8nN)

# Asper Framework

Asper is a modern GUI maker framework that seamlessly integrates website rendering for dynamic content in software applications. Developers can effortlessly blend native and web technologies, creating visually appealing software with ergonomic tools.

## How Asper Works

Asper is a framework that enables the creation of desktop applications by leveraging both native code and web technologies. Here's an overview of how it operates:

1. **Component-Based Architecture**: Asper applications are built by assembling various components, each serving a specific purpose or functionality. These components can be created using a combination of native code (such as Python) and web technologies (HTML, CSS, JavaScript).

2. **Integration with Web Frameworks**: Asper integrates seamlessly with popular web frameworks like Flask or Django. This integration allows developers to render existing web applications within the Asper desktop environment.

3. **Web Rendering Engine**: Asper utilizes web rendering engines, such as `QWebEngineView` in PyQt, to display web content within the desktop application. This enables developers to combine the power of web technologies with the familiarity of desktop applications.

4. **Customization and Flexibility**: Asper provides developers with the flexibility to customize components according to their specific requirements. This allows for the creation of rich and interactive user interfaces using both native and web technologies.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from src.main import App

class FullScreenWebApp(QMainWindow):
    def __init__(self, url, flask_app):
        super().__init__()
        self.web_view = QWebEngineView(self)
        self.setCentralWidget(self.web_view)
        self.setWindowTitle("Asper")
        self.setWindowIcon(QIcon("logo.ico"))
        self.showFullScreen()
        self.web_view.load(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows_app = App()
    windows_app.run()
    url = "http://127.0.0.1:8000/"
    window = FullScreenWebApp(url, windows_app)
    sys.exit(app.exec_())
```
## Asper Application Structure
```scss
.
├── .gitignore
├── LICENSE.txt
├── modules/
├── src/
│   ├── style.css
│   └── images/
├── templates/
│   ├── index.html
│   └── about.html
├── app.py
├── linux_runner.sh
├── package.bat
├── win_runner.vbs
└── .git/

```

## Asper Web/Ui Support

* You can build a website and place in templates folder to run on desktop app
* You can write flask website and modify framework codes
* You can build launchers, applications, browsers, website pannels and so on ...