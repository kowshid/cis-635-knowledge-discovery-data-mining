# Project Specification Document

## CIS 635: Data Mining and Knowledge Discovery

### Goal

Analysis and prediction of monthly national park visitation from visitor statistics and daily weather records.

### Team

S M Ahsanul Kabir\
G02587087

------------------

## Problem Statement and Motivation

Park authorities need estimates to plan resources, staffing, shuttle and campground capacity. Surrounding communities
depend on the same seasonal patterns. Much of the visitation is calendar-driven like summer travel, public holidays, but
weather can shift visitation within and between seasons. An unusually snowy spring may delay the season at a mountain
park, while an extreme-heat month may suppress visits to a desert park.

In this project we want to link monthly national park visitation records to station-based daily weather observations for
the same location and period. We want to measure seasonality, long-term trend and find any observable pattern. We want
to find whether weather affects visitation.

## Datasets

### Dataset 1 — NPS Visitor Use Statistics (monthly visitation).

The National Park Service (NPS) Visitor Use Statistics Data Package, 2025
(https://irma.nps.gov/DataStore/Reference/Profile/2317666), published by the NPS Social Science Program through the NPS
DataStore. The database contains monthly visitor statistics for all reporting park units from 1979 through 2025,
including visits, recreation hours, and overnight stays, indexed by park unit and reporting month.

- Format: CSV.
- License: CC0 1.0 public domain dedication.

### Dataset 2 — NOAA GHCN-Daily (daily weather observations).

The Global Historical Climatology Network – Daily
(https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) (GHCNd), maintained
by National Centers for Environmental Information (NCEI) of National Oceanic and Atmospheric Administration (NOAA). It
provides daily station observations of maximum and minimum temperature, precipitation, snowfall, and snow depth,
together with a station inventory giving each station's latitude, longitude, elevation, and the years each variable is
available. The project uses U.S. and U.S.-territory stations matched to park units.

- Format: CSV.
- License: U.S. federal government data in the public domain.

## Dataset Relationship

The datasets are linked through both a geographic and temporal dimension.

- **Geographic link**: each park unit is identified by its four-letter NPS unit code. They are matched to their nearest
  GHCN-Daily station using the park's coordinates and station coordinates.
- **Temporal link**: daily weather is aggregated to calendar months and joined to visitation on (unit code, year,
  month).

The result is a single park-month table in which each row combines the visitation outcome with the weather observed near
that park in the same month. The visitation data alone contains no environmental explanatory variables, and the weather
data alone contains no park or visitor outcome, so the analysis depend on the join.

## Proposed KDD Methods

- **Preprocessing and integration**: Match each park unit to the nearest GHCN station reporting temperature and
  precipitation over the study period. Aggregate daily weather observations into monthly means, totals, and
  threshold-day counts. On the visitation side, distinguish legitimate seasonal-closure zeros from unreported months and
  flag COVID-19 months and federal shutdown months. Handle remaining missing observations appropriately.

- **Feature engineering**: Construct monthly weather aggregates, station-specific calendar-month weather anomalies, and
  static park attributes. Weather anomalies are calculated relative to station-specific monthly climate estimated using
  the training period to avoid temporal leakage.

- **Supervised learning**: To be added.

- **Unsupervised learning**: To be added.

## Feasibility and Scope Justification

All data is public and downloadable without registration. No data collection is involved.

The joined table has approximately 30–40 features. The process is not computationally intensive enough to prevent it
from being run on Google Colab. The plan below aligns with the expected progression of the project as well.

## Preliminary Work Plan

| Course week | Planned work                                                                                            |
|-------------|---------------------------------------------------------------------------------------------------------|
| 4           | Submit specification                                                                                    |
| 5-6         | Download necessary data and packages, missing-data handling, join the data                              |
| 7-8         | Exploratory analysis: distributions, trends, seasonality, weather–visitation correlations; Refine scope |
| 9           | Supervised models (ridge, random forest, gradient boosting)                                             |
| 10-11       | Seasonality profiles - comparison with region, designation, and climate                                 |
| 12          | Consolidate results and figures                                                                         |
| 13          | Draft report draft and presentation                                                                     |
| 14          | Finalize report and notebook and Submit                                                                 |

## 7. Tools and Environment

- Google Colab.
- API requests for NPS API and NCEI downloads.
- Python with pandas and NumPy, scikit-learn, SciPy, matplotlib, and seaborn.
- Google Drive for raw and intermediate files storation.

No tool-change request is required at this moment.

## 8. Expected Challenges and Risks

- **Structural shocks**: COVID-19, government shutdowns, and closures are not ordinary weather effects.
- **Seasonality dominates the signal**: A calendar-only model will already score well, which can make any model look
  strong.
- **Join on location**: The nearest station may lie outside the park, at a different elevation, or have gaps, and one
  station may not represent a very large park.
- **Heterogeneous units**: Monthly visits can range from hundreds to millions. This can result in lack of a common unit.

All these challenges will be addressed with appropriate mitigation techniques as we move forward with the project.
