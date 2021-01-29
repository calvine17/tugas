import sys
str1 = "23"
b = a = c = 0

for line in sys.stdin:
    str1 = line
    for z in range(len(str1)):
        if((str1[z] >= 'a' and str1[z] <= 'z') or (str1[z] >= 'A' and str1[z] <= 'Z')): 
            b = b + 1 
        elif(str1[z] >= '0' and str1[z] <= '9'):
            a = a + 1
        else:
            c = c + 1

sys.stdout.write("Total angka: " + str(a))
sys.stdout.write('\n')
sys.stdout.write("Total huruf: " + str(b))
sys.stdout.write('\n')
sys.stdout.write("Total symbol: " + str(c))
sys.stdout.write('\n')
