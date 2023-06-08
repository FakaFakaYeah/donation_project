from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import CharityProjectAndDonation


class Donation(CharityProjectAndDonation):

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
