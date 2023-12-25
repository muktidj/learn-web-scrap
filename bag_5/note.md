## Using Search xpath in Chrome Developer Tool
Press F12 to open Chrome Developer Tool
In "Elements" panel, press Ctrl+F
In the search box, type in XPath or CSS Selector, if elements are found, they will be highlighted in yellow.

## Xpath
`//label[@analytic-event="All matches"]`
Berikut adalah penjelasan rinci dari kode XPath //label[@analytics-event='All matches']:

1. //label:

Mencari semua elemen label di seluruh dokumen HTML, terlepas dari posisinya dalam struktur dokumen.
Tanda **//** di awal menunjukkan pencarian dilakukan secara global di seluruh dokumen.

2. [@analytics-event='All matches']:

Menentukan kondisi filter untuk elemen label yang ingin ditemukan.
**@** menunjukkan bahwa kita akan mencari berdasarkan atribut.
analytics-event adalah nama atribut yang ingin difilter.
**='All matches'** adalah nilai yang harus dimiliki atribut analytics-event agar elemen label tersebut terpilih.

>Arti keseluruhan kode XPath:

Temukan elemen label di mana pun di dalam dokumen HTML.
Filter pencarian agar hanya elemen label yang memiliki atribut analytics-event dengan nilai 'All matches' yang ditemukan.
Dalam konteks kode Python yang Anda berikan:

Kode tersebut menggunakan XPath ini untuk menemukan elemen label spesifik yang memiliki atribut analytics-event dengan nilai 'All matches'.
Elemen yang ditemukan kemudian akan disimpan dalam variabel element untuk digunakan dalam proses selanjutnya.
Contoh:

Jika terdapat kode HTML berikut: <label analytics-event="All matches">Tampilkan semua pertandingan</label>
XPath tersebut akan berhasil menemukan elemen label tersebut karena memenuhi kondisi yang ditentukan.

---
`//tr/td` `//tr/td[]`