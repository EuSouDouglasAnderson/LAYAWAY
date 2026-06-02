def verifica_lay_visitante(odd_h, odd_d, odd_a):

    # Probabilidades implícitas
    p_h = 1 / odd_h
    p_d = 1 / odd_d
    p_a = 1 / odd_a

    p_sum = p_h + p_d + p_a

    # Odds justas
    odd_h_justa = p_sum / p_h
    odd_d_justa = p_sum / p_d
    odd_a_justa = p_sum / p_a

    # Variáveis
    h_d = odd_h_justa / odd_d_justa
    d_a = odd_d_justa / odd_a_justa

    # Filtro
    dentro = (
        (1.60 <= odd_h_justa <= 2.40) and
        (3.30 <= odd_a_justa <= 5.00) and
        (0.7710 <= d_a <= 1) and
        (h_d <= 0.70)
    )

    print(f"Odd_H_Justa: {odd_h_justa:.2f}")
    print(f"Odd_A_Justa: {odd_a_justa:.2f}")
    print(f"D_A: {d_a:.4f}")
    print(f"H_D: {h_d:.4f}")

    if dentro:
        print("\n✅ JOGO DENTRO DO PADRÃO")
    else:
        print("\n❌ JOGO FORA DO PADRÃO")