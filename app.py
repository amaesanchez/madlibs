from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

STORIES = {
    "silly_story": silly_story,
    "excited_story": excited_story
}

@app.get("/")
def homepage():
    """ render dropdown """

    return render_template("input.html", stories=STORIES.keys())


# rename endpoint
@app.get("/questions")
def get_questions():
    """Renders questions template"""
    story = request.args["stories"]

    prompts = STORIES[story].prompts

    return render_template("questions.html", prompts=prompts, story=story)



@app.get("/<story>/results")
def get_results(story):
    """Renders  with user inputs"""
    # how to get story instance here
    user_story = STORIES[story]

    results = user_story.generate(request.args)

    return render_template("results.html", results=results, story=story)
