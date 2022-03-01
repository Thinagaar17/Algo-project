
positive = open("C:/Users/user/PycharmProjects/Assignment/wordlist/list of positive words.txt")
negative = open("C:/Users/user/PycharmProjects/Assignment/wordlist/list of negative words.txt")

p = positive.read().split(',')
for i in range(len(p)):
    if p[i][0] == ' ':
        p[i] = p[i][1:]
for i in range(len(p)):
    p[i] = p[i].lower()

positive2 = open("C:/Users/user/PycharmProjects/Assignment/wordlist/positivewords.txt", 'w', encoding='utf-8')
[positive2.write(word + '\n') for word in p]

n = negative.read().split(',')
for i in range(len(n)):
    if n[i][0] == ' ':
        n[i] = n[i][1:]
negative2 = open("C:/Users/user/PycharmProjects/Assignment/wordlist/negativewords.txt", 'w', encoding='utf-8')
[negative2.write(word + '\n') for word in n]

print(p)

positive.close()
positive2.close()
negative.close()
negative2.close()
