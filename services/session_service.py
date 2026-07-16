from uuid import uuid4


class SessionService:

    def create_session(self):
        return str(uuid4())