# Milestone 3: Interim Status Report

##Air Quality and COPD Prevalence Analysis

## Update on tasks described in the project plan:

In milestone 3, we mainly focus on the following four parts of the project, including data collection, data cleaning, data integration, and data visualization. This report will summarize the progress made by Jackson and Erica. We will introduce our progress in each of the project components. 

## Update on Tasks Described in the Project Plan

During this milestone, we completed the full data preparation pipeline. We conducted the first round of the analysis. 

## 1. Data collection and acquisition: 

We got the COPD dataset from the Disease Control and Prevention (CDC) website. The air quality dataset is from the Environmental Protection Agency(EPA) website. They are both CSV files that can be downloaded directly from the two websites. 

1. COPD (CDC): https://www.cdc.gov/copd/php/case-reporting/county-level-estimates-in-copd.html You need to scroll down the page and navigate to the Data Table section to download the CSV file. 

2. Air quality (EPA): https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual You have to scroll down the page and navigate to the annual_aqi_by_country_2021.zip. Then you will find the CSV file.

After getting the two CSV files, we start checking the integrity of the data by using SHA-256. (Reference in GitHub: scripts/check_integrity.py)

## 2. Data Cleaning:

Before we merged both datasets, we used several data cleaning techniques. First, we did the text normalization by removing the text “ County” from all county names. The purpose of doing this is to ensure we can integrate the datasets on county names without extra “ County” wording. Second, we did the data conversion with coercion to convert the text values to numeric data. Third, we remove the invalid and missing data by using the dropna() function. (Reference in GitHub: scripts/data_clean.py, cleaned datasets: Data/cleaned/air_clean.csv and Data /cleaned/copd_clean.csv)
 
## 3. Data Integration：

After we cleaned both datasets, we merged the two datasets by inner joining them on the State and County columns. The merged dataset has both COPD data and air quality data. 
(Reference in GitHub: scripts/data_integration.py, merged dataset: Data/merged_data/merged_dataset.py)

## 4. Data Analysis and Visualization:

Before doing the data analysis and visualization, we first check the number of missing values and data types to make sure there are no explicit and implicit missing values. After checking the missing values, we start exploring the dataset. We calculated the correlation between the variables to find out the relationships between pairs of variables. We built an OLS regression model and printed out the summary to find how each variable influences the COPD prevalence. In addition, we drew four scatterplots with regression lines to visualize the relationship between COPD prevalence and median AQI, Days Ozone, Days PM2.5, Days NO2, and Days PM10. (Reference in GitHub: workflow.ipynb)

## 5. Requirement txt:

We also created a requirements.txt file that contains the Python packages and their version numbers. This helps the grading team and future data scientists to recreate the same environment for running the scripts and notebooks. 

## Updated timeline:


## Change compared to the initial project plan:


## Erica’s contribution:

Erica mainly works on data collection, data acquisition, and data analysis. She got the two CSV files from the official websites and checked their integrity by using SHA-256 (Reference in GitHub: scripts/check_integrity.py). She also worked on the data visualization by checking correlations between pairs of variables and using scatterplots to visualize the relationships. For the status report writing, she finished the writing of updated tasks and her own contribution.

## Jackson’s contribution:

