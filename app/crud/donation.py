from app.models import Donation
from .base import CRUDBase


donation_crud = CRUDBase(Donation)
