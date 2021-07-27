import random
max_leader=4
lst_group=[]
lst_leader_name=[]
lst_leader_count=[]
member=[]
count_anggota=[]

lst_jadwal=[['Senin','07.00-09.30'],['Senin','10.00-12.30'],['Senin','13.00-15.30'],['Senin','16.00-18.30'],
            ['Selasa','07.00-09.30'],['Selasa','10.00-12.30'],['Selasa','13.00-15.30'],['Selasa','16.00-18.30'],
            ['Rabu','07.00-09.30'],['Rabu','10.00-12.30'],['Rabu','13.00-15.30'],['Rabu','16.00-18.30'],['Kamis','07.00-09.30'],
            ['Kamis','10.00-12.30'],['Kamis','13.00-15.30'],['Kamis','16.00-18.30'],['Jumat','07.00-09.30'],
            ['Jumat','10.00-12.30'],['Jumat','13.00-15.30'],['Jumat','16.00-18.30']]

def check_special_char(nama):
    count_char=0
    for i in range(len(nama)):
        if 33<=ord(nama[i])<=64 or 91<=ord(nama[i])<=96 or 123<=ord(nama[i])<=126:
            count_char+=1
    if count_char>0:
        return False
    elif count_char==0:
        return True

def menu():
    print('==MENU==')
    print('1. Input Ketua')
    print('2. Input Anggota')
    print('3. Tambah Anggota')
    print('4. Ganti ketua atau anggota dan Remove anggota')
    print('5. Tampilkan Schedule')
    print('0. Exit')

def cek_member_leader_di_satu_jadwal_sama(idx_jadwal):
    nama_di_jadwal=[]
    jum_di_jadwal=[]
    for i in range(2,len(lst_jadwal[idx_jadwal])): #sebanyak panjang group
        # untuk team leader
        for j in range(0, len(lst_jadwal[idx_jadwal][i][1])):
            nama = lst_jadwal[idx_jadwal][i][1][j]
            if ( nama not in nama_di_jadwal):
                nama_di_jadwal.append(nama)
                jum_di_jadwal.append(1)
            else:
                idx = nama_di_jadwal.index(nama)
                jum_di_jadwal[idx]+=1
        # untuk team member
        for j in range(0, len(lst_jadwal[idx_jadwal][i][2])):
            nama = lst_jadwal[idx_jadwal][i][2][j]
            if ( nama not in nama_di_jadwal):
                nama_di_jadwal.append(nama)
                jum_di_jadwal.append(1)
            else:
                idx = nama_di_jadwal.index(nama)
                jum_di_jadwal[idx]+=1
    #cek orang yang sama di satu jadwal 
    #print(nama_di_jadwal)
    #print(jum_di_jadwal)
    if 2 in jum_di_jadwal:
        return False
    else:
        return True

def cek_member_leader_di_satu_hari_sama():
    nama_di_hari=[]
    for z in range(len(lst_jadwal)):
        for i in range(2,len(lst_jadwal[z])): #minus #namahari #jam jadi mulai dari 2 
            # untuk team leader
            for j in range(0, len(lst_jadwal[z][i][1])): #1 = team leader #2 anggota
                nama = lst_jadwal[z][i][1][j]
                hari = lst_jadwal[z][0]
                posisi = -1
                for k in range(len(nama_di_hari)):
                    if (nama_di_hari[k][0]==hari and nama_di_hari[k][1]==nama):
                        posisi=k
                if posisi==-1:
                    nama_di_hari.append([hari,nama,1])
                else:
                    nama_di_hari[posisi][2]+=1
            # untuk team member
            for j in range(0, len(lst_jadwal[z][i][2])):
                nama = lst_jadwal[z][i][2][j]
                hari = lst_jadwal[z][0]
                posisi = -1
                for k in range(len(nama_di_hari)):
                    if (nama_di_hari[k][0]==hari and nama_di_hari[k][1]==nama):
                        posisi=k
                if posisi==-1:
                    nama_di_hari.append([hari,nama,1])
                else:
                    nama_di_hari[posisi][2]+=1
    #print(nama_di_hari)
    valid = True
    for j in range(0,len(nama_di_hari)):
        if nama_di_hari[j][2]>3:
           valid=False
    return valid

def choose_jadwal():
    team_regis = 2
    while team_regis>=2:
        noJadwal   = random.randint(0,len(lst_jadwal)-1)
        team_regis = len(lst_jadwal[noJadwal])-2 
    return noJadwal

def output_schedule(lst_jadwal):
    back_lower='lala'
    while back_lower!='back':
        print('==Pembagian Jadwal==')
        for i in range(len(lst_jadwal)):
            if len(lst_jadwal[i])>2:
                for j in range(len(lst_jadwal[i])):
                    if j<2:
                        print(*lst_jadwal[i][j],sep='')
                    else:
                        for k in range(len(lst_jadwal[i][j])):
                            if k==0:
                                print(*lst_jadwal[i][j][0],sep='')
                            elif k==1:
                                print('Ketua:', end="")
                                print(*lst_jadwal[i][j][1],sep=',')
                            else:
                                print('Anggota :', end="")
                                print(*lst_jadwal[i][j][2],sep=',')
                print("")
        back=input('Ketik back untuk kembali = ')
        back_lower=back.lower()
        if back_lower != 'back':
            print('Anda hanya bisa mengisi dengan back saja untuk kembali!')

def match_sche_and_team():
    ctr=0 
    while(ctr<len(lst_group)):
        idx_jadwal = choose_jadwal()
        lst_jadwal[idx_jadwal].append(lst_group[ctr]) #append 1 group utuh ke jadwal
        cek_person_di_jadwal_sama = cek_member_leader_di_satu_jadwal_sama(idx_jadwal)
        cek_person_di_hari_sama=cek_member_leader_di_satu_hari_sama()
        if cek_person_di_jadwal_sama==False  or  cek_person_di_hari_sama==False:
            lst_jadwal[idx_jadwal].pop()
        else:
            ctr+=1
    output_schedule(lst_jadwal)

def insert_And_Check_team_leader_in_team(leader_name,i):
    if leader_name not in lst_leader_name and leader_name not in member:
        lst_leader_name.append(leader_name)
        lst_leader_count.append(1)
        return True
    elif leader_name in lst_leader_name and leader_name not in member:
        posisi = lst_leader_name.index(leader_name)
        if lst_leader_count[posisi]==max_leader:
            print(leader_name,'sudah tergabung dalam 4 team')
            return False
        elif leader_name in lst_group[i][1]:
            print(leader_name,'sudah berada di group ini')
            return False
        elif lst_leader_count[posisi]<max_leader and leader_name not in lst_group[i][1]:
            lst_leader_count[posisi]+=1
            return True
    elif leader_name in member:
        print(leader_name,'sudah tergabung menjadi anggota silahkan masukkan nama yang lain untuk menjadi team leader')
        return False

def input_nama_ketua(temp):
    if temp==1:
        i=0
        while (i<len(lst_group)):
            jumlah_leader=input('Masukkan jumlah leader '+'Group '+str(i+1)+' (1/2):')
            if jumlah_leader!='1' and jumlah_leader !='2':
                print('Anda hanya bisa memilih 1/2 team leader saja dan harus dalam bentuk angka')
            else:
                ctr=0
                while ctr<int(jumlah_leader):
                    leader_name=input('Masukkan Nama Ketua '+str(ctr+1)+ ' Group '+ str(i+1)+' =')
                    if leader_name==' ' or leader_name=='' or check_special_char(leader_name)==False:
                        print('Nama yang anda masukkan salah')
                    else:
                        leader_name=leader_name.lower()
                        if insert_And_Check_team_leader_in_team(leader_name,i)==True:
                            lst_group[i][1].append(leader_name)
                            ctr+=1
                i+=1
    else:
        print('Maaf anda tidak bisa kembali ke menu input ketua karena sebelumnya sudah pernah masuk ke dalam menu ini, jika ingin mengganti ketua silahkan ke menu 4')
            
def cek_nama_anggota(nama_anggota,i):
    if nama_anggota not in member and nama_anggota not in lst_leader_name:
        member.append(nama_anggota)
        count_anggota.append(1)
        return True
    elif nama_anggota in member and nama_anggota not in lst_leader_name:
        position = member.index(nama_anggota)
        if count_anggota[position]==7:
            print(nama_anggota,'sudah tergabung dalam 7 team')
            return False
        elif nama_anggota in lst_group[i][2]:
            print(nama_anggota,'sudah berada di group ini')
            return False
        elif nama_anggota not in lst_group[i][2] and count_anggota[position]<7:
            count_anggota[position]+=1
            return True
    elif nama_anggota in lst_leader_name:
        print(nama_anggota,'tidak bisa tergabung dalam group ini karena telah menjadi team leader')
        return False
    
def input_nama_anggota(once):
    if once==1:
        i=0
        while (i<len(lst_group)):
            jumlah_anggota=(input('Masukkan jumlah anggota group '+str(i+1)+' :'))
            if not jumlah_anggota.isnumeric() or int(jumlah_anggota)<1 or int(jumlah_anggota)>30:
                print('Input harus dalam angka dan jumlah anggota dibatasi 1 hingga 30 anggota saja!')
            else:
                ctr=0
                while (ctr<int(jumlah_anggota)):
                    nama_anggota=input('Masukkan nama anggota '+str(ctr+1)+' pada group ' + str(i+1)+':')
                    if nama_anggota==' ' or nama_anggota=='' or check_special_char(nama_anggota)==False:
                        print('Maaf nama yang anda masukkan salah')
                    else:
                        nama_anggota=nama_anggota.lower()
                        if cek_nama_anggota(nama_anggota, i)==True:
                            lst_group[i][2].append(nama_anggota)
                            ctr+=1
                i+=1
    else:
        print('Maaf anda tidak bisa kembali ke menu input anggota karena sebelumnya telah masuk ke dalam menu ini, jika ingin menambahkan anggota silahkan ke menu 3')

def checking_nama_beda():
    if len(member)>171 or len(lst_leader_name)>80:
        print('Jumlah nama yang berbeda di anggota sudah melebihi 171 atau jumlah nama yang berbeda di ketua sudah melebihi 80')
        print('Jumlah nama yang berbeda di anggota sekarang ada', len(member))
        print('Jumlah nama yang berbeda di ketua sekarang ada', len(lst_leader_name))
        return False
    else:
        return True

def checking_requirement_leader_for_scheduling():
    valid_leader=True
    for i in range(len(lst_group)):
        if len(lst_group[i][1])==1 or len(lst_group[i][1])==2:
            valid_leader=True
        else:
            print(lst_group[i][0], 'belum memiliki ketua (harus memiliki ketua min. 1 dan max. 2)')
            valid_leader=False
    return valid_leader

def checking_requirement_member_for_scheduling():
    valid_member=True
    for i in range(len(member)):
        if (count_anggota[i]==7):
            valid_member=True
        else:
            print(member[i]  + ' baru tergabung dalam ' + str(count_anggota[i]) +" team")
            print(member[i], "harus tergabung dalam 7 team, silahkan menambahkan anggota di menu ke-3 atau menghapus anggota di menu ke-4 untuk melanjutkan program")
            valid_member = False
    return valid_member

def checking_count_member():
    valid_count=True
    for i in range(len(lst_group)):
      if len(lst_group[i][2])>0:
          valid_count=True
      else:
          print(lst_group[i][0],'belum memiliki anggota')
          valid_count=False
    return valid_count

def schedule():
    if checking_requirement_leader_for_scheduling()==False  or checking_requirement_member_for_scheduling()==False or checking_count_member()==False or checking_nama_beda()==False:
        pass
    else:
        match_sche_and_team()

def tambah_anggota():
    pilihan_group='-1'
    while int(pilihan_group)!=0:
        print('Berikut tampilan group beserta anggota dan ketua yang sudah terdaftar : ')
        for i in range(len(lst_group)):
            a=','
            print(lst_group[i][0]+' - ','Ketua :', a.join(lst_group[i][1])+' - ','Anggota :', a.join(lst_group[i][2]))
        print('Petunjuk : ')
        print('Jika telah selesai menambahkan anggota silahkan ketik' +' 0 '+'pada group yang ingin ditambah')
        pilihan_group=input('Group yang ingin ditambah:' + ' Group- ')
        if pilihan_group=='0':
            break
        elif not pilihan_group.isnumeric() or int(pilihan_group)>len(lst_group) or int(pilihan_group)<0:
            print('Maaf Inputan Anda Salah, anda hanya bisa memasukkan angka dan hanya antara 1 hingga '+str(len(lst_group)))
        elif len(lst_group[int(pilihan_group)-1][2])==30:
            print('Maaf anggota group ini sudah berjumlah 30 sehingga tidak dapat ditambah lagi')    
        else:
            nama_tambahan=input('Masukkan nama anggota baru :')
            while nama_tambahan=='' or nama_tambahan==' ' or check_special_char(nama_tambahan)==False:
                print('Maaf nama yang anda masukkan salah!')
                nama_tambahan=input('Masukkan nama anggota baru :')
            nama_tambahan=nama_tambahan.lower()
            if cek_nama_anggota(nama_tambahan,int(pilihan_group)-1)==True :
                lst_group[int(pilihan_group)-1][2].append(nama_tambahan)

def cek_ganti_ketua(nama,i):
    if nama in lst_group[i-1][1]:
        return True
    else:
        return False

def ganti_ketua():
    n=1
    while n!=0 :
        print('Berikut tampilan group dan ketua yang sudah terdaftar : ')
        for i in range(len(lst_group)):
            a=','
            print(lst_group[i][0]+' - ','Ketua :', a.join(lst_group[i][1]))
        print('Petunjuk : ')
        print('Jika ingin batal atau selesai silahkan ketik 0 pada nama yang diganti dan group dari nama tersebut')
        nama_yang_diganti=input('Masukkan nama yang ingin diganti = ')
        nama_yang_diganti=nama_yang_diganti.lower()
        group_dari_nama=input('Group dari '+nama_yang_diganti+' = ')
        if nama_yang_diganti =='0' or group_dari_nama=='0':
            break
        elif nama_yang_diganti==' ' or nama_yang_diganti=='' or check_special_char(nama_yang_diganti)==False:
            print('Nama yang Anda masukkan salah!')
        elif not group_dari_nama.isnumeric() or int(group_dari_nama)>len(lst_group) or int(group_dari_nama)<1:
            print('Invalid Group')
        elif cek_ganti_ketua(nama_yang_diganti,int(group_dari_nama))==False:
            print('Invalid nama atau group')
        else:
            nama_pengganti=input('Masukkan nama pengganti = ')
            while check_special_char(nama_pengganti)==False:
                print("Invalid Nama")
                nama_pengganti=input('Masukkan nama pengganti = ')
            nama_pengganti=nama_pengganti.lower()
            if insert_And_Check_team_leader_in_team(nama_pengganti,int(group_dari_nama)-1)==True:
                posisi_count=lst_leader_name.index(nama_yang_diganti)
                lst_leader_count[posisi_count]-=1
                posisi=lst_group[int(group_dari_nama)-1][1].index(nama_yang_diganti)
                lst_group[int(group_dari_nama)-1][1][posisi]=nama_pengganti
                if lst_leader_count[posisi_count]==0:
                    lst_leader_name.remove(nama_yang_diganti)
                    lst_leader_count.remove(0)

def cek_ganti_anggota(nama,i):
    if nama in lst_group[i-1][2]:
        return True
    else:
        return False

def ganti_anggota():
    n=1
    while n!=0 :
        print('Berikut tampilan group dan member yang sudah terdaftar : ')
        for i in range(len(lst_group)):
            a=','
            print(lst_group[i][0]+' - ','Anggota :', a.join(lst_group[i][2]))
        print('Petunjuk : ')
        print('Jika ingin batal atau selesai silahkan ketik 0 pada nama yang diganti dan group dari nama tersebut')
        nama_yang_diganti=input('Masukkan nama yang ingin diganti = ')
        nama_yang_diganti=nama_yang_diganti.lower()
        group_dari_nama=input('Group dari '+nama_yang_diganti+' = ')
        if nama_yang_diganti =='0' or group_dari_nama=='0':
            break
        elif nama_yang_diganti==' ' or nama_yang_diganti=='' or check_special_char(nama_yang_diganti)==False:
            print('Nama yang Anda masukkan salah!')
        elif not group_dari_nama.isnumeric() or int(group_dari_nama)>len(lst_group) or int(group_dari_nama)<1:
            print('Invalid Group')
        elif cek_ganti_anggota(nama_yang_diganti,int(group_dari_nama))==False:
            print('Invalid nama atau group')
        else:
            nama_pengganti=input('Masukkan nama pengganti = ')
            while check_special_char(nama_pengganti)==False:
                print("Invalid Nama")
                nama_pengganti=input('Masukkan nama pengganti = ')
            nama_pengganti=nama_pengganti.lower()
            if cek_nama_anggota(nama_pengganti,int(group_dari_nama)-1)==True:
                posisi_count=member.index(nama_yang_diganti)
                count_anggota[posisi_count]-=1
                posisi=lst_group[int(group_dari_nama)-1][2].index(nama_yang_diganti)
                lst_group[int(group_dari_nama)-1][2][posisi]=nama_pengganti
                if count_anggota[posisi_count]==0:
                    member.remove(nama_yang_diganti)
                    count_anggota.remove(0)
 
def remove_anggota():
    n=1
    while n!=0 :
        print('Berikut tampilan group dan member yang sudah terdaftar : ')
        for i in range(len(lst_group)):
            a=','
            print(lst_group[i][0]+' - ','Anggota :', a.join(lst_group[i][2]))
        print('Petunjuk :')
        print('Untuk batal atau kembali ke menu sebelumnya silahkan ketik 0 pada nama yang dihapus')
        nama_yang_dihapus=input('Masukkan nama yang ingin dihapus = ')
        nama_yang_dihapus=nama_yang_dihapus.lower()
        if nama_yang_dihapus=='0':
            break
        else:
            group_dari_nama=input('Group dari '+nama_yang_dihapus+' = ')
            if nama_yang_dihapus==' ' or nama_yang_dihapus=='':
                print('Nama yang Anda masukkan salah!')
            elif not group_dari_nama.isnumeric() or int(group_dari_nama)>len(lst_group) or int(group_dari_nama)<1:
                print('Invalid Group')
            elif cek_ganti_anggota(nama_yang_dihapus,int(group_dari_nama))==False:
                print('Invalid nama atau group')
            else:
                posisi=lst_group[int(group_dari_nama)-1][2].index(nama_yang_dihapus)
                del lst_group[int(group_dari_nama)-1][2][posisi]
                posisi_count=member.index(nama_yang_dihapus)
                count_anggota[posisi_count]-=1
                if count_anggota[posisi_count]==0:
                    member.remove(nama_yang_dihapus)
                    count_anggota.remove(0)

def ganti_anggota_ketua():
    pilihann='-1'
    while int(pilihann)!=0:
        print('==Ganti Ketua atau Anggota==')
        print('1. Ganti Ketua')
        print('2. Ganti Anggota')
        print('3. Remove Anggota')
        print('0. Back')
        pilihann=input('Masukkan pilihan menu = ')
        while not pilihann.isnumeric() or int(pilihann)>3 or int(pilihann)<0:
            print('Maaf Inputan Anda Salah, anda hanya bisa memasukkan angka dan hanya antara 1 hingga 2 serta 0 untuk exit')
            pilihann=input('Masukkan Pilihan Menu : ')
        if int(pilihann) == 1:
            ganti_ketua()
        elif int(pilihann)== 2:
            ganti_anggota()
        elif int(pilihann)==3:
            remove_anggota()

def main():
    print('==Welcome to Group Scheduler==')
    print('Untuk langkah awal silahkan masukkan banyaknya team yang akan dijadwalkan (Minimal. 7)')
    jumlahtim=input('Masukkan Banyaknya Team = ')
    while not jumlahtim.isnumeric() or int(jumlahtim) < 7 or int(jumlahtim) > 40:
        print('Jumlah tim minimal 7 dan maximal 40 dan harus dalam angka!')
        jumlahtim=input('Masukkan Banyaknya Tim = ')
    for i in range(1,int(jumlahtim)+1) :
        lst_group.append(['Group '+str(i)]) 
    for i in range((len(lst_group))):
        lst_group[i].append([])
        lst_group[i].append([])
    pilih_menu='-1'
    one,one1=1,1
    while int(pilih_menu)!=0:
        menu()
        pilih_menu=input('Masukkan Pilihan Menu : ')
        while not pilih_menu.isnumeric() or int(pilih_menu)>5 or int(pilih_menu)<0:
            print('Maaf Inputan Anda Salah, anda hanya bisa memasukkan angka dan hanya antara 1 hingga 5 serta 0 untuk exit')
            pilih_menu=input('Masukkan Pilihan Menu : ')
        if int(pilih_menu) == 1 :
            input_nama_ketua(one)
            one+=1
        elif int(pilih_menu) == 2 :
            input_nama_anggota(one1)
            one1+=1
        elif int(pilih_menu) ==3:
            tambah_anggota()
        elif int(pilih_menu)==4:
            ganti_anggota_ketua()
        elif int(pilih_menu) == 5:
            schedule()
main()