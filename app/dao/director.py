from typing import List
from sqlalchemy.orm import Session

from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self) -> List[Director]:
        return self.session.query(Director).all()

    def get_one(self, uid) -> Director:
        return self.session.query(Director).get(uid)
