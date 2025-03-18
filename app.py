from flask import Flask, render_template, request, redirect, url_for, flash
import database
from forms import AddBookForm, SearchBooksForm
import os

app = Flask(__name__)  # Corrected name variable
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        database.add_book(
            form.isbn.data,
            form.title.data,
            form.author.data,
            form.language.data,
            form.publication_year.data
        )
        flash('Book added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)

@app.route('/search_books', methods=['GET', 'POST'])
def search_books():
    form = SearchBooksForm()
    return render_template('search_books.html', form=form)

@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    form = SearchBooksForm()
    if form.validate_on_submit():
        query = form.query.data
        books = database.search_books(query)
        return render_template('search_results.html', books=books, form=form)
    else:
        return render_template('search_results.html', books=[], form=form) # added else statement.

if __name__ == '__main__':
    app.run(debug=True)

