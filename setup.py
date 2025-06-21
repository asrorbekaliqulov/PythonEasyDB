from setuptools import setup, find_packages

setup(
    name="unidb",
    version="0.1.0",
    author="Asrorbek Aliqulov",
    author_email="your_email@example.com",
    description="Unified interface to access SQLite, PostgreSQL, Redis, and MongoDB with high-level Python API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/asrorbekaliqulov/unidb",  # agar yo'q bo‘lsa, comment qilib qo‘ying
    packages=find_packages(),
    install_requires=[
        "pymongo>=4.0.0",
        "redis>=4.0.0",
        "psycopg2-binary>=2.9.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
    ],
    python_requires=">=3.7",
)
