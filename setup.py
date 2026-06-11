import os

# =========================
# ESTRUTURA DO PROJETO
# =========================

project_name = "davs-trader"

folders = [
    project_name,
    f"{project_name}/src"
]

files = {
    f"{project_name}/app.py": "",
    f"{project_name}/requirements.txt": "streamlit\npandas\n",
    f"{project_name}/src/__init__.py": "",
    f"{project_name}/src/odds.py": """def fair_odds(h, d, a):
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
""",
    f"{project_name}/src/rules.py": """def lay_visitante(fH, fD, fA):
    d_a = fD / fA

    return (
        0.7710 <= d_a <= 1.02 and
        1.80 <= fH <= 2.24 and
        3.00 <= fA <= 5.00
    )


def lay_0x1(odd_h, odd_d, odd_a, pre_hd, pre_da, pre_ad):
    return (
        1.01 <= odd_h <= 1.99 and
        3.00 <= odd_d <= 100 and
        4.00 <= odd_a <= 100 and
        100 <= pre_hd <= 4850 and
        5000 <= pre_da <= 7710 and
        pre_ad >= 12500
    )
"""
}

# =========================
# CRIA PASTAS
# =========================

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# =========================
# CRIA ARQUIVOS
# =========================

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Projeto davs-trader criado com sucesso!")
print("👉 Entre na pasta: cd davs-trader")
print("👉 Rode: streamlit run app.py")
