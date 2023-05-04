from flask import render_template, redirect, url_for

from . import app, db
from .forms import NewsForm, FeedbackForm
from .models import Category, News, Feedback


@app.route('/')
def main_page():
    categories = Category.query.all()
    news_list = News.query.all()
    return render_template('index.html', news=news_list, categories=categories)


@app.route('/news_detail/<int:new_id>')
def news_detail_page(new_id):
    categories = Category.query.all()
    new = News.query.get(new_id)
    if new:
        return render_template('news_detail.html', new=new, categories=categories)
    return render_template('news_detail.html', new={'title': 'Данной новости ещё не существует',
                                                    'text': ''}, categories=categories)


@app.route('/add_new', methods=['GET', 'POST'])
def add_new():
    categories = Category.query.all()
    form = NewsForm()
    if form.validate_on_submit():
        new = News()
        new.title = form.title.data
        new.text = form.text.data
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('news_detail_page', new_id=new.id))
    return render_template('add_new.html', form=form, categories=categories)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback_page():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback()
        feedback.name = form.name.data
        feedback.text = form.text.data
        feedback.email = form.email.data
        feedback.email = form.rating.data
        db.session.add(feedback)
        db.session.commit()
        return redirect('/')
    return render_template('feedback.html', form=form)


@app.route('/category/<int:category_id>')
def category_page(category_id):
    category = Category.query.get(category_id)
    news_list = News.query.filter(News.category_id == category_id).all()
    return render_template('category.html', news=news_list, category=category)
