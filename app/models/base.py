from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, CheckConstraint

from app.core.config import DEFAULT_INVESTED
from app.core.db import Base


class CharityProjectAndDonation(Base):

    __abstract__ = True
    __table_args__ = (
        CheckConstraint(f'full_amount > {DEFAULT_INVESTED}'),
        CheckConstraint('invested_amount <= full_amount')
    )

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=DEFAULT_INVESTED)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
