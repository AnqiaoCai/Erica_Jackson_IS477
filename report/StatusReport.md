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

Before the deadline of the stage 3 status report, we have completed the major components of data cleaning, merging, and exploratory analysis. Our next step is to refine the statistical analysis, strengthen the visualizations, complete the workflow automation, and write the final report.

From Nov 21st to Nov 26th, we will mainly focus on finishing the ongoing work. For data acquisition, data integration, data cleaning, and data analysis, we have finished the scripts. However, we have not finished the documentation describing the steps for each of these parts. Thus, we will focus on finishing the documentation in this period.

From Nov 27th to Nov 30th, we will work on the unfinished artifact parts of the project, including data storage, data quality, workflow automation, reproducibility, and metadata documentation. We will finish both of the scripts and the documentation for these parts.

From Dec 1st to Dec 5th, we will work on writing the README.md, which is the project report. We will finish the writing of the title, contributors, summary, data profile, data quality, findings, future work, and reference. 

On the last two days, we will recheck the report to make sure we have covered all the required components. We will also check the reproducibility of the scripts and files.

## Change compared to the initial project plan:

There are a few changes we made to our original plan based on what we discovered in the analysis. First, the original project plan assumed that most counties would appear in both datasets. However, after we merged both datasets, we found out that more than 1100 rural counties in the COPD dataset didn’t match the EPA air quality data. We are thinking this is because they do not have monitoring stations. 

To reduce bias, Erica and I plan to add a new preprocessing step after the milestone 3 deadline. We will keep all the COPD counties and fill in missing pollution values using state-level averages. This will help us run the statistical models, and we will be transparent about the dataset’s limitations. 
       
## Erica’s contribution:

Erica mainly works on data collection, data acquisition, and data analysis. She got the two CSV files from the official websites and checked their integrity by using SHA-256 (Reference in GitHub: scripts/check_integrity.py). She also worked on the data visualization by checking correlations between pairs of variables and using scatterplots to visualize the relationships. For the status report writing, she finished the writing of updated tasks and her own contribution.

## Jackson’s contribution:

Jackson mainly worked on clearing the COPD and air-quality datasets by fixing the county names, converting text into numbers, and removing invalid rows. He also wrote the code that combines the two datasets using the State and Country columns. These steps are implemented in the data_clean.py and data_integration.py scripts. At the same time, Jackson also works with Erica to check the files are all in a good format. This is because we need to make sure the processed data can be relied on for later analysis and visualization. 