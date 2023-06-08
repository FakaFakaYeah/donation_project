from datetime import datetime
from typing import Union, List

from app.models import Donation, CharityProject


def close_obj(
        obj: Union[Donation, CharityProject]
) -> None:
    obj.close_date = datetime.now()
    obj.fully_invested = True


def investing(
    target: Union[CharityProject, Donation],
    sources: List[Union[CharityProject, Donation]]
) -> None:
    can_invest = target.full_amount
    for source in sources:
        can_source_invest = source.full_amount - source.invested_amount
        invest = min(can_invest, can_source_invest)
        source.invested_amount += invest
        target.invested_amount += invest
        can_invest -= invest

        if source.full_amount == source.invested_amount:
            close_obj(source)

        if not can_invest:
            close_obj(target)
            break
