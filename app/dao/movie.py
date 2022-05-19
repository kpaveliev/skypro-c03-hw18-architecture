from typing import List
from sqlalchemy.orm import Session

from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self) -> List[Movie]:
        return self.session.query(Movie).all()

    def get_one(self, uid) -> Movie:
        return self.session.query(Movie).get(uid)

    def create(self, data: dict) -> Movie:
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, uid: int, data: dict) -> None:
        self.session.query(Movie).filter(Movie.id == uid).update(data)
        self.session.commit()

    def delete(self, uid: int) -> None:
        movie = self.get_one(uid)
        self.session.delete(movie)
        self.session.commit()

    def filter(self, filters: dict) -> List[Movie]:
        movies = self.session.query(Movie)

        if filters['director_id']:
            movies = movies.filter(Movie.director_id == filters['director_id'])
        if filters['genre_id']:
            movies = movies.filter(Movie.genre_id == filters['genre_id'])
        if filters['year']:
            movies = movies.filter(Movie.year == filters['year'])

        return movies.all()

