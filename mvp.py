with open('conf', 'r') as imp_f:
    imp_lns = imp_f.readlines()
    fxd_lns = []
    for x in imp_lns:
        t = ''
        for i in x:
            if i != '#' and i != ';':
                t += i
            else:
                break
        fxd_lns.append(t)
        for i in range(len(fxd_lns)):
            if fxd_lns[i] == '\n' or len(fxd_lns[i]) == 0:
                del fxd_lns[i]
    fxd_lns = [x.rstrip() for x in fxd_lns]
    dct_lns = {}
    for x in fxd_lns:
        t = x.split()
        if len(t) == 1:
            dct_lns[t[0]] = 'просто существует ключ'
        else:
            dct_lns[t[0]] = ' '.join(t[1:])
    while True:
        gt_ky = input('get param ')
        try:
            print(gt_ky + ': ' + dct_lns[gt_ky])
        except:
            print('Неверный ключ')
        while True:
            a = input('Продолжить? (Да/Нет)')
            if a == 'Да':
                break
            elif a == 'Нет':
                print('До связи')
                quit()
            else:
                print('Попробуйте ввести снова (Да/Нет)')
