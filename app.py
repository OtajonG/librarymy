from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import database  # Ensure this handles database operations correctly
from forms import AddBookForm, SearchBooksForm
import os
import fitz  # PyMuPDF for PDF processing

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


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
        pdf_file = form.pdf_path.data  # Accessing the file using form.pdf_path

        pdf_path = None
        if pdf_file and pdf_file.filename.endswith(".pdf"):
            filename = os.path.join(app.config["UPLOAD_FOLDER"], pdf_file.filename)
            pdf_file.save(filename)
            pdf_path = os.path.relpath(filename, "static")

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


@app.route("/search_books")
def search_books():
    return render_template("search_books.html")


@app.route("/list_pdfs")
def list_pdfs():
    """Returns a JSON list of all PDF filenames in the upload folder."""
    pdfs = [f for f in os.listdir(app.config["UPLOAD_FOLDER"]) if f.endswith(".pdf")]
    return jsonify(pdfs)


@app.route("/search_pdf_text", methods=["POST"])
def search_pdf_text():
    """Searches the content of all uploaded PDFs for a given query."""
    data = request.get_json()
    query = data.get("query", "").lower()
    matching_pdfs = []

    for filename in os.listdir(app.config["UPLOAD_FOLDER"]):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            try:
                with fitz.open(pdf_path) as doc:
                    for page in doc:
                        text = page.get_text().lower()
                        if query in text:
                            matching_pdfs.append(filename)
                            break  # Found in this PDF, move to the next
            except Exception as e:
                print(f"Error reading PDF {filename}: {e}")

    return jsonify(matching_pdfs)


if __name__ == "__main__":
    app.run(debug=True)
