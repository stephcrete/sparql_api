# app.py

from flask import render_template, request
import connexion
import config, sparql_query_templates, sparql_functions
from OpenSSL import SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.minimum_version = ssl.TLSVersion.TLSv1_3
context.maximum_version = ssl.TLSVersion.TLSv1_3
context.use_privatekey_file('/root/server.key')
context.use_certificate_file('/root/server.crt')

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, ssl_context=context)


