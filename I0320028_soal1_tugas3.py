# Menampilkan list 10 nama teman
list = ['Ara', 'Gea', 'Hanna', 'Candrika', 'Funny', 'Ayu', 'Angela', 'Alifiana', 'Dhea', 'Deadila']

# Menampilkan isi list indeks nomor 4, 6, dan 7
print("List indeks nomor 4, 6, dan 7 yaitu", list[4], ",", list[6], ",", "dan", list[7])

# Mengganti nama teman di list 3, 5, dan 9
list[3] = 'Vizal'
list[5] = 'Jefri'
list[9] = 'Diva'

# Menambahkan 2 nama teman
list.append('Issa')
list.append('Hani')

# Menampilkan semua teman dengan pengulangan
print(list*2)

# Menampilkan panjang list
print(len(list))