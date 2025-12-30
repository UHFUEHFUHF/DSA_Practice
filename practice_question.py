n = [5,3,2,2,1,5,5,7,5,10]
m = [10 , 11 , 1, 9 , 5 , 67 ,2]

freq_n = {}

for num in n:
    if num in freq_n:
        freq_n[num] += 1
    else:
        freq_n[num] = 1

answers = []
for mum in m:
    if mum in n:
        answers.append(freq_n[mum])
    else:
        answers.append(0)

print(answers)
