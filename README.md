# Investigation of COVID-19 Clinical Trial Metadata
#### SOURCE: [clinicaltrials.gov](https://clinicaltrials.gov/ct2/results?cond=COVID-19)
Data downloaded January 22, 2021, on which 4,542 studies were returned on a search for 'COVID-19'.

#### CONTENTS:
- **01.** Data Ingestion
- **02.** Exploratory Data Analysis (EDA)
- **03.** Modeling
- **04.** Conclusion
    
#### QUESTIONS:
- What are some potential uses for the densely populated text fields (e.g. detailed_description)?
- How many people are currently enrolled in COVID-19 studies?
- How many COVID-19 studies have been completed to date?
- Can we predict enrollment numbers for COVID-19 studies? If not, what can we potentially predict?

#### CHANGES:
- 03.16.2021 // Moved data conversion functions to data_utils.py script and added this import to the notebook