"""A madlib game that compliments its users."""

from random import choice
import re

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/game")
def show_madlib_form():
    """Provide entry fields for the user to enter a name, color, noun, & adjective to play Madlibs"""

    """If the player opted not to play, send them to a goodby page"""
    
    wants_to_play = request.args.get("play_or_not")

    if wants_to_play == "yes":
        return render_template("game.html", play_or_not=wants_to_play)
    else:
        return render_template("goodbye.html", play_or_not=wants_to_play)

    
@app.route("/madlib")
def show_madlib():
    """Display the Madlib story that contains the user's entries from /game"""

    madperson = request.args.get("madperson")

    madcolor = request.args.get("color")

    madnoun = request.args.get("noun")

    madadj = request.args.get("adj")

    return render_template("madlib.html", displayed_person=madperson, displayed_color=madcolor, displayed_noun=madnoun, displayed_adj=madadj)


@app.route("/goodbye")
def say_goodbye():
    """For visitors that chose not to play the game, say goodbye"""

    return render_template("goodbye.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)
    
    return render_template("compliment.html", person=player, compliment=compliment)

    


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0", port="5001")
