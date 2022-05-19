from typing import List

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO) -> None:
        self.dao = dao

    def get_all(self) -> List[Movie]:
        return self.dao.get_all()

    def get_one(self, uid: int) -> Movie:
        return self.dao.get_one(uid)

    def create(self, data: dict) -> Movie:
        return self.dao.create(data)

    def update(self, uid: int, data: dict) -> None:
        self.dao.update(uid, data)

    def delete(self, uid: int) -> None:
        self.dao.delete(uid)

    def filter(self, filters: dict) -> List[Movie]:
        return self.dao.filter(filters)
