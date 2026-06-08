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

    juice, fH, fD, fA = fair_odds(odd_h, odd_d, odd_a)

    pre_hd = (odd_h / odd_d) * 10000
    pre_da = (odd_d / odd_a) * 10000
    pre_ad = (odd_a / odd_d) * 10000

    # ==========================================
    # DISTÂNCIA EUCLIDIANA
    # ==========================================

    ponto_hd = 5000
    ponto_da = 8000

    dist = math.sqrt(
        (pre_hd - ponto_hd) ** 2 +
        (pre_da - ponto_da) ** 2
    )

    # ==========================================
    # FILTRO LAY VISITANTE
    # ==========================================

    lay_v = (
        pre_da >= 7710 and pre_da <= 10900 and
        pre_hd < 7100 and
        odd_a >= 3.26 and odd_a <= 5.00 and
        odd_h >= 1.60 and odd_h <= 2.40 and
        dist < 2300
    )

    # ==========================================
    # FILTRO LAY 0X1
    # ==========================================

    lay_0x1 = (
        1.01 <= odd_h <= 1.99 and
        3.00 <= odd_d <= 100 and
        4.00 <= odd_a <= 100 and
        100 <= pre_hd <= 4850 and
        5000 <= pre_da <= 7710 and
        pre_ad >= 12500
    )

    # ==========================================
    # MÉTRICAS
    # ==========================================

    st.subheader("Mercado")

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    r1c1.metric("Juice", f"{juice:.2%}")
    r1c2.metric("H Justa", f"{fH:.2f}")
    r1c3.metric("D Justa", f"{fD:.2f}")
    r1c4.metric("A Justa", f"{fA:.2f}")

    st.subheader("Indicadores")

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)

    r2c1.metric("PRÉ H/D", f"{pre_hd:.0f}")
    r2c2.metric("PRÉ D/A", f"{pre_da:.0f}")
    r2c3.metric("PRÉ A/D", f"{pre_ad:.0f}")
    r2c4.metric("DIST", f"{dist:.0f}")

    st.divider()

    # ==========================================
    # RESULTADO
    # ==========================================

    if lay_v and lay_0x1:

        st.success("✅ Lay Visitante")
        st.info("📌 Punter: odd de entrada entre 3.30 e 5.00")

        st.success("✅ Lay 0x1")
        st.info(
            "📌 Lay 0x1 — filtro pré-jogo. "
            "Confirme campo: chutes ou escanteios a favor da casa. "
            "Odd de entrada ≤ 25."
        )

    elif lay_v:

        st.success("✅ Lay Visitante")

        if 3.30 <= odd_a <= 5.00:
            st.info(
                "📌 Punter: odd de entrada dentro da faixa ideal "
                "(3.30 a 5.00)."
            )
        else:
            st.warning(
                f"⚠️ Padrão encontrado, mas odd ({odd_a:.2f}) "
                "fora da faixa ideal."
            )

    elif lay_0x1:

        st.success("✅ Lay 0x1")
        st.info(
            "📌 Filtro pré-jogo. "
            "Confirme campo: chutes ou escanteios a favor da casa. "
            "Odd de entrada ≤ 25."
        )

    else:

        st.error("🚫 Fique de Fora")

    # ==========================================
    # HISTÓRICO
    # ==========================================

    indicacao = []

    if lay_v:
        indicacao.append("Lay Visitante")

    if lay_0x1:
        indicacao.append("Lay 0x1")

    if not indicacao:
        indicacao.append("Stay Out")

    st.session_state.historico.insert(
        0,
        {
            "Odd H": odd_h,
            "Odd D": odd_d,
            "Odd A": odd_a,
            "DIST": round(dist),
            "Indicação": " + ".join(indicacao),
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
