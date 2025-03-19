from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Optional, Length

class AddBookForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired(), Length(max=20)])
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(max=100)])
    language = StringField('Language', validators=[Optional(), Length(max=50)])  # Optional
    publication_year = IntegerField('Publication Year', validators=[Optional()])  # Optional
    submit = SubmitField('Add Book')

class SearchBooksForm(FlaskForm):
    query = StringField('Search Query', validators=[DataRequired(), Length(max=100)])
    language = StringField('Language', validators=[Optional(), Length(max=50)])  # Optional
    publication_year = IntegerField('Publication Year', validators=[Optional()])  # Optional
    submit = SubmitField('Search')