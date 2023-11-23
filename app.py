# app.py

#from flask import render_template, request
#import connexion
#import config, sparql_query_templates, sparql_functions
from flask import Flask

#app = connexion.App(__name__, specification_dir="./")
#app.add_api("swagger.yml")
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

#if __name__ == "__main__":
#    app.run()


