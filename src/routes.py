from flask import render_template, send_from_directory
import os

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
    
    @self.app.route('/<path:folder>/<path:filename>')
    def serve_file(folder, filename):
        directory = os.path.join(self.app.root_path, 'templates', folder)
        return send_from_directory(directory, filename)
    @self.app.route('/<path:filename>')
    def serve_static_file(filename):
        return render_template(filename)