# Deskripsi
N-barisan kegiatan terakhir anggota dapat digunakan untuk melihat kegiatan apa saja yang dihadiri, apakah dalam masih aktif mengikuti kegiatan (misal) dalam 1-2 bulan terakhir
atau tidak. Karena hal tersebut tidak dapat dilihat jika hanya menggunakan jumlah poin. Hasilnya yang sudah jadi dapat dilihat seperti pada 
[web ini](https://www.kopmaits.net/administrasi/rekap-poin-keaktifan). Pengerjaan secara **komputasi** dapat membantu mempermudah pencarian n-barisan ini, sebab:
1. Dalam kondisi riil, data **cukup besar**, yaitu sebanyak P anggota dan Q kegiatan, di mana ![equation](https://latex.codecogs.com/gif.latex?P>200,&space;Q>30&space;\in&space;\mathbb{N}).
2. **Variasi perbedaan kehadiran yang tinggi antar anggota**.
3. Pengerjaan secara manual **rentan akan kesalahan**.

Ilustrasi tabel kehadiran kegiatan:
| Nama        | ID          | Kegiatan Q | Kegiatan Q-1 | Kegiatan Q-2 | ... | Kegiatan 0 |
| ----------- | ----------- | ---------- | ------------ | ------------ | --- | ---------- | 
| Anggota-1   | A-1         | 0          | 1            | 1            | ... | ...        |
| ...         | ...         | ...        | ...          | ...          | ... | ...        |
| Anggota-P   | A-P         | 1          | 0            | 0            | ... | ...        |


# Contoh
## Input
* ![equation](https://latex.codecogs.com/gif.latex?N&space;=&space;3) 
* Tabel sumber data, dengan ![equation](https://latex.codecogs.com/svg.image?P=3,&space;Q=5):  

| Nama        | ID          | Kegiatan E | Kegiatan D | Kegiatan C | Kegiatan B | Kegiatan A |
| ----------- | ----------- | ---------- | ---------- | ---------- | ---------- | ---------- | 
| Anggota 1   | 001         | 0          | 1          | 1          | 1          | 0          |
| Anggota 2   | 002         | 1          | 1          | 0          | 1          | 1          |
| Anggota 3   | 003         | 1          | 0          | 0          | 0          | 1          |

## _Pseudocode_
```
function n_barisan(tabel, N, P, Q):
  list_kegiatan := []
  for i in range(P) do:
    k := 0    
    kegiatan := []
    for j in range(Q) do:                
        if tabel[i,j]==1 and k<N then:
            kegiatan += tabel.columns[j]
            k++                
        if k==N then:
            break  
    list_kegiatan += kegiatan
  return list_kegiatan
```

## Output
* [[Kegiatan D, Kegiatan C, Kegiatan B],  
  &nbsp;[Kegiatan E, Kegiatan D, Kegiatan B],  
  &nbsp;[Kegiatan E, Kegiatan A]]
  
  Dapat diartikan sebagai:  
  Anggota 1 = {Kegiatan D, Kegiatan C, Kegiatan B}  
  Anggota 2 = {Kegiatan E, Kegiatan D, Kegiatan B}  
  Anggota 3 = {Kegiatan E, Kegiatan A}
