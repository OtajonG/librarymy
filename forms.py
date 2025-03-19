from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Optional, Length

class AddBookForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired(), Length(max=20)])
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(max=100)])
    language = StringField('Language', validators=[Optional(), Length(max=50)])
    publication_year = IntegerField('Publication Year', validators=[Optional()])
    pdf_file = FileField('Upload PDF')  # Added field for uploading PDF
    submit = SubmitField('Add Book')

class SearchBooksForm(FlaskForm):
    query = StringField('Search Query', validators=[DataRequired(), Length(max=100)])
    language = StringField('Language', validators=[Optional(), Length(max=50)])
    publication_year = IntegerField('Publication Year', validators=[Optional()])
    submit = SubmitField('Search')