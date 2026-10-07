@echo off
chcp 65001 >nul
echo =====================================================================
echo    MOURA BARRETTO ENGENHARIA - PUBLICACAO DO DASHBOARD FINANCEIRO
echo =====================================================================
echo.
set "PATH=C:\Program Files\Git\cmd;C:\Program Files\GitHub CLI;C:\Program Files\Git\mingw64\bin;%PATH%"

echo 1. Verificando autenticacao com o GitHub...
"C:\Program Files\GitHub CLI\gh.exe" auth status >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Conectando sua conta do GitHub... Uma janela do navegador sera aberta.
    "C:\Program Files\GitHub CLI\gh.exe" auth login -h github.com -p https --web
    "C:\Program Files\GitHub CLI\gh.exe" auth setup-git
)

echo.
echo 2. Enviando atualizacoes para o seu GitHub Pages...
cd /d "C:\Users\ACER\Desktop\ANTIGRAVITY\07. PLANILHA DE AUXILIO FINANCEIRO\temp_github_repo"
git push origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo =====================================================================
    echo    SUCESSO! O seu Painel Financeiro ja esta online!
    echo.
    echo    Link de acesso:
    echo    https://mateusbarrettoai-max.github.io/financeiro/
    echo =====================================================================
    echo.
    start https://mateusbarrettoai-max.github.io/financeiro/
) else (
    echo.
    echo Ocorreu um erro no envio. Verifique a conexao e tente novamente.
)

pause
