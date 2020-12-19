from flask import Flask,render_template
import json

app=Flask(__name__)

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route("/")
def hope():
    return render_template("test.html",jsonl=json.loads,length=len)


if __name__=="__main__":
    app.run(debug=True)