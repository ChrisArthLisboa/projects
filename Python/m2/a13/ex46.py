from time import sleep

for c in range(10,-1,-1):
    sleep(1)  # type: ignore
    print(c)
print("BUM! BUM! POOOW!")
