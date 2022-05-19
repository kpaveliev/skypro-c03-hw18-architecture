from typing import List

from app.dao.model.genre import Genre
from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO) -> None:
        self.dao = dao

    def get_all(self) -> List[Genre]:
        return self.dao.get_all()

    def get_one(self, uid: int) -> Genre:
        return self.dao.get_one(uid)
