from flask import Flask, render_template, request, redirect, url_for, flash
import database  # Ensure this handles database operations correctly
from forms import AddBookForm, SearchBooksForm
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    UPLOAD_FOLDER = "static/uploads"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    form = AddBookForm()
    if form.validate_on_submit():
        pdf_file = request.files.get("pdf_file")

        pdf_path = None
        if pdf_file and pdf_file.filename.endswith(".pdf"):
            filename = os.path.join(app.config["UPLOAD_FOLDER"], pdf_file.filename)
            pdf_file.save(filename)
            pdf_path = filename

        database.add_book(
            form.isbn.data,
            form.title.data,
            form.author.data,
            form.language.data,
            form.publication_year.data,
            pdf_path,
        )
        flash("Book added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_book.html", form=form)


@app.route("/search_books", methods=["GET", "POST"])
def search_books():
    form = SearchBooksForm()
    books = []  # Initialize books list
    if form.validate_on_submit():
        query = form.query.data
        language = form.language.data
        publication_year = form.publication_year.data

        # Perform database search based on form data
        books = database.search_books(query, language, publication_year)

        return render_template("search_books.html", form=form, books=books)


if __name__ == "__main__":
    app.run(debug=True)
