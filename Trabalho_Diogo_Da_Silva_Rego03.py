# ==================== IMPORTAÇÕES ====================
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import time
import warnings
import random

warnings.filterwarnings('ignore')

# ==================== CONFIGURAÇÃO ====================
plt.rcParams.update({
    'figure.figsize': (10, 6),
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 11,
    'figure.dpi': 100
})

# ==================== CARREGAMENTO DE DADOS ====================
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

tips = sns.load_dataset('tips')

# ==================== GRÁFICOS MATPLOTLIB ====================
print("🎨 GERANDO GRÁFICOS MATPLOTLIB...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Definição das cores ANTES de usar
colors = ['#E74C3C', '#3498DB', '#2ECC71']
species = iris_df['species'].unique()

# Scatter plot
for i, species_name in enumerate(species):
    subset = iris_df[iris_df['species'] == species_name]
    ax1.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'], 
               c=colors[i], label=species_name, alpha=0.7, s=60)

ax1.set_xlabel('Comprimento da Sépala (cm)', fontweight='bold')
ax1.set_ylabel('Largura da Sépala (cm)', fontweight='bold')
ax1.set_title('Relação entre Comprimento e Largura da Sépala\n(Matplotlib)', fontweight='bold')
ax1.legend(title='Espécie')
ax1.grid(True, alpha=0.3)

# Histograma
ax2.hist(tips['tip'], bins=20, color='#3498DB', alpha=0.7, edgecolor='black')
ax2.set_xlabel('Valor da Gorjeta ($)', fontweight='bold')
ax2.set_ylabel('Frequência', fontweight='bold')
ax2.set_title('Distribuição dos Valores de Gorjetas\n(Matplotlib)', fontweight='bold')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ==================== IMPLEMENTAÇÃO MONTE CARLO ====================
def monte_carlo_pi_python(n_samples):
    """Aproximação de π usando método Monte Carlo em Python puro."""
    count_inside = 0
    
    for i in range(n_samples):
        x = random.random()
        y = random.random()
        
        if x*x + y*y <= 1.0:
            count_inside += 1
    
    pi_estimate = 4.0 * count_inside / n_samples
    return pi_estimate

# Teste de performance
print("🔍 TESTANDO PERFORMANCE...")
sample_sizes = [1000, 5000, 10000]  # Reduzido para teste rápido

python_results = []
for n in sample_sizes:
    start_time = time.time()
    pi_est = monte_carlo_pi_python(n)
    execution_time = time.time() - start_time
    error = abs(pi_est - np.pi)
    
    python_results.append({'n': n, 'pi': pi_est, 'error': error, 'time': execution_time})
    print(f"Amostras: {n}, π estimado: {pi_est:.6f}, Tempo: {execution_time:.4f}s")

print("✅ EXECUÇÃO CONCLUÍDA COM SUCESSO!")
