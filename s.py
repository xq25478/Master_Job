def Solution(graph):
    def find(x):
        while x != uf[x]:
            x = uf[x]
        return x

    hash = {}
    uf = [i for i in range(1000)]
    cnt = 0
    if not graph:
        return 0

    for g in graph:
        a,b = '',''
        for ch in g:
            if ch != '-':
                a += ch
            else:
                break
        for ch in reversed(g):
            if ch != '>':
                b += ch
            else:
                break
        if a not in  hash:
            hash[a] = cnt 
            cnt += 1
        if b not in hash:
            hash[b] = cnt 
            cnt += 1

        uf[hash[b]] = hash[a]

        if find(uf[hash[a]]) == hash[b]:
            return -1

    return 0

print(Solution(['A->B','B->C','C->A']))

    

    
    

        
        
      
        
    

        


