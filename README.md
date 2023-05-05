<a name="top"></a>
# Cancer Prevention-Regression Analysis (The African Cancer Institute)
---

> <img align="left" width="25" height="25" src="https://user-images.githubusercontent.com/67068918/228323145-dc1343c4-a9e5-4e15-ae91-8af1bc9898b8.svg"> **Author:** Richard Taracha 

> <img align="left" width="25" height="25" src="https://user-images.githubusercontent.com/67068918/228325498-2a141e3e-3e77-48b0-96ae-cbfffa4ef2b3.svg"> **Date:** 07/02/2021

> <img align="left" width="25" height="25" src="https://user-images.githubusercontent.com/67068918/228318759-abcf91d4-5ddd-4230-aed8-4c8d7f63f8d2.svg"> **Web Application:** <a href="https://cancer-deathrate-regression-analysis.onrender.com" target="_blank">Click Me!</a>

<!-- <img align="right"  width="450" height="350" src="https://user-images.githubusercontent.com/67068918/107158150-3977d700-6999-11eb-9603-63f72f2741a9.png"> -->
<img align="right" width="600" height="338" src="https://user-images.githubusercontent.com/67068918/228472429-c1626ff6-98a6-43bd-b713-d1dcc75fc6e3.gif">

---
</br>


> ### <img align="left" width="25" height="25" src="https://user-images.githubusercontent.com/67068918/228328212-52e66179-e80d-4416-906d-64e401ce7052.svg"> Table of Contents
- [Background Information](#background-information)
- [Understanding The Context](#understanding-the-context)
- [Project Deliverable](#project-deliverable)
- [Recording the Experimental Design](#recording-the-experimental-design)

</br>

---

</br>

> ## <img align="left" width="25" height="25" src="https://user-images.githubusercontent.com/67068918/228328828-3d2fa345-dc76-44c6-a604-5a05aeea636b.svg"> Background Information
The African Cancer Institute at Stellenbosch University aims to contribute to improving cancer prevention (both primary and secondary prevention, including screening), diagnosis and management in Africa. The institute is a coordinating and directive institution for research and training in the field of cancer within the University.
</br>
</br>
Website: https://aci.org.za/

---

> ## <img align="left" width="25" height="25" src="https://user-images.githubusercontent.com/67068918/228329440-1b010e60-3ec5-4d81-b545-ef3991a6eb95.svg"> Understanding The Context

As a Data Scientist working for the institution you have been tasked to identify factors that contribute to the death rate of cancer patients using collected dataset.
In addition, you have also been requested to build a multiple linear regression model to predict the death rate - **"TARGET_deathRate"**. You will be required to check for the assumptions of your model as well as perform k-fold (k=10) cross-validation while challenging your solution.

#### Technologies and Tools: Python, Pandas, Numpy, Matplotlib, Scikit-Learn

<p align="right"><a href="#top">Back to top</a></p>

---

> ## <img align="left" width="25" height="25" src="https://user-images.githubusercontent.com/67068918/228330000-aab764a7-0178-4536-b3f9-50fa169afe63.svg"> Project Deliverable
Deliverable is a Python notebook with the Regression Analysis.
</br>
</br>
**Dataset URL:** https://bit.ly/3gJ5Jad
</br>
**Dataset Glossary Download Link:** https://bit.ly/3gYSst9
</br>

<h4 align="center">Dataset Attributes:</h4>

| Column number | Column Name | Column Type | Description |
| --- | --- | --- | --- |
| 0 | avganncount | decimal | Mean number of reported cases of cancer diagnosed annually (a) |
| 1 | avgdeathsperyear | integer | Mean number of reported mortalities due to cancer (a) |
| 2 | target_deathrate | decimal | Dependent variable. Mean per capita (100,000) cancer mortalities (a) |
| 3 | incidencerate | decimal | Mean per capita (100,000) cancer diagnoses (a) |
| 4 | medincome | integer | Median income per county (b) |
| 5 | popest2015 | integer | Population of county (b) |
| 6 | povertypercent | decimal | Percent of populace in poverty (b) |
| 7 | studypercap | decimal | Per capita number of cancer-related clinical trials per county (a) |
| 8 | binnedinc | string | Median income per capita binned by decile (b) |
| 9 | medianage | decimal | Median age of county residents (b) |
| 10 | medianagemale | decimal | Median age of male county residents (b) |
| 11 | medianagefemale | decimal | Median age of female county residents (b) |
| 12 | geography | string | County name (b) |
| 13 | percentmarried | decimal | Percent of county residents who are married (b) |
| 14 | pctnohs18_24 | decimal | Percent of county residents ages 18-24 highest education attained: less than high school (b) |
| 15 | pcths18_24 | decimal | Percent of county residents ages 18-24 highest education attained: high school diploma (b) |
| 16 | pctsomecol18_24 | decimal | Percent of county residents ages 18-24 highest education attained: some college (b) |
| 17 | pctbachdeg18_24 | decimal | Percent of county residents ages 18-24 highest education attained: bachelor's degree (b) |
| 18 | pcths25_over | decimal | Percent of county residents ages 25 and over highest education attained: high school diploma (b) |
| 19 | pctbachdeg25_over | decimal | Percent of county residents ages 25 and over highest education attained: bachelor's degree (b) |
| 20 | pctemployed16_over | decimal | Percent of county residents ages 16 and over employed (b) |
| 21 | pctunemployed16_over | decimal | Percent of county residents ages 16 and over unemployed (b) |
| 22 | pctprivatecoverage | decimal | Percent of county residents with private health coverage (b) |
| 23 | pctprivatecoveragealone | decimal | Percent of county residents with private health coverage alone (no public assistance) (b) |
| 24 | pctempprivcoverage | decimal | Percent of county residents with employee-provided private health coverage (b) |
| 25 | pctpubliccoverage | decimal | Percent of county residents with government-provided health coverage (b) |
| 26 | pctpubliccoveragealone | decimal | Percent of county residents with government-provided health coverage alone (b) |
| 27 | pctwhite | decimal | Percent of county residents who identify as White (b) |
| 28 | pctblack | decimal | Percent of county residents who identify as Black (b) |
| 29 | pctasian | decimal | Percent of county residents who identify as Asian (b) |
| 30 | pctotherrace | decimal | Percent of county residents who identify in a category which is not White, Black, or Asian (b) |
| 31 | pctmarriedhouseholds | decimal | Percent of married households (b) |
| 32 | birthrate | decimal | Number of live births relative to number of women in county (b) |


**NB:** These dataset provided was aggregated from a number of sources including the American Community Survey (census.gov), clinicaltrials.gov, and cancer.gov.

<p align="right"><a href="#top">Back to top</a></p>

---

> ## <img align="left" width="25" height="25" src="https://user-images.githubusercontent.com/67068918/228331342-873c97d4-48bf-49e6-992e-788202af2cd3.svg"> Recording the Experimental Design
| Step | Description |
| --- | --- |
| 1 | Load dataset and libraries. |
| 2 | Clean dataset. |
| 3 | Carry out data analysis. |
| 4 | Carry out data modeling. |
| 5 | Summarize findings. |
| 6 | Provide recommendations. |
| 7 | Challenge the solution. |

While performing model selection/diagnosis, I performed the following steps in an effort to check for the following assumptions:

| Assumption | Description |
| --- | --- |
| Assess the linearity of the model (parameters) | Check if the relationship between the independent and dependent variables is linear and the model coefficients are constant. |
| Assess heteroskedasticity | Check if the variance of the residuals is constant across different levels of the predicted values. |
| Assess the normality of residual distribution | Check if the residuals are normally distributed around zero. |
| Assess multicollinearity | Check if the independent variables are highly correlated with each other. |


<p align="right"><a href="#top">Back to top</a></p>

---

<h3 align="center">Made with ❤️ by Richard Taracha</h3>