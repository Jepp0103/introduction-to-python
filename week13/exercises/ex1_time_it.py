import time

start = time.time()
# do some stuff you want to meassure here
for i in range(1000):
    print(i)
end = time.time()
print(end - start, "seconds")   