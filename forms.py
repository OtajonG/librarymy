from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Optional, Length, ValidationError
import os


def validate_pdf(form, field):
    if field.data:
        filename = field.data.filename
        if not filename.endswith(".pdf"):
            raise ValidationError("Only PDF files are allowed.")


class AddBookForm(FlaskForm):
    isbn = StringField("ISBN", validators=[DataRequired(), Length(max=20)])
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    author = StringField("Author", validators=[DataRequired(), Length(max=100)])
    language = StringField("Language", validators=[Optional(), Length(max=50)])
    publication_year = IntegerField("Publication Year", validators=[Optional()])
    pdf_path = FileField(
        "Upload PDF", validators=[Optional(), validate_pdf]
    )  # Renamed and added validator
    submit = SubmitField("Add Book")


class SearchBooksForm(FlaskForm):
    query = StringField("Search Query", validators=[DataRequired(), Length(max=100)])
    language = StringField("Language", validators=[Optional(), Length(max=50)])
    publication_year = IntegerField("Publication Year", validators=[Optional()])
    submit = SubmitField("Search")
