from flask import Flask
octo_site = Flask(__name__)

@octo_site.route("/")
def newString():
    return("Octo is vet!")

octo_site.run()
