
from flask import render_template

def setup_routes(self):
    
    @self.app.route('/')
    def index():
        return render_template("index.html")

    @self.app.route('/about')
    def about():
        return render_template("about.html")

    @self.app.route('/quit')
    def quit():
        self.quit_signal.emit()
        return "App quitting..."
    
