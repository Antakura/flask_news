from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

from .models import Category


def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class NewsForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[DataRequired(message='Поле не должно быть пустым'),
                    Length(max=127, message='Длина заголовка не должна превышать 127 символов')])
    text = TextAreaField(
        'Текст',
        validators=[DataRequired(message='Поле не должно быть пустым'),
                    Length(max=65535, message='Слишком длинное содержание')])
    submit = SubmitField('Добавить')


class FeedbackForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[DataRequired(message='Поле не должно быть пустым'),
                    Length(max=255, message='Длина заголовка не должна превышать 255 символов')])
    text = TextAreaField(
        'Текст отзыва',
        validators=[DataRequired(message='Поле не должно быть пустым')])
    email = StringField(
        'Ваш email',
        validators=[Length(max=64, message='Длина заголовка не должна превышать 64 символа')])
    rating = SelectField(
        'Ваша оценка?',
        choices=list(range(1, 6))
    )
    submit = SubmitField('Добавить')
