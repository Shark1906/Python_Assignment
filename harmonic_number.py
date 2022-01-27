print('Enter the number of flipcoin')
n = input()
harmonic_num = 0

for i in range(1, int(n)+1):
    temp = 1/i
    harmonic_num += temp

print('Harmonic number at nth term', n ,'is', harmonic_num)