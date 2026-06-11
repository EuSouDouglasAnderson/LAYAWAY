import streamlit as st
import pandas as pd

from src.odds import fair_odds
from src.rules import lay_visitante, lay_0x1

# ==================================================
# CONFIGURAÇÃO
# ==================================================

st.set_page_config(
    page_title="Davs Trader",
    layout="centered"
)

st.title("Filtro de Jogos")

# ==================================================
# HISTÓRICO
# ==================================================

if "historico" not in st.session_state:
    st.session_state.historico = []

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

    # Odds Justas
    juice, fH, fD, fA = fair_odds(
        odd_h,
        odd_d,
        odd_a
    )

    # Ratios do Lay 0x1
    pre_hd = (odd_h / odd_d) * 10000
    pre_da = (odd_d / odd_a) * 10000
    pre_ad = (odd_a / odd_d) * 10000

    # Regras
    lv = lay_visitante(
        fH,
        fD,
        fA
    )

    l01 = lay_0x1(
        odd_h,
        odd_d,
        odd_a,
        pre_hd,
        pre_da,
        pre_ad
    )

    # Resultado
    if lv and l01:
        resultado = "Lay Visitante + Lay 0x1"
        st.success("✅ Lay Visitante + Lay 0x1")

    elif lv:
        resultado = "Lay Visitante"
        st.success("✅ Lay Visitante")

    elif l01:
        resultado = "Lay 0x1"
        st.success("✅ Lay 0x1")

    else:
        resultado = "Fique de Fora"
        st.error("🚫 Fique de Fora")

    # Histórico
    st.session_state.historico.insert(
        0,
        {
            "Odd H": odd_h,
            "Odd D": odd_d,
            "Odd A": odd_a,
            "Resultado": resultado
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
