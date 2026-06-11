
def fair_odds(h, d, a):
    ph = 1 / h
    pd_ = 1 / d
    pa = 1 / a

    s = ph + pd_ + pa

    return (
        s - 1,
        s / ph,
        s / pd_,
        s / pa
    )
