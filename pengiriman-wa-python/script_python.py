# Import library yang diperlukan
import pandas as pd
import time
import pyautogui as pg
import webbrowser as web
from datetime import datetime

# Mengambil dan meyiapkan data dari file excel
data = pd.read_excel('Contoh File Data Nama dan No WA.xlsx')
data_dict = data.to_dict('list')
daftar_nomor = data_dict['nomor']
isi_pesan = data_dict['pesan']
combo = zip(daftar_nomor,isi_pesan)
first = True

# Looping untuk pengiriman pesan
for nomor, pesan in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+nomor+"&text="+pesan)
    if first:
        time.sleep(6)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')
    now = datetime.now()
    waktu_sekarang = now.strftime("%H:%M:%S")
    
    # Untuk keterangan pengiriman
    print('Pesan dikirim ke ' +nomor +' pada: ' +waktu_sekarang)
