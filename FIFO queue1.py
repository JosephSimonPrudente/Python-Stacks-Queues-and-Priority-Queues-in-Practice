from queues import Queue1

fifo = Queue1("1st", "2nd", "3rd")
print(len(fifo))
print("_______________________________")

for element in fifo:
    print(element)

print("_______________________________")
print(len(fifo))
