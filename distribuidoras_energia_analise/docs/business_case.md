# Business Case - Análise Comparativa de Distribuidoras

## Contexto
[Explicar o setor de distribuição brasileiro]

## Problema
[Descrever a falta de transparência e comparabilidade]

## Objetivo
[Sistema de análise para benchmarking]

## Stakeholders
[Listar e explicar cada um]

## Perguntas de Negócio
[As 5 categorias acima]

## KPIs e Métricas
[Detalhar cada indicador]

## Valor Gerado
[Como este projeto agrega valor]

## Escopo
### Incluído:
- Top 10 distribuidoras por número de consumidores
- Dados de 2019-2024
- Foco em DEC, FEC, tarifas, perdas

### Não incluído (futuro):
- Geração distribuída
- Mercado livre de energia
- Dados em tempo real
```

### ✅ Checklist - Seção 1.1

- [ ] Ler sobre o setor de distribuição de energia no Brasil
- [ ] Definir quais 10 distribuidoras analisar (sugestão abaixo)
- [ ] Criar arquivo `docs/business_case.md`
- [ ] Documentar as 5 categorias de perguntas de negócio
- [ ] Listar todos os KPIs que serão calculados

**Distribuidoras sugeridas para análise:**
1. CPFL Paulista (SP)
2. Enel São Paulo
3. Enel Rio (Light)
4. CEMIG (MG)
5. Copel (PR)
6. Celesc (SC)
7. Energisa (vários estados)
8. EDP São Paulo (antiga Bandeirante)
9. RGE (RS - do grupo CPFL)
10. Equatorial (MA/PA/AL)

---

## 1.2 Desenhar Arquitetura de Dados

### 🏗️ Arquitetura - Visão Geral
```
┌─────────────────────────────────────────────────┐
│            FONTES DE DADOS (APIs/CSV)           │
├─────────────┬─────────────┬─────────────────────┤
│   ANEEL     │     ONS     │    IBGE/BCB         │
│  (Principal)│  (Geração)  │  (Complementar)     │
└──────┬──────┴──────┬──────┴──────┬──────────────┘
       │             │              │
       │    AIRFLOW ORCHESTRATION   │
       │    (DAGs de Extração)      │
       │                            │
       ▼                            ▼
┌─────────────────────────────────────────────────┐
│         BRONZE LAYER (Raw Data Lake)            │
├─────────────────────────────────────────────────┤
│ • aneel_distribuidoras_raw/                     │
│ • aneel_dec_fec_raw/                            │
│ • aneel_tarifas_raw/                            │
│ • aneel_consumidores_raw/                       │
│ • ons_geracao_raw/ (CPFL Renováveis)            │
│                                                 │
│ Storage: Parquet particionado por data_extracao│
│ Retenção: Todos os dados históricos             │
└──────┬──────────────────────────────────────────┘
       │
       │    DBT TRANSFORMATIONS
       │    (Limpeza e Padronização)
       │
       ▼
┌─────────────────────────────────────────────────┐
│        SILVER LAYER (Cleaned & Validated)       │
├─────────────────────────────────────────────────┤
│ • distribuidoras (dim)                          │
│ • indicadores_qualidade (fact)                  │
│ • tarifas (fact)                                │
│ • consumidores (fact)                           │
│ • geracao_cpfl (fact)                           │
│                                                 │
│ Storage: PostgreSQL (schemas: silver)           │
│ Validação: Great Expectations                   │
└──────┬──────────────────────────────────────────┘
       │
       │    DBT AGGREGATIONS
       │    (Business Metrics)
       │
       ▼
┌─────────────────────────────────────────────────┐
│         GOLD LAYER (Analytics Ready)            │
├─────────────────────────────────────────────────┤
│ • ranking_qualidade_mensal                      │
│ • evolucao_tarifas                              │
│ • benchmarking_cpfl                             │
│ • kpis_consolidados                             │
│ • comparativo_regional                          │
│                                                 │
│ Storage: PostgreSQL (schemas: gold)             │
│ Uso: Dashboards, Reports, APIs                  │
└─────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────┐
│              CAMADA DE CONSUMO                  │
├─────────────────────────────────────────────────┤
│ • Streamlit Dashboard (opcional)                │
│ • Jupyter Notebooks (análises ad-hoc)           │
│ • Exports CSV (para stakeholders)               │
└─────────────────────────────────────────────────┘
```

### 🔧 Componentes Técnicos

**1. Orquestração - Apache Airflow**
```
DAGs a criar:
├── dag_bronze_aneel_distribuidoras (mensal)
├── dag_bronze_aneel_indicadores (mensal)
├── dag_bronze_aneel_tarifas (anual)
├── dag_bronze_ons_geracao (diário)
├── dag_silver_transformations (após bronze)
└── dag_gold_aggregations (após silver)
```

**2. Processamento - Python + Pandas**
```
Bronze → Silver:
- Limpeza de dados (nulls, duplicatas)
- Padronização de nomes
- Conversão de tipos
- Enriquecimento (geo, códigos)

Silver → Gold:
- Agregações temporais
- Cálculos de KPIs
- Rankings e percentis
```

**3. Transformação - dbt**
```
models/
├── bronze/
│   └── sources.yml (definição das fontes)
├── silver/
│   ├── stg_distribuidoras.sql
│   ├── stg_indicadores.sql
│   ├── stg_tarifas.sql
│   └── stg_consumidores.sql
└── gold/
    ├── ranking_qualidade.sql
    ├── evolucao_tarifas.sql
    └── benchmarking_cpfl.sql
```

**4. Armazenamento - PostgreSQL**
```
Schemas:
├── bronze (raw data)
├── silver (cleaned data)
└── gold (analytics)

Justificativa PostgreSQL:
- Gratuito e open source
- Fácil setup com Docker
- Suficiente para volume de dados
- Permite queries SQL complexas
```

**Alternativa Cloud (BigQuery):**
Se preferir cloud, use BigQuery:
- Datasets: bronze, silver, gold
- Vantagem: Escala melhor, serverless
- Desvantagem: Custos (mas tem free tier)

**5. Qualidade de Dados - Great Expectations**
```
Expectativas a implementar:
- Valores de DEC/FEC > 0
- Tarifas dentro de range esperado
- Sem duplicatas por (distribuidora, período)
- Nomes de distribuidoras válidos
- Datas sequenciais sem gaps
```

**6. CI/CD - GitHub Actions**
```
Workflows:
├── ci.yml (testes em PRs)
├── dbt-test.yml (validação de modelos)
└── deploy.yml (opcional)