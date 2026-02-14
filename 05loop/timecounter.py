import time

myTime=int (input('Enter time in seconds: '))

# for x in range(0 ,myTime):
#     print(x)
#     time.sleep(1)
# print('times up')



# for x in reversed(range(0 ,myTime)):
#     print(x)
#     time.sleep(1)
# print('times up')


# for x in range(myTime,0,-1):
#     print(x)
#     time.sleep(1)
# print('times up')


for x in range(1,myTime):
    seconds= x %60
    minutes= int(x/60)%60
    hours= int(x/3600)
    print(f'00:{minutes:02}:{seconds:02}')
    time.sleep(1)
print('times up')