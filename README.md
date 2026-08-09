# Comparative Analysis of Machine Learning Algorithms for Earthquake Magnitude Classification in Muğla

## 📁 Project Structure

```text
statistical-data-analysis/
│
├── data/
│   └── ...
│
├── notebooks/
│   └── ...
│
├── data_preparation.py # data preparation steps in Python (data import + train-test splitting)
├── earthquake.r        # data import steps in R
├── README.md
└── LICENSE
```

## Description of the Earthquakes Dataset 
- **id**: id of earthquake
- **date**: date of earthquake
- **time**: time of earthquake
- **lat**: latitude of earthquake
- **long**: longitude of earthquake
- **country**: country of earthquake
- **city**: city of earthquake
- **area**: area of earthquake
- **direction**: direction of earthquake
- **dist**: distance of direction in km
- **depth**: depth of earthquake
- **xm**: xm of earthquake
- **md**: md of earthquake
- **richter**: intensity of earthquake (Richter) / local magnitude
- **mw**: mw of earthquake / moment magnitude
- **ms**: ms of earthquake / surface-wave magnitude
- **mb**: mb of earthquake / body-wave magnitude
- **mg**: magnitude class of the earthquake. It is 0 if the magnitude is less than 5, and 1 if the magnitude is 5 or greater. **(Response)**
- **day**: day of the earthquake
- **month**: month of the earthquake
- **year**: year of the earthquake
- **day_diff**: number of days elapsed since the first recorded earthquake
- **dirname**: direction of the earthquake
- **dir**: direction of the earthquake encoded as a numeric variable
