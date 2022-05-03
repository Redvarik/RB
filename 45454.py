terminator = ['terminator', 1, 0, 0, 0]
rais = ['rais', 1, 1, 1, 1]
cr7 = ['cr7', 1, 1, 1, 0]
kyuri = ['kyuri', 0, 1, 0, 0]
petrl = ['petrl', 1, 1, 0, 0]

sudo = [terminator, petrl, kyuri, cr7, rais]

que = ["Men?", 'реален?', 'живой?', 'идиот?']
for i in range(len(que)):
    print(que[i])
    ans = input('da / net: ')
    if ans == "da":
        ans = 1
    else:
        ans = 0
    que[i] = ans

for i in range(len(sudo)):
    r = 0
    for k in range(len(que)):
        if sudo[i][k + 1] == que[k]:
            r += 1
    if r == len(que):
        print('It', sudo[i][0])

