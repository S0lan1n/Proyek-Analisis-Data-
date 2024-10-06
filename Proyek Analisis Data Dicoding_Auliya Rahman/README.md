# Submission Proyek Belajar Analisis Data dengan Python

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Before running streamlit app
Pindahkan requirements.txt, day.csv, dan dashboard.py ke direktori yang telah dibuat.
Jika pada terminal direktorinya belum sesuai, maka direktorinya harus diarahkan dengan:
cd proyek_analisis_data

## Run steamlit app
```
Jika direktori sudah sesuai, maka streamlit dapat dirun:
streamlit run dashboard.py
```