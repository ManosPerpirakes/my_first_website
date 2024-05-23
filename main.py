from flask import Flask, render_template
import os
os.remove("Database.db")
from sql import *
set_db()
timevar = get_data()[0][0]

def index():
    return render_template("index.html", timevar = timevar)

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder) 
app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    app.run()