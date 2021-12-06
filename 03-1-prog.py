import numpy as np

with open('03-1-input.txt', 'r') as f:
    stri = f.read()

stri = stri.strip()
liste = stri.split('\n')
length = len(liste)
n_bits = len(liste[0])  # assuming all have same length


print(liste)

occurence_0 = np.zeros(n_bits)
occurence_1 = np.zeros(n_bits)

for i in range(length):
    for j in range(n_bits):
        if liste[i][j] == '0':
            occurence_0[j] += 1
        elif liste[i][j] == '1':
            occurence_1[j] += 1
        else:
            print('liste[', i, '][', j, ']=', liste[i][j], sep='')

print(occurence_0)
print(occurence_1)

gamma_rate_binary = np.where(occurence_0 > occurence_1, 0, 1)
epsilon_rate_binary = np.where(occurence_0 < occurence_1, 0, 1)

print(gamma_rate_binary)
print(epsilon_rate_binary)

## convert to decimal number:
gamma_rate_decimal = 0
epsilon_rate_decimal = 0
power_of_2 = 1
j = n_bits-1
while j>=0:
    gamma_rate_decimal += gamma_rate_binary[j] * power_of_2
    epsilon_rate_decimal += epsilon_rate_binary[j] * power_of_2

    power_of_2 *= 2
    j -= 1

print(gamma_rate_decimal)
print(epsilon_rate_decimal)

print('----------')
print('gamma_rate * epsilon_rate = ', gamma_rate_decimal*epsilon_rate_decimal)
