from setuptools import setup

setup(
    name="weatherScraper",
    version="1.0",
    description="Hourly weather scraper for Dublin city",
    author="Conor Kiy",
    author_email="conorkiy@gmail.com",
    licence = "GPL3",
    install_requires=['requests','sqlalchemy','mysql-connector-python'],
    packages=['weatherScraper'],
    entry_points={
        'console_scripts':['dublin_weather_scraper=weatherScraper.main:main']
        }
    )