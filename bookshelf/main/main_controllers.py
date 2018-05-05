from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/books/')
def display_books():
    books = {
        "Learn Python The Hard Way": {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        }
    }

    # passing data to the template
    return render_template("books.html", books=books)