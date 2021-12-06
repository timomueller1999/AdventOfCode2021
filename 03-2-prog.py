
import numpy as np
import pdb  # Python debugger

with open('03-2-input.txt', 'r') as f:
    stri = f.read()

stri = stri.strip()
liste = stri.split('\n')
length = len(liste)
n_bits = len(liste[0])  # assuming all have same length

## first find the oxygen generator rating
still_in_liste_ogr = np.ones(length)

for position in range(n_bits):
    occurence_0 = 0
    occurence_1 = 0

    for iter in range(length):
        if still_in_liste_ogr[iter]==0:
            continue

        elem = liste[iter]

        if elem[position] == '0':
            occurence_0 += 1
        elif elem[position] == '1':
            occurence_1 += 1
        else:
            print('Mind the non-binary element', elem)

    # print('occurence_0=', occurence_0, sep='')
    # print('occurence_1=', occurence_1, sep='')

    for iter in range(length):
        if liste[iter][position]=='1' and occurence_0 > occurence_1:
            still_in_liste_ogr[iter] = 0
        if liste[iter][position]=='0' and occurence_0 <= occurence_1:
            still_in_liste_ogr[iter] = 0

    # print(still_in_liste_ogr)

    # print('remaining liste:')
    # for iter in range(length):
    #     if still_in_liste_ogr[iter]==1:
    #         print(liste[iter], end='\t')
    # print()

    if still_in_liste_ogr.sum() <= 1:
    #     print('Only', still_in_liste_ogr.sum(), 'element left in liste.')
    #     print('Current position:', position)
        break;

index = still_in_liste_ogr.argmax()
ogr_binary = liste[index]
print('Oxygen generating rate binary = ', ogr_binary)



## now compute the CO2 scrubber rating
still_in_liste_csr = np.ones(length)

for position in range(n_bits):
    occurence_0 = 0
    occurence_1 = 0

    for iter in range(length):
        if still_in_liste_csr[iter]==0:
            continue

        elem = liste[iter]

        if elem[position] == '0':
            occurence_0 += 1
        elif elem[position] == '1':
            occurence_1 += 1
        else:
            print('Mind the non-binary element', elem)

    # print('occurence_0=', occurence_0, sep='')
    # print('occurence_1=', occurence_1, sep='')

    for iter in range(length):
        if liste[iter][position]=='0' and occurence_0 > occurence_1:
            still_in_liste_csr[iter] = 0
        if liste[iter][position]=='1' and occurence_0 <= occurence_1:
            still_in_liste_csr[iter] = 0

    # print(still_in_liste_csr)

    # print('remaining liste:')
    # for iter in range(length):
    #     if still_in_liste_csr[iter]==1:
    #         print(liste[iter], end='\t')
    # print()

    if still_in_liste_csr.sum() <= 1:
    #     print('Only', still_in_liste_csr.sum(), 'element left in liste.')
    #     print('Current position:', position)
        break;

index = still_in_liste_csr.argmax()
csr_binary = liste[index]
print('CO2 scrubber rate binary = ', csr_binary)






## convert to decimal number:
ogr_decimal = 0
csr_decimal = 0
power_of_2 = 1
j = n_bits-1
while j>=0:
    ogr_decimal += int(ogr_binary[j]) * power_of_2
    csr_decimal += int(csr_binary[j]) * power_of_2

    power_of_2 *= 2
    j -= 1

print('Oxygen generating rate decimal = ', ogr_decimal)
print('CO2 scrubber rate decimal = ', csr_decimal)

print('Life support rating = ', ogr_decimal*csr_decimal)
