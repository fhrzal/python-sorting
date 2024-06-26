import os

def selection_sort(arr):
    os.system("clear")
    n = len(arr)
    print("Array awal:", arr,"\n")
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Tukar elemen terkecil dengan elemen pertama yang belum diurutkan
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Langkah {i+1}: Menukar elemen index {i} dengan elemen index {min_idx}, Array sekarang: {arr}\n")
        kon = input("klik enter >>")

    os.system("clear")    
    print("Array telah diurutkan:", arr)

# Contoh penggunaan
angka = [64, 25, 15, 12, 22, 11]
selection_sort(angka)
