from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Optional

class AddBookForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    publisher = StringField('Publisher')
    language = StringField('Language', validators=[Optional()]) # Language is now optional
    publication_year = IntegerField('Publication Year', validators=[Optional()]) # Publication year is now optional.
    submit = SubmitField('Add Book')

class SearchBooksForm(FlaskForm):
    query = StringField('Search Query', validators=[DataRequired()])
    submit = SubmitField('Search')