from setuptools import setup, find_packages

setup(
    name="fastapi_backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.109.2",
        "uvicorn==0.27.1",
        "sqlalchemy==2.0.27",
        "psycopg2-binary==2.9.9",
        "python-dotenv==1.0.1",
        "pydantic==2.6.1",
        "python-jose[cryptography]==3.3.0",
        "passlib[bcrypt]==1.7.4",
        "python-multipart==0.0.9",
    ],
) 