# TCGA-PAAD Survival Modeling

Survival prediction modeling in pancreatic cancer using clinical data from TCGA-PAAD.

## Project Overview

This project reanalyzes TCGA-PAAD clinical data (185 patients) to identify prognostic factors and develop individualized survival prediction models.

The study integrates traditional survival analysis techniques with neural survival modeling approaches to compare statistical and deep learning-based methods.

## Objectives

- Identify clinical prognostic factors in pancreatic cancer  
- Perform survival analysis using Kaplan–Meier and Cox regression  
- Develop and compare statistical and neural survival models  
- Evaluate predictive performance using the Concordance Index (C-index)  
- Assess model interpretability using SHAP  

## Methodology

1. Data extraction and preprocessing of clinical datasets  
2. Exploratory Data Analysis (EDA)  
3. Survival analysis (Kaplan–Meier curves and Cox regression)  
4. Neural survival modeling using a Cox-based MLP implemented with PyCox and PyTorch. 
5. Model evaluation and interpretability analysis  

## Results

- Competitive survival prediction performance  
- C-index ≈ 0.6–0.7  
- Identification of clinically relevant prognostic factors  
- Interpretable feature contributions via SHAP  

## Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- Lifelines  
- PyTorch / PyCox  
- SHAP  
- Matplotlib / Seaborn  

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── report/
│   ├── Presentation.pdf
│   └── Thesis.pdf
├── notebooks/
│   ├── 01_preprocessing.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_survival_analysis.ipynb
│   └── 04_survival_modeling.ipynb
├── src/
│   ├── __init__.py
│   └── utils.py
├── data/
│   ├── raw/        # contains raw data (not tracked in version control)
│   └── processed/  # generated during preprocessing
├── models/
│   ├── best_model.pt
│   └── scaler.pkl
└── outputs/        # generated figures and tables
    ├── figures/ 
    └── tables/
```
> **Note:** `data/processed/` and `outputs/` are generated when running the notebooks and are not tracked in version control.

---

## Data Source

The clinical data used in this project were obtained from the **Genomic Data Commons (GDC) Data Portal**:

- **Project:** TCGA-PAAD  
- **Portal:** https://portal.gdc.cancer.gov/projects/TCGA-PAAD  

Specifically, clinical datasets from the TCGA Pancreatic Adenocarcinoma (PAAD) cohort were used.

Raw data files are not included in this repository to follow data governance and reproducibility best practices.

### How to Obtain the Data

1. Visit the GDC portal link above.  
2. Download the clinical data for the TCGA-PAAD project.  
3. Place the downloaded files inside: `data/raw/`
4. Run `01_preprocessing.ipynb` to generate the processed dataset.

---

## Reproducibility

To reproduce the analysis:

1. Create a Python environment (recommended: **Python 3.10+**).
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Run the notebooks in the following order:
- 01_preprocessing.ipynb
- 02_exploratory_data_analysis.ipynb
- 03_survival_analysis.ipynb
- 04_survival_modeling.ipynb

### Notes

Results may slightly vary depending on environment versions and random seeds.

For full reproducibility, consider fixing random seeds in the notebooks.

The trained model (models/best_model.pt) and scaler are provided for convenience and quick reproducibility.

---

## Project Status

Final version corresponding to the Master’s Thesis (MSc in Data Science).