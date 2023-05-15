def prob_red_from_urn(N, K, g, r):
    n = N - r - g
    k1 = K - r
    k2 = K - g
    py = 0.5
    if g > K or r > N-K:
        py = 1
    if r > K or g > N-K:
        py = 0
    px_given_1 = 0 if n == 0 else py * k1 / n
    px_given_2 = 0 if n == 0 else (1 - py) * (n - k2) / n
    px = px_given_1 + px_given_2
    return px


def prob_red_from_1_urn(N, K, g, r):
    px = (K-r)/(N-g-r)
    return px


def calc_tokens(p, m):
    f = 2 * p - 1
    v = min(max(f * m, 1), m)
    return round(v)


def bet(N, K, m, g1, r1, g2, r2,b):
    if N == g1 + r1:
        if g1 == K:
            p_r2 = prob_red_from_1_urn(N, K, g2, r2)
        else:
            p_r2 = prob_red_from_1_urn(N, N-K, g2, r2)
    else:
        p_r2 = prob_red_from_urn(N, K, g2, r2)

    if N == g2 + r2:
        p_r2 = -1
        if g2 == K:
            p_r1 = prob_red_from_1_urn(N, K, g1, r1)
        else:
            p_r1 = prob_red_from_1_urn(N, N - K, g1, r1)
    else:
        p_r1 = prob_red_from_urn(N, K, g1, r1)

    if N == g1 + r1:
        p_r1 = -1

    if p_r1 == -1:
        p_r1 = p_g1 = 0
    else:
        p_g1 = 1 - p_r1
    if p_r2 == -1:
        p_r2 = p_g2 = 0
    else:
        p_g2 = 1 - p_r2

    maxi = max(p_r1, p_r2, p_g1, p_g2)
    if maxi == p_r1:
        return (calc_tokens(p_r1, m), True, True)
    if maxi == p_r2:
        return (calc_tokens(p_r2, m), False, True)
    if maxi == p_g1:
        return (calc_tokens(p_g1, m), True, False)
    if maxi == p_g2:
        return (calc_tokens(p_g2, m), False, False)
