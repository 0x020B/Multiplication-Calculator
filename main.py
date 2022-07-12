x, y = input().split('x')
a = str(int(x) * int(y))
b = []
t = l = len(a) * 2 + 1
print(f'{" ".join(x):>{l}}')
print(f'x {" ".join(y):>{l-2}}')
print('-'*l)
x, y = int(x), list(map(int, y))
c = [str(x*i) for i in y[::-1]]
for i in c:
    print(f'{" ".join(i):>{t}}')
    t -= 2
for i, _ in enumerate(c):
    c[i] += '0'*i
    c[i] = f'{c[i]:0>{l//2}}'
t = 0
for i in list(zip(*c))[::-1]:
    t += sum(map(int, i))
    if t < 10:
        t = '00'
    t = int(str(t)[:-1])
    b.append(t if t else ' ')
b.reverse()
print(f'{" ".join(map(str, b)):>{l-1}}')
print('-'*l)
print(f'{" ".join(a):>{l}}')
