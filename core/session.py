from dataclasses import dataclass
from datetime import datetime


@dataclass
class ConversationSession:

    passenger_language: str | None = None

    operator_language: str = "hi"

    active: bool = False

    last_activity: datetime | None = None

    def start(self, language):

        self.passenger_language = language

        self.active = True

        self.last_activity = datetime.now()

    def update(self):

        self.last_activity = datetime.now()

    def reset(self):

        self.passenger_language = None

        self.active = False

        self.last_activity = None