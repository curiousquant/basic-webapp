from flask import Flask, render_template

from connect import connect, selectItems
app = Flask(__name__, template_folder='static')


@app.route("/")
def main():
    con = connect()
    data = selectItems(con)
    
    return render_template("index.html",data=data) 

if __name__ == "__main__":
    app.run()