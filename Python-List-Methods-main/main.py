# List example
myList = [10, 20, "Python"]  # A list with different data types
print("Initial list: ", myList)  # Print the initial list

# Variable definitions
x = 10
y = 20
z = "Python"
myList = [x, y, z]  # A new list containing variables and a string
print("New list: ", myList)  # Print the new list

# Basic list operations
print("List length: ", len(myList))  # Print the length of the list
print("First element: ", myList[0])  # Print the first element
print("Last element: ", myList[-1])  # Print the last element

# Adding an element to the list
myList.append("Javascript")  # Add "Javascript" to the end of the list
print("List after adding an element: ", myList)  # Print the list after adding an element

# Accessing and slicing list elements
print("Slice: ", myList[0:2])  # List slicing (first two elements)

# Inserting a specific value into the list
myList.insert(1, "Java")  # Insert "Java" at index 1
print("List after inserting Java: ", myList)  # Print the list after inserting "Java"

# Removing an element from the list
myList.remove("Python")  # Remove the element "Python"
print("List after removing Python: ", myList)  # Print the list after removing "Python"

# Removing the last element
last_item = myList.pop()  # Remove and store the last element
print("Removed last element: ", last_item)  # Print the removed element
print("List after removing the last element: ", myList)  # Print the list after removing the last element

# Index of a specific element in the list
index_of_java = myList.index("Java")  # Find the index of "Java"
print("Index of Java: ", index_of_java)  # Print the index

# Clearing all elements in the list
myList.clear()  # Clear all elements in the list
print("List after clearing all elements: ", myList)  # Print the cleared list


--

# Liste örneği / List example
myList = [10, 20, "Python"]  # Farklı veri tiplerinden oluşan bir liste / A list with different data types
print("Başlangıçtaki liste: ", myList)  # Listeyi yazdırma / Print the initial list

# Değişken tanımlamaları / Variable definitions
x = 10
y = 20
z = "Python"
myList = [x, y, z]  # String ve değişkenleri içeren yeni bir liste / A new list containing variables and a string
print("Yeni liste: ", myList)  # Yeni listeyi yazdırma / Print the new list

# Liste ile ilgili temel işlemler / Basic list operations
print("Liste uzunluğu: ", len(myList))  # Liste uzunluğunu yazdırma / Print the length of the list
print("İlk eleman: ", myList[0])  # İlk elemanı yazdırma / Print the first element
print("Son eleman: ", myList[-1])  # Son elemanı yazdırma / Print the last element

# Listeye eleman ekleme / Adding an element to the list
myList.append("Javascript")  # Listenin sonuna "Javascript" ekleme / Add "Javascript" to the end of the list
print("Eleman eklendikten sonraki liste: ", myList)  # Eleman eklendikten sonraki listeyi yazdırma / Print the list after adding an element

# Liste elemanına erişim ve dilimleme / Accessing and slicing list elements
print("Dilim: ", myList[0:2])  # Liste dilimleme (ilk iki eleman) / List slicing (first two elements)

# Belirli bir değeri listeye ekleme / Inserting a specific value into the list
myList.insert(1, "Java")  # 1. indise "Java" ekleme / Insert "Java" at index 1
print("Java eklendikten sonraki liste: ", myList)  # Listeyi yazdırma / Print the list after inserting "Java"

# Liste elemanını silme / Removing an element from the list
myList.remove("Python")  # "Python" elemanını silme / Remove the element "Python"
print("Python silindikten sonraki liste: ", myList)  # Listeyi yazdırma / Print the list after removing "Python"

# Liste sonundaki elemanı çıkarma / Removing the last element
last_item = myList.pop()  # Son elemanı çıkarma ve saklama / Remove and store the last element
print("Son eleman çıkarıldı: ", last_item)  # Çıkarılan elemanı yazdırma / Print the removed element
print("Son eleman çıkarıldıktan sonraki liste: ", myList)  # Listeyi yazdırma / Print the list after removing the last element

# Listedeki belirli bir elemanın indeksi / Index of a specific element in the list
index_of_java = myList.index("Java")  # "Java"nın indeksini bulma / Find the index of "Java"
print("Java'nın indeksi: ", index_of_java)  # İndeksi yazdırma / Print the index

# Listedeki tüm elemanları temizleme / Clearing all elements in the list
myList.clear()  # Tüm listeyi temizleme / Clear all elements in the list
print("Liste temizlendikten sonraki hali: ", myList)  # Boş listeyi yazdırma / Print the cleared list
