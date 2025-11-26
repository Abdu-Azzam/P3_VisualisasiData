import matplotlib.pyplot as plt 

#Buat data sample
months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

#Trend
plt.plot(months, product_A_sales, label='Product A trend', color='blue') 
plt.plot(months, product_B_sales, label='Product B trend', color='red')
plt.title('Penjualan Produk Per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')
plt.legend()
plt.grid(True)
plt.show()