"""
[==============================]
MADE BY KELOMPOK 9
Find More at https://github.com
Member :
1. Regha Rahmadian Bintang  156
2. M Ibnu Nadhif            161
3. Refany Dwi Lestari       170

===============================
This code can be used at :
https://reeborg.ca/reeborg.html
to complete Hurdle 1-4 
===============================
"""
#membuat fungsi yang digunakan untuk membuat robot dapat menghadap kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#membuat loop yang berfungsi agar selama robot belum mencapai tujuan maka harus melakukan serangkaian gerakan hingga mencapai finish
while not at_goal():
    #jika depan kosong atau tidak ada halangan maka :
    if front_is_clear():
