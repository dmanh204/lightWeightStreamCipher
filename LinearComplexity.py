def runTest(arr):
    N = len(arr)
    b = [0]*N
    c = [0]*N

    b[0] = 1
    c[0] = 1
    l = 0
    m = -1
    for n in range(N):
        d = 0
        for i in range(l+1):
            d ^= (c[i] * arr[n-i])
        if d== 1:
            t = c.copy()
            N_M = n-m
            for j in range(N-N_M):
                c[N_M +j] ^= b[j]
            if(l<= n/2):
                l = n+1 -l
                m = n
                b = t.copy()
        
    return l