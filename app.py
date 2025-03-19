from flask import Flask, render_template, request, redirect, url_for, flash
import database  # Ensure this handles database operations correctly
from forms import AddBookForm, SearchBooksForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
@app.route("/")
def home():
    return "Flask is running!"

# Define the folder to store uploaded PDFs
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        pdf_file = request.files.get('pdf_file')  # Get the uploaded file

        # Save the file if uploaded
        pdf_path = None
        if pdf_file and pdf_file.filename.endswith('.pdf'):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
            pdf_file.save(filename)
            pdf_path = filename  # Store the path in the database

        # Save book details in the database
        database.add_book(
            form.isbn.data,
            form.title.data,
            form.author.data,
            form.language.data,
            form.publication_year.data,
            pdf_path  # Store the PDF path
        )
        flash('Book added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_book.html', form=form)
if __name__ == "__main__":
    app.run(debug=True)