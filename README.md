🎃 Mini‑Projeto Avaliativo — Festa em Cena (com Pandas)

📌 Resumo
Este projeto utiliza Python e Pandas para analisar o arquivo halloween_vendas.csv.
O sistema realiza Configuração e Ingestão, Transformação de Strings, Nulos e Validação e Regras de Negócio, Datas e gera automaticamente o relatório REPORT.md.

🎯 Objetivo da Análise
- Identificar problemas nos dados:
  - Categorias vazias
  - Canais inconsistentes
  - Quantidades inválidas
  - Preços ausentes ou negativos
  - Datas incorretas
- Testar a hipótese:
  Todos os pedidos sem data_entrega possuem status "Cancelado".
- Produzir relatório com:
  - Total de linhas
  - Problemas encontrados
  - Contagem por canal
  - Contagem por período (ano‑mês)
  - Hipótese sobre entregas sem data
  - Duas descobertas com interpretação e limitação

📂 Arquivos Principais
- main.py → script principal com Pandas
- halloween_vendas.csv → base de dados
- REPORT.md → relatório gerado automaticamente
- README.md → documentação do projeto

🗂️ Significado dos Dados
- Linha: representa um pedido
- pedido_id: identificador único
- categoria: tipo de produto (fantasia, acessório)
- canal_venda: Mercado, Loja física ou Web
- data_venda: data e hora da compra (YYYY-MM-DD HH:MM:SS)

⚙️ Regras Aplicadas
- Categorias: .strip(), .lower(), regex; se vazias → "sem categoria"
- Canal: padronizado para Mercado, Loja física ou Web
- Quantidade: inteiro > 0
- Preço: número ≥ 0
- Data venda: convertida com pd.to_datetime; inválidas são marcadas
- Data entrega vazia: verificar se status == "Cancelado"; listar contraexemplos

▶️ Como Executar
1. Instale Pandas:
   pip install pandas
2. Coloque halloween_vendas.csv na mesma pasta.
3. Rode:
   python main_pandas.py
4. Abra REPORT.md para ver o relatório.

📊 Saída Esperada
O REPORT.md apresenta:
- Total de linhas lidas
- Problemas por campo
- Contagem por canal
- Contagem por período (ano‑mês)
- Hipótese sobre entregas sem data
- Duas descobertas com interpretação e limitação

🏗️ Organização das Tarefas
- Sprint 1 — Configuração e Ingestão
- Sprint 2 — Transformação de Strings
- Sprint 3 — Nulos e Validação
- Sprint 4 — Regras de Negócio, Datas e Relatório

Branches criadas:
- sprint1-configuracao_e_ingestao
- sprint2-transformacao_de_strings
- sprint3-nulos_e_validacao
- sprint4-regras_de_negocio_datas_e_relatorio

🚀 Melhorias Futuras
- Salvar também um CSV com registros marcados
- Adicionar testes automatizados
- Criar logs de execução
- Comparar versão sem Pandas e com Pandas

📦 Entregáveis
Repositório no GitHub contendo:
- main_pandas.py
- funcoes.py
- halloween_vendas.csv
- README.md
- REPORT.md
- .gitignore