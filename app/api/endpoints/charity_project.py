from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_duplicate, check_project_exists, check_project_for_update,
    check_project_for_delete
)
from app.core import current_superuser, get_async_session
from app.crud import charity_project_crud, donation_crud
from app.schemas import (
    CharityProjectDB, CharityProjectCreate, CharityProjectUpdate
)
from app.services import investing

router = APIRouter()


@router.get(
    '/',
    summary='Получение всех проектов',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True
)
async def get_all_charity_project(
        session: AsyncSession = Depends(get_async_session)
) -> List[CharityProjectDB]:
    objs = await charity_project_crud.get_all(session)
    return objs


@router.post(
    '/',
    summary='Создать благотворительный проект',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def create_charity_project(
        project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
) -> CharityProjectDB:
    """
    Создание благотворительного проекта

    - **name**: имя
    - **description** описание
    - **full_amount** общая сумма сбора
    """

    await check_duplicate(project.name, session)
    project = await charity_project_crud.create(project, session)
    sources = await donation_crud.get_all_open(session)
    if sources:
        investing(target=project, sources=sources)
    await session.commit()
    await session.refresh(project)
    return project


@router.patch(
    '/{project_id}',
    summary='Обновить благотворительный проект',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def update_charity_project(
        project_id: int,
        project_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session)
) -> CharityProjectDB:
    """
    Обновление благотворительного проекта

    - **name**: имя (опционально)
    - **description** описание (опционально)
    - **full_amount** общая сумма сбора (опционально)
    """

    project = await check_project_exists(
        project_id=project_id, session=session
    )
    if project_in.name:
        await check_duplicate(project_name=project_in.name, session=session)
    await check_project_for_update(project=project, project_in=project_in)
    project = await charity_project_crud.update(
        obj=project, obj_in=project_in, session=session
    )
    return project


@router.delete(
    '/{project_id}',
    summary='Удалить благотворительный проект',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def remove_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session)
) -> CharityProjectDB:

    project = await check_project_exists(
        project_id=project_id, session=session
    )
    await check_project_for_delete(project=project)
    await charity_project_crud.remove(obj=project, session=session)
    return project
