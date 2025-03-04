# =============================================CIKLAI IR MASYVAI=======================================================
import random
from itertools import count
from operator import truediv
from traceback import print_tb

number = 17
numbers = [6, 10, 12, 15, 18, 17]  # jei [ ] ir su kableliais, skaitosi kaip listas
print(number)
print(numbers)

empty_list = []
print(empty_list)

empty_list.append(20)
print(empty_list)
empty_list.extend([14, 20, 4])  # butini lauztiniai skliaustai, t.y [], jose vardijamos reiksmes, kurios norime,
# kad butu atvaizduotos konsoleje
print(empty_list)

print(empty_list.count(20))  # suskaiciuoja kiek yra parasytu reiksmes vienetu
empty_list.remove(14)  # panaikina pasirinkta elementa
print(empty_list)
empty_list.pop()
print(empty_list)
popped_element = empty_list.pop()
print(empty_list)
print(popped_element)  # panaikina lauztinius skliaustus, ir pateikia be ju
print("===========================================================================================================")
# ================================================================================
students = ["ingrida", "arnas", "paulius", "anzelika", "raimundas", "rolandas", "dalia", "edvinas", "julija"]
print(students)
students.sort(reverse=True)  # sort () rusiuoja, jei vardai tai pagal abecele, reverse=true surusiuos mazejancia tvarka
print(students)
print("============================================================================================================")
# =======================================================================================================================
# copy = my_numbers.copy() # naudojama istrint pasirinkta reiksme
# copy.remove(7) # naudojama istrint pasirinkta reiksme
# print(my_numbers), print(copy)
#             0  1  2  3  4
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # control + alt + l - surusiuoja
print(my_numbers[7])  # vienas
print(my_numbers[4:8])  # nuo iki
print(my_numbers[1:])  # nuo parasyto, iki galo
print(my_numbers[:4])  # iki nurodytos reiksmes, taciau parasyto neima
print(my_numbers[-5:])  # nuo 5 pozicijos nuo galo iki pat galo
print(my_numbers[:-5])  # nuo pradzios iki 5 pozicijos nuo galo
print(my_numbers[2:-5])  # nuo antros pozicijos iki 5 nuo galo
print(my_numbers[-8:4])  # ima nuo galo IKI pradzios, zydu ismislas
print(my_numbers[:])  # viska atspausdina, kaip paprastas print my_numbers
print(my_numbers[::2])  # paima pagal atitinkama reiksme, pvz jei 2, ima kas antra skaiciu ar reiksme
print(my_numbers[1::2])  # visa imtis nuo pirmo indekso iki galo, kas antras elementas
print(my_numbers[3:7:2])  # visa imtis nuo 3-io indekso iki 7, exclusive kas antras elementas
print(my_numbers[2:-2])  # viskas be pirmu dvieju IR paskutiniu dvieju kas antra
print(my_numbers[::-2])  # visa imtis, kas antras elementas, bet NUO galo
# =====================================================================================================================
# print(len(students))
# for studento_vardas in students: # vaziuoja tiek, kiek yra studentu kaip pvz, paraso studento vardas yra ....
#     print("studento vardas yra:")
#     print(studento_vardas)

# =======================================================================================================================
# for i in range(0,20):
#     if i % 5 == 0: # ar dalinasi is 3 be liekanos
#         continue
#     print(i)
# =====================================================================================================================
# print("break")
# for i in range(1,20):
#     if i % 5 == 0: # ar dalinasi is 3 be liekanos
#         break
#     print(i)
# print(range(0,10))
# =========================================================EXTRA KALNAPILIO DALIS========================================
# for number in range (0,10):
#     print(number)
# for i in range(0, len(students)):
#     print(f"{i}-a literacija. bandau paimti studenta[{i}] studenta kuris yra {students[i]}")
#
# for i in range(0, len(students)):
#     print(f"{i+1}. {students[i]}")
# ===========================================================EKSTRA KALNAPILIO DALIS=====================================
# =======================the while loop==========
# i = 1
# while i < 6: # kol sita salyga grazina TRUE, tol ciklas sukasi
#     print(i)
#     i += 1

# i = 0
# while True:
#     i += 1
#     print(i)
#     if i >= 10:
#         break
print("====================================================================")
# dice = 0
# while dice < 6:
#     dice = random.randint(1, 6)
#     print(dice)
print("=====================================================================")

# print(10 / 2)
# print(12 % 5)  # 10 - 5 = 7, 7 - 5 = 2
# print(12 % 6 == 0)
print("==========================================================")
# for y in range(1,11):
#     for x in range(1,11):
#     lopas += str(y * x)+ " "
#     print(lopas)
# =============================================UZDUOTYS================
# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
# for i in range(10):
#     print("labas")
# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.
# for i in range(10):
#     print(i)
# Sukurkite masyvą iš dešimties augalų pavadinimų.
# augalai = ["roze", "tulpe", "berzas", "azuolas", "liepa", "egle", "orchideja", "kaktusas", "levanda", "saulegraza"]
# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

# for augals in augalai:
#     print(augals)
# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).
# augalai = ["roze, tulpe, berzas, azuolas, liepa, egle, orchideja, kaktusas, levanda, saulegraza"]
# augalai.reverse()
# print(augalai)
# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
# for skaicius in range(10,51,2):
#     print(skaicius)
# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
# for skaicius in range(10,51,2):
#     if skaicius % 10 == 0:
#         continue
#     print(skaicius)
# Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę
# count = 0
# for i in range(21):
#     if i % 2 == 0:
#         count += 1
#
# print("Porinių reikšmių kiekis:", count)
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)
# print(augalai)
# trumpi = [len(x) < 5 for x in augalai]
# print(trumpi.count(True))
# ilgi = [len(x) > 7 for x in augalai]
# print(ilgi.count(True))
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)
# tarpas = [5 < len(x) < 10 for x in augalai]
# print("tarp:", tarpas.count(True))
print("=====================================")
# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

# random_numbers = []
# for i in range (0,300):
#     random_numbers.append(random.randint(0,301))
# # print(random_numbers)
# kiekis = len([number for number in random_numbers if number >150])
# for kkk in random_numbers:
#     if kkk > 275:
#      print(f"({kkk})")
#     else:
#         print(kkk)
# print("kiekis:", kiekis)



# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.
# for s in range(1,3001):
#     if s % 77 == 0:
#         print(s, end=", ")
# Nupieškite kvadratą iš “ * ”, kurio kraštines sudaro 25“ * ”.
size = 5
for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("X ", end=" ")
        else:
            print("o ", end=" ")
    print()
# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;
print("========================================")


# kiek = 10
# for i in range(kiek):
#     print("H" if random.randint(0,1) ==0
# else "S")
# herbass = 0
# while True:
#     metimas = random.randint(0,1)
#     print("H" if metimas == 0
# else "S")
#     if metimas == 0:
#         break
#
# # ===============================
# while herbass < 3:
#     metimas = random.randint(0,1)
#     print("H" if metimas == 0
# else "S")
#     if metimas == 0:
#         herbass +=1
# else:
#     herbass = 0
# ==================================================
# vienmatis nuo dvimacio masyvai = masyvas kaunas, kas jame yra
# Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25. Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: ​laimėtojo vardas​”. Taškų kiekį generuokite funkcija ​random.randint(x,x)​. Žaidimą laimi tas, kas greičiau surenka 222 taškus. Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.
# kazio = 0
# petro = 0
# while kazio < 222 and petro < 222:
#     kazio += random.randint(5,25)
#     petro += random.randint(10,20)
#     print(f"kazys: {kazio} tasku, petras: {petro} tasku")
# if kazio >= 222:
#     print(f"laimejo Kazys su {kazio} tasku")
# else:
#     print(f"laimejo Petras su {petro} tasku")

# ===============================================================================
# Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą (https://lt.wikipedia.org/wiki/Rombas), kurio aukštis 21 eilutė.

# for y in range(11,20):
#     row = " "
#     for x in range(11,20):
#         if (21 - y < x and x < (21/2)) or (x < y and x >= (20/2)):
#             row += "*"
#         else:
#             row +="_"
#     print(row)

# ==========================================================================
# Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# import random
# ilgis = 85
# ikalimas = 0
# kartai = 0
#
# while ikalimas < ilgis:
#     kartai = random.randint(1,5)
#     ikalimas += kartai
#     kartai += 1
#     print(f"vini pavyko ikelti per {kartai} smugius. Ikalimo gylis: {ikalimas} cm")

# ilgis = 85
# sukalta = 0
# smugiai = 0
# #for i in range(0,7):
# while sukalta < ilgis:
#     smugis = random.randint(5,20)
#     sukalta += smugis # prideda dar viena
#     smugiai += 1
# print(f"{smugiai}-tas smugis {smugis}mm, is viso sukalta {sukalta}mm")
# “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# import random
# ilgis = 85
# sukaltu_viniu = 5
# for i in range(0,sukaltu_viniu):
#     ikalimas = 0
#     smugis = 0
#     while ikalimas < ilgis:
#         smugis = random.randint(5,20)
#         ikalimas += smugis
#         smugis += 1
#         print(f"{i+1} vinis pavyko ikalti per {smugis} smugius, is viso sukalta {ikalimas}mm")
# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.
# ilgis = 85
# vinys = 5
# for vinis in range (1,vinys +1):
#     ikalimas = 0
#     smugis = 0
#
#     while ikalimas < ilgis:
#         smugis += 1
#         if random.randint(0,1) == 1:
#             smugiai = random.randint(20,30)
#             ikalimas += smugiai
#     print(f"{vinis}-a vini pavyko ikalti per {smugis} smugius.")
# Sugeneruokite stringą, kurį sudarytų 50 atsitiktinių skaičių nuo 1 iki 200, atskirtų tarpais. Skaičiai turi būti unikalūs (t.y. nesikartoti).
# randominiai = [random.randint(1,200)
#                for i in range(50)]
# print("pirmas:", randominiai)
# Sugeneruokite antrą stringą, pasinaudodami pirmu, palikdami jame tik pirminius skaičius(t.y tokius,kurie dalinasi be liekanos tik iš 1 ir patys is savęs)

# randominiai = set(random.randint(1,200) for i in range(50))
# print("pirmas stringas:", randominiai)
# for sk in randominiai:
#     if sk > 1:
#         prime = True
#         for i in range(2,sk):
#             if sk % i == 0:
#                 prime = False
#                 break
#         if prime:
#             print(f" {sk} ", end=" ")

git config --global user.email "meskynasw@gmail.com"
git config --global user.name "Tymberis"