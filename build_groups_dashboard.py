import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_advanced_excel():
    wb = openpyxl.load_workbook('CONTROLE_FINANCEIRO_MESTRE_2026.xlsx')
    
    # 1. Ajuste em Lancamentos: AutoFilter e FreezePanes
    ws_lanc = wb['Lancamentos']
    ws_lanc.auto_filter.ref = f"A1:N{ws_lanc.max_row}"
    ws_lanc.freeze_panes = 'A2'

    # 2. Criar ou recriar aba Dashboard_Grupos
    if 'Dashboard_Grupos' in wb.sheetnames:
        del wb['Dashboard_Grupos']
    
    # Inserir como 2ª aba
    ws_grp = wb.create_sheet(title='Dashboard_Grupos', index=1)
    ws_grp.views.sheetView[0].showGridLines = True

    # Estilos
    NAVY_DARK = '0F172A'
    NAVY_BLUE = '1E293B'
    BLUE_ACCENT = '0284C7'
    BLUE_LIGHT = 'E0F2FE'
    GREEN_ACCENT = '059669'
    GREEN_LIGHT = 'D1FAE5'
    RED_ACCENT = 'E11D48'
    RED_LIGHT = 'FFE4E6'
    PURPLE_ACCENT = '7C3AED'
    PURPLE_LIGHT = 'EDE9FE'
    AMBER_ACCENT = 'D97706'
    AMBER_LIGHT = 'FEF3C7'
    GRAY_BORDER = 'CBD5E1'

    font_title = Font(name='Segoe UI', size=15, bold=True, color='0F172A')
    font_subtitle = Font(name='Segoe UI', size=10, italic=True, color='64748B')
    font_sec_pf = Font(name='Segoe UI', size=11, bold=True, color=BLUE_ACCENT)
    font_sec_pj = Font(name='Segoe UI', size=11, bold=True, color=PURPLE_ACCENT)
    font_tbl_header = Font(name='Segoe UI', size=9, bold=True, color='FFFFFF')
    font_row_bold = Font(name='Segoe UI', size=9, bold=True, color='0F172A')
    font_row = Font(name='Segoe UI', size=9, color='1E293B')
    font_small = Font(name='Segoe UI', size=8, italic=True, color='64748B')

    fill_pf_header = PatternFill(start_color=BLUE_ACCENT, end_color=BLUE_ACCENT, fill_type='solid')
    fill_pj_header = PatternFill(start_color=PURPLE_ACCENT, end_color=PURPLE_ACCENT, fill_type='solid')
    fill_sub_header = PatternFill(start_color='334155', end_color='334155', fill_type='solid')
    fill_total_pf = PatternFill(start_color=BLUE_LIGHT, end_color=BLUE_LIGHT, fill_type='solid')
    fill_total_pj = PatternFill(start_color=PURPLE_LIGHT, end_color=PURPLE_LIGHT, fill_type='solid')
    fill_group_title_pf = PatternFill(start_color='F0F9FF', end_color='F0F9FF', fill_type='solid')
    fill_group_title_pj = PatternFill(start_color='FAF5FF', end_color='FAF5FF', fill_type='solid')

    border_thin = Side(border_style='thin', color=GRAY_BORDER)
    border_double = Side(border_style='double', color='0F172A')
    box_border = Border(left=border_thin, right=border_thin, top=border_thin, bottom=border_thin)
    total_border = Border(top=border_thin, bottom=border_double, left=border_thin, right=border_thin)

    align_center = Alignment(horizontal='center', vertical='center')
    align_left = Alignment(horizontal='left', vertical='center')
    align_right = Alignment(horizontal='right', vertical='center')

    CURR_FMT = 'R$ #,##0.00'
    PCT_FMT = '0.0%'

    # Cabeçalho da Aba
    ws_grp['B2'] = "DASHBOARD ANALÍTICO POR GRUPOS & SUBGRUPOS (SETEMBRO/2026)"
    ws_grp['B2'].font = font_title
    ws_grp['B3'] = "Visão estruturada por tópicos para gestão de gastos da Pessoa Física e Pessoa Jurídica"
    ws_grp['B3'].font = font_subtitle

    # =========================================================================
    # TABELA 1: PESSOAL (PF)
    # =========================================================================
    ws_grp['B5'] = "👤 GRUPO PESSOAL (PESSOA FÍSICA - PF)"
    ws_grp['B5'].font = font_sec_pf

    headers_pf = ["Tópico / Grupo", "Subgrupo / Detalhamento", "Realizado Set/26", "% Total PF", "Meta Proposta", "Diferença", "Diagnóstico & Estratégia de Redução"]
    for c_idx, h_text in enumerate(headers_pf, start=2):
        cell = ws_grp.cell(row=6, column=c_idx, value=h_text)
        cell.font = font_tbl_header
        cell.fill = fill_pf_header
        cell.alignment = align_center
        cell.border = box_border

    # Linhas de grupos e subgrupos PF
    # Formato: (Grupo, Subgrupo, Formula_Real, Formula_Meta, Diagnostico)
    pf_rows = [
        # 1. Alimentação
        ("1. ALIMENTAÇÃO", "Supermercados (Mart Minas + Buritis)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Supermercados\")", 2200.00, "Compra grande planejada + compras de reposição"),
        ("1. ALIMENTAÇÃO", "Restaurantes, Saídas & Fins de Semana", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Restaurantes & Lanches\")", 900.00, "Cota de R$ 225 por fim de semana para sair com família"),
        ("1. ALIMENTAÇÃO", "Feira Livre, Padarias, Pastelzinho & Granel", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Feira / Padaria\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Padaria / Lanches\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Hortifruti / Feira\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Hortifruti / Granel\")", 400.00, "1 feira semanal para frescos (~R$ 100/semana)"),
        ("1. ALIMENTAÇÃO", "Subtotal Alimentação", "=SUM(D7:D9)", 3500.00, "Economia potencial de mais de R$ 2.200/mês"),

        # 2. Carro & Transporte
        ("2. CARRO & TRANSPORTE", "Parcela Financiamento Carro (Banco RCI)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Parcela Carro\")", 2080.09, "Parcela fixa regular (Setembro teve 2 parcelas pagas)"),
        ("2. CARRO & TRANSPORTE", "Combustível nos Postos (Mariano, Pedra Forte)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Combustível\")", 900.00, "Otimizar deslocamentos e lançar viagens PJ no CNPJ"),
        ("2. CARRO & TRANSPORTE", "Passagens, Uber & Pedágios", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Passagens Aéreas\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Passagens Terrestres\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Mobilidade Urbana\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Pedágio\")", 0.00, "Latam (3/4) encerra em Outubro! Zero em Novembro"),
        ("2. CARRO & TRANSPORTE", "Subtotal Carro & Transporte", "=SUM(D11:D13)", 2980.09, "Queda de R$ 4.160 para R$ 2.080 na parcela do carro"),

        # 3. Moradia
        ("3. MORADIA & HABITAÇÃO", "Imóvel Salvador (Ocean Breeze / Costa Azul)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Imóvel Salvador\")", 1662.67, "Fase 2: Alugar/monetizar para zerar este custo"),
        ("3. MORADIA & HABITAÇÃO", "Aluguel Residencial Pouso Alegre (Joelma)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Aluguel Residencial\")", 800.00, "Aluguel residencial fixo mensal"),
        ("3. MORADIA & HABITAÇÃO", "Energia Elétrica (CEMIG Minas Gerais)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Energia Elétrica\")", 550.00, "Contas de luz da residência"),
        ("3. MORADIA & HABITAÇÃO", "Telefonia Celular (TIM)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Conectividade / Telefone\")", 125.00, "Planos de celular pessoal"),
        ("3. MORADIA & HABITAÇÃO", "Subtotal Moradia", "=SUM(D15:D18)", 3137.67, "Na Fase 2, alugando Salvador, desce para R$ 1.475"),

        # 4. Filho / Educação
        ("4. EDUCAÇÃO (BENJAMIM)", "Escola Benjamim (Associação das Obras)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Escola\")", 1870.00, "Mensalidade escolar regular"),
        ("4. EDUCAÇÃO (BENJAMIM)", "Curso de Inglês (Spectrum Line)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Cursos\")", 240.00, "Inglês curricular"),
        ("4. EDUCAÇÃO (BENJAMIM)", "Vestuário Infantil, Brinquedos & Material", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Vestuário Infantil\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Lazer / Infantil\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Material Escolar\")", 100.00, "Sigga Moda Infantil quitada em Setembro (4/4)!"),
        ("4. EDUCAÇÃO (BENJAMIM)", "Subtotal Educação (Benjamim)", "=SUM(D20:D22)", 2210.00, "Investimento prioritário preservado"),

        # 5. Saúde & Previdência
        ("5. SAÚDE & BEM-ESTAR", "Plano de Saúde Familiar (Unimed)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Plano de Saúde\")", 1546.83, "Proteção familiar essencial (3 boletos Unimed)"),
        ("5. SAÚDE & BEM-ESTAR", "Atividades Físicas & Lutas (Respect / BL)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Atividades Físicas\")", 500.00, "Jiu-jitsu parcela 2/3 termina em Outubro"),
        ("5. SAÚDE & BEM-ESTAR", "Farmácias & Odontologia (Medicamentos)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Farmácia\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Odontologia\")", 300.00, "Farmácia de rotina e prevenção"),
        ("5. SAÚDE & BEM-ESTAR", "Previdência Privada (BB Previdência)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Previdência Privada\")", 226.00, "Aporte para aposentadoria privada"),
        ("5. SAÚDE & BEM-ESTAR", "Subtotal Saúde & Bem-Estar", "=SUM(D24:D27)", 2572.83, "Saúde estruturada"),

        # 6. Compras, Lazer & Parcelas
        ("6. COMPRAS & PARCELAS", "Parcelamentos Antigos (Casas Bahia + Promo)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Parcelamentos Antigos\")", 111.63, "QUITADOS! Casas Bahia (10/10) e Promo (3/3) zeram"),
        ("6. COMPRAS & PARCELAS", "Streaming & Assinaturas (Netflix, Spotify...)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Streaming / Assinaturas\")", 100.00, "Cancelar canais extras do Amazon Prime"),
        ("6. COMPRAS & PARCELAS", "Pets & Agropecuária (Rações / Cuidados)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Pets / Agropecuária\")", 250.00, "Cachorro e galinhas"),
        ("6. COMPRAS & PARCELAS", "Compras Online, Vestuário & Utilidades", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Compras Online\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Vestuário / Calçados\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Casa & Utilidades\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Diversos\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Vestuário / Casa\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Tarifas Cartão\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PF\", Lancamentos!H:H, \"Farmácia / Cosméticos\")", 300.00, "Compras pontuais à vista"),
        ("6. COMPRAS & PARCELAS", "Subtotal Compras & Parcelas", "=SUM(D29:D32)", 761.63, "Alívio conquistado de R$ 1.425/mês"),
    ]

    r_curr = 7
    subtotals_pf_rows = []
    for grp, sub, form_real, meta_val, diag in pf_rows:
        is_sub = "Subtotal" in sub
        ws_grp.cell(row=r_curr, column=2, value=grp).font = font_row_bold if is_sub else font_row
        ws_grp.cell(row=r_curr, column=3, value=sub).font = font_row_bold if is_sub else font_row
        
        c_r = ws_grp.cell(row=r_curr, column=4, value=form_real)
        c_r.number_format = CURR_FMT
        c_r.alignment = align_right
        c_r.font = font_row_bold if is_sub else font_row
        
        # % sobre total PF
        c_pct = ws_grp.cell(row=r_curr, column=5, value=f"=D{r_curr}/$D$35")
        c_pct.number_format = PCT_FMT
        c_pct.alignment = align_right
        c_pct.font = font_row_bold if is_sub else font_row

        c_m = ws_grp.cell(row=r_curr, column=6, value=meta_val)
        c_m.number_format = CURR_FMT
        c_m.alignment = align_right
        c_m.font = font_row_bold if is_sub else font_row

        c_dif = ws_grp.cell(row=r_curr, column=7, value=f"=F{r_curr}-D{r_curr}")
        c_dif.number_format = CURR_FMT
        c_dif.alignment = align_right
        c_dif.font = font_row_bold if is_sub else font_row

        c_diag = ws_grp.cell(row=r_curr, column=8, value=diag)
        c_diag.font = font_small

        if is_sub:
            subtotals_pf_rows.append(r_curr)
            for c_i in range(2, 9):
                ws_grp.cell(row=r_curr, column=c_i).fill = fill_group_title_pf
                ws_grp.cell(row=r_curr, column=c_i).border = box_border
        else:
            for c_i in range(2, 9):
                ws_grp.cell(row=r_curr, column=c_i).border = box_border
        r_curr += 1

    # Linha Total PF
    row_tot_pf = r_curr
    ws_grp.cell(row=row_tot_pf, column=2, value="TOTAL GERAL PESSOA FÍSICA (PF)").font = Font(name='Segoe UI', size=10, bold=True, color=NAVY_DARK)
    ws_grp.merge_cells(f"B{row_tot_pf}:C{row_tot_pf}")
    c_tot_r = ws_grp.cell(row=row_tot_pf, column=4, value=f"=D10+D14+D19+D23+D28+D33")
    c_tot_r.number_format = CURR_FMT
    c_tot_r.font = font_row_bold
    c_tot_r.alignment = align_right

    c_tot_pct = ws_grp.cell(row=row_tot_pf, column=5, value=1.0)
    c_tot_pct.number_format = PCT_FMT
    c_tot_pct.font = font_row_bold
    c_tot_pct.alignment = align_right

    c_tot_m = ws_grp.cell(row=row_tot_pf, column=6, value=f"=F10+F14+F19+F23+F28+F33")
    c_tot_m.number_format = CURR_FMT
    c_tot_m.font = font_row_bold
    c_tot_m.alignment = align_right

    c_tot_dif = ws_grp.cell(row=row_tot_pf, column=7, value=f"=F{row_tot_pf}-D{row_tot_pf}")
    c_tot_dif.number_format = CURR_FMT
    c_tot_dif.font = font_row_bold
    c_tot_dif.alignment = align_right

    c_tot_diag = ws_grp.cell(row=row_tot_pf, column=8, value="Redução planejada de R$ 23.298 para R$ 15.162 na PF!")
    c_tot_diag.font = font_row_bold

    for c_i in range(2, 9):
        ws_grp.cell(row=row_tot_pf, column=c_i).fill = fill_total_pf
        ws_grp.cell(row=row_tot_pf, column=c_i).border = total_border

    # =========================================================================
    # TABELA 2: EMPRESA / ESCRITÓRIO (PJ)
    # =========================================================================
    r_curr += 3
    ws_grp.cell(row=r_curr, column=2, value="🏢 GRUPO EMPRESA / ESCRITÓRIO (PESSOA JURÍDICA - PJ)").font = font_sec_pj
    r_curr += 1

    for c_idx, h_text in enumerate(headers_pf, start=2):
        cell = ws_grp.cell(row=r_curr, column=c_idx, value=h_text)
        cell.font = font_tbl_header
        cell.fill = fill_pj_header
        cell.alignment = align_center
        cell.border = box_border
    r_curr += 1

    r_pj_start = r_curr
    pj_rows = [
        # 1. Equipe
        ("1. EQUIPE & ESTÁGIO", "Estagiária Técnica (Fernanda Mayra)", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Equipe & Estágio\")", 1700.00, "Bolsa de estágio regular mantida"),
        # 2. Infraestrutura
        ("2. INFRAESTRUTURA", "Coworking & Internet Escritório", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Infraestrutura / Coworking\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Conectividade / Internet\")", 650.00, "DW Treinamento R$ 525 + BRT Internet R$ 99"),
        # 3. Viagens a Trabalho
        ("3. VIAGENS A TRABALHO", "Passagens Aéreas GOL & Seguro Frota", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Viagens & Deslocamento\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Operação & Frota\")", 500.00, "Passagens GOL (2/2) encerrada! Parcela 2/3 encerra em Out"),
        # 4. Tributos & Conselhos
        ("4. TRIBUTOS & TAXAS", "INSS / DCTFWeb, CREA PF & ABECE", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Tributos & Taxas\")", 800.00, "Obrigações tributárias e de classe do escritório"),
        # 5. Softwares & Capacitação
        ("5. SOFTWARES & CURSOS", "Google Workspace & Pós-Graduação IPOG", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Softwares & TI\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Capacitação & Cursos\")", 500.00, "Assinatura Google R$ 98 + IPOG R$ 279"),
        # 6. Tarifas & Operações
        ("6. TARIFAS & OPERAÇÕES", "Tarifas Bancárias Caixa & Deslocamentos", "=SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Tarifas Bancárias\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Serviços Operacionais\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Alimentação Operacional\")+SUMIFS(Lancamentos!J:J, Lancamentos!E:E, \"PJ\", Lancamentos!H:H, \"Deslocamento Operacional\")", 350.00, "Operação enxuta do dia a dia"),
    ]

    for grp, sub, form_real, meta_val, diag in pj_rows:
        ws_grp.cell(row=r_curr, column=2, value=grp).font = font_row_bold
        ws_grp.cell(row=r_curr, column=3, value=sub).font = font_row
        
        c_r = ws_grp.cell(row=r_curr, column=4, value=form_real)
        c_r.number_format = CURR_FMT
        c_r.alignment = align_right
        c_r.font = font_row_bold

        c_pct = ws_grp.cell(row=r_curr, column=5, value=f"=D{r_curr}/$D${r_pj_start + len(pj_rows)}")
        c_pct.number_format = PCT_FMT
        c_pct.alignment = align_right
        c_pct.font = font_row

        c_m = ws_grp.cell(row=r_curr, column=6, value=meta_val)
        c_m.number_format = CURR_FMT
        c_m.alignment = align_right
        c_m.font = font_row_bold

        c_dif = ws_grp.cell(row=r_curr, column=7, value=f"=F{r_curr}-D{r_curr}")
        c_dif.number_format = CURR_FMT
        c_dif.alignment = align_right
        c_dif.font = font_row_bold

        c_diag = ws_grp.cell(row=r_curr, column=8, value=diag)
        c_diag.font = font_small

        for c_i in range(2, 9):
            ws_grp.cell(row=r_curr, column=c_i).border = box_border
        r_curr += 1

    row_tot_pj = r_curr
    ws_grp.cell(row=row_tot_pj, column=2, value="TOTAL GERAL EMPRESA (PJ)").font = Font(name='Segoe UI', size=10, bold=True, color=NAVY_DARK)
    ws_grp.merge_cells(f"B{row_tot_pj}:C{row_tot_pj}")
    c_tot_pj_r = ws_grp.cell(row=row_tot_pj, column=4, value=f"=SUM(D{r_pj_start}:D{r_curr-1})")
    c_tot_pj_r.number_format = CURR_FMT
    c_tot_pj_r.font = font_row_bold
    c_tot_pj_r.alignment = align_right

    c_tot_pj_pct = ws_grp.cell(row=row_tot_pj, column=5, value=1.0)
    c_tot_pj_pct.number_format = PCT_FMT
    c_tot_pj_pct.font = font_row_bold
    c_tot_pj_pct.alignment = align_right

    c_tot_pj_m = ws_grp.cell(row=row_tot_pj, column=6, value=f"=SUM(F{r_pj_start}:F{r_curr-1})")
    c_tot_pj_m.number_format = CURR_FMT
    c_tot_pj_m.font = font_row_bold
    c_tot_pj_m.alignment = align_right

    c_tot_pj_dif = ws_grp.cell(row=row_tot_pj, column=7, value=f"=F{row_tot_pj}-D{row_tot_pj}")
    c_tot_pj_dif.number_format = CURR_FMT
    c_tot_pj_dif.font = font_row_bold
    c_tot_pj_dif.alignment = align_right

    c_tot_pj_diag = ws_grp.cell(row=row_tot_pj, column=8, value="Operação da PJ enxuta e dentro da meta saudável!")
    c_tot_pj_diag.font = font_row_bold

    for c_i in range(2, 9):
        ws_grp.cell(row=row_tot_pj, column=c_i).fill = fill_total_pj
        ws_grp.cell(row=row_tot_pj, column=c_i).border = total_border

    # =========================================================================
    # TABELA CONSOLIDADA RESUMO GERAL
    # =========================================================================
    r_curr += 3
    row_consol = r_curr
    ws_grp.cell(row=row_consol, column=2, value="🎯 CONSOLIDADO GERAL (PF + PJ)").font = font_title
    ws_grp.merge_cells(f"B{row_consol}:C{row_consol}")

    c_c_r = ws_grp.cell(row=row_consol, column=4, value=f"=D{row_tot_pf}+D{row_tot_pj}")
    c_c_r.number_format = CURR_FMT
    c_c_r.font = Font(name='Segoe UI', size=12, bold=True, color=RED_ACCENT)
    c_c_r.alignment = align_right

    ws_grp.cell(row=row_consol, column=5, value="Meta Geral:").font = font_row_bold
    c_c_m = ws_grp.cell(row=row_consol, column=6, value=f"=F{row_tot_pf}+F{row_tot_pj}")
    c_c_m.number_format = CURR_FMT
    c_c_m.font = Font(name='Segoe UI', size=12, bold=True, color=GREEN_ACCENT)
    c_c_m.alignment = align_right

    c_c_dif = ws_grp.cell(row=row_consol, column=7, value=f"=F{row_consol}-D{row_consol}")
    c_c_dif.number_format = CURR_FMT
    c_c_dif.font = Font(name='Segoe UI', size=12, bold=True, color=BLUE_ACCENT)
    c_c_dif.alignment = align_right

    ws_grp.cell(row=row_consol, column=8, value="Redução planejada de R$ 8.318/mês sem perda de conforto!").font = font_row_bold

    for c_i in range(2, 9):
        ws_grp.cell(row=row_consol, column=c_i).fill = PatternFill(start_color='FEF9C3', end_color='FEF9C3', fill_type='solid') # Yellow highlight
        ws_grp.cell(row=row_consol, column=c_i).border = total_border

    # Larguras de coluna
    ws_grp.column_dimensions['A'].width = 3
    ws_grp.column_dimensions['B'].width = 28
    ws_grp.column_dimensions['C'].width = 44
    ws_grp.column_dimensions['D'].width = 18
    ws_grp.column_dimensions['E'].width = 14
    ws_grp.column_dimensions['F'].width = 18
    ws_grp.column_dimensions['G'].width = 18
    ws_grp.column_dimensions['H'].width = 55

    # Salvar
    out_path = 'CONTROLE_FINANCEIRO_MESTRE_2026_V2.xlsx'
    wb.save(out_path)
    print(f"Planilha avançada criada com sucesso em: {out_path}")

if __name__ == '__main__':
    build_advanced_excel()
