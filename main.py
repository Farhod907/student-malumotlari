import json
with open('student.json') as s_js:
    info  = json.load(s_js)
stop =False
while True:
    print("\n\t\tStudent information\n\n")
    
    
    print("1) Talaba Qo'shish")
    print("2) Talabalar Ro'yxati")
    print("3) Talabani Qidirish")
    print("4) Talabani O'chirish")
    print("5) Taxrirlash")
    print("6) To'xtatish\n")
    choose = input("Iltimos tanlang:  ")
    # info = []
    user_list={}
    if choose =='1':
        ism=input('Ism kiriting: ')
        user_list['ismi']=ism
        familiya = input('Familiyangizni kiriting: ')
        user_list['familiya']=familiya
        yosh = int(input('Yoshingizni kiriting: '))
        user_list['yosh']=yosh
        shaxar =input('Shaxringizni kiriting: ')
        user_list['shaxar']=shaxar
        info.append(user_list)
    # print(info)
        with open("student.json",'w') as s_js:
            json.dump(info,s_js)
    if choose =='2':
        for i in range(len(info)):
            ism = info[i]['ismi']
            fam = info[i]['familiya']
            yosh = info[i]['yosh']
            shaxar = info[i]['shaxar']
            
            print(f"Talaba Ismi = {ism.title()}\nFamiliyasi = {fam.title()}\nYoshi = {yosh}\nShaxari = {shaxar.title()}")
            print("_____________________________")
    
    if choose =='3':
        ism = input('Talaba Ismini kiriting: ')     
        yoq =True
        for i in range(len(info)):
            if ism.lower() ==info[i]['ismi'.lower()]:
                ism = info[i]['ismi']
                fam = info[i]['familiya']
                yosh = info[i]['yosh']
                shaxar = info[i]['shaxar']
                yoq = False
                
                print(f"\nTalaba Ismi = {ism.title()}\nFamiliyasi = {fam.title()}\nYoshi = {yosh}\nShaxari = {shaxar.title()}")
                print("_____________________________")
        if yoq:
            print('Kechirasiz Bunday ismli Talaba yoq?')
    if choose =='4':
        index = []
        ism = input("Ism kiriting: ")
        son=0
        for i in range(len(info)):
            if ism.lower() ==info[i]['ismi'.lower()]:
                ism = info[i]['ismi']
                fam = info[i]['familiya']
                son = i
                index.append(son)
                
                print(f"\nTalaba Ismi = {ism.title()}\nFamiliyasi = {fam.title()}\nO'chirish kod = {i}")
                print("_________________")
        tanla = int(input("Tanlang: "))
        print("Esda tuting arxivda qoladi!")
        arxiv = info.pop(tanla)
        with open('arxiv.json','a') as a_js:
            json.dump(arxiv,a_js)
        with open('student.json','w') as s_js:
            json.dump(info,s_js)
        print("O'chirildi")
    if choose =='5':
        ism = input('Ism Kiriting: ')
        for i in range(len(info)):
            if ism.lower()==info[i]['ismi'.lower()]:
                ism = info[i]['ismi']
                fam = info[i]['familiya']
                son = i
                
                print(f"\nTalaba Ismi = {ism.title()}\nFamiliyasi = {fam.title()}\nO'chirish kod = {i}")
                print("_________________")
        t = int(input("Tanlang: "))
        ism = info[t]['ismi']
        fam = info[t]['familiya']
        yosh = info[t]['yosh']
        print('1) Ism tahrirlash')
        print('2) Familiya tahrirlash')
        print('3) yosh tahrirlash')
        t1 = input('tanlang: ')
        if t1 == '1':
            ism = input("Ism kiriting: ")
            info[t]['ismi'] = ism
            print('Ism tastiqlandi')
        if t1 == '2':
            fam = input("Familiya kiriting: ")
            info[t]['familiya'] = fam
            print('Familiya tasdiqlandi')
        if t1 == '3':
            yosh = input("Ism kiriting: ")
            info[t]['yosh'] = yosh
            print('Yosh tasdiqlandi')
    if choose =='6':
        stop=True
    if stop:
        print("tizim To'xtadi")
        break
    
        

        
            
    
    
    
    