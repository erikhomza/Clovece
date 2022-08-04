

import  random
plocha = ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]

hrac1 = ["O","O","O","O"]
hrac2 = ["O","O","O","O"]
hrac3 = ["O","O","O","O"]
hrac4 = ["O","O","O","O"]

hrac1_domcek = ["đ","Đ","ł","Ł"]
hrac2_domcek = ["€","$","#","&"]
hrac3_domcek = ["x","y","c","v"]
hrac4_domcek = ["1","2","3","4"]



def nova_hra(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    print("Pre novú hru stlačte 1, pre vypnutie stlačte 0.")
    novahra = input()
    if novahra == "1":
        plocha = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
                  "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]

        hrac1 = ["O", "O", "O", "O"]
        hrac2 = ["O", "O", "O", "O"]
        hrac3 = ["O", "O", "O", "O"]
        hrac4 = ["O", "O", "O", "O"]

        hrac1_domcek = ["đ", "Đ", "ł", "Ł"]
        hrac2_domcek = ["€", "$", "#", "&"]
        hrac3_domcek = ["x", "y", "c", "v"]
        hrac4_domcek = ["1", "2", "3", "4"]
        hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
    elif novahra == "0":
        quit()
    else:
        nova_hra(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)




def hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    print(" ",hrac1_domcek[0],hrac1_domcek[1]," "," ",plocha[38],plocha[39],plocha[0]," "," ",hrac2_domcek[0],hrac2_domcek[1])
    print(" ", hrac1_domcek[2], hrac1_domcek[3], " ", " ",plocha[37],hrac1[0], plocha[1], " ", " ", hrac2_domcek[2],
          hrac2_domcek[3])
    print(" ", " ", " "," ", " ",plocha[36], hrac1[1], plocha[2], " ", " ", " "," ")
    print(" ", " ", " ", " ", " ", plocha[35], hrac1[2], plocha[3], " ", " ", " ", " ")
    print(" ", plocha[30], plocha[31], plocha[32], plocha[33], plocha[34], hrac1[3], plocha[4], plocha[5], plocha[6], plocha[7], plocha[8])
    print(" ", plocha[29], hrac4[0], hrac4[1], hrac4[2], hrac4[3], " ", hrac2[3], hrac2[2], hrac2[1], hrac2[0], plocha[9])

    print(" ", plocha[28], plocha[27], plocha[26], plocha[25], plocha[24], hrac3[3], plocha[14], plocha[13], plocha[12],
          plocha[11], plocha[10])
    print(" ", " ", " ", " ", " ", plocha[23], hrac3[2], plocha[15], " ", " ", " ", " ")
    print(" ", " ", " ", " ", " ", plocha[22], hrac3[1], plocha[16], " ", " ", " ", " ")
    print(" ", hrac4_domcek[0], hrac4_domcek[1], " ", " ", plocha[21], hrac3[0], plocha[17], " ", " ", hrac3_domcek[0],
          hrac3_domcek[1])
    print(" ", hrac4_domcek[2], hrac4_domcek[3], " ", " ", plocha[20], plocha[19], plocha[18], " ", " ", hrac3_domcek[2],
          hrac3_domcek[3])



#Hrac1 zaciatok
def nova_figurka1(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    vyber = input()
    if vyber in hrac1_domcek:
        index = hrac1_domcek.index(vyber)
        if plocha[0] == "€":
            hrac2_domcek[0] = "€"
        elif plocha[0] == "$":
            hrac2_domcek[1] = "$"
        elif plocha[0] == "#":
            hrac2_domcek[2] = "#"
        elif plocha[0] == "&":
            hrac2_domcek[3] = "&"
        elif plocha[0] == "x":
            hrac3_domcek[0] = "x"
        elif plocha[0] == "y":
            hrac3_domcek[1] = "y"
        elif plocha[0] == "c":
            hrac3_domcek[2] = "c"
        elif plocha[0] == "v":
            hrac3_domcek[3] = "v"
        elif plocha[0] == "1":
            hrac4_domcek[0] = "1"
        elif plocha[0] == "2":
            hrac4_domcek[1] = "2"
        elif plocha[0] == "3":
            hrac4_domcek[2] = "3"
        elif plocha[0] == "4":
            hrac4_domcek[3] = "4"
        plocha[0] = hrac1_domcek[index]
        hrac1_domcek[index] = "-"
        hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        hrac2_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
    else:
        print("Chybný ťah.")
        nova_figurka1(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)



def hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    if "đ" in hrac1 and "Đ" in hrac1 and "ł" in hrac1 and "Ł" in hrac1:
        print("Hráč 1 vyhral.")
    if "€" in hrac2 and "$" in hrac2 and "#" in hrac2 and "&" in hrac2:
        print("Hráč 2 vyhral.")
    if "x" in hrac3 and "y" in hrac3 and "c" in hrac3 and "v" in hrac3:
        print("Hráč 3 vyhral.")
    if "1" in hrac4 and "2" in hrac4 and "3" in hrac4 and "4" in hrac4:
        print("Hráč 4 vyhral.")
    print("Vyberte figúrku.")
    vyber = input()
    if vyber == "đ" or vyber == "Đ" or vyber == "ł" or vyber == "Ł":
        if vyber in plocha:
            index = plocha.index(vyber)
            if (index + hod) < len(plocha):
                if plocha[index + hod] != "đ" and plocha[index + hod] != "Đ" and plocha[index + hod] != "ł" and plocha[
                    index + hod] != "Ł":
                    if plocha[index + hod] == "€":
                        hrac2_domcek[0] = "€"
                    elif plocha[index + hod] == "$":
                        hrac2_domcek[1] = "$"
                    elif plocha[index + hod] == "#":
                        hrac2_domcek[2] = "#"
                    elif plocha[index + hod] == "&":
                        hrac2_domcek[3] = "&"
                    elif plocha[index + hod] == "x":
                        hrac3_domcek[0] = "x"
                    elif plocha[index + hod] == "y":
                        hrac3_domcek[1] = "y"
                    elif plocha[index + hod] == "c":
                        hrac3_domcek[2] = "c"
                    elif plocha[index + hod] == "v":
                        hrac3_domcek[3] = "v"
                    elif plocha[index + hod] == "1":
                        hrac4_domcek[0] = "1"
                    elif plocha[index + hod] == "2":
                        hrac4_domcek[1] = "2"
                    elif plocha[index + hod] == "3":
                        hrac4_domcek[2] = "3"
                    elif plocha[index + hod] == "4":
                        hrac4_domcek[3] = "4"
                    plocha[index + hod] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        print("Na rade je hráč 1.")
                        print(hod)
                        hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac2_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
            else:
                x = (index + hod) - len(plocha)
                if x <= len(hrac1):
                    hrac1[x - 1] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac2_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac2_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        elif vyber in hrac1_domcek and hod == 6:
            if plocha[0] != "đ" and plocha[0] != "Đ" and plocha[0] != "ł" and plocha[0] != "Ł":
                if plocha[0] == "€":
                    hrac2_domcek[0] = "€"
                elif plocha[0] == "$":
                    hrac2_domcek[1] = "$"
                elif plocha[0] == "#":
                    hrac2_domcek[2] = "#"
                elif plocha[0] == "&":
                    hrac2_domcek[3] = "&"
                elif plocha[0] == "x":
                    hrac3_domcek[0] = "x"
                elif plocha[0] == "y":
                    hrac3_domcek[1] = "y"
                elif plocha[0] == "c":
                    hrac3_domcek[2] = "c"
                elif plocha[0] == "v":
                    hrac3_domcek[3] = "v"
                elif plocha[0] == "1":
                    hrac4_domcek[0] = "1"
                elif plocha[0] == "2":
                    hrac4_domcek[1] = "2"
                elif plocha[0] == "3":
                    hrac4_domcek[2] = "3"
                elif plocha[0] == "4":
                    hrac4_domcek[3] = "4"
                index = hrac1_domcek.index(vyber)
                plocha[0] = vyber
                hrac1_domcek[index] = "-"
                hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                              hrac4_domcek)
                if hod == 6:
                    hod = random.randint(1,6)
                    hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                              hrac4_domcek)
                hrac2_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
            else:
                hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                            hrac4_domcek)

        else:
            hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                        hrac4_domcek)
    else:
        hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                    hrac4_domcek)




def hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    if "đ" in hrac1 and "Đ" in hrac1 and "ł" in hrac1 and "Ł" in hrac1:
        print("Hráč 1 vyhral.")
    if "€" in hrac2 and "$" in hrac2 and "#" in hrac2 and "&" in hrac2:
        print("Hráč 2 vyhral.")
    if "x" in hrac3 and "y" in hrac3 and "c" in hrac3 and "v" in hrac3:
        print("Hráč 3 vyhral.")
    if "1" in hrac4 and "2" in hrac4 and "3" in hrac4 and "4" in hrac4:
        print("Hráč 4 vyhral.")
    print("Na rade je hráč 1.")
    hod = random.randint(1, 6)
    print(hod)
    if "đ" not in plocha and "Đ" not in plocha and "ł" not in plocha and "Ł" not in plocha:
        if hod == 6:
            nova_figurka1(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        else:
            hod = random.randint(1, 6)
            print(hod)
            if hod == 6:
                nova_figurka1(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
            else:
                hod = random.randint(1, 6)
                print(hod)
                if hod == 6:
                    nova_figurka1(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
                else:
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac2_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)

    else:
        hrac1_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
# Hrac1 koniec

# Hrac2 zaciatok


def nova_figurka2(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    vyber = input()
    if vyber in hrac2_domcek:
        index = hrac2_domcek.index(vyber)
        if plocha[10] == "đ":
            hrac1_domcek[0] = "đ"
        elif plocha[10] == "Đ":
            hrac1_domcek[1] = "Đ"
        elif plocha[10] == "ł":
            hrac1_domcek[2] = "ł"
        elif plocha[10] == "Ł":
            hrac1_domcek[3] = "Ł"
        elif plocha[10] == "x":
            hrac3_domcek[0] = "x"
        elif plocha[10] == "y":
            hrac3_domcek[1] = "y"
        elif plocha[10] == "c":
            hrac3_domcek[2] = "c"
        elif plocha[10] == "v":
            hrac3_domcek[3] = "v"
        elif plocha[10] == "1":
            hrac4_domcek[0] = "1"
        elif plocha[10] == "2":
            hrac4_domcek[1] = "2"
        elif plocha[10] == "3":
            hrac4_domcek[2] = "3"
        elif plocha[10] == "4":
            hrac4_domcek[3] = "4"
        plocha[10] = hrac2_domcek[index]
        hrac2_domcek[index] = "-"
        hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        hrac3_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
    else:
        print("Chybný ťah.")
        nova_figurka2(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)



def hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    if "đ" in hrac1 and "Đ" in hrac1 and "ł" in hrac1 and "Ł" in hrac1:
        print("Hráč 1 vyhral.")
    if "€" in hrac2 and "$" in hrac2 and "#" in hrac2 and "&" in hrac2:
        print("Hráč 2 vyhral.")
    if "x" in hrac3 and "y" in hrac3 and "c" in hrac3 and "v" in hrac3:
        print("Hráč 3 vyhral.")
    if "1" in hrac4 and "2" in hrac4 and "3" in hrac4 and "4" in hrac4:
        print("Hráč 4 vyhral.")
    print("Vyberte figúrku.")
    vyber = input()
    if vyber == "€" or vyber == "$" or vyber == "#" or vyber == "&":
        if vyber in plocha:
            index = plocha.index(vyber)
            if ((index+hod) < len(plocha) and (index+hod) > 9) or (index+hod) <= 9:
                if plocha[index + hod] != "€" and plocha[index + hod] != "$" and plocha[index + hod] != "#" and plocha[
                    index + hod] != "&":
                    if plocha[index + hod] == "đ":
                        hrac1_domcek[0] = "đ"
                    elif plocha[index + hod] == "Đ":
                        hrac1_domcek[1] = "Đ"
                    elif plocha[index + hod] == "ł":
                        hrac1_domcek[2] = "ł"
                    elif plocha[index + hod] == "Ł":
                        hrac1_domcek[3] = "Ł"
                    elif plocha[index + hod] == "x":
                        hrac3_domcek[0] = "x"
                    elif plocha[index + hod] == "y":
                        hrac3_domcek[1] = "y"
                    elif plocha[index + hod] == "c":
                        hrac3_domcek[2] = "c"
                    elif plocha[index + hod] == "v":
                        hrac3_domcek[3] = "v"
                    elif plocha[index + hod] == "1":
                        hrac4_domcek[0] = "1"
                    elif plocha[index + hod] == "2":
                        hrac4_domcek[1] = "2"
                    elif plocha[index + hod] == "3":
                        hrac4_domcek[2] = "3"
                    elif plocha[index + hod] == "4":
                        hrac4_domcek[3] = "4"
                    plocha[index + hod] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        print("Na rade je hráč 2.")
                        print(hod)
                        hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac3_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
            elif ((index + hod) - len(plocha)) <= 9 and (index + hod) > 9:
                if plocha[index + hod - len(plocha)] != "€" and plocha[index + hod - len(plocha)] != "$" and plocha[index + hod - len(plocha)] != "#" and plocha[
                    index + hod - len(plocha)] != "&":
                    if plocha[(index + hod) - len(plocha)] == "đ":
                        hrac1_domcek[0] = "đ"
                    elif plocha[(index + hod) - len(plocha)] == "Đ":
                        hrac1_domcek[1] = "Đ"
                    elif plocha[(index + hod) - len(plocha)] == "ł":
                        hrac1_domcek[2] = "ł"
                    elif plocha[(index + hod) - len(plocha)] == "Ł":
                        hrac1_domcek[3] = "Ł"
                    elif plocha[(index + hod) - len(plocha)] == "x":
                        hrac3_domcek[0] = "x"
                    elif plocha[(index + hod) - len(plocha)] == "y":
                        hrac3_domcek[1] = "y"
                    elif plocha[(index + hod) - len(plocha)] == "c":
                        hrac3_domcek[2] = "c"
                    elif plocha[(index + hod) - len(plocha)] == "v":
                        hrac3_domcek[3] = "v"
                    elif plocha[(index + hod) - len(plocha)] == "1":
                        hrac4_domcek[0] = "1"
                    elif plocha[(index + hod) - len(plocha)] == "2":
                        hrac4_domcek[1] = "2"
                    elif plocha[(index + hod) - len(plocha)] == "3":
                        hrac4_domcek[2] = "3"
                    elif plocha[(index + hod) - len(plocha)] == "4":
                        hrac4_domcek[3] = "4"
                    plocha[(index + hod) - len(plocha)] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        print("Na rade je hráč 2.")
                        print(hod)
                        hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac3_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
            else:
                x = (index + hod) - 9
                if x <= len(hrac2):
                    hrac2[x - 1] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac3_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac3_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        elif vyber in hrac2_domcek and hod == 6:
            if plocha[10] != "€" and plocha[10] != "$" and plocha[10] != "#" and plocha[10] != "&":
                if plocha[10] == "đ":
                    hrac1_domcek[0] = "đ"
                elif plocha[10] == "Đ":
                    hrac1_domcek[1] = "Đ"
                elif plocha[10] == "ł":
                    hrac1_domcek[2] = "ł"
                elif plocha[10] == "Ł":
                    hrac1_domcek[3] = "Ł"
                elif plocha[10] == "x":
                    hrac3_domcek[0] = "x"
                elif plocha[10] == "y":
                    hrac3_domcek[1] = "y"
                elif plocha[10] == "c":
                    hrac3_domcek[2] = "c"
                elif plocha[10] == "v":
                    hrac3_domcek[3] = "v"
                elif plocha[10] == "1":
                    hrac4_domcek[0] = "1"
                elif plocha[10] == "2":
                    hrac4_domcek[1] = "2"
                elif plocha[10] == "3":
                    hrac4_domcek[2] = "3"
                elif plocha[10] == "4":
                    hrac4_domcek[3] = "4"
                index = hrac2_domcek.index(vyber)
                plocha[10] = vyber
                hrac2_domcek[index] = "-"
                hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                              hrac4_domcek)
                if hod == 6:
                    hod = random.randint(1,6)
                    hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                              hrac4_domcek)
                hrac3_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
            else:
                hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                            hrac4_domcek)

        else:
            hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                        hrac4_domcek)
    else:
        hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                    hrac4_domcek)




def hrac2_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    if "đ" in hrac1 and "Đ" in hrac1 and "ł" in hrac1 and "Ł" in hrac1:
        print("Hráč 1 vyhral.")
    if "€" in hrac2 and "$" in hrac2 and "#" in hrac2 and "&" in hrac2:
        print("Hráč 2 vyhral.")
    if "x" in hrac3 and "y" in hrac3 and "c" in hrac3 and "v" in hrac3:
        print("Hráč 3 vyhral.")
    if "1" in hrac4 and "2" in hrac4 and "3" in hrac4 and "4" in hrac4:
        print("Hráč 4 vyhral.")
    print("Na rade je hráč 2.")
    hod = random.randint(1, 6)
    print(hod)
    if "€" not in plocha and "$" not in plocha and "#" not in plocha and "&" not in plocha:
        if hod == 6:
            nova_figurka2(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        else:
            hod = random.randint(1, 6)
            print(hod)
            if hod == 6:
                nova_figurka2(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
            else:
                hod = random.randint(1, 6)
                print(hod)
                if hod == 6:
                    nova_figurka2(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
                else:
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac3_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)

    else:
        hrac2_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)

# Hrac2 koniec

# Hrac3 zaciatok



def nova_figurka3(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    vyber = input()
    if vyber in hrac3_domcek:
        index = hrac3_domcek.index(vyber)
        if plocha[20] == "đ":
            hrac1_domcek[0] = "đ"
        elif plocha[20] == "Đ":
            hrac1_domcek[1] = "Đ"
        elif plocha[20] == "ł":
            hrac1_domcek[2] = "ł"
        elif plocha[20] == "Ł":
            hrac1_domcek[3] = "Ł"
        elif plocha[20] == "€":
            hrac2_domcek[0] = "€"
        elif plocha[20] == "$":
            hrac2_domcek[1] = "$"
        elif plocha[20] == "#":
            hrac2_domcek[2] = "#"
        elif plocha[20] == "&":
            hrac2_domcek[3] = "&"
        elif plocha[20] == "1":
            hrac4_domcek[0] = "1"
        elif plocha[20] == "2":
            hrac4_domcek[1] = "2"
        elif plocha[20] == "3":
            hrac4_domcek[2] = "3"
        elif plocha[20] == "4":
            hrac4_domcek[3] = "4"
        plocha[20] = hrac3_domcek[index]
        hrac3_domcek[index] = "-"
        hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        hrac4_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
    else:
        print("Chybný ťah.")
        nova_figurka3(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)



def hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    if "đ" in hrac1 and "Đ" in hrac1 and "ł" in hrac1 and "Ł" in hrac1:
        print("Hráč 1 vyhral.")
    if "€" in hrac2 and "$" in hrac2 and "#" in hrac2 and "&" in hrac2:
        print("Hráč 2 vyhral.")
    if "x" in hrac3 and "y" in hrac3 and "c" in hrac3 and "v" in hrac3:
        print("Hráč 3 vyhral.")
    if "1" in hrac4 and "2" in hrac4 and "3" in hrac4 and "4" in hrac4:
        print("Hráč 4 vyhral.")
    print("Vyberte figúrku.")
    vyber = input()
    if vyber == "x" or vyber == "y" or vyber == "c" or vyber == "v":
        if vyber in plocha:
            index = plocha.index(vyber)
            if ((index+hod) < len(plocha) and (index+hod) > 19) or (index+hod) <= 19:
                if plocha[index + hod] != "x" and plocha[index + hod] != "y" and plocha[index + hod] != "c" and plocha[
                    index + hod] != "v":
                    if plocha[index + hod] == "đ":
                        hrac1_domcek[0] = "đ"
                    elif plocha[index + hod] == "Đ":
                        hrac1_domcek[1] = "Đ"
                    elif plocha[index + hod] == "ł":
                        hrac1_domcek[2] = "ł"
                    elif plocha[index + hod] == "Ł":
                        hrac1_domcek[3] = "Ł"
                    elif plocha[index + hod] == "€":
                        hrac2_domcek[0] = "€"
                    elif plocha[index + hod] == "$":
                        hrac2_domcek[1] = "$"
                    elif plocha[index + hod] == "#":
                        hrac2_domcek[2] = "#"
                    elif plocha[index + hod] == "&":
                        hrac2_domcek[3] = "&"
                    elif plocha[index + hod] == "1":
                        hrac4_domcek[0] = "1"
                    elif plocha[index + hod] == "2":
                        hrac4_domcek[1] = "2"
                    elif plocha[index + hod] == "3":
                        hrac4_domcek[2] = "3"
                    elif plocha[index + hod] == "4":
                        hrac4_domcek[3] = "4"
                    plocha[index + hod] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        print("Na rade je hráč 3.")
                        print(hod)
                        hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac4_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
            elif ((index + hod) - len(plocha)) <= 19 and (index + hod) > 19:
                if plocha[index + hod - len(plocha)] != "x" and plocha[index + hod - len(plocha)] != "y" and plocha[index + hod - len(plocha)] != "c" and plocha[
                    index + hod - len(plocha)] != "v":
                    if plocha[(index + hod) - len(plocha)] == "đ":
                        hrac1_domcek[0] = "đ"
                    elif plocha[(index + hod) - len(plocha)] == "Đ":
                        hrac1_domcek[1] = "Đ"
                    elif plocha[(index + hod) - len(plocha)] == "ł":
                        hrac1_domcek[2] = "ł"
                    elif plocha[(index + hod) - len(plocha)] == "Ł":
                        hrac1_domcek[3] = "Ł"
                    elif plocha[(index + hod) - len(plocha)] == "€":
                        hrac2_domcek[0] = "€"
                    elif plocha[(index + hod) - len(plocha)] == "$":
                        hrac2_domcek[1] = "$"
                    elif plocha[(index + hod) - len(plocha)] == "#":
                        hrac2_domcek[2] = "#"
                    elif plocha[(index + hod) - len(plocha)] == "&":
                        hrac2_domcek[3] = "&"
                    elif plocha[(index + hod) - len(plocha)] == "1":
                        hrac4_domcek[0] = "1"
                    elif plocha[(index + hod) - len(plocha)] == "2":
                        hrac4_domcek[1] = "2"
                    elif plocha[(index + hod) - len(plocha)] == "3":
                        hrac4_domcek[2] = "3"
                    elif plocha[(index + hod) - len(plocha)] == "4":
                        hrac4_domcek[3] = "4"
                    plocha[(index + hod) - len(plocha)] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        print("Na rade je hráč 3.")
                        print(hod)
                        hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac4_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
            else:
                x = (index + hod) - 19
                if x <= len(hrac2):
                    hrac3[x - 1] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac4_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac4_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        elif vyber in hrac3_domcek and hod == 6:
            if plocha[20] != "x" and plocha[20] != "y" and plocha[20] != "c" and plocha[20] != "v":
                if plocha[20] == "đ":
                    hrac1_domcek[0] = "đ"
                elif plocha[20] == "Đ":
                    hrac1_domcek[1] = "Đ"
                elif plocha[20] == "ł":
                    hrac1_domcek[2] = "ł"
                elif plocha[20] == "Ł":
                    hrac1_domcek[3] = "Ł"
                elif plocha[20] == "€":
                    hrac2_domcek[0] = "€"
                elif plocha[20] == "$":
                    hrac2_domcek[1] = "$"
                elif plocha[20] == "#":
                    hrac2_domcek[2] = "#"
                elif plocha[20] == "&":
                    hrac2_domcek[3] = "&"
                elif plocha[20] == "1":
                    hrac4_domcek[0] = "1"
                elif plocha[20] == "2":
                    hrac4_domcek[1] = "2"
                elif plocha[20] == "3":
                    hrac4_domcek[2] = "3"
                elif plocha[20] == "4":
                    hrac4_domcek[3] = "4"
                index = hrac3_domcek.index(vyber)
                plocha[20] = vyber
                hrac3_domcek[index] = "-"
                hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                              hrac4_domcek)
                if hod == 6:
                    hod = random.randint(1,6)
                    hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                              hrac4_domcek)
                hrac4_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
            else:
                hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                            hrac4_domcek)

        else:
            hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                        hrac4_domcek)
    else:
        hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                    hrac4_domcek)




def hrac3_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    if "đ" in hrac1 and "Đ" in hrac1 and "ł" in hrac1 and "Ł" in hrac1:
        print("Hráč 1 vyhral.")
    if "€" in hrac2 and "$" in hrac2 and "#" in hrac2 and "&" in hrac2:
        print("Hráč 2 vyhral.")
    if "x" in hrac3 and "y" in hrac3 and "c" in hrac3 and "v" in hrac3:
        print("Hráč 3 vyhral.")
    if "1" in hrac4 and "2" in hrac4 and "3" in hrac4 and "4" in hrac4:
        print("Hráč 4 vyhral.")
    print("Na rade je hráč 3.")
    hod = random.randint(1, 6)
    print(hod)
    if "x" not in plocha and "y" not in plocha and "c" not in plocha and "v" not in plocha:
        if hod == 6:
            nova_figurka3(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        else:
            hod = random.randint(1, 6)
            print(hod)
            if hod == 6:
                nova_figurka3(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
            else:
                hod = random.randint(1, 6)
                print(hod)
                if hod == 6:
                    nova_figurka3(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
                else:
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac4_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)

    else:
        hrac3_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)

# Hráč3 koniec

# Hráč4 začiatok



def nova_figurka4(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    vyber = input()
    if vyber in hrac4_domcek:
        index = hrac4_domcek.index(vyber)
        if plocha[30] == "đ":
            hrac1_domcek[0] = "đ"
        elif plocha[30] == "Đ":
            hrac1_domcek[1] = "Đ"
        elif plocha[30] == "ł":
            hrac1_domcek[2] = "ł"
        elif plocha[30] == "Ł":
            hrac1_domcek[3] = "Ł"
        elif plocha[30] == "€":
            hrac2_domcek[0] = "€"
        elif plocha[30] == "$":
            hrac2_domcek[1] = "$"
        elif plocha[30] == "#":
            hrac2_domcek[2] = "#"
        elif plocha[30] == "&":
            hrac2_domcek[3] = "&"
        elif plocha[30] == "x":
            hrac3_domcek[0] = "x"
        elif plocha[30] == "y":
            hrac3_domcek[1] = "y"
        elif plocha[30] == "c":
            hrac3_domcek[2] = "c"
        elif plocha[30] == "v":
            hrac3_domcek[3] = "v"
        plocha[30] = hrac4_domcek[index]
        hrac4_domcek[index] = "-"
        hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
    else:
        print("Chybný ťah.")
        nova_figurka3(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)



def hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    if "đ" in hrac1 and "Đ" in hrac1 and "ł" in hrac1 and "Ł" in hrac1:
        print("Hráč 1 vyhral.")
    if "€" in hrac2 and "$" in hrac2 and "#" in hrac2 and "&" in hrac2:
        print("Hráč 2 vyhral.")
    if "x" in hrac3 and "y" in hrac3 and "c" in hrac3 and "v" in hrac3:
        print("Hráč 3 vyhral.")
    if "1" in hrac4 and "2" in hrac4 and "3" in hrac4 and "4" in hrac4:
        print("Hráč 4 vyhral.")
    print("Vyberte figúrku.")
    vyber = input()
    if vyber == "1" or vyber == "2" or vyber == "3" or vyber == "4":
        if vyber in plocha:
            index = plocha.index(vyber)
            if ((index+hod) < len(plocha) and (index+hod) > 29) or (index+hod) <= 29:
                if plocha[index + hod] != "1" and plocha[index + hod] != "2" and plocha[index + hod] != "3" and plocha[
                    index + hod] != "4":
                    if plocha[index + hod] == "đ":
                        hrac1_domcek[0] = "đ"
                    elif plocha[index + hod] == "Đ":
                        hrac1_domcek[1] = "Đ"
                    elif plocha[index + hod] == "ł":
                        hrac1_domcek[2] = "ł"
                    elif plocha[index + hod] == "Ł":
                        hrac1_domcek[3] = "Ł"
                    elif plocha[index + hod] == "€":
                        hrac2_domcek[0] = "€"
                    elif plocha[index + hod] == "$":
                        hrac2_domcek[1] = "$"
                    elif plocha[index + hod] == "#":
                        hrac2_domcek[2] = "#"
                    elif plocha[index + hod] == "&":
                        hrac2_domcek[3] = "&"
                    elif plocha[index + hod] == "x":
                        hrac3_domcek[0] = "x"
                    elif plocha[index + hod] == "y":
                        hrac3_domcek[1] = "y"
                    elif plocha[index + hod] == "c":
                        hrac3_domcek[2] = "c"
                    elif plocha[index + hod] == "v":
                        hrac3_domcek[3] = "v"
                    plocha[index + hod] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        print("Na rade je hráč 4.")
                        print(hod)
                        hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
            elif ((index + hod) - len(plocha)) <= 29 and (index + hod) > 29:
                if plocha[index + hod - len(plocha)] != "1" and plocha[index + hod - len(plocha)] != "2" and plocha[index + hod - len(plocha)] != "3" and plocha[
                    index + hod - len(plocha)] != "4":
                    if plocha[(index + hod) - len(plocha)] == "đ":
                        hrac1_domcek[0] = "đ"
                    elif plocha[(index + hod) - len(plocha)] == "Đ":
                        hrac1_domcek[1] = "Đ"
                    elif plocha[(index + hod) - len(plocha)] == "ł":
                        hrac1_domcek[2] = "ł"
                    elif plocha[(index + hod) - len(plocha)] == "Ł":
                        hrac1_domcek[3] = "Ł"
                    elif plocha[(index + hod) - len(plocha)] == "€":
                        hrac2_domcek[0] = "€"
                    elif plocha[(index + hod) - len(plocha)] == "$":
                        hrac2_domcek[1] = "$"
                    elif plocha[(index + hod) - len(plocha)] == "#":
                        hrac2_domcek[2] = "#"
                    elif plocha[(index + hod) - len(plocha)] == "&":
                        hrac2_domcek[3] = "&"
                    elif plocha[(index + hod) - len(plocha)] == "x":
                        hrac3_domcek[0] = "x"
                    elif plocha[(index + hod) - len(plocha)] == "y":
                        hrac3_domcek[1] = "y"
                    elif plocha[(index + hod) - len(plocha)] == "c":
                        hrac3_domcek[2] = "c"
                    elif plocha[(index + hod) - len(plocha)] == "v":
                        hrac3_domcek[3] = "v"
                    plocha[(index + hod) - len(plocha)] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        print("Na rade je hráč 4.")
                        print(hod)
                        hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
            else:
                x = (index + hod) - 29
                if x <= len(hrac2):
                    hrac4[x - 1] = vyber
                    plocha[index] = "O"
                    if hod == 6:
                        hod = random.randint(1, 6)
                        hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                    hrac4_domcek)
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                else:
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        elif vyber in hrac4_domcek and hod == 6:
            if plocha[30] != "1" and plocha[30] != "2" and plocha[30] != "3" and plocha[30] != "4":
                if plocha[30] == "đ":
                    hrac1_domcek[0] = "đ"
                elif plocha[30] == "Đ":
                    hrac1_domcek[1] = "Đ"
                elif plocha[30] == "ł":
                    hrac1_domcek[2] = "ł"
                elif plocha[30] == "Ł":
                    hrac1_domcek[3] = "Ł"
                elif plocha[30] == "€":
                    hrac2_domcek[0] = "€"
                elif plocha[30] == "$":
                    hrac2_domcek[1] = "$"
                elif plocha[30] == "#":
                    hrac2_domcek[2] = "#"
                elif plocha[30] == "&":
                    hrac2_domcek[3] = "&"
                elif plocha[30] == "x":
                    hrac3_domcek[0] = "x"
                elif plocha[30] == "y":
                    hrac3_domcek[1] = "y"
                elif plocha[30] == "c":
                    hrac3_domcek[2] = "c"
                elif plocha[30] == "v":
                    hrac3_domcek[3] = "v"
                index = hrac4_domcek.index(vyber)
                plocha[30] = vyber
                hrac4_domcek[index] = "-"
                hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                              hrac4_domcek)
                if hod == 6:
                    hod = random.randint(1,6)
                    hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                hrac4_domcek)
                hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                              hrac4_domcek)
                hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
            else:
                hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                            hrac4_domcek)

        else:
            hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                        hrac4_domcek)
    else:
        hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                    hrac4_domcek)




def hrac4_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek):
    if "đ" in hrac1 and "Đ" in hrac1 and "ł" in hrac1 and "Ł" in hrac1:
        print("Hráč 1 vyhral.")
    if "€" in hrac2 and "$" in hrac2 and "#" in hrac2 and "&" in hrac2:
        print("Hráč 2 vyhral.")
    if "x" in hrac3 and "y" in hrac3 and "c" in hrac3 and "v" in hrac3:
        print("Hráč 3 vyhral.")
    if "1" in hrac4 and "2" in hrac4 and "3" in hrac4 and "4" in hrac4:
        print("Hráč 4 vyhral.")
    print("Na rade je hráč 4.")
    hod = random.randint(1, 6)
    print(hod)
    if "1" not in plocha and "2" not in plocha and "3" not in plocha and "4" not in plocha:
        if hod == 6:
            nova_figurka4(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
        else:
            hod = random.randint(1, 6)
            print(hod)
            if hod == 6:
                nova_figurka4(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
            else:
                hod = random.randint(1, 6)
                print(hod)
                if hod == 6:
                    nova_figurka4(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)
                else:
                    hracia_plocha(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek,
                                  hrac4_domcek)
                    hrac1_pohyb(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)

    else:
        hrac4_vyber(hod, plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)


nova_hra(plocha, hrac1, hrac2, hrac3, hrac4, hrac1_domcek, hrac2_domcek, hrac3_domcek, hrac4_domcek)