CSV = "halloween_vendas.csv"
REPORT = "REPORT.md"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def main():
    df = pd.read_csv(CSV, encoding="utf-8")

def limpar_categoria(s):
    if pd.isna(s) or str(s).strip() == "":
        return "sem categoria"
    t = str(s).strip().lower()
    t = re.sub(r"[^a-z\s]", "", t)
    t = " ".join(t.split())
    return t if t else "sem categoria"

def padronizar_canal(s):
    if pd.isna(s):
        return None
    t = str(s).strip().lower()
    if "mercado" in t:
        return "Mercado"
    if "loja" in t:
        return "Loja física"
    if "web" in t:
        return "Web"
    return None

# aplicação das funções no DataFrame
df["categoria_limpa"] = df["categoria"].apply(limpar_categoria)
df["canal_pad"] = df["canal_venda"].apply(padronizar_canal)
