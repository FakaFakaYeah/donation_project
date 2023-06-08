from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


async def check_duplicate(
        project_name: str,
        session: AsyncSession
) -> None:
    project = await charity_project_crud.get_by_attribute(
        session=session, name=project_name
    )
    if project:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!'
        )


async def check_project_exists(
        project_id: int,
        session: AsyncSession
) -> CharityProject:
    project = await charity_project_crud.get_by_attribute(
        session=session, id=project_id
    )
    if not project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Проект с id = {project_id} не найден!'
        )
    return project


async def check_project_for_update(
        project: CharityProject,
        project_in: CharityProjectUpdate,
) -> None:
    if project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Закрытый проект нельзя редактировать!'
        )
    if project_in.full_amount and project_in.full_amount < project.invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Запрещено менять сумму сбора в меньшую сторону!'
        )


async def check_project_for_delete(
        project: CharityProject
) -> None:
    if project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
