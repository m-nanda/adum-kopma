import pandas as pd
import smtplib
from email.message import EmailMessage
from datetime import datetime


# Fungsi untuk keterangan waktu secara otomatis
def keterangan_waktu():    
    now = datetime.now()
    waktu_sekarang = now.strftime("%H:%M:%S")
    ket = ''

    if (waktu_sekarang>='00:00:00' and waktu_sekarang<'11:00:00'):
        ket = 'pagi'
    elif (waktu_sekarang>='11:00:00' and waktu_sekarang<'15:00:00'):
        ket = 'siang'
    elif (waktu_sekarang>='15:00:00' and waktu_sekarang<'18:00:00'):
        ket = 'sore'
    else:
        ket = 'malam'
    return ket


# Fungsi untuk pengiriman banyak email dengan data dinamis
def auto_send (pengirim, password, penerima, nama, judul_email):   
    msg = EmailMessage()
    msg['Subject'] = judul_email
    msg['From'] = pengirim
    msg['To'] = penerima    
    
    # Pesan teks biasa
    msg.set_content('Haloo ' +nama +'\n'+
    'Email ini dikirim dengan script python\n'+
    'Cek github saya di sini')
    
    # pesan dalam bentuk html
    msg.add_alternative("""
    <html>      
      <body>
        Haloo """ +nama +"""<br>
        Email ini dikirim dengan <em>script python</em><br>
        Cek github saya <b><a href='https://github.com/m-nanda/adum-kopma/pengiriman-email-python' style="color:orange; text-decoration:none">di sini</a></b>    
      </body>
    </html>    
    """,subtype='html')    
    
    # Untuk pengiriman pesan email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(pengirim, password)
        server.send_message(msg)
        
    print('Pesan telah terkirim ke ' +penerima)
    
    
# Mengambil data dari file excel
data = pd.read_excel('Contoh File Data Nama dan Email.xlsx')

# Contoh untuk pengiriman
pengirim = 'contoh@pengirim.com' 
password = 'isi_password_kamu'
judul_email = 'Test'
nama = data['nama'].to_list()
alamat_email = data['email'].to_list()

# Looping untuk pengiriman email
for i in range(len(nama)):    
    auto_send (pengirim, password, alamat_email[i], nama[i], judul_email)    
