import random  # Import the random module for generating random numbers

# Comparison Operators
x = 2
y = 5

print(x < y)        # Is x less than y? - True
print(x > y)        # Is x greater than y? - False
print(x < y and x < 0)  # Is x less than y AND less than 0? - False
print(x < y or x > 0)   # Is x less than y OR greater than 0? - True
print(x == y)       # Is x equal to y? - False
print(x != y)       # Is x not equal to y? - True

# Output:
# True
# False
# False
# True
# False
# True

# List Check
myList = [10, 20, 30, 40, 50]
if 20 in myList:
    print("20 found in the list.")  # 20 is in the


--

import random  # Rastgele sayılar oluşturmak için random modülünü içe aktarıyoruz / Import the random module for generating random numbers

# Karşılaştırma Operatörleri / Comparison Operators
x = 2
y = 5

print(x < y)        # x, y'den küçük mü? / Is x less than y? - True
print(x > y)        # x, y'den büyük mü? / Is x greater than y? - False
print(x < y and x < 0)  # x, y'den küçük VE x 0'dan küçük mü? / Is x less than y AND less than 0? - False
print(x < y or x > 0)   # x, y'den küçük VEYA x 0'dan büyük mü? / Is x less than y OR greater than 0? - True
print(x == y)       # x, y'ye eşit mi? / Is x equal to y? - False
print(x != y)       # x, y'ye eşit değil mi? / Is x not equal to y? - True

# Çıktı / Output:
# True
# False
# False
# True
# False
# True

# Liste Kontrolü / List Check
myList = [10, 20, 30, 40, 50]
if 20 in myList:
    print("20 listede bulundu.")  # 20 is in the list / 20 found in the list
else:
    print("Koşul sağlanmadı.")  # If 20 is not in the list / Condition not met

# Çıktı / Output:
# 20 listede bulundu.

# Continue ve Break Örneği / Continue and Break Example
for num in myList:
    if num == 30:
        continue  # Eğer num 30 ise, bu döngüdeki iterasyonu atla / If num is 30, skip this iteration.
    if num == 40:
        break  # Eğer num 40 ise, döngüyü kır / If num is 40, break the loop.
    print(num)  # num, 30 veya 40 değilse yazdır / Print num if it's not 30 or 40

print("For döngüsü tamamlandı.")  # For loop has completed / For loop completed

# Çıktı / Output:
# 10
# 20
# For döngüsü tamamlandı.

# While Döngüsü Örneği / While Loop Example
count = 0  # Sayacı başlat / Initialize counter
while count < 5:  # Count 5'ten küçük olduğu sürece / While count is less than 5
    print("Count:", count)  # Count değerini yazdır / Print count value
    count += 1  # Count'u 1 artır / Increment count by 1
    if count == 3:
        continue  # Eğer count 3 ise, bu iterasyonu atla / If count is 3, skip this iteration.
    print("Bu mesaj, count 3 olmadığında yazdırılır.")  # Print when count is not 3

print("While döngüsü tamamlandı.")  # While loop has completed / While loop completed

# Çıktı / Output:
# Count: 0
# Bu mesaj, count 3 olmadığında yazdırılır.
# Count: 1
# Bu mesaj, count 3 olmadığında yazdırılır.
# Count: 2
# Count: 3
# Count: 4
# While döngüsü tamamlandı.

# Enumerate Örneği / Enumerate Example
for index, value in enumerate(myList):
    print(f"Index: {index}, Value: {value}")  # İndeks ve değeri yazdır / Print index and value

# Çıktı / Output:
# Index: 0, Value: 10
# Index: 1, Value: 20
# Index: 2, Value: 30
# Index: 3, Value: 40
# Index: 4, Value: 50

# Belirli Bir Koşul ile Enumerate Örneği / Enumerate with Condition Example
for index, value in enumerate(myList):
    if value % 20 == 0:
        print(f"Index: {index}, Value: {value} - 20'nin katı.")  # 20'nin katı olan değerleri yazdır / Print values that are multiples of 20

# Çıktı / Output:
# Index: 1, Value: 20 - 20'nin katı.
# Index: 3, Value: 40 - 20'nin katı.

# Rastgele Sayı Örneği / Random Number Example
random_number = random.randint(1, 100)  # 1 ile 100 arasında rastgele bir tam sayı üret / Generate a random integer between 1 and 100
print(f"Rastgele sayı: {random_number}")  # Rastgele sayıyı yazdır / Print the random number

# Çıktı: (Örnek) / Output: (Example)
# Rastgele sayı: 47

# Rastgele Sayılar Listesi Ekleme / Adding Random Numbers to a List
random_numbers = [random.randint(1, 50) for _ in range(5)]  # 1 ile 50 arasında 5 rastgele tam sayı üret / Generate a list of 5 random integers between 1 and 50
print(f"Rastgele sayıların listesi: {random_numbers}")  # Rastgele sayıların listesini yazdır / Print the list of random numbers

# Çıktı: (Örnek) / Output: (Example)
# Rastgele sayıların listesi: [15, 28, 34, 6, 22]
