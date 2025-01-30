from setuptools import setup, find_packages

setup(
    name="monorepo",
    version="0.1.0", 
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.75.0",
        "sqlalchemy>=2.0.0",
        "pydantic>=1.8.0",
        "pytest>=6.0",
        "psycopg2-binary",
        "alembic>=1.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.14.0",
        ],
    },
    tests_require=["pytest"],
    include_package_data=True,
    python_requires=">=3.10",
)
