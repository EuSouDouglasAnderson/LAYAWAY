import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="Davs Trader", layout="centered")
st.title("Filtro de Jogos")

# ==================================================
# HISTÓRICO
# ==================================================

if "historico" not in st.session_state:
    st.session_state.historico = []

# ==================================================
# FUNÇÕES
# ==================================================

def fair_odds(h, d, a):
    ph, pd_, pa = 1 / h, 1 / d, 1 / a
    s = ph + pd_ + pa
    return s - 1, s / ph, s / pd_, s / pa

# ==================================================
# INPUTS
# ==================================================

c1, c2, c3 = st.columns(3)

odd_h = c1.number_input(
    "Odd Casa",
    min_value=1.01,
    value=2.00,
    step=0.01
)

odd_d = c2.number_input(
    "Odd Empate",
    min_value=1.01,
    value=3.50,
    step=0.01
)

odd_a = c3.number_input(
    "Odd Fora",
    min_value=1.01,
    value=4.00,
    step=0.01
)

# ==================================================
# PROCESSAMENTO
# ==================================================

if st.button("Verificar", use_container_width=True):

    # Cálculos internos (não exibidos)
    juice, fH, fD, fA = fair_odds(odd_h, odd_d, odd_a)

    pre_hd = (odd_h / odd_d) * 10000
    pre_da = (odd_d / odd_a) * 10000
    pre_ad = (odd_a / odd_d) * 10000

    ponto_hd = 5000
    ponto_da = 8000

    dist = math.sqrt(
        (pre_hd - ponto_hd) ** 2 +
        (pre_da - ponto_da) ** 2
    )

    # ==================================================
    # FILTRO LAY VISITANTE
    # ==================================================

    lay_v = (
        7710 <= pre_da <= 10900 and
        pre_hd < 7100 and
        3.26 <= odd_a <= 5.00 and
        1.60 <= odd_h <= 2.40 and
        dist < 2300
    )

    # ==================================================
    # FILTRO LAY 0X1
    # ==================================================

    lay_0x1 = (
        1.01 <= odd_h <= 1.99 and
        3.00 <= odd_d <= 100 and
        4.00 <= odd_a <= 100 and
        100 <= pre_hd <= 4850 and
        5000 <= pre_da <= 7710 and
        pre_ad >= 12500
    )

    # ==================================================
    # RESULTADO
    # ==================================================

    if lay_v and lay_0x1:
        resultado = "Lay Visitante + Lay 0x1"
        st.success("✅ Lay Visitante + Lay 0x1")

    elif lay_v:
        resultado = "Lay Visitante"
        st.success("✅ Lay Visitante")

    elif lay_0x1:
        resultado = "Lay 0x1"
        st.success("✅ Lay 0x1")

    else:
        resultado = "Fique de Fora"
        st.error("🚫 Fique de Fora")

    # ==================================================
    # HISTÓRICO
    # ==================================================

    st.session_state.historico.insert(
        0,
        {
            "Odd H": odd_h,
            "Odd D": odd_d,
            "Odd A": odd_a,
            "Resultado": resultado,
        }
    )

# ==================================================
# HISTÓRICO
# ==================================================

if st.session_state.historico:

    st.divider()
    st.subheader("Histórico")

    st.dataframe(
        pd.DataFrame(st.session_state.historico),
        use_container_width=True
    )

    if st.button("🗑️ Limpar histórico"):
        st.session_state.historico = []
        st.rerun()
