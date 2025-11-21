# Project Plan: Air Quality and COPD Prevalence Analysis

## Overview
This project will study how air quality relates to Chronic Obstructive Pulmonary Disease (COPD) in different counties across the United States. We aim to discover whether areas with higher levels of pollution are more likely to have higher percentages of COPD patients. The goal of the project is to find out the relationship between air quality and COPD, which provides insights for COPD medical care and prevention strategies. It will also raise people’s awareness of COPD and environmental issues.

## Research Questions 
Our research focuses on two main questions. First, do counties with worse air quality have a higher percentage of COPD patients? Second, which kind of air pollutant is most closely linked to COPD?

## Team
Our team is called Double Vision. Teammates are Jackson and Erica. We will collaborate on all components of the project. Both of us will do 50% of the technical work and 50% of the writing.

Jackson will write Python code to clean the datasets and combine them by matching counties from both sources. He will also help with organizing the project and setting up the workflow. In the report, he will describe the technical process, including the data lifecycle, data integration, data cleaning, data storage, and the setup of the workflow.

Erica will work on the statistical analysis and create visualizations to show the results. She will also write about the project background, ethical data handling, and how the results were interpreted. Erica will also help document the data quality, reproducibility, and metadata for each data source.

## Datasets
This project will use two datasets: one from the Centers for Disease Control and Prevention (CDC) and one from the Environmental Protection Agency (EPA).

Here are the links:
COPD (CDC): https://www.cdc.gov/copd/php/case-reporting/county-level-estimates-in-copd.html

Air qulity (EPA): https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual 

The EPA dataset shows air quality levels in U.S. counties. It includes yearly pollutant levels like PM2.5, ozone, and nitrogen dioxide. This data comes from monitoring stations in each county. The indexes of different air pollutants show the air quality of each of the counties.

The CDC dataset shows how COPD prevalence spread in each county. It includes the percentage of adults diagnosed with COPD. It also includes extra statistical details, like confidence intervals and rankings that compare counties to each other.

We will first clean and organize both datasets. Then we will match the counties that appear in both. After that, we will combine them into one dataset. This will let us study the relationship between air pollution and COPD rates.


## Timeline 
We will follow the project deadlines provided by the course instruction team. Our first task is to complete and submit the project plan by October 14, 2025. Before this deadline, Jackson and Erica had a meeting to discuss the topic of the project and decided to do the environment and disease. We also discussed each one’s roles and responsibilities to split the project work.

After the project plan is submitted, we will begin collecting and cleaning both datasets. Erica will investigate the data lifecycle and ethical constraints first. Jackson will focus on writing Python code to preprocess the data, including checking for missing values. We will then work together to combine the datasets by matching counties from both sources.

At the beginning of November, we will begin our initial analysis. Erica will lead the statistical testing and create charts to present the data. Jackson will support this by preparing the merged dataset and setting up automation for reproducibility. During this time, we will also start writing the interim status report, which is due on November 11, 2025.

After submitting the status report, we will move on to deeper analysis and finalize our visualizations. Jackson will review and refine the workflow, while Erica will update documentation and prepare for the final writing. Both of us will write and edit different parts of the final report.

During the last two weeks of the project, we will complete the final report, organize all code files, and prepare our submission to GitHub. Jackson will ensure all scripts run properly to ensure reproducibility, and Erica will review the documentation and metadata. We will submit the final project on GitHub by December 10, 2025.

## Constraints
There are a few constraints we may find while working on this project. One constraint is that not every county in the United States has air quality data. The EPA dataset only includes counties with monitoring stations, so some counties in the COPD dataset may not have matching records. This could make the combined dataset smaller than expected, and it may affect the variety or size of our final results.

We may also need to filter or drop some rows if the data is incomplete. The air quality dataset includes many missing values because some of the air pollutants are not measured in some of the counties. Thus, we need to focus on pollutants with enough data, including PM2.5 and Ozone 4.

We also expect some differences in data formats, such as different expressions of county names, different expressions of recorded dates, or how missing values are shown differently. These formatting issues may cause executable errors during the cleaning process, so we need to pay attention to them.

## Gaps
There are gaps we need to figure out or think about for the project. The first gap is to find the best measure to determine the relationship between air quality and COPD. We are not sure whether a simple correlation analysis is enough, such as drawing scatterplots. We are thinking about trying more advanced machine learning models like K-Nearest Neighbors and other regression models. We will make a final decision once we work more closely with the data and finish the initial exploratory data analysis.

Another gap is figuring out the best way to show our results. We plan to include charts and maps, but we are still deciding which ones will be the easiest to understand. We want to make sure our visuals are easy to read and convey our goal to the audience well. We need to make sure our visualizations include enough details or explanations, allowing the audience to understand the results.
