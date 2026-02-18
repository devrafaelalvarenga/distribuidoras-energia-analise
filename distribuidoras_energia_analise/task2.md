poetry install
poetry env info
poetry env activate

Se poetry env activate não “entrar” no shell (isso depende do seu terminal), usar o caminho do venv:

poetry env info --path

source "$(poetry env info --path)/bin/activate"

--configurar python
poetry env use python3.12
poetry install

--dependencias
poetry add pandas requests python-dotenv loguru
poetry add -G dev pytest ruff black

-verificar se o ambiente está funcional, antes de qualquer lógica de negócio.
Teste “smoke” (garante que ambiente está OK)

tests/test_smoke.py:

def test_smoke():
    assert 1 + 1 == 2

--rodar:
poetry run pytest -q

--Função: garantir que o projeto pode ser executado como módulo Python.
--Criar src/distribuidoras_energia_analise/cli.py:

def main():
    print("distribuidoras-energia-analise: ambiente OK")

if __name__ == "__main__":
    main()

--Rodar:
poetry run python -m distribuidoras_energia_analise.cli

--Função: manter padrão, legibilidade e segurança do código desde o primeiro commit.
black → formatação automática (estilo único)
ruff → lint rápido (imports, variáveis não usadas, erros comuns)
--No pyproject.toml, adicionar:

[tool.ruff]
line-length = 100

[tool.black]
line-length = 100

--Rodar:

poetry run ruff check .
poetry run black .


--validar que a estrutura está certa:

poetry run python -c "import distribuidoras_energia_analise; print('OK')"


--Rodar a ingestão

export BRONZE_DATASET="indicadores"
export BRONZE_RESOURCE_URL="https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/4493985c-baea-429c-9df5-3030422c71d7/download/indicadores-continuidade-coletivos-2020-2029.csv"
poetry run python -m distribuidoras_energia_analise.cli
