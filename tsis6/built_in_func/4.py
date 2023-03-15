import time
print("enter n")
n=int(input())
print("enter ms")
tm=float(input())
time.sleep(tm/1000)
print("Square root of {} after {} miliseconds is {}".format(n,tm,n**0.5))