# Fontes de Dados

## Resumo
| Fonte | Datasets | Atualização | Volume |
|-------|----------|-------------|--------|
| ANEEL | 5 principais | Mensal | ~3K registros/mês |
| ONS | 1 complementar | Diário | Opcional |
| IBGE/BCB | 2 enriquecimento | Mensal/Anual | Pequeno |

## ANEEL - Dados Abertos (Principal)

### Dataset 1: Distribuidoras
[Detalhar conforme template acima]

### Dataset 2: Indicadores DEC/FEC
[Detalhar]

[...continuar para todos]

## Testes Realizados
- [ ] Download manual dos CSVs
- [ ] Leitura com Pandas
- [ ] Validação de colunas esperadas
- [ ] Identificação de problemas (encoding, separador)

## Limitações Conhecidas
- CSV sem versionamento
- Delay de publicação
- Possíveis mudanças de schema
```

### ✅ Checklist - Seção 1.3

- [ ] Acessar portal ANEEL e explorar datasets
- [ ] Baixar 3 CSVs principais manualmente
- [ ] Testar leitura com Python/Pandas
- [ ] Identificar possíveis problemas (encoding, separadores)
- [ ] Salvar amostras em `docs/sample_data/`
- [ ] Criar arquivo `docs/data_sources.md`
- [ ] Documentar cada dataset com detalhes

---

## 1.4 Criar Estrutura de Pastas do Repositório

### 📁 Estrutura Completa
```
distribuidoras-energia-analise/
│
├── .github/
│   └── workflows/
│       ├── ci.yml                    # Testes automatizados
│       └── dbt-tests.yml             # Validação dbt
│
├── airflow/
│   ├── dags/
│   │   ├── bronze_aneel_distribuidoras.py
│   │   ├── bronze_aneel_indicadores.py
│   │   ├── bronze_aneel_tarifas.py
│   │   ├── silver_transformations.py
│   │   └── gold_aggregations.py
│   ├── plugins/
│   │   └── custom_operators/       # Operadores customizados
│   ├── config/
│   │   └── airflow.cfg
│   └── logs/                        # Gitignored
│
├── dbt/
│   ├── models/
│   │   ├── bronze/
│   │   │   └── sources.yml
│   │   ├── silver/
│   │   │   ├── stg_distribuidoras.sql
│   │   │   ├── stg_indicadores.sql
│   │   │   ├── stg_tarifas.sql
│   │   │   └── schema.yml
│   │   └── gold/
│   │       ├── ranking_qualidade.sql
│   │       ├── evolucao_tarifas.sql
│   │       ├── benchmarking_cpfl.sql
│   │       └── schema.yml
│   ├── tests/
│   │   └── custom_tests/
│   ├── macros/
│   ├── seeds/                       # CSVs de referência
│   │   └── distribuidoras_metadata.csv
│   ├── snapshots/                   # Histórico SCD Type 2
│   ├── dbt_project.yml
│   └── profiles.yml
│
├── src/
│   ├── extractors/
│   │   ├── __init__.py
│   │   ├── aneel_extractor.py      # Classe para extrair ANEEL
│   │   └── ons_extractor.py
│   ├── transformers/
│   │   ├── __init__.py
│   │   ├── data_cleaner.py
│   │   └── data_validator.py
│   ├── loaders/
│   │   ├── __init__.py
│   │   └── postgres_loader.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py               # Configuração de logs
│       ├── config.py               # Gerenciamento de configs
│       └── helpers.py
│
├── tests/
│   ├── unit/
│   │   ├── test_extractors.py
│   │   ├── test_transformers.py
│   │   └── test_loaders.py
│   ├── integration/
│   │   ├── test_pipeline_bronze.py
│   │   └── test_pipeline_silver.py
│   └── fixtures/                   # Dados para testes
│       └── sample_data.csv
│
├── great_expectations/
│   ├── expectations/
│   │   ├── bronze_suite.json
│   │   └── silver_suite.json
│   ├── checkpoints/
│   └── great_expectations.yml
│
├── data/                           # Gitignored (local development)
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── notebooks/
│   ├── 01_exploracao_aneel.ipynb
│   ├── 02_analise_qualidade.ipynb
│   └── 03_benchmarking_cpfl.ipynb
│
├── docs/
│   ├── architecture.md
│   ├── architecture_diagram.png
│   ├── business_case.md
│   ├── data_sources.md
│   ├── setup_guide.md
│   ├── data_dictionary.md          # Dicionário de dados
│   └── sample_data/
│       ├── distribuidoras_sample.csv
│       ├── indicadores_sample.csv
│       └── tarifas_sample.csv
│
├── scripts/
│   ├── setup_local.sh              # Setup ambiente local
│   ├── init_database.sql           # Criação de schemas
│   ├── download_aneel_data.py      # Download inicial dos dados
│   └── run_pipeline.sh
│
├── sql/
│   ├── ddl/
│   │   ├── create_schemas.sql
│   │   └── create_tables.sql
│   └── queries/
│       └── exploratory_queries.sql
│
├── docker/
│   ├── Dockerfile.airflow
│   ├── Dockerfile.dbt
│   └── docker-compose.yml
│
├── .env.example                    # Template de variáveis
├── .gitignore
├── .dockerignore
├── .pre-commit-config.yaml        # Hooks de pre-commit
├── requirements.txt
├── requirements-dev.txt           # Dependências de desenvolvimento
├── setup.py                       # Para instalar src/ como pacote
├── pyproject.toml                 # Poetry (alternativa)
├── Makefile                       # Comandos úteis
├── README.md
└── LICENSE