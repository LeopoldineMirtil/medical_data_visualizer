# Medical Data Visualizer

A project from the freeCodeCamp *"Data Analysis with Python"* course, instructions [here](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer). The goal of the project is to manipulate and visualize data by using matplotlib, seaborn and pandas to create two functions that create a categorical plot and a heatmap.


### Data Description
The file 'medical_examination.csv' is the data source for this project and was made available by freeCodeCamp.  The file was compiled from medical examinations. Below is a description of the data values: 


|          Feature 	       |         Variable Type    |     Variable 	    |     Value Type    |
|:------------------------:|:------------------------:|:-----------------:|:-----------------:|
|  Age | 	Objective Feature 	|`age` |	int (days)|
|  Height |	Objective Feature |	`height` |	int (cm)|
| Weight |	Objective Feature 	|`weight` |	float (kg)|
|  Gender |	Objective Feature |	`gender` |	categorical code|
|  Systolic blood pressure 	|Examination Feature 	|`ap_hi` |	int|
|  Diastolic blood pressure |	Examination Feature |	`ap_lo` |	int|
|  Cholesterol |	Examination Feature |	`cholesterol` |	1: normal, 2: above normal, 3: well above normal|
|  Glucose |	Examination Feature |	`gluc` |	1: normal, 2: above normal, 3: well above normal
|  Smoking |	Subjective Feature |	`smoke` |	binary|
|  Alcohol intake |	Subjective Feature |	`alco` |	binary|
|  Physical activity 	|Subjective Feature |	`active` |	binary|
|  Presence or absence of cardiovascular disease |	Target Variable |	`cardio` |	binary|
