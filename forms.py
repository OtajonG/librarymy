from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Optional

class AddBookForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    language = StringField('Language', validators=[Optional()])  # Optional
    publication_year = IntegerField('Publication Year', validators=[Optional()])  # Optional
    submit = SubmitField('Add Book')

class SearchBooksForm(FlaskForm):
    query = StringField('Search Query', validators=[DataRequired()])
    language = StringField('Language', validators=[Optional()])  # Now optional
    publication_year = IntegerField('Publication Year', validators=[Optional()])  # Now optional
    submit = SubmitField('Search')