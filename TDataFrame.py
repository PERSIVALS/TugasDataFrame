import pandas as pd


data = {
    'Kabupaten/Kota': ['Kota Bandung', 'Kabupaten Bogor', 'Kota Bekasi', 'Kabupaten Bandung',
                       'Kota Depok', 'Kabupaten Garut', 'Kota Cimahi', 'Kabupaten Cianjur',
                       'Kota Sukabumi', 'Kabupaten Sukabumi', 'Kota Tasikmalaya', 'Kabupaten Tasikmalaya',
                       'Kota Bandung', 'Kabupaten Bogor', 'Kota Bekasi', 'Kabupaten Bandung',
                       'Kota Depok', 'Kabupaten Garut', 'Kota Cimahi', 'Kabupaten Cianjur',
                       'Kota Sukabumi', 'Kabupaten Sukabumi', 'Kota Tasikmalaya', 'Kabupaten Tasikmalaya',
                       'Kota Bandung', 'Kabupaten Bogor', 'Kota Bekasi', 'Kabupaten Bandung',
                       'Kota Depok', 'Kabupaten Garut', 'Kota Cimahi', 'Kabupaten Cianjur',
                       'Kota Sukabumi', 'Kabupaten Sukabumi', 'Kota Tasikmalaya', 'Kabupaten Tasikmalaya',
                       'Kota Bandung', 'Kabupaten Bogor', 'Kota Bekasi', 'Kabupaten Bandung',
                       'Kota Depok', 'Kabupaten Garut', 'Kota Cimahi', 'Kabupaten Cianjur',
                       'Kota Sukabumi', 'Kabupaten Sukabumi', 'Kota Tasikmalaya', 'Kabupaten Tasikmalaya'],
    'Tahun': [2020, 2020, 2020, 2020, 
              2020, 2020, 2020, 2020,
              2020, 2020, 2020, 2020,
              2021, 2021, 2021, 2021,
              2021, 2021, 2021, 2021,
              2021, 2021, 2021, 2021,
              2022, 2022, 2022, 2022,
              2022, 2022, 2022, 2022,
              2022, 2022, 2022, 2022,
              2023, 2023, 2023, 2023,
              2023, 2023, 2023, 2023,
              2023, 2023, 2023, 2023],
    'Produksi Sampah (ton)': [50000, 75000, 60000, 85000, 
                              47000, 56000, 52000, 48000,
                              49000, 53000, 51000, 55000,
                              55000, 77000, 62000, 88000,
                              47000, 57000, 54000, 50000,
                              52000, 58000, 56000, 59000,
                              58000, 79000, 65000, 89000,
                              50000, 59000, 57000, 52000,
                              54000, 60000, 58000, 61000,
                              60000, 80000, 68000, 91000,
                              52000, 61000, 59000, 55000,
                              56000, 63000, 60000, 65000]
}


for key, value in data.items():
    print(f"{key}: {len(value)} elemen")


df = pd.DataFrame(data)
print("\nDataFrame Awal:")
print(df)


tahun_tertentu = 2023
total_produksi_tahun = df[df['Tahun'] == tahun_tertentu]['Produksi Sampah (ton)'].sum()
print(f"\nTotal Produksi Sampah pada Tahun {tahun_tertentu}: {total_produksi_tahun} ton")

df_produksi_per_tahun = df.groupby('Tahun')['Produksi Sampah (ton)'].sum().reset_index()
df_produksi_per_tahun.rename(columns={'Produksi Sampah (ton)': 'Total Produksi Sampah (ton)'}, inplace=True)
print("\nTotal Produksi Sampah Per Tahun:")
print(df_produksi_per_tahun)

df_produksi_per_kota_tahun = df.groupby(['Kabupaten/Kota', 'Tahun'])['Produksi Sampah (ton)'].sum().reset_index()
df_produksi_per_kota_tahun.rename(columns={'Produksi Sampah (ton)': 'Total Produksi Sampah (ton)'}, inplace=True)
print("\nTotal Produksi Sampah Per Kota/Kabupaten Per Tahun:")
print(df_produksi_per_kota_tahun)

df_produksi_per_tahun.to_csv('produksi_per_tahun.csv', index=False)
df_produksi_per_kota_tahun.to_excel('produksi_per_kota_tahun.xlsx', index=False)
print("\nHasil telah diexport ke 'produksi_per_tahun.csv' dan 'produksi_per_kota_tahun.xlsx'")
