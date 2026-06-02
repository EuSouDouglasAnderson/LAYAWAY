import streamlit as st

def verifica_lay_visitante(odd_h, odd_d, odd_a):
    p_h = 1 / odd_h
    p_d = 1 / odd_d
    p_a = 1 / odd_a
    p_sum = p_h + p_d + p_a

    odd_h_justa = p_sum / p_h
    odd_d_justa = p_sum / p_d
    odd_a_justa = p_sum / p_a
    Soma = odd_h_justa + odd_d_justa + odd_a_justa

    h_d = odd_h_justa / odd_d_justa
    d_a = odd_d_justa / odd_a_justa

    dentro = (
        (1.60 <= odd_h_justa <= 2.40) and
        (3.30 <= odd_a_justa <= 5.00) and
        (0.7710 < d_a <= 1) and
        (h_d < 0.71)
    )
    st.write(f"Odd_A_Justa: {Soma:.2f}")
    st.write(f"Odd_H_Justa: {odd_h_justa:.2f}")
    st.write(f"Odd_D_Justa: {odd_a_justa:.2f}")
    st.write(f"Odd_A_Justa: {odd_a_justa:.2f}")
    st.write(f"D_A: {d_a:.4f}")
    st.write(f"H_D: {h_d:.4f}")

    if dentro:
        st.success("✅ JOGO DENTRO DO PADRÃO")
    else:
        st.error("❌ JOGO FORA DO PADRÃO")

# --- Interface ---
st.title("Lay Visitante")

odd_h = st.number_input("Odd Casa",    min_value=1.01, value=2.00, step=0.01)
odd_d = st.number_input("Odd Empate",  min_value=1.01, value=3.50, step=0.01)
odd_a = st.number_input("Odd Fora",    min_value=1.01, value=4.00, step=0.01)

if st.button("Verificar"):
    verifica_lay_visitante(odd_h, odd_d, odd_a)
