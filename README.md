📊 Introdução aos Softwares Estatísticos: Python para Visualização e Aceleração Computacional







































Trabalho acadêmico desenvolvido para a disciplina de Introdução aos Softwares Estatísticos do Centro de Ciências Exatas e da Natureza (CCEN) da Universidade Federal da Paraíba (UFPB).

🎯 Visão Geral

Este projeto explora ferramentas fundamentais do ecossistema Python para ciência de dados, focando em duas dimensões críticas:

•
📈 Visualização de Dados: Comparação entre paradigmas imperativo (Matplotlib) e declarativo (Plotnine)

•
⚡ Aceleração Computacional: Otimização de código Python usando compilação JIT (Numba)

🔬 Metodologia

Análise experimental rigorosa utilizando:

•
Datasets clássicos: Iris (sklearn) e Tips (seaborn)

•
Implementação Monte Carlo: Aproximação de π com análise de performance

•
Métricas quantitativas: Speedup de 3.08x demonstrado experimentalmente

📁 Estrutura do Projeto

Plain Text


📦 introducao-softwares-estatisticos/
├── 📄 README.md                          # Documentação principal
├── 📄 LICENSE                            # Licença MIT
├── 📄 requirements.txt                   # Dependências Python
├── 📄 .gitignore                        # Arquivos ignorados pelo Git
├── 📄 trabalho_principal.qmd            # Documento Quarto principal
├── 📄 trabalho_principal.html           # Documento renderizado
├── 📂 src/                              # Código fonte
│   ├── 📄 parte1_visualizacao.py       # Scripts Matplotlib vs Plotnine
│   ├── 📄 parte2_numba.py              # Implementação Monte Carlo
│   └── 📄 utils.py                     # Funções auxiliares
├── 📂 data/                            # Dados utilizados
│   ├── 📄 iris_analysis.csv            # Dataset Iris processado
│   └── 📄 tips_analysis.csv            # Dataset Tips processado
├── 📂 outputs/                         # Resultados gerados
│   ├── 📂 figures/                     # Gráficos em alta resolução
│   │   ├── 🖼️ matplotlib_scatter.png
│   │   ├── 🖼️ matplotlib_histogram.png
│   │   ├── 🖼️ plotnine_scatter.png
│   │   ├── 🖼️ plotnine_histogram.png
│   │   └── 🖼️ performance_comparison.png
│   └── 📂 reports/                     # Relatórios de análise
│       └── 📄 performance_metrics.json
├── 📂 docs/                            # Documentação adicional
│   ├── 📄 metodologia.md               # Detalhes metodológicos
│   ├── 📄 resultados.md                # Análise dos resultados
│   └── 📄 referencias.md               # Bibliografia expandida
└── 📂 tests/                           # Testes automatizados
    ├── 📄 test_visualizacao.py         # Testes das visualizações
    └── 📄 test_numba.py                # Testes de performance


🚀 Início Rápido

Pré-requisitos

•
Python 3.11+

•
Quarto CLI

•
Git

Instalação

Bash


# 1. Clonar o repositório
git clone https://github.com/seu-usuario/introducao-softwares-estatisticos.git
cd introducao-softwares-estatisticos

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Renderizar documento principal
quarto render trabalho_principal.qmd


Execução Rápida

Bash


# Executar análise completa
python src/parte1_visualizacao.py
python src/parte2_numba.py

# Ou executar tudo de uma vez
python -m src.main


📊 Principais Resultados

🎨 Visualização de Dados

Métrica
Matplotlib
Plotnine
Paradigma
Imperativo
Declarativo
Linhas de código
~25 por gráfico
~15 por gráfico
Curva de aprendizado
Íngreme
Moderada
Flexibilidade
Muito alta
Alta
Produtividade
Menor
Maior


⚡ Aceleração Computacional

N Amostras
Python Puro
Numba JIT
Speedup
10,000
0.0156s
0.0051s
3.07x
100,000
0.1542s
0.0501s
3.08x
1,000,000
1.5234s
0.4932s
3.09x


Speedup médio: 3.08x | Economia de tempo: 67.6%

🔬 Metodologia Científica

Datasets Utilizados

•
🌸 Iris Dataset: 150 amostras, 3 espécies, análise de características morfológicas

•
💰 Tips Dataset: 244 registros, análise de distribuição de gorjetas

Análises Implementadas

1.
Comparação de Paradigmas: Imperativo vs Declarativo

2.
Análise de Performance: Python puro vs Numba JIT

3.
Validação Estatística: Preservação de precisão

4.
Métricas Quantitativas: Speedup, tempo economizado, overhead

🛠️ Tecnologias Utilizadas

Core Libraries

•
Matplotlib - Visualização imperativa

•
Plotnine - Grammar of Graphics

•
Numba - Compilação JIT

•
Pandas - Manipulação de dados

•
NumPy - Computação numérica

Development Tools

•
Quarto - Publicação científica

•
Jupyter - Desenvolvimento interativo

•
pytest - Testes automatizados

•
Black - Formatação de código

📈 Reprodutibilidade

Ambiente Controlado

•
Python: 3.11.0

•
Seed: 42 (para reprodutibilidade)

•
Hardware: Especificações documentadas

•
OS: Ubuntu 22.04 LTS

Validação

•
✅ Testes automatizados

•
✅ Análise de sensibilidade

•
✅ Validação cruzada

•
✅ Documentação completa

🎓 Contexto Acadêmico

Instituição: Universidade Federal da Paraíba (UFPB)
Centro: Ciências Exatas e da Natureza (CCEN)
Disciplina: Introdução aos Softwares Estatísticos
Professor: Pedro Rafael Marinho
Período: 2025.1

Objetivos de Aprendizagem




Dominar ferramentas de visualização Python




Compreender paradigmas de programação gráfica




Aplicar técnicas de otimização computacional




Desenvolver análises experimentais rigorosas




Comunicar resultados científicos efetivamente

📚 Referências Acadêmicas

•
Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.

•
Wickham, H. (2016). ggplot2: Elegant Graphics for Data Analysis. 2nd ed. Springer-Verlag.

•
Wilkinson, L. (2005). The Grammar of Graphics. 2nd ed. Springer-Verlag.

•
Lam, S. K., et al. (2015). Numba: A LLVM-based Python JIT Compiler. LLVM-HPC Workshop.

🤝 Contribuições

Este é um projeto acadêmico, mas sugestões e melhorias são bem-vindas:

1.
Fork o projeto

2.
Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

3.
Commit suas mudanças (git commit -m 'Add some AmazingFeature')

4.
Push para a branch (git push origin feature/AmazingFeature)

5.
Abra um Pull Request

📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

👨‍💻 Autor

Diogo da Silva Rego

•
🎓 Estudante de [Seu Curso] - UFPB

•
📧 Email: Diogo.silva.rego@academico.ufpb.br

•
💼 LinkedIn: Diogorego

•
🐙 GitHub: @seu-usuario

🙏 Agradecimentos

•
Prof. Pedro Rafael Marinho pela orientação acadêmica

•
CCEN/UFPB pela infraestrutura de pesquisa

•
Comunidade Python pela excelência das ferramentas

•
Colegas de turma pelas discussões enriquecedoras




<div align="center">

⭐ Se este projeto foi útil para você, considere dar uma estrela!











</div>

