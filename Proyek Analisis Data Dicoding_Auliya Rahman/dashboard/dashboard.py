import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

day_df = pd.read_csv ('C:/Users/LENOVO/Downloads/day.csv')
day_df.head()

day_df.groupby(by='weathersit').agg({
    'casual': ['max', 'min', 'mean', 'sum'],
    'registered': ['max', 'min', 'mean', 'sum'],
    'cnt': ['max', 'min', 'mean', 'sum']
})
day_df.groupby(by='holiday').agg({
    'casual': ['max', 'min', 'mean', 'sum'],
    'registered': ['max', 'min', 'mean', 'sum'],
    'cnt': ['max', 'min', 'mean','sum']
})
day_df.groupby(by='weekday').agg({
    'casual': ['max', 'min', 'mean', 'sum'],
    'registered': ['max', 'min', 'mean', 'sum'],
    'cnt': ['max', 'min', 'mean','sum']
})
day_df.groupby(by='workingday').agg({
    'casual': ['max', 'min', 'mean', 'sum'],
    'registered': ['max', 'min', 'mean', 'sum'],
    'cnt': ['max', 'min', 'mean','sum']
})


# Mengelompokkan data berdasarkan cuaca dan menghitung jumlah penyewaan casual dan registered
weather_usage = day_df.groupby('weathersit')['cnt'].sum().reset_index()

plt.figure(figsize=(10, 6))

# Membuat barplot
plt.bar(
    weather_usage['weathersit'],
    weather_usage['cnt'],
    label='Registered',
    color='tab:blue'
)

# Menambahkan label dan judul
plt.xlabel(None)
plt.ylabel(None)
plt.title('Jumlah Penyewaan Sepeda berdasarkan Kondisi Cuaca')
plt.legend()

# Tampilkan plot
st.pyplot(plt)

# Mengelompokkan data berdasarkan cuaca dan menghitung jumlah penyewaan casual dan registered
weather_usage = day_df.groupby('weathersit')[['registered', 'casual']].sum().reset_index()

plt.figure(figsize=(10, 6))

# Membuat barplot
plt.bar(
    weather_usage['weathersit'],
    weather_usage['registered'],
    label='Registered',
    color='tab:red'
)

plt.bar(
    weather_usage['weathersit'],
    weather_usage['casual'],
    label='Casual',
    color='tab:blue'
)

# Menambahkan label dan judul
plt.xlabel(None)
plt.ylabel(None)
plt.title('Jumlah Penyewaan Sepeda berdasarkan Kondisi Cuaca')
plt.legend()

# Tampilkan plot
st.pyplot(plt)

plt.figure(figsize=(25, 6))

# Bar plot untuk holiday
plt.subplot(1, 3, 1)
sns.barplot(
    x='holiday',
    y='cnt',
    data=day_df,
    alpha=0.5
)
plt.title('Jumlah Penyewaan Holiday')

# Bar plot untuk weekday
plt.subplot(1, 3, 2)
sns.barplot(
    x='weekday',
    y='cnt',
    data=day_df,
    alpha=0.5
)
plt.title('Jumlah Penyewaan Weekday')

# Bar plot untuk workingday
plt.subplot(1, 3, 3)
sns.barplot(
    x='workingday',
    y='cnt',
    data=day_df,
    alpha=0.5
)
plt.title('Jumlah Penyewaan Workingday')

# Tampilkan plot
st.pyplot(plt)

st.write('Kesimpulan')
st.write('1. Bagaimana pengaruh cuaca terhadap jumlah penyewaan sepeda?')
st.write('Berdasarkan hasil analisisnya, didapatkan kesimpulan bahwa jumlah penyewaan sepeda terbanyak ada pada cuaca cerah berawan. Hal ini dapat terjadi, kemungkinan dikarenakan pada cuaca hujan, lintasan/jalan akan sangat licin, ditambah dengan kencangnya angin menyebabkan sulitnya bersepeda pada cuaca tersebut. Selain itu, ketika cuaca berawan, ada kemungkinan besar akan terjadi hujan, itulah mengapa jumlah penyewaan sepeda pada kedua cuaca ini jauh lebih sedikit dibandingkan pada cuaca cerah berawan.')
st.write('2. Bagaimana pengaruh variabel holiday, weekday, dan workingday terhadap jumlah penyewa sepeda?')
st.write('Pada hari kerja atau bukan hari libur, banyak orang menggunakan sepeda sebagai alat transportasi untuk pergi ke tempat kerja, sekolah, atau tujuan lainnya. Inilah yang menyebabkan jumlah penyewaan sepeda yang lebih tinggi dibandingkan dengan hari yang bukan hari kerja atau hari libur. Selain itu, hari Jumat sering dianggap sebagai awal akhir pekan. Banyak orang mungkin menyewa sepeda untuk bersenang-senang atau berolahraga setelah minggu kerja yang panjang. Ini bisa menjelaskan mengapa penyewaan sepeda pada hari tersebut lebih tinggi dibandingkan hari lainnya.')
