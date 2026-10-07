import json

def generate_web_app():
    with open('transactions_data.json', 'r', encoding='utf-8') as f:
        transactions = json.load(f)

    html_content = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gestão Financeira Integrada — Moura Barretto & Mateus</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <!-- Google Fonts Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'sans-serif'],
          }},
          colors: {{
            brand: {{
              50: '#f0f9ff',
              100: '#e0f2fe',
              500: '#0284c7',
              600: '#0369a1',
              700: '#075985',
              900: '#0c4a6e',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      font-family: 'Inter', sans-serif;
      background-color: #0f172a;
      color: #f8fafc;
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    .custom-scrollbar::-webkit-scrollbar-track {{
      background: #1e293b;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #475569;
      border-radius: 3px;
    }}
    .glass-card {{
      background: rgba(30, 41, 59, 0.7);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col">

  <!-- TOPBAR -->
  <header class="border-b border-slate-800 bg-slate-900/90 backdrop-blur sticky top-0 z-50 px-6 py-4">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center md:justify-between gap-4">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center font-bold text-white shadow-lg shadow-sky-500/20">
          MB
        </div>
        <div>
          <h1 class="text-lg font-bold text-white flex items-center gap-2">
            Sistema Financeiro Integrado
            <span class="text-xs px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-medium">Setembro/2026</span>
          </h1>
          <p class="text-xs text-slate-400">Moura Barretto Engenharia (PJ) & Mateus Moura (PF)</p>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <button onclick="exportToCSV()" class="px-3 py-2 text-xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          Exportar CSV
        </button>
        <button onclick="toggleModal(true)" class="px-4 py-2 text-xs font-semibold rounded-lg bg-sky-600 hover:bg-sky-500 text-white shadow-lg shadow-sky-600/30 transition flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
          Novo Lançamento
        </button>
      </div>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 space-y-6">

    <!-- KPI CARDS -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- Card 1: Receita -->
      <div class="glass-card rounded-2xl p-5 relative overflow-hidden">
        <div class="absolute -right-4 -bottom-4 w-24 h-24 bg-emerald-500/10 rounded-full blur-xl"></div>
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-semibold uppercase tracking-wider">Faturamento Total</span>
          <span class="p-2 rounded-lg bg-emerald-500/10 text-emerald-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 11l5-5m0 0l5 5m-5-5v12"/></svg>
          </span>
        </div>
        <div class="text-2xl font-bold text-white tracking-tight" id="kpi-receita">R$ 16.560,00</div>
        <p class="text-xs text-slate-400 mt-2 flex items-center gap-1">
          <span class="text-emerald-400 font-medium">Grado (R$ 7.2k)</span> + <span class="text-sky-400 font-medium">Wise (1575 €)</span>
        </p>
      </div>

      <!-- Card 2: Custos PJ -->
      <div class="glass-card rounded-2xl p-5 relative overflow-hidden">
        <div class="absolute -right-4 -bottom-4 w-24 h-24 bg-sky-500/10 rounded-full blur-xl"></div>
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-semibold uppercase tracking-wider">Despesas Operacionais PJ</span>
          <span class="p-2 rounded-lg bg-sky-500/10 text-sky-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
          </span>
        </div>
        <div class="text-2xl font-bold text-white tracking-tight" id="kpi-pj">R$ 4.674,65</div>
        <p class="text-xs text-slate-400 mt-2 flex items-center gap-1">
          <span class="text-emerald-400 font-medium">17.8% abaixo</span> da meta orçada (R$ 5.689)
        </p>
      </div>

      <!-- Card 3: Lucro Líquido PJ -->
      <div class="glass-card rounded-2xl p-5 relative overflow-hidden">
        <div class="absolute -right-4 -bottom-4 w-24 h-24 bg-purple-500/10 rounded-full blur-xl"></div>
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-semibold uppercase tracking-wider">Lucro Líquido PJ</span>
          <span class="p-2 rounded-lg bg-purple-500/10 text-purple-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
          </span>
        </div>
        <div class="text-2xl font-bold text-purple-400 tracking-tight" id="kpi-lucro">R$ 11.885,35</div>
        <p class="text-xs text-slate-400 mt-2 flex items-center gap-1">
          Margem Operacional Líquida de <span class="text-purple-300 font-medium">71.8%</span>
        </p>
      </div>

      <!-- Card 4: Custo de Vida PF -->
      <div class="glass-card rounded-2xl p-5 relative overflow-hidden">
        <div class="absolute -right-4 -bottom-4 w-24 h-24 bg-rose-500/10 rounded-full blur-xl"></div>
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-semibold uppercase tracking-wider">Custo de Vida PF (Real)</span>
          <span class="p-2 rounded-lg bg-rose-500/10 text-rose-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
          </span>
        </div>
        <div class="text-2xl font-bold text-white tracking-tight" id="kpi-pf">R$ 23.298,14</div>
        <p class="text-xs text-rose-400/90 mt-2 flex items-center gap-1 font-medium">
          Inclui 2 parcelas de carro (R$ 4.160)
        </p>
      </div>
    </div>

    <!-- BANNER DE ALÍVIO FUTURO -->
    <div class="rounded-2xl p-4 bg-gradient-to-r from-sky-950/80 via-indigo-950/80 to-slate-900 border border-sky-500/30 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-sky-500/20 text-sky-400 flex items-center justify-center font-bold text-lg">
          💡
        </div>
        <div>
          <h3 class="text-sm font-bold text-white">Previsão Conquistada: Alívio Imediato de R$ 1.425,89/mês</h3>
          <p class="text-xs text-slate-300">
            As parcelas das <strong>Casas Bahia (10/10: R$ 678,77)</strong>, <strong>Vai de Promo (3/3: R$ 633,97)</strong> e <strong>Moda Infantil (4/4: R$ 113,15)</strong> foram quitadas em setembro!
          </p>
        </div>
      </div>
      <div class="text-right">
        <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
          Redução Automática em Outubro
        </span>
      </div>
    </div>

    <!-- GRÁFICOS INTERATIVOS -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Gráfico 1: Donut Categorias -->
      <div class="glass-card rounded-2xl p-5 flex flex-col">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-sm font-bold text-white">Distribuição por Categoria</h2>
          <span class="text-xs text-slate-400">Total Despesas</span>
        </div>
        <div class="relative flex-1 flex items-center justify-center min-h-[260px]">
          <canvas id="categoryChart"></canvas>
        </div>
      </div>

      <!-- Gráfico 2: Orçado vs Realizado -->
      <div class="glass-card rounded-2xl p-5 flex flex-col">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-sm font-bold text-white">Orçado (Meta) vs Realizado</h2>
          <span class="text-xs text-slate-400">Comparativo R$</span>
        </div>
        <div class="relative flex-1 flex items-center justify-center min-h-[260px]">
          <canvas id="budgetChart"></canvas>
        </div>
      </div>

      <!-- Gráfico 3: Projeção de Parcelas -->
      <div class="glass-card rounded-2xl p-5 flex flex-col">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-sm font-bold text-white">Queda Prevista das Parcelas</h2>
          <span class="text-xs text-slate-400">Set -> Dez/2026</span>
        </div>
        <div class="relative flex-1 flex items-center justify-center min-h-[260px]">
          <canvas id="timelineChart"></canvas>
        </div>
      </div>
    </div>

    <!-- CARD DA CONCILIAÇÃO PF x PJ -->
    <div class="glass-card rounded-2xl p-5">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-700/60 pb-3 mb-4">
        <div>
          <h2 class="text-base font-bold text-white flex items-center gap-2">
            <span>🔄</span> Conciliação Cirúrgica: Contas Cruzadas (PF x PJ)
          </h2>
          <p class="text-xs text-slate-400">
            Acompanhe exatamente o que foi bancado entre o CNPJ e o CPF para apurar a remuneração real do sócio.
          </p>
        </div>
        <div class="flex gap-2">
          <span class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-rose-500/20 text-rose-300 border border-rose-500/30">
            PJ bancou PF: R$ 7.930,36
          </span>
          <span class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-sky-500/20 text-sky-300 border border-sky-500/30">
            PF pagou PJ: R$ 855,00
          </span>
        </div>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="bg-slate-900/60 rounded-xl p-4 border border-slate-800">
          <h4 class="font-bold text-rose-400 mb-2 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-rose-500"></span> Despesas Pessoais Pagas pela Empresa (PJ)
          </h4>
          <ul class="space-y-1.5 text-slate-300">
            <li class="flex justify-between"><span>• Carro Banco RCI (2 parcelas de R$ 2.080,09):</span> <strong class="text-white">R$ 4.160,18</strong></li>
            <li class="flex justify-between"><span>• Costa Azul Salvador / Ocean Breeze:</span> <strong class="text-white">R$ 1.662,67</strong></li>
            <li class="flex justify-between"><span>• Aluguel Residencial Joelma:</span> <strong class="text-white">R$ 800,00</strong></li>
            <li class="flex justify-between"><span>• CEMIG Energia MG (2 contas):</span> <strong class="text-white">R$ 557,01</strong></li>
            <li class="flex justify-between"><span>• Exercícios / Respect Jiu-Jitsu + BL:</span> <strong class="text-white">R$ 669,90</strong></li>
            <li class="flex justify-between"><span>• Combustível & Pedágio em débito:</span> <strong class="text-white">R$ 207,70</strong></li>
          </ul>
        </div>
        <div class="bg-slate-900/60 rounded-xl p-4 border border-slate-800">
          <h4 class="font-bold text-sky-400 mb-2 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-sky-500"></span> Despesas da Empresa Pagas pelo Sócio (PF)
          </h4>
          <ul class="space-y-1.5 text-slate-300">
            <li class="flex justify-between"><span>• DW Coworking / Aluguel Escritório:</span> <strong class="text-white">R$ 525,00</strong></li>
            <li class="flex justify-between"><span>• INSS / DCTFWeb Moura Barretto Eng:</span> <strong class="text-white">R$ 220,00</strong></li>
            <li class="flex justify-between"><span>• ABECE Associação de Engenharia:</span> <strong class="text-white">R$ 110,00</strong></li>
          </ul>
          <div class="mt-4 pt-3 border-t border-slate-800 text-slate-400">
            <p><strong>Conclusão Contábil:</strong> A remuneração líquida real do sócio em setembro foi de <strong>R$ 7.275,36</strong> (despesas pessoais bancadas menos aportes da PF).</p>
          </div>
        </div>
      </div>
    </div>

    <!-- TABELA DE LANÇAMENTOS COM FILTROS E BUSCA -->
    <div class="glass-card rounded-2xl p-5 space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 class="text-base font-bold text-white flex items-center gap-2">
            <span>📝</span> Extrato Consolidado & Lançamentos
          </h2>
          <p class="text-xs text-slate-400">Todos os lançamentos de cartões, contas e comprovantes</p>
        </div>

        <!-- SEARCH BAR -->
        <div class="relative w-full sm:w-72">
          <input type="text" id="searchInput" placeholder="Buscar por loja, categoria, valor..." onkeyup="filterTable()" class="w-full px-3 py-2 pl-9 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-500">
          <svg class="w-4 h-4 text-slate-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </div>
      </div>

      <!-- FILTER BUTTONS -->
      <div class="flex flex-wrap gap-2 pt-2 border-t border-slate-800">
        <button onclick="setFilter('all')" id="btn-filter-all" class="filter-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-sky-600 text-white">Todos (<span id="count-all">0</span>)</button>
        <button onclick="setFilter('PF')" id="btn-filter-PF" class="filter-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">Apenas PF (<span id="count-pf">0</span>)</button>
        <button onclick="setFilter('PJ')" id="btn-filter-PJ" class="filter-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">Apenas PJ (<span id="count-pj">0</span>)</button>
        <button onclick="setFilter('cruzados')" id="btn-filter-cruzados" class="filter-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">Contas Cruzadas (<span id="count-cruz">0</span>)</button>
        <button onclick="setFilter('receitas')" id="btn-filter-receitas" class="filter-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">Receitas (<span id="count-rec">0</span>)</button>
      </div>

      <!-- TABELA SCROLLÁVEL -->
      <div class="overflow-x-auto custom-scrollbar border border-slate-800 rounded-xl">
        <table class="w-full text-left text-xs whitespace-nowrap">
          <thead class="bg-slate-900/90 text-slate-400 uppercase font-semibold border-b border-slate-800">
            <tr>
              <th class="px-4 py-3">Data</th>
              <th class="px-4 py-3">Entidade</th>
              <th class="px-4 py-3">Conta / Meio</th>
              <th class="px-4 py-3">Categoria</th>
              <th class="px-4 py-3">Descrição</th>
              <th class="px-4 py-3 text-right">Valor</th>
              <th class="px-4 py-3">Cruzamento</th>
              <th class="px-4 py-3">Observações</th>
            </tr>
          </thead>
          <tbody id="transactionTableBody" class="divide-y divide-slate-800/60">
            <!-- Renderizado via JS -->
          </tbody>
        </table>
      </div>

      <div class="flex items-center justify-between text-xs text-slate-400 pt-2">
        <span id="resultsCount">Exibindo todas as transações</span>
        <span class="text-slate-500">Dados baseados no fechamento oficial de Setembro/2026</span>
      </div>
    </div>

  </main>

  <!-- MODAL DE NOVO LANÇAMENTO -->
  <div id="newModal" class="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-6 space-y-4">
      <div class="flex justify-between items-center border-b border-slate-800 pb-3">
        <h3 class="text-base font-bold text-white">Inserir Novo Lançamento</h3>
        <button onclick="toggleModal(false)" class="text-slate-400 hover:text-white">&times;</button>
      </div>
      <form id="newTransactionForm" onsubmit="addTransaction(event)" class="space-y-3 text-xs">
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-400 mb-1">Data</label>
            <input type="date" id="m_data" required class="w-full px-3 py-2 rounded-lg bg-slate-800 border border-slate-700 text-white">
          </div>
          <div>
            <label class="block text-slate-400 mb-1">Entidade</label>
            <select id="m_entidade" required class="w-full px-3 py-2 rounded-lg bg-slate-800 border border-slate-700 text-white">
              <option value="PF">Pessoa Física (PF)</option>
              <option value="PJ">Pessoa Jurídica (PJ)</option>
            </select>
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-400 mb-1">Tipo</label>
            <select id="m_tipo" required class="w-full px-3 py-2 rounded-lg bg-slate-800 border border-slate-700 text-white">
              <option value="Despesa">Despesa</option>
              <option value="Receita">Receita</option>
            </select>
          </div>
          <div>
            <label class="block text-slate-400 mb-1">Valor (R$)</label>
            <input type="number" step="0.01" id="m_valor" required placeholder="0.00" class="w-full px-3 py-2 rounded-lg bg-slate-800 border border-slate-700 text-white">
          </div>
        </div>
        <div>
          <label class="block text-slate-400 mb-1">Conta / Cartão</label>
          <select id="m_conta" required class="w-full px-3 py-2 rounded-lg bg-slate-800 border border-slate-700 text-white">
            <option value="Cartão Nubank PF">Cartão Nubank PF</option>
            <option value="Cartão Caixa PF">Cartão Caixa PF</option>
            <option value="Cartão Nubank PJ">Cartão Nubank PJ</option>
            <option value="Conta Nubank PF">Conta Nubank PF</option>
            <option value="Conta Caixa PJ">Conta Caixa PJ</option>
            <option value="Conta Nubank PJ">Conta Nubank PJ</option>
            <option value="Wise Portugal">Wise Portugal</option>
          </select>
        </div>
        <div>
          <label class="block text-slate-400 mb-1">Categoria</label>
          <select id="m_categoria" required class="w-full px-3 py-2 rounded-lg bg-slate-800 border border-slate-700 text-white">
            <option value="Alimentação">Alimentação</option>
            <option value="Moradia">Moradia</option>
            <option value="Transporte & Veículos">Transporte & Veículos</option>
            <option value="Saúde & Bem-Estar">Saúde & Bem-Estar</option>
            <option value="Educação (Benjamim)">Educação (Benjamim)</option>
            <option value="Compras & Lazer">Compras & Lazer</option>
            <option value="Custos Escritório">Custos Escritório (PJ)</option>
            <option value="Receita Operacional">Receita Operacional</option>
          </select>
        </div>
        <div>
          <label class="block text-slate-400 mb-1">Descrição</label>
          <input type="text" id="m_descricao" required placeholder="Ex: Supermercado, Aluguel, Posto..." class="w-full px-3 py-2 rounded-lg bg-slate-800 border border-slate-700 text-white">
        </div>
        <div>
          <label class="block text-slate-400 mb-1">Cruzamento PF/PJ</label>
          <select id="m_cruzamento" class="w-full px-3 py-2 rounded-lg bg-slate-800 border border-slate-700 text-white">
            <option value="Normal">Normal</option>
            <option value="PJ bancou PF">PJ bancou PF (Despesa pessoal no CNPJ)</option>
            <option value="PF pagou PJ">PF pagou PJ (Despesa do escritório no CPF)</option>
          </select>
        </div>
        <div class="flex justify-end gap-2 pt-3 border-t border-slate-800">
          <button type="button" onclick="toggleModal(false)" class="px-3 py-2 rounded-lg bg-slate-800 text-slate-300">Cancelar</button>
          <button type="submit" class="px-4 py-2 rounded-lg bg-sky-600 text-white font-semibold">Salvar Lançamento</button>
        </div>
      </form>
    </div>
  </div>

  <!-- SCRIPT COM DADOS E LÓGICA -->
  <script>
    // DADOS INICIAIS EMBUTIDOS
    let allTransactions = {json.dumps(transactions, ensure_ascii=False)};
    let currentFilter = 'all';

    // Formatar Moeda
    function formatBRL(val) {{
      return new Intl.NumberFormat('pt-BR', {{ style: 'currency', currency: 'BRL' }}).format(val);
    }}

    // Renderizar Tabela
    function renderTable() {{
      const tbody = document.getElementById('transactionTableBody');
      const search = document.getElementById('searchInput').value.toLowerCase();
      tbody.innerHTML = '';

      let filtered = allTransactions.filter(item => {{
        // Filtro por tipo/entidade
        if (currentFilter === 'PF' && item.entidade !== 'PF') return false;
        if (currentFilter === 'PJ' && item.entidade !== 'PJ') return false;
        if (currentFilter === 'cruzados' && !item.cruzamento.includes('bancou') && !item.cruzamento.includes('pagou')) return false;
        if (currentFilter === 'receitas' && item.tipo !== 'Receita') return false;

        // Filtro por busca
        if (search) {{
          const match = item.descricao.toLowerCase().includes(search) ||
                        item.categoria.toLowerCase().includes(search) ||
                        item.conta.toLowerCase().includes(search) ||
                        item.valor.toString().includes(search);
          if (!match) return false;
        }}
        return true;
      }});

      filtered.forEach(item => {{
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-800/40 transition';

        const badgeEnt = item.entidade === 'PJ' 
          ? '<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">PJ</span>'
          : '<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">PF</span>';

        let badgeCruz = '<span class="text-slate-500">—</span>';
        if (item.cruzamento.includes('PJ bancou PF')) {{
          badgeCruz = '<span class="px-2 py-0.5 rounded-md text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">PJ bancou PF</span>';
        }} else if (item.cruzamento.includes('PF pagou PJ')) {{
          badgeCruz = '<span class="px-2 py-0.5 rounded-md text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">PF pagou PJ</span>';
        }}

        const isReceita = item.tipo === 'Receita';
        const valorClass = isReceita ? 'text-emerald-400 font-bold' : 'text-slate-100 font-semibold';
        const valorSign = isReceita ? '+ ' : '- ';

        tr.innerHTML = `
          <td class="px-4 py-2.5 text-slate-400">${{item.data}}</td>
          <td class="px-4 py-2.5">${{badgeEnt}}</td>
          <td class="px-4 py-2.5 text-slate-300">${{item.conta}}</td>
          <td class="px-4 py-2.5 font-medium text-slate-200">${{item.categoria}}</td>
          <td class="px-4 py-2.5 text-white font-medium">${{item.descricao}}</td>
          <td class="px-4 py-2.5 text-right ${{valorClass}}">${{valorSign}}${{formatBRL(item.valor)}}</td>
          <td class="px-4 py-2.5">${{badgeCruz}}</td>
          <td class="px-4 py-2.5 text-slate-400 truncate max-w-xs" title="${{item.observacao || ''}}">${{item.observacao || ''}}</td>
        `;
        tbody.appendChild(tr);
      }});

      document.getElementById('resultsCount').innerText = `Exibindo ${{filtered.length}} de ${{allTransactions.length}} lançamentos`;
      updateCounts();
    }}

    function updateCounts() {{
      document.getElementById('count-all').innerText = allTransactions.length;
      document.getElementById('count-pf').innerText = allTransactions.filter(x => x.entidade === 'PF').length;
      document.getElementById('count-pj').innerText = allTransactions.filter(x => x.entidade === 'PJ').length;
      document.getElementById('count-cruz').innerText = allTransactions.filter(x => x.cruzamento.includes('bancou') || x.cruzamento.includes('pagou')).length;
      document.getElementById('count-rec').innerText = allTransactions.filter(x => x.tipo === 'Receita').length;
    }}

    function setFilter(filter) {{
      currentFilter = filter;
      document.querySelectorAll('.filter-btn').forEach(btn => {{
        btn.className = 'filter-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700';
      }});
      const activeBtn = document.getElementById(`btn-filter-${{filter}}`);
      if (activeBtn) {{
        activeBtn.className = 'filter-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-sky-600 text-white shadow-lg shadow-sky-600/30';
      }}
      renderTable();
    }}

    function filterTable() {{
      renderTable();
    }}

    function toggleModal(show) {{
      document.getElementById('newModal').classList.toggle('hidden', !show);
    }}

    function addTransaction(e) {{
      e.preventDefault();
      const novo = {{
        id: allTransactions.length + 1,
        data: document.getElementById('m_data').value,
        competencia: '09/2026',
        conta: document.getElementById('m_conta').value,
        entidade: document.getElementById('m_entidade').value,
        tipo: document.getElementById('m_tipo').value,
        categoria: document.getElementById('m_categoria').value,
        subcategoria: '',
        descricao: document.getElementById('m_descricao').value,
        valor: parseFloat(document.getElementById('m_valor').value),
        conta_pagadora: document.getElementById('m_conta').value,
        cruzamento: document.getElementById('m_cruzamento').value,
        status: 'Liquidado',
        observacao: 'Lançamento manual via Web App'
      }};
      allTransactions.unshift(novo);
      renderTable();
      toggleModal(false);
      document.getElementById('newTransactionForm').reset();
    }}

    function exportToCSV() {{
      let csv = 'Data;Entidade;Conta;Tipo;Categoria;Descricao;Valor;Cruzamento;Observacao\\n';
      allTransactions.forEach(t => {{
        csv += `${{t.data}};${{t.entidade}};${{t.conta}};${{t.tipo}};${{t.categoria}};\"${{t.descricao}}\";${{t.valor}};${{t.cruzamento}};\"${{t.observacao}}\"\\n`;
      }});
      const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'extrato_consolidado_setembro_2026.csv';
      link.click();
    }}

    // INICIALIZAÇÃO DOS GRÁFICOS
    window.onload = function() {{
      renderTable();

      // Donut Chart: Categorias
      const ctxCat = document.getElementById('categoryChart').getContext('2d');
      new Chart(ctxCat, {{
        type: 'doughnut',
        data: {{
          labels: ['Alimentação', 'Transporte', 'Custos PJ', 'Moradia', 'Saúde', 'Compras/Lazer', 'Benjamim'],
          datasets: [{{
            data: [5742.00, 6138.31, 4674.65, 3145.02, 2951.83, 2867.01, 2453.97],
            backgroundColor: [
              '#10b981', '#38bdf8', '#818cf8', '#f59e0b', '#ec4899', '#a855f7', '#06b6d4'
            ],
            borderWidth: 0
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ color: '#94a3b8', font: {{ size: 10 }}, boxWidth: 10 }}
            }}
          }},
          cutout: '65%'
        }}
      }});

      // Bar Chart: Orçado vs Realizado
      const ctxBudget = document.getElementById('budgetChart').getContext('2d');
      new Chart(ctxBudget, {{
        type: 'bar',
        data: {{
          labels: ['Alimentação', 'Transporte', 'Moradia', 'Saúde', 'Benjamim', 'Escritório PJ'],
          datasets: [
            {{
              label: 'Meta / Orçado',
              data: [5000, 4000, 6973, 2510, 2437, 5689],
              backgroundColor: 'rgba(148, 163, 184, 0.4)',
              borderRadius: 6
            }},
            {{
              label: 'Realizado Setembro',
              data: [5742, 6138, 3145, 2951, 2453, 4674],
              backgroundColor: 'rgba(56, 189, 248, 0.85)',
              borderRadius: 6
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ color: '#94a3b8', font: {{ size: 10 }}, boxWidth: 10 }}
            }}
          }},
          scales: {{
            x: {{ ticks: {{ color: '#64748b', font: {{ size: 9 }} }}, grid: {{ display: false }} }},
            y: {{ ticks: {{ color: '#64748b', font: {{ size: 9 }} }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
          }}
        }}
      }});

      // Line / Bar Chart: Queda de Parcelas
      const ctxTimeline = document.getElementById('timelineChart').getContext('2d');
      new Chart(ctxTimeline, {{
        type: 'line',
        data: {{
          labels: ['Setembro/26 (Real)', 'Outubro/26 (Proj.)', 'Novembro/26 (Proj.)', 'Dezembro/26 (Proj.)'],
          datasets: [{{
            label: 'Total de Parcelas a Pagar (R$)',
            data: [3182.34, 1756.45, 111.63, 111.63],
            borderColor: '#38bdf8',
            backgroundColor: 'rgba(56, 189, 248, 0.15)',
            fill: true,
            tension: 0.3,
            pointBackgroundColor: '#38bdf8',
            pointRadius: 5
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ color: '#94a3b8', font: {{ size: 10 }}, boxWidth: 10 }}
            }}
          }},
          scales: {{
            x: {{ ticks: {{ color: '#64748b', font: {{ size: 9 }} }}, grid: {{ display: false }} }},
            y: {{ ticks: {{ color: '#64748b', font: {{ size: 9 }} }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
          }}
        }}
      }});
    }};
  </script>
</body>
</html>
'''
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("index.html criado com sucesso!")

if __name__ == '__main__':
    generate_web_app()
