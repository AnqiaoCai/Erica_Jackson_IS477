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