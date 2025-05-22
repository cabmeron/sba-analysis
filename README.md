# sba-award-json

## [Streamlit APP (WIP)](https://sba-analysis.streamlit.app/)

## SBA: Small Business Administration
### an independent agency of the United States government that provides support to entrepreneurs and small businesses
##### [SBIR: Small Business Innovation Research](https://www.sbir.gov/)
##### [STTR: Small Business Technology Transfer](https://www.sbir.gov/tutorials/program-basics/tutorial-3#)

## Data Source:
> (Award History Data)[https://www.sbir.gov/awards]

## How to run
> 1) run git clone https://github.com/cabmeron/sba-analysis
> 2) run pip install ./requirements.txt
> 3) run python main.py`

## Data Organization


```json "COVALENT LLC": [
              {
                     "py/object": "models.Award",
                     "pi": {
                            "py/object": "models.PI",
                            "name": "Martin  Edelstein",
                            "phone": "4156086139",
                            "email": "martin@covalent.science",
                            "education_level": "Unknown"
                     },
                     "phase": "Phase I",
                     "agency": "Department of Energy",
                     "program": "SBIR",
                     "topic_code": "C58-12b",
                     "award_title": "Atomic Precision in Gas Separations",
                     "award_year": 2024,
                     "award_amount": 199980.0
              },
              {
                     "py/object": "models.Award",
                     "pi": {
                            "py/object": "models.PI",
                            "name": "Martin  Edelstein",
                            "phone": "(650) 486-1192",
                            "email": "martin@covalent.to",
                            "education_level": "Unknown"
                     },
                     "phase": "Phase I",
                     "agency": "Department of Energy",
                     "program": "SBIR",
                     "topic_code": "07a",
                     "award_title": "High Yield, Atomically Precise Chemical Activation",
                     "award_year": 2018,
                     "award_amount": 224838.0
              },
              {
                     "py/object": "models.Award",
                     "pi": {
                            "py/object": "models.PI",
                            "name": "Martin  Edelstein",
                            "phone": "(650) 486-1192",
                            "email": "martin@covalent.to",
                            "education_level": "Unknown"
                     },
                     "phase": "Phase I",
                     "agency": "Department of Energy",
                     "program": "SBIR",
                     "topic_code": "15a",
                     "award_title": "Nanomembrane Interactive Forward Osmosis (FO) Polymers for Desalination and Remediation",
                     "award_year": 2017,
                     "award_amount": 150000.0
              },
```
![UML](https://github.com/cabmeron/sba-award-json/blob/main/out/uml_src/models/models.png)
