import json

def generate_v2_web_app():
    with open('transactions_data.json', 'r', encoding='utf-8') as f:
        transactions = json.load(f)

    html_content = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gestão Financeira por Grupos — Moura Barretto</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'sans-serif'],
          }},
        }}
      }}
    }}
  </script>
  <style>
    body {{
      font-family: 'Inter', sans-serif;
      background-color: #0b1120;
      color: #f1f5f9;
    }}
    .custom-scroll::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    .custom-scroll::-webkit-scrollbar-track {{
      background: #1e293b;
    }}
    .custom-scroll::-webkit-scrollbar-thumb {{
      background: #475569;
      border-radius: 3px;
    }}
    .panel-card {{
      background: #131c31;
      border: 1px solid rgba(255, 255, 255, 0.07);
    }}
    .tab-btn.active {{
      background: #0284c7;
      color: #ffffff;
      font-weight: 600;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased">

  <!-- TOP HEADER -->
  <header class="border-b border-slate-800 bg-[#0f172a]/95 sticky top-0 z-50 px-4 md:px-8 py-3.5 backdrop-blur">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row sm:items-center justify-between gap-3">
      <div class="flex items-center space-x-3">
        <div class="w-9 h-9 rounded-lg bg-sky-600 flex items-center justify-center font-bold text-white text-sm">
          MB
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-base font-bold text-white tracking-tight">Painel Financeiro por Grupos</h1>
            <span class="text-[11px] font-semibold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Setembro/2026</span>
          </div>
          <p class="text-xs text-slate-400">Moura Barretto Engenharia Ltda (PJ) & Mateus Moura Barretto (PF)</p>
        </div>
      </div>

      <!-- TABS DE NAVEGAÇÃO -->
      <nav class="flex items-center bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs">
        <button onclick="switchTab('pf')" id="tab-nav-pf" class="tab-btn active px-3.5 py-1.5 rounded-lg text-slate-400 hover:text-white transition">
          👤 Pessoal (PF)
        </button>
        <button onclick="switchTab('pj')" id="tab-nav-pj" class="tab-btn px-3.5 py-1.5 rounded-lg text-slate-400 hover:text-white transition">
          🏢 Escritório (PJ)
        </button>
        <button onclick="switchTab('consolidado')" id="tab-nav-consolidado" class="tab-btn px-3.5 py-1.5 rounded-lg text-slate-400 hover:text-white transition">
          🎯 Consolidado & Metas
        </button>
        <button onclick="switchTab('extrato')" id="tab-nav-extrato" class="tab-btn px-3.5 py-1.5 rounded-lg text-slate-400 hover:text-white transition">
          📝 Extrato com Filtros
        </button>
      </nav>
    </div>
  </header>

  <!-- MAIN VIEW CONTAINER -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 space-y-6">

    <!-- ================================================================= -->
    <!-- TAB 1: DASHBOARD PESSOAL (PF) -->
    <!-- ================================================================= -->
    <div id="view-pf" class="space-y-6">
      <!-- HEADER DO BLOCO PF -->
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 p-5 rounded-2xl bg-gradient-to-r from-sky-950/60 to-slate-900 border border-sky-800/30">
        <div>
          <span class="text-xs uppercase font-bold tracking-wider text-sky-400">Dashboard de Gestão Pessoal (PF)</span>
          <h2 class="text-xl font-bold text-white mt-0.5">Gastos da Família por Grupos & Subgrupos</h2>
          <p class="text-xs text-slate-400 mt-1">Acompanhamento de alimentação, carro, moradia, filho, saúde e compras.</p>
        </div>
        <div class="flex items-center gap-3">
          <div class="text-right">
            <span class="text-[11px] text-slate-400 block">Total Realizado Setembro</span>
            <span class="text-xl font-bold text-white">R$ 23.298,14</span>
          </div>
          <div class="h-8 w-px bg-slate-700"></div>
          <div class="text-right">
            <span class="text-[11px] text-emerald-400 block">Nova Meta Saudável</span>
            <span class="text-xl font-bold text-emerald-400">R$ 15.162,00</span>
          </div>
        </div>
      </div>

      <!-- GRID DE TÓPICOS DA PESSOA FÍSICA -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">

        <!-- Tópico 1: ALIMENTAÇÃO -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">1. Alimentação da Família</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 3.500,00</span>
              </div>
              <span class="text-base font-bold text-rose-400">R$ 5.742,00</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Supermercados (Mart Minas + Buritis)</span>
                <strong class="text-white">R$ 3.210,90</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Restaurantes, Saídas & Fins de Semana</span>
                <strong class="text-white">R$ 1.576,40</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Feira Livre, Padarias & Pastelzinho</span>
                <strong class="text-white">R$ 954,70</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-sky-400">
            🎯 <strong>Estratégia:</strong> Cortar as 14 idas ao mercado no mês e limitar saídas a R$ 225/fim de semana. <strong>Economia: R$ 2.242/mês</strong>.
          </div>
        </div>

        <!-- Tópico 2: CARRO & TRANSPORTE -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">2. Carro & Transporte</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 2.980,09</span>
              </div>
              <span class="text-base font-bold text-rose-400">R$ 6.138,31</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Parcela Carro (Banco RCI) <span class="text-[10px] text-amber-400 font-semibold">[2 parcelas]</span></span>
                <strong class="text-white">R$ 4.160,18</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Combustível (Posto Mariano / Pedra Forte)</span>
                <strong class="text-white">R$ 1.399,67</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Passagens (Latam 3/4), Uber & Pedágio</span>
                <strong class="text-white">R$ 578,46</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-sky-400">
            🎯 <strong>Estratégia:</strong> O fluxo normal é 1 parcela de R$ 2.080. Latam encerra em Outubro. <strong>Economia automática: R$ 2.500/mês</strong>.
          </div>
        </div>

        <!-- Tópico 3: MORADIA -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">3. Moradia & Habitação</h3>
                <span class="text-[11px] text-slate-400">Meta Fase 2: R$ 1.475,00</span>
              </div>
              <span class="text-base font-bold text-white">R$ 3.145,02</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Imóvel Salvador (Ocean Breeze)</span>
                <strong class="text-white">R$ 1.662,67</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Aluguel Residencial P. Alegre (Joelma)</span>
                <strong class="text-white">R$ 800,00</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Energia CEMIG (Minas Gerais)</span>
                <strong class="text-white">R$ 557,01</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Telefonia Celular (TIM)</span>
                <strong class="text-white">R$ 125,34</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-sky-400">
            🎯 <strong>Estratégia:</strong> Colocar o imóvel de Salvador para alugar ou Airbnb zera este custo de R$ 1.662.
          </div>
        </div>

        <!-- Tópico 4: BENJAMIM -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">4. Filho & Educação</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 2.210,00</span>
              </div>
              <span class="text-base font-bold text-white">R$ 2.453,97</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Mensalidade Escolar (Assoc. Obras)</span>
                <strong class="text-white">R$ 1.870,00</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Curso de Inglês (Spectrum Line)</span>
                <strong class="text-white">R$ 240,00</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Vestuário (Sigga Moda 4/4) & Itens</span>
                <strong class="text-white">R$ 343,97</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-emerald-400">
            ✅ <strong>Prioridade Protegida:</strong> Sigga Moda Infantil quitada em Setembro (4/4). Custo estabilizado em R$ 2.210.
          </div>
        </div>

        <!-- Tópico 5: SAÚDE & PREVIDÊNCIA -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">5. Saúde & Previdência</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 2.572,83</span>
              </div>
              <span class="text-base font-bold text-white">R$ 2.951,83</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Plano de Saúde Familiar (Unimed)</span>
                <strong class="text-white">R$ 1.546,83</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Lutas & Atividades Físicas (Respect / BL)</span>
                <strong class="text-white">R$ 837,90</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Farmácias & Odontologia</span>
                <strong class="text-white">R$ 341,10</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Previdência Privada (BB Prev)</span>
                <strong class="text-white">R$ 226,00</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-emerald-400">
            ✅ <strong>Proteção Completa:</strong> Cobertura médica e aposentadoria preservadas integralmente.
          </div>
        </div>

        <!-- Tópico 6: COMPRAS, LAZER & PARCELAS -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">6. Compras & Parcelamentos</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 761,63</span>
              </div>
              <span class="text-base font-bold text-white">R$ 2.867,01</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Casas Bahia (10/10) + Vai de Promo (3/3)</span>
                <strong class="text-emerald-400">R$ 1.312,74 [QUITADOS!]</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Compras Online, Vestuário & Casa</span>
                <strong class="text-white">R$ 840,72</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Pets & Rações (Petagro / Edwiges)</span>
                <strong class="text-white">R$ 347,60</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Streaming (Netflix, Spotify, Prime Canais)</span>
                <strong class="text-white">R$ 205,49</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-emerald-400">
            🎉 <strong>Alívio Garantido:</strong> As duas maiores parcelas acabaram! Fatura cai R$ 1.312 direto em Outubro.
          </div>
        </div>

      </div>
    </div>

    <!-- ================================================================= -->
    <!-- TAB 2: DASHBOARD ESCRITÓRIO (PJ) -->
    <!-- ================================================================= -->
    <div id="view-pj" class="space-y-6 hidden">
      <!-- HEADER DO BLOCO PJ -->
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 p-5 rounded-2xl bg-gradient-to-r from-purple-950/60 to-slate-900 border border-purple-800/30">
        <div>
          <span class="text-xs uppercase font-bold tracking-wider text-purple-400">Dashboard da Empresa (PJ)</span>
          <h2 class="text-xl font-bold text-white mt-0.5">Moura Barretto Engenharia Ltda</h2>
          <p class="text-xs text-slate-400 mt-1">Custos operacionais estruturados por tópicos de escritório, equipe e viagens.</p>
        </div>
        <div class="flex items-center gap-3">
          <div class="text-right">
            <span class="text-[11px] text-slate-400 block">Faturamento Líquido</span>
            <span class="text-xl font-bold text-white">R$ 16.560,00</span>
          </div>
          <div class="h-8 w-px bg-slate-700"></div>
          <div class="text-right">
            <span class="text-[11px] text-purple-400 block">Lucro Líquido Gerado</span>
            <span class="text-xl font-bold text-purple-400">R$ 11.885,35</span>
          </div>
        </div>
      </div>

      <!-- GRID DE TÓPICOS DA PESSOA JURÍDICA -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">

        <!-- PJ 1: EQUIPE -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">1. Equipe & Estágio</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 1.700,00</span>
              </div>
              <span class="text-base font-bold text-white">R$ 1.701,00</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Estagiária Técnica (Fernanda Mayra)</span>
                <strong class="text-white">R$ 1.621,00</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Complemento / Bolsa Estágio</span>
                <strong class="text-white">R$ 80,00</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400">
            Estrutura de equipe enxuta e alinhada ao orçamento.
          </div>
        </div>

        <!-- PJ 2: INFRAESTRUTURA -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">2. Infraestrutura & Coworking</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 650,00</span>
              </div>
              <span class="text-base font-bold text-white">R$ 624,90</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Aluguel Coworking (DW Treinamento)</span>
                <strong class="text-white">R$ 525,00</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Internet Escritório (BRT Telecomunicações)</span>
                <strong class="text-white">R$ 99,90</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400">
            Escritório físico em Pouso Alegre operando com baixo custo fixo.
          </div>
        </div>

        <!-- PJ 3: VIAGENS A TRABALHO -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">3. Viagens a Trabalho & Frota</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 500,00</span>
              </div>
              <span class="text-base font-bold text-white">R$ 948,29</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Passagens GOL (2/2: R$ 462,95 [FIM])</span>
                <strong class="text-white">R$ 709,52</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Seguro Veicular Auto (Azul Seguros 9/10)</span>
                <strong class="text-white">R$ 238,77</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-emerald-400">
            ✅ Parcela GOL 2/2 encerrou em Setembro. Em Outubro encerra a 2/3 e o seguro Azul!
          </div>
        </div>

        <!-- PJ 4: TRIBUTOS & TAXAS -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">4. Tributos, Conselhos & Taxas</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 800,00</span>
              </div>
              <span class="text-base font-bold text-white">R$ 558,84</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• CREA PF (Conselho Profissional)</span>
                <strong class="text-white">R$ 228,84</strong>
              </div>
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• INSS / DCTFWeb Empresa</span>
                <strong class="text-white">R$ 220,00</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Associação Estrutural ABECE</span>
                <strong class="text-white">R$ 110,00</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400">
            Regularidade fiscal e registro profissional do engenheiro.
          </div>
        </div>

        <!-- PJ 5: SOFTWARES & CURSOS -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">5. Softwares, TI & Cursos</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 500,00</span>
              </div>
              <span class="text-base font-bold text-white">R$ 377,14</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Pós-Graduação Técnica (IPOG)</span>
                <strong class="text-white">R$ 279,14</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Google Workspace (Drive / E-mail)</span>
                <strong class="text-white">R$ 98,00</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400">
            Ferramentas essenciais para elaboração de projetos e gestão.
          </div>
        </div>

        <!-- PJ 6: TARIFAS & OPERAÇÕES -->
        <div class="panel-card rounded-2xl p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
              <div>
                <h3 class="text-sm font-bold text-white">6. Tarifas & Operações</h3>
                <span class="text-[11px] text-slate-400">Meta: R$ 350,00</span>
              </div>
              <span class="text-base font-bold text-white">R$ 464,48</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="flex justify-between py-1 border-b border-slate-800/40 text-slate-300">
                <span>• Manutenção Conta Caixa PJ & Tarifas Pix</span>
                <strong class="text-white">R$ 84,79</strong>
              </div>
              <div class="flex justify-between py-1 text-slate-300">
                <span>• Serviços Operacionais & Deslocamento</span>
                <strong class="text-white">R$ 379,69</strong>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400">
            Pequenas despesas bancárias e operacionais do CNPJ.
          </div>
        </div>

      </div>
    </div>

    <!-- ================================================================= -->
    <!-- TAB 3: VISÃO CONSOLIDADA & METAS -->
    <!-- ================================================================= -->
    <div id="view-consolidado" class="space-y-6 hidden">
      <!-- PAINEL COMPARATIVO GERAL -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div class="panel-card rounded-2xl p-5">
          <span class="text-xs font-semibold text-slate-400 uppercase">Custo Consolidado Real (Setembro)</span>
          <div class="text-2xl font-bold text-rose-400 mt-1">R$ 27.972,79</div>
          <p class="text-xs text-slate-400 mt-2">
            Inclui a segunda parcela do carro paga no mesmo mês (R$ 2.080) e compras antigas.
          </p>
        </div>
        <div class="panel-card rounded-2xl p-5">
          <span class="text-xs font-semibold text-slate-400 uppercase">Custo Normal Recorrente</span>
          <div class="text-2xl font-bold text-sky-400 mt-1">R$ 24.466,81</div>
          <p class="text-xs text-slate-400 mt-2">
            Com apenas 1 parcela de carro e os custos de rotina atuais.
          </p>
        </div>
        <div class="panel-card rounded-2xl p-5 bg-gradient-to-br from-emerald-950/40 to-slate-900 border border-emerald-500/20">
          <span class="text-xs font-semibold text-emerald-400 uppercase">Nova Meta Planejada</span>
          <div class="text-2xl font-bold text-emerald-400 mt-1">R$ 19.662,00</div>
          <p class="text-xs text-slate-300 mt-2">
            Economia conquistada de <strong>R$ 8.310/mês</strong> sem perder padrão de vida!
          </p>
        </div>
      </div>

      <!-- CRONOGRAMA DE ALÍVIO DE PARCELAS -->
      <div class="panel-card rounded-2xl p-5">
        <h3 class="text-sm font-bold text-white mb-2">Cronograma de Queda Automática das Parcelas nos Cartões</h3>
        <p class="text-xs text-slate-400 mb-4">Veja como as faturas vão murchar sozinhas nos próximos meses sem você criar novas parcelas:</p>
        
        <div class="grid grid-cols-1 sm:grid-cols-4 gap-3 text-center">
          <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
            <span class="text-[11px] text-slate-400 block">Setembro/26 (Real)</span>
            <strong class="text-base text-rose-400">R$ 3.182,34</strong>
            <span class="text-[10px] text-slate-500 block mt-1">Casas Bahia + Promo + Sigga</span>
          </div>
          <div class="p-3 rounded-xl bg-slate-900 border border-sky-800/40">
            <span class="text-[11px] text-sky-400 block">Outubro/26 (Proj.)</span>
            <strong class="text-base text-sky-400">R$ 1.756,45</strong>
            <span class="text-[10px] text-emerald-400 block mt-1">Economia de R$ 1.425/mês</span>
          </div>
          <div class="p-3 rounded-xl bg-slate-900 border border-emerald-800/40">
            <span class="text-[11px] text-emerald-400 block">Novembro/26 (Proj.)</span>
            <strong class="text-base text-emerald-400">R$ 111,63</strong>
            <span class="text-[10px] text-emerald-400 block mt-1">Latam & Jiu-Jitsu quitados!</span>
          </div>
          <div class="p-3 rounded-xl bg-slate-900 border border-emerald-800/40">
            <span class="text-[11px] text-emerald-400 block">Dezembro/26 (Proj.)</span>
            <strong class="text-base text-emerald-400">R$ 111,63</strong>
            <span class="text-[10px] text-emerald-400 block mt-1">Cartões 100% livres de dívidas</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ================================================================= -->
    <!-- TAB 4: EXTRATO COM FILTROS EM CADA COLUNA -->
    <!-- ================================================================= -->
    <div id="view-extrato" class="space-y-4 hidden">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <h2 class="text-base font-bold text-white">Extrato & Lançamentos Detalhados</h2>
          <p class="text-xs text-slate-400">Filtre individualmente por qualquer coluna abaixo para investigar os gastos.</p>
        </div>
        <div class="relative w-full sm:w-64">
          <input type="text" id="globalSearch" placeholder="Busca rápida por texto..." onkeyup="applyColumnFilters()" class="w-full px-3 py-2 pl-8 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-500">
          <svg class="w-4 h-4 text-slate-500 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </div>
      </div>

      <!-- BARRA DE FILTROS POR COLUNAS -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-xs">
        <div>
          <label class="block text-slate-400 text-[10px] uppercase font-bold mb-1">Filtrar Entidade</label>
          <select id="colFilterEntidade" onchange="applyColumnFilters()" class="w-full px-2 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-white">
            <option value="">Todas (PF e PJ)</option>
            <option value="PF">Pessoa Física (PF)</option>
            <option value="PJ">Pessoa Jurídica (PJ)</option>
          </select>
        </div>
        <div>
          <label class="block text-slate-400 text-[10px] uppercase font-bold mb-1">Filtrar Categoria</label>
          <select id="colFilterCategoria" onchange="applyColumnFilters()" class="w-full px-2 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-white">
            <option value="">Todas as Categorias</option>
            <option value="Alimentação">Alimentação</option>
            <option value="Transporte & Veículos">Transporte & Veículos</option>
            <option value="Moradia">Moradia</option>
            <option value="Educação (Benjamim)">Educação (Benjamim)</option>
            <option value="Saúde & Bem-Estar">Saúde & Bem-Estar</option>
            <option value="Compras & Lazer">Compras & Lazer</option>
            <option value="Custos Escritório">Custos Escritório (PJ)</option>
            <option value="Receita">Receitas</option>
          </select>
        </div>
        <div>
          <label class="block text-slate-400 text-[10px] uppercase font-bold mb-1">Filtrar Conta / Cartão</label>
          <select id="colFilterConta" onchange="applyColumnFilters()" class="w-full px-2 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-white">
            <option value="">Todas as Contas</option>
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
          <label class="block text-slate-400 text-[10px] uppercase font-bold mb-1">Cruzamento de Contas</label>
          <select id="colFilterCruzamento" onchange="applyColumnFilters()" class="w-full px-2 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-white">
            <option value="">Todos os Lançamentos</option>
            <option value="PJ bancou PF">PJ bancou PF (Contas pessoais no CNPJ)</option>
            <option value="PF pagou PJ">PF pagou PJ (Contas da empresa no CPF)</option>
            <option value="Normal">Normais</option>
          </select>
        </div>
      </div>

      <!-- TABELA COM AUTO-SCROLL -->
      <div class="overflow-x-auto custom-scroll border border-slate-800 rounded-xl bg-slate-900/60">
        <table class="w-full text-left text-xs whitespace-nowrap">
          <thead class="bg-slate-900 text-slate-400 uppercase font-semibold border-b border-slate-800">
            <tr>
              <th class="px-3.5 py-2.5">Data</th>
              <th class="px-3.5 py-2.5">Entidade</th>
              <th class="px-3.5 py-2.5">Conta / Origem</th>
              <th class="px-3.5 py-2.5">Categoria</th>
              <th class="px-3.5 py-2.5">Subcategoria</th>
              <th class="px-3.5 py-2.5">Descrição</th>
              <th class="px-3.5 py-2.5 text-right">Valor (R$)</th>
              <th class="px-3.5 py-2.5">Cruzamento</th>
              <th class="px-3.5 py-2.5">Observações</th>
            </tr>
          </thead>
          <tbody id="filteredTableBody" class="divide-y divide-slate-800/60">
            <!-- Gerado via JS -->
          </tbody>
        </table>
      </div>

      <div class="flex items-center justify-between text-xs text-slate-400 pt-1">
        <span id="filteredStats">Carregando transações...</span>
        <button onclick="resetFilters()" class="text-sky-400 hover:underline">Limpar Filtros</button>
      </div>
    </div>

  </main>

  <script>
    const dataset = {json.dumps(transactions, ensure_ascii=False)};

    function formatCurrency(v) {{
      return new Intl.NumberFormat('pt-BR', {{ style: 'currency', currency: 'BRL' }}).format(v);
    }}

    function switchTab(tabId) {{
      ['pf', 'pj', 'consolidado', 'extrato'].forEach(t => {{
        document.getElementById(`view-${{t}}`).classList.add('hidden');
        document.getElementById(`tab-nav-${{t}}`).classList.remove('active');
      }});
      document.getElementById(`view-${{tabId}}`).classList.remove('hidden');
      document.getElementById(`tab-nav-${{tabId}}`).classList.add('active');

      if (tabId === 'extrato') {{
        applyColumnFilters();
      }}
    }}

    function applyColumnFilters() {{
      const fEnt = document.getElementById('colFilterEntidade').value;
      const fCat = document.getElementById('colFilterCategoria').value;
      const fCnt = document.getElementById('colFilterConta').value;
      const fCrz = document.getElementById('colFilterCruzamento').value;
      const search = document.getElementById('globalSearch').value.toLowerCase();

      const tbody = document.getElementById('filteredTableBody');
      tbody.innerHTML = '';

      let matches = dataset.filter(row => {{
        if (fEnt && row.entidade !== fEnt) return false;
        if (fCat && !row.categoria.includes(fCat) && !row.tipo.includes(fCat)) return false;
        if (fCnt && row.conta !== fCnt) return false;
        if (fCrz && !row.cruzamento.includes(fCrz)) return false;

        if (search) {{
          const str = (row.descricao + ' ' + row.categoria + ' ' + row.subcategoria + ' ' + row.conta + ' ' + row.valor).toLowerCase();
          if (!str.includes(search)) return false;
        }}
        return true;
      }});

      matches.forEach(r => {{
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-800/50 transition';

        const badgeEnt = r.entidade === 'PJ'
          ? '<span class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">PJ</span>'
          : '<span class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">PF</span>';

        let badgeCruz = '<span class="text-slate-500">—</span>';
        if (r.cruzamento.includes('PJ bancou PF')) {{
          badgeCruz = '<span class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">PJ bancou PF</span>';
        }} else if (r.cruzamento.includes('PF pagou PJ')) {{
          badgeCruz = '<span class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">PF pagou PJ</span>';
        }}

        const isRec = r.tipo === 'Receita';
        const valClass = isRec ? 'text-emerald-400 font-bold' : 'text-slate-100 font-medium';
        const valSign = isRec ? '+ ' : '- ';

        tr.innerHTML = `
          <td class="px-3.5 py-2 text-slate-400">${{r.data}}</td>
          <td class="px-3.5 py-2">${{badgeEnt}}</td>
          <td class="px-3.5 py-2 text-slate-300">${{r.conta}}</td>
          <td class="px-3.5 py-2 font-medium text-slate-200">${{r.categoria}}</td>
          <td class="px-3.5 py-2 text-slate-400">${{r.subcategoria || '—'}}</td>
          <td class="px-3.5 py-2 text-white font-medium">${{r.descricao}}</td>
          <td class="px-3.5 py-2 text-right ${{valClass}}">${{valSign}}${{formatCurrency(r.valor)}}</td>
          <td class="px-3.5 py-2">${{badgeCruz}}</td>
          <td class="px-3.5 py-2 text-slate-400 max-w-xs truncate" title="${{r.observacao || ''}}">${{r.observacao || ''}}</td>
        `;
        tbody.appendChild(tr);
      }});

      document.getElementById('filteredStats').innerText = `Exibindo ${{matches.length}} de ${{dataset.length}} lançamentos`;
    }}

    function resetFilters() {{
      document.getElementById('colFilterEntidade').value = '';
      document.getElementById('colFilterCategoria').value = '';
      document.getElementById('colFilterConta').value = '';
      document.getElementById('colFilterCruzamento').value = '';
      document.getElementById('globalSearch').value = '';
      applyColumnFilters();
    }}

    window.onload = function() {{
      applyColumnFilters();
    }};
  </script>
</body>
</html>
'''
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("index.html V2 gerado com sucesso!")

if __name__ == '__main__':
    generate_v2_web_app()
