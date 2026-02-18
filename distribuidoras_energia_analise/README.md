# Análise Comparativa de Distribuidoras de Energia do Brasil

## 📊 Sobre o Projeto

Sistema de engenharia de dados para análise comparativa de desempenho das principais distribuidoras de energia elétrica do Brasil, utilizando dados públicos da ANEEL e ONS.

### Objetivos
- Comparar indicadores de qualidade (DEC/FEC) entre distribuidoras
- Analisar evolução tarifária por região e classe de consumo
- Realizar benchmarking da CPFL vs concorrentes
- Identificar padrões de eficiência operacional

## 🏗️ Arquitetura

![Arquitetura](docs/architecture_diagram.png)

**Stack Tecnológica:**
- **Orquestração:** Apache Airflow
- **Transformação:** dbt (Data Build Tool)
- **Armazenamento:** PostgreSQL
- **Qualidade:** Great Expectations
- **Linguagem:** Python 3.14
- **Containerização:** Docker

**Arquitetura de Dados:** Medallion (Bronze → Silver → Gold)

## 🎯 Distribuidoras Analisadas

1. CPFL Paulista (SP)
2. Enel São Paulo
3. Light (RJ)
4. CEMIG (MG)
5. Copel (PR)
6. Celesc (SC)
7. RGE Sul (RS)
8. EDP São Paulo
9. Energisa
10. Equatorial

## 📈 KPIs e Métricas

### Qualidade do Serviço
- DEC (Duração Equivalente de Interrupção)
- FEC (Frequência Equivalente de Interrupção)

### Tarifas
- Tarifa média por distribuidora
- Evolução tarifária (% a.a.)
- Comparativo por classe (residencial, comercial, industrial)

### Operacionais
- Perdas técnicas e não-técnicas
- Consumidores por km de rede
- Energia distribuída (GWh)

## 🚀 Como Executar

### Pré-requisitos
- Docker & Docker Compose
- Python 3.12+
- Git

### Setup Local
```bash
# Clone o repositório
git clone https://github.com/devrafaelalvarenga/distribuidoras-energia-analise.git
cd distribuidoras-energia-analise

# Configure variáveis de ambiente
cp .env.example .env
# Edite .env com suas configurações

# Execute setup
./scripts/setup_local.sh

# Suba os containers
docker-compose up -d

# Acesse Airflow
http://localhost:8080
```

## 📁 Estrutura do Projeto
```
├── airflow/          # DAGs e configurações
├── dbt/              # Modelos de transformação
├── src/              # Código Python (extractors, transformers)
├── tests/            # Testes unitários e integração
├── docs/             # Documentação
└── notebooks/        # Análises exploratórias
```

## 📊 Fontes de Dados

- **ANEEL** (Agência Nacional de Energia Elétrica)
  - Distribuidoras
  - Indicadores DEC/FEC
  - Tarifas
  - Consumidores
  - Geração por usina (CPFL)

Mais detalhes em [docs/data_sources.md](docs/data_sources.md)

## 🔄 Pipeline de Dados

1. **Bronze:** Extração de dados brutos da ANEEL/ONS
2. **Silver:** Limpeza, padronização e validação
3. **Gold:** Agregações e métricas de negócio

## 🧪 Qualidade de Dados

- Validações automáticas com Great Expectations
- Testes dbt em modelos
- CI/CD com GitHub Actions

## 📈 Status do Projeto

🚧 **Em Desenvolvimento**

- [x] Task 1: Planejamento e Arquitetura
- [x] Task 2: Setup do Ambiente
- [ ] Task 3: Ingestão de Dados (Bronze)
- [ ] Task 4: Transformação (Silver)
- [ ] Task 5: Camada Analítica (Gold)
- [ ] Task 6: Qualidade e Testes
- [ ] Task 7: CI/CD
- [ ] Task 8: Documentação Final

## 👤 Autor

Rafael Alvarenga
- LinkedIn: [link]
- GitHub: [link]

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes

## 🙏 Agradecimentos

- ANEEL pela disponibilização dos dados abertos
- ONS pelos dados de geração
- Comunidade open source
```

#### `LICENSE` (MIT)
```
MIT License

Copyright (c) 2025 [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy...
[texto completo da licença MIT]

✅ CHECKLIST FINAL - TASK 1 COMPLETA

Antes de considerar a Task 1 concluída, você deve ter:
Planejamento

 Caso de uso definido: "Análise Comparativa de Distribuidoras"
 10 distribuidoras selecionadas para análise
 5 categorias de perguntas de negócio documentadas
 Lista de KPIs e métricas definida
 Arquivo docs/business_case.md criado e completo

Arquitetura

 Decisão tomada: PostgreSQL ou BigQuery
 Diagrama de arquitetura desenhado
 Diagrama salvo em docs/architecture_diagram.png
 Arquivo docs/architecture.md criado
 Justificativa de tecnologias documentada
 Estrutura de schemas/layers definida

Fontes de Dados

 Portal ANEEL explorado
 3+ CSVs baixados manualmente
 Teste de leitura com Pandas realizado
 Amostras salvas em docs/sample_data/
 Arquivo docs/data_sources.md criado
 Todos os 5 datasets principais documentados
 Limitações e desafios identificados

Repositório

 Repositório GitHub criado
 Estrutura de pastas completa criada localmente
 .gitignore configurado
 README.md inicial criado
 LICENSE adicionado
 .env.example criado
 Primeiro commit realizado
 Código no GitHub (branch main)

Documentação

 docs/business_case.md ✓
 docs/architecture.md ✓
 docs/data_sources.md ✓
 docs/data_dictionary.md (template inicial)
 docs/setup_guide.md (template inicial)

