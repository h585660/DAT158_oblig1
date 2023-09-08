#oppgave 2b

def boyer_moore_search_with_count(p, t):
    m, n = len(p), len(t)
    antall_sammenligninger = 0  
    
    
    siste_bokstav = {}
    for i in range(m):
        siste_bokstav[p[i]] = i
    
    i = m - 1  # pekeren for teksten
    j = m - 1  # pekeren for mønsteret
    
    while i < n:
        antall_sammenligninger += 1  
        if t[i] == p[j]:
            if j == 0:
                return i, antall_sammenligninger  # mønster funnet
            else:
                i -= 1
                j -= 1
        else:
            i = i + m - min(j, 1 + siste_bokstav.get(t[i], -1))
            j = m - 1
    
    return -1, antall_sammenligninger  # mønster ikke funnet

# utskrift
tekst = norsk_tekst = """
Settinntekstendinher
"""
mønster = "tekst"

resultat, antall_sammenligninger = boyer_moore_search_with_count(mønster, tekst)
print(f"Funnet ved indeks {resultat}, sammenligninger: {antall_sammenligninger}, per teksttegn blir det: {antall_sammenligninger / len(tekst):.2f}")

