import chestii

output = open("rezultate.txt", "w")

#luam input de la un user cat a investit si la ce rata de return
#apoi deschidem un fisier text unde sa fie scrise datele intr-un tabel

ani = input("Cati ani doriti sa tineti investitia?: ")
rata_retur = input("Introduceti rata de retur (ex. 10% = 0.1): ")
suma_initiala = input("Introduceti suma care a fost investita initial: ")
output.write("anul retur retur_total suma_totala\n")
retur_int = chestii.calcul_retur(int(suma_initiala), float(rata_retur))
retur_total_int = chestii.calcul_retur(int(suma_initiala), float(rata_retur))
suma_totala_int = int(suma_initiala) + chestii.calcul_retur(int(suma_initiala), float(rata_retur))

#output.write(str(1))
#output.write("     ")
#output.write(str(chestii.calcul_retur(int(suma_initiala), float(rata_retur))))
#output.write("     ")
#output.write(str(chestii.calcul_retur(int(suma_initiala), float(rata_retur))))
#output.write("     ")
#output.write(str(int(suma_initiala) + chestii.calcul_retur(int(suma_initiala), float(rata_retur))))

for i in range (1,int(ani)+1):
    output.write(str(i))
    output.write("   ")
    output.write(str('{0:.2f}'.format(retur_int)))
    output.write("   ")
    output.write(str('{0:.2f}'.format(retur_total_int)))
    output.write("   ")
    output.write(str('{0:.2f}'.format(suma_totala_int)))
    output.write("\n")
    retur_int = chestii.calcul_retur(suma_totala_int, float(rata_retur))
    retur_total_int += retur_int
    suma_totala_int += retur_int
    