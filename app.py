from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def homepage():
    """Renders questions template"""
    prompts = silly_story.prompts

    return render_template("questions.html", prompts=prompts)

@app.get("/results")
def get_results():
    """Renders story with user inputs"""
    results = silly_story.generate(request.args)

    return render_template("results.html", results=results)