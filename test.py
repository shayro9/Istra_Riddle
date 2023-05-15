def bet(N, K, m, g1, r1, g2, r2):
    n1 = N - g1 - r1
    n2 = N - g2 - r2

    if K >= N/2:
        if r1 == K:
            return (m, True, False)  #G1 = 100%
        if r2 == K:
            return (m, False, False)  #G2 = 100%
        if g2 == K:
            return (m, False, True)  #R2 = 100%
        if g1 == K:
            return (m, True, True)  #R1 = 100%
    else:
        if r1 == N-K:
            return (m, True, False)  # G1 = 100%
        if r2 == N-K:
            return (m, False, False)  # G2 = 100%
        if g2 == N-K:
            return (m, False, True)  # R2 = 100%
        if g1 == N-K:
            return (m, True, True)  # R1 = 100%


