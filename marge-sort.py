import os

def merge_sort(arr, level=0):
    if len(arr) > 1:
        mid = len(arr) // 2  # Mencari titik tengah array
        left_half = arr[:mid]  # Membagi array menjadi dua bagian
        right_half = arr[mid:]
        
        print("Level", level, "- Membagi:", arr,"\n")
        print("Kiri:", left_half, "Kanan:", right_half,"\n")

        merge_sort(left_half, level+1)  # Rekursi untuk bagian kiri
        merge_sort(right_half, level+1)  # Rekursi untuk bagian kanan

        i = j = k = 0

        # Menggabungkan dua bagian
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Memeriksa jika ada elemen yang tersisa
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print("Level", level, "- Menggabungkan:", arr,"\n")
        kon = input("klik enter >>")

# Contoh penggunaan
os.system("clear")
arr = [38, 27, 43, 3, 9, 82, 10]
print("Array sebelum diurutkan:", arr,"\n")
print(f"total array = ",len(arr))
kon1 = input("klik enter >>\n")
merge_sort(arr)
print("Array setelah diurutkan:", arr)

