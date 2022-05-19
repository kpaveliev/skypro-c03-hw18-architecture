from typing import List
from sqlalchemy.orm import Session

from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self) -> List[Genre]:
        return self.session.query(Genre).all()

    def get_one(self, uid) -> Genre:
        return self.session.query(Genre).get(uid)
