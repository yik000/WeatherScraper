# WeatherScraper

This is a hourly weather scraper Dublin city. It uses the [open weather API](https://openweathermap.org/api).


## Installation  

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install DublinWeatherScraper.

```bash
pip install git+"https://github.com/yik000/WeatherScraper.git"
```


## Usage
Create `dbinfo.py` file in `~/miniconda3/envs/enviroment/bin/DublinWeatherScraper` with database URI, database PASS, database USER, DBNAME and OW_APIKEY.

Run module in the background.

```bash
nohup dublin_weather_scraper &
```

Then:

```bash
echo $! >> scraper_process.pid
```

to store pid of scraper.

***