from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from sqlalchemy import desc
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MOVIES.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db = SQLAlchemy(app)

API_endpoint = "https://api.themoviedb.org/3/search/movie"
API_key = "45c732a76fc75cb6a35b7547f4cc2097"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    
class EditRating(FlaskForm):
    new_rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    new_review = StringField("Your review", validators=[DataRequired()])
    submit = SubmitField("Done")
    
class AddMovie(FlaskForm):
    NewTitle = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    movies = Movie.query.order_by(desc(Movie.rating)).all()
    for i, movie in enumerate(movies):
        movie.ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title_search = form.NewTitle.data
        
        API_parameters_for_movies = {
            "api_key": API_key,
            "query": movie_title_search,
            "language": "en-US"
            }
                    
        response = requests.get(API_endpoint, params=API_parameters_for_movies)
        response.raise_for_status()
        
        movies = response.json()["results"]
        
        return render_template("select.html", movies=movies)
            
    return render_template("add.html", form=form)

@app.route("/add-particular-movie/<int:movie_id>", methods=["GET", "POST"])
def add_particular_movie(movie_id):

    API_parameters_for_movie = {
        "api_key": API_key,
        "language": "en-US"
    }

    response = requests.get(f"{'https://api.themoviedb.org/3/movie'}/{movie_id}", params=API_parameters_for_movie)
    response.raise_for_status()

    movie_data = response.json()

    new_movie = Movie(
        title=movie_data["title"],
        year=int(movie_data["release_date"][:4]),
        description=movie_data["overview"],
        rating=0,
        ranking=0,
        review="",
        img_url=f"https://image.tmdb.org/t/p/w500/{movie_data['poster_path']}"
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', movie_id=new_movie.id))
    

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditRating()
    if form.validate_on_submit():
        new_rating = form.new_rating.data
        new_review = form.new_review.data
        movie_to_edit = Movie.query.get(movie_id)
        movie_to_edit.rating = new_rating
        movie_to_edit.review = new_review
        db.session.commit()
        
        return redirect(url_for('home'))    

    return render_template("edit.html", form=form)

@app.route("/delete/<int:movie_id>'", methods=["GET", "POST"])
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
