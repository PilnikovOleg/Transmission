# -*- coding: utf-8 -*-

#Импорт библиотек
from math import *
from array import *
from tkinter import *

#Задание констант
#КПД
performance1 = float(0.965) #КПД закрытой цилиндрической зубчатой передачи 0.95...0.98
performance2 = float(0.91) #КПД открытой цепной передачи 0.9...0.92
performance3 = float(0.94) #КПД открытой клиноременной передачи 0.93...0.95
performance4 = float(0.9925) #КПД одной пары подшипников качения 0.99...0.995
performance5 = float(0.985) #КПД муфт 0.98...0.99

#Передаточные числа
ur1 = float(4.0) #Передаточное число быстроходной цилиндрической передачи 3.15...4.0...5.0
ur2 = float(3.15) #Передаточное число тихоходной цилиндрической передачи 2.5...3.15...4.0
ur3 = float(4.0) #Передаточное число шевронной передачи 3.15...4.0...5.0

#Число зацеплений за один оборот колеса
c = 1
#Базовое число циклов при изгибе
NF0 = 4000000

#Коэффициент ширины зубчатого венца
fba1 = 0.4075 #Коэффициент ширины зубчатого венца при симметричном расположении передачи относительно опор 0.315...0.5
fba2 = 0.325 #При несимметричном 0.25...0.4
fba3 = 0.515 #Для шевронных передач 0.4...0.63

#Ряд стандартных чисел Ra=40
standart = [10, 10.5, 11, 11.5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 30, 32, 34, 36, 38, 40, 42, 45, 48, 50, 53, 56, 60, 63, 67, 71, 75, 80, 85, 90, 95, 100, 105, 110, 120, 125, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 240, 250, 260, 280, 300, 320, 340, 360, 380, 400, 420, 450, 480, 500, 530, 560, 600, 630, 670, 710, 750, 800, 850, 900, 950, 1000, 1060, 1120, 1180, 1250, 1320, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2120, 2240, 2360, 2500, 2650, 2800, 3000, 3150, 3350, 3750, 4000, 4250, 4500, 4750, 5000, 5300, 5600, 6000, 6300, 6700, 7100, 7500]

#Угол профиля зуба исходного контура
a = 20

#Выбор электродвигателя
def ElectroMotor():
    Po = float(Po_entry.get())
    no = float(no_entry.get())
    d_type = int(d_type_entry.get())
    global Pr
    if d_type == 0:
        Pr = Po/(performance1*performance3*(performance4**2)*performance5)
    else:
        Pr = Po/(performance1*performance2*(performance4**2)*performance5)
    ncmin = 5*no
    ncmax = 10*no
    E3000 = [
        [3000, 1.1, '71B2', 6.3, 19],
        [3000, 1.5, '80A2', 4.2, 22],
        [3000, 2.2, '80B2', 4.3, 22],
        [3000, 3.0, '90L2', 4.3, 24],
        [3000, 4.0, '100S2', 3.3, 28],
        [3000, 5.5, '100L2', 3.4, 28],
        [3000, 7.5, '112M2', 2.5, 32],
        [3000, 11, '132M2', 2.3, 38],
        [3000, 15, '160S2', 2.1, 42],
        [3000, 18.5, '160M2', 2.1, 42],
        [3000, 22, '180S2', 2.0, 48],
        [3000, 30, '180M2', 1.9, 48],
        [3000, 37, '200M2', 1.9, 55],
        [3000, 45, '200L2', 1.8, 55],
        [3000, 55, '225M2', 1.8, 55],
        [3000, 75, '250S2', 1.4, 65],
        [3000, 90, '250M2', 1.4, 65]
        ]
    E1500 = [
        [1500, 1.1, '80A4', 5.4, 22],
        [1500, 1.5, '80B4', 5.8, 22],
        [1500, 2.2, '90L4', 5.1, 24],
        [1500, 3.0, '100S4', 4.4, 28],
        [1500, 4.0, '100L4', 4.7, 28],
        [1500, 5.5, '112M4', 3.7, 32],
        [1500, 7.5, '132S4', 3.0, 38],
        [1500, 11, '132M4', 2.8, 38],
        [1500, 15, '160S4', 2.3, 48],
        [1500, 18.5, '160M4', 2.2, 48],
        [1500, 22, '180S4', 2.0, 55],
        [1500, 30, '180M4', 1.9, 55],
        [1500, 37, '200M4', 1.7, 60],
        [1500, 45, '200L4', 1.6, 60],
        [1500, 55, '225M4', 1.4, 65],
        [1500, 75, '250S4', 1.2, 75],
        [1500, 90, '250M4', 1.3, 75]
        ]
    E1000 = [
        [1000, 1.1, '80B6', 8.0, 22],
        [1000, 1.5, '90L6', 6.4, 24],
        [1000, 2.2, '100L6', 5.1, 28],
        [1000, 3.0, '112MA6', 4.7, 32],
        [1000, 4.0, '112MB6', 5.1, 32],
        [1000, 5.5, '132S6', 3.3, 38],
        [1000, 7.5, '132M6', 3.2, 38],
        [1000, 11, '160S6', 2.7, 48],
        [1000, 15, '160M6', 2.6, 48],
        [1000, 18.5, '180M6', 2.7, 55],
        [1000, 22, '200M6', 2.8, 60],
        [1000, 30, '200L6', 2.1, 60],
        [1000, 37, '225M6', 1.8, 65],
        [1000, 45, '250S6', 1.4, 75],
        [1000, 55, '250M6', 1.3, 75],
        [1000, 75, '280S6', 2.0, 80],
        [1000, 90, '9280M6', 2.0, 80]
        ]
    E750 = [
        [750, 1.1, '90LB8', 7.0, 24],
        [750, 1.5, '100L8', 7.0, 28],
        [750, 2.2, '112MA8', 6.0, 32],
        [750, 3.0, '112M8', 5.8, 32],
        [750, 4.0, '132S8', 4.1, 38],
        [750, 5.5, '132M8', 4.1, 38],
        [750, 7.5, '160S8', 2.5, 48],
        [750, 11, '160M8', 2.5, 48],
        [750, 15, '180M8', 2.5, 55],
        [750, 18.5, '200M8', 2.3, 60],
        [750, 22, '200L8', 2.7, 60],
        [750, 30, '225M8', 1.8, 65],
        [750, 37, '250S8', 1.5, 75],
        [750, 45, '250M8', 1.4, 75],
        [750, 55, '280S8', 2.2, 80],
        [750, 75, '280M8', 2.2, 80],
        [750, 90, '315S8', 2.0, 85]
        ]
    global nc
    global S
    global di
    if 375 <= ncmin <= 500:
        j = 1
        for i in range(0, len(E750)-1):
            if (Pr <= E750[i][j]):
                nc = E750[i][0]
                Pi = E750[i][j]
                model = E750[i][2]
                S = E750[i][3]
                di = E750[i][4]
                break
    elif 500 < ncmin <= 1000:
        j = 1
        for i in range(0, len(E1000)-1):
            if (Pr <= E1000[i][j]):
                nc = E1000[i][0]
                Pi = E1000[i][j]
                model = E1000[i][2]
                S = E1000[i][3]
                di = E1000[i][4]
                break
    elif 1000 < ncmin <= 1500:
        j = 1
        for i in range(0, len(E1500)-1):
            if (Pr <= E1500[i][j]):
                nc = E1500[i][0]
                Pi = E1500[i][j]
                model = E1500[i][2]
                S = E1500[i][3]
                di = E1500[i][4]
                break
    else:
        j = 1
        for i in range(0, len(E3000)-1):
            if (Pr <= E3000[i][j]):
                nc = E3000[i][0]
                Pi = E3000[i][j]
                model = E3000[i][2]
                S = E3000[i][3]
                di = E3000[i][4]
                break
    global Pr_string
    global ncmin_string
    global ncmax_string
    global nc_string
    global Pi_string
    global model_string
    global S_string
    Pr_string = str(round(Pr, 3))
    ncmin_string = str(ncmin)
    ncmax_string = str(ncmax)
    nc_string = str(nc)
    Pi_string = str(Pi)
    model_string = str(model)
    S_string = str(S)
    di_string = str(di)
    ElectroMotor_file = open('C:/Users/Public/Documents/ElectroMotor.txt', 'w')
    ElectroMotor_file.write('Pr = '+Pr_string+' кВт'+"\n")
    ElectroMotor_file.write('ncmin = '+ncmin_string+' об/мин'+"\n")
    ElectroMotor_file.write('ncmax = '+ncmax_string+' об/мин'+"\n")
    ElectroMotor_file.write('nc = '+nc_string+' об/мин'+"\n")
    ElectroMotor_file.write('Pi = '+Pi_string+' кВт'+"\n")
    ElectroMotor_file.write('model - '+model_string+"\n")
    ElectroMotor_file.write('S = '+S_string+' %'+"\n")
    ElectroMotor_file.write('di = '+di_string+' мм'+"\n")
    ElectroMotor_file.close()

#Основные параметры передачи
def MainParameters():
    Po = float(Po_entry.get())
    no = float(no_entry.get())
    g_type = int(g_type_entry.get())
    d_type = int(d_type_entry.get())
    scheme = int(scheme_entry.get())
    ni = nc*(1-S/100)
    ut = ni/no
    global u_add
    if (g_type == 0 or g_type == 1) and scheme == 1:
        u_add = ut/ur1
    elif (g_type == 0 or g_type == 1) and scheme == 0:
        u_add = ut/ur2
    else:
        u_add = ut/ur3
    global n0
    global n1
    global n2
    if scheme == 0 and (g_type == 0 or g_type == 1):
        n0 = ni
        n1 = n0/u_add
        n2 = n1/ur2
        n3 = n2
    elif scheme == 1 and (g_type == 0 or g_type == 1):
        n0 = ni
        n1 = n0
        n2 = n1/ur1
        n3 = n2/u_add
    elif scheme == 0 and g_type == 2:
        n0 = ni
        n1 = n0/u_add
        n2 = n1/ur3
        n3 = n2
    else:
        n0 = ni
        n1 = n0
        n2 = n1/ur3
        n3 = n2/u_add
    if scheme == 0 and d_type == 0:
        P0 = Pr
        P1 = P0*performance3*performance4
        P2 = P1*performance1*performance4
        P3 = P2*performance5
    elif scheme == 0 and d_type == 1:
        P0 = Pr
        P1 = P0*performance2*performance4
        P2 = P1*performance1*performance4
        P3 = P2*performance5
    elif scheme == 1 and d_type == 0:
        P0 = Pr
        P1 = P0*performance5*performance4
        P2 = P1*performance1*performance4
        P3 = P2*performance3
    else:
        P0 = Pr
        P1 = P0*performance5*performance4
        P2 = P1*performance1*performance4
        P3 = P2*performance2
    global T0
    global T1
    global T2
    T0 = 9550*P0/n0
    T1 = 9550*P1/n1
    T2 = 9550*P2/n2
    T3 = 9550*P3/n3
    global ni_string
    global ut_string
    global u_add_string
    global n0_string
    global n1_string
    global n2_string
    global n3_string
    global P0_string
    global P1_string
    global P2_string
    global P3_string
    global T0_string
    global T1_string
    global T2_string
    global T3_string
    ni_string = str(round(ni, 3))
    ut_string = str(round(ut, 3))
    u_add_string = str(round(u_add, 3))
    n0_string = str(round(n0, 3))
    n1_string = str(round(n1, 3))
    n2_string = str(round(n2, 3))
    n3_string = str(round(n3, 3))
    P0_string = str(round(P0, 3))
    P1_string = str(round(P1, 3))
    P2_string = str(round(P2, 3))
    P3_string = str(round(P3, 3))
    T0_string = str(round(T0, 3))
    T1_string = str(round(T1, 3))
    T2_string = str(round(T2, 3))
    T3_string = str(round(T3, 3))
    MainParameters_file = open('C:/Users/Public/Documents/MainParameters.txt', 'w')
    MainParameters_file.write('ni = '+ni_string+' об/мин'+"\n")
    MainParameters_file.write('ut = '+ut_string+"\n")
    MainParameters_file.write('u_add = '+u_add_string+"\n")
    MainParameters_file.write('n0 = '+n0_string+' об/мин'+"\n")
    MainParameters_file.write('n1 = '+n1_string+' об/мин'+"\n")
    MainParameters_file.write('n2 = '+n2_string+' об/мин'+"\n")
    MainParameters_file.write('n3 = '+n3_string+' об/мин'+"\n")
    MainParameters_file.write('P0 = '+P0_string+' кВт'+"\n")
    MainParameters_file.write('P1 = '+P1_string+' кВт'+"\n")
    MainParameters_file.write('P2 = '+P2_string+' кВт'+"\n")
    MainParameters_file.write('P3 = '+P3_string+' кВт'+"\n")
    MainParameters_file.write('T0 = '+T0_string+' Нм'+"\n")
    MainParameters_file.write('T1 = '+T1_string+' Нм'+"\n")
    MainParameters_file.write('T2 = '+T2_string+' Нм'+"\n")
    MainParameters_file.write('T3 = '+T3_string+' Нм'+"\n")
    MainParameters_file.close()

#Выбор материалов зубчатых колес
def ChoiceMaterial():
    g_type = int(g_type_entry.get())
    scheme = int(scheme_entry.get())
    if g_type == 0:
        km = 24
    else:
        km = 20
    global ur
    if scheme == 0 and (g_type == 0 or g_type == 1):
        ur = ur2
    elif scheme == 1 and (g_type == 0 or g_type == 1):
        ur = ur1
    else:
        ur = ur3
    global Dm
    global Sm
    global dk
    Dm = km*((T1/ur)**(1/3))
    Sm = 1.2*(1+ur)*((T1/ur)**(1/3))
    dk = ur*Dm
    def Choice():
        global brand1
        global Dm1
        global Sm1
        global heat1
        global HBmin1
        global HBmax1
        global sb1
        global NH01
        if var.get() == 0:
            brand1 = 'Сталь 35'
            Dm1 = 'Любой'
            Sm1 = 'Любой'
            heat1 = 'Н'
            HBmin1 = 163
            HBmax1 = 192
            sb1 = 550
            NH01 = 2.5*1000000
        elif var.get() == 1:
            brand1 = 'Сталь 40'
            Dm1 = 120
            Sm1 = 60
            heat1 = 'У'
            HBmin1 = 192
            HBmax1 = 228
            sb1 = 700
            NH01 = 11.2*1000000
        elif var.get() == 2:
            brand1 = 'Сталь 45'
            Dm1 = 'Любой'
            Sm1 = 'Любой'
            heat1 = 'Н'
            HBmin1 = 179
            HBmax1 = 207
            sb1 = 600
            NH01 = 9.17*1000000
        elif var.get() == 3:
            brand1 = 'Сталь 45'
            Dm1 = 125
            Sm1 = 80
            heat1 = 'У'
            HBmin1 = 235
            HBmax1 = 262
            sb1 = 780
            NH01 = 16.8*1000000
        elif var.get() == 4:
            brand1 = 'Сталь 45'
            Dm1 = 80
            Sm1 = 50
            heat1 = 'У'
            HBmin1 = 269
            HBmax1 = 302
            sb1 = 890
            NH01 = 23.5*1000000
        elif var.get() == 5:
            brand1 = 'Сталь 40Х'
            Dm1 = 200
            Sm1 = 125
            heat1 = 'У'
            HBmin1 = 235
            HBmax1 = 262
            sb1 = 790
            NH01 = 16.8*1000000
        elif var.get() == 6:
            brand1 = 'Сталь 40Х'
            Dm1 = 125
            Sm1 = 80
            heat1 = 'У'
            HBmin1 = 269
            HBmax1 = 302
            sb1 = 900
            NH01 = 23.5*1000000
        elif var.get() == 7:
            brand1 = 'Сталь 40Х'
            Dm1 = 125
            Sm1 = 80
            heat1 = 'У+З(ТВЧ)'
            HBmin1 = 409
            HBmax1 = 470
            sb1 = 900
            NH01 = 73.0*1000000
        elif var.get() == 8:
            brand1 = 'Сталь 40ХН'
            Dm1 = 315
            Sm1 = 200
            heat1 = 'У'
            HBmin1 = 235
            HBmax1 = 262
            sb1 = 800
            NH01 = 16.8*1000000
        elif var.get() == 9:
            brand1 = 'Сталь 40ХН'
            Dm1 = 200
            Sm1 = 125
            heat1 = 'У'
            HBmin1 = 269
            HBmax1 = 302
            sb1 = 920
            NH01 = 23.5*1000000
        elif var.get() == 10:
            brand1 = 'Сталь 40ХН'
            Dm1 = 200
            Sm1 = 125
            heat1 = 'У+З(ТВЧ)'
            HBmin1 = 444
            HBmax1 = 511
            sb1 = 920
            NH01 = 86.9*1000000
        elif var.get() == 11:
            brand1 = 'Сталь 35ХМ'
            Dm1 = 315
            Sm1 = 200
            heat1 = 'У'
            HBmin1 = 235
            HBmax1 = 262
            sb1 = 800
            NH01 = 16.8*1000000
        elif var.get() == 12:
            brand1 = 'Сталь 35ХМ'
            Dm1 = 200
            Sm1 = 125
            heat1 = 'У'
            HBmin1 = 269
            HBmax1 = 302
            sb1 = 920
            NH01 = 23.5*1000000
        elif var.get() == 13:
            brand1 = 'Сталь 35ХМ'
            Dm1 = 200
            Sm1 = 125
            heat1 = 'У+З(ТВЧ)'
            HBmin1 = 444
            HBmax1 = 511
            sb1 = 920
            NH01 = 86.9*1000000
        elif var.get() == 14:
            brand1 = 'Сталь 20Х'
            Dm1 = 200
            Sm1 = 125
            heat1 = 'У+Ц+З'
            HBmin1 = 538
            HBmax1 = 632
            sb1 = 1000
            NH01 = 120.0*1000000
        elif var.get() == 15:
            brand1 = 'Сталь 20ХНМ'
            Dm1 = 200
            Sm1 = 125
            heat1 = 'У+Ц+З'
            HBmin1 = 538
            HBmax1 = 632
            sb1 = 1000
            NH01 = 120.0*1000000
        elif var.get() == 16:
            brand1 = '18ХГТ'
            Dm1 = 200
            Sm1 = 125
            heat1 = 'У+Ц+З'
            HBmin1 = 538
            HBmax1 = 632
            sb1 = 1000
            NH01 = 120.0*1000000
        elif var.get() == 17:
            brand1 = '35Л'
            Dm1 = 'Любой'
            Sm1 = 'Любой'
            heat1 = 'Н'
            HBmin1 = 163
            HBmax1 = 207
            sb1 = 550
            NH01 = 8.3*1000000
        else:
            brand1 = '45Л'
            Dm1 = 315
            Sm1 = 200
            heat1 = 'У'
            HBmin1 = 207
            HBmax1 = 235
            sb1 = 680
            NH01 = 12.7*1000000
        global brand2
        global Dm2
        global Sm2
        global heat2
        global HBmin2
        global HBmax2
        global sb2
        global NH02
        if var1.get() == 0:
            brand2 = 'Сталь 35'
            Dm2 = 'Любой'
            Sm2 = 'Любой'
            heat2 = 'Н'
            HBmin2 = 163
            HBmax2 = 192
            sb2 = 550
            NH02 = 2.5*1000000
        elif var1.get() == 1:
            brand2 = 'Сталь 40'
            Dm2 = 120
            Sm2 = 60
            heat2 = 'У'
            HBmin2 = 192
            HBmax2 = 228
            sb2 = 700
            NH02 = 11.2*1000000
        elif var1.get() == 2:
            brand2 = 'Сталь 45'
            Dm2 = 'Любой'
            Sm2 = 'Любой'
            heat2 = 'Н'
            HBmin2 = 179
            HBmax2 = 207
            sb2 = 600
            NH02 = 9.17*1000000
        elif var1.get() == 3:
            brand2 = 'Сталь 45'
            Dm2 = 125
            Sm2 = 80
            heat2 = 'У'
            HBmin2 = 235
            HBmax2 = 262
            sb2 = 780
            NH02 = 16.8*1000000
        elif var1.get() == 4:
            brand2 = 'Сталь 45'
            Dm2 = 80
            Sm2 = 50
            heat2 = 'У'
            HBmin2 = 269
            HBmax2 = 302
            sb2 = 890
            NH02 = 23.5*1000000
        elif var1.get() == 5:
            brand2 = 'Сталь 40Х'
            Dm2 = 200
            Sm2 = 125
            heat2 = 'У'
            HBmin2 = 235
            HBmax2 = 262
            sb2 = 790
            NH02 = 16.8*1000000
        elif var1.get() == 6:
            brand2 = 'Сталь 40Х'
            Dm2 = 125
            Sm2 = 80
            heat2 = 'У'
            HBmin2 = 269
            HBmax2 = 302
            sb2 = 900
            NH02 = 23.5*1000000
        elif var1.get() == 7:
            brand2 = 'Сталь 40Х'
            Dm2 = 125
            Sm2 = 80
            heat2 = 'У+З(ТВЧ)'
            HBmin2 = 409
            HBmax2 = 470
            sb2 = 900
            NH02 = 73.0*1000000
        elif var1.get() == 8:
            brand2 = 'Сталь 40ХН'
            Dm2 = 315
            Sm2 = 200
            heat2 = 'У'
            HBmin2 = 235
            HBmax2 = 262
            sb2 = 800
            NH02 = 16.8*1000000
        elif var1.get() == 9:
            brand2 = 'Сталь 40ХН'
            Dm2 = 200
            Sm2 = 125
            heat2 = 'У'
            HBmin2 = 269
            HBmax2 = 302
            sb2 = 920
            NH02 = 23.5*1000000
        elif var1.get() == 10:
            brand2 = 'Сталь 40ХН'
            Dm2 = 200
            Sm2 = 125
            heat2 = 'У+З(ТВЧ)'
            HBmin2 = 444
            HBmax2 = 511
            sb2 = 920
            NH02 = 86.9*1000000
        elif var1.get() == 11:
            brand2 = 'Сталь 35ХМ'
            Dm2 = 315
            Sm2 = 200
            heat2 = 'У'
            HBmin2 = 235
            HBmax2 = 262
            sb2 = 800
            NH02 = 16.8*1000000
        elif var1.get() == 12:
            brand2 = 'Сталь 35ХМ'
            Dm2 = 200
            Sm2 = 125
            heat2 = 'У'
            HBmin2 = 269
            HBmax2 = 302
            sb2 = 920
            NH02 = 23.5*1000000
        elif var1.get() == 13:
            brand2 = 'Сталь 35ХМ'
            Dm2 = 200
            Sm2 = 125
            heat2 = 'У+З(ТВЧ)'
            HBmin2 = 444
            HBmax2 = 511
            sb2 = 920
            NH02 = 86.9*1000000
        elif var1.get() == 14:
            brand2 = 'Сталь 20Х'
            Dm2 = 200
            Sm2 = 125
            heat2 = 'У+Ц+З'
            HBmin2 = 538
            HBmax2 = 632
            sb2 = 1000
            NH02 = 120.0*1000000
        elif var1.get() == 15:
            brand2 = 'Сталь 20ХНМ'
            Dm2 = 200
            Sm2 = 125
            heat2 = 'У+Ц+З'
            HBmin2 = 538
            HBmax2 = 632
            sb2 = 1000
            NH02 = 120.0*1000000
        elif var1.get() == 16:
            brand2 = '18ХГТ'
            Dm2 = 200
            Sm2 = 125
            heat2 = 'У+Ц+З'
            HBmin2 = 538
            HBmax2 = 632
            sb2 = 1000
            NH02 = 120.0*1000000
        elif var1.get() == 17:
            brand2 = '35Л'
            Dm2 = 'Любой'
            Sm2 = 'Любой'
            heat2 = 'Н'
            HBmin2 = 163
            HBmax2 = 207
            sb2 = 550
            NH02 = 8.3*1000000
        else:
            brand2 = '45Л'
            Dm2 = 315
            Sm2 = 200
            heat2 = 'У'
            HBmin2 = 207
            HBmax2 = 235
            sb2 = 680
            NH02 = 12.7*1000000
    
    choice = Toplevel()
    choice.title('Материал зубчатых колес')
    choice.geometry()

    var = IntVar()
    var.set(0)
    var1 = IntVar()
    var1.set(0)

    frame0 = Frame(choice)
    frame0.grid(row=0, column=0)
    Dm_label0 = Label(frame0, text='Dm = ').grid(row=0, column=0)
    Dm_label1 = Label(frame0, text=round(Dm, 3)).grid(row=0, column=1)
    Dm_label2 = Label(frame0, text='Sm = ').grid(row=1, column=0)
    Dm_label3 = Label(frame0, text=round(Sm, 3)).grid(row=1, column=1)
    Dm_label4 = Label(frame0, text='dk = ').grid(row=2, column=0)
    Dm_label5 = Label(frame0, text=round(dk, 3)).grid(row=2, column=1)

    frame1 = Frame(choice)
    frame1.grid(row=1, column=0)
    material_label1 = Label(frame1, text='Метериал ведущего зубчатого колеса').grid(row=0, column=0)
    mmaterial1 = Radiobutton(frame1, text='Сталь 35, Dm - любой, Sm - любой, Термообработка - Н, HBmin-HBmax = 163-192 HB, Предел прочности 550 МПа, N0 = 2.5 млн.', variable=var, value=0).grid(row=1, column=0)
    mmaterial2 = Radiobutton(frame1, text='Сталь 40, Dm - 120 мм, Sm - 60 мм, Термообработка - У, HBmin-HBmax = 192-228 HB, Предел прочности 700 МПа, N0 = 11.2 млн.', variable=var, value=1).grid(row=2, column=0)
    mmaterial3 = Radiobutton(frame1, text='Сталь 45, Dm - любой, Sm - любой, Термообработка - Н, HBmin-HBmax = 179-207 HB, Предел прочности 600 МПа, N0 = 9.17 млн.', variable=var, value=2).grid(row=3, column=0)
    mmaterial4 = Radiobutton(frame1, text='Сталь 45, Dm - 125 мм, Sm - 80 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности 780 МПа, N0 = 16.8 млн.', variable=var, value=3).grid(row=4, column=0)
    mmaterial5 = Radiobutton(frame1, text='Сталь 45, Dm - 80 мм, Sm - 50 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности 890 МПа, N0 = 23.5 млн.', variable=var, value=4).grid(row=5, column=0)
    mmaterial6 = Radiobutton(frame1, text='Сталь 40Х, Dm - 200 мм, Sm - 125 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности 790 МПа, N0 = 16.8 млн.', variable=var, value=5).grid(row=6, column=0)
    mmaterial7 = Radiobutton(frame1, text='Сталь 40Х, Dm - 125 мм, Sm - 80 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности 900 МПа, N0 = 23.5 млн.', variable=var, value=6).grid(row=7, column=0)
    mmaterial8 = Radiobutton(frame1, text='Сталь 40Х, Dm - 125 мм, Sm - 80 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 45-50 HRCэ, Предел прочности 900 МПа, N0 = 73.0 млн.', variable=var, value=7).grid(row=8, column=0)
    mmaterial9 = Radiobutton(frame1, text='Сталь 40ХН, Dm - 315 мм, Sm - 200 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности 800 МПа, N0 = 16.8 млн.', variable=var, value=8).grid(row=9, column=0)
    mmaterial10 = Radiobutton(frame1, text='Сталь 40ХН, Dm - 200 мм, Sm - 125 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности 920 МПа, N0 = 23.5 млн.', variable=var, value=9).grid(row=10, column=0)
    mmaterial11 = Radiobutton(frame1, text='Сталь 40ХН, Dm - 200 мм, Sm - 125 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 48-53 HRCэ, Предел прочности 920 МПа, N0 = 86.9 млн.', variable=var, value=10).grid(row=11, column=0)
    mmaterial12 = Radiobutton(frame1, text='Сталь 35ХМ, Dm - 315 мм, Sm - 200 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности 800 МПа, N0 = 16.8 млн.', variable=var, value=11).grid(row=12, column=0)
    mmaterial13 = Radiobutton(frame1, text='Сталь 35ХМ, Dm - 200 мм, Sm - 125 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности 920 МПа, N0 = 23.5 млн.', variable=var, value=12).grid(row=13, column=0)
    mmaterial14 = Radiobutton(frame1, text='Сталь 35ХМ, Dm - 200 мм, Sm - 125 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 48-53 HRCэ, Предел прочности 920 МПа, N0 = 86.9 млн.', variable=var, value=13).grid(row=14, column=0)
    mmaterial15 = Radiobutton(frame1, text='Сталь 20Х, Dm - 200 мм, Sm - 125 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности 1000 МПа, N0 = 120.0 млн.', variable=var, value=14).grid(row=15, column=0)
    mmaterial16 = Radiobutton(frame1, text='Сталь 20ХНМ, Dm - 200 мм, Sm - 125 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности 1000 МПа, N0 = 120.0 млн.', variable=var, value=15).grid(row=16, column=0)
    mmaterial17 = Radiobutton(frame1, text='Сталь 18ХГТ, Dm - 200 мм, Sm - 125 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности 1000 МПа, N0 = 120.0 млн.', variable=var, value=16).grid(row=17, column=0)
    mmaterial18 = Radiobutton(frame1, text='Сталь 35Л, Dm - любой, Sm - любой, Термообработка - Н, HBmin-HBmax = 163-207 HB, Предел прочности 550 МПа, N0 = 8.3 млн.', variable=var, value=17).grid(row=18, column=0)
    mmaterial19 = Radiobutton(frame1, text='Сталь 45Л, Dm - 315 мм, Sm - 200 мм, Термообработка - У, HBmin-HBmax = 207-235 HB, Предел прочности 680 МПа, N0 = 12.7 млн.', variable=var, value=18).grid(row=19, column=0)

    frame2 = Frame(choice)
    frame2.grid(row=1, column=1)
    material_label2 = Label(frame2, text='Метериал ведомого зубчатого колеса').grid(row=0, column=0)
    mmaterial1 = Radiobutton(frame2, text='Сталь 35, Dm - любой, Sm - любой, Термообработка - Н, HBmin-HBmax = 163-192 HB, Предел прочности 550 МПа, N0 = 2.5 млн.', variable=var1, value=0).grid(row=1, column=0)
    mmaterial2 = Radiobutton(frame2, text='Сталь 40, Dm - 120 мм, Sm - 60 мм, Термообработка - У, HBmin-HBmax = 192-228 HB, Предел прочности 700 МПа, N0 = 11.2 млн.', variable=var1, value=1).grid(row=2, column=0)
    mmaterial3 = Radiobutton(frame2, text='Сталь 45, Dm - любой, Sm - любой, Термообработка - Н, HBmin-HBmax = 179-207 HB, Предел прочности 600 МПа, N0 = 9.17 млн.', variable=var1, value=2).grid(row=3, column=0)
    mmaterial4 = Radiobutton(frame2, text='Сталь 45, Dm - 125 мм, Sm - 80 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности 780 МПа, N0 = 16.8 млн.', variable=var1, value=3).grid(row=4, column=0)
    mmaterial5 = Radiobutton(frame2, text='Сталь 45, Dm - 80 мм, Sm - 50 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности 890 МПа, N0 = 23.5 млн.', variable=var1, value=4).grid(row=5, column=0)
    mmaterial6 = Radiobutton(frame2, text='Сталь 40Х, Dm - 200 мм, Sm - 125 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности 790 МПа, N0 = 16.8 млн.', variable=var1, value=5).grid(row=6, column=0)
    mmaterial7 = Radiobutton(frame2, text='Сталь 40Х, Dm - 125 мм, Sm - 80 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности 900 МПа, N0 = 23.5 млн.', variable=var1, value=6).grid(row=7, column=0)
    mmaterial8 = Radiobutton(frame2, text='Сталь 40Х, Dm - 125 мм, Sm - 80 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 45-50 HRCэ, Предел прочности 900 МПа, N0 = 73.0 млн.', variable=var1, value=7).grid(row=8, column=0)
    mmaterial9 = Radiobutton(frame2, text='Сталь 40ХН, Dm - 315 мм, Sm - 200 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности 800 МПа, N0 = 16.8 млн.', variable=var1, value=8).grid(row=9, column=0)
    mmaterial10 = Radiobutton(frame2, text='Сталь 40ХН, Dm - 200 мм, Sm - 125 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности 920 МПа, N0 = 23.5 млн.', variable=var1, value=9).grid(row=10, column=0)
    mmaterial11 = Radiobutton(frame2, text='Сталь 40ХН, Dm - 200 мм, Sm - 125 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 48-53 HRCэ, Предел прочности 920 МПа, N0 = 86.9 млн.', variable=var1, value=10).grid(row=11, column=0)
    mmaterial12 = Radiobutton(frame2, text='Сталь 35ХМ, Dm - 315 мм, Sm - 200 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности 800 МПа, N0 = 16.8 млн.', variable=var1, value=11).grid(row=12, column=0)
    mmaterial13 = Radiobutton(frame2, text='Сталь 35ХМ, Dm - 200 мм, Sm - 125 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности 920 МПа, N0 = 23.5 млн.', variable=var1, value=12).grid(row=13, column=0)
    mmaterial14 = Radiobutton(frame2, text='Сталь 35ХМ, Dm - 200 мм, Sm - 125 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 48-53 HRCэ, Предел прочности 920 МПа, N0 = 86.9 млн.', variable=var1, value=13).grid(row=14, column=0)
    mmaterial15 = Radiobutton(frame2, text='Сталь 20Х, Dm - 200 мм, Sm - 125 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности 1000 МПа, N0 = 120.0 млн.', variable=var1, value=14).grid(row=15, column=0)
    mmaterial16 = Radiobutton(frame2, text='Сталь 20ХНМ, Dm - 200 мм, Sm - 125 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности 1000 МПа, N0 = 120.0 млн.', variable=var1, value=15).grid(row=16, column=0)
    mmaterial17 = Radiobutton(frame2, text='Сталь 18ХГТ, Dm - 200 мм, Sm - 125 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности 1000 МПа, N0 = 120.0 млн.', variable=var1, value=16).grid(row=17, column=0)
    mmaterial18 = Radiobutton(frame2, text='Сталь 35Л, Dm - любой, Sm - любой, Термообработка - Н, HBmin-HBmax = 163-207 HB, Предел прочности 550 МПа, N0 = 8.3 млн.', variable=var1, value=17).grid(row=18, column=0)
    mmaterial19 = Radiobutton(frame2, text='Сталь 45Л, Dm - 315 мм, Sm - 200 мм, Термообработка - У, HBmin-HBmax = 207-235 HB, Предел прочности 680 МПа, N0 = 12.7 млн.', variable=var1, value=18).grid(row=19, column=0)

    frame3 = Frame(choice)
    frame3.grid(row=3, column=0)
    choice_button = Button(frame3, text='Назначить', command=Choice, bg = 'light green').grid(row=0, column=0)
    close_button = Button(frame3, text='Завершить', command=choice.destroy, bg = 'light pink').grid(row=1, column=0)

#Расчет зубчатой передачи
def CalculationGear():
    sl = float(sl_entry.get())
    c_y = float(c_y_entry.get())
    c_d = float(c_d_entry.get())
    dc = float(dc_entry.get())
    t_mode = int(t_mode_entry.get())
    t_type = int(t_type_entry.get())
    g_type = int(g_type_entry.get())
    d_type = int(d_type_entry.get())
    scheme = int(scheme_entry.get())
    #Определение допускаемых контактных напряжений
    HB1 = 0.5*(HBmin1+HBmax1)
    HB2 = 0.5*(HBmin2+HBmax2)
    sHlim1 = 2*HB1+70
    sHlim2 = 2*HB2+70
    Lh = 365*sl*24*c_y*c_d*(dc/100)
    Ns1 = 60*n1*c*Lh
    Ns2 = Ns1/ur
    if t_mode == 0:
        mh = 1.0
    elif t_mode == 1:
        mh = 0.5
    elif t_mode == 2:
        mh = 0.25
    elif t_mode == 3:
        mh = 0.18
    elif t_mode == 4:
        mh = 0.125
    else:
        mh = 0.063
    NHE1 = mh*Ns1
    NHE2 = mh*Ns2
    if NHE1 > NH01:
        KHL1 = 1
    else:
        KHL1 = (NH01/NHE1)**(1/6)
    if NHE2 > NH02:
        KHL2 = 1
    else:
        KHL2 = (NH02/NHE2)**(1/6)
    if heat1 == 'У':
        SH1 = 1.1
    else:
        SH1 = 1.2
    if heat2 == 'У' or heat2 == 'Н':
        SH2 = 1.1
    else:
        SH2 = 1.2
    sHP1 = (sHlim1*KHL1)/SH1
    sHP2 = (sHlim2*KHL2)/SH2
    if sHP1 < sHP2:
        sHPmin = sHP1
    else:
        sHPmin = sHP2
    sHP = 0.45*(sHP1+sHP2)
    s1HP = 1.23*sHPmin
    #Определение допускаемых напряжений изгиба
    sFlim1 = 1.75*HB1
    sFlim2 = 1.75*HB2
    if t_mode == 0 and (heat1 == 'У' or heat1 == 'Н'):
        mf1 = 1.0
    elif t_mode == 1 and (heat1 == 'У' or heat1 == 'Н'):
        mf1 = 0.3
    elif t_mode == 2 and (heat1 == 'У' or heat1 == 'Н'):
        mf1 = 0.14
    elif t_mode == 3 and (heat1 == 'У' or heat1 == 'Н'):
        mf1 = 0.06
    elif t_mode == 4 and (heat1 == 'У' or heat1 == 'Н'):
        mf1 = 0.038
    elif t_mode == 5 and (heat1 == 'У' or heat1 == 'Н'):
        mf1 = 0.013
    elif t_mode == 0 and (heat1 == 'У+З(ТВЧ)' or heat1 == 'У+Ц+З'):
        mf1 = 1.0
    elif t_mode == 1 and (heat1 == 'У+З(ТВЧ)' or heat1 == 'У+Ц+З'):
        mf1 = 0.2
    elif t_mode == 2 and (heat1 == 'У+З(ТВЧ)' or heat1 == 'У+Ц+З'):
        mf1 = 0.1
    elif t_mode == 3 and (heat1 == 'У+З(ТВЧ)' or heat1 == 'У+Ц+З'):
        mf1 = 0.04
    elif t_mode == 4 and (heat1 == 'У+З(ТВЧ)' or heat1 == 'У+Ц+З'):
        mf1 = 0.016
    else:
        mf1 = 0.004
    if t_mode == 0 and (heat2 == 'У' or heat2 == 'Н'):
        mf2 = 1.0
    elif t_mode == 1 and (heat2 == 'У' or heat2 == 'Н'):
        mf2 = 0.3
    elif t_mode == 2 and (heat2 == 'У' or heat2 == 'Н'):
        mf2 = 0.14
    elif t_mode == 3 and (heat2 == 'У' or heat2 == 'Н'):
        mf2 = 0.06
    elif t_mode == 4 and (heat2 == 'У' or heat2 == 'Н'):
        mf2 = 0.038
    elif t_mode == 5 and (heat2 == 'У' or heat2 == 'Н'):
        mf2 = 0.013
    elif t_mode == 0 and (heat2 == 'У+З(ТВЧ)' or heat2 == 'У+Ц+З'):
        mf2 = 1.0
    elif t_mode == 1 and (heat2 == 'У+З(ТВЧ)' or heat2 == 'У+Ц+З'):
        mf2 = 0.2
    elif t_mode == 2 and (heat2 == 'У+З(ТВЧ)' or heat2 == 'У+Ц+З'):
        mf2 = 0.1
    elif t_mode == 3 and (heat2 == 'У+З(ТВЧ)' or heat2 == 'У+Ц+З'):
        mf2 = 0.04
    elif t_mode == 4 and (heat2 == 'У+З(ТВЧ)' or heat2 == 'У+Ц+З'):
        mf2 = 0.016
    else:
        mf2 = 0.004
    NFE1 = mf1*Ns1
    NFE2 = mf2*Ns2
    if heat1 == 'У' or heat1 == 'Н':
        q1 = 6
    else:
        q1 = 9
    if heat2 == 'У' or heat2 == 'Н':
        q2 = 6
    else:
        q2 = 9
    if NFE1 > NF0:
        KFL1 = 1
    else:
        KFL1 = ((NF0/NFE1)**(1/q1))
    if NFE2 > NF0:
        KFL2 = 1
    else:
        KFL2 = ((NF0/NFE2)**(1/q2))
    if t_type == 0 and (heat1 == 'У' or heat1 == 'Н'):
        KFC1 = 0.65
    elif t_type == 0 and (heat1 == 'У+З(ТВЧ)' or heat1 == 'У+Ц+З'):
        KFC1 = 0.75
    else:
        KFC1 = 1
    if t_type == 0 and (heat2 == 'У' or heat2 == 'Н'):
        KFC2 = 0.65
    elif t_type == 0 and (heat2 == 'У+З(ТВЧ)' or heat2 == 'У+Ц+З'):
        KFC2 = 0.75
    else:
        KFC2 = 1
    if heat1 == 'У+Ц+З':
        Sf1 = 1.65
    else:
        Sf1 = 1.7
    if heat2 == 'У+Ц+З':
        Sf2 = 1.65
    else:
        Sf2 = 1.7
    sFP1 = (sFlim1*KFL1*KFC1)/Sf1
    sFP2 = (sFlim2*KFL2*KFC2)/Sf2
    #Проектный расчет зубчатой передачи
    if g_type == 0:
        Ka = 450
    else:
        Ka = 410
    KH = 1.2
    if g_type == 2:
        fba = fba3
    else:
        fba = fba1
    global aw
    aw = Ka*(ur+1)*(((KH*T1)/(fba*ur*(sHP**2)))**(1/3))
    aws = [
        [40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000],
        [71, 90, 112, 140, 180, 225, 280, 355, 450, 560, 710, 900, 1120, 1400]
        ]
    i = 0
    j = 0
    for j in range(0, len(aws[0])-1):
        if (aw <= aws[i][j]):
            aw1 = aws[i][j]
            break
    i = 1
    j = 0
    for j in range(0, len(aws[1])-1):
        if (aw <= aws[i][j]):
            aw2 = aws[i][j]
            break
    if aw1 <= aw2:
        aw = aw1
    else:
        aw = aw2
    mnmin = 0.01*aw
    mnmax = 0.02*aw
    mn1 = []
    mn2 = []
    mns = [
        [1, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10],
        [1.125, 1.375, 1.75, 2.25, 2.75, 3.5, 4.5, 5.5, 7, 9]
        ]
    i = 0
    for j in range(0, len(mns[0])-1):
        if (mnmin <= mns[i][j] and mnmax > mns[i][j]):
            mn1.append(mns[i][j])
    i = 1
    for j in range(0, len(mns[1])-1):
        if (mnmin <= mns[i][j] and mnmax > mns[i][j]):
            mn2.append(mns[i][j])
    k = len(mn1)%2
    global mn
    mn = mn1[k]
    if g_type == 0:
        B1 = 0
    elif g_type == 1:
        B1 = 12
    else:
        B1 = 30
    Zs1 = (2*aw*cos(B1*pi/180))/mn
    Zs = round(Zs1, 0)
    global B
    B = (acos(Zs*mn*0.5/aw))*(180/pi)
    Z1 = Zs/(ur+1)
    Z1 = round(Z1, 0)
    Z2 = Zs-Z1
    x1 = 0
    x2 = 0
    uf = Z2/Z1
    du = ((ur-uf)/ur)*100
    global bw2
    bw2 = fba*aw
    for i in range(0, len(standart)-1):
        if (bw2 <= standart[i]):
            bw2 = standart[i]
            break
    global bw1
    bw1 = bw2+5
    global d1
    global d2
    d1 = (mn*Z1)/(cos(B*pi/180))
    d2 = (mn*Z2)/(cos(B*pi/180))
    global da1
    global da2
    da1 = d1+2*mn*(1+x1)
    da2 = d2+2*mn*(1+x2)
    global df1
    global df2
    df1 = d1 - 2.5*mn*(1.25-x1)
    df2 = d2 - 2.5*mn*(1.25-x2)
    V = pi*d1*n1/60000
    if g_type == 0 and V <= 6:
        nct = 8
    elif g_type == 0 and 6 < V <=12:
        nct = 7
    else:
        nct = 6
    if (g_type == 1 or g_type == 2) and V <= 10:
        nct = 8
    elif (g_type == 1 or g_type == 2) and 10 < V <= 20:
        nct = 7
    else:
        nct = 6
    #Уточненный расчет зубчатой передачи
    #Проверка контактной прочности зубьев
    if g_type == 0:
        zs = 9600
    else:
        zs = 8400
    if g_type == 0:
        A = 0.06
    else:
        A = 0.15
    if HB2 > 350:
        Kw = 1
    else:
        Kw = 0.002*HB2+0.036*(V-9)
    KHa = 1+A*(nct-5)*Kw
    fbd = 0.5*fba*(ur+1)
    if HB2 <= 350:
        K0HBt = [
            [0.6, 1.03],
            [0.8, 1.03],
            [1.0, 1.04],
            [1.2, 1.06],
            [1.4, 1.08],
            [1.6, 1.11],
            ]
    else:
        K0HBt = [
            [0.6, 1.05],
            [0.8, 1.07],
            [1.0, 1.11],
            [1.2, 1.15],
            [1.4, 1.20],
            [1.6, 1.26],
            ]
    j = 0
    for i in range(0, len(K0HBt)-1):
        if fbd <= K0HBt[i][j]:
            fbd1 = K0HBt[i-1][j]
            fbd2 = K0HBt[i][j]
            K0HB1 = K0HBt[i-1][1]
            K0HB2 = K0HBt[i][j]
            break
    a1 = (K0HB2-K0HB1)/(fbd2-fbd1)
    b1 = K0HB1-a1*fbd1
    K0HB = a1*fbd+b1
    KHB = 1+(K0HB-1)*Kw
    if HB2 < 350 and g_type == 0 and nct == 6:
        KHVt = [
            [1, 1.03],
            [3, 1.09],
            [5, 1.16],
            [8, 1.25],
            [10, 1.32],
            [15, 1.48]
            ]
    elif HB2 < 350 and g_type == 0 and nct == 7:
        KHVt = [
            [1, 1.04],
            [3, 1.12],
            [5, 1.20],
            [8, 1.32],
            [10, 1.40],
            [15, 1.60]
            ]
    elif HB2 < 350 and g_type == 0 and nct == 8:
        KHVt = [
            [1, 1.05],
            [3, 1.15],
            [5, 1.24],
            [8, 1.38],
            [10, 1.48],
            [15, 1.72]
            ]
    elif HB2 >= 350 and g_type == 0 and nct == 6:
        KHVt = [
            [1, 1.02],
            [3, 1.06],
            [5, 1.10],
            [8, 1.16],
            [10, 1.20],
            [15, 1.30]
            ]
    elif HB2 >= 350 and g_type == 0 and nct == 7:
        KHVt = [
            [1, 1.02],
            [3, 1.06],
            [5, 1.12],
            [8, 1.19],
            [10, 1.25],
            [15, 1.37]
            ]
    elif HB2 >= 350 and g_type == 0 and nct == 8:
        KHVt = [
            [1, 1.03],
            [3, 1.09],
            [5, 1.15],
            [8, 1.24],
            [10, 1.30],
            [15, 1.45]
            ]
    elif HB2 < 350 and (g_type == 1 or g_type == 2) and nct == 6:
        KHVt = [
            [1, 1.01],
            [3, 1.03],
            [5, 1.06],
            [8, 1.09],
            [10, 1.13],
            [15, 1.19]
            ]
    elif HB2 < 350 and (g_type == 1 or g_type == 2) and nct == 7:
        KHVt = [
            [1, 1.02],
            [3, 1.06],
            [5, 1.08],
            [8, 1.13],
            [10, 1.16],
            [15, 1.24]
            ]
    elif HB2 < 350 and (g_type == 1 or g_type == 2) and nct == 8:
        KHVt = [
            [1, 1.02],
            [3, 1.06],
            [5, 1.10],
            [8, 1.15],
            [10, 1.19],
            [15, 1.29]
            ]
    elif HB2 >= 350 and (g_type == 1 or g_type == 2) and nct == 6:
        KHVt = [
            [1, 1.01],
            [3, 1.03],
            [5, 1.04],
            [8, 1.06],
            [10, 1.08],
            [15, 1.12]
            ]
    elif HB2 >= 350 and (g_type == 1 or g_type == 2) and nct == 7:
        KHVt = [
            [1, 1.01],
            [3, 1.03],
            [5, 1.05],
            [8, 1.08],
            [10, 1.10],
            [15, 1.15]
            ]
    else:
        KHVt = [
            [1, 1.01],
            [3, 1.03],
            [5, 1.06],
            [8, 1.09],
            [10, 1.12],
            [15, 1.18]
            ]
    j = 0
    for i in range(0, len(KHVt)-1):
        if V <= KHVt[i][j]:
            V1 = KHVt[i-1][j]
            V2 = KHVt[i][j]
            KHV1 = KHVt[i-1][1]
            KHV2 = KHVt[i][j]
            break
    a1 = (KHV2-KHV1)/(V2-V1)
    b1 = KHV1-a1*V1
    KHV = a1*V+b1
    KH = KHa*KHB*KHV
    sH = (zs/aw)*((KH*T1*((uf+1)**3)/(bw2*uf))**(1/2))
    dsH = ((sH-sHP)/sHP)*100
    #Проверка изгибной прочности зубьев
    if g_type == 0:
        Zv1 = Z1
        Zv2 = Z2
    else:
        Zv1 = Z1/((cos(B*pi/180))**3)
        Zv2 = Z2/((cos(B*pi/180))**3)
    Yf1 = 3.47+(13.2-27.9*x1)/Zv1+0.092*(x1**2)
    Yf2 = 3.47+(13.2-27.9*x2)/Zv2+0.092*(x2**2)
    YB = 1-B/100
    if YB >= 0.7:
        YB = YB
    else:
        YB = 0.7
    Ea = (1.88-3.2*(1/Z1+1/Z2))*cos(B*pi/180)
    YE = 1/Ea
    if g_type == 0:
        KFa = 1
    else:
        KFa = 1+A*(nct-5)
    KFB = 0.18+0.82*K0HB
    if HB2 <350:
        KFV = 1+1.5*(KHV-1)
    else:
        KFV = KHV
    KF = KFa*KFB*KFV
    if g_type == 0:
        sF1 = Yf1*2000*T1*KF/(bw1*d1*mn)
    else:
        sF1 = Yf1*YB*YE*2000*T1*KF/(bw1*d1*mn)
    sF2 = sF1*bw1*Yf2/(bw2*Yf1)
    if g_type == 0:
        Ft = 2000*T1/d1
        Fr = Ft*tan(a*pi/180)
        Fa = 0
    elif g_type == 1:
        Ft = 2000*T1/d1
        Fr = Ft*tan(a*pi/180)/cos(B*pi/180)
        Fa = Ft*tan(B*pi/180)
    else:
        Ft = 0.5*2000*T1/d1
        Fr = 0.5*Ft*tan(a*pi/180)/cos(B*pi/180)
        Fa = 0.5*Ft*tan(B*pi/180)
    Dm_string = str(round(Dm, 3))
    Sm_string = str(round(Sm, 3))
    dk_string = str(round(dk, 3))
    brand1_string = str(brand1)
    Dm1_string = str(Dm1)
    Sm1_string = str(Sm1)
    heat1_string = str(heat1)
    HBmin1_string = str(HBmin1)
    HBmax1_string = str(HBmax1)
    sb1_string = str(sb1)
    NH01_string = str(NH01)
    brand2_string = str(brand2)
    Dm2_string = str(Dm2)
    Sm2_string = str(Sm2)
    heat2_string = str(heat2)
    HBmin2_string = str(HBmin2)
    HBmax2_string = str(HBmax2)
    sb2_string = str(sb2)
    NH02_string = str(NH02)
    HB1_string = str(round(HB1, 3))
    HB2_string = str(round(HB2, 3))
    sHlim1_string = str(round(sHlim1, 3))
    sHlim2_string = str(round(sHlim2, 3))
    Lh_string = str(round(Lh, 3))
    Ns1_string = str(round(Ns1, 3))
    Ns2_string = str(round(Ns2, 3))
    NHE1_string = str(round(NHE1, 3))
    NHE2_string = str(round(NHE2, 3))
    sHP1_string = str(round(sHP1, 3))
    sHP2_string = str(round(sHP2, 3))
    sHPmin_string = str(round(sHPmin, 3))
    sHP_string = str(round(sHP, 3))
    s1HP_string = str(round(s1HP, 3))
    sFlim1_string = str(round(sFlim1, 3))
    sFlim2_string = str(round(sFlim2, 3))
    NFE1_string = str(round(NFE1, 3))
    NFE2_string = str(round(NFE2, 3))
    q1_string = str(q1)
    q2_string = str(q2)
    KFL1_string = str(round(KFL1, 3))
    KFL2_string = str(round(KFL2, 3))
    sFP1_string = str(round(sFP1, 3))
    sFP2_string = str(round(sFP2, 3))
    aw_string = str(aw)
    mn_string = str(mn)
    Zs1_string = str(round(Zs1, 3))
    Zs_string = str(Zs)
    B_string = str(round(B, 3))
    Z1_string = str(Z1)
    Z2_string = str(Z2)
    uf_string = str(round(uf, 3))
    du_string = str(round(du, 3))
    bw2_string = str(bw2)
    bw1_string = str(bw1)
    d1_string = str(round(d1, 3))
    d2_string = str(round(d2, 3))
    da1_string = str(round(da1, 3))
    da2_string = str(round(da2, 3))
    df1_string = str(round(df1, 3))
    df2_string = str(round(df2, 3))
    V_string = str(round(V, 3))
    nct_string = str(nct)
    Kw_string = str(round(Kw, 3))
    KHa_string = str(round(KHa, 3))
    fbd_string = str(round(fbd, 3))
    K0HB_string = str(round(K0HB, 3))
    KHB_string = str(round(KHB, 3))
    KHV_string = str(round(KHV, 3))
    KH_string = str(round(KH, 3))
    sH_string = str(round(sH, 3))
    dsH_string = str(round(dsH, 3))
    Zv1_string = str(round(Zv1, 3))
    Zv2_string = str(round(Zv2, 3))
    Yf1_string = str(round(Yf1, 3))
    Yf2_string = str(round(Yf2, 3))
    YB_string = str(round(YB, 3))
    Ea_string = str(round(Ea, 3))
    YE_string = str(round(YE, 3))
    KFa_string = str(round(KFa, 3))
    KFB_string = str(round(KFB, 3))
    KFV_string = str(round(KFV, 3))
    KF_string = str(round(KF, 3))
    sF1_string = str(round(sF1, 3))
    sF2_string = str(round(sF2, 3))
    Ft_string = str(round(Ft, 3))
    Fr_string = str(round(Fr, 3))
    Fa_string = str(round(Fa, 3))
    CalculationGear_file = open('C:/Users/Public/Documents/CalculationGear.txt', 'w')
    CalculationGear_file.write('Dm = '+Dm_string+' мм'+"\n")
    CalculationGear_file.write('Sm = '+Sm_string+' мм'+"\n")
    CalculationGear_file.write('dk = '+dk_string+' мм'+"\n")
    CalculationGear_file.write('Марка стали - '+brand1_string+"\n")
    CalculationGear_file.write('Dm1 = '+Dm1_string+' мм'+"\n")
    CalculationGear_file.write('Sm1 = '+Sm1_string+' мм'+"\n")
    CalculationGear_file.write('Термообработка - '+heat1_string+"\n")
    CalculationGear_file.write('HBmin1 = '+HBmin1_string+' HB'+"\n")
    CalculationGear_file.write('HBmax1 = '+HBmax1_string+' HB'+"\n")
    CalculationGear_file.write('sb1 = '+sb1_string+' МПа'+"\n")
    CalculationGear_file.write('NH01 = '+NH01_string+' циклов'+"\n")
    CalculationGear_file.write('Марка стали - '+brand2_string+"\n")
    CalculationGear_file.write('Dm2 = '+Dm2_string+' мм'+"\n")
    CalculationGear_file.write('Sm2 = '+Sm2_string+' мм'+"\n")
    CalculationGear_file.write('Термообработка - '+heat2_string+"\n")
    CalculationGear_file.write('HBmin2 = '+HBmin2_string+' HB'+"\n")
    CalculationGear_file.write('HBmax2 = '+HBmax2_string+' HB'+"\n")
    CalculationGear_file.write('sb2 = '+sb2_string+' МПа'+"\n")
    CalculationGear_file.write('NH02 = '+NH02_string+' циклов'+"\n")
    CalculationGear_file.write('HB1 = '+HB1_string+' HB'+"\n")
    CalculationGear_file.write('HB2 = '+HB2_string+' HB'+"\n")
    CalculationGear_file.write('sHlim1 = '+sHlim1_string+' МПа'+"\n")
    CalculationGear_file.write('sHlim2 = '+sHlim2_string+' МПа'+"\n")
    CalculationGear_file.write('Lh = '+Lh_string+' часов'+"\n")
    CalculationGear_file.write('Ns1 = '+Ns1_string+' циклов'+"\n")
    CalculationGear_file.write('Ns2 = '+Ns2_string+' циклов'+"\n")
    CalculationGear_file.write('NHE1 = '+NHE1_string+' циклов'+"\n")
    CalculationGear_file.write('NHE2 = '+NHE2_string+' циклов'+"\n")
    CalculationGear_file.write('sHP1 = '+sHP1_string+' МПа'+"\n")
    CalculationGear_file.write('sHP2 = '+sHP2_string+' МПа'+"\n")
    CalculationGear_file.write('sHPmin = '+sHPmin_string+' МПа'+"\n")
    CalculationGear_file.write('sHP = '+sHP_string+' МПа'+"\n")
    CalculationGear_file.write('s1HP = '+s1HP_string+' МПа'+"\n")
    CalculationGear_file.write('sFlim1 = '+sFlim1_string+' МПа'+"\n")
    CalculationGear_file.write('sFlim2 = '+sFlim2_string+' МПа'+"\n")
    CalculationGear_file.write('NFE1 = '+NFE1_string+' циклов'+"\n")
    CalculationGear_file.write('NFE2 = '+NFE2_string+' циклов'+"\n")
    CalculationGear_file.write('q1 = '+q1_string+"\n")
    CalculationGear_file.write('q2 = '+q2_string+"\n")
    CalculationGear_file.write('KFL1 = '+KFL1_string+"\n")
    CalculationGear_file.write('KFL2 = '+KFL2_string+"\n")
    CalculationGear_file.write('sFP1 = '+sFP1_string+' МПа'+"\n")
    CalculationGear_file.write('sFP2 = '+sFP2_string+' МПа'+"\n")
    CalculationGear_file.write('aw = '+aw_string+' мм'+"\n")
    CalculationGear_file.write('mn = '+mn_string+' мм'+"\n")
    CalculationGear_file.write('Zs1 = '+Zs1_string+"\n")
    CalculationGear_file.write('Zs = '+Zs_string+"\n")
    CalculationGear_file.write('B = '+B_string+' градусов'+"\n")
    CalculationGear_file.write('Z1 = '+Z1_string+"\n")
    CalculationGear_file.write('Z2 = '+Z2_string+"\n")
    CalculationGear_file.write('uf = '+uf_string+"\n")
    CalculationGear_file.write('du = '+du_string+' %'+"\n")
    CalculationGear_file.write('bw2 = '+bw2_string+' мм'+"\n")
    CalculationGear_file.write('bw1 = '+bw1_string+' мм'+"\n")
    CalculationGear_file.write('d1 = '+d1_string+' мм'+"\n")
    CalculationGear_file.write('d2 = '+d2_string+' мм'+"\n")
    CalculationGear_file.write('da1 = '+da1_string+' мм'+"\n")
    CalculationGear_file.write('da2 = '+da2_string+' мм'+"\n")
    CalculationGear_file.write('df1 = '+df1_string+' мм'+"\n")
    CalculationGear_file.write('df2 = '+df2_string+' мм'+"\n")
    CalculationGear_file.write('V = '+V_string+' м/с'+"\n")
    CalculationGear_file.write('nct = '+nct_string+"\n")
    CalculationGear_file.write('Kw = '+Kw_string+"\n")
    CalculationGear_file.write('KHa = '+KHa_string+"\n")
    CalculationGear_file.write('fbd = '+fbd_string+"\n")
    CalculationGear_file.write('K0HB = '+K0HB_string+"\n")
    CalculationGear_file.write('KHB = '+KHB_string+"\n")
    CalculationGear_file.write('KHV = '+KHV_string+"\n")
    CalculationGear_file.write('KH = '+KH_string+"\n")
    CalculationGear_file.write('sH = '+sH_string+' МПа'+"\n")
    CalculationGear_file.write('dsH = '+dsH_string+' %'+"\n")
    CalculationGear_file.write('Zv1 = '+Zv1_string+"\n")
    CalculationGear_file.write('Zv2 = '+Zv2_string+"\n")
    CalculationGear_file.write('Yf1 = '+Yf1_string+"\n")
    CalculationGear_file.write('Yf2 = '+Yf2_string+"\n")
    CalculationGear_file.write('YB = '+YB_string+"\n")
    CalculationGear_file.write('Ea = '+Ea_string+"\n")
    CalculationGear_file.write('YE = '+YE_string+"\n")
    CalculationGear_file.write('KFa = '+KFa_string+"\n")
    CalculationGear_file.write('KFB = '+KFB_string+"\n")
    CalculationGear_file.write('KFV = '+KFV_string+"\n")
    CalculationGear_file.write('KF = '+KF_string+"\n")
    CalculationGear_file.write('sF1 = '+sF1_string+' МПа'+"\n")
    CalculationGear_file.write('sF2 = '+sF2_string+' МПа'+"\n")
    CalculationGear_file.write('Ft = '+Ft_string+' Н'+"\n")
    CalculationGear_file.write('Fr = '+Fr_string+' Н'+"\n")
    CalculationGear_file.write('Fa = '+Fa_string+' Н'+"\n")
    CalculationGear_file.close()

#Расчет дополнительной передачи
def AdditionalDrive():
    #Исходные данные
    c_d = float(c_d_entry.get())
    d_type = int(d_type_entry.get())
    t_mode = int(t_mode_entry.get())
    t_type = int(t_type_entry.get())
    scheme = int(scheme_entry.get())
    if scheme == 0:
        T = T0
        n = n0
    else:
        n = n2
        T = T2
    u = u_add
    E_b = 0.015
    nc_b = 2
    BELT = [
        ['Z', 8.5, 6, 47, 400, 3150, 0.06, 63, 25],
        ['A', 11, 8, 81, 560, 4500, 0.105, 90, 70],
        ['B', 14, 11, 138, 630, 6300, 0.18, 125, 190],
        ['C', 19, 14, 230, 1800, 10000, 0.3, 200, 550],
        ['D', 27, 20, 476, 2240, 15000, 0.62, 315, 2000],
        ['E', 32, 25, 692, 4000, 18000, 0.9, 500, 4500],
        ['EO', 42, 30, 1170, 6300, 18000, 1.52, 800, 4500]
        ]
    CHAIN1 = [
        ['ПР-8-4.6', 8, 3, 5, 7.5, 11, 4.6, 0.2],
        ['ПР-9.525-9.1', 9.525, 5.72, 6.35, 8.5, 28, 9.1, 0.45],
        ['ПР-12.7-10-1', 12.7, 2.4, 7.75, 10, 13, 10, 0.3],
        ['ПР-12.7-9', 12.7, 3.3, 7.75, 10, 22, 9, 0.35],
        ['ПР-12.7-18.2-1', 12.7, 5.4, 8.51, 11.8, 39, 18.2, 0.65],
        ['ПР-12.7-18.2', 12.7, 7.75, 8.51, 11.8, 50, 18.2, 0.75],
        ['ПР-15.875-23-1', 15.875, 6.48, 10.16, 14.8, 51, 23, 0.8],
        ['ПР-15.875-23', 15.875, 9.63, 10.16, 14.8, 67, 23, 1.0],
        ['ПР-19.05-31.8', 19.05, 12.7, 11.91, 18.2, 105, 31.8, 1.9],
        ['ПР-25.4-60', 25.4, 15.88, 15.88, 24.2, 179, 60, 2.6],
        ['ПР-31.75-89', 31.75, 19.05, 19.05, 30.2, 262, 89, 3.8],
        ['ПР-38.1-127', 38.1, 25.4, 22.23, 36.2, 394, 127, 5.5],
        ['ПР-44.45-172.4', 44.45, 25.4, 25.4, 42.4, 472, 172.4, 7.5],
        ['ПР-50.8-227', 50.8, 31.75, 28.58, 48.3, 645, 227, 9.7],
        ['ПР-63.5-354', 63.5, 38.1, 39.68, 60.4, 1089, 354, 16.0]
        ]
    CHAIN2 = [
        ['2ПР-12.7-31.8', 12.7, 7.75, 8.51, 11.8, 105, 31.8, 1.4],
        ['2ПР-15.875-45.4', 15.875, 9.65, 10.16, 14.8, 140, 45.4, 1.9],
        ['2ПР-19.05-64', 19.05, 12.7, 11.91, 18.08, 211, 64, 2.9],
        ['2ПР-25.4-114', 25.4, 15.88, 15.88, 24.2, 359, 114, 5.0],
        ['2ПР-31.75-177', 31.75, 19.05, 19.05, 30.2, 524, 177, 7.3],
        ['2ПР-38.1-254', 38.1, 25.4, 22.23, 36.2, 788, 254, 11],
        ['2ПР-44.45-344', 44.45, 25.4, 25.4, 42.24, 946, 344, 14.4],
        ['2ПР-50.8-453.6', 50.8, 31.75, 28.58, 48.3, 1292, 453.6, 19.1]
        ]
    #Расчет ременной передачи
    if d_type == 0:
        j = 8
        for i in range(0, len(BELT)-1):
            if (T <= BELT[i][j]):
                designation_b = BELT[i][0]
                bp_b = BELT[i][1]
                h_b = BELT[i][2]
                A_b = BELT[i][3]
                Lmin_b = BELT[i][4]
                Lmax_b = BELT[i][5]
                qm_b = BELT[i][6]
                break
            else:
                designation_b = BELT[6][0]
                bp_b = BELT[6][1]
                h_b = BELT[6][2]
                A_b = BELT[6][3]
                qm_b = BELT[6][6]
        K = 40
        d1_b = K*((T)**(1/3))
        for i in range(0, len(standart)-1):
            if (d1_b <= standart[i]):
                d1_b = standart[i]
                break
        d2_b = u*d1_b*(1-E_b)
        for i in range(0, len(standart)-1):
            if (d2_b <= standart[i]):
                d2_b = standart[i]
                break
        uf_b = d2_b/d1_b
        du_b = ((u-uf_b)/u)*100
        aw1_b = 0.8*(d1_b+d2_b)
        L_b = 2*aw1_b+0.5*pi*(d1_b+d2_b)+(((d2_b-d1_b)**2)/(4*aw1_b))
        for i in range(0, len(standart)-1):
            if (L_b <= standart[i]):
                L_b = standart[i]
                break
        W_b = 0.5*pi*(d1_b+d2_b)
        Y_b = 2*((d2_b-d1_b)**2)
        aw_b = 0.25*(L_b-W_b+((((L_b-W_b)**2)-Y_b)**(1/2)))
        a1_b = 180-57.3*((d2_b-d1_b)/aw_b)
        V_b = pi*d1_b*n/60000
        Ft_b = 2000*T/d1_b
        lam_b = 1000*V_b/L_b
        Ca_b = 1-0.44*log(180/a1_b)
        if t_mode == 0 and (t_type == 0 or t_type == 1):
            CH_b = 1
        elif t_mode == 1 and t_type == 0:
            CH_b = 0.7
        else:
            CH_b = 0.85
        Cp_b = CH_b - 0.1*(nc_b-1)
        Cu_b = 1.14-0.14/(u**3.8)
        st0_b = 5.55/(lam_b**0.09)-((6*(bp_b**1.57))/(Cu_b*d1_b))-0.001*(V_b**2)
        st_b = st0_b*Ca_b*Cp_b
        Z_b = 3
        Cz_b = 0.95
        Z1_b = Ft_b/(st_b*A_b*Cz_b)
        Z1_b = round(Z1_b, 0)
        if Z1_b <= Z_b:
            Z1_b = Z1_b
        elif Z1_b > Z_b and Z1_b <= 6:
            Z_b = Z1_b
            Cz_b = 0.9
            Z1_b = Ft_b/(st_b*A_b*Cz_b)
            Z1_b = round(Z1_b, 0)
        if Z1_b <= Z_b:
            Z1_b = Z1_b
        else:
            Z_b = Z1_b
            Cz_b = 0.85
            Z1_b = Ft_b/(st_b*A_b*Cz_b)
            Z1_b = round(Z1_b, 0)
        S0_b = 0.75*(Ft_b/(Z1_b*Ca_b*Cp_b))+qm_b*(V_b**2)
        Fb_b = 2*S0_b*Z1_b*sin(0.5*a1_b*pi/180)
        designation_b_string = str(designation_b)
        bp_b_string = str(bp_b)
        h_b_string = str(h_b)
        A_b_string = str(A_b)
        Lmin_b_string = str(Lmin_b)
        Lmax_b_string = str(Lmax_b)
        qm_b_string = str(qm_b)
        d1_b_string = str(d1_b)
        d2_b_string = str(d2_b)
        uf_b_string = str(round(uf_b, 3))
        du_b_string = str(round(du_b, 3))
        aw1_b_string = str(round(aw1_b, 3))
        L_b_string = str(round(L_b, 3))
        W_b_string = str(round(W_b, 3))
        Y_b_string = str(round(Y_b, 3))
        aw_b_string = str(round(aw_b, 3))
        a1_b_string = str(round(a1_b, 3))
        V_b_string = str(round(V_b, 3))
        Ft_b_string = str(round(Ft_b, 3))
        lam_b_string = str(round(lam_b, 3))
        Ca_b_string = str(round(Ca_b, 3))
        CH_b_string = str(round(CH_b, 3))
        Cp_b_string = str(round(Cp_b, 3))
        Cu_b_string = str(round(Cu_b, 3))
        st0_b_string = str(round(st0_b, 3))
        st_b_string = str(round(st_b, 3))
        Z_b_string = str(round(Z_b, 3))
        Cz_b_string = str(round(Cz_b, 3))
        Z1_b_string = str(round(Z1_b, 3))
        S0_b_string = str(round(S0_b, 3))
        Fb_b_string = str(round(Fb_b, 3))
        AdditionalDrive_file = open('C:/Users/Public/Documents/AdditionalDrive.txt', 'w')
        AdditionalDrive_file.write('Ременная передача'+"\n")
        AdditionalDrive_file.write('designation - '+designation_b_string+"\n")
        AdditionalDrive_file.write('bp = '+bp_b_string+' мм'+"\n")
        AdditionalDrive_file.write('h = '+h_b_string+' мм'+"\n")
        AdditionalDrive_file.write('A = '+A_b_string+' мм2'+"\n")
        AdditionalDrive_file.write('Lmin = '+Lmin_b_string+' мм'+"\n")
        AdditionalDrive_file.write('Lmax = '+Lmax_b_string+' мм'+"\n")
        AdditionalDrive_file.write('qm = '+qm_b_string+' кг/м'+"\n")
        AdditionalDrive_file.write('d1 = '+d1_b_string+' мм'+"\n")
        AdditionalDrive_file.write('d2 = '+d2_b_string+' мм'+"\n")
        AdditionalDrive_file.write('uf = '+uf_b_string+"\n")
        AdditionalDrive_file.write('du = '+du_b_string+"\n")
        AdditionalDrive_file.write('aw1 = '+aw1_b_string+' мм'+"\n")
        AdditionalDrive_file.write('L = '+L_b_string+' мм'+"\n")
        AdditionalDrive_file.write('W = '+W_b_string+' мм'+"\n")
        AdditionalDrive_file.write('Y = '+Y_b_string+' мм2'+"\n")
        AdditionalDrive_file.write('aw = '+aw_b_string+' мм'+"\n")
        AdditionalDrive_file.write('a1 = '+a1_b_string+' градусов'+"\n")
        AdditionalDrive_file.write('V = '+V_b_string+' м/с'+"\n")
        AdditionalDrive_file.write('Ft = '+Ft_b_string+' Н'+"\n")
        AdditionalDrive_file.write('lam = '+lam_b_string+' об/с'+"\n")
        AdditionalDrive_file.write('Ca = '+Ca_b_string+"\n")
        AdditionalDrive_file.write('CH = '+CH_b_string+"\n")
        AdditionalDrive_file.write('Cp = '+Cp_b_string+"\n")
        AdditionalDrive_file.write('Cu = '+Cu_b_string+"\n")
        AdditionalDrive_file.write('st0 = '+st0_b_string+' МПа'+"\n")
        AdditionalDrive_file.write('st = '+st_b_string+' МПа'+"\n")
        AdditionalDrive_file.write('Z = '+Z_b_string+"\n")
        AdditionalDrive_file.write('Cz = '+Cz_b_string+"\n")
        AdditionalDrive_file.write('Z1 = '+Z1_b_string+"\n")
        AdditionalDrive_file.write('S0 = '+S0_b_string+' Н'+"\n")
        AdditionalDrive_file.write('Fb = '+Fb_b_string+' Н'+"\n")
        AdditionalDrive_file.close()
    #Расчет передачи роликовой цепью
    else:
        Z1_c = 29-2*u
        Z1_c = round(Z1_c, 0)
        Z2_c = Z1_c*u
        Z2_c = round(Z2_c, 0)
        uf_c = Z2_c/Z1_c
        du_c = ((u-uf_c)/u)*100
        if t_mode == 0 and (t_type == 0 or t_type == 1):
            Kd_c = 1
        elif t_mode == 1 and t_type == 0:
            Kd_c = 1.8
        else:
            Kd_c = 1.35 #1.2...1.5
        KH_c = 1
        Kp_c = 1.25
        Kcm_c = 1.5
        Kpe_c = (3*c_d)**(1/3)
        Ke_c = Kd_c*KH_c*Kp_c*Kcm_c*Kpe_c
        mp_с = 1
        p1_c = 20
        tp_c = 28*((Ke_c*T/(Z1_c*p1_c*mp_с))**(1/3))
        j = 1
        for i in range(0, len(CHAIN1)-1):
            if (tp_c <= CHAIN1[i][j]):
                designation_c = CHAIN1[i][0]
                tp_c = BELT[i][j]
                B_c = BELT[i][2]
                d_c = BELT[i][3]
                h_c = BELT[i][4]
                A_c = BELT[i][5]
                Q_c = BELT[i][6]
                q_c = BELT[i][7]
                break
        if tp_c < 19.05:
            p_ct = [
                [50, 200, 400, 600, 800, 1000, 1200, 1600, 2000],
                [35, 31.5, 28.5, 26, 24, 22.5, 21, 18.5, 16.5]
                ]
            i = 0
            for j in range(0, len(p_ct[0])-1):
                if n <= p_ct[i][j]:
                    n1 = p_ct[i][j-1]
                    n2 = p_ct[i][j]
                    p_c1 = p_ct[1][j-1]
                    p_c2 = p_ct[1][j]
                    break
            a1 = (p_c2-p_c1)/(n2-n1)
            b1 = p_c1-a1*n1
            p_c = a1*n+b1
        elif 19.05 <= tp_c < 25.4:
            p_ct = [
                [50, 200, 400, 600, 800, 1000, 1200, 1600, 2000],
                [35, 30, 26, 23.5, 21, 19, 17.5, 15, 0]
                ]
            i = 0
            for j in range(0, len(p_ct[0])-1):
                if n <= p_ct[i][j]:
                    n1 = p_ct[i][j-1]
                    n2 = p_ct[i][j]
                    p_c1 = p_ct[1][j-1]
                    p_c2 = p_ct[1][j]
                    break
            a1 = (p_c2-p_c1)/(n2-n1)
            b1 = p_c1-a1*n1
            p_c = a1*n+b1
        elif 25.4 <= tp_c < 38.1:
            p_ct = [
                [50, 200, 400, 600, 800, 1000, 1200, 1600, 2000],
                [35, 29, 26, 21, 18.5, 16.5, 15, 0, 0]
                ]
            i = 0
            for j in range(0, len(p_ct[0])-1):
                if n <= p_ct[i][j]:
                    n1 = p_ct[i][j-1]
                    n2 = p_ct[i][j]
                    p_c1 = p_ct[1][j-1]
                    p_c2 = p_ct[1][j]
                    break
            a1 = (p_c2-p_c1)/(n2-n1)
            b1 = p_c1-a1*n1
            p_c = a1*n+b1
        else:
            p_ct = [
                [50, 200, 400, 600, 800, 1000, 1200, 1600, 2000],
                [35, 26, 24, 17.5, 15, 0, 0, 0, 0]
                ]
            i = 0
            for j in range(0, len(p_ct[0])-1):
                if n <= p_ct[i][j]:
                    n1 = p_ct[i][j-1]
                    n2 = p_ct[i][j]
                    p_c1 = p_ct[1][j-1]
                    p_c2 = p_ct[1][j]
                    break
            a1 = (p_c2-p_c1)/(n2-n1)
            b1 = p_c1-a1*n1
            p_c = a1*n+b1
        At_c = 40
        Lt_c = 2*At_c+0.5*(Z1_c+Z2_c)+(1/At_c)*(((Z2_c-Z1_c)/(2*pi))**2)
        Lt_c = round(Lt_c, 0)
        L_c = tp_c*Lt_c
        Y_c = Lt_c-0.5*(Z1_c+Z2_c)
        aw_c = 0.25*tp_c*(Y_c+(Y_c**2-2*(((Z2_c-Z1_c)/pi)**2))**(1/2))
        d1_c = tp_c/sin(180*pi/(Z1_c*180))
        d2_c = tp_c/sin(180*pi/(Z2_c*180))
        V_c = Z1_c*n*tp_c/60000
        Ft_c = 2000*T/d1_c
        Kf_c = 6.25
        Ff_c = 0.01*Kf_c*q_c*aw_c
        Fv_c = q_c *(V_c**2)
        p_1c = (Kd_c*Ft_c+Ff_c+Fv_c)/A_c
        Fb_c = Ft_c+2*Ff_c
        Z1_c_string = str(Z1_c)
        Z2_c_string = str(Z2_c)
        uf_c_string = str(round(uf_c, 3))
        du_c_string = str(round(du_c, 3))
        Kd_c_string = str(round(Kd_c, 3))
        KH_c_string = str(round(KH_c, 3))
        Kp_c_string = str(round(Kp_c, 3))
        Kcm_c_string = str(round(Kcm_c, 3))
        Kpe_c_string = str(round(Kpe_c, 3))
        Ke_c_string = str(round(Ke_c, 3))
        mp_c_string = str(round(mp_c, 3))
        p1_c_string = str(round(p1_c, 3))
        designation_c_string = str(designation_c)
        tp_c_string = str(tp_c)
        B_c_string = str(B_c)
        d_c_string = str(d_c)
        h_c_string = str(h_c)
        A_c_string = str(A_c)
        Q_c_string = str(Q_c)
        q_c_string = str(q_c)
        p_c_string = str(round(p_c, 3))
        At_c_string = str(round(At_c, 3))
        Lt_c_string = str(round(Lt_c, 3))
        L_c_string = str(round(L_c, 3))
        Y_c_string = str(round(Y_c, 3))
        aw_c_string = str(round(aw_c, 3))
        d1_c_string = str(round(d1_c, 3))
        d2_c_string = str(round(d2_c, 3))
        V_c_string = str(round(V_c, 3))
        Ft_c_string = str(round(Ft_c, 3))
        Kf_c_string = str(round(Kf_c, 3))
        Ff_c_string = str(round(Ff_c, 3))
        Fv_c_string = str(round(Fv_c, 3))
        p_1c_string = str(round(p_1c, 3))
        Fb_c_string = str(round(Fb_c, 3))
        AdditionalDrive_file = open('C:/Users/Public/Documents/AdditionalDrive.txt', 'w')
        AdditionalDrive_file.write('Цепная передача'+"\n")
        AdditionalDrive_file.write('Z1 = '+Z1_c_string+"\n")
        AdditionalDrive_file.write('Z2 = '+Z2_c_string+"\n")
        AdditionalDrive_file.write('uf = '+uf_c_string+"\n")
        AdditionalDrive_file.write('du = '+du_c_string+"\n")
        AdditionalDrive_file.write('Kd = '+Kd_c_string+"\n")
        AdditionalDrive_file.write('KH = '+KH_c_string+"\n")
        AdditionalDrive_file.write('Kp = '+Kp_c_string+"\n")
        AdditionalDrive_file.write('Kcm = '+Kcm_c_string+"\n")
        AdditionalDrive_file.write('Kpe = '+Kpe_c_string+"\n")
        AdditionalDrive_file.write('Ke = '+Ke_c_string+"\n")
        AdditionalDrive_file.write('mp = '+mp_c_string+"\n")
        AdditionalDrive_file.write('p1 = '+p1_c_string+' МПа'+"\n")
        AdditionalDrive_file.write('designation - '+designation_c_string+"\n")
        AdditionalDrive_file.write('tp = '+tp_c_string+' мм'+"\n")
        AdditionalDrive_file.write('B = '+B_c_string+' мм'+"\n")
        AdditionalDrive_file.write('d = '+d_c_string+' мм'+"\n")
        AdditionalDrive_file.write('h = '+h_c_string+' мм'+"\n")
        AdditionalDrive_file.write('A = '+A_c_string+' мм2'+"\n")
        AdditionalDrive_file.write('Q = '+Q_c_string+' кН'+"\n")
        AdditionalDrive_file.write('q = '+q_c_string+' кг/м'+"\n")
        AdditionalDrive_file.write('[p] = '+p_c_string+' МПа'+"\n")
        AdditionalDrive_file.write('At = '+At_c_string+"\n")
        AdditionalDrive_file.write('Lt = '+Lt_c_string+"\n")
        AdditionalDrive_file.write('L = '+L_c_string+' мм'+"\n")
        AdditionalDrive_file.write('Y = '+Y_c_string+' мм'+"\n")
        AdditionalDrive_file.write('aw = '+aw_c_string+' мм'+"\n")
        AdditionalDrive_file.write('d1 = '+d1_c_string+' мм'+"\n")
        AdditionalDrive_file.write('d2 = '+d2_c_string+' мм'+"\n")
        AdditionalDrive_file.write('V = '+V_c_string+' м/с'+"\n")
        AdditionalDrive_file.write('Ft = '+Ft_c_string+' Н'+"\n")
        AdditionalDrive_file.write('Kf = '+Kf_c_string+"\n")
        AdditionalDrive_file.write('Ff = '+Ff_c_string+' Н'+"\n")
        AdditionalDrive_file.write('Fv = '+Fv_c_string+' Н'+"\n")
        AdditionalDrive_file.write('p = '+p_1c_string+' МПа'+"\n")
        AdditionalDrive_file.write('Fb = '+Fb_c_string+' Н'+"\n")
        AdditionalDrive_file.close()

#Выбор материала тихоходного вала
def ChoiceShaftMaterial():
    def ChoiceShaft():
        global brand2_s
        global Dm2_s
        global heat2_s
        global HBmin2_s
        global HBmax2_s
        global sb2_s
        global st2_s
        if var.get() == 0:
            brand2_s = 'Сталь 45'
            Dm2_s = 'Любой'
            heat2_s = 'Н'
            HBmin2_s = 179
            HBmax2_s = 207
            sb2_s = 600
            st2_s = 320
        elif var.get() == 1:
            brand2_s = 'Сталь 45'
            Dm2_s = 125
            heat2_s = 'У'
            HBmin2_s = 235
            HBmax2_s = 262
            sb2_s = 780
            st2_s = 540
        elif var.get() == 2:
            brand2_s = 'Сталь 45'
            Dm2_s = 80
            heat2_s = 'У'
            HBmin2_s = 269
            HBmax2_s = 302
            sb2_s = 890
            st2_s = 650
        elif var.get() == 3:
            brand2_s = 'Сталь 40Х'
            Dm2_s = 200
            heat2_s = 'У'
            HBmin2_s = 235
            HBmax2_s = 262
            sb2_s = 790
            st2_s = 640
        elif var.get() == 4:
            brand2_s = 'Сталь 40Х'
            Dm2_s = 125
            heat2_s = 'У'
            HBmin2_s = 269
            HBmax2_s = 302
            sb2_s = 900
            st2_s = 750
        elif var.get() == 5:
            brand2_s = 'Сталь 40Х'
            Dm2_s = 125
            heat2_s = 'У+З(ТВЧ)'
            HBmin2_s = 409
            HBmax2_s = 470
            sb2_s = 900
            st2_s = 750
        elif var.get() == 6:
            brand2_s = 'Сталь 40ХН'
            Dm2_s = 315
            heat2_s = 'У'
            HBmin2_s = 235
            HBmax2_s = 262
            sb2_s = 800
            st2_s = 630
        elif var.get() == 7:
            brand2_s = 'Сталь 40ХН'
            Dm2_s = 200
            heat2_s = 'У'
            HBmin2_s = 269
            HBmax2_s = 302
            sb2_s = 920
            st2_s = 750
        elif var.get() == 8:
            brand2_s = 'Сталь 40ХН'
            Dm2_s = 200
            heat2_s = 'У+З(ТВЧ)'
            HBmin2_s = 444
            HBmax2_s = 511
            sb2_s = 920
            st2_s = 750
        elif var.get() == 9:
            brand2_s = 'Сталь 35ХМ'
            Dm2_s = 315
            heat2_s = 'У'
            HBmin2_s = 235
            HBmax2_s = 262
            sb2_s = 800
            st2_s = 670
        elif var.get() == 10:
            brand2_s = 'Сталь 35ХМ'
            Dm2_s = 200
            heat2_s = 'У'
            HBmin2_s = 269
            HBmax2_s = 302
            sb2_s = 920
            st2_s = 790
        elif var.get() == 11:
            brand2_s = 'Сталь 35ХМ'
            Dm2_s = 200
            heat2_s = 'У+З(ТВЧ)'
            HBmin2_s = 444
            HBmax2_s = 511
            sb2_s = 920
            st2_s = 790
        elif var.get() == 12:
            brand2_s = 'Сталь 20Х'
            Dm2_s = 200
            heat2_s = 'У+Ц+З'
            HBmin2_s = 538
            HBmax2_s = 632
            sb2_s = 1000
            st2_s = 800
        elif var.get() == 13:
            brand2_s = 'Сталь 20ХНМ'
            Dm2_s = 200
            heat2_s = 'У+Ц+З'
            HBmin2_s = 538
            HBmax2_s = 632
            sb2_s = 1000
            st2_s = 800
        else:
            brand2_s = 'Сталь 18ХГТ'
            Dm2_s = 200
            heat2_s = 'У+Ц+З'
            HBmin2_s = 538
            HBmax2_s = 632
            sb2_s = 1000
            st2_s = 800
    choiceshaft = Toplevel()
    choiceshaft.title('Материал вала')
    choiceshaft.geometry()

    var = IntVar()
    var.set(0)

    frame0 = Frame(choiceshaft)
    frame0.grid(row=0, column=0)
    material_label1 = Label(frame0, text='Метериал вала').grid(row=0, column=0)
    mmaterial1 = Radiobutton(frame0, text='Сталь 45, Dm - любой, Термообработка - Н, HBmin-HBmax = 179-207 HB, Предел прочности - 600 МПа, Предел текучести - 320 МПа', variable=var, value=0).grid(row=1, column=0)
    mmaterial2 = Radiobutton(frame0, text='Сталь 45, Dm - 125 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности - 780 МПа, Предел текучести - 540 МПа', variable=var, value=1).grid(row=2, column=0)
    mmaterial3 = Radiobutton(frame0, text='Сталь 45, Dm - 80 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности - 890 МПа, Предел текучести - 650 МПа', variable=var, value=2).grid(row=3, column=0)   
    mmaterial4 = Radiobutton(frame0, text='Сталь 40Х, Dm - 200 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности - 790 МПа, Предел текучести - 640 МПа', variable=var, value=3).grid(row=4, column=0)
    mmaterial5 = Radiobutton(frame0, text='Сталь 40Х, Dm - 125 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности - 900 МПа, Предел текучести - 750 МПа', variable=var, value=4).grid(row=5, column=0)
    mmaterial6 = Radiobutton(frame0, text='Сталь 40Х, Dm - 125 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 45-50 HRCэ, Предел прочности - 900 МПа, Предел текучести - 750 МПа', variable=var, value=5).grid(row=6, column=0)   
    mmaterial7 = Radiobutton(frame0, text='Сталь 40ХН, Dm - 315 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности - 800 МПа, Предел текучести - 630 МПа', variable=var, value=6).grid(row=7, column=0)
    mmaterial8 = Radiobutton(frame0, text='Сталь 40ХН, Dm - 200 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности - 920 МПа, Предел текучести - 750 МПа', variable=var, value=7).grid(row=8, column=0)
    mmaterial9 = Radiobutton(frame0, text='Сталь 40ХН, Dm - 200 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 48-53 HRCэ, Предел прочности - 920 МПа, Предел текучести - 750 МПа', variable=var, value=8).grid(row=9, column=0)
    mmaterial10 = Radiobutton(frame0, text='Сталь 35ХМ, Dm - 315 мм, Термообработка - У, HBmin-HBmax = 235-262 HB, Предел прочности - 800 МПа, Предел текучести - 670 МПа', variable=var, value=9).grid(row=10, column=0)
    mmaterial11 = Radiobutton(frame0, text='Сталь 35ХМ, Dm - 200 мм, Термообработка - У, HBmin-HBmax = 269-302 HB, Предел прочности - 920 МПа, Предел текучести - 790 МПа', variable=var, value=10).grid(row=11, column=0)
    mmaterial12 = Radiobutton(frame0, text='Сталь 35ХМ, Dm - 200 мм, Термообработка - У+З(ТВЧ), HRCэmin-HRCэmax = 48-53 HRCэ, Предел прочности - 920 МПа, Предел текучести - 790 МПа', variable=var, value=11).grid(row=12, column=0)    
    mmaterial13 = Radiobutton(frame0, text='Сталь 20Х, Dm - 200 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности - 1000 МПа, Предел текучести - 800 МПа', variable=var, value=12).grid(row=13, column=0)
    mmaterial14 = Radiobutton(frame0, text='Сталь 20ХНМ, Dm - 200 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности - 1000 МПа, Предел текучести - 800 МПа', variable=var, value=13).grid(row=14, column=0)
    mmaterial15 = Radiobutton(frame0, text='Сталь 18ХГТ, Dm - 200 мм, Термообработка - У+Ц+З, HRCэmin-HRCэmax = 56-63 HRCэ, Предел прочности - 1000 МПа, Предел текучести - 800 МПа', variable=var, value=14).grid(row=15, column=0)
      
    frame1 = Frame(choiceshaft)
    frame1.grid(row=1, column=0)
    choice_button = Button(frame1, text='Назначить', command=ChoiceShaft, bg = 'light green').grid(row=0, column=0)
    close_button = Button(frame1, text='Завершить', command=choiceshaft.destroy, bg = 'light pink').grid(row=1, column=0)

#Проектный расчет валов и выбор подшипников качения
def DesignShaft():
    g_type = int(g_type_entry.get())
    scheme = int(scheme_entry.get())
    T_s1 = T1
    T_s2 = T2
    sb_s1 = sb1
    tk_s1 = 0.0275*sb_s1
    global d0_s1
    if scheme == 0:
        d_s1 = round((1000*T_s1/(0.2*tk_s1))**(1/3), 0)
        d0_s1 = 5*((d_s1+4)//5)
    else:
        d_s1 = round((1000*T_s1/(0.2*tk_s1))**(1/3), 0)
        de_s1 = round(0.9*di, 0)
        if d_s1 >= de_s1:
           d_s1 = d_s1
        else:
            d_s1 = de_s1
        d0_s1 = 5*((d_s1+4)//5)
    global d1_s1
    global d2_s1
    global d3_s1
    global d4_s1
    global d5_s1
    global d6_s1
    global d7_s1
    global d8_s1
    if g_type == 0 or g_type == 1:
        d1_s1 = d0_s1+5
        d2_s1 = d1_s1+5
        d3_s1 = d2_s1+5
        d4_s1 = da1
        d5_s1 = d3_s1
        d6_s1 = d2_s1
    else:
        d1_s1 = d0_s1+5
        d2_s1 = d1_s1+5
        d3_s1 = d2_s1+5
        d4_s1 = da1
        d5_s1 = da1-2*2.5*mn
        d6_s1 = d4_s1
        d7_s1 = d3_s1
        d8_s1 = d2_s1
    tk_s2 = 0.0275*sb2_s
    d_s2 = round((1000*T_s2/(0.2*tk_s2))**(1/3), 0)
    global d0_s2
    d0_s2 = 5*((d_s2+4)//5)
    global d1_s2
    global d2_s2
    global d3_s2
    global d4_s2
    global d5_s2
    global d6_s2
    d1_s2 = d0_s2+5
    d2_s2 = d1_s2+5
    d3_s2 = d2_s2+5
    d4_s2 = d3_s2+5
    d5_s2 = d3_s2
    d6_s2 = d2_s2
    BEARING_LIGHT = [
        [204, 20, 47, 14, 1.5, 12.7, 6.55],
        [205, 25, 52, 15, 1.5, 14.0, 7.8],
        [206, 30, 62, 16, 1.5, 19.5, 11.2],
        [207, 35, 72, 17, 2, 25.5, 15.3],
        [208, 40, 80, 18, 2, 30.7, 19.0],
        [209, 45, 85, 19, 2, 33.2, 21.6],
        [210, 50, 90, 20, 2, 35.1, 23.2],
        [211, 55, 100, 21, 2.5, 43.6, 29.0],
        [212, 60, 110, 22, 2.5, 52.0, 31.0],
        [213, 65, 120, 23, 2.5, 56.0, 34.0],
        [214, 70, 125, 24, 2.5, 60.5, 45.0],
        [215, 75, 130, 25, 2.5, 66.3, 41.0],
        [216, 80, 140, 26, 3.0, 70.2, 45.0],
        [217, 85, 150, 28, 3.0, 83.2, 64.0],
        [218, 90, 160, 30, 3.0, 95.6, 62.0],
        [219, 95, 170, 32, 3.5, 108, 81.5],
        [220, 100, 180, 34, 3.5, 124, 79.0],
        [221, 105, 190, 36, 3.5, 133, 90.0],
        [222, 110, 200, 38, 3.5, 146, 100],
        [224, 120, 215, 40, 3.5, 156, 112],
        [226, 130, 230, 40, 4.0, 156, 112],
        [228, 140, 250, 42, 4.0, 165, 122],
        [230, 150, 270, 45, 4.0, 189, 150]
        ]
    BEARING_MEDIUM = [
        [304, 20, 52, 15, 2, 15.9, 7.8],
        [305, 25, 62, 17, 2, 22.5, 11.6],
        [306, 30, 72, 19, 2, 28.1, 16.0],
        [307, 35, 80, 21, 2.5, 33.2, 19.0],
        [308, 40, 90, 23, 2.5, 41.0, 24.0],
        [309, 45, 100, 25, 2.5, 52.7, 31.5],
        [310, 50, 110, 27, 3.0, 61.8, 38.0],
        [311, 55, 120, 29, 3.0, 71.5, 41.5],
        [312, 60, 130, 31, 3.5, 81.9, 52.0],
        [313, 65, 140, 33, 3.5, 92.3, 60.0],
        [314, 70, 150, 35, 3.5, 104, 63.0],
        [315, 75, 160, 37, 3.5, 112, 72.5],
        [316, 80, 170, 39, 3.5, 124, 80.0],
        [317, 85, 180, 41, 4.0, 133, 90.0],
        [318, 90, 190, 43, 4.0, 143, 108],
        [319, 95, 200, 45, 4.0, 153, 110],
        [320, 100, 215, 47, 4.0, 174, 140],
        [321, 105, 225, 49, 4.0, 182, 153],
        [322, 110, 240, 50, 4.0, 203, 166],
        [324, 120, 260, 55, 4.0, 208, 180],
        [326, 130, 280, 58, 5.0, 229, 186],
        [330, 150, 320, 65, 5.0, 276, 285]
        ]
    j = 1
    global bearing1
    global d_b1
    global D_b1
    global B_b1
    global r_b1
    global C_b1
    global C0_b1
    for i in range(0, len(BEARING_MEDIUM)-1):
        if d2_s1 <= BEARING_MEDIUM[i][j]:
            bearing1 = BEARING_MEDIUM[i][0]
            d_b1 = BEARING_MEDIUM[i][j]
            D_b1 = BEARING_MEDIUM[i][2]
            B_b1 = BEARING_MEDIUM[i][3]
            r_b1 = BEARING_MEDIUM[i][4]
            C_b1 = BEARING_MEDIUM[i][5]
            C0_b1 = BEARING_MEDIUM[i][6]
            break
    j = 1
    global bearing2
    global d_b2
    global D_b2
    global B_b2
    global r_b2
    global C_b2
    global C0_b2
    for i in range(0, len(BEARING_LIGHT)-1):
        if d2_s2 <= BEARING_LIGHT[i][j]:
            bearing2 = BEARING_LIGHT[i][0]
            d_b2 = BEARING_LIGHT[i][j]
            D_b2 = BEARING_LIGHT[i][2]
            B_b2 = BEARING_LIGHT[i][3]
            r_b2 = BEARING_LIGHT[i][4]
            C_b2 = BEARING_LIGHT[i][5]
            C0_b2 = BEARING_LIGHT[i][6]
            break
    tk_s1_string = str(tk_s1)
    if g_type == 0 or g_type == 1:
        d0_s1_string = str(d0_s1)
        d1_s1_string = str(d1_s1)
        d2_s1_string = str(d2_s1)
        d3_s1_string = str(d3_s1)
        d4_s1_string = str(round(d4_s1, 3))
        d5_s1_string = str(d5_s1)
        d6_s1_string = str(d6_s1)
    else:
        d0_s1_string = str(d0_s1)
        d1_s1_string = str(d1_s1)
        d2_s1_string = str(d2_s1)
        d3_s1_string = str(d3_s1)
        d4_s1_string = str(round(d4_s1, 3))
        d5_s1_string = str(d5_s1)
        d6_s1_string = str(d6_s1)
        d7_s1_string = str(d7_s1)
        d8_s1_string = str(d8_s1)
    tk_s2_string = str(tk_s2)
    d0_s2_string = str(d0_s2)
    d1_s2_string = str(d1_s2)
    d2_s2_string = str(d2_s2)
    d3_s2_string = str(d3_s2)
    d4_s2_string = str(d4_s2)
    d5_s2_string = str(d5_s2)
    d6_s2_string = str(d6_s2)
    bearing1_string = str(bearing1)
    d_b1_string = str(d_b1)
    D_b1_string = str(D_b1)
    B_b1_string = str(B_b1)
    r_b1_string = str(r_b1)
    C_b1_string = str(C_b1)
    C0_b1_string = str(C0_b1)
    bearing2_string = str(bearing2)
    d_b2_string = str(d_b2)
    D_b2_string = str(D_b2)
    B_b2_string = str(B_b2)
    r_b2_string = str(r_b2)
    C_b2_string = str(C_b2)
    C0_b2_string = str(C0_b2)
    DesignShaft_file = open('C:/Users/Public/Documents/DesignShaft.txt', 'w')
    DesignShaft_file.write('tk_s1 = '+tk_s1_string+' МПа'+"\n")
    if g_type == 0 or g_type == 1:
        DesignShaft_file.write('d0_s1 = '+d0_s1_string+' мм'+"\n")
        DesignShaft_file.write('d1_s1 = '+d1_s1_string+' мм'+"\n")
        DesignShaft_file.write('d2_s1 = '+d2_s1_string+' мм'+"\n")
        DesignShaft_file.write('d3_s1 = '+d3_s1_string+' мм'+"\n")
        DesignShaft_file.write('d4_s1 = '+d4_s1_string+' мм'+"\n")
        DesignShaft_file.write('d5_s1 = '+d5_s1_string+' мм'+"\n")
        DesignShaft_file.write('d6_s1 = '+d6_s1_string+' мм'+"\n")
    else:
        DesignShaft_file.write('d0_s1 = '+d0_s1_string+' мм'+"\n")
        DesignShaft_file.write('d1_s1 = '+d1_s1_string+' мм'+"\n")
        DesignShaft_file.write('d2_s1 = '+d2_s1_string+' мм'+"\n")
        DesignShaft_file.write('d3_s1 = '+d3_s1_string+' мм'+"\n")
        DesignShaft_file.write('d4_s1 = '+d4_s1_string+' мм'+"\n")
        DesignShaft_file.write('d5_s1 = '+d5_s1_string+' мм'+"\n")
        DesignShaft_file.write('d6_s1 = '+d6_s1_string+' мм'+"\n")
        DesignShaft_file.write('d7_s1 = '+d7_s1_string+' мм'+"\n")
        DesignShaft_file.write('d8_s1 = '+d8_s1_string+' мм'+"\n")
    DesignShaft_file.write('tk_s2 = '+tk_s2_string+' МПа'+"\n")
    DesignShaft_file.write('d0_s2 = '+d0_s2_string+' мм'+"\n")
    DesignShaft_file.write('d1_s2 = '+d1_s2_string+' мм'+"\n")
    DesignShaft_file.write('d2_s2 = '+d2_s2_string+' мм'+"\n")
    DesignShaft_file.write('d3_s2 = '+d3_s2_string+' мм'+"\n")
    DesignShaft_file.write('d4_s2 = '+d4_s2_string+' мм'+"\n")
    DesignShaft_file.write('d5_s2 = '+d5_s2_string+' мм'+"\n")
    DesignShaft_file.write('d6_s2 = '+d6_s2_string+' мм'+"\n")
    DesignShaft_file.write('bearing1 - '+bearing1_string+"\n")
    DesignShaft_file.write('d_b1 = '+d_b1_string+' мм'+"\n")
    DesignShaft_file.write('D_b1 = '+D_b1_string+' мм'+"\n")
    DesignShaft_file.write('B_b1 = '+B_b1_string+' мм'+"\n")
    DesignShaft_file.write('r_b1 = '+r_b1_string+' мм'+"\n")
    DesignShaft_file.write('C_b1 = '+C_b1_string+' кН'+"\n")
    DesignShaft_file.write('C0_b1 = '+C0_b1_string+' кН'+"\n")
    DesignShaft_file.write('bearing2 - '+bearing2_string+"\n")
    DesignShaft_file.write('d_b2 = '+d_b2_string+' мм'+"\n")
    DesignShaft_file.write('D_b2 = '+D_b2_string+' мм'+"\n")
    DesignShaft_file.write('B_b2 = '+B_b2_string+' мм'+"\n")
    DesignShaft_file.write('r_b2 = '+r_b2_string+' мм'+"\n")
    DesignShaft_file.write('C_b2 = '+C_b2_string+' кН'+"\n")
    DesignShaft_file.write('C0_b2 = '+C0_b2_string+' кН'+"\n")
    DesignShaft_file.close()

#Расчет элементов корпуса
def BodyElements():
    #Толщина стенки корпуса
    global delta_b
    delta_b = 0.025*aw+1
    if delta_b < 8:
        delta_b = 8
    else:
        delta_b = round(delta_b, 0)
    L_b = aw +0.5*(da1+da2)
    #Расстояние от передачи до внутренних стенок корпуса редуктора
    global a_b
    a_b = round((L_b)**(1/3)+3, 0)
    for i in range(0, len(standart)-1):
        if (a_b <= standart[i]):
            a_b= standart[i]
            break
    #Расстояние от внутренней стенки корпуса редуктора до подшипника быстроходного вала
    global n_b
    n_b = 7
    dbs_t = [
        [8, 13, 24, 9, 17],
        [10, 15, 28, 11, 20],
        [12, 18, 33, 13, 25],
        [16, 21, 40, 17, 30],
        [20, 25, 48, 22, 38],
        [24, 28, 55, 26, 45],
        [30, 35, 68, 32, 56]
        ]
    #Диаметр фундаментного болта
    global db1_b
    global a1_b
    global b1_b
    global d1_b
    global D1_b
    db1_b = 0.036*aw+12
    j = 0
    for i in range(0, len(dbs_t)-1):
        if db1_b <= dbs_t[i][j]:
            db1_b = dbs_t[i][j]
            a1_b = dbs_t[i][1]
            b1_b = dbs_t[i][2]
            d1_b = dbs_t[i][3]
            D1_b = dbs_t[i][4]
            break
    #Расстояние от внутренней стенки корпуса до края лапы и до оси фундаментного болта
    global L1_b
    global P1_b
    L1_b = 3+delta_b+b1_b
    P1_b = 3+delta_b+a1_b
    #Диаметр болтов крепления крышки корпуса к основанию у подшипников
    global db2_b
    global a2_b
    global b2_b
    global d2_b
    global D2_b
    db2_b = 0.725*db1_b
    j = 0
    for i in range(0, len(dbs_t)-1):
        if db2_b <= dbs_t[i][j]:
            db2_b = dbs_t[i][j]
            a2_b = dbs_t[i][1]
            b2_b = dbs_t[i][2]
            d2_b = dbs_t[i][3]
            D2_b = dbs_t[i][4]
            break
    #Ширина фланцев у подшипников и расстояние от внутренней стенки корпуса редуктора до оси болта
    global L2_b
    global P2_b
    global t_b
    global Lb2_b
    t_b = 4
    L2_b = 3+delta_b+t_b+b2_b
    P2_b = 3+delta_b+a2_b
    Lb2_b = 0.5*D_b1+1.125*db2_b
    #Расчет подшипниковых крышек
    global db_c1
    global n0_c1
    global d0_c1
    global d1_c1
    global d2_c1
    global d3_c1
    global d4_c1
    global E_c1
    global e1_c1
    global C_c1
    global R_c1
    global a_c1
    if D_b1 <= 62:
        db_c1 = 6
        n0_c1 = 4
        d0_c1 = 7
        d1_c1 = D_b1-1
        d3_c1 = D_b1+2*db_c1
        d4_c1 = D_b1+4.5*db_c1
        E_c1 = 6
        e1_c1 = 8
        C_c1 = 1
        R_c1 = 0.6
    elif 62 < D_b1 <= 95:
        db_c1 = 8
        n0_c1 = 4
        d0_c1 = 9
        d1_c1 = D_b1-1.5
        d3_c1 = D_b1+2*db_c1
        d4_c1 = D_b1+4.5*db_c1
        E_c1 = 8
        e1_c1 = 10
        C_c1 = 1.5
        R_c1 = 0.6
    elif 95 < D_b1 <= 145:
        db_c1 = 10
        n0_c1 = 6
        d0_c1 = 11
        d1_c1 = D_b1-1.5
        d3_c1 = D_b1+2*db_c1
        d4_c1 = D_b1+4.5*db_c1
        E_c1 = 10
        e1_c1 = 12
        C_c1 = 2
        R_c1 = 0.6
    else:
        db_c1 = 12
        n0_c1 = 6
        d0_c1 = 13
        d1_c1 = D_b1-2
        d3_c1 = D_b1+2*db_c1
        d4_c1 = D_b1+4.5*db_c1
        E_c1 = 12
        e1_c1 = 15
        C_c1 = 2
        R_c1 = 0.8
    d2_c1 = 0.85*D_b1
    a_c1 = 5
    global db_c2
    global n0_c2
    global d0_c2
    global d1_c2
    global d2_c2
    global d3_c2
    global d4_c2
    global E_c2
    global e1_c2
    global C_c2
    global R_c2
    global a_c2
    if D_b2 <= 62:
        db_c2 = 6
        n0_c2 = 4
        d0_c2 = 7
        d1_c2 = D_b2-1
        d3_c2 = D_b2+2*db_c2
        d4_c2 = D_b2+4.5*db_c2
        E_c2 = 6
        e1_c2 = 8
        C_c2 = 1
        R_c2 = 0.6
    elif 62 < D_b2 <= 95:
        db_c2 = 8
        n0_c2 = 4
        d0_c2 = 9
        d1_c2 = D_b2-1.5
        d3_c2 = D_b2+2*db_c2
        d4_c2 = D_b2+4.5*db_c2
        E_c2 = 8
        e1_c2 = 10
        C_c2 = 1.5
        R_c2 = 0.6
    elif 95 < D_b2 <= 145:
        db_c2 = 10
        n0_c2 = 6
        d0_c2 = 11
        d1_c2 = D_b2-1.5
        d3_c2 = D_b2+2*db_c2
        d4_c2 = D_b2+4.5*db_c2
        E_c2 = 10
        e1_c2 = 12
        C_c2 = 2
        R_c2 = 0.6
    else:
        db_c2 = 12
        n0_c2 = 6
        d0_c2 = 13
        d1_c2 = D_b2-2
        d3_c2 = D_b2+2*db_c2
        d4_c2 = D_b2+4.5*db_c2
        E_c2 = 12
        e1_c2 = 15
        C_c2 = 2
        R_c2 = 0.8
    d2_c2 = 0.85*D_b2
    a_c2 = 5
    global d5_c1
    global S_c1
    if d1_s1 < 30:
        d5_c1 = d1_s1+1
        S_c1 = 2.5
    elif 30 <= d1_s1 < 60:
        d5_c1 = d1_s1+1
        S_c1 = 3.0
    elif 60 <= d1_s1 < 75:
        d5_c1 = d1_s1+1
        S_c1 = 3.5
    elif 75 <= d1_s1 < 100:
        d5_c1 = d1_s1+2
        S_c1 = 3.5
    else:
        d5_c1 = d1_s1+3
        S_c1 = 4.0
    global d5_c2
    global S_c2
    if d1_s2 < 30:
        d5_c2 = d1_s2+1
        S_c2 = 2.5
    elif 30 <= d1_s2 < 60:
        d5_c2 = d1_s2+1
        S_c2 = 3.0
    elif 60 <= d1_s2 < 75:
        d5_c2 = d1_s2+1
        S_c2 = 3.5
    elif 75 <= d1_s2 < 100:
        d5_c2 = d1_s2+2
        S_c2 = 3.5
    else:
        d5_c2 = d1_s2+3
        S_c2 = 4.0
    global Dy_c1
    global Sy_c1
    if d1_s1 == 20:
        Dy_c1 = 35
        Sy_c1 = 8
    elif d1_s1 == 25:
        Dy_c1 = 40
        Sy_c1 = 8
    elif d1_s1 == 30:
        Dy_c1 = 45
        Sy_c1 = 10
    elif d1_s1 == 35:
        Dy_c1 = 47
        Sy_c1 = 10
    elif d1_s1 == 40:
        Dy_c1 = 55
        Sy_c1 = 10
    elif d1_s1 == 45:
        Dy_c1 = 62
        Sy_c1 = 10
    elif d1_s1 == 50:
        Dy_c1 = 70
        Sy_c1 = 10
    elif d1_s1 == 55:
        Dy_c1 = 80
        Sy_c1 = 10
    elif d1_s1 == 60:
        Dy_c1 = 75
        Sy_c1 = 10
    elif d1_s1 == 65:
        Dy_c1 = 80
        Sy_c1 = 10
    elif d1_s1 == 70:
        Dy_c1 = 90
        Sy_c1 = 10
    elif d1_s1 == 75:
        Dy_c1 = 95
        Sy_c1 = 10
    global Dy_c2
    global Sy_c2
    if d1_s2 == 20:
        Dy_c2 = 35
        Sy_c2 = 8
    elif d1_s2 == 25:
        Dy_c2 = 40
        Sy_c2 = 8
    elif d1_s2 == 30:
        Dy_c2 = 45
        Sy_c2 = 10
    elif d1_s2 == 35:
        Dy_c2 = 47
        Sy_c2 = 10
    elif d1_s2 == 40:
        Dy_c2 = 55
        Sy_c2 = 10
    elif d1_s2 == 45:
        Dy_c2 = 62
        Sy_c2 = 10
    elif d1_s2 == 50:
        Dy_c2 = 70
        Sy_c2 = 10
    elif d1_s2 == 55:
        Dy_c2 = 80
        Sy_c2 = 10
    elif d1_s2 == 60:
        Dy_c2 = 75
        Sy_c2 = 10
    elif d1_s2 == 65:
        Dy_c2 = 80
        Sy_c2 = 10
    elif d1_s2 == 70:
        Dy_c2 = 90
        Sy_c2 = 10
    elif d1_s2 == 75:
        Dy_c2 = 95
        Sy_c2 = 10
    global Sc1_w
    global Kc1_b
    if db_c1 == 6:
        Sc1_w = 1.4
        Kc1_b = 4.0
    elif db_c1 == 8:
        Sc1_w = 2.0
        Kc1_b = 5.3
    elif db_c1 == 10:
        Sc1_w = 2.5
        Kc1_b = 6.4
    else:
        Sc1_w = 3.0
        Kc1_b = 7.5
    global Sc2_w
    global Kc2_b
    if db_c2 == 6:
        Sc2_w = 1.4
        Kc2_b = 4.0
    elif db_c2 == 8:
        Sc2_w = 2.0
        Kc2_b = 5.3
    elif db_c2 == 10:
        Sc2_w = 2.5
        Kc2_b = 6.4
    else:
        Sc2_w = 3.0
        Kc2_b = 7.5
    #Диаметр болтов крепления крышки корпуса к основанию на боковых фланцах
    global db3_b
    global a3_b
    global b3_b
    global d3_b
    global D3_b
    db3_b = 0.55*db1_b
    j = 0
    for i in range(0, len(dbs_t)-1):
        if db3_b <= dbs_t[i][j]:
            db3_b = dbs_t[i][j]
            a3_b = dbs_t[i][1]
            b3_b = dbs_t[i][2]
            d3_b = dbs_t[i][3]
            D3_b = dbs_t[i][4]
            break
    #Ширина боковых фланцев
    global L3_b
    L3_b = 3+delta_b+b3_b
    global t1_b
    t1_b = 2
    delta_b_string = str(delta_b)
    a_b_string = str(a_b)
    n_b_string = str(n_b)
    db1_b_string = str(db1_b)
    a1_b_string = str(a1_b)
    b1_b_string = str(b1_b)
    d1_b_string = str(d1_b)
    D1_b_string = str(D1_b)
    L1_b_string = str(L1_b)
    P1_b_string = str(P1_b)
    db2_b_string = str(db2_b)
    a2_b_string = str(a2_b)
    b2_b_string = str(b2_b)
    d2_b_string = str(d2_b)
    D2_b_string = str(D2_b)
    t_b_string = str(t_b)
    L2_b_string = str(L2_b)
    P2_b_string = str(P2_b)
    Lb2_b_string = str(Lb2_b)
    db_c1_string = str(db_c1)
    n0_c1_string = str(n0_c1)
    d0_c1_string = str(d0_c1)
    d1_c1_string = str(d1_c1)
    d2_c1_string = str(d2_c1)
    d3_c1_string = str(d3_c1)
    d4_c1_string = str(d4_c1)
    E_c1_string = str(E_c1)
    e1_c1_string = str(e1_c1)
    C_c1_string = str(C_c1)
    R_c1_string = str(R_c1)
    d5_c1_string = str(d5_c1)
    S_c1_string = str(S_c1)
    Dy_c1_string = str(Dy_c1)
    Sy_c1_string = str(Sy_c1)
    Sc1_w_string = str(Sc1_w)
    Kc1_b_string = str(Kc1_b)
    a_c1_string = str(a_c1)
    db_c2_string = str(db_c2)
    n0_c2_string = str(n0_c2)
    d0_c2_string = str(d0_c2)
    d1_c2_string = str(d1_c2)
    d2_c2_string = str(d2_c2)
    d3_c2_string = str(d3_c2)
    d4_c2_string = str(d4_c2)
    E_c2_string = str(E_c2)
    e1_c2_string = str(e1_c2)
    C_c2_string = str(C_c2)
    R_c2_string = str(R_c2)
    d5_c2_string = str(d5_c2)
    S_c2_string = str(S_c2)
    Dy_c2_string = str(Dy_c2)
    Sy_c2_string = str(Sy_c2)
    Sc2_w_string = str(Sc2_w)
    Kc2_b_string = str(Kc2_b)
    a_c2_string = str(a_c2)
    db3_b_string = str(db3_b)
    a3_b_string = str(a3_b)
    b3_b_string = str(b3_b)
    d3_b_string = str(d3_b)
    D3_b_string = str(D3_b)
    L3_b_string = str(L3_b)
    BodyElements_file = open('C:/Users/Public/Documents/BodyElements.txt', 'w')
    BodyElements_file.write('delta_b = '+delta_b_string+' мм'+"\n")
    BodyElements_file.write('a_b = '+a_b_string+' мм'+"\n")
    BodyElements_file.write('n_b = '+n_b_string+' мм'+"\n")
    BodyElements_file.write('Фундаментные болты'+"\n")
    BodyElements_file.write('М'+db1_b_string+"\n")
    BodyElements_file.write('a1_b = '+a1_b_string+' мм'+"\n")
    BodyElements_file.write('b1_b = '+b1_b_string+' мм'+"\n")
    BodyElements_file.write('d1_b = '+d1_b_string+' мм'+"\n")
    BodyElements_file.write('D1_b = '+D1_b_string+' мм'+"\n")
    BodyElements_file.write('L1_b = '+L1_b_string+' мм'+"\n")
    BodyElements_file.write('P1_b = '+P1_b_string+' мм'+"\n")
    BodyElements_file.write('Болты крепления крышки корпуса к основанию у подшипников'+"\n")
    BodyElements_file.write('М'+db2_b_string+"\n")
    BodyElements_file.write('a2_b = '+a2_b_string+' мм'+"\n")
    BodyElements_file.write('b2_b = '+b2_b_string+' мм'+"\n")
    BodyElements_file.write('d2_b = '+d2_b_string+' мм'+"\n")
    BodyElements_file.write('D2_b = '+D2_b_string+' мм'+"\n")
    BodyElements_file.write('L2_b = '+L2_b_string+' мм'+"\n")
    BodyElements_file.write('P2_b = '+P2_b_string+' мм'+"\n")
    BodyElements_file.write('Lb2_b = '+Lb2_b_string+' мм'+"\n")
    BodyElements_file.write('Подшипниковые крышки'+"\n")
    BodyElements_file.write('db_c1 = '+db_c1_string+' мм'+"\n")
    BodyElements_file.write('n0_c1 = '+n0_c1_string+"\n")
    BodyElements_file.write('d0_c1 = '+d0_c1_string+' мм'+"\n")
    BodyElements_file.write('d1_c1 = '+d1_c1_string+' мм'+"\n")
    BodyElements_file.write('d2_c1 = '+d2_c1_string+' мм'+"\n")
    BodyElements_file.write('d3_c1 = '+d3_c1_string+' мм'+"\n")
    BodyElements_file.write('d4_c1 = '+d4_c1_string+' мм'+"\n")
    BodyElements_file.write('E_c1 = '+E_c1_string+' мм'+"\n")
    BodyElements_file.write('e1_c1 = '+e1_c1_string+' мм'+"\n")
    BodyElements_file.write('C_c1 = '+C_c1_string+' мм'+"\n")
    BodyElements_file.write('R_c1 = '+R_c1_string+' мм'+"\n")
    BodyElements_file.write('d5_c1 = '+d5_c1_string+' мм'+"\n")
    BodyElements_file.write('S_c1 = '+S_c1_string+' мм'+"\n")
    BodyElements_file.write('Dy_c1 = '+Dy_c1_string+' мм'+"\n")
    BodyElements_file.write('Sy_c1 = '+Sy_c1_string+' мм'+"\n")
    BodyElements_file.write('Sc1_w = '+Sc1_w_string+' мм'+"\n")
    BodyElements_file.write('Kc1_b = '+Kc1_b_string+' мм'+"\n")
    BodyElements_file.write('a_c1 = '+a_c1_string+' град'+"\n")
    BodyElements_file.write('db_c2 = '+db_c2_string+' мм'+"\n")
    BodyElements_file.write('n0_c2 = '+n0_c2_string+"\n")
    BodyElements_file.write('d0_c2 = '+d0_c2_string+' мм'+"\n")
    BodyElements_file.write('d1_c2 = '+d1_c2_string+' мм'+"\n")
    BodyElements_file.write('d2_c2 = '+d2_c2_string+' мм'+"\n")
    BodyElements_file.write('d3_c2 = '+d3_c2_string+' мм'+"\n")
    BodyElements_file.write('d4_c2 = '+d4_c2_string+' мм'+"\n")
    BodyElements_file.write('E_c2 = '+E_c2_string+' мм'+"\n")
    BodyElements_file.write('e1_c2 = '+e1_c2_string+' мм'+"\n")
    BodyElements_file.write('C_c2 = '+C_c2_string+' мм'+"\n")
    BodyElements_file.write('R_c2 = '+R_c2_string+' мм'+"\n")
    BodyElements_file.write('d5_c2 = '+d5_c2_string+' мм'+"\n")
    BodyElements_file.write('S_c2 = '+S_c2_string+' мм'+"\n")
    BodyElements_file.write('Dy_c2 = '+Dy_c2_string+' мм'+"\n")
    BodyElements_file.write('Sy_c2 = '+Sy_c2_string+' мм'+"\n")
    BodyElements_file.write('Sc2_w = '+Sc2_w_string+' мм'+"\n")
    BodyElements_file.write('Kc2_b = '+Kc2_b_string+' мм'+"\n")
    BodyElements_file.write('a_c2 = '+a_c2_string+' град'+"\n")
    BodyElements_file.write('Болты крепления крышки корпуса к основанию на боковых фланцах'+"\n")
    BodyElements_file.write('М'+db3_b_string+"\n")
    BodyElements_file.write('a3_b = '+a3_b_string+' мм'+"\n")
    BodyElements_file.write('b3_b = '+b3_b_string+' мм'+"\n")
    BodyElements_file.write('d3_b = '+d3_b_string+' мм'+"\n")
    BodyElements_file.write('D3_b = '+D3_b_string+' мм'+"\n")
    BodyElements_file.write('L3_b = '+L3_b_string+' мм'+"\n")
    BodyElements_file.close()

#Компановочное решение
def LayoutSolution():
    g_type = int(g_type_entry.get())
    scheme = int(scheme_entry.get())
    c_type = int(c_type_entry.get())
    #Определение ширины проточной дорожки для выхода фрезы
    a_dt = [
        [1.5, 28, 30],
        [2, 32, 35],
        [2.5, 37, 40],
        [3, 42, 45],
        [3.5, 47, 50],
        [4, 52, 55],
        [4.5, 55, 58],
        [5, 58, 63],
        [6, 67, 72],
        [7, 75, 82],
        [8, 82, 90],
        [10, 100, 108]
        ]
    j = 0
    for i in range(0, len(a_dt)-1):
        if (mn <= a_dt[i][j] and B < 30):
            a = a_dt[i][1]
            break
        elif (mn <= a_dt[i][j] and B >= 30):
            a = a_dt[i][2]
            break
    if c_type == 0:
        L = 841
        W = 594
    else:
        L = 594
        W = 841
    L_string = str(L)
    W_string = str(W)
    LayoutSolution_file = open('C:/Users/Public/Documents/LayoutSolution.txt', 'w')
    #Лист чертежа А1 ГОСТ Р 21.1101-2013
    LayoutSolution_file.write(';The clipping path'+"\n")
    LayoutSolution_file.write('(command "LAYER" "M" "1" "C" "3" "1" "LW" "0.05" "1" "")'+"\n")
    LayoutSolution_file.write('(command "LAYER" "s" "1"  "")'+"\n")
    LayoutSolution_file.write('(setq P0 (list 0 0))'+"\n")
    LayoutSolution_file.write('(setq P1 (list 0 '+W_string+'))'+"\n")
    LayoutSolution_file.write('(setq P2 (list '+L_string+' '+W_string+'))'+"\n")
    LayoutSolution_file.write('(setq P3 (list '+L_string+' 0))'+"\n")
    LayoutSolution_file.write('(command "PLINE" P0 P1 P2 P3 P0 "")'+"\n")
    LayoutSolution_file.write(';The design of the drawing sheet'+"\n")
    LayoutSolution_file.write('(command "LAYER" "M" "2" "C" "3" "2" "LW" "1" "2" "")'+"\n")
    LayoutSolution_file.write('(command "LAYER" "s" "2"  "")'+"\n")
    LayoutSolution_file.write('(setq P4 (list 20 5))'+"\n")
    LayoutSolution_file.write('(setq P5 (list 20 (- '+W_string+' 5)))'+"\n")
    LayoutSolution_file.write('(setq P6 (list (- '+L_string+' 5) (- '+W_string+' 5)))'+"\n")
    LayoutSolution_file.write('(setq P7 (list (- '+L_string+' 5) 5))'+"\n")
    LayoutSolution_file.write('(command "PLINE" P4 P5 P6 P7 P4 "")'+"\n")
    LayoutSolution_file.write('(setq P8 (list (- '+L_string+' 190) 5))'+"\n")
    LayoutSolution_file.write('(setq P9 (list (- '+L_string+' 190) 60))'+"\n")
    LayoutSolution_file.write('(setq P10 (list (- '+L_string+' 5) 60))'+"\n")
    LayoutSolution_file.write('(command "LINE" P8 P9 P10 "")'+"\n")
    LayoutSolution_file.write('(setq P11 (list (- '+L_string+' 180) 35))'+"\n")
    LayoutSolution_file.write('(setq P12 (list (- '+L_string+' 180) 60))'+"\n")
    LayoutSolution_file.write('(command "LINE" P11 P12 "")'+"\n")
    LayoutSolution_file.write('(setq P13 (list (- '+L_string+' 170) 5))'+"\n")
    LayoutSolution_file.write('(setq P14 (list (- '+L_string+' 170) 60))'+"\n")
    LayoutSolution_file.write('(command "LINE" P13 P14 "")'+"\n")
    LayoutSolution_file.write('(setq P15 (list (- '+L_string+' 160) 35))'+"\n")
    LayoutSolution_file.write('(setq P16 (list (- '+L_string+' 160) 60))'+"\n")
    LayoutSolution_file.write('(command "LINE" P15 P16 "")'+"\n")
    LayoutSolution_file.write('(setq P17 (list (- '+L_string+' 150) 5))'+"\n")
    LayoutSolution_file.write('(setq P18 (list (- '+L_string+' 150) 60))'+"\n")
    LayoutSolution_file.write('(command "LINE" P17 P18 "")'+"\n")
    LayoutSolution_file.write('(setq P19 (list (- '+L_string+' 135) 5))'+"\n")
    LayoutSolution_file.write('(setq P20 (list (- '+L_string+' 135) 60))'+"\n")
    LayoutSolution_file.write('(command "LINE" P19 P20 "")'+"\n")
    LayoutSolution_file.write('(setq P21 (list (- '+L_string+' 125) 5))'+"\n")
    LayoutSolution_file.write('(setq P22 (list (- '+L_string+' 125) 60))'+"\n")
    LayoutSolution_file.write('(command "LINE" P21 P22 "")'+"\n")
    LayoutSolution_file.write('(setq P23 (list (- '+L_string+' 55) 5))'+"\n")
    LayoutSolution_file.write('(setq P24 (list (- '+L_string+' 55) 45))'+"\n")
    LayoutSolution_file.write('(command "LINE" P23 P24 "")'+"\n")
    LayoutSolution_file.write('(setq P25 (list (- '+L_string+' 40) 25))'+"\n")
    LayoutSolution_file.write('(setq P26 (list (- '+L_string+' 40) 45))'+"\n")
    LayoutSolution_file.write('(command "LINE" P25 P26 "")'+"\n")
    LayoutSolution_file.write('(setq P27 (list (- '+L_string+' 35) 20))'+"\n")
    LayoutSolution_file.write('(setq P28 (list (- '+L_string+' 35) 25))'+"\n")
    LayoutSolution_file.write('(command "LINE" P27 P28 "")'+"\n")
    LayoutSolution_file.write('(setq P29 (list (- '+L_string+' 25) 25))'+"\n")
    LayoutSolution_file.write('(setq P30 (list (- '+L_string+' 25) 45))'+"\n")
    LayoutSolution_file.write('(command "LINE" P29 P30 "")'+"\n")
    LayoutSolution_file.write('(setq P31 (list (- '+L_string+' 125) 45))'+"\n")
    LayoutSolution_file.write('(setq P32 (list (- '+L_string+' 5) 45))'+"\n")
    LayoutSolution_file.write('(command "LINE" P31 P32 "")'+"\n")
    LayoutSolution_file.write('(setq P33 (list (- '+L_string+' 190) 40))'+"\n")
    LayoutSolution_file.write('(setq P34 (list (- '+L_string+' 125) 40))'+"\n")
    LayoutSolution_file.write('(command "LINE" P33 P34 "")'+"\n")
    LayoutSolution_file.write('(setq P35 (list (- '+L_string+' 55) 40))'+"\n")
    LayoutSolution_file.write('(setq P36 (list (- '+L_string+' 5) 40))'+"\n")
    LayoutSolution_file.write('(command "LINE" P35 P36 "")'+"\n")
    LayoutSolution_file.write('(setq P37 (list (- '+L_string+' 190) 35))'+"\n")
    LayoutSolution_file.write('(setq P38 (list (- '+L_string+' 125) 35))'+"\n")
    LayoutSolution_file.write('(command "LINE" P37 P38 "")'+"\n")
    LayoutSolution_file.write('(setq P39 (list (- '+L_string+' 125) 20))'+"\n")
    LayoutSolution_file.write('(setq P40 (list (- '+L_string+' 5) 20))'+"\n")
    LayoutSolution_file.write('(command "LINE" P39 P40 "")'+"\n")
    LayoutSolution_file.write('(setq P41 (list 20 (- '+W_string+' 19)))'+"\n")
    LayoutSolution_file.write('(setq P42 (list 90 (- '+W_string+' 19)))'+"\n")
    LayoutSolution_file.write('(setq P43 (list 90 (- '+W_string+' 5)))'+"\n")
    LayoutSolution_file.write('(command "LINE" P41 P42 P43 "")'+"\n")
    LayoutSolution_file.write('(command "LAYER" "M" "3" "C" "3" "3" "LW" "0.5" "3" "")'+"\n")
    LayoutSolution_file.write('(command "LAYER" "s" "3"  "")'+"\n")
    LayoutSolution_file.write('(setq P44 (list (- '+L_string+' 190) 55))'+"\n")
    LayoutSolution_file.write('(setq P45 (list (- '+L_string+' 125) 55))'+"\n")
    LayoutSolution_file.write('(command "LINE" P44 P45 "")'+"\n")
    LayoutSolution_file.write('(setq P46 (list (- '+L_string+' 190) 50))'+"\n")
    LayoutSolution_file.write('(setq P47 (list (- '+L_string+' 125) 50))'+"\n")
    LayoutSolution_file.write('(command "LINE" P46 P47 "")'+"\n")
    LayoutSolution_file.write('(setq P48 (list (- '+L_string+' 190) 45))'+"\n")
    LayoutSolution_file.write('(setq P49 (list (- '+L_string+' 125) 45))'+"\n")
    LayoutSolution_file.write('(command "LINE" P48 P49 "")'+"\n")
    LayoutSolution_file.write('(setq P50 (list (- '+L_string+' 190) 30))'+"\n")
    LayoutSolution_file.write('(setq P51 (list (- '+L_string+' 125) 30))'+"\n")
    LayoutSolution_file.write('(command "LINE" P50 P51 "")'+"\n")
    LayoutSolution_file.write('(setq P52 (list (- '+L_string+' 190) 25))'+"\n")
    LayoutSolution_file.write('(setq P53 (list (- '+L_string+' 125) 25))'+"\n")
    LayoutSolution_file.write('(command "LINE" P52 P53 "")'+"\n")
    LayoutSolution_file.write('(setq P54 (list (- '+L_string+' 190) 20))'+"\n")
    LayoutSolution_file.write('(setq P55 (list (- '+L_string+' 125) 20))'+"\n")
    LayoutSolution_file.write('(command "LINE" P54 P55 "")'+"\n")
    LayoutSolution_file.write('(setq P56 (list (- '+L_string+' 190) 15))'+"\n")
    LayoutSolution_file.write('(setq P57 (list (- '+L_string+' 125) 15))'+"\n")
    LayoutSolution_file.write('(command "LINE" P56 P57 "")'+"\n")
    LayoutSolution_file.write('(setq P58 (list (- '+L_string+' 190) 10))'+"\n")
    LayoutSolution_file.write('(setq P59 (list (- '+L_string+' 125) 10))'+"\n")
    LayoutSolution_file.write('(command "LINE" P58 P59 "")'+"\n")
    LayoutSolution_file.write('(setq P60 (list (- '+L_string+' 55) 25))'+"\n")
    LayoutSolution_file.write('(setq P61 (list (- '+L_string+' 5) 25))'+"\n")
    LayoutSolution_file.write('(command "LINE" P60 P61 "")'+"\n")
    LayoutSolution_file.write('(command "LAYER" "M" "4" "C" "30" "4" "LW" "1" "4" "")'+"\n")
    LayoutSolution_file.write('(command "LAYER" "s" "4"  "")'+"\n")
    #Оформление компановочного решения горизонтального редуктора с прямым или косым зубом
    if c_type == 0 and (g_type == 0 or g_type == 1):
        x1_d = L/2-aw/2-da1/2
        y1_d = W/2-bw1/2
        x2_d = x1_d
        y2_d = W/2+bw1/2
        x3_d = L/2-aw/2+da1/2
        y3_d = y2_d
        x4_d = x3_d
        y4_d = y1_d
        x5_d = L/2+aw/2-da2/2
        y5_d = W/2-bw2/2
        x6_d = x5_d
        y6_d = W/2+bw2/2
        x7_d = L/2+aw/2+da2/2
        y7_d = y6_d
        x8_d = x7_d
        y8_d = y5_d
        x9_d = x1_d-a_b
        y9_d = y1_d-a_b
        x10_d = x9_d
        y10_d = y2_d+a_b
        x11_d = x7_d+a_b
        y11_d = y10_d
        x12_d = x11_d
        y12_d = y9_d
        x13_d = L/2-aw/2-D_b1/2
        y13_d = y9_d-n_b-B_b1
        x14_d = x13_d
        y14_d = y9_d-n_b
        x15_d = L/2-aw/2+D_b1/2
        y15_d = y14_d
        x16_d = x15_d
        y16_d = y13_d
        x17_d = L/2-aw/2-d_b1/2
        y17_d = y16_d
        x18_d = x17_d
        y18_d = y15_d
        x19_d = L/2-aw/2+d_b1/2
        y19_d = y18_d
        x20_d = x19_d
        y20_d = y17_d
        x21_d = x14_d
        y21_d = y10_d+n_b
        x22_d = x21_d
        y22_d = y10_d+n_b+B_b1
        x23_d = x16_d
        y23_d = y22_d
        x24_d = x23_d
        y24_d = y21_d
        x25_d = x18_d
        y25_d = y24_d
        x26_d = x25_d
        y26_d = y23_d
        x27_d = x20_d
        y27_d = y26_d
        x28_d = x27_d
        y28_d = y25_d
        x29_d = L/2+aw/2-D_b2/2
        y29_d = y19_d-B_b1/2-B_b2/2
        x30_d = x29_d
        y30_d = y29_d+B_b2
        x31_d = L/2+aw/2+D_b2/2
        y31_d = y30_d
        x32_d = x31_d
        y32_d = y29_d
        x33_d = L/2+aw/2-d_b2/2
        y33_d = y32_d
        x34_d = x33_d
        y34_d = y31_d
        x35_d = L/2+aw/2+d_b2/2
        y35_d = y34_d
        x36_d = x35_d
        y36_d = y33_d
        x37_d = x30_d
        y37_d = y28_d+B_b1/2-B_b2/2
        x38_d = x37_d
        y38_d = y37_d+B_b2
        x39_d = x32_d
        y39_d = y38_d
        x40_d = x39_d
        y40_d = y37_d
        x41_d = x34_d
        y41_d = y40_d
        x42_d = x41_d
        y42_d = y39_d
        x43_d = x36_d
        y43_d = y42_d
        x44_d = x43_d
        y44_d = y41_d
        x45_d = (x14_d+x18_d)/2
        y45_d = (y17_d+y18_d)/2
        x46_d = (x16_d+x20_d)/2
        y46_d = y45_d
        x47_d = x45_d
        y47_d = (y25_d+y26_d)/2
        x48_d = x46_d
        y48_d = y47_d
        #Условный радиус подшипникового шарика
        r1_d = 2*B_b1/3*0.5
        x49_d = (x30_d+x34_d)/2
        y49_d = (y33_d+y34_d)/2
        x50_d = (x31_d+x35_d)/2
        y50_d = y49_d
        x51_d = x49_d
        y51_d = (y41_d+y42_d)/2
        x52_d = x50_d
        y52_d = y51_d
        #Условный радиус подшипникового шарика
        r2_d = 2*B_b2/3*0.5
        x53_d = x14_d
        y53_d = y14_d+n_b
        x54_d = x53_d
        y54_d = y53_d-L2_b
        x55_d = x15_d
        y55_d = y53_d
        x56_d = x55_d
        y56_d = y54_d
        x57_d = x21_d
        y57_d = y21_d-n_b
        x58_d = x57_d
        y58_d = y57_d+L2_b
        x59_d = x24_d
        y59_d = y57_d
        x60_d = x59_d
        y60_d = y58_d
        x61_d = x30_d
        y61_d = y55_d
        x62_d = x61_d
        y62_d = y61_d-L2_b
        x63_d = x31_d
        y63_d = y61_d
        x64_d = x63_d
        y64_d = y62_d
        x65_d = x37_d
        y65_d = y59_d
        x66_d = x65_d
        y66_d = y65_d+L2_b
        x67_d = x40_d
        y67_d = y65_d
        x68_d = x67_d
        y68_d = y66_d
        x69_d = L/2-aw/2-d4_c1/2
        y69_d = y54_d
        x70_d = L/2-aw/2+d4_c1/2
        y70_d = y56_d
        x71_d = x69_d
        y71_d = y58_d
        if x69_d <x9_d:
            x9_d = x69_d
            x10_d = x71_d
        else:
            x9_d = x9_d
            x10_d = x10_d
        x72_d = x70_d
        y72_d = y60_d
        x73_d = L/2+aw/2-d4_c2/2
        y73_d = y62_d
        x74_d = L/2+aw/2+d4_c2/2
        y74_d = y64_d
        x75_d = x73_d
        y75_d = y66_d
        x76_d = x74_d
        y76_d = y68_d
        x77_d = x69_d
        y77_d = y69_d+t_b
        x78_d = x77_d-L3_b
        y78_d = y77_d
        x79_d = x78_d
        y79_d = y71_d-t_b
        x80_d = x77_d
        y80_d = y79_d
        x81_d = x70_d
        y81_d = y70_d+t_b
        x82_d = x73_d
        y82_d = y81_d
        x83_d = x72_d
        y83_d = y72_d-t_b
        x84_d = x75_d
        y84_d = y83_d
        x85_d = x74_d
        y85_d = y74_d+t_b
        x86_d = x12_d+L3_b
        y86_d = y85_d
        x87_d = x86_d
        y87_d = y76_d-t_b
        x88_d = x76_d
        y88_d = y87_d
        x89_d = x69_d
        y89_d = y69_d-t1_b
        x90_d = x54_d
        y90_d = y89_d
        x91_d = x71_d
        y91_d = y71_d+t1_b
        x92_d = x58_d
        y92_d = y91_d
        x93_d = x56_d
        y93_d = y90_d
        x94_d = x70_d
        y94_d = y93_d
        x95_d = x60_d
        y95_d = y92_d
        x96_d = x72_d
        y96_d = y95_d
        x97_d = x73_d
        y97_d = y94_d
        x98_d = x62_d
        y98_d = y97_d
        x99_d = x75_d
        y99_d = y96_d
        x100_d = x66_d
        y100_d = y99_d
        x101_d = x64_d
        y101_d = y98_d
        x102_d = x74_d
        y102_d = y101_d
        x103_d = x68_d
        y103_d = y100_d
        x104_d = x76_d
        y104_d = y103_d
        x105_d = x91_d
        y105_d = y91_d+E_c1-C_c1
        x106_d = x105_d+C_c1
        y106_d = y91_d+E_c1
        x107_d = x96_d-C_c1
        y107_d = y106_d
        x108_d = x96_d
        y108_d = y96_d+E_c1-C_c1
        x109_d = x92_d
        y109_d = y92_d-e1_c1
        x110_d = x109_d+0.5*(D_b1-d1_c1)
        y110_d = y109_d
        x111_d = x110_d
        y111_d = y22_d
        x112_d = x95_d
        y112_d = y110_d
        x113_d = x112_d-0.5*(D_b1-d1_c1)
        y113_d = y112_d
        x114_d = x113_d
        y114_d = y23_d
        x115_d = x111_d+0.5*(d1_c1-d2_c1)
        y115_d = y111_d
        x116_d = x115_d+(y92_d-y111_d)*tan(a_c1*pi/180)
        y116_d = y92_d
        x117_d = x115_d+d2_c1-2*(y92_d-y111_d)*tan(a_c1*pi/180)
        y117_d = y116_d
        x118_d = x117_d+(y92_d-y111_d)*tan(a_c1*pi/180)
        y118_d = y115_d
        x119_d = x89_d
        y119_d = y89_d-E_c1+C_c1
        x120_d = x119_d+C_c1
        y120_d = y119_d-C_c1
        x121_d = L/2-aw/2-d5_c1/2
        y121_d = y120_d
        x122_d = L/2-aw/2-d1_s1/2
        y122_d = y121_d
        x123_d = L/2-aw/2+d1_s1/2
        y123_d = y122_d
        x124_d = L/2-aw/2+d5_c1/2
        y124_d = y123_d
        x125_d = x94_d-C_c1
        y125_d = y124_d
        x126_d = x94_d
        y126_d = y125_d+C_c1
        x127_d = x115_d
        y127_d = y16_d
        y128_d = y121_d+S_c1+Sy_c1
        x128_d = x127_d+(y127_d-y128_d)*tan(a_c1*pi/180)
        x129_d = L/2-aw/2-Dy_c1/2
        y129_d = y128_d
        x130_d = x122_d
        y130_d = y129_d
        x131_d = x123_d
        y131_d = y130_d
        x132_d = L/2-aw/2+Dy_c1/2
        y132_d = y131_d
        x134_d = x118_d
        y134_d = y127_d
        x133_d = x134_d-(y127_d-y128_d)*tan(a_c1*pi/180)
        y133_d = y132_d
        x135_d = x129_d
        y135_d = y129_d-Sy_c1
        x136_d = x121_d
        y136_d = y135_d
        x137_d = x122_d
        y137_d = y136_d
        x138_d = x123_d
        y138_d = y137_d
        x139_d = x124_d
        y139_d = y138_d
        x140_d = x132_d
        y140_d = y139_d
        x141_d = x13_d
        y141_d = y13_d-e1_c1
        x142_d = x110_d
        y142_d = y141_d
        x143_d = x142_d
        y143_d = y13_d
        x144_d = x16_d
        y144_d = y142_d
        x145_d = x113_d
        y145_d = y144_d
        x146_d = x145_d
        y146_d = y16_d
        x147_d = x99_d
        y147_d = y99_d+E_c2-C_c2
        x148_d = x147_d+C_c2
        y148_d = y147_d+C_c2
        x149_d = L/2+aw/2-d5_c2/2
        y149_d = y148_d
        x150_d = L/2+aw/2-d1_s2/2
        y150_d = y149_d
        x151_d = L/2+aw/2+d1_s2/2
        y151_d = y150_d
        x152_d = L/2+aw/2+d5_c2/2
        y152_d = y151_d
        x153_d = x104_d-C_c2
        y153_d = y152_d
        x154_d = x104_d
        y154_d = y153_d-C_c2
        x155_d = L/2+aw/2-d2_c2/2
        y155_d = y42_d
        y156_d = y153_d-S_c2-Sy_c2
        x156_d = x155_d+(y156_d-y155_d)*tan(a_c2*pi/180)
        x157_d = L/2+aw/2-Dy_c2/2
        y157_d = y156_d
        x157_1_d = x150_d
        y157_1_d = y157_d
        x158_d = x157_d
        y158_d = y157_d+Sy_c2
        x159_d = x149_d
        y159_d = y158_d
        x160_d = x150_d
        y160_d = y159_d
        x161_d = x151_d
        y161_d = y160_d
        x162_d = x152_d
        y162_d = y161_d
        x163_d = L/2+aw/2+Dy_c2/2
        y163_d = y162_d
        x164_d = x163_d
        y164_d = y157_d
        x165_d = L/2+aw/2+d2_c2/2-(y156_d-y155_d)*tan(a_c2*pi/180)
        x164_1_d = x161_d
        y164_1_d = y164_d
        y165_d = y164_d
        x166_d = L/2+aw/2+d2_c2/2
        y166_d = y155_d
        x167_d = x100_d
        y167_d = y100_d-e1_c2
        x168_d = L/2+aw/2-d1_c2/2
        y168_d = y167_d
        x169_d = x168_d
        y169_d = y155_d
        x170_d = x103_d
        y170_d = y103_d-e1_c2
        x171_d = L/2+aw/2+d1_c2/2
        y171_d = y170_d
        x172_d = x171_d
        y172_d = y166_d
        x173_d = x97_d
        y173_d = y97_d-E_c2+C_c2
        x174_d = x173_d+C_c2
        y174_d = y173_d-C_c2
        x175_d = x102_d-C_c2
        y175_d = y174_d
        x176_d = x175_d+C_c2
        y176_d = y173_d
        x177_d = x98_d
        y177_d = y98_d+e1_c2
        x178_d = L/2+aw/2-d1_c2/2
        y178_d = y177_d
        x179_d = x178_d
        y179_d = y29_d
        x180_d = x101_d
        y180_d = y177_d
        x181_d = L/2+aw/2+d1_c2/2
        y181_d = y180_d
        x182_d = x181_d
        y182_d = y179_d
        x183_d = L/2+aw/2+d2_c2/2
        y183_d = y182_d
        y184_d = y101_d
        x184_d = x183_d-(y183_d-y184_d)*tan(a_c2*pi/180)
        x186_d = L/2+aw/2-d2_c2/2
        y186_d = y179_d
        x185_d = x186_d+(y183_d-y184_d)*tan(a_c2*pi/180)
        y185_d = y184_d
        x187_d = L/2-aw/2-d5_s1/2
        y187_d = y28_d
        x188_d = x187_d
        y188_d = y3_d
        x189_d = L/2-aw/2+d5_s1/2
        y189_d = y187_d
        x190_d = x189_d
        y190_d = y188_d
        x191_d = x188_d
        y191_d = y4_d
        x192_d = x191_d
        y192_d = y19_d
        x193_d = x190_d
        y193_d = y191_d
        x194_d = x193_d
        y194_d = y192_d
        x195_d = L/2-aw/2-d1_s1/2
        y195_d = y20_d
        x196_d = L/2-aw/2+d1_s1/2
        y196_d = y195_d
        x197_d = x195_d
        y197_d = y122_d-Sc1_w-Kc1_b-10
        x198_d = x196_d
        y198_d = y197_d
        x199_d = L/2-aw/2-d0_s1/2
        y199_d = y198_d
        x200_d = L/2-aw/2+d0_s1/2
        y200_d = y199_d
        x201_d = x199_d
        y201_d = y199_d-2*d0_s1
        x202_d = x200_d
        y202_d = y201_d
        x209_d = L/2+aw/2-d3_s2/2
        y209_d = y8_d
        x210_d = x209_d
        y210_d = y7_d
        x211_d = L/2+aw/2+d3_s2/2
        y211_d = y210_d
        x212_d = x211_d
        y212_d = y209_d
        x213_d = L/2+aw/2-d2_s2/2
        y213_d = y210_d
        x214_d = L/2+aw/2+d2_s2/2
        y214_d = y211_d
        x215_d = L/2+aw/2-d1_s2/2
        y215_d = y42_d
        x216_d = L/2+aw/2+d1_s2/2
        y216_d = y43_d
        x217_d = x215_d
        y217_d = y150_d+Sc2_w+Kc2_b+10
        x218_d = x216_d
        y218_d = y217_d
        x219_d = L/2+aw/2-d0_s2/2
        y219_d = y218_d
        x220_d = L/2+aw/2+d0_s2/2
        y220_d = y219_d
        x221_d = x219_d
        y221_d = y219_d+2*d0_s2
        x222_d = x220_d
        y222_d = y221_d
        x223_d = L/2+aw/2-d4_s2/2
        y223_d = y209_d
        x224_d = L/2+aw/2+d4_s2/2
        y224_d = y212_d
        x225_d = x223_d
        y225_d = y223_d-10
        x226_d = x224_d
        y226_d = y225_d
        x227_d = L/2+aw/2-d5_s2/2
        y227_d = y225_d
        x228_d = L/2+aw/2+d5_s2/2
        y228_d = y227_d
        x229_d = x227_d
        y229_d = y34_d
        x230_d = x228_d
        y230_d = y229_d
        x240_d = L/2-aw/2-df1/2
        y240_d = y1_d
        x241_d = x240_d
        y241_d = y2_d
        x242_d = L/2-aw/2+df1/2
        y242_d = y240_d
        x243_d = x242_d
        y243_d = y241_d
        x244_d = L/2+aw/2-df2/2
        y244_d = y5_d
        x245_d = x244_d
        y245_d = y6_d
        x246_d = L/2+aw/2+df2/2
        y246_d = y244_d
        x247_d = x246_d
        y247_d = y245_d
        x1_d_string = str(round(x1_d, 3))
        y1_d_string = str(round(y1_d, 3))
        x2_d_string = str(round(x2_d, 3))
        y2_d_string = str(round(y2_d, 3))
        x3_d_string = str(round(x3_d, 3))
        y3_d_string = str(round(y3_d, 3))
        x4_d_string = str(round(x4_d, 3))
        y4_d_string = str(round(y4_d, 3))
        x5_d_string = str(round(x5_d, 3))
        y5_d_string = str(round(y5_d, 3))
        x6_d_string = str(round(x6_d, 3))
        y6_d_string = str(round(y6_d, 3))
        x7_d_string = str(round(x7_d, 3))
        y7_d_string = str(round(y7_d, 3))
        x8_d_string = str(round(x8_d, 3))
        y8_d_string = str(round(y8_d, 3))
        x9_d_string = str(round(x9_d, 3))
        y9_d_string = str(round(y9_d, 3))
        x10_d_string = str(round(x10_d, 3))
        y10_d_string = str(round(y10_d, 3))
        x11_d_string = str(round(x11_d, 3))
        y11_d_string = str(round(y11_d, 3))
        x12_d_string = str(round(x12_d, 3))
        y12_d_string = str(round(y12_d, 3))
        x13_d_string = str(round(x13_d, 3))
        y13_d_string = str(round(y13_d, 3))
        x14_d_string = str(round(x14_d, 3))
        y14_d_string = str(round(y14_d, 3))
        x15_d_string = str(round(x15_d, 3))
        y15_d_string = str(round(y15_d, 3))
        x16_d_string = str(round(x16_d, 3))
        y16_d_string = str(round(y16_d, 3))
        x17_d_string = str(round(x17_d, 3))
        y17_d_string = str(round(y17_d, 3))
        x18_d_string = str(round(x18_d, 3))
        y18_d_string = str(round(y18_d, 3))
        x19_d_string = str(round(x19_d, 3))
        y19_d_string = str(round(y19_d, 3))
        x20_d_string = str(round(x20_d, 3))
        y20_d_string = str(round(y20_d, 3))
        x21_d_string = str(round(x21_d, 3))
        y21_d_string = str(round(y21_d, 3))
        x22_d_string = str(round(x22_d, 3))
        y22_d_string = str(round(y22_d, 3))
        x23_d_string = str(round(x23_d, 3))
        y23_d_string = str(round(y23_d, 3))
        x24_d_string = str(round(x24_d, 3))
        y24_d_string = str(round(y24_d, 3))
        x25_d_string = str(round(x25_d, 3))
        y25_d_string = str(round(y25_d, 3))
        x26_d_string = str(round(x26_d, 3))
        y26_d_string = str(round(y26_d, 3))
        x27_d_string = str(round(x27_d, 3))
        y27_d_string = str(round(y27_d, 3))
        x28_d_string = str(round(x28_d, 3))
        y28_d_string = str(round(y28_d, 3))
        x29_d_string = str(round(x29_d, 3))
        y29_d_string = str(round(y29_d, 3))
        x30_d_string = str(round(x30_d, 3))
        y30_d_string = str(round(y30_d, 3))
        x31_d_string = str(round(x31_d, 3))
        y31_d_string = str(round(y31_d, 3))
        x32_d_string = str(round(x32_d, 3))
        y32_d_string = str(round(y32_d, 3))
        x33_d_string = str(round(x33_d, 3))
        y33_d_string = str(round(y33_d, 3))
        x34_d_string = str(round(x34_d, 3))
        y34_d_string = str(round(y34_d, 3))
        x35_d_string = str(round(x35_d, 3))
        y35_d_string = str(round(y35_d, 3))
        x36_d_string = str(round(x36_d, 3))
        y36_d_string = str(round(y36_d, 3))
        x37_d_string = str(round(x37_d, 3))
        y37_d_string = str(round(y37_d, 3))
        x38_d_string = str(round(x38_d, 3))
        y38_d_string = str(round(y38_d, 3))
        x39_d_string = str(round(x39_d, 3))
        y39_d_string = str(round(y39_d, 3))
        x40_d_string = str(round(x40_d, 3))
        y40_d_string = str(round(y40_d, 3))
        x41_d_string = str(round(x41_d, 3))
        y41_d_string = str(round(y41_d, 3))
        x42_d_string = str(round(x42_d, 3))
        y42_d_string = str(round(y42_d, 3))
        x43_d_string = str(round(x43_d, 3))
        y43_d_string = str(round(y43_d, 3))
        x44_d_string = str(round(x44_d, 3))
        y44_d_string = str(round(y44_d, 3))
        x45_d_string = str(round(x45_d, 3))
        y45_d_string = str(round(y45_d, 3))
        x46_d_string = str(round(x46_d, 3))
        y46_d_string = str(round(y46_d, 3))
        x47_d_string = str(round(x47_d, 3))
        y47_d_string = str(round(y47_d, 3))
        x48_d_string = str(round(x48_d, 3))
        y48_d_string = str(round(y48_d, 3))
        r1_d_string = str(round(r1_d, 3))
        x49_d_string = str(round(x49_d, 3))
        y49_d_string = str(round(y49_d, 3))
        x50_d_string = str(round(x50_d, 3))
        y50_d_string = str(round(y50_d, 3))
        x51_d_string = str(round(x51_d, 3))
        y51_d_string = str(round(y51_d, 3))
        x52_d_string = str(round(x52_d, 3))
        y52_d_string = str(round(y52_d, 3))
        r2_d_string = str(round(r2_d, 3))
        x53_d_string = str(round(x53_d, 3))
        y53_d_string = str(round(y53_d, 3))
        x54_d_string = str(round(x54_d, 3))
        y54_d_string = str(round(y54_d, 3))
        x55_d_string = str(round(x55_d, 3))
        y55_d_string = str(round(y55_d, 3))
        x56_d_string = str(round(x56_d, 3))
        y56_d_string = str(round(y56_d, 3))
        x57_d_string = str(round(x57_d, 3))
        y57_d_string = str(round(y57_d, 3))
        x58_d_string = str(round(x58_d, 3))
        y58_d_string = str(round(y58_d, 3))
        x59_d_string = str(round(x59_d, 3))
        y59_d_string = str(round(y59_d, 3))
        x60_d_string = str(round(x60_d, 3))
        y60_d_string = str(round(y60_d, 3))
        x61_d_string = str(round(x61_d, 3))
        y61_d_string = str(round(y61_d, 3))
        x62_d_string = str(round(x62_d, 3))
        y62_d_string = str(round(y62_d, 3))
        x63_d_string = str(round(x63_d, 3))
        y63_d_string = str(round(y63_d, 3))
        x64_d_string = str(round(x64_d, 3))
        y64_d_string = str(round(y64_d, 3))
        x65_d_string = str(round(x65_d, 3))
        y65_d_string = str(round(y65_d, 3))
        x66_d_string = str(round(x66_d, 3))
        y66_d_string = str(round(y66_d, 3))
        x67_d_string = str(round(x67_d, 3))
        y67_d_string = str(round(y67_d, 3))
        x68_d_string = str(round(x68_d, 3))
        y68_d_string = str(round(y68_d, 3))
        x69_d_string = str(round(x69_d, 3))
        y69_d_string = str(round(y69_d, 3))
        x70_d_string = str(round(x70_d, 3))
        y70_d_string = str(round(y70_d, 3))
        x71_d_string = str(round(x71_d, 3))
        y71_d_string = str(round(y71_d, 3))
        x72_d_string = str(round(x72_d, 3))
        y72_d_string = str(round(y72_d, 3))
        x73_d_string = str(round(x73_d, 3))
        y73_d_string = str(round(y73_d, 3))
        x74_d_string = str(round(x74_d, 3))
        y74_d_string = str(round(y74_d, 3))
        x75_d_string = str(round(x75_d, 3))
        y75_d_string = str(round(y75_d, 3))
        x76_d_string = str(round(x76_d, 3))
        y76_d_string = str(round(y76_d, 3))
        x77_d_string = str(round(x77_d, 3))
        y77_d_string = str(round(y77_d, 3))
        x78_d_string = str(round(x78_d, 3))
        y78_d_string = str(round(y78_d, 3))
        x79_d_string = str(round(x79_d, 3))
        y79_d_string = str(round(y79_d, 3))
        x80_d_string = str(round(x80_d, 3))
        y80_d_string = str(round(y80_d, 3))
        x81_d_string = str(round(x81_d, 3))
        y81_d_string = str(round(y81_d, 3))
        x82_d_string = str(round(x82_d, 3))
        y82_d_string = str(round(y82_d, 3))
        x83_d_string = str(round(x83_d, 3))
        y83_d_string = str(round(y83_d, 3))
        x84_d_string = str(round(x84_d, 3))
        y84_d_string = str(round(y84_d, 3))
        x85_d_string = str(round(x85_d, 3))
        y85_d_string = str(round(y85_d, 3))
        x86_d_string = str(round(x86_d, 3))
        y86_d_string = str(round(y86_d, 3))
        x87_d_string = str(round(x87_d, 3))
        y87_d_string = str(round(y87_d, 3))
        x88_d_string = str(round(x88_d, 3))
        y88_d_string = str(round(y88_d, 3))
        x89_d_string = str(round(x89_d, 3))
        y89_d_string = str(round(y89_d, 3))
        x90_d_string = str(round(x90_d, 3))
        y90_d_string = str(round(y90_d, 3))
        x91_d_string = str(round(x91_d, 3))
        y91_d_string = str(round(y91_d, 3))
        x92_d_string = str(round(x92_d, 3))
        y92_d_string = str(round(y92_d, 3))
        x93_d_string = str(round(x93_d, 3))
        y93_d_string = str(round(y93_d, 3))
        x94_d_string = str(round(x94_d, 3))
        y94_d_string = str(round(y94_d, 3))
        x95_d_string = str(round(x95_d, 3))
        y95_d_string = str(round(y95_d, 3))
        x96_d_string = str(round(x96_d, 3))
        y96_d_string = str(round(y96_d, 3))
        x97_d_string = str(round(x97_d, 3))
        y97_d_string = str(round(y97_d, 3))
        x98_d_string = str(round(x98_d, 3))
        y98_d_string = str(round(y98_d, 3))
        x99_d_string = str(round(x99_d, 3))
        y99_d_string = str(round(y99_d, 3))
        x100_d_string = str(round(x100_d, 3))
        y100_d_string = str(round(y100_d, 3))
        x101_d_string = str(round(x101_d, 3))
        y101_d_string = str(round(y101_d, 3))
        x102_d_string = str(round(x102_d, 3))
        y102_d_string = str(round(y102_d, 3))
        x103_d_string = str(round(x103_d, 3))
        y103_d_string = str(round(y103_d, 3))
        x104_d_string = str(round(x104_d, 3))
        y104_d_string = str(round(y104_d, 3))
        x105_d_string = str(round(x105_d, 3))
        y105_d_string = str(round(y105_d, 3))
        x106_d_string = str(round(x106_d, 3))
        y106_d_string = str(round(y106_d, 3))
        x107_d_string = str(round(x107_d, 3))
        y107_d_string = str(round(y107_d, 3))
        x108_d_string = str(round(x108_d, 3))
        y108_d_string = str(round(y108_d, 3))
        x109_d_string = str(round(x109_d, 3))
        y109_d_string = str(round(y109_d, 3))
        x110_d_string = str(round(x110_d, 3))
        y110_d_string = str(round(y110_d, 3))
        x111_d_string = str(round(x111_d, 3))
        y111_d_string = str(round(y111_d, 3))
        x112_d_string = str(round(x112_d, 3))
        y112_d_string = str(round(y112_d, 3))
        x113_d_string = str(round(x113_d, 3))
        y113_d_string = str(round(y113_d, 3))
        x114_d_string = str(round(x114_d, 3))
        y114_d_string = str(round(y114_d, 3))
        x115_d_string = str(round(x115_d, 3))
        y115_d_string = str(round(y115_d, 3))
        x116_d_string = str(round(x116_d, 3))
        y116_d_string = str(round(y116_d, 3))
        x117_d_string = str(round(x117_d, 3))
        y117_d_string = str(round(y117_d, 3))
        x118_d_string = str(round(x118_d, 3))
        y118_d_string = str(round(y118_d, 3))
        x119_d_string = str(round(x119_d, 3))
        y119_d_string = str(round(y119_d, 3))
        x120_d_string = str(round(x120_d, 3))
        y120_d_string = str(round(y120_d, 3))
        x121_d_string = str(round(x121_d, 3))
        y121_d_string = str(round(y121_d, 3))
        x122_d_string = str(round(x122_d, 3))
        y122_d_string = str(round(y122_d, 3))
        x123_d_string = str(round(x123_d, 3))
        y123_d_string = str(round(y123_d, 3))
        x124_d_string = str(round(x124_d, 3))
        y124_d_string = str(round(y124_d, 3))
        x125_d_string = str(round(x125_d, 3))
        y125_d_string = str(round(y125_d, 3))
        x126_d_string = str(round(x126_d, 3))
        y126_d_string = str(round(y126_d, 3))
        x127_d_string = str(round(x127_d, 3))
        y127_d_string = str(round(y127_d, 3))
        x128_d_string = str(round(x128_d, 3))
        y128_d_string = str(round(y128_d, 3))
        x129_d_string = str(round(x129_d, 3))
        y129_d_string = str(round(y129_d, 3))
        x130_d_string = str(round(x130_d, 3))
        y130_d_string = str(round(y130_d, 3))
        x131_d_string = str(round(x131_d, 3))
        y131_d_string = str(round(y131_d, 3))
        x132_d_string = str(round(x132_d, 3))
        y132_d_string = str(round(y132_d, 3))
        x133_d_string = str(round(x133_d, 3))
        y133_d_string = str(round(y133_d, 3))
        x134_d_string = str(round(x134_d, 3))
        y134_d_string = str(round(y134_d, 3))
        x135_d_string = str(round(x135_d, 3))
        y135_d_string = str(round(y135_d, 3))
        x136_d_string = str(round(x136_d, 3))
        y136_d_string = str(round(y136_d, 3))
        x137_d_string = str(round(x137_d, 3))
        y137_d_string = str(round(y137_d, 3))
        x138_d_string = str(round(x138_d, 3))
        y138_d_string = str(round(y138_d, 3))
        x139_d_string = str(round(x139_d, 3))
        y139_d_string = str(round(y139_d, 3))
        x140_d_string = str(round(x140_d, 3))
        y140_d_string = str(round(y140_d, 3))
        x141_d_string = str(round(x141_d, 3))
        y141_d_string = str(round(y141_d, 3))
        x142_d_string = str(round(x142_d, 3))
        y142_d_string = str(round(y142_d, 3))
        x143_d_string = str(round(x143_d, 3))
        y143_d_string = str(round(y143_d, 3))
        x144_d_string = str(round(x144_d, 3))
        y144_d_string = str(round(y144_d, 3))
        x145_d_string = str(round(x145_d, 3))
        y145_d_string = str(round(y145_d, 3))
        x146_d_string = str(round(x146_d, 3))
        y146_d_string = str(round(y146_d, 3))
        x147_d_string = str(round(x147_d, 3))
        y147_d_string = str(round(y147_d, 3))
        x148_d_string = str(round(x148_d, 3))
        y148_d_string = str(round(y148_d, 3))
        x149_d_string = str(round(x149_d, 3))
        y149_d_string = str(round(y149_d, 3))
        x150_d_string = str(round(x150_d, 3))
        y150_d_string = str(round(y150_d, 3))
        x151_d_string = str(round(x151_d, 3))
        y151_d_string = str(round(y151_d, 3))
        x152_d_string = str(round(x152_d, 3))
        y152_d_string = str(round(y152_d, 3))
        x153_d_string = str(round(x153_d, 3))
        y153_d_string = str(round(y153_d, 3))
        x154_d_string = str(round(x154_d, 3))
        y154_d_string = str(round(y154_d, 3))
        x155_d_string = str(round(x155_d, 3))
        y155_d_string = str(round(y155_d, 3))
        x156_d_string = str(round(x156_d, 3))
        y156_d_string = str(round(y156_d, 3))
        x157_d_string = str(round(x157_d, 3))
        y157_d_string = str(round(y157_d, 3))
        x157_1_d_string = str(round(x157_1_d, 3))
        y157_1_d_string = str(round(y157_1_d, 3))
        x158_d_string = str(round(x158_d, 3))
        y158_d_string = str(round(y158_d, 3))
        x159_d_string = str(round(x159_d, 3))
        y159_d_string = str(round(y159_d, 3))
        x160_d_string = str(round(x160_d, 3))
        y160_d_string = str(round(y160_d, 3))
        x161_d_string = str(round(x161_d, 3))
        y161_d_string = str(round(y161_d, 3))
        x162_d_string = str(round(x162_d, 3))
        y162_d_string = str(round(y162_d, 3))
        x163_d_string = str(round(x163_d, 3))
        y163_d_string = str(round(y163_d, 3))
        x164_d_string = str(round(x164_d, 3))
        y164_d_string = str(round(y164_d, 3))
        x164_1_d_string = str(round(x164_1_d, 3))
        y164_1_d_string = str(round(y164_1_d, 3))
        x165_d_string = str(round(x165_d, 3))
        y165_d_string = str(round(y165_d, 3))
        x166_d_string = str(round(x166_d, 3))
        y166_d_string = str(round(y166_d, 3))
        x167_d_string = str(round(x167_d, 3))
        y167_d_string = str(round(y167_d, 3))
        x168_d_string = str(round(x168_d, 3))
        y168_d_string = str(round(y168_d, 3))
        x169_d_string = str(round(x169_d, 3))
        y169_d_string = str(round(y169_d, 3))
        x170_d_string = str(round(x170_d, 3))
        y170_d_string = str(round(y170_d, 3))
        x171_d_string = str(round(x171_d, 3))
        y171_d_string = str(round(y171_d, 3))
        x172_d_string = str(round(x172_d, 3))
        y172_d_string = str(round(y172_d, 3))
        x173_d_string = str(round(x173_d, 3))
        y173_d_string = str(round(y173_d, 3))
        x174_d_string = str(round(x174_d, 3))
        y174_d_string = str(round(y174_d, 3))
        x175_d_string = str(round(x175_d, 3))
        y175_d_string = str(round(y175_d, 3))
        x176_d_string = str(round(x176_d, 3))
        y176_d_string = str(round(y176_d, 3))
        x177_d_string = str(round(x177_d, 3))
        y177_d_string = str(round(y177_d, 3))
        x178_d_string = str(round(x178_d, 3))
        y178_d_string = str(round(y178_d, 3))
        x179_d_string = str(round(x179_d, 3))
        y179_d_string = str(round(y179_d, 3))
        x180_d_string = str(round(x180_d, 3))
        y180_d_string = str(round(y180_d, 3))
        x181_d_string = str(round(x181_d, 3))
        y181_d_string = str(round(y181_d, 3))
        x182_d_string = str(round(x182_d, 3))
        y182_d_string = str(round(y182_d, 3))
        x183_d_string = str(round(x183_d, 3))
        y183_d_string = str(round(y183_d, 3))
        x184_d_string = str(round(x184_d, 3))
        y184_d_string = str(round(y184_d, 3))
        x185_d_string = str(round(x185_d, 3))
        y185_d_string = str(round(y185_d, 3))
        x186_d_string = str(round(x186_d, 3))
        y186_d_string = str(round(y186_d, 3))
        x187_d_string = str(round(x187_d, 3))
        y187_d_string = str(round(y187_d, 3))
        x188_d_string = str(round(x188_d, 3))
        y188_d_string = str(round(y188_d, 3))
        x189_d_string = str(round(x189_d, 3))
        y189_d_string = str(round(y189_d, 3))
        x190_d_string = str(round(x190_d, 3))
        y190_d_string = str(round(y190_d, 3))
        x191_d_string = str(round(x191_d, 3))
        y191_d_string = str(round(y191_d, 3))
        x192_d_string = str(round(x192_d, 3))
        y192_d_string = str(round(y192_d, 3))
        x193_d_string = str(round(x193_d, 3))
        y193_d_string = str(round(y193_d, 3))
        x194_d_string = str(round(x194_d, 3))
        y194_d_string = str(round(y194_d, 3))
        x195_d_string = str(round(x195_d, 3))
        y195_d_string = str(round(y195_d, 3))
        x196_d_string = str(round(x196_d, 3))
        y196_d_string = str(round(y196_d, 3))
        x197_d_string = str(round(x197_d, 3))
        y197_d_string = str(round(y197_d, 3))
        x198_d_string = str(round(x198_d, 3))
        y198_d_string = str(round(y198_d, 3))
        x199_d_string = str(round(x199_d, 3))
        y199_d_string = str(round(y199_d, 3))
        x200_d_string = str(round(x200_d, 3))
        y200_d_string = str(round(y200_d, 3))
        x201_d_string = str(round(x201_d, 3))
        y201_d_string = str(round(y201_d, 3))
        x202_d_string = str(round(x202_d, 3))
        y202_d_string = str(round(y202_d, 3))
        x209_d_string = str(round(x209_d, 3))
        y209_d_string = str(round(y209_d, 3))
        x210_d_string = str(round(x210_d, 3))
        y210_d_string = str(round(y210_d, 3))
        x211_d_string = str(round(x211_d, 3))
        y211_d_string = str(round(y211_d, 3))
        x212_d_string = str(round(x212_d, 3))
        y212_d_string = str(round(y212_d, 3))
        x213_d_string = str(round(x213_d, 3))
        y213_d_string = str(round(y213_d, 3))
        x214_d_string = str(round(x214_d, 3))
        y214_d_string = str(round(y214_d, 3))
        x215_d_string = str(round(x215_d, 3))
        y215_d_string = str(round(y215_d, 3))
        x216_d_string = str(round(x216_d, 3))
        y216_d_string = str(round(y216_d, 3))
        x217_d_string = str(round(x217_d, 3))
        y217_d_string = str(round(y217_d, 3))
        x218_d_string = str(round(x218_d, 3))
        y218_d_string = str(round(y218_d, 3))
        x219_d_string = str(round(x219_d, 3))
        y219_d_string = str(round(y219_d, 3))
        x220_d_string = str(round(x220_d, 3))
        y220_d_string = str(round(y220_d, 3))
        x221_d_string = str(round(x221_d, 3))
        y221_d_string = str(round(y221_d, 3))
        x222_d_string = str(round(x222_d, 3))
        y222_d_string = str(round(y222_d, 3))
        x223_d_string = str(round(x223_d, 3))
        y223_d_string = str(round(y223_d, 3))
        x224_d_string = str(round(x224_d, 3))
        y224_d_string = str(round(y224_d, 3))
        x225_d_string = str(round(x225_d, 3))
        y225_d_string = str(round(y225_d, 3))
        x226_d_string = str(round(x226_d, 3))
        y226_d_string = str(round(y226_d, 3))
        x227_d_string = str(round(x227_d, 3))
        y227_d_string = str(round(y227_d, 3))
        x228_d_string = str(round(x228_d, 3))
        y228_d_string = str(round(y228_d, 3))
        x229_d_string = str(round(x229_d, 3))
        y229_d_string = str(round(y229_d, 3))
        x230_d_string = str(round(x230_d, 3))
        y230_d_string = str(round(y230_d, 3))
        x240_d_string = str(round(x240_d, 3))
        y240_d_string = str(round(y240_d, 3))
        x241_d_string = str(round(x241_d, 3))
        y241_d_string = str(round(y241_d, 3))
        x242_d_string = str(round(x242_d, 3))
        y242_d_string = str(round(y242_d, 3))
        x243_d_string = str(round(x243_d, 3))
        y243_d_string = str(round(y243_d, 3))
        x244_d_string = str(round(x244_d, 3))
        y244_d_string = str(round(y244_d, 3))
        x245_d_string = str(round(x245_d, 3))
        y245_d_string = str(round(y245_d, 3))
        x246_d_string = str(round(x246_d, 3))
        y246_d_string = str(round(y246_d, 3))
        x247_d_string = str(round(x247_d, 3))
        y247_d_string = str(round(y247_d, 3))
        LayoutSolution_file.write('(setq X1 (list '+x1_d_string+' '+y1_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X2 (list '+x2_d_string+' '+y2_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X3 (list '+x3_d_string+' '+y3_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X4 (list '+x4_d_string+' '+y4_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X1 X2 X3 X4 X1 "")'+"\n")
        LayoutSolution_file.write('(setq X5 (list '+x5_d_string+' '+y5_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X6 (list '+x6_d_string+' '+y6_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X7 (list '+x7_d_string+' '+y7_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X8 (list '+x8_d_string+' '+y8_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X5 X6 X7 X8 X5 "")'+"\n")
        LayoutSolution_file.write('(setq X9 (list '+x9_d_string+' '+y9_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X10 (list '+x10_d_string+' '+y10_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X11 (list '+x11_d_string+' '+y11_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X12 (list '+x12_d_string+' '+y12_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X9 X10 X11 X12 X9 "")'+"\n")
        LayoutSolution_file.write('(setq X13 (list '+x13_d_string+' '+y13_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X14 (list '+x14_d_string+' '+y14_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X15 (list '+x15_d_string+' '+y15_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X16 (list '+x16_d_string+' '+y16_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X13 X14 X15 X16 X13 "")'+"\n")
        LayoutSolution_file.write('(setq X17 (list '+x17_d_string+' '+y17_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X18 (list '+x18_d_string+' '+y18_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X17 X18 "")'+"\n")
        LayoutSolution_file.write('(setq X19 (list '+x19_d_string+' '+y19_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X20 (list '+x20_d_string+' '+y20_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X19 X20 "")'+"\n")
        LayoutSolution_file.write('(setq X21 (list '+x21_d_string+' '+y21_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X22 (list '+x22_d_string+' '+y22_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X23 (list '+x23_d_string+' '+y23_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X24 (list '+x24_d_string+' '+y24_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X21 X22 X23 X24 X21 "")'+"\n")
        LayoutSolution_file.write('(setq X25 (list '+x25_d_string+' '+y25_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X26 (list '+x26_d_string+' '+y26_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X25 X26 "")'+"\n")
        LayoutSolution_file.write('(setq X27 (list '+x27_d_string+' '+y27_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X28 (list '+x28_d_string+' '+y28_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X27 X28 "")'+"\n")
        LayoutSolution_file.write('(setq X29 (list '+x29_d_string+' '+y29_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X30 (list '+x30_d_string+' '+y30_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X31 (list '+x31_d_string+' '+y31_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X32 (list '+x32_d_string+' '+y32_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X29 X30 X31 X32 X29 "")'+"\n")
        LayoutSolution_file.write('(setq X33 (list '+x33_d_string+' '+y33_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X34 (list '+x34_d_string+' '+y34_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X33 X34 "")'+"\n")
        LayoutSolution_file.write('(setq X35 (list '+x35_d_string+' '+y35_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X36 (list '+x36_d_string+' '+y36_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X35 X36 "")'+"\n")
        LayoutSolution_file.write('(setq X37 (list '+x37_d_string+' '+y37_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X38 (list '+x38_d_string+' '+y38_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X39 (list '+x39_d_string+' '+y39_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X40 (list '+x40_d_string+' '+y40_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X37 X38 X39 X40 X37 "")'+"\n")
        LayoutSolution_file.write('(setq X41 (list '+x41_d_string+' '+y41_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X42 (list '+x42_d_string+' '+y42_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X41 X42 "")'+"\n")
        LayoutSolution_file.write('(setq X43 (list '+x43_d_string+' '+y43_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X44 (list '+x44_d_string+' '+y44_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X43 X44 "")'+"\n")
        LayoutSolution_file.write('(setq X45 (list '+x45_d_string+' '+y45_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "CIRCLE" X45 '+r1_d_string+')'+"\n")
        LayoutSolution_file.write('(setq X46 (list '+x46_d_string+' '+y46_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "CIRCLE" X46 '+r1_d_string+')'+"\n")
        LayoutSolution_file.write('(setq X47 (list '+x47_d_string+' '+y47_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "CIRCLE" X47 '+r1_d_string+')'+"\n")
        LayoutSolution_file.write('(setq X48 (list '+x48_d_string+' '+y48_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "CIRCLE" X48 '+r1_d_string+')'+"\n")
        LayoutSolution_file.write('(setq X49 (list '+x49_d_string+' '+y49_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "CIRCLE" X49 '+r2_d_string+')'+"\n")
        LayoutSolution_file.write('(setq X50 (list '+x50_d_string+' '+y50_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "CIRCLE" X50 '+r2_d_string+')'+"\n")
        LayoutSolution_file.write('(setq X51 (list '+x51_d_string+' '+y51_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "CIRCLE" X51 '+r2_d_string+')'+"\n")
        LayoutSolution_file.write('(setq X52 (list '+x52_d_string+' '+y52_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "CIRCLE" X52 '+r2_d_string+')'+"\n")
        LayoutSolution_file.write('(setq X53 (list '+x53_d_string+' '+y53_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X54 (list '+x54_d_string+' '+y54_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X69 (list '+x69_d_string+' '+y69_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X53 X54 X69 "")'+"\n")
        LayoutSolution_file.write('(setq X55 (list '+x55_d_string+' '+y55_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X56 (list '+x56_d_string+' '+y56_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X70 (list '+x70_d_string+' '+y70_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X55 X56 X70 "")'+"\n")
        LayoutSolution_file.write('(setq X57 (list '+x57_d_string+' '+y57_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X58 (list '+x58_d_string+' '+y58_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X71 (list '+x71_d_string+' '+y71_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X57 X58 X71 "")'+"\n")
        LayoutSolution_file.write('(setq X59 (list '+x59_d_string+' '+y59_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X60 (list '+x60_d_string+' '+y60_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X72 (list '+x72_d_string+' '+y72_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X59 X60 X72 "")'+"\n")
        LayoutSolution_file.write('(setq X61 (list '+x61_d_string+' '+y61_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X62 (list '+x62_d_string+' '+y62_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X73 (list '+x73_d_string+' '+y73_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X61 X62 X73 "")'+"\n")
        LayoutSolution_file.write('(setq X63 (list '+x63_d_string+' '+y63_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X64 (list '+x64_d_string+' '+y64_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X74 (list '+x74_d_string+' '+y74_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X63 X64 X74 "")'+"\n")
        LayoutSolution_file.write('(setq X65 (list '+x65_d_string+' '+y65_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X66 (list '+x66_d_string+' '+y66_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X75 (list '+x75_d_string+' '+y75_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X65 X66 X75 "")'+"\n")
        LayoutSolution_file.write('(setq X67 (list '+x67_d_string+' '+y67_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X68 (list '+x68_d_string+' '+y68_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X76 (list '+x76_d_string+' '+y76_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X67 X68 X76 "")'+"\n")
        LayoutSolution_file.write('(setq X77 (list '+x77_d_string+' '+y77_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X78 (list '+x78_d_string+' '+y78_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X79 (list '+x79_d_string+' '+y79_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X80 (list '+x80_d_string+' '+y80_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X69 X77 X78 X79 X80 X71 "")'+"\n")
        LayoutSolution_file.write('(setq X81 (list '+x81_d_string+' '+y81_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X82 (list '+x82_d_string+' '+y82_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X70 X81 X82 X73 "")'+"\n")
        LayoutSolution_file.write('(setq X83 (list '+x83_d_string+' '+y83_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X84 (list '+x84_d_string+' '+y84_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X72 X83 X84 X75 "")'+"\n")
        LayoutSolution_file.write('(setq X85 (list '+x85_d_string+' '+y85_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X86 (list '+x86_d_string+' '+y86_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X87 (list '+x87_d_string+' '+y87_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X88 (list '+x88_d_string+' '+y88_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X74 X85 X86 X87 X88 X76 "")'+"\n")
        LayoutSolution_file.write('(setq X89 (list '+x89_d_string+' '+y89_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X90 (list '+x90_d_string+' '+y90_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X54 X90 X89 X69 "")'+"\n")
        LayoutSolution_file.write('(setq X91 (list '+x91_d_string+' '+y91_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X92 (list '+x92_d_string+' '+y92_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X58 X92 X91 X71 "")'+"\n")
        LayoutSolution_file.write('(setq X93 (list '+x93_d_string+' '+y93_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X94 (list '+x94_d_string+' '+y94_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X56 X93 X94 X70 "")'+"\n")
        LayoutSolution_file.write('(setq X95 (list '+x95_d_string+' '+y95_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X96 (list '+x96_d_string+' '+y96_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X60 X95 X96 X72 "")'+"\n")
        LayoutSolution_file.write('(setq X97 (list '+x97_d_string+' '+y97_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X98 (list '+x98_d_string+' '+y98_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X73 X97 X98 X62 "")'+"\n")
        LayoutSolution_file.write('(setq X99 (list '+x99_d_string+' '+y99_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X100 (list '+x100_d_string+' '+y100_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X75 X99 X100 X66 "")'+"\n")
        LayoutSolution_file.write('(setq X101 (list '+x101_d_string+' '+y101_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X102 (list '+x102_d_string+' '+y102_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X64 X101 X102 X74 "")'+"\n")
        LayoutSolution_file.write('(setq X103 (list '+x103_d_string+' '+y103_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X104 (list '+x104_d_string+' '+y104_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X68 X103 X104 X76 "")'+"\n")
        LayoutSolution_file.write('(setq X105 (list '+x105_d_string+' '+y105_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X106 (list '+x106_d_string+' '+y106_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X107 (list '+x107_d_string+' '+y107_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X108 (list '+x108_d_string+' '+y108_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X91 X105 X106 X107 X108 X96 "")'+"\n")
        LayoutSolution_file.write('(setq X109 (list '+x109_d_string+' '+y109_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X110 (list '+x110_d_string+' '+y110_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X111 (list '+x111_d_string+' '+y111_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X109 X110 X111 "")'+"\n")
        LayoutSolution_file.write('(setq X112 (list '+x112_d_string+' '+y112_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X113 (list '+x113_d_string+' '+y113_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X114 (list '+x114_d_string+' '+y114_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X112 X113 X114 "")'+"\n")
        LayoutSolution_file.write('(setq X115 (list '+x115_d_string+' '+y115_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X116 (list '+x116_d_string+' '+y116_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X117 (list '+x117_d_string+' '+y117_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X118 (list '+x118_d_string+' '+y118_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X115 X116 X117 X118 "")'+"\n")
        LayoutSolution_file.write('(setq X119 (list '+x119_d_string+' '+y119_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X120 (list '+x120_d_string+' '+y120_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X121 (list '+x121_d_string+' '+y121_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X122 (list '+x122_d_string+' '+y122_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X89 X119 X120 X121 X122 "")'+"\n")
        LayoutSolution_file.write('(setq X123 (list '+x123_d_string+' '+y123_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X124 (list '+x124_d_string+' '+y124_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X125 (list '+x125_d_string+' '+y125_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X126 (list '+x126_d_string+' '+y126_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X123 X124 X125 X126 X94 "")'+"\n")
        LayoutSolution_file.write('(setq X127 (list '+x127_d_string+' '+y127_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X128 (list '+x128_d_string+' '+y128_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X129 (list '+x129_d_string+' '+y129_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X130 (list '+x130_d_string+' '+y130_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X127 X128 X129 X130 "")'+"\n")
        LayoutSolution_file.write('(setq X131 (list '+x131_d_string+' '+y131_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X132 (list '+x132_d_string+' '+y132_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X133 (list '+x133_d_string+' '+y133_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X134 (list '+x134_d_string+' '+y134_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X131 X132 X133 X134 "")'+"\n")
        LayoutSolution_file.write('(setq X135 (list '+x135_d_string+' '+y135_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X136 (list '+x136_d_string+' '+y136_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X137 (list '+x137_d_string+' '+y137_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X129 X135 X136 X137 "")'+"\n")
        LayoutSolution_file.write('(setq X138 (list '+x138_d_string+' '+y138_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X139 (list '+x139_d_string+' '+y139_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X140 (list '+x140_d_string+' '+y140_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X138 X139 X140 X132 "")'+"\n")
        LayoutSolution_file.write('(setq X141 (list '+x141_d_string+' '+y141_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X142 (list '+x142_d_string+' '+y142_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X143 (list '+x143_d_string+' '+y143_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X141 X142 X143 "")'+"\n")
        LayoutSolution_file.write('(setq X144 (list '+x144_d_string+' '+y144_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X145 (list '+x145_d_string+' '+y145_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X146 (list '+x146_d_string+' '+y146_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X144 X145 X146 "")'+"\n")
        LayoutSolution_file.write('(command "LINE" X121 X136 "")'+"\n")
        LayoutSolution_file.write('(command "LINE" X124 X139 "")'+"\n")
        LayoutSolution_file.write('(setq X147 (list '+x147_d_string+' '+y147_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X148 (list '+x148_d_string+' '+y148_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X149 (list '+x149_d_string+' '+y149_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X150 (list '+x150_d_string+' '+y150_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X99 X147 X148 X149 X150 "")'+"\n")
        LayoutSolution_file.write('(setq X151 (list '+x151_d_string+' '+y151_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X152 (list '+x152_d_string+' '+y152_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X153 (list '+x153_d_string+' '+y153_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X154 (list '+x154_d_string+' '+y154_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X151 X152 X153 X154 X104 "")'+"\n")
        LayoutSolution_file.write('(setq X155 (list '+x155_d_string+' '+y155_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X156 (list '+x156_d_string+' '+y156_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X157 (list '+x157_d_string+' '+y157_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X158 (list '+x158_d_string+' '+y158_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X159 (list '+x159_d_string+' '+y159_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X160 (list '+x160_d_string+' '+y160_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X155 X156 X157 X158 X159 X160 "")'+"\n")
        LayoutSolution_file.write('(setq X161 (list '+x161_d_string+' '+y161_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X162 (list '+x162_d_string+' '+y162_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X163 (list '+x163_d_string+' '+y163_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X164 (list '+x164_d_string+' '+y164_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X165 (list '+x165_d_string+' '+y165_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X166 (list '+x166_d_string+' '+y166_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X161 X162 X163 X164 X165 X166 "")'+"\n")
        LayoutSolution_file.write('(setq X157_1 (list '+x157_1_d_string+' '+y157_1_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X157 X157_1 "")'+"\n")
        LayoutSolution_file.write('(setq X164_1 (list '+x164_1_d_string+' '+y164_1_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X164 X164_1 "")'+"\n")
        LayoutSolution_file.write('(setq X167 (list '+x167_d_string+' '+y167_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X168 (list '+x168_d_string+' '+y168_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X169 (list '+x169_d_string+' '+y169_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X167 X168 X169 "")'+"\n")
        LayoutSolution_file.write('(setq X170 (list '+x170_d_string+' '+y170_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X171 (list '+x171_d_string+' '+y171_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X172 (list '+x172_d_string+' '+y172_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X170 X171 X172 "")'+"\n")
        LayoutSolution_file.write('(command "LINE" X149 X159 "")'+"\n")
        LayoutSolution_file.write('(command "LINE" X152 X162 "")'+"\n")
        LayoutSolution_file.write('(setq X173 (list '+x173_d_string+' '+y173_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X174 (list '+x174_d_string+' '+y174_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X175 (list '+x175_d_string+' '+y175_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X176 (list '+x176_d_string+' '+y176_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X97 X173 X174 X175 X176 X102 "")'+"\n")
        LayoutSolution_file.write('(setq X177 (list '+x177_d_string+' '+y177_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X178 (list '+x178_d_string+' '+y178_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X179 (list '+x179_d_string+' '+y179_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X177 X178 X179 "")'+"\n")
        LayoutSolution_file.write('(setq X180 (list '+x180_d_string+' '+y180_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X181 (list '+x181_d_string+' '+y181_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X182 (list '+x182_d_string+' '+y182_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X180 X181 X182 "")'+"\n")
        LayoutSolution_file.write('(setq X183 (list '+x183_d_string+' '+y183_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X184 (list '+x184_d_string+' '+y184_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X185 (list '+x185_d_string+' '+y185_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X186 (list '+x186_d_string+' '+y186_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X183 X184 X185 X186 "")'+"\n")
        LayoutSolution_file.write('(setq X187 (list '+x187_d_string+' '+y187_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X188 (list '+x188_d_string+' '+y188_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X187 X188 "")'+"\n")
        LayoutSolution_file.write('(setq X189 (list '+x189_d_string+' '+y189_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X190 (list '+x190_d_string+' '+y190_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X189 X190 "")'+"\n")
        LayoutSolution_file.write('(setq X191 (list '+x191_d_string+' '+y191_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X192 (list '+x192_d_string+' '+y192_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X191 X192 "")'+"\n")
        LayoutSolution_file.write('(setq X193 (list '+x193_d_string+' '+y193_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X194 (list '+x194_d_string+' '+y194_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X193 X194 "")'+"\n")
        LayoutSolution_file.write('(setq X195 (list '+x195_d_string+' '+y195_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X196 (list '+x196_d_string+' '+y196_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X197 (list '+x197_d_string+' '+y197_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X198 (list '+x198_d_string+' '+y198_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X195 X196 X198 X197 X195 "")'+"\n")
        LayoutSolution_file.write('(setq X199 (list '+x199_d_string+' '+y199_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X200 (list '+x200_d_string+' '+y200_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X201 (list '+x201_d_string+' '+y201_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X202 (list '+x202_d_string+' '+y202_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X199 X200 X202 X201 X199 "")'+"\n")
        LayoutSolution_file.write('(setq X203 (list '+x188_d_string+' '+y10_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X204 (list '+x190_d_string+' '+y10_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X205 (list '+x25_d_string+' '+y10_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "TRIM" X203 X204 "" X205 "")'+"\n")
        LayoutSolution_file.write('(setq X206 (list '+x192_d_string+' '+y9_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X207 (list '+x194_d_string+' '+y9_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X208 (list '+x18_d_string+' '+y9_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "TRIM" X206 X207 "" X208 "")'+"\n")
        LayoutSolution_file.write('(setq X209 (list '+x209_d_string+' '+y209_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X210 (list '+x210_d_string+' '+y210_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X209 X210 "")'+"\n")
        LayoutSolution_file.write('(setq X211 (list '+x211_d_string+' '+y211_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X212 (list '+x212_d_string+' '+y212_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X211 X212 "")'+"\n")
        LayoutSolution_file.write('(setq X213 (list '+x213_d_string+' '+y213_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X213 X41 "")'+"\n")
        LayoutSolution_file.write('(setq X214 (list '+x214_d_string+' '+y214_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X214 X44 "")'+"\n")
        LayoutSolution_file.write('(setq X215 (list '+x215_d_string+' '+y215_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X216 (list '+x216_d_string+' '+y216_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X217 (list '+x217_d_string+' '+y217_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X218 (list '+x218_d_string+' '+y218_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X215 X216 X218 X217 X215 "")'+"\n")
        LayoutSolution_file.write('(setq X219 (list '+x219_d_string+' '+y219_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X220 (list '+x220_d_string+' '+y220_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X221 (list '+x221_d_string+' '+y221_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X222 (list '+x222_d_string+' '+y222_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X219 X220 X222 X221 X219 "")'+"\n")
        LayoutSolution_file.write('(setq X223 (list '+x223_d_string+' '+y223_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X224 (list '+x224_d_string+' '+y224_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X225 (list '+x225_d_string+' '+y225_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X226 (list '+x226_d_string+' '+y226_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X223 X224 X226 X225 X223 "")'+"\n")
        LayoutSolution_file.write('(setq X227 (list '+x227_d_string+' '+y227_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X229 (list '+x229_d_string+' '+y229_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X227 X229 "")'+"\n")
        LayoutSolution_file.write('(setq X228 (list '+x228_d_string+' '+y228_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X230 (list '+x230_d_string+' '+y230_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X228 X230 "")'+"\n")
        LayoutSolution_file.write('(setq X231 (list '+x213_d_string+' '+y11_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X232 (list '+x214_d_string+' '+y11_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X233 (list '+x215_d_string+' '+y11_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "TRIM" X231 X232 "" X233 "")'+"\n")
        LayoutSolution_file.write('(setq X234 (list '+x213_d_string+' '+y44_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X235 (list '+x214_d_string+' '+y44_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X236 (list '+x215_d_string+' '+y44_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "TRIM" X234 X235 "" X236 "")'+"\n")
        if y225_d < y12_d:
            LayoutSolution_file.write('(setq X237 (list '+x225_d_string+' '+y12_d_string+'))'+"\n")
            LayoutSolution_file.write('(setq X238 (list '+x226_d_string+' '+y12_d_string+'))'+"\n")
            LayoutSolution_file.write('(setq X239 (list '+x227_d_string+' '+y12_d_string+'))'+"\n")
            LayoutSolution_file.write('(command "TRIM" X237 X238 "" X239 "")'+"\n")
        else:
            LayoutSolution_file.write('(setq X237 (list '+x227_d_string+' '+y12_d_string+'))'+"\n")
            LayoutSolution_file.write('(setq X238 (list '+x228_d_string+' '+y12_d_string+'))'+"\n")
            LayoutSolution_file.write('(setq X239 (list '+x34_d_string+' '+y12_d_string+'))'+"\n")
            LayoutSolution_file.write('(command "TRIM" X237 X238 "" X239 "")'+"\n")
        LayoutSolution_file.write('(setq X240 (list '+x240_d_string+' '+y240_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X241 (list '+x241_d_string+' '+y241_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X240 X241 "")'+"\n")
        LayoutSolution_file.write('(setq X242 (list '+x242_d_string+' '+y242_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X243 (list '+x243_d_string+' '+y243_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X242 X243 "")'+"\n")
        LayoutSolution_file.write('(setq X244 (list '+x244_d_string+' '+y244_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X245 (list '+x245_d_string+' '+y245_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X244 X245 "")'+"\n")
        LayoutSolution_file.write('(setq X246 (list '+x246_d_string+' '+y246_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X247 (list '+x247_d_string+' '+y247_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X246 X247 "")'+"\n")
    #Оформление компановочного решения горизонтального шевронного редуктора
    elif c_type == 0 and g_type == 2:
        k = 2.5*mn
        x1_d = L/2-aw/2-da1/2
        y1_d = W/2-a/2-bw1/2
        x2_d = x1_d
        y2_d = W/2-a/2
        x3_d = x2_d+k
        y3_d = y2_d
        x4_d = x3_d
        y4_d = W/2+a/2
        x5_d = x2_d
        y5_d = y4_d
        x6_d = x5_d
        y6_d = W/2+a/2+bw1/2
        x7_d = L/2-aw/2+da1/2
        y7_d = y6_d
        x8_d = x7_d
        y8_d = y5_d
        x9_d = x8_d-k
        y9_d = y8_d
        x10_d = x9_d
        y10_d = y3_d
        x11_d = x8_d
        y11_d = y10_d
        x12_d = x11_d
        y12_d = y1_d
        x13_d = L/2+aw/2-da2/2
        y13_d = y12_d+1.25
        x14_d = x13_d
        y14_d = y13_d+bw2/2
        x15_d = L/2+aw/2+da2/2
        y15_d = y14_d
        x16_d = x15_d
        y16_d = y13_d
        x17_d = x14_d
        y17_d = y8_d+1.25
        x18_d = x17_d
        y18_d = y17_d+bw2/2
        x19_d = x16_d
        y19_d = y18_d
        x20_d = x19_d
        y20_d = y17_d
        x21_d = x6_d-a_b
        y21_d = y1_d-a_b
        x22_d = x21_d
        y22_d = y6_d+a_b
        x23_d = x20_d+a_b
        y23_d = y22_d
        x24_d = x23_d
        y24_d = y21_d
        x25_d = L/2-aw/2-D_b1/2
        y25_d = y21_d-n_b-B_b1
        x26_d = x25_d
        y26_d = y21_d-n_b
        x27_d = L/2-aw/2+D_b1/2
        y27_d = y26_d
        x28_d = x27_d
        y28_d = y25_d
        x29_d = L/2-aw/2-d_b1/2
        y29_d = y28_d
        x30_d = x29_d
        y30_d = y27_d
        x31_d = L/2-aw/2+d_b1/2
        y31_d = y30_d
        x32_d = x31_d
        y32_d = y29_d
        x33_d = x26_d
        y33_d = y22_d+n_b
        x34_d = x33_d
        y34_d = y33_d+B_b1
        x35_d = x28_d
        y35_d = y34_d
        x36_d = x35_d
        y36_d = y33_d
        x37_d = x30_d
        y37_d = y36_d
        x38_d = x37_d
        y38_d = y35_d
        x39_d = x31_d
        y39_d = y38_d
        x40_d = x39_d
        y40_d = y37_d
        x41_d = L/2+aw/2-D_b2/2
        y41_d = y27_d-B_b1/2-B_b2/2
        x42_d = x41_d
        y42_d = y41_d+B_b2
        x43_d = L/2+aw/2+D_b2/2
        y43_d = y42_d
        x44_d = x43_d
        y44_d = y41_d
        x45_d = L/2+aw/2-d_b2/2
        y45_d = y44_d
        x46_d = x45_d
        y46_d = y43_d
        x47_d = L/2+aw/2+d_b2/2
        y47_d = y46_d
        x48_d = x47_d
        y48_d = y45_d
        x49_d = x42_d
        y49_d = y36_d+B_b1/2-B_b2/2
        x50_d = x49_d
        y50_d = y49_d+B_b2
        x51_d = x43_d
        y51_d = y50_d
        x52_d = x51_d
        y52_d = y49_d
        x53_d = x46_d
        y53_d = y52_d
        x54_d = x53_d
        y54_d = y51_d
        x55_d = x47_d
        y55_d = y54_d
        x56_d = x55_d
        y56_d = y53_d
        x1_d_string = str(round(x1_d, 3))
        y1_d_string = str(y1_d)
        x2_d_string = str(round(x2_d, 3))
        y2_d_string = str(y2_d)
        x3_d_string = str(round(x3_d, 3))
        y3_d_string = str(y3_d)
        x4_d_string = str(round(x4_d, 3))
        y4_d_string = str(y4_d)
        x5_d_string = str(round(x5_d, 3))
        y5_d_string = str(y5_d)
        x6_d_string = str(round(x6_d, 3))
        y6_d_string = str(y6_d)
        x7_d_string = str(round(x7_d, 3))
        y7_d_string = str(y7_d)
        x8_d_string = str(round(x8_d, 3))
        y8_d_string = str(y8_d)
        x9_d_string = str(round(x9_d, 3))
        y9_d_string = str(y9_d)
        x10_d_string = str(round(x10_d, 3))
        y10_d_string = str(y10_d)
        x11_d_string = str(round(x11_d, 3))
        y11_d_string = str(y11_d)
        x12_d_string = str(round(x12_d, 3))
        y12_d_string = str(y12_d)
        x13_d_string = str(round(x13_d, 3))
        y13_d_string = str(y13_d)
        x14_d_string = str(round(x14_d, 3))
        y14_d_string = str(y14_d)
        x15_d_string = str(round(x15_d, 3))
        y15_d_string = str(y15_d)
        x16_d_string = str(round(x16_d, 3))
        y16_d_string = str(y16_d)
        x17_d_string = str(round(x17_d, 3))
        y17_d_string = str(y17_d)
        x18_d_string = str(round(x18_d, 3))
        y18_d_string = str(y18_d)
        x19_d_string = str(round(x19_d, 3))
        y19_d_string = str(y19_d)
        x20_d_string = str(round(x20_d, 3))
        y20_d_string = str(y20_d)
        x21_d_string = str(round(x21_d, 3))
        y21_d_string = str(y21_d)
        x22_d_string = str(round(x22_d, 3))
        y22_d_string = str(y22_d)
        x23_d_string = str(round(x23_d, 3))
        y23_d_string = str(y23_d)
        x24_d_string = str(round(x24_d, 3))
        y24_d_string = str(y24_d)
        x25_d_string = str(round(x25_d, 3))
        y25_d_string = str(y25_d)
        x26_d_string = str(round(x26_d, 3))
        y26_d_string = str(y26_d)
        x27_d_string = str(round(x27_d, 3))
        y27_d_string = str(y27_d)
        x28_d_string = str(round(x28_d, 3))
        y28_d_string = str(y28_d)
        x29_d_string = str(round(x29_d, 3))
        y29_d_string = str(y29_d)
        x30_d_string = str(round(x30_d, 3))
        y30_d_string = str(y30_d)
        x31_d_string = str(round(x31_d, 3))
        y31_d_string = str(y31_d)
        x32_d_string = str(round(x32_d, 3))
        y32_d_string = str(y32_d)
        x33_d_string = str(round(x33_d, 3))
        y33_d_string = str(y33_d)
        x34_d_string = str(round(x34_d, 3))
        y34_d_string = str(y34_d)
        x35_d_string = str(round(x35_d, 3))
        y35_d_string = str(y35_d)
        x36_d_string = str(round(x36_d, 3))
        y36_d_string = str(y36_d)
        x37_d_string = str(round(x37_d, 3))
        y37_d_string = str(y37_d)
        x38_d_string = str(round(x38_d, 3))
        y38_d_string = str(y38_d)
        x39_d_string = str(round(x39_d, 3))
        y39_d_string = str(y39_d)
        x40_d_string = str(round(x40_d, 3))
        y40_d_string = str(y40_d)
        x41_d_string = str(round(x41_d, 3))
        y41_d_string = str(y41_d)
        x42_d_string = str(round(x42_d, 3))
        y42_d_string = str(y42_d)
        x43_d_string = str(round(x43_d, 3))
        y43_d_string = str(y43_d)
        x44_d_string = str(round(x44_d, 3))
        y44_d_string = str(y44_d)
        x45_d_string = str(round(x45_d, 3))
        y45_d_string = str(y45_d)
        x46_d_string = str(round(x46_d, 3))
        y46_d_string = str(y46_d)
        x47_d_string = str(round(x47_d, 3))
        y47_d_string = str(y47_d)
        x48_d_string = str(round(x48_d, 3))
        y48_d_string = str(y48_d)
        x49_d_string = str(round(x49_d, 3))
        y49_d_string = str(y49_d)
        x50_d_string = str(round(x50_d, 3))
        y50_d_string = str(y50_d)
        x51_d_string = str(round(x51_d, 3))
        y51_d_string = str(y51_d)
        x52_d_string = str(round(x52_d, 3))
        y52_d_string = str(y52_d)
        x53_d_string = str(round(x53_d, 3))
        y53_d_string = str(y53_d)
        x54_d_string = str(round(x54_d, 3))
        y54_d_string = str(y54_d)
        x55_d_string = str(round(x55_d, 3))
        y55_d_string = str(y55_d)
        x56_d_string = str(round(x56_d, 3))
        y56_d_string = str(y56_d)
        LayoutSolution_file.write('(setq X1 (list '+x1_d_string+' '+y1_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X2 (list '+x2_d_string+' '+y2_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X3 (list '+x3_d_string+' '+y3_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X4 (list '+x4_d_string+' '+y4_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X5 (list '+x5_d_string+' '+y5_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X6 (list '+x6_d_string+' '+y6_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X7 (list '+x7_d_string+' '+y7_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X8 (list '+x8_d_string+' '+y8_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X9 (list '+x9_d_string+' '+y9_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X10 (list '+x10_d_string+' '+y10_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X11 (list '+x11_d_string+' '+y11_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X12 (list '+x12_d_string+' '+y12_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12 X1 "")'+"\n")
        LayoutSolution_file.write('(setq X13 (list '+x13_d_string+' '+y13_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X14 (list '+x14_d_string+' '+y14_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X15 (list '+x15_d_string+' '+y15_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X16 (list '+x16_d_string+' '+y16_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X13 X14 X15 X16 X13 "")'+"\n")
        LayoutSolution_file.write('(setq X17 (list '+x17_d_string+' '+y17_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X18 (list '+x18_d_string+' '+y18_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X19 (list '+x19_d_string+' '+y19_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X20 (list '+x20_d_string+' '+y20_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X17 X18 X19 X20 X17 "")'+"\n")
        LayoutSolution_file.write('(setq X21 (list '+x21_d_string+' '+y21_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X22 (list '+x22_d_string+' '+y22_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X23 (list '+x23_d_string+' '+y23_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X24 (list '+x24_d_string+' '+y24_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X21 X22 X23 X24 X21 "")'+"\n")
        LayoutSolution_file.write('(setq X25 (list '+x25_d_string+' '+y25_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X26 (list '+x26_d_string+' '+y26_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X27 (list '+x27_d_string+' '+y27_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X28 (list '+x28_d_string+' '+y28_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X25 X26 X27 X28 X25 "")'+"\n")
        LayoutSolution_file.write('(setq X29 (list '+x29_d_string+' '+y29_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X30 (list '+x30_d_string+' '+y30_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X29 X30 "")'+"\n")
        LayoutSolution_file.write('(setq X31 (list '+x31_d_string+' '+y31_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X32 (list '+x32_d_string+' '+y32_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X31 X32 "")'+"\n")
        LayoutSolution_file.write('(setq X33 (list '+x33_d_string+' '+y33_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X34 (list '+x34_d_string+' '+y34_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X35 (list '+x35_d_string+' '+y35_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X36 (list '+x36_d_string+' '+y36_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X33 X34 X35 X36 X33 "")'+"\n")
        LayoutSolution_file.write('(setq X37 (list '+x37_d_string+' '+y37_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X38 (list '+x38_d_string+' '+y38_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X37 X38 "")'+"\n")
        LayoutSolution_file.write('(setq X39 (list '+x39_d_string+' '+y39_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X40 (list '+x40_d_string+' '+y40_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X39 X40 "")'+"\n")
        LayoutSolution_file.write('(setq X41 (list '+x41_d_string+' '+y41_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X42 (list '+x42_d_string+' '+y42_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X43 (list '+x43_d_string+' '+y43_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X44 (list '+x44_d_string+' '+y44_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X41 X42 X43 X44 X41 "")'+"\n")
        LayoutSolution_file.write('(setq X45 (list '+x45_d_string+' '+y45_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X46 (list '+x46_d_string+' '+y46_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X45 X46 "")'+"\n")
        LayoutSolution_file.write('(setq X47 (list '+x47_d_string+' '+y47_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X48 (list '+x48_d_string+' '+y48_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X47 X48 "")'+"\n")
        LayoutSolution_file.write('(setq X49 (list '+x49_d_string+' '+y49_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X50 (list '+x50_d_string+' '+y50_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X51 (list '+x51_d_string+' '+y51_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X52 (list '+x52_d_string+' '+y52_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "PLINE" X49 X50 X51 X52 X49 "")'+"\n")
        LayoutSolution_file.write('(setq X53 (list '+x53_d_string+' '+y53_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X54 (list '+x54_d_string+' '+y54_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X53 X54 "")'+"\n")
        LayoutSolution_file.write('(setq X55 (list '+x55_d_string+' '+y55_d_string+'))'+"\n")
        LayoutSolution_file.write('(setq X56 (list '+x56_d_string+' '+y56_d_string+'))'+"\n")
        LayoutSolution_file.write('(command "LINE" X55 X56 "")'+"\n")
    LayoutSolution_file.close()

#Формирование пояснительной записки
def ExplanatoryNote():
    Po = str(Po_entry.get())
    no = str(no_entry.get())
    sl = str(sl_entry.get())
    c_y = str(c_y_entry.get())
    c_d = str(c_d_entry.get())
    dc = str(dc_entry.get())
    t_mode = float(t_mode_entry.get())
    t_type = float(t_type_entry.get())
    d_type = float(d_type_entry.get())
    scheme = float(scheme_entry.get())
    g_type = float(g_type_entry.get())
    performance1_string = str(performance1)
    performance2_string = str(performance2)
    performance3_string = str(performance3)
    performance4_string = str(performance4)
    performance5_string = str(performance5)
    ur1_string = str(ur1)
    ur2_string = str(ur2)
    ur3_string = str(ur3)
    ExplanatoryNote_file = open('C:/Users/Public/Documents/ExplanatoryNote.txt', 'w')
    #Оформление титульного листа
    ExplanatoryNote_file.write('Министерство образования и науки РФ'+"\n")
    ExplanatoryNote_file.write('«Уральский федеральный университет имени первого Президента России Б. Н. Ельцина»'+"\n")
    ExplanatoryNote_file.write('Кафедра «Детали машин»'+"\n")
    ExplanatoryNote_file.write('Проектирование привода технологического оборудования'+"\n")
    ExplanatoryNote_file.write('Курсовой проект'+"\n")
    ExplanatoryNote_file.write('Пояснительная записка'+"\n")
    ExplanatoryNote_file.write('0000.000000.000 ПЗ'+"\n")
    ExplanatoryNote_file.write('Руководитель'+"\n")
    ExplanatoryNote_file.write('Студент'+"\n")
    ExplanatoryNote_file.write('Группа'+"\n")
    ExplanatoryNote_file.write('Екатеринбург 2019'+"\n")
    ExplanatoryNote_file.write('\n'+"\n")
    #Оформление содержания
    ExplanatoryNote_file.write('СОДЕРЖАНИЕ'+"\n")
    ExplanatoryNote_file.write('ВВЕДЕНИЕ'+"\n")
    ExplanatoryNote_file.write('1. ВЫБОР ДВИГАТЕЛЯ И РАСЧЕТ ОСНОВНЫХ ПАРАМЕТРОВ ПРИВОДА'+"\n")
    ExplanatoryNote_file.write('2. РАСЧЕТ ЗУБЧАТОЙ ПЕРЕДАЧИ'+"\n")
    ExplanatoryNote_file.write('3. РАСЧЕТ РЕМЕННОЙ ПЕРЕДАЧИ'+"\n")
    ExplanatoryNote_file.write('4. ПРОЕКТНЫЙ РАСЧЕТ И КОНСТРУИРОВАНИЕ ВАЛОВ'+"\n")
    ExplanatoryNote_file.write('5. РАСЧЕТ ВАЛА НА УСТАЛОСТНУЮ ПРОЧНОСТЬ'+"\n")
    ExplanatoryNote_file.write('6. РАСЧЕТ ПОДШИПНИКОВ'+"\n")
    ExplanatoryNote_file.write('7. КРЫШКИ ПОДШИПНИКОВ'+"\n")
    ExplanatoryNote_file.write('8. РАСЧЕТ ШПОНОЧНЫХ СОЕДИНЕНИЙ'+"\n")
    ExplanatoryNote_file.write('9. СМАЗКА ЗУБЧАТОГО ЗАЦЕПЛЕНИЯ И ПОДШИПНИКОВ'+"\n")
    ExplanatoryNote_file.write('10. РАСЧЕТ ГЕОМЕТРИЧЕСКИХ ПАРАМЕТРОВ ЗУБЧАТОГО КОЛЕСА'+"\n")
    ExplanatoryNote_file.write('11. РАСЧЕТ ЭЛЕМЕНТОВ КОРПУСА'+"\n")
    ExplanatoryNote_file.write('ЗАКЛЮЧЕНИЕ'+"\n")
    ExplanatoryNote_file.write('СПИСОК ЛИТЕРАТУРЫ'+"\n")
    ExplanatoryNote_file.write('\n'+"\n")
    #Оформление задания на проектирование
    ExplanatoryNote_file.write('Задание на проектирование'+"\n")
    ExplanatoryNote_file.write('Мощность на ведомом валу Р3 = '+Po+' кВт'+"\n")
    ExplanatoryNote_file.write('Частота вращения ведомого вала n3 = '+no+' об/мин'+"\n")
    ExplanatoryNote_file.write('Срок службы передачи Lг= '+sl+' лет'+"\n")
    ExplanatoryNote_file.write('Коэффициент использования передачи в течение года Kг = '+c_y+"\n")
    ExplanatoryNote_file.write('Коэффициент использования передачи в течение суток Kс = '+c_d+"\n")
    ExplanatoryNote_file.write('Продолжительность включения ПВ% = '+dc+' %'+"\n")
    if t_mode == 0:
        ExplanatoryNote_file.write('Режим работы - Постоянный'+"\n")
    elif t_mode == 1:
        ExplanatoryNote_file.write('Режим работы - Тяжелый'+"\n")
    elif t_mode == 2:
        ExplanatoryNote_file.write('Режим работы - Средний равновероятный'+"\n")
    elif t_mode == 3:
        ExplanatoryNote_file.write('Режим работы - Средний нормальный'+"\n")
    elif t_mode == 4:
        ExplanatoryNote_file.write('Режим работы - Легкий'+"\n")
    else:
        ExplanatoryNote_file.write('Режим работы - Особо легкий'+"\n")
    if t_type == 0:
        ExplanatoryNote_file.write('Тип привода – Реверсивный'+"\n")
    else:
        ExplanatoryNote_file.write('Тип привода – Нереверсивный'+"\n")
    ExplanatoryNote_file.write('\n'+"\n")
    #Оформление введения
    ExplanatoryNote_file.write('ВВЕДЕНИЕ'+"\n")
    ExplanatoryNote_file.write('Цель проектирования - спроектировать редуктор под заданные параметры.'+"\n")
    ExplanatoryNote_file.write('Объектом изучения расчетов и проектирования является привод технологического оборудования,'+"\n")
    if d_type == 0:
        ExplanatoryNote_file.write('состоящий из двигателя, ременной передачи и одноступенчатого цилиндрического редуктора.'+"\n")
    else:
        ExplanatoryNote_file.write('состоящий из двигателя, передачи роликовой цепью и одноступенчатого цилиндрического редуктора.'+"\n")
    ExplanatoryNote_file.write('Зубчатые редукторы подобного типа широко используются в приводе различных машин (транспортеры,'+"\n")
    ExplanatoryNote_file.write('металлорежущие станки и т.д.).'+"\n")
    ExplanatoryNote_file.write('Для проектирования редуктора выполнены проектные и проверочные расчеты зубчатых передач.'+"\n")
    if d_type == 0:
        ExplanatoryNote_file.write('Спроектирована ременная передача.'+"\n")
    else:
        ExplanatoryNote_file.write('Спроектирована цепная передача.'+"\n")
    ExplanatoryNote_file.write('На основе эскизного проектирования полученные данные для прочностных расчетов валов'+"\n")
    ExplanatoryNote_file.write('и подшипников качения.'+"\n")
    ExplanatoryNote_file.write('Расчеты, выполненные на основании современных подходов по проектированию зубчатых передач с'+"\n")
    ExplanatoryNote_file.write('использованием критерия работоспособности – прочности по контактным и изгибным напряжениям.'+"\n")
    ExplanatoryNote_file.write('Редуктор в приводе машины используется для согласования скорости двигателя и исполнительного'+"\n")
    ExplanatoryNote_file.write('механизма, а также для повышения крутящего момента.'+"\n")
    ExplanatoryNote_file.write('\n'+"\n")
    #Выбор электродвигателя
    ExplanatoryNote_file.write('1. ВЫБОР ЭЛЕКТРОДВИГАТЕЛЯ И РАСЧЕТ ОСНОВНЫХ ПАРАМЕТРОВ ПРИВОДА'+"\n")
    ExplanatoryNote_file.write('1.1. Выбор электродвигателя'+"\n")
    ExplanatoryNote_file.write('Требуемая мощность электродвигателя'+"\n")
    ExplanatoryNote_file.write('Ртр = Р3/n_0, (1)'+"\n")
    ExplanatoryNote_file.write('где n_0 – общий КПД привода'+"\n")
    ExplanatoryNote_file.write('n_0 = n_1*n_2*n_3*n_4, (2)'+"\n")
    ExplanatoryNote_file.write('где'+"\n")
    ExplanatoryNote_file.write('n_1 - КПД закрытой цилиндрической зубчатой передачи 0.95...0.98,'+"\n")
    ExplanatoryNote_file.write('принимаем '+performance1_string+"\n")
    if d_type == 0:
        ExplanatoryNote_file.write('n_2 - КПД открытой клиноременной передачи 0.93...0.95,'+"\n")
        ExplanatoryNote_file.write('принимаем '+performance3_string+"\n")
    else:
        ExplanatoryNote_file.write('n_2 - КПД открытой цепной передачи 0.9...0.92,'+"\n")
        ExplanatoryNote_file.write('принимаем '+performance2_string+"\n")
    ExplanatoryNote_file.write('n_3 - КПД одной пары подшипников качения 0.99...0.995,'+"\n")
    ExplanatoryNote_file.write('принимаем '+performance4_string+"\n")
    ExplanatoryNote_file.write('n_4 - КПД муфт 0.98...0.99,'+"\n")
    ExplanatoryNote_file.write('принимаем '+performance5_string+"\n")
    ExplanatoryNote_file.write('Тогда'+"\n")
    if d_type == 0:
        ExplanatoryNote_file.write('Ртр = '+Po+'/'+performance1_string+'*'+performance2_string+'*'+performance4_string+'**2*'+performance5_string+' = '+Pr_string+' кВт'+"\n")
    else:
        ExplanatoryNote_file.write('Ртр = '+Po+'/'+performance1_string+'*'+performance3_string+'*'+performance4_string+'**2*'+performance5_string+' = '+Pr_string+' кВт'+"\n")
    ExplanatoryNote_file.write('Синхронную частоту вращения двигателя выбираем из диапазона'+"\n")
    ExplanatoryNote_file.write('nс = (5…10)*n3 (3)'+"\n")
    ExplanatoryNote_file.write('nс = (5…10)*'+no+' = '+ncmin_string+'...'+ncmax_string+' об/мин'+"\n")
    ExplanatoryNote_file.write('Из условия  Рдв>=Ртр'+"\n")
    ExplanatoryNote_file.write('По требуемой мощности выбираем асинхронный электродвигатель'+"\n")
    ExplanatoryNote_file.write('4А'+model_string+' с ближайшей большей стандартной мощностью Pэ = '+Pi_string+' кВт.'+"\n")
    ExplanatoryNote_file.write('Синхронная частота вращения nс = '+nc_string+' об/мин и скольжением S = '+S_string+'%.'+"\n")
    #Основные параметры привода
    ExplanatoryNote_file.write('1.2. Частота вращения вала двигателя'+"\n")
    ExplanatoryNote_file.write('n0 = nс*(1-S/100) (4)'+"\n")
    ExplanatoryNote_file.write('n0 = '+nc_string+'*(1-'+S_string+'/100) = '+ni_string+' об/мин'+"\n")
    ExplanatoryNote_file.write('1.3. Общее передаточное число привода'+"\n")
    ExplanatoryNote_file.write('u0 = n0/n3 (5)'+"\n")
    ExplanatoryNote_file.write('u0 = '+ni_string+'/'+no+' = '+ut_string+"\n")
    ExplanatoryNote_file.write('1.4. Передаточное число зубчатой передачи'+"\n")
    if scheme == 0 and (g_type == 0 or g_type == 1):
        ExplanatoryNote_file.write('Передаточное число тихоходной цилиндрической передачи 2.5...3.15...4.0,'+"\n")
        ExplanatoryNote_file.write('принимаем по ГОСТ 2185-66 '+ur2_string+"\n")
    elif scheme == 1 and (g_type == 0 or g_type == 1):
        ExplanatoryNote_file.write('Передаточное число быстроходной цилиндрической передачи 3.15...4.0...5.0,'+"\n")
        ExplanatoryNote_file.write('принимаем по ГОСТ 2185-66 '+ur1_string+"\n")
    else:
        ExplanatoryNote_file.write('Передаточное число шевронной передачи 3.15...4.0...5.0,'+"\n")
        ExplanatoryNote_file.write('принимаем по ГОСТ 2185-66 '+ur3_string+"\n")
    if d_type == 0:
        ExplanatoryNote_file.write('1.5. Передаточное число ременной передачи'+"\n")
        ExplanatoryNote_file.write('uрем = u0/uр (6)'+"\n")
        if scheme == 0 and (g_type == 0 or g_type == 1):
            ExplanatoryNote_file.write('uрем = '+ut_string+'/'+ur2_string+' = '+u_add_string+"\n")
        elif scheme == 1 and (g_type == 0 or g_type == 1):
            ExplanatoryNote_file.write('uрем = '+ut_string+'/'+ur1_string+' = '+u_add_string+"\n")
        else:
            ExplanatoryNote_file.write('uрем = '+ut_string+'/'+ur3_string+' = '+u_add_string+"\n")
    else:
        ExplanatoryNote_file.write('1.5. Передаточное число цепной передачи'+"\n")
        ExplanatoryNote_file.write('uцеп = u0/uр (6)'+"\n")
        if scheme == 0 and (g_type == 0 or g_type == 1):
            ExplanatoryNote_file.write('uцеп = '+ut_string+'/'+ur2_string+' = '+u_add_string+"\n")
        elif scheme == 1 and (g_type == 0 or g_type == 1):
            ExplanatoryNote_file.write('uцеп = '+ut_string+'/'+ur1_string+' = '+u_add_string+"\n")
        else:
            ExplanatoryNote_file.write('uцеп = '+ut_string+'/'+ur3_string+' = '+u_add_string+"\n")
    ExplanatoryNote_file.write('1.6. Частоты вращения валов'+"\n")
    ExplanatoryNote_file.write('Индекс соответствует номеру вала на схеме привода'+"\n")
    ExplanatoryNote_file.write('n0 = '+n0_string+' об/мин'+"\n")
    if d_type == 0:
        if scheme == 0 and (g_type == 0 or g_type == 1):
            ExplanatoryNote_file.write('n1 = n0/uрем = '+n0_string+'/'+u_add_string+' = '+n1_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n2 = n1/uр = '+n1_string+'/'+ur2_string+' = '+n2_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n3 = n2 = '+n3_string+' об/мин'+"\n")
        elif scheme == 1 and (g_type == 0 or g_type == 1):
            ExplanatoryNote_file.write('n1 = n0 = '+n0_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n2 = n1/uр = '+n1_string+'/'+ur1_string+' = '+n2_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n3 = n2/uрем = '+n2_string+'/'+u_add_string+' = '+n3_string+' об/мин'+"\n")
        elif scheme == 0 and g_type == 2:
            ExplanatoryNote_file.write('n1 = n0/uрем = '+n0_string+'/'+u_add_string+' = '+n1_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n2 = n1/uр = '+n1_string+'/'+ur3_string+' = '+n2_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n3 = n2 = '+n3_string+' об/мин'+"\n")
        else:
            ExplanatoryNote_file.write('n1 = n0 = '+n0_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n2 = n1/uр = '+n1_string+'/'+ur3_string+' = '+n2_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n3 = n2/uрем = '+n2_string+'/'+u_add_string+' = '+n3_string+' об/мин'+"\n")
    else:
        if scheme == 0 and (g_type == 0 or g_type == 1):
            ExplanatoryNote_file.write('n1 = n0/uцеп = '+n0_string+'/'+u_add_string+' = '+n1_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n2 = n1/uр = '+n1_string+'/'+ur2_string+' = '+n2_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n3 = n2 = '+n3_string+' об/мин'+"\n")
        elif scheme == 1 and (g_type == 0 or g_type == 1):
            ExplanatoryNote_file.write('n1 = n0 = '+n0_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n2 = n1/uр = '+n1_string+'/'+ur1_string+' = '+n2_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n3 = n2/uцеп = '+n2_string+'/'+u_add_string+' = '+n3_string+' об/мин'+"\n")
        elif scheme == 0 and g_type == 2:
            ExplanatoryNote_file.write('n1 = n0/uцеп = '+n0_string+'/'+u_add_string+' = '+n1_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n2 = n1/uр = '+n1_string+'/'+ur3_string+' = '+n2_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n3 = n2 = '+n3_string+' об/мин'+"\n")
        else:
            ExplanatoryNote_file.write('n1 = n0 = '+n0_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n2 = n1/uр = '+n1_string+'/'+ur3_string+' = '+n2_string+' об/мин'+"\n")
            ExplanatoryNote_file.write('n3 = n2/uцеп = '+n2_string+'/'+u_add_string+' = '+n3_string+' об/мин'+"\n")
    ExplanatoryNote_file.write('1.7. Мощности на валах'+"\n")
    ExplanatoryNote_file.write('P0 = Ртр = '+Pr_string+' кВт'+"\n")
    if scheme == 0 and d_type == 0:
        ExplanatoryNote_file.write('P1 = Р0*n_3*n_4 = '+Pr_string+'*'+performance3_string+'*'+performance4_string+' = '+P1_string+' кВт'+"\n")
        ExplanatoryNote_file.write('P2 = Р1*n_1*n_4 = '+P1_string+'*'+performance1_string+'*'+performance4_string+' = '+P2_string+' кВт'+"\n")
        ExplanatoryNote_file.write('P3 = Р2*n_5 = '+P2_string+'*'+performance5_string+' = '+P3_string+' кВт'+"\n")
    elif scheme == 0 and d_type == 1:
        ExplanatoryNote_file.write('P1 = Р0*n_2*n_4 = '+Pr_string+'*'+performance2_string+'*'+performance4_string+' = '+P1_string+' кВт'+"\n")
        ExplanatoryNote_file.write('P2 = Р1*n_1*n_4 = '+P1_string+'*'+performance1_string+'*'+performance4_string+' = '+P2_string+' кВт'+"\n")
        ExplanatoryNote_file.write('P3 = Р2*n_5 = '+P2_string+'*'+performance5_string+' = '+P3_string+' кВт'+"\n")
    elif scheme == 1 and d_type == 0:
        ExplanatoryNote_file.write('P1 = Р0*n_5*n_4 = '+Pr_string+'*'+performance5_string+'*'+performance4_string+' = '+P1_string+' кВт'+"\n")
        ExplanatoryNote_file.write('P2 = Р1*n_1*n_4 = '+P1_string+'*'+performance1_string+'*'+performance4_string+' = '+P2_string+' кВт'+"\n")
        ExplanatoryNote_file.write('P3 = Р2*n_3 = '+P2_string+'*'+performance3_string+' = '+P3_string+' кВт'+"\n")
    else:
        ExplanatoryNote_file.write('P1 = Р0*n_5*n_4 = '+Pr_string+'*'+performance5_string+'*'+performance4_string+' = '+P1_string+' кВт'+"\n")
        ExplanatoryNote_file.write('P2 = Р1*n_1*n_4 = '+P1_string+'*'+performance1_string+'*'+performance4_string+' = '+P2_string+' кВт'+"\n")
        ExplanatoryNote_file.write('P3 = Р2*n_2 = '+P2_string+'*'+performance2_string+' = '+P3_string+' кВт'+"\n")
    ExplanatoryNote_file.write('1.8. Крутящие моменты, передаваемые валами'+"\n")
    ExplanatoryNote_file.write('T0 = 9550*P0/n0 = 9550*'+P0_string+'/'+n0_string+' = '+T0_string+'Нм'+"\n")
    ExplanatoryNote_file.write('T1 = 9550*P1/n1 = 9550*'+P1_string+'/'+n1_string+' = '+T1_string+'Нм'+"\n")
    ExplanatoryNote_file.write('T2 = 9550*P2/n2 = 9550*'+P2_string+'/'+n2_string+' = '+T2_string+'Нм'+"\n")
    ExplanatoryNote_file.write('T3 = 9550*P3/n3 = 9550*'+P3_string+'/'+n3_string+' = '+T3_string+'Нм'+"\n")
    ExplanatoryNote_file.close()

#Пользовательский интерфейс
root = Tk()
root.title('Проектирование приводов технологических машин')
root.geometry('900x600')
frame = Frame(root)
frame.grid()

label0 = Label(text='Мощность на ведомом валу, кВт')
label0.grid(row=0, column=0)
Po_entry = Entry(root, width=10)
Po_entry.grid(row=0, column=2)

label1 = Label(text='Частота вращения ведомого вала, об/мин')
label1.grid(row=1, column=0)
no_entry = Entry(root, width=10)
no_entry.grid(row=1, column=2)

label2 = Label(text='Срок службы передачи, лет')
label2.grid(row=2, column=0)
sl_entry = Entry(root, width=10)
sl_entry.grid(row=2, column=2)

label3 = Label(text='Коэффициент использования передачи в течение года')
label3.grid(row=3, column=0)
c_y_entry = Entry(root, width=10)
c_y_entry.grid(row=3, column=2)

label4 = Label(text='Коэффициент использования передачи в течение суток')
label4.grid(row=4, column=0)
c_d_entry = Entry(root, width=10)
c_d_entry.grid(row=4, column=2)

label5 = Label(text='Продолжительность включения, %')
label5.grid(row=5, column=0)
dc_entry = Entry(root, width=10)
dc_entry.grid(row=5, column=2)

label6 = Label(text='Режим работы привода')
label6.grid(row=6, column=0)
label7 = Label(text='0 - Постоянный')
label7.grid(row=7, column=0)
label8 = Label(text='1 - Тяжелый')
label8.grid(row=8, column=0)
label9 = Label(text='2 - Средний равновероятный')
label9.grid(row=9, column=0)
label10 = Label(text='3 - Средний нормальный')
label10.grid(row=10, column=0)
label11 = Label(text='4 - Легкий')
label11.grid(row=11, column=0)
label12 = Label(text='5 - Особо легкий')
label12.grid(row=12, column=0)
t_mode_entry = Entry(root, width=10)
t_mode_entry.grid(row=6, column=2)

label13 = Label(text='Тип привода')
label13.grid(row=0, column=4)
label14 = Label(text='0 - Реверсивный')
label14.grid(row=1, column=4)
label15 = Label(text='1 - Нереверсивный')
label15.grid(row=2, column=4)
t_type_entry = Entry(root, width=10)
t_type_entry.grid(row=0, column=6)

label16 = Label(text='Тип зубчатой передачи')
label16.grid(row=3, column=4)
label17 = Label(text='0 - Цилиндрическая прямозубая')
label17.grid(row=4, column=4)
label18 = Label(text='1 - Цилиндрическая косозубая')
label18.grid(row=5, column=4)
label19 = Label(text='2 - Шевронная')
label19.grid(row=6, column=4)
g_type_entry = Entry(root, width=10)
g_type_entry.grid(row=3, column=6)

label20 = Label(text='Тип дополнительной передачи')
label20.grid(row=7, column=4)
label21 = Label(text='0 - Ременная передача')
label21.grid(row=8, column=4)
label22 = Label(text='1 - Цепная передача')
label22.grid(row=9, column=4)
d_type_entry = Entry(root, width=10)
d_type_entry.grid(row=7, column=6)

label23 = Label(text='Схема привода')
label23.grid(row=10, column=4)
label24 = Label(text='0 - Мотор-Цепь/Ремень-Редуктор-Муфта-Исполняющий механизм')
label24.grid(row=11, column=4)
label25 = Label(text='1 - Мотор-Муфта-Редуктор-Цепь/Ремень-Исполняющий механизм')
label25.grid(row=12, column=4)
scheme_entry = Entry(root, width=10)
scheme_entry.grid(row=10, column=6)

label26 = Label(text='Конструкция редуктора')
label26.grid(row=13, column=4)
label27 = Label(text='0 - Горизонтальный')
label27.grid(row=14, column=4)
label28 = Label(text='1 - Вертикальный: быстроходный вал сверху')
label28.grid(row=15, column=4)
label29 = Label(text='2 - Вертикальный: быстроходный вал снизу')
label29.grid(row=16, column=4)
c_type_entry = Entry(root, width=10)
c_type_entry.grid(row=13, column=6)

electromotor_button = Button(root, text = 'Подбор электродвигателя',  command = ElectroMotor, bg = 'light green')
electromotor_button.grid(row=17, column=0)

mainparameters_button = Button(root, text = 'Расчет основных параметров передачи',  command = MainParameters, bg = 'light green')
mainparameters_button.grid(row=18, column=0)

material_button = Button(root, text = 'Подобрать материал зубчатых колес',  command = ChoiceMaterial, bg = 'light green')
material_button.grid(row=19, column=0)

calculationgear_button = Button(root, text = 'Расчет зубчатой передачи',  command = CalculationGear, bg = 'light green')
calculationgear_button.grid(row=20, column=0)

additionaldrive_button = Button(root, text = 'Расчет дополнительной передачи',  command = AdditionalDrive, bg = 'light green')
additionaldrive_button.grid(row=21, column=0)

shaftmaterial_button = Button(root, text = 'Подобрать материал валов',  command = ChoiceShaftMaterial, bg = 'light green')
shaftmaterial_button.grid(row=22, column=0)

designshaft_button = Button(root, text = 'Проектный расчет валов',  command = DesignShaft, bg = 'light green')
designshaft_button.grid(row=17, column=4)

bodyelements_button = Button(root, text = 'Расчет элементов корпуса',  command = BodyElements, bg = 'light green')
bodyelements_button.grid(row=18, column=4)

layoutsolution_button = Button(root, text = 'Компоновочное решение',  command = LayoutSolution, bg = 'light green')
layoutsolution_button.grid(row=19, column=4)

layoutsolution_button = Button(root, text = 'Пояснительная записка',  command = ExplanatoryNote, bg = 'light green')
layoutsolution_button.grid(row=20, column=4)

total_close_button = Button(root, text='Завершить', command=root.destroy, bg = 'light pink')
total_close_button.grid(row=23, column=6)

root.mainloop()