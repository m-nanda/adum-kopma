function sendMail() {
  //Untuk memudahkan mengakses kolom
  var nama = 0;  
  var na = 1;
  var jenis_kelamin = 2;
  var alamat_email = 3;
  var kirim_ = 4;
  
  //menghubungkan file gs dan html. Parameter disesuaikan dengan nama file html
  var konektor_ke_html = HtmlService.createTemplateFromFile("isi_email");  
  
  //mengakses sheet yang akan digunakan pada spreadsheet
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Sheet1");  
  
  //mengakses range cell yang akan digunakan dari sheet yang telah dipilih
  var data = sheet.getRange("A2:E" +sheet.getLastRow()).getValues();  
  
  //filter agar hannya mengirimkan ke e-mail yg dicentang saja
  data = data.filter(function(nama_kolom){return nama_kolom[kirim_] == true});
  
  //tes awal. hanya untuk mengecek apakah data dari sheet berhasil diambil 
  //dengan benar atau tidak
  Logger.log(data);
  
  //mengganti nilai fungsi yang ada pada e-mail html dengan data dari sheet
  data.forEach(function(baris){       
    konektor_ke_html.ket = cekKetWaktu();
    konektor_ke_html.nama = baris[nama];    
    konektor_ke_html.na = baris[na];    
    var htmlMessage = konektor_ke_html.evaluate().getContent();        
  }); 
  
  //looping untuk memasukkan data yang diinginkan dari sheet ke isi_e-mail
  data.forEach(function(baris){   
    //mengganti nilai fungsi yang ada pada e-mail html dengan data dari sheet
    konektor_ke_html.ket = cekKetWaktu();
    konektor_ke_html.nama = baris[nama];    
    konektor_ke_html.na = baris[na];
    var htmlMessage = konektor_ke_html.evaluate().getContent();
    
    //fungsi untuk melakukan pengiriman e-mail
    GmailApp.sendEmail(
      baris[alamat_email], 
      "Sample Automation for Sending Bulk Email with GSheet-GS-HTML", 
      "E-mail kamu tidak support HTML",
      {name: "</>", htmlBody: htmlMessage})
  });   
}

function cekKetWaktu(){
  // Mengambil data tanggal sekarang
  var sekarang = new Date()    

  // Mengambil jam sekarang (dalam waktu Indonesia Barat)
  var jam = Utilities.formatDate(sekarang, 'Etc/GMT-8', 'HH:mm:ss')
  
  // Jika ingin mengecek matikan komennya
  // Logger.log(jam)

  // Percabangan untuk memberi keterangan otomatis
  var ket = ''
  if (jam>='00:00:00' && jam<'11:00:00')
    ket = 'pagi'
  else if (jam>='11:00:00' && jam<'15:00:00')
    ket = 'siang'
  else if (jam>='15:00:00' && jam<'18:00:00')
    ket = 'sore'
  else
    ket = 'malam'
  
  // Jika ingin mengecek matikan komennya
  //Logger.log(ket)

  return ket
}
