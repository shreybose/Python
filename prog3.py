# Written by Sarayu Das and Shreya Bose
import sys
with open(sys.argv[1], 'r') as f:
    contents = f.read()
    contents = contents.split(" ")
    a = int(contents[0])
    b = int(contents[1])
    prime = int(contents[2])

count = 0
possib = []
for num1 in range(0, prime-1):
    for num2 in range(0, prime-1):
        val = num1**3 + num1*a + b
        val1 = num2**2 % prime
        if (val == val1):
            x1 = num1
            y1 = num2
            z1 = 1
            possib.append([x1, y1, z1])
            x = possib[0][0]
            y = possib[0][1]
            z = possib[0][2]

co = (x, y, z)
list = []
list.append(co)

# doubling
A = (y**2) % prime
B = (4*x*A) % prime
C = (8*(A**2)) % prime
D = (3*(x**2) + a*(z**4)) % prime
x_jacob = (D**2 - (2 * B)) % prime
y_jacob = ((D * (B - x_jacob)) - C) % prime
z_jacob = (2*y*z) % prime

jacobList = (x_jacob, y_jacob, z_jacob)

list.append(jacobList)

# adding
def adding(x_param, y_param, z_param):
    A1 = (z_param**2) % prime
    B1 = (z_param*A1) % prime
    C1 = (x*A1) % prime
    D1 = (y*B1) % prime
    E1 = (C1 - x_param) % prime
    F1 = (D1 - y_param) % prime
    G1 = (E1**2) % prime
    H1 = (G1*E1) % prime
    I1 = (x_param * G1) % prime
    xadd = ((F1**2) - H1 - (2*I1)) % prime
    yadd = ((F1 * (I1-xadd)) - (y_param*H1)) % prime
    zadd = (z_param*E1) % prime

    return xadd, yadd, zadd


x1, y1, z1 = adding(x_jacob, y_jacob, z_jacob)
tempList = (x1, y1, z1)


def egcd (a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


# multi inverse
def modinv (a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def moddiv (a, b, p):
    b_inv = modinv(b, p)
    return (a*b_inv) % p


# main method
i = 1
new_C = -1
list2 = []
list2.append(i)
while new_C != 0:
    tempList = list[i]
    tempA, tempB, tempC = tempList[0], tempList[1], tempList[2]
    new_A, new_B, new_C = adding(tempA, tempB, tempC)
    tempListB = (new_A, new_B, new_C)
    list.append(tempListB)
    i += 1
    list2.append(i)
list2.append(i+1)
print("CURVE      {}    {}   {}     ORDER = POINT (   {}   {}   {}   )  ". format(prime, a, b, x, y, z))
print("MAXORDPT   {}    {}   {}     ORDER = POINT (   {}   {}   {}   )  ". format(prime, a, b, x, y, z))
count = 1
for item in list:
    z = item[2]
    if z != 0:
        a = moddiv(item[0], pow(z, 2), prime)
        b = moddiv(item[1], pow(z, 3), prime)
        c = 1
        converted_item = (a, b, c)
        print("POW   {} POINT: {}  ->  POINT: {}".format(count, item, converted_item))
    else:
        print("POW   {} POINT: {}  ->  POINT: {}".format(count, item, item))
    count += 1
order = count - 1




