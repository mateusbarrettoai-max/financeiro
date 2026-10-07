import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_master_workbook():
    wb = openpyxl.Workbook()
    
    # -------------------------------------------------------------
    # Paleta de Cores e Estilos Elegantes
    # -------------------------------------------------------------
    NAVY_DARK = '1E293B'      # Slate 800
    NAVY_LIGHT = '334155'     # Slate 700
    BLUE_ACCENT = '0284C7'    # Sky 600
    BLUE_LIGHT = 'E0F2FE'     # Sky 100
    GREEN_ACCENT = '059669'   # Emerald 600
    GREEN_LIGHT = 'D1FAE5'    # Emerald 100
    RED_ACCENT = 'E11D48'     # Rose 600
    RED_LIGHT = 'FFE4E6'      # Rose 100
    GRAY_HEADER = 'F1F5F9'    # Slate 100
    GRAY_BORDER = 'CBD5E1'    # Slate 300
    WHITE = 'FFFFFF'
    PURPLE_ACCENT = '7C3AED'  # Violet 600
    PURPLE_LIGHT = 'EDE9FE'   # Violet 100
    
    font_title = Font(name='Segoe UI', size=16, bold=True, color='0F172A')
    font_subtitle = Font(name='Segoe UI', size=11, italic=True, color='64748B')
    font_section = Font(name='Segoe UI', size=12, bold=True, color=NAVY_DARK)
    font_header = Font(name='Segoe UI', size=10, bold=True, color=WHITE)
    font_body = Font(name='Segoe UI', size=10, color='1E293B')
    font_body_bold = Font(name='Segoe UI', size=10, bold=True, color='1E293B')
    font_kpi_num = Font(name='Segoe UI', size=18, bold=True, color=NAVY_DARK)
    font_kpi_label = Font(name='Segoe UI', size=9, bold=True, color='64748B')
    
    fill_header_navy = PatternFill(start_color=NAVY_DARK, end_color=NAVY_DARK, fill_type='solid')
    fill_header_blue = PatternFill(start_color=BLUE_ACCENT, end_color=BLUE_ACCENT, fill_type='solid')
    fill_header_green = PatternFill(start_color=GREEN_ACCENT, end_color=GREEN_ACCENT, fill_type='solid')
    fill_header_purple = PatternFill(start_color=PURPLE_ACCENT, end_color=PURPLE_ACCENT, fill_type='solid')
    fill_zebra = PatternFill(start_color='F8FAFC', end_color='F8FAFC', fill_type='solid')
    fill_highlight_green = PatternFill(start_color=GREEN_LIGHT, end_color=GREEN_LIGHT, fill_type='solid')
    fill_highlight_red = PatternFill(start_color=RED_LIGHT, end_color=RED_LIGHT, fill_type='solid')
    fill_highlight_blue = PatternFill(start_color=BLUE_LIGHT, end_color=BLUE_LIGHT, fill_type='solid')
    fill_highlight_purple = PatternFill(start_color=PURPLE_LIGHT, end_color=PURPLE_LIGHT, fill_type='solid')
    fill_card = PatternFill(start_color='F8FAFC', end_color='F8FAFC', fill_type='solid')

    border_thin = Side(border_style='thin', color=GRAY_BORDER)
    border_double = Side(border_style='double', color=NAVY_DARK)
    box_border = Border(left=border_thin, right=border_thin, top=border_thin, bottom=border_thin)
    bottom_double_border = Border(top=border_thin, bottom=border_double)
    
    align_center = Alignment(horizontal='center', vertical='center')
    align_left = Alignment(horizontal='left', vertical='center')
    align_right = Alignment(horizontal='right', vertical='center')
    align_wrap = Alignment(horizontal='left', vertical='center', wrap_text=True)

    CURR_FMT = 'R$ #,##0.00'
    PCT_FMT = '0.0%'
    DATE_FMT = 'DD/MM/YYYY'

    # =============================================================
    # 1. ABA: DASHBOARD
    # =============================================================
    ws_dash = wb.active
    ws_dash.title = 'Dashboard'
    ws_dash.views.sheetView[0].showGridLines = True

    ws_dash['B2'] = "PAINEL FINANCEIRO EXECUTIVO — SETEMBRO DE 2026"
    ws_dash['B2'].font = font_title
    ws_dash['B3'] = "Moura Barretto Engenharia Ltda (PJ) & Mateus Moura Barretto (PF)"
    ws_dash['B3'].font = font_subtitle

    # KPI CARDS
    # Card 1: Faturamento Operacional
    kpis = [
        ("B5", "D6", "FATURAMENTO LÍQUIDO OPERACIONAL", "=SUM(Lancamentos!J2:J4)", fill_highlight_green, font_section, GREEN_ACCENT),
        ("E5", "G6", "DESPESAS OPERACIONAIS PJ", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!F:F, \"Despesa\")", fill_highlight_blue, font_section, BLUE_ACCENT),
        ("H5", "J6", "LUCRO LÍQUIDO PJ GERADO", "=B6-E6", fill_highlight_purple, font_section, PURPLE_ACCENT),
        ("K5", "M6", "CUSTO DE VIDA PF (REALIZADO)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!F:F, \"Despesa\")", fill_highlight_red, font_section, RED_ACCENT),
    ]

    for start_c, end_c, title, form, fill_col, font_c, col_border in kpis:
        c1, r1 = start_c[0], int(start_c[1:])
        c2, r2 = end_c[0], int(end_c[1:])
        ws_dash.merge_cells(f"{start_c}:{end_c[0]}{r1}")
        ws_dash.merge_cells(f"{start_c[0]}{r2}:{end_c}")
        
        lbl_cell = ws_dash[start_c]
        lbl_cell.value = title
        lbl_cell.font = font_kpi_label
        lbl_cell.alignment = align_center
        lbl_cell.fill = fill_col
        
        val_cell = ws_dash[f"{start_c[0]}{r2}"]
        val_cell.value = form
        val_cell.font = Font(name='Segoe UI', size=16, bold=True, color=col_border)
        val_cell.number_format = CURR_FMT
        val_cell.alignment = align_center
        val_cell.fill = fill_col

    # Sub-resumo Executivo
    ws_dash['B8'] = "RESUMO E CONCILIAÇÃO FINANCEIRA MÊS A MÊS"
    ws_dash['B8'].font = font_section

    dash_headers = ["Indicador / Conceito", "PJ (Escritório)", "PF (Pessoal)", "Consolidado Geral", "Observações Estratégicas"]
    for col_idx, text in enumerate(dash_headers, start=2):
        cell = ws_dash.cell(row=9, column=col_idx, value=text)
        cell.font = font_header
        cell.fill = fill_header_navy
        cell.alignment = align_center
        cell.border = box_border

    dre_rows = [
        ("Receita Bruta / Entradas de Projetos", "=Lancamentos!J2+Lancamentos!J3", "=Lancamentos!J4", "=C10+D10", "Grado (R$ 7.200) + Wise Portugal 1575 € (~R$ 9.360)"),
        ("(-) Custos Operacionais da Empresa", "=E6", 0.00, "=C11+D11", "Equipe, Coworking, Softwares, Tributos, Viagens trabalho"),
        ("(=) Lucro Líquido Operacional PJ", "=C10-C11", "—", "=C12", "Capacidade real da empresa remunerar o sócio"),
        ("(-) Despesas Pessoais Pagas pela PJ", "=Conciliacao_PF_PJ!C7", "—", "=C13", "Carro RCI, Ocean Breeze, CEMIG, Lutas pagos no CNPJ"),
        ("(-) Pró-labore Direto Transferido (Pix)", "=Conciliacao_PF_PJ!C8", "—", "=C14", "Retiradas financeiras em conta"),
        ("(=) Total Transferido da PJ para PF", "=C13+C14", "—", "=C15", "Remuneração Total Realizada do Sócio no mês"),
        ("Total de Gastos de Vida PF no Mês", "—", "=K6", "=D16", "Moradia, Alimentação, Benjamim, Saúde, Carro, Lazer"),
        ("Alívio Imediato: Parcelas Encerradas em Setembro", "—", 1425.89, 1425.89, "Casas Bahia (R$ 678), Promo (R$ 633), Moda Infantil (R$ 113)"),
        ("Projeção de Fatura PF Pós-Alívio (Outubro)", "—", "=D16-D17", "=D18", "Custo projetado com término dessas 3 parcelas antigas"),
    ]

    for idx, (label, pj_val, pf_val, tot_val, obs) in enumerate(dre_rows, start=10):
        ws_dash.cell(row=idx, column=2, value=label).font = font_body_bold if '(=)' in label else font_body
        
        c3 = ws_dash.cell(row=idx, column=3, value=pj_val)
        c4 = ws_dash.cell(row=idx, column=4, value=pf_val)
        c5 = ws_dash.cell(row=idx, column=5, value=tot_val)
        c6 = ws_dash.cell(row=idx, column=6, value=obs)
        
        for c in [c3, c4, c5]:
            if str(c.value).startswith('=') or str(c.value).startswith('R$'):
                c.number_format = CURR_FMT
                c.alignment = align_right
            else:
                c.alignment = align_center
            c.font = font_body_bold if '(=)' in label else font_body
            
        c6.font = font_subtitle
        c6.alignment = align_left

        if '(=)' in label:
            for col_i in range(2, 7):
                ws_dash.cell(row=idx, column=col_i).fill = fill_highlight_purple

        for col_i in range(2, 7):
            ws_dash.cell(row=idx, column=col_i).border = box_border

    # Comparativo Rápido Orçado vs Realizado de Setembro
    ws_dash['B21'] = "COMPARATIVO: META / ORÇAMENTO BASE vs. REALIZADO (SETEMBRO/2026)"
    ws_dash['B21'].font = font_section

    comp_headers = ["Macro-Categoria", "Tipo", "Orçamento Base (Meta)", "Realizado Setembro", "Diferença (R$)", "Status / Diagnóstico"]
    for col_idx, text in enumerate(comp_headers, start=2):
        cell = ws_dash.cell(row=22, column=col_idx, value=text)
        cell.font = font_header
        cell.fill = fill_header_blue
        cell.alignment = align_center
        cell.border = box_border

    comp_data = [
        ("Moradia & Habitação", "PF", 6973.33, "=SUMIFS(Lancamentos!J:J, Lancamentos!G:G, \"Moradia\")", "Dentro do limite (Casa SSA/Ocean Breeze e aluguel)", fill_highlight_green),
        ("Alimentação (Mercados + Restaurantes)", "PF", 5000.00, "=SUMIFS(Lancamentos!J:J, Lancamentos!G:G, \"Alimentação\")", "Supermercados (Mart Minas/Buritis) + Lazer", fill_highlight_green),
        ("Saúde & Bem-Estar", "PF", 2510.00, "=SUMIFS(Lancamentos!J:J, Lancamentos!G:G, \"Saúde & Bem-Estar\")", "Unimed (R$ 1.546) + Farmácias + Lutas/Jiu-jitsu", fill_highlight_blue),
        ("Educação (Benjamim)", "PF", 2437.29, "=SUMIFS(Lancamentos!J:J, Lancamentos!G:G, \"Educação (Benjamim)\")", "Escola (R$ 1.870) + Inglês (R$ 240) + Vestuário", fill_highlight_green),
        ("Transporte & Veículo", "PF", 4000.00, "=SUMIFS(Lancamentos!J:J, Lancamentos!G:G, \"Transporte & Veículos\")", "Carro Nissan RCI + Combustíveis nos postos", fill_highlight_blue),
        ("Compras Pessoais, Lazer & Parcelas", "PF", 3750.00, "=SUMIFS(Lancamentos!J:J, Lancamentos!G:G, \"Compras & Lazer\")", "Parcelas antigas que já terminaram", fill_highlight_green),
        ("Custos Operacionais Escritório", "PJ", 5689.00, "=E6", "Abaixo do orçado! (Meta R$ 5.689 vs Real R$ 4.674)", fill_highlight_green),
        ("TOTAL GERAL", "PF+PJ", "=SUM(D23:D29)", "=SUM(E23:E29)", "Controle orçamentário consolidado", fill_highlight_purple),
    ]

    for idx, (cat, ent, meta, form_real, diag, fill_row) in enumerate(comp_data, start=23):
        ws_dash.cell(row=idx, column=2, value=cat).font = font_body_bold if idx==30 else font_body
        ws_dash.cell(row=idx, column=3, value=ent).alignment = align_center
        
        c_meta = ws_dash.cell(row=idx, column=4, value=meta)
        c_meta.number_format = CURR_FMT
        c_meta.alignment = align_right
        
        c_real = ws_dash.cell(row=idx, column=5, value=form_real)
        c_real.number_format = CURR_FMT
        c_real.alignment = align_right
        
        c_dif = ws_dash.cell(row=idx, column=6, value=f"=D{idx}-E{idx}")
        c_dif.number_format = CURR_FMT
        c_dif.alignment = align_right
        
        c_diag = ws_dash.cell(row=idx, column=7, value=diag)
        c_diag.font = font_subtitle
        
        if idx == 30:
            for col_i in range(2, 8):
                ws_dash.cell(row=idx, column=col_i).fill = fill_highlight_purple
                ws_dash.cell(row=idx, column=col_i).font = font_body_bold
                ws_dash.cell(row=idx, column=col_i).border = bottom_double_border
        else:
            for col_i in range(2, 8):
                ws_dash.cell(row=idx, column=col_i).border = box_border

    # =============================================================
    # 2. ABA: LANCAMENTOS
    # =============================================================
    ws_lanc = wb.create_sheet(title='Lancamentos')
    ws_lanc.views.sheetView[0].showGridLines = True

    lanc_headers = [
        "ID", "Data", "Competência", "Conta / Meio", "Entidade", 
        "Tipo", "Categoria", "Subcategoria", "Descrição / Estabelecimento", 
        "Valor (R$)", "Conta Pagadora", "Cruzamento PF/PJ", "Status", "Observações Detalhadas"
    ]

    for col_idx, text in enumerate(lanc_headers, start=1):
        cell = ws_lanc.cell(row=1, column=col_idx, value=text)
        cell.font = font_header
        cell.fill = fill_header_navy
        cell.alignment = align_center
        cell.border = box_border

    # Dados reais compilados de todas as fontes de Setembro
    transactions = [
        # --- RECEITAS ---
        ("2026-09-21", "09/2026", "Conta Caixa PJ", "PJ", "Receita", "Receita Operacional", "Projetos Nacionais", "Grado Engenharia - Reforma Prédio Ondina (Rampa)", 3500.00, "Conta Caixa PJ", "Normal PJ", "Liquidado", "TED recebida"),
        ("2026-09-21", "09/2026", "Conta Caixa PJ", "PJ", "Receita", "Receita Operacional", "Projetos Nacionais", "Grado Engenharia - Reforma Prédio Ondina (Mezanino)", 3700.00, "Conta Caixa PJ", "Normal PJ", "Liquidado", "TED recebida"),
        ("2026-09-04", "09/2026", "Wise Portugal", "PJ", "Receita", "Receita Internacional", "Projetos Internacionais", "TDP Braga (Portugal) - 1.575,00 Euros", 9360.00, "Wise / PF", "Normal PJ", "Liquidado", "Contrato recorrente internacional"),

        # --- DESPESAS PJ OPERACIONAIS ---
        ("2026-09-04", "09/2026", "Conta Caixa PJ", "PJ", "Despesa", "Custos Escritório", "Equipe & Estágio", "Fernanda Mayra Campos Barretto (Estagiária)", 1621.00, "Conta Caixa PJ", "Normal PJ", "Liquidado", "Bolsa de estágio mensal"),
        ("2026-09-23", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Equipe & Estágio", "Fernanda Mayra Campos Barretto", 80.00, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Complemento estágio / reembolso"),
        ("2026-09-04", "09/2026", "Conta Nubank PF", "PJ", "Despesa", "Custos Escritório", "Infraestrutura / Coworking", "D W Treinamento e Desenvolvimento Ltda (Coworking)", 525.00, "Conta Nubank PF", "PF pagou PJ", "Liquidado", "Aluguel escritório Pouso Alegre pago via PF"),
        ("2026-09-04", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Conectividade / Internet", "BRT Telecomunicações / CVS Telecom (Internet)", 99.90, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Internet Pouso Alegre"),
        ("2026-09-02", "09/2026", "Cartão Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Softwares & TI", "Google Workspace (GSuite / Drive / E-mail)", 98.00, "Cartão Nubank PJ", "Normal PJ", "Liquidado", "Assinatura mensal Google"),
        ("2026-09-04", "09/2026", "Conta Nubank PF", "PJ", "Despesa", "Custos Escritório", "Tributos & Taxas", "Receita Federal - INSS / DCTFWeb Moura Barretto", 220.00, "Conta Nubank PF", "PF pagou PJ", "Liquidado", "Tributo da empresa pago com conta pessoal"),
        ("2026-09-04", "09/2026", "Conta Nubank PF", "PJ", "Despesa", "Custos Escritório", "Tributos & Taxas", "CREA PF (Conselho Regional de Engenharia)", 228.84, "Conta Nubank PF", "PF pagou PJ", "Liquidado", "Anuidade profissional engenharia"),
        ("2026-08-28", "09/2026", "Conta Nubank PF", "PJ", "Despesa", "Custos Escritório", "Tributos & Taxas", "ABECE - Associação Bras. Engenharia Estrutural", 110.00, "Conta Nubank PF", "PF pagou PJ", "Liquidado", "Associação de classe técnica"),
        ("2026-09-04", "09/2026", "Conta Caixa PJ", "PJ", "Despesa", "Custos Escritório", "Capacitação & Cursos", "IPOG (Pós-graduação / Especialização Técnica)", 279.14, "Conta Caixa PJ", "Normal PJ", "Liquidado", "Curso técnico engenharia"),
        ("2026-09-25", "09/2026", "Conta Caixa PJ", "PJ", "Despesa", "Custos Escritório", "Tarifas Bancárias", "Tarifa Manutenção Conta Caixa PJ", 73.00, "Conta Caixa PJ", "Normal PJ", "Liquidado", "Tarifa de cesta PJ"),
        ("2026-09-04", "09/2026", "Conta Caixa PJ", "PJ", "Despesa", "Custos Escritório", "Tarifas Bancárias", "Tarifa Pix Caixa PJ", 8.50, "Conta Caixa PJ", "Normal PJ", "Liquidado", "Tarifa transferência Pix"),
        ("2026-09-28", "09/2026", "Conta Caixa PJ", "PJ", "Despesa", "Custos Escritório", "Tarifas Bancárias", "Tarifa Pix Caixa PJ", 1.78, "Conta Caixa PJ", "Normal PJ", "Liquidado", "Tarifa transferência Pix"),
        ("2026-09-30", "09/2026", "Conta Caixa PJ", "PJ", "Despesa", "Custos Escritório", "Tarifas Bancárias", "Tarifa Pix Caixa PJ", 1.51, "Conta Caixa PJ", "Normal PJ", "Liquidado", "Tarifa transferência Pix"),
        ("2026-08-31", "09/2026", "Cartão Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Viagens & Deslocamento", "Gol Linhas Aéreas - Parcela 2/2", 462.95, "Cartão Nubank PJ", "Normal PJ", "Liquidado", "ÚLTIMA PARCELA 2/2 - Concluída"),
        ("2026-08-31", "09/2026", "Cartão Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Viagens & Deslocamento", "Gol Linhas Aéreas - Parcela 2/3", 246.57, "Cartão Nubank PJ", "Normal PJ", "Liquidado", "Parcela 2 de 3 (Encerra em Out)"),
        ("2026-08-31", "09/2026", "Cartão Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Operação & Frota", "Azul Seguros - Parcela 9/10", 238.77, "Cartão Nubank PJ", "Normal PJ", "Liquidado", "Seguro auto parcela 9 de 10"),
        ("2026-09-03", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Serviços Operacionais", "Luciano de Oliveira Leite (Mercado Pago)", 75.00, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Serviço operacional"),
        ("2026-09-03", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Serviços Operacionais", "Solver Instituição de Pagamentos", 62.80, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Serviço operacional"),
        ("2026-09-03", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Serviços Operacionais", "Solver Instituição de Pagamentos", 39.53, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Serviço operacional"),
        ("2026-09-01", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Alimentação Operacional", "iFood Escritório", 15.89, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Refeição em trabalho"),
        ("2026-09-02", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Alimentação Operacional", "iFood Escritório", 12.89, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Refeição em trabalho"),
        ("2026-09-19", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Deslocamento Operacional", "Anilton de Paula Martins", 94.60, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Deslocamento"),
        ("2026-09-19", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Deslocamento Operacional", "Ueder Alcantara Cassiano", 26.00, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Deslocamento"),
        ("2026-09-19", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Deslocamento Operacional", "Ueder Alcantara Cassiano", 39.00, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Deslocamento"),
        ("2026-09-19", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Deslocamento Operacional", "Emerson Rodrigo Cardoso", 6.00, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Deslocamento"),
        ("2026-09-19", "09/2026", "Conta Nubank PJ", "PJ", "Despesa", "Custos Escritório", "Deslocamento Operacional", "Mercadinho 24h", 7.98, "Conta Nubank PJ", "Normal PJ", "Liquidado", "Despesa em trânsito"),

        # --- DESPESAS PESSOAIS (PF) PAGAS PELA EMPRESA (PJ BANCOU PF) ---
        ("2026-09-01", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Transporte & Veículos", "Parcela Carro", "Banco RCI Brasil (Parcela Financiamento)", 2080.09, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Parcela mensal regular do veículo"),
        ("2026-09-28", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Transporte & Veículos", "Parcela Carro", "Banco RCI Brasil (Parcela Financiamento 2)", 2080.09, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Parcela adiantada/regularizada do carro"),
        ("2026-09-04", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Moradia", "Imóvel Salvador", "Costa Azul Salvador / Ocean Breeze", 1662.67, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Condomínio/Parcela imóvel SSA pago no PJ"),
        ("2026-09-18", "09/2026", "Conta Nubank PJ", "PF", "Despesa", "Moradia", "Aluguel Residencial", "Joelma Pereira de Aquino Souza (Aluguel)", 800.00, "Conta Nubank PJ", "PJ bancou PF", "Liquidado", "Aluguel residencial pago no PJ"),
        ("2026-09-30", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Moradia", "Energia Elétrica", "CEMIG Distribuição MG (Conta 1)", 382.80, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Energia residencial Pouso Alegre"),
        ("2026-09-30", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Moradia", "Energia Elétrica", "CEMIG Distribuição MG (Conta 2)", 174.21, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Energia residencial"),
        ("2026-09-18", "09/2026", "Conta Nubank PJ", "PF", "Despesa", "Saúde & Bem-Estar", "Atividades Físicas", "Escola Respect 4 Jiu-Jitsu", 500.00, "Conta Nubank PJ", "PJ bancou PF", "Liquidado", "Jiu-jitsu pago no Nubank PJ"),
        ("2026-09-30", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Saúde & Bem-Estar", "Atividades Físicas", "Escola de Lutas BL", 169.90, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Mensalidade de lutas na Caixa PJ"),
        ("2026-09-03", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Mega Posto (Débito)", 100.00, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Abastecimento carro"),
        ("2026-09-03", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Posto Conceição (Débito)", 100.00, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Abastecimento carro"),
        ("2026-09-03", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Transporte & Veículos", "Pedágio", "Concessionária Bahia Norte (Débito)", 7.70, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Pedágio na estrada"),
        ("2026-09-26", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 73.31, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Compra de mercado na Caixa PJ"),
        ("2026-09-26", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Alimentação", "Diversos", "Nayara Pereira do", 39.00, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Despesa pessoal na Caixa PJ"),
        ("2026-09-26", "09/2026", "Conta Caixa PJ", "PF", "Despesa", "Alimentação", "Diversos", "Nayara Pereira do", 18.00, "Conta Caixa PJ", "PJ bancou PF", "Liquidado", "Despesa pessoal na Caixa PJ"),

        # --- DESPESAS PESSOAIS (PF) PAGAS VIA CONTA NUBANK PF / CAIXA PF ---
        ("2026-09-21", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Educação (Benjamim)", "Escola", "Associação das Obras Sociais (Escola Benjamim)", 1870.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Mensalidade escolar Benjamim"),
        ("2026-09-15", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Educação (Benjamim)", "Cursos", "Spectrum Line Language Center (Inglês)", 240.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Curso de inglês Benjamim"),
        ("2026-09-10", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Saúde & Bem-Estar", "Plano de Saúde", "Unimed Pouso Alegre (Boleto 1/3)", 791.72, "Conta Nubank PF", "Normal PF", "Liquidado", "Plano de saúde família"),
        ("2026-09-10", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Saúde & Bem-Estar", "Plano de Saúde", "Unimed Pouso Alegre (Boleto 2/3)", 470.79, "Conta Nubank PF", "Normal PF", "Liquidado", "Plano de saúde família"),
        ("2026-09-10", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Saúde & Bem-Estar", "Plano de Saúde", "Unimed Pouso Alegre (Boleto 3/3)", 284.32, "Conta Nubank PF", "Normal PF", "Liquidado", "Plano de saúde família"),
        ("2026-09-04", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Saúde & Bem-Estar", "Previdência Privada", "BB Previdência - Banco do Brasil", 226.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Previdência complementar privada"),
        ("2026-09-04", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Moradia", "Conectividade / Telefone", "TIM S/A (Plano Celular)", 64.99, "Conta Nubank PF", "Normal PF", "Liquidado", "Telefonia celular"),
        ("2026-09-14", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Saúde & Bem-Estar", "Atividades Físicas", "Escola Respect 4 Jiu-Jitsu", 3.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Taxa atividade"),
        ("2026-09-14", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "André Fernandes Poppinger", 150.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Alimentação"),
        ("2026-09-12", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Compras & Lazer", "Vestuário / Casa", "Bianca Almeida de Moura", 100.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Pessoal"),
        ("2026-09-14", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Cirilo Carlos Oliveira dos Santos", 30.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Julio Silvério da Silva", 35.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Julio Silvério da Silva", 14.30, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Otto Ude Neto", 27.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Arquidiocese de Pouso Alegre", 20.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Doação / Bazar"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Josuel Alexandre Garcia", 20.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Jose Messias da Rosa", 17.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Joao Cezario Gomes", 16.50, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Samara de Cassia Pereira Silva", 12.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-13", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Feira / Padaria", "Joao Batista da Silva", 10.00, "Conta Nubank PF", "Normal PF", "Liquidado", "Feira"),
        ("2026-09-16", "09/2026", "Conta Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Mercadinho 24h", 23.98, "Conta Nubank PF", "Normal PF", "Liquidado", "Mercado"),

        # --- CARTÃO CAIXA PF ---
        ("2026-08-28", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Hortifruti / Feira", "Supermercado Verds Fru (Feira de Santana)", 88.20, "Cartão Caixa PF", "Normal PF", "Liquidado", "Hortifruti"),
        ("2026-08-28", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Diversos", "Ivanildo de Almeida C", 36.50, "Cartão Caixa PF", "Normal PF", "Liquidado", "Alimentação"),
        ("2026-08-28", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Saúde & Bem-Estar", "Farmácia", "Pague Menos Farmácia", 150.16, "Cartão Caixa PF", "Normal PF", "Liquidado", "Medicamentos"),
        ("2026-09-03", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "DoceGelato (Camaçari)", 15.46, "Cartão Caixa PF", "Normal PF", "Liquidado", "Lanches"),
        ("2026-09-03", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Sal e Brasa Express (Camaçari)", 50.00, "Cartão Caixa PF", "Normal PF", "Liquidado", "Almoço / Refeição"),
        ("2026-09-03", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Transporte & Veículos", "Pedágio", "Concessionaria Bahia Norte", 7.70, "Cartão Caixa PF", "Normal PF", "Liquidado", "Pedágio"),
        ("2026-09-03", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Sal e Brasa Express (Camaçari)", 5.00, "Cartão Caixa PF", "Normal PF", "Liquidado", "Lanches"),
        ("2026-09-05", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Pizza Hut Aeroporto Guarulhos", 45.09, "Cartão Caixa PF", "Normal PF", "Liquidado", "Refeição viagem"),
        ("2026-09-05", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Subway Aeroporto Salvador", 37.00, "Cartão Caixa PF", "Normal PF", "Liquidado", "Refeição viagem"),
        ("2026-09-05", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Cappta Vovo Dalva Comida", 38.00, "Cartão Caixa PF", "Normal PF", "Liquidado", "Refeição"),
        ("2026-09-05", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Tabuleiro Sabor da Bahia", 12.00, "Cartão Caixa PF", "Normal PF", "Liquidado", "Refeição"),
        ("2026-09-05", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Qsq Aero Salvador", 6.00, "Cartão Caixa PF", "Normal PF", "Liquidado", "Refeição viagem"),
        ("2026-09-06", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Rei do Mate T3 Mezanino GRU", 36.90, "Cartão Caixa PF", "Normal PF", "Liquidado", "Café viagem"),
        ("2026-09-06", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "GRSA Baguettes São Paulo", 48.50, "Cartão Caixa PF", "Normal PF", "Liquidado", "Refeição viagem"),
        ("2026-09-06", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Transporte & Veículos", "Passagens Terrestres", "A V Braganca TTE (Ônibus SP/Pouso Alegre)", 94.90, "Cartão Caixa PF", "Normal PF", "Liquidado", "Passagem interestadual"),
        ("2026-09-07", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Compras & Lazer", "Pets / Agropecuária", "Agropecuaria Santa Edwiges", 204.00, "Cartão Caixa PF", "Normal PF", "Liquidado", "Ração / Animais"),
        ("2026-09-12", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 16.99, "Cartão Caixa PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-12", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Supermercados", "Minimercado Sao Vicente", 37.45, "Cartão Caixa PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-12", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 102.00, "Cartão Caixa PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-25", "09/2026", "Cartão Caixa PF", "PF", "Despesa", "Compras & Lazer", "Tarifas Cartão", "Anuidade Nacional Titular (02/12)", 5.25, "Cartão Caixa PF", "Normal PF", "Liquidado", "Anuidade cartão"),

        # --- CARTÃO NUBANK PF (FATURA OUTUBRO/26 - GASTOS SETEMBRO) ---
        # Parcelamentos que impactaram setembro
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Parcelamentos Antigos", "Grupo Casas Bahia - Parcela 10/10", 678.77, "Cartão Nubank PF", "Normal PF", "Liquidado", "ÚLTIMA PARCELA 10/10 - ENCERRADA! Alívio em Outubro"),
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Parcelamentos Antigos", "Vai de Promo - Parcela 3/3", 633.97, "Cartão Nubank PF", "Normal PF", "Liquidado", "ÚLTIMA PARCELA 3/3 - ENCERRADA! Alívio em Outubro"),
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Educação (Benjamim)", "Vestuário Infantil", "Sigga Moda Infantil - Parcela 4/4", 113.15, "Cartão Nubank PF", "Normal PF", "Liquidado", "ÚLTIMA PARCELA 4/4 - ENCERRADA! Alívio em Outubro"),
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Passagens Aéreas", "Latam Linhas Aéreas - Parcela 3/4", 426.53, "Cartão Nubank PF", "Normal PF", "Liquidado", "Parcela 3 de 4 (Última parcela em Outubro)"),
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Parcelamentos Antigos", "Pg *Pza Comercio - Parcela 3/6", 111.63, "Cartão Nubank PF", "Normal PF", "Liquidado", "Parcela 3 de 6"),
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Saúde & Bem-Estar", "Atividades Físicas", "Respect 4 Jiu-Jitsu - Parcela 2/3", 165.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Parcela 2 de 3 (Encerra em Outubro)"),
        
        # Gastos do dia a dia no Cartão Nubank PF
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Streaming / Assinaturas", "Amazon Prime Canais", 19.99, "Cartão Nubank PF", "Normal PF", "Liquidado", "Assinatura streaming"),
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Mobilidade Urbana", "Uber - NuPay", 14.89, "Cartão Nubank PF", "Normal PF", "Liquidado", "Corrida Uber"),
        ("2026-08-31", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Mobilidade Urbana", "Uber - NuPay", 13.82, "Cartão Nubank PF", "Normal PF", "Liquidado", "Corrida Uber"),
        ("2026-09-01", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Posto Pedra Forte II", 100.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-01", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 15.60, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-01", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 4.19, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-01", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Rosinairibeir", 17.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Padaria"),
        ("2026-09-02", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Mobilidade Urbana", "Uber - NuPay", 12.92, "Cartão Nubank PF", "Normal PF", "Liquidado", "Corrida Uber"),
        ("2026-09-02", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 94.20, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-02", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 31.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-02", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "50677684 Adriano Cesar", 22.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Alimentação"),
        ("2026-09-03", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Pastelzinho", 23.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Lanches"),
        ("2026-09-04", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Auto Posto Mariano", 152.81, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-04", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Saúde & Bem-Estar", "Farmácia", "Drogaria Nossa Senhora", 127.94, "Cartão Nubank PF", "Normal PF", "Liquidado", "Medicamentos"),
        ("2026-09-04", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Restaurante Cardeal", 79.60, "Cartão Nubank PF", "Normal PF", "Liquidado", "Almoço"),
        ("2026-09-05", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Edevaldo Jose da Mota", 78.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Alimentação"),
        ("2026-09-05", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Ice Bom Sorvetes", 25.27, "Cartão Nubank PF", "Normal PF", "Liquidado", "Sorveteria"),
        ("2026-09-05", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Farmácia / Cosméticos", "Perfumaria Sao Paulo L", 7.99, "Cartão Nubank PF", "Normal PF", "Liquidado", "Higiene / Cosméticos"),
        ("2026-09-06", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Mart Minas (Atacado - Compra do Mês)", 1369.38, "Cartão Nubank PF", "Normal PF", "Liquidado", "Compra principal da casa"),
        ("2026-09-06", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 253.40, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado reposição"),
        ("2026-09-06", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Auto Posto Mariano", 50.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-07", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Moradia", "Conectividade / Telefone", "Tim *75992503292", 60.35, "Cartão Nubank PF", "Normal PF", "Liquidado", "Recarga / Telefonia"),
        ("2026-09-07", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Abastecedora Jaborandi", 84.03, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-08", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Compras Online", "Mercado Livre *Serversi", 129.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Compra online"),
        ("2026-09-08", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Rodrigues Rodrigues Su", 77.93, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-08", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Diversos", "de Paula Comercio", 46.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Comércio"),
        ("2026-09-09", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Rosinairibeir", 17.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Padaria"),
        ("2026-09-09", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Diversos", "43 839 29 Marlon Nery", 45.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Serviço"),
        ("2026-09-10", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Pg *Cantina do Bila", 53.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Refeição"),
        ("2026-09-10", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 52.39, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-10", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Rosinairibeir", 18.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Padaria"),
        ("2026-09-11", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Auto Posto Mariano", 157.83, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-11", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Auto Posto Mariano", 105.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-11", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Pets / Agropecuária", "Petagro", 79.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Petshop / Rações"),
        ("2026-09-11", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Rodrigues Rodrigues Su", 39.49, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-12", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Edevaldo Jose da Mota", 72.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Alimentação"),
        ("2026-09-12", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Churros Balducci", 30.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Sobremesa"),
        ("2026-09-12", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Rosinairibeir", 13.50, "Cartão Nubank PF", "Normal PF", "Liquidado", "Padaria"),
        ("2026-09-13", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Streaming / Assinaturas", "Netflix.Com", 44.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Streaming"),
        ("2026-09-13", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Streaming / Assinaturas", "Ebn *Spotify", 40.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Música"),
        ("2026-09-13", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 44.94, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-14", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Streaming / Assinaturas", "Paramount+", 34.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Streaming"),
        ("2026-09-14", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Dirceíagarcia", 21.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Alimentação"),
        ("2026-09-15", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Rodrigues Rodrigues Su", 57.64, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-15", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 45.62, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-15", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Educação (Benjamim)", "Material Escolar", "Papelaria Lapis de Cor", 26.05, "Cartão Nubank PF", "Normal PF", "Liquidado", "Material escolar"),
        ("2026-09-16", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Casa & Utilidades", "Bazar Paraiso", 66.95, "Cartão Nubank PF", "Normal PF", "Liquidado", "Utilidades domésticas"),
        ("2026-09-16", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Casa & Utilidades", "Jomar Tecidos", 30.36, "Cartão Nubank PF", "Normal PF", "Liquidado", "Tecidos / Casa"),
        ("2026-09-17", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Auto Posto Mariano", 150.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-17", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Educação (Benjamim)", "Lazer / Infantil", "Point da Molekada", 99.87, "Cartão Nubank PF", "Normal PF", "Liquidado", "Brinquedos / Infantil"),
        ("2026-09-17", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Pg *Cantina do Bila", 53.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Refeição"),
        ("2026-09-17", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Casa & Utilidades", "Bazar Paraiso", 50.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Utilidades"),
        ("2026-09-18", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 91.36, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-19", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "El Ternazo Buritis", 228.79, "Cartão Nubank PF", "Normal PF", "Liquidado", "Churrascaria / Restaurante"),
        ("2026-09-19", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 29.37, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-19", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Pastelzinho", 28.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Lanches"),
        ("2026-09-20", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Restaurante Bom Apetit", 82.50, "Cartão Nubank PF", "Normal PF", "Liquidado", "Almoço domingo"),
        ("2026-09-20", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Mp *Tilaineebotta", 50.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Lanches"),
        ("2026-09-20", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Ice Bom Sorvetes", 44.40, "Cartão Nubank PF", "Normal PF", "Liquidado", "Sorveteria"),
        ("2026-09-20", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Pastel do Cardoso", 14.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Lanche"),
        ("2026-09-21", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 137.25, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-21", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Habib's", 116.60, "Cartão Nubank PF", "Normal PF", "Liquidado", "Refeição"),
        ("2026-09-22", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Compras Online", "Amazon Br *Amazon", 89.70, "Cartão Nubank PF", "Normal PF", "Liquidado", "Compra Amazon"),
        ("2026-09-22", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Rodrigues Rodrigues Su", 64.11, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-22", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Pets / Agropecuária", "Agro Sta Edwiges", 34.80, "Cartão Nubank PF", "Normal PF", "Liquidado", "Rações / Animais"),
        ("2026-09-22", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Pastelzinho", 28.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Lanche"),
        ("2026-09-22", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Streaming / Assinaturas", "Amazonprimebr", 19.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Prime mensal"),
        ("2026-09-23", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Vestuário / Calçados", "Dafiti *4607571793", 203.62, "Cartão Nubank PF", "Normal PF", "Liquidado", "Vestuário"),
        ("2026-09-23", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Auto Posto Mariano", 150.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-23", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Compras Online", "Amazonmktplc *Fkcomerci", 44.91, "Cartão Nubank PF", "Normal PF", "Liquidado", "Compra Amazon"),
        ("2026-09-24", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Educação (Benjamim)", "Lazer / Infantil", "Point da Molekada", 104.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Brinquedos / Infantil"),
        ("2026-09-24", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 104.86, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-24", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Posto Classe A", 100.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-24", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Pg *Cantina do Bila", 93.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Refeição"),
        ("2026-09-24", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Copa Cafe Bistro", 42.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Café / Bistro"),
        ("2026-09-24", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Pets / Agropecuária", "Petagro", 28.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Petshop"),
        ("2026-09-24", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 20.53, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-25", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Prado", 68.48, "Cartão Nubank PF", "Normal PF", "Liquidado", "Padaria"),
        ("2026-09-25", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 20.13, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-26", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "El Ternazo Buritis", 212.29, "Cartão Nubank PF", "Normal PF", "Liquidado", "Churrascaria / Restaurante"),
        ("2026-09-26", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Saúde & Bem-Estar", "Odontologia", "Multi Dental", 63.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Odontologia"),
        ("2026-09-26", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Streaming / Assinaturas", "Amazon Prime Canais", 44.90, "Cartão Nubank PF", "Normal PF", "Liquidado", "Streaming canais"),
        ("2026-09-26", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Pastelzinho", 31.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Lanches"),
        ("2026-09-27", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 63.34, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-28", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 161.97, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-28", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Compras & Lazer", "Compras Online", "Amazonmktplc *Fastgosho", 69.87, "Cartão Nubank PF", "Normal PF", "Liquidado", "Compra Amazon"),
        ("2026-09-29", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Transporte & Veículos", "Combustível", "Auto Posto Mariano", 150.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Abastecimento"),
        ("2026-09-29", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Supermercados", "Supermercado Buritis", 178.47, "Cartão Nubank PF", "Normal PF", "Liquidado", "Mercado"),
        ("2026-09-29", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Hortifruti / Granel", "D Terra Emporio Granel", 117.22, "Cartão Nubank PF", "Normal PF", "Liquidado", "Produtos a granel"),
        ("2026-09-29", "09/2026", "Cartão Nubank PF", "PF", "Despesa", "Alimentação", "Padaria / Lanches", "Mp *Rosinairibeir", 25.00, "Cartão Nubank PF", "Normal PF", "Liquidado", "Padaria"),
    ]

    for idx, item in enumerate(transactions, start=1):
        row = idx + 1
        ws_lanc.cell(row=row, column=1, value=idx).alignment = align_center
        ws_lanc.cell(row=row, column=2, value=item[0]).alignment = align_center
        ws_lanc.cell(row=row, column=3, value=item[1]).alignment = align_center
        ws_lanc.cell(row=row, column=4, value=item[2]).alignment = align_left
        
        c_ent = ws_lanc.cell(row=row, column=5, value=item[3])
        c_ent.alignment = align_center
        c_ent.font = font_body_bold
        c_ent.fill = fill_highlight_purple if item[3] == 'PJ' else fill_highlight_blue
        
        c_tipo = ws_lanc.cell(row=row, column=6, value=item[4])
        c_tipo.alignment = align_center
        c_tipo.font = font_body_bold
        c_tipo.fill = fill_highlight_green if item[4] == 'Receita' else PatternFill(fill_type=None)
        
        ws_lanc.cell(row=row, column=7, value=item[5]).alignment = align_left
        ws_lanc.cell(row=row, column=8, value=item[6]).alignment = align_left
        ws_lanc.cell(row=row, column=9, value=item[7]).alignment = align_left
        
        c_val = ws_lanc.cell(row=row, column=10, value=item[8])
        c_val.number_format = CURR_FMT
        c_val.alignment = align_right
        c_val.font = font_body_bold
        
        ws_lanc.cell(row=row, column=11, value=item[9]).alignment = align_left
        
        c_cruz = ws_lanc.cell(row=row, column=12, value=item[10])
        c_cruz.alignment = align_center
        if 'PJ bancou PF' in item[10]:
            c_cruz.fill = fill_highlight_red
            c_cruz.font = font_body_bold
        elif 'PF pagou PJ' in item[10]:
            c_cruz.fill = fill_highlight_blue
            c_cruz.font = font_body_bold
            
        ws_lanc.cell(row=row, column=13, value=item[11]).alignment = align_center
        ws_lanc.cell(row=row, column=14, value=item[12]).alignment = align_left

        for col_i in range(1, 15):
            ws_lanc.cell(row=row, column=col_i).border = box_border

    # =============================================================
    # 3. ABA: CONCILIACAO_PF_PJ
    # =============================================================
    ws_conc = wb.create_sheet(title='Conciliacao_PF_PJ')
    ws_conc.views.sheetView[0].showGridLines = True

    ws_conc['B2'] = "CONCILIAÇÃO FINANCEIRA ENTRE EMPRESA (PJ) E SÓCIO (PF)"
    ws_conc['B2'].font = font_title
    ws_conc['B3'] = "Demonstrativo exato de quem pagou o quê e apuração da remuneração real do sócio"
    ws_conc['B3'].font = font_subtitle

    ws_conc['B5'] = "1. RESUMO DOS REPASSES E GASTOS CRUZADOS (SETEMBRO/2026)"
    ws_conc['B5'].font = font_section

    conc_headers = ["Conceito", "Valor (R$)", "Impacto Contábil / Financeiro"]
    for col_idx, text in enumerate(conc_headers, start=2):
        cell = ws_conc.cell(row=6, column=col_idx, value=text)
        cell.font = font_header
        cell.fill = fill_header_navy
        cell.alignment = align_center
        cell.border = box_border

    conc_summary = [
        ("Despesas Pessoais Pagas Diretamente pela Empresa (Caixa PJ + Nubank PJ)", "=SUMIFS(Lancamentos!J:J, Lancamentos!L:L, \"PJ bancou PF\")", "Pró-Labore / Distribuição Indireta de Lucros"),
        ("Pró-Labore Direto Transferido da PJ para PF (Pix na conta)", 200.00, "Retirada financeira direta do sócio"),
        ("TOTAL BANCADO PELA EMPRESA PARA A VIDA PESSOAL", "=C7+C8", "Remuneração Total Realizada do Sócio"),
        ("Despesas da Empresa Pagas com Recursos do Sócio (Nubank PF)", "=SUMIFS(Lancamentos!J:J, Lancamentos!L:L, \"PF pagou PJ\")", "Aporte do sócio / Reembolso devido pela PJ"),
        ("SALDO LÍQUIDO RETIRADO PELO SÓCIO (PJ -> PF)", "=C9-C10", "Transferência líquida real de riqueza da PJ para PF"),
    ]

    for idx, (conc, form, imp) in enumerate(conc_summary, start=7):
        ws_conc.cell(row=idx, column=2, value=conc).font = font_body_bold if 'TOTAL' in conc or 'SALDO' in conc else font_body
        c_v = ws_conc.cell(row=idx, column=3, value=form)
        c_v.number_format = CURR_FMT
        c_v.alignment = align_right
        c_v.font = font_body_bold
        
        c_i = ws_conc.cell(row=idx, column=4, value=imp)
        c_i.font = font_subtitle
        c_i.alignment = align_left

        if 'TOTAL' in conc or 'SALDO' in conc:
            for col_i in range(2, 5):
                ws_conc.cell(row=idx, column=col_i).fill = fill_highlight_purple

        for col_i in range(2, 5):
            ws_conc.cell(row=idx, column=col_i).border = box_border

    ws_conc['B14'] = "2. DETALHAMENTO: CONTAS PESSOAIS (PF) QUE SAÍRAM DA EMPRESA (PJ)"
    ws_conc['B14'].font = font_section

    headers_det_pj = ["Data", "Conta Saída", "Categoria", "Descrição", "Valor (R$)", "Motivo / Destino"]
    for col_idx, text in enumerate(headers_det_pj, start=2):
        cell = ws_conc.cell(row=15, column=col_idx, value=text)
        cell.font = font_header
        cell.fill = fill_header_blue
        cell.alignment = align_center
        cell.border = box_border

    items_pj_bancou_pf = [
        ("01/09/2026", "Conta Caixa PJ", "Transporte & Veículo", "Banco RCI Brasil (Parcela Financiamento Carro)", 2080.09, "Veículo pessoal"),
        ("28/09/2026", "Conta Caixa PJ", "Transporte & Veículo", "Banco RCI Brasil (Parcela Financiamento Carro 2)", 2080.09, "Veículo pessoal (regularização/adiantamento)"),
        ("04/09/2026", "Conta Caixa PJ", "Moradia", "Costa Azul Salvador / Ocean Breeze", 1662.67, "Condomínio/Parcela imóvel Salvador"),
        ("18/09/2026", "Conta Nubank PJ", "Moradia", "Joelma Pereira de Aquino Souza", 800.00, "Aluguel residencial"),
        ("30/09/2026", "Conta Caixa PJ", "Moradia", "CEMIG Distribuição MG (Conta 1)", 382.80, "Energia elétrica Pouso Alegre"),
        ("30/09/2026", "Conta Caixa PJ", "Moradia", "CEMIG Distribuição MG (Conta 2)", 174.21, "Energia elétrica"),
        ("18/09/2026", "Conta Nubank PJ", "Saúde & Exercício", "Escola Respect 4 Jiu-Jitsu", 500.00, "Atividade física"),
        ("30/09/2026", "Conta Caixa PJ", "Saúde & Exercício", "Escola de Lutas BL", 169.90, "Atividade física"),
        ("03/09/2026", "Conta Caixa PJ", "Transporte", "Mega Posto (Débito)", 100.00, "Combustível"),
        ("03/09/2026", "Conta Caixa PJ", "Transporte", "Posto Conceição (Débito)", 100.00, "Combustível"),
        ("03/09/2026", "Conta Caixa PJ", "Transporte", "Concessionária Bahia Norte", 7.70, "Pedágio"),
        ("26/09/2026", "Conta Caixa PJ", "Alimentação", "Supermercado Buritis", 73.31, "Mercado da família"),
        ("26/09/2026", "Conta Caixa PJ", "Alimentação", "Nayara Pereira do", 39.00, "Serviço/Alimentação pessoal"),
        ("26/09/2026", "Conta Caixa PJ", "Alimentação", "Nayara Pereira do", 18.00, "Serviço/Alimentação pessoal"),
    ]

    for idx, (dt, cnt, cat, desc, val, mot) in enumerate(items_pj_bancou_pf, start=16):
        ws_conc.cell(row=idx, column=2, value=dt).alignment = align_center
        ws_conc.cell(row=idx, column=3, value=cnt).alignment = align_left
        ws_conc.cell(row=idx, column=4, value=cat).alignment = align_left
        ws_conc.cell(row=idx, column=5, value=desc).alignment = align_left
        c_v = ws_conc.cell(row=idx, column=6, value=val)
        c_v.number_format = CURR_FMT
        c_v.alignment = align_right
        ws_conc.cell(row=idx, column=7, value=mot).alignment = align_left

        for col_i in range(2, 8):
            ws_conc.cell(row=idx, column=col_i).border = box_border

    tot_row_pj = 16 + len(items_pj_bancou_pf)
    ws_conc.cell(row=tot_row_pj, column=2, value="SUBTOTAL CONTAS PF PAGAS PELA PJ").font = font_body_bold
    ws_conc.merge_cells(f"B{tot_row_pj}:E{tot_row_pj}")
    c_tot_pj = ws_conc.cell(row=tot_row_pj, column=6, value=f"=SUM(F16:F{tot_row_pj-1})")
    c_tot_pj.font = font_body_bold
    c_tot_pj.number_format = CURR_FMT
    c_tot_pj.alignment = align_right
    for col_i in range(2, 8):
        ws_conc.cell(row=tot_row_pj, column=col_i).fill = fill_highlight_red
        ws_conc.cell(row=tot_row_pj, column=col_i).border = box_border

    # =============================================================
    # 4. ABA: PREVISAO_FUTURA_PARCELAS
    # =============================================================
    ws_prev = wb.create_sheet(title='Previsao_Futura')
    ws_prev.views.sheetView[0].showGridLines = True

    ws_prev['B2'] = "CRONOGRAMA DE PARCELAMENTOS & ALÍVIO FINANCEIRO FUTURO"
    ws_prev['B2'].font = font_title
    ws_prev['B3'] = "Mapeamento das parcelas em aberto e projeção da redução das faturas até o fim do ano"
    ws_prev['B3'].font = font_subtitle

    ws_prev['B5'] = "1. PARCELAS MAPEADAS NOS CARTÕES DE CRÉDITO"
    ws_prev['B5'].font = font_section

    prev_headers = ["Origem / Cartão", "Entidade", "Descrição da Compra", "Parcela Set/26", "Valor Parcela", "Status Setembro", "Outubro/26", "Novembro/26", "Dezembro/26", "Impacto no Fluxo de Caixa"]
    for col_idx, text in enumerate(prev_headers, start=2):
        cell = ws_prev.cell(row=6, column=col_idx, value=text)
        cell.font = font_header
        cell.fill = fill_header_navy
        cell.alignment = align_center
        cell.border = box_border

    parcels = [
        ("Cartão Nubank PF", "PF", "Grupo Casas Bahia", "10/10", 678.77, "ENCERRADA!", 0.00, 0.00, 0.00, "Economia imediata de R$ 678,77/mês"),
        ("Cartão Nubank PF", "PF", "Vai de Promo (Viagem)", "3/3", 633.97, "ENCERRADA!", 0.00, 0.00, 0.00, "Economia imediata de R$ 633,97/mês"),
        ("Cartão Nubank PF", "PF", "Sigga Moda Infantil", "4/4", 113.15, "ENCERRADA!", 0.00, 0.00, 0.00, "Economia imediata de R$ 113,15/mês"),
        ("Cartão Nubank PF", "PF", "Latam Linhas Aéreas", "3/4", 426.53, "Ativa", 426.53, 0.00, 0.00, "Encerra em Outubro! Zero em Novembro"),
        ("Cartão Nubank PF", "PF", "Respect 4 Jiu-Jitsu", "2/3", 165.00, "Ativa", 165.00, 0.00, 0.00, "Encerra em Outubro! Zero em Novembro"),
        ("Cartão Nubank PF", "PF", "Pg *Pza Comercio", "3/6", 111.63, "Ativa", 111.63, 111.63, 111.63, "Segue até Dezembro"),
        ("Cartão Nubank PJ", "PJ", "Gol Linhas Aéreas", "2/2", 462.95, "ENCERRADA!", 0.00, 0.00, 0.00, "Economia imediata de R$ 462,95/mês na PJ"),
        ("Cartão Nubank PJ", "PJ", "Gol Linhas Aéreas", "2/3", 246.57, "Ativa", 246.57, 0.00, 0.00, "Encerra em Outubro! Zero em Novembro"),
        ("Cartão Nubank PJ", "PJ", "Azul Seguros", "9/10", 238.77, "Ativa", 238.77, 0.00, 0.00, "Encerra em Outubro! Zero em Novembro"),
    ]

    for idx, (cart, ent, desc, parc, val, st, out_v, nov_v, dez_v, imp) in enumerate(parcels, start=7):
        ws_prev.cell(row=idx, column=2, value=cart).alignment = align_left
        ws_prev.cell(row=idx, column=3, value=ent).alignment = align_center
        ws_prev.cell(row=idx, column=4, value=desc).alignment = align_left
        ws_prev.cell(row=idx, column=5, value=parc).alignment = align_center
        
        c_v = ws_prev.cell(row=idx, column=6, value=val)
        c_v.number_format = CURR_FMT
        c_v.alignment = align_right
        
        c_st = ws_prev.cell(row=idx, column=7, value=st)
        c_st.alignment = align_center
        c_st.font = font_body_bold
        if st == 'ENCERRADA!':
            c_st.fill = fill_highlight_green
            
        c_out = ws_prev.cell(row=idx, column=8, value=out_v)
        c_out.number_format = CURR_FMT
        c_out.alignment = align_right
        
        c_nov = ws_prev.cell(row=idx, column=9, value=nov_v)
        c_nov.number_format = CURR_FMT
        c_nov.alignment = align_right
        
        c_dez = ws_prev.cell(row=idx, column=10, value=dez_v)
        c_dez.number_format = CURR_FMT
        c_dez.alignment = align_right
        
        ws_prev.cell(row=idx, column=11, value=imp).font = font_subtitle

        for col_i in range(2, 12):
            ws_prev.cell(row=idx, column=col_i).border = box_border

    tot_row_parc = 7 + len(parcels)
    ws_prev.cell(row=tot_row_parc, column=2, value="TOTAL DAS PARCELAS NO MÊS").font = font_body_bold
    ws_prev.merge_cells(f"B{tot_row_parc}:E{tot_row_parc}")
    
    for c_i, col_letter in [(6, 'F'), (8, 'H'), (9, 'I'), (10, 'J')]:
        c_t = ws_prev.cell(row=tot_row_parc, column=c_i, value=f"=SUM({col_letter}7:{col_letter}{tot_row_parc-1})")
        c_t.font = font_body_bold
        c_t.number_format = CURR_FMT
        c_t.alignment = align_right
        
    for col_i in range(2, 12):
        ws_prev.cell(row=tot_row_parc, column=col_i).fill = fill_highlight_purple
        ws_prev.cell(row=tot_row_parc, column=col_i).border = bottom_double_border

    alivio_row = tot_row_parc + 2
    ws_prev.cell(row=alivio_row, column=2, value="ALÍVIO FINANCEIRO MENSAL CONQUISTADO (REDUÇÃO EM RELAÇÃO A SETEMBRO):").font = font_section
    ws_prev.merge_cells(f"B{alivio_row}:G{alivio_row}")
    
    c_aliv_out = ws_prev.cell(row=alivio_row, column=8, value=f"=F{tot_row_parc}-H{tot_row_parc}")
    c_aliv_out.font = Font(name='Segoe UI', size=11, bold=True, color=GREEN_ACCENT)
    c_aliv_out.number_format = CURR_FMT
    c_aliv_out.fill = fill_highlight_green
    c_aliv_out.alignment = align_right
    c_aliv_out.border = box_border
    
    c_aliv_nov = ws_prev.cell(row=alivio_row, column=9, value=f"=F{tot_row_parc}-I{tot_row_parc}")
    c_aliv_nov.font = Font(name='Segoe UI', size=11, bold=True, color=GREEN_ACCENT)
    c_aliv_nov.number_format = CURR_FMT
    c_aliv_nov.fill = fill_highlight_green
    c_aliv_nov.alignment = align_right
    c_aliv_nov.border = box_border
    
    c_aliv_dez = ws_prev.cell(row=alivio_row, column=10, value=f"=F{tot_row_parc}-J{tot_row_parc}")
    c_aliv_dez.font = Font(name='Segoe UI', size=11, bold=True, color=GREEN_ACCENT)
    c_aliv_dez.number_format = CURR_FMT
    c_aliv_dez.fill = fill_highlight_green
    c_aliv_dez.alignment = align_right
    c_aliv_dez.border = box_border

    # =============================================================
    # 5. ABA: PLANO_DE_CONTAS
    # =============================================================
    ws_plan = wb.create_sheet(title='Plano_de_Contas')
    ws_plan.views.sheetView[0].showGridLines = True

    ws_plan['B2'] = "ESTRUTURA DE CATEGORIAS & PLANO DE CONTAS PADRONIZADO"
    ws_plan['B2'].font = font_title
    ws_plan['B3'] = "Estrutura para categorizar extratos e faturas dos próximos meses com consistência"
    ws_plan['B3'].font = font_subtitle

    plan_headers = ["Entidade", "Tipo", "Categoria Principal", "Subcategoria", "Descrição / Exemplos de Aplicação", "Conta Recomendada"]
    for col_idx, text in enumerate(plan_headers, start=2):
        cell = ws_plan.cell(row=5, column=col_idx, value=text)
        cell.font = font_header
        cell.fill = fill_header_navy
        cell.alignment = align_center
        cell.border = box_border

    cats = [
        ("PJ", "Receita", "Receita Operacional", "Projetos Nacionais", "Honorários de projetos e laudos emitidos (Grado, Gráfico, etc.)", "Conta Caixa PJ / Nubank PJ"),
        ("PJ", "Receita", "Receita Internacional", "Projetos Internacionais", "Contrato internacional recorrente TDP Braga (Portugal)", "Wise -> Nubank/Caixa"),
        ("PJ", "Despesa", "Custos Escritório", "Equipe & Estágio", "Bolsa de estágio estagiários técnicos (Fernanda)", "Conta Caixa PJ"),
        ("PJ", "Despesa", "Custos Escritório", "Infraestrutura / Coworking", "Aluguel de sala, estação de trabalho (DW Treinamento)", "Conta Nubank PJ"),
        ("PJ", "Despesa", "Custos Escritório", "Conectividade / Internet", "Link de internet do escritório (BRT / CVS)", "Conta Nubank PJ"),
        ("PJ", "Despesa", "Custos Escritório", "Softwares & TI", "Google Workspace, licenças de cálculo/desenho (TQS/Eberick)", "Cartão Nubank PJ"),
        ("PJ", "Despesa", "Custos Escritório", "Tributos & Taxas", "Simples Nacional, ISS, INSS/DCTFWeb, CREA PJ, ABECE", "Conta Caixa PJ / Nubank PJ"),
        ("PJ", "Despesa", "Custos Escritório", "Capacitação & Cursos", "Especializações, cursos e pós-graduação (IPOG)", "Conta Caixa PJ"),
        ("PJ", "Despesa", "Custos Escritório", "Tarifas Bancárias", "Manutenção de conta, tarifas de Pix PJ e emissão de boletos", "Conta Caixa PJ"),
        ("PJ", "Despesa", "Custos Escritório", "Viagens & Deslocamento", "Passagens de avião para visitas técnicas e reuniões (Gol/Azul)", "Cartão Nubank PJ"),
        ("PF", "Despesa", "Moradia", "Imóvel Salvador", "Parcela / condomínio empreendimento Ocean Breeze Salvador", "Conta Nubank PF"),
        ("PF", "Despesa", "Moradia", "Aluguel Residencial", "Aluguel da moradia mensal (Joelma Pereira)", "Conta Nubank PF"),
        ("PF", "Despesa", "Moradia", "Energia Elétrica", "Contas de luz (CEMIG Minas Gerais / Coelba Bahia)", "Conta Nubank PF"),
        ("PF", "Despesa", "Moradia", "Conectividade / Telefone", "Contas de celular pessoal e internet residencial (TIM)", "Conta Nubank PF"),
        ("PF", "Despesa", "Educação (Benjamim)", "Escola", "Mensalidade escolar (Associação das Obras Sociais)", "Conta Nubank PF"),
        ("PF", "Despesa", "Educação (Benjamim)", "Cursos", "Curso de línguas (Spectrum Line Language Center)", "Conta Nubank PF"),
        ("PF", "Despesa", "Educação (Benjamim)", "Material Escolar", "Livros, apostilas e itens escolares (Lápis de Cor)", "Cartão Nubank PF"),
        ("PF", "Despesa", "Educação (Benjamim)", "Vestuário Infantil", "Roupas e calçados infantis (Sigga Moda Infantil)", "Cartão Nubank PF"),
        ("PF", "Despesa", "Saúde & Bem-Estar", "Plano de Saúde", "Plano de saúde familiar (Unimed Pouso Alegre)", "Conta Nubank PF"),
        ("PF", "Despesa", "Saúde & Bem-Estar", "Previdência Privada", "Fundo de pensão e previdência privada (BB Previdência)", "Conta Nubank PF"),
        ("PF", "Despesa", "Saúde & Bem-Estar", "Farmácia", "Medicamentos e suplementação (Drogaria N. Senhora / Pague Menos)", "Cartão Nubank PF / Caixa PF"),
        ("PF", "Despesa", "Saúde & Bem-Estar", "Atividades Físicas", "Jiu-jitsu, artes marciais e academia (Respect 4 / BL)", "Cartão Nubank PF"),
        ("PF", "Despesa", "Transporte & Veículos", "Parcela Carro", "Financiamento do veículo mensal (Banco RCI Brasil)", "Conta Nubank PF"),
        ("PF", "Despesa", "Transporte & Veículos", "Combustível", "Abastecimentos semanais (Auto Posto Mariano, Pedra Forte)", "Cartão Nubank PF"),
        ("PF", "Despesa", "Transporte & Veículos", "Mobilidade Urbana", "Corridas de aplicativo (Uber)", "Cartão Nubank PF"),
        ("PF", "Despesa", "Alimentação", "Supermercados", "Compras volumosas de supermercado e atacado (Mart Minas, Buritis)", "Cartão Nubank PF"),
        ("PF", "Despesa", "Alimentação", "Hortifruti / Feira", "Frutas, verduras e itens frescos de feira livre", "Cartão Nubank PF / Pix PF"),
        ("PF", "Despesa", "Alimentação", "Restaurantes & Lanches", "Almoços fora, jantares, lanches e fins de semana", "Cartão Nubank PF / Caixa PF"),
        ("PF", "Despesa", "Compras & Lazer", "Compras Online", "Compras diversas (Amazon, Mercado Livre, Dafiti)", "Cartão Nubank PF"),
        ("PF", "Despesa", "Compras & Lazer", "Streaming / Assinaturas", "Netflix, Spotify, Amazon Prime, Paramount", "Cartão Nubank PF"),
        ("PF", "Despesa", "Compras & Lazer", "Pets / Agropecuária", "Alimentação e cuidados cachorro/animais (Petagro, Sta Edwiges)", "Cartão Nubank PF"),
    ]

    for idx, (ent, tip, cat, sub, desc, cnt) in enumerate(cats, start=6):
        c_e = ws_plan.cell(row=idx, column=2, value=ent)
        c_e.alignment = align_center
        c_e.font = font_body_bold
        c_e.fill = fill_highlight_purple if ent == 'PJ' else fill_highlight_blue
        
        ws_plan.cell(row=idx, column=3, value=tip).alignment = align_center
        ws_plan.cell(row=idx, column=4, value=cat).font = font_body_bold
        ws_plan.cell(row=idx, column=5, value=sub)
        ws_plan.cell(row=idx, column=6, value=desc).font = font_subtitle
        ws_plan.cell(row=idx, column=7, value=cnt).alignment = align_left

        for col_i in range(2, 8):
            ws_plan.cell(row=idx, column=col_i).border = box_border

    # =============================================================
    # AJUSTE AUTOMÁTICO DE LARGURA DE COLUNAS EM TODAS AS ABAS
    # =============================================================
    for ws in wb.worksheets:
        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                # ignore merged cells with very long content
                if cell.row in [2, 3] and ws.title in ['Dashboard', 'Conciliacao_PF_PJ', 'Previsao_Futura', 'Plano_de_Contas']:
                    continue
                val_str = str(cell.value or '')
                if len(val_str) > max_len and len(val_str) < 60:
                    max_len = len(val_str)
            ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

    # Ajustes finos específicos de largura
    ws_dash.column_dimensions['A'].width = 3
    ws_dash.column_dimensions['B'].width = 38
    ws_dash.column_dimensions['C'].width = 22
    ws_dash.column_dimensions['D'].width = 22
    ws_dash.column_dimensions['E'].width = 22
    ws_dash.column_dimensions['F'].width = 35
    ws_dash.column_dimensions['G'].width = 40

    ws_lanc.column_dimensions['A'].width = 6
    ws_lanc.column_dimensions['B'].width = 13
    ws_lanc.column_dimensions['C'].width = 13
    ws_lanc.column_dimensions['D'].width = 20
    ws_lanc.column_dimensions['E'].width = 10
    ws_lanc.column_dimensions['F'].width = 12
    ws_lanc.column_dimensions['G'].width = 25
    ws_lanc.column_dimensions['H'].width = 25
    ws_lanc.column_dimensions['I'].width = 45
    ws_lanc.column_dimensions['J'].width = 16
    ws_lanc.column_dimensions['K'].width = 18
    ws_lanc.column_dimensions['L'].width = 18
    ws_lanc.column_dimensions['M'].width = 12
    ws_lanc.column_dimensions['N'].width = 45

    output_path = r'CONTROLE_FINANCEIRO_MESTRE_2026.xlsx'
    wb.save(output_path)
    print(f"Planilha Master criada com sucesso em: {output_path}")

if __name__ == '__main__':
    create_master_workbook()
