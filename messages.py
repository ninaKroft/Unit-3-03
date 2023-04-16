#Create a program that solves the Beaver Computing Challenges problem.
#Letter T E  A    K    C    R
#Code   1 00 0010 0110 1010 1110
#Goal: Determine which of the 4 answers correctly deciphers the code "1001001100010100010111000"

T = "1"
E = "00"
A = "0010"
K = "0110"
C = "1010"
R = "1110"

message = "1001001100010100010111000"
teacrate = T+E+A+C+R+A+T+E
eatcake = E+A+T+C+A+K+E
takecare = T+A+K+E+C+A+R+E
retake = R+E+T+A+K+E

if message == teacrate:
    print("The message is 'teacrate'.")
elif message == eatcake:
    print("The message is 'eatcake'.")
elif message == takecare:
    print("The message is 'takecare'.")
elif message == retake:
    print("The message is: 'retake'.")

