start with uvicorn from root (goit-pyweb-hw-11):

uvicorn fastapi_project.main:app --reload

alembic from root (goit-pyweb-hw-11):

alembic -c fastapi_project/alembic.ini revision --autogenerate -m "Init"

alembic -c fastapi_project/alembic.ini upgrade head