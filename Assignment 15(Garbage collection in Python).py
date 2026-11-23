
import gc
import time

class Demo:
    def __init__(self, name):
        self.name = name

gc.disable()

print("Garbage collection disabled")

objects = []

for i in range(10000):
    objects.append(Demo(i))

print("Objects created:", len(objects))

objects = None

print("Objects deleted")

start = time.time()

collected = gc.collect()

end = time.time()

print("Garbage collected:", collected)
print("Time taken:", end - start)

gc.enable()

print("Garbage collection enabled")
