#!/bin/bash

FILE=./COVID-19
if [ ! -d "$FILE" ]; then
    git clone https://github.com/CSSEGISandData/COVID-19.git
fi


cd COVID-19
git checkout csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
git checkout csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv
git checkout csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv
git pull
sed -i "s/Korea, South/Korea South/g" ./csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
sed -i "s/Korea, South/Korea South/g" ./csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv
sed -i "s/Korea, South/Korea South/g" ./csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv

sed -i "s/Bonaire, Sint Eustatius and Saba/Bonaire Sint Eustatius and Saba/g" ./csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
sed -i "s/Bonaire, Sint Eustatius and Saba/Bonaire Sint Eustatius and Saba/g" ./csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv
sed -i "s/Bonaire, Sint Eustatius and Saba/Bonaire Sint Eustatius and Saba/g" ./csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv


cd ..

mkdir -p reports

python daily_report.py
