# Contoh cara membuat dua subplot vertikal
fig, ax = plt.subplots(2, 1, figsize=(12, 8))

# Plot untuk Produk A
ax[0].plot(months, product_A_sales, label='Product A', color='blue', marker='o')
ax[0].set_ylabel('Jumlah Penjualan')
ax[0].set_title('Penjualan Produk A per Bulan')
ax[0].set_xticks(months)  # jika ingin menampilkan bulan sebagai label pada sumbu x
ax[0].legend()
ax[0].grid(True)

# Plot untuk Produk B
ax[1].plot(months, product_B_sales, label='Product B', color='red', marker='x')
ax[1].set_ylabel('Jumlah Penjualan')
ax[1].set_title('Penjualan Produk B per Bulan')
ax[1].set_xticks(months)
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()
