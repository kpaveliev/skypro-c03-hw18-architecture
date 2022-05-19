from typing import List

from app.dao.model.director import Director
from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO) -> None:
        self.dao = dao

    def get_all(self) -> List[Director]:
        return self.dao.get_all()

    def get_one(self, uid: int) -> Director:
        return self.dao.get_one(uid)
