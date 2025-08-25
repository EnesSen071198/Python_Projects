import numpy as np

# max, min, average -> dizinin max min ortalamasını alır
my_np_array = np.array([10, 20, 30, 40])
print("Max: ", my_np_array.max())
print("Min: ", my_np_array.min())
print("Average: ", my_np_array.mean())

# matrix -> istenilen matrix düzenini oluşturur
my_np_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(my_np_matrix)
print("İlk eleman: ", my_np_matrix[0])
print("Matrix Bilgisi: ", my_np_matrix.shape)

# range -> istenilen sayıya kadar sayılan dizi oluşturur
my_np_range = np.arange(0, 50, 5)
print("Range: ", my_np_range)

# her değeri 0 olan dizi
my_np_zeros = np.zeros((10, 10))
print("Zeros: ", my_np_zeros)

# her değeri 1 olan dizi
my_np_ones = np.ones((10, 10))
print("Ones: ", my_np_ones)

# linspace -> 0=Başlangıç , 10=Bitiş , 100=Kaç adet -> 0 dan 10 a kadar 100 tane değer oluştur ve eşit artışlarla gitt
my_np_linspace = np.linspace(0, 10, 100)
print("Linspace: ", my_np_linspace)

#random
my_np_random=np.random.randint(1,100,5) #1 ile 100 arasında 5 adet random sayı ver
print("My random number: ",my_np_random)

#slicing
my_np_list = np.arange(0, 20)
print("Slicing: ",my_np_list[4:9])

#update array
my_np_list[4:9] = -10
print("Updated Array: ", my_np_list)

