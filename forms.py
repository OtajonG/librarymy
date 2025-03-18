from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddBookForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    publisher = StringField('Publisher')
    language = StringField('Language')  # Optional for adding
    publication_year = IntegerField('Publication Year')  # Optional for adding
    submit = SubmitField('Add Book')

class SearchBooksForm(FlaskForm):
    query = StringField('Search Query', validators=[DataRequired()])
    language = StringField('Language', validators=[DataRequired()]) # Required for searching
    publication_year = IntegerField('Publication Year', validators=[DataRequired()]) # Required for searching
    submit = SubmitField('Search')