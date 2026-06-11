
def lay_visitante(fH, fD, fA):

    d_a = fD / fA

    return (
        0.7710 <= d_a <= 1.02 and
        1.80 <= fH <= 2.24 and
        3.00 <= fA <= 5.00
    )


def lay_0x1(
    odd_h,
    odd_d,
    odd_a,
    pre_hd,
    pre_da,
    pre_ad
):

    return (
        1.01 <= odd_h <= 1.99 and
        3.00 <= odd_d <= 100 and
        4.00 <= odd_a <= 100 and
        100 <= pre_hd <= 4850 and
        5000 <= pre_da <= 7710 and
        pre_ad >= 12500
    )
