def sorting(a):
    n = len(a)
    for i in range(n):
        for j in range(0,n-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return(a)
    
arr = []

print('Enter the number of values:')
num = int(input())

print('Enter the values now:')
for v in range(num):
    ui = int(input())
    arr.append(ui)

print(f'Array before sorting is {arr}')

result = sorting(arr)

print(f'Array after sorting is {result}')