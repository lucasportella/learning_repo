from time import sleep
import emoji
for c in range(10,-1,-1): #o primeiro -1 é para contar o 0, já q o python não conta o último número
    sleep(0.5)            #o segundo -1 é para contar regressivamente
    print(c)
sleep(1)
for x in range(5):
    print(emoji.emojize(':fireworks:'),end=' ')