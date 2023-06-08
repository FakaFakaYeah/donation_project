from sqlalchemy import Column, String, Text

from app.core.config import MAX_LENGTH
from app.models.base import CharityProjectAndDonation


class CharityProject(CharityProjectAndDonation):

    name = Column(String(MAX_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)
