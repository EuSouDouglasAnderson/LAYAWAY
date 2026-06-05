import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lay Filter", layout="centered")
st.title("Lay Filter")

# Inicializa históricos
if "hist_visitante" not in st.session_state:
    st.session_state.hist_visitante = [] 
if "hist_ox1" not in st.session_state:
    st.session_state.hist_ox1 = []


def fair_odds(h, d, a):
    ph, pd_, pa = 1 / h, 1 / d, 1 / a
    s = ph + pd_ + pa
    return s - 1, s / ph, s / pd_, s / pa


tab1, tab2 = st.tabs(["Lay Visitante", "Lay 0x1"])

# ── LAY VISITANTE ────────────────────────────────────────────────────────────
with tab1:
    c1, c2, c3 = st.columns(3)
    odd_h = c1.number_input("Odd Casa",   min_value=1.01, value=2.00, step=0.01, key="v_h")
    odd_d = c2.number_input("Odd Empate", min_value=1.01, value=3.50, step=0.01, key="v_d")
    odd_a = c3.number_input("Odd Fora",   min_value=1.01, value=4.00, step=0.01, key="v_a")

    if st.button("Verificar", key="btn_v"):
        juice, fH, fD, fA = fair_odds(odd_h, odd_d, odd_a)
        pre_hd = (odd_h / odd_d) * 10000
        pre_da = (odd_d / odd_a) * 10000

        dentro = (
            pre_da >= 7710 and pre_da <= 10900 and
            pre_hd <= 7100 and
            odd_a >= 3.26 and odd_a <= 5.00 and
            odd_h >= 1.60 and odd_h <= 2.40
        )

        m1, m2, m3, m4, m5, m6 = st.columns(6)
        m1.metric("Juice",        f"{juice:.2%}")
        m2.metric("H justa",      f"{fH:.2f}")
        m3.metric("D justa",      f"{fD:.2f}")
        m4.metric("A justa",      f"{fA:.2f}")
        m5.metric("PRÉ H/D",      f"{pre_hd:.0f}")
        m6.metric("PRÉ D/A",      f"{pre_da:.0f}")

        if dentro:
            st.success("✅ Jogo dentro do padrão")
            if 3.30 <= odd_a <= 5.00:
                st.info("📌 **Punter:** odd de entrada (Lay Visitante) dentro da faixa ideal — 3.30 a 5.00.")
            else:
                st.warning(f"⚠️ **Atenção:** padrão batido, mas odd de entrada ({odd_a}) fora da faixa ideal (3.30 – 5.00).")
        else:
            st.error("❌ Jogo fora do padrão")

        st.session_state.hist_visitante.insert(0, {
            "Odd H": odd_h, "Odd D": odd_d, "Odd A": odd_a,
            "PRÉ H/D": round(pre_hd), "PRÉ D/A": round(pre_da),
            "Resultado": "✅ Dentro" if dentro else "❌ Fora"
        })

    if st.session_state.hist_visitante:
        st.divider()
        st.subheader("Histórico")
        st.dataframe(pd.DataFrame(st.session_state.hist_visitante), use_container_width=True)
        if st.button("🗑️ Limpar histórico", key="clr_v"):
            st.session_state.hist_visitante = []
            st.rerun()


# ── LAY 0X1 ──────────────────────────────────────────────────────────────────
with tab2:
    c1, c2, c3 = st.columns(3)
    odd_h = c1.number_input("Odd Casa",   min_value=1.01, value=1.51, step=0.01, key="o_h")
    odd_d = c2.number_input("Odd Empate", min_value=1.01, value=5.10, step=0.01, key="o_d")
    odd_a = c3.number_input("Odd Fora",   min_value=1.01, value=7.40, step=0.01, key="o_a")

    if st.button("Verificar", key="btn_o"):
        juice, fH, fD, fA = fair_odds(odd_h, odd_d, odd_a)
        pre_hd = (odd_h / odd_d) * 10000
        pre_da = (odd_d / odd_a) * 10000
        pre_ad = (odd_a / odd_d) * 10000

        dentro = (
            1.01 <= odd_h <= 1.99 and
            3 <= odd_d <= 100 and
            4 <= odd_a <= 100 and
            100 <= pre_hd <= 4850 and
            5000 <= pre_da <= 7710 and
            pre_ad >= 12500
        )

        m1, m2, m3, m4, m5, m6, m7 = st.columns(7)
        m1.metric("Juice",    f"{juice:.2%}")
        m2.metric("H justa",  f"{fH:.2f}")
        m3.metric("D justa",  f"{fD:.2f}")
        m4.metric("A justa",  f"{fA:.2f}")
        m5.metric("PRÉ H/D",  f"{pre_hd:.0f}")
        m6.metric("PRÉ D/A",  f"{pre_da:.0f}")
        m7.metric("PRÉ A/D",  f"{pre_ad:.0f}")

        if dentro:
            st.success("✅ Jogo dentro do padrão")
            st.info(
                "📌 **Lay 0x1 — filtro pré-jogo.** "
                "Eficiência aumenta com confirmação de campo: priorize jogos em que a casa "
                "apresente mais chutes a gol ou escanteios. "
                "Odd de entrada no mercado Lay 0x1 deve ser **≤ 25**."
            )
        else:
            st.error("❌ Jogo fora do padrão")

        st.session_state.hist_ox1.insert(0, {
            "Odd H": odd_h, "Odd D": odd_d, "Odd A": odd_a,
            "PRÉ H/D": round(pre_hd), "PRÉ D/A": round(pre_da), "PRÉ A/D": round(pre_ad),
            "Resultado": "✅ Dentro" if dentro else "❌ Fora"
        })

    if st.session_state.hist_ox1:
        st.divider()
        st.subheader("Histórico")
        st.dataframe(pd.DataFrame(st.session_state.hist_ox1), use_container_width=True)
        if st.button("🗑️ Limpar histórico", key="clr_o"):
            st.session_state.hist_ox1 = []
            st.rerun()
