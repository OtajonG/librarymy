from flask import Flask, render_template, request, redirect, url_for
import database
from forms import AddBookForm, SearchBooksForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        database.add_book(form.isbn.data, form.title.data, form.author.data, form.language.data, form.publication_year.data)  # Corrected function call
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)

@app.route('/search_books', methods=['GET', 'POST'])
def search_books():
    form = SearchBooksForm()
    return render_template('search_books.html', form=form)

@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    form = SearchBooksForm()
    query = request.args.get('query')
    books = database.search_books(query)
    return render_template('search_results.html', books=books, form=form)

if __name__ == '__main__':
    app.run(debug=True)

