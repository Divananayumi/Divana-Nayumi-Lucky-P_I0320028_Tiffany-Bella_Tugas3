# Membuat Dictionary pada Python
dict = {'Nama':'Divana','Hobi1':'Berenang','Hobi2':'Membaca novel','Hobi3':'Kulineran','Sosmed1':'twitter:DivanaNayumiLP','Sosmed2':'line:nayumi_13','Sosmed3':'ig:divanaaayumi','Lagukesukaan1':'Imagination','Lagukesukaan2':'Perfect','Lagukesukaan3':'To The Bone','Makananfavorit1':'Mie ayam','Makananfavorit2':'Steak','Makananfavorit3':'Nasi goreng'}

# Mengubah salah satu dari hobi dan sosial media
dict['Hobi3'] = 'Jalan-jalan'
dict['Sosmed1'] = 'twitter:Divanayumi'

# Menghapus 2 makanan favorit
del dict['Makananfavorit2']
del dict['Makananfavorit3']

# Menambahkan 1 hobi
dict['Hobi4'] = 'Mendengarkan musik'

print(dict)