import pandas as pd
import matplotlib.pyplot as plt

# Data penjualan
data_penjualan = {
    'id_penjualan': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'tanggal_penjualan': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15', '2024-03-01', '2024-03-15', '2024-04-01', '2024-04-15', '2024-05-01', '2024-05-15'],
    'total_penjualan': [500000, 750000, 300000, 600000, 900000, 1200000, 800000, 700000, 1000000, 1100000],
    'id_produk': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],
    'kategori_produk': ['Elektronik', 'Furnitur', 'Buku', 'Elektronik', 'Furnitur', 'Buku', 'Elektronik', 'Furnitur', 'Buku', 'Elektronik']
}
df_penjualan = pd.DataFrame(data_penjualan)

# Grafik penjualan per bulan
df_penjualan['bulan'] = pd.to_datetime(df_penjualan['tanggal_penjualan']).dt.month
penjualan_per_bulan = df_penjualan.groupby('bulan')['total_penjualan'].sum()
plt.figure(figsize=(10, 6))
plt.bar(penjualan_per_bulan.index, penjualan_per_bulan.values, color='skyblue')
plt.title('Total Penjualan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan')
plt.xticks(penjualan_per_bulan.index, ['Jan', 'Feb', 'Mar', 'Apr', 'May'])
plt.show()

# Grafik penjualan berdasarkan kategori produk
penjualan_per_kategori = df_penjualan.groupby('kategori_produk')['total_penjualan'].sum()
plt.figure(figsize=(8, 8))
plt.pie(penjualan_per_kategori, labels=penjualan_per_kategori.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'lightskyblue'])
plt.title('Porsi Penjualan per Kategori Produk')
plt.show()

# Grafik top produk yang paling laris
top_produk = df_penjualan.groupby('id_produk')['total_penjualan'].sum().nlargest(3)
nama_produk = ['Laptop', 'Meja', 'Buku']
plt.figure(figsize=(10, 6))
plt.bar(nama_produk, top_produk, color=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Top 3 Produk Paling Laris')
plt.xlabel('Produk')
plt.ylabel('Total Penjualan')
plt.show()

# Grafik performa pengiriman barang
data_pengiriman = {
    'id_penjualan': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'status_pengiriman': ['Sudah Dikirim', 'Sudah Dikirim', 'Sudah Dikirim', 'Sedang Dikirim', 'Sedang Dikirim', 'Sedang Dikirim', 'Sudah Dikirim', 'Sudah Dikirim', 'Sedang Dikirim', 'Sedang Dikirim']
}
df_pengiriman = pd.DataFrame(data_pengiriman)
pengiriman_status = df_pengiriman['status_pengiriman'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(pengiriman_status, labels=pengiriman_status.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
plt.title('Status Pengiriman Barang')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib_venn import venn2, venn3

# Data penjualan
data_penjualan = {
    'id_penjualan': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'tanggal_penjualan': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15', '2024-03-01', '2024-03-15', '2024-04-01', '2024-04-15', '2024-05-01', '2024-05-15'],
    'total_penjualan': [500000, 750000, 300000, 600000, 900000, 1200000, 800000, 700000, 1000000, 1100000],
    'id_produk': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],
    'kategori_produk': ['Elektronik', 'Furnitur', 'Buku', 'Elektronik', 'Furnitur', 'Buku', 'Elektronik', 'Furnitur', 'Buku', 'Elektronik']
}
df_penjualan = pd.DataFrame(data_penjualan)

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df_penjualan['id_penjualan'], df_penjualan['total_penjualan'], color='blue')
plt.title('Scatter Plot Penjualan')
plt.xlabel('ID Penjualan')
plt.ylabel('Total Penjualan')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df_penjualan['total_penjualan'], bins=5, color='green')
plt.title('Histogram Total Penjualan')
plt.xlabel('Total Penjualan')
plt.ylabel('Frekuensi')
plt.show()

# Pie Chart
penjualan_per_kategori = df_penjualan.groupby('kategori_produk')['total_penjualan'].sum()
plt.figure(figsize=(8, 8))
plt.pie(penjualan_per_kategori, labels=penjualan_per_kategori.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'lightskyblue'])
plt.title('Porsi Penjualan per Kategori Produk')
plt.show()

# Diagram Venn
# Contoh data untuk Diagram Venn
set1 = set(df_penjualan['id_penjualan'][:5])
set2 = set(df_penjualan['id_penjualan'][3:])
set3 = set(df_penjualan['id_penjualan'][1:7])

plt.figure(figsize=(10, 6))
venn3([set1, set2, set3], ('Set 1', 'Set 2', 'Set 3'))
plt.title('Diagram Venn')
plt.show()

# 3D Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df_penjualan['id_penjualan'], df_penjualan['total_penjualan'], df_penjualan['id_produk'], color='red')
ax.set_title('3D Scatter Plot Penjualan')
ax.set_xlabel('ID Penjualan')
ax.set_ylabel('Total Penjualan')
ax.set_zlabel('ID Produk')
plt.show()
