import streamlit as st

def verifica_lay_visitante(odd_h, odd_d, odd_a):
    p_h = 1 / odd_h
    p_d = 1 / odd_d
    p_a = 1 / odd_a
    p_sum = p_h + p_d + p_a

    odd_h_justa = p_sum / p_h
    odd_d_justa = p_sum / p_d
    odd_a_justa = p_sum / p_a

    Soma = p_sum - 1

    # Variáveis no mesmo formato do notebook (× 10000)
    pre_hd = (odd_h / odd_d) * 10000
    pre_da = (odd_d / odd_a) * 10000

    dentro = (
        (pre_da >= 7710) and (pre_da <= 10110) and
        (pre_hd <= 7100) and
        (odd_a >= 3.26) and (odd_a <= 5.00) and
        (odd_h >= 1.60) and (odd_h <= 2.40)
    )

    st.write(f"JUICE: {Soma:.2f}")
    st.write(f"Odd_H_Justa: {odd_h_justa:.2f}")
    st.write(f"Odd_D_Justa: {odd_d_justa:.2f}")
    st.write(f"Odd_A_Justa: {odd_a_justa:.2f}")
    st.write(f"PRÉ_H/D: {pre_hd:.0f}")
    st.write(f"PRÉ_D/A: {pre_da:.0f}")

    if dentro:
        st.success("✅ JOGO DENTRO DO PADRÃO")
    else:
        st.error("❌ JOGO FORA DO PADRÃO")

# --- Interface ---
st.title("Lay Visitante")

odd_h = st.number_input("Odd Casa",   min_value=1.01, value=2.00, step=0.01)
odd_d = st.number_input("Odd Empate", min_value=1.01, value=3.50, step=0.01)
odd_a = st.number_input("Odd Fora",   min_value=1.01, value=4.00, step=0.01)

if st.button("Verificar"):
    verifica_lay_visitante(odd_h, odd_d, odd_a)
