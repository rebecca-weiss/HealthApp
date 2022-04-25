# HealthApp Data

Data mining project to run analyses and visualize data from the Apple Health app from 1/1/2016 - 4/1/2022
``` 
.gitignore
README.md
app.py
data
   |-- activitysummary.csv
   |-- steps.csv
   |-- workouts.csv
get_steps.py
import_clean.ipynb

```

Data explored first is the activity summary and workout data, but also could do general health (HR, HRV) found in `apple_health_export/all_records.csv` with a lot large data files

## import_clean
Imports XML data, converts to dictionary, cleans columns/data types
* workouts and activity summary data done so far, saved in `data/workouts.csv` and `data/activitysummary.csv`
* As of 4/25/2022: steps data extracted from `all_records.csv` and cleaned using `get_steps.py`


## visualize
* `app.py` ia a plotly / dash interactive dashboard: in progress
* `dataviz.py` is working progress of visualizations (matplotlib, plotly): in progress


[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)







## Author: Rebecca Weiss
[![Connect with me](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rebeccajweiss33/)
