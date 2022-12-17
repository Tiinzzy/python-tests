score = input("Enter Score: ")
fs = float(score)
if 1 >= fs >= 0.9 :
    print('A')
elif 0.9 > fs >= 0.8 :
    print('B')
elif 0.8 > fs >= 0.7 :
    print('C')
elif 0.7 > fs >= 0.6 :
    print('D')
elif fs < 0.6 :
    print('F')
else: 
    print('Error!')
    print('Value out of range')
    print('Please enter a value between 0.0 and 1.0')
    quit()