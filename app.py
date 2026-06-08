import streamlit as st

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
