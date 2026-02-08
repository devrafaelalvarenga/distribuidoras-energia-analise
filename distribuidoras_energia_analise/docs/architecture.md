# Arquitetura de Dados

## Visão Geral
[Explicar arquitetura medallion]

## Decisões Técnicas

### Por que PostgreSQL?
[Justificar escolha]

### Por que Airflow?
[Justificar vs Prefect, Dagster]

### Por que dbt?
[Justificar transformações em SQL]

## Camadas de Dados

### Bronze (Raw)
[Detalhar estrutura]

### Silver (Cleaned)
[Detalhar modelos]

### Gold (Analytics)
[Detalhar agregações]

## Fluxo de Dados
[Descrever ETL completo]

## Escalabilidade
[Como o sistema pode crescer]

## Segurança
[Gestão de credenciais, .env]
```

### ✅ Checklist - Seção 1.2

- [ ] Decidir: PostgreSQL local ou BigQuery cloud?
- [ ] Criar diagrama de arquitetura visual
- [ ] Salvar diagrama em `docs/architecture_diagram.png`
- [ ] Criar arquivo `docs/architecture.md`
- [ ] Documentar justificativa de cada tecnologia
- [ ] Definir estrutura de schemas/datasets

---

## 1.3 Especificar Fontes de Dados

### 📊 Fonte 1: ANEEL - Dados Abertos ⭐ PRINCIPAL

**URL Base:** https://dadosabertos.aneel.gov.br/

**Tipo:** API REST + Download CSV

**Autenticação:** Não requer (público)

**Datasets Necessários:**

#### 1.3.1 - Distribuidoras (Agentes)
```
Dataset: agentes-de-distribuicao
URL: https://dadosabertos.aneel.gov.br/dataset/agentes-de-distribuicao
Formato: CSV
Atualização: Mensal

Campos principais:
- CodAgente: código único da distribuidora
- NomAgente: nome da distribuidora
- SigAgente: sigla (ex: CPFL, ENEL)
- CodEstado: UF de atuação
- CNPJ: identificação fiscal
- DatConcessao: data de início da concessão

Volume: ~100 distribuidoras
Uso: Tabela dimensão (silver.distribuidoras)
```

#### 1.3.2 - Indicadores de Qualidade (DEC/FEC)
```
Dataset: indicadores-coletivos-de-continuidade
URL: https://dadosabertos.aneel.gov.br/dataset/indicadores-coletivos-de-continuidade
Formato: CSV
Atualização: Mensal

Campos principais:
- CodAgente: código da distribuidora
- AnoReferencia: ano
- MesReferencia: mês
- DEC: duração de interrupções (horas)
- FEC: frequência de interrupções (vezes)
- DECLimite: limite regulatório
- FECLimite: limite regulatório

Volume: ~600 registros/mês (54 distribuidoras)
Uso: Tabela fato (silver.indicadores_qualidade)
```

#### 1.3.3 - Tarifas
```
Dataset: tarifas-medias
URL: https://dadosabertos.aneel.gov.br/dataset/tarifa-media
Formato: CSV/Excel
Atualização: Anual (com reajustes intermediários)

Campos principais:
- CodAgente: código da distribuidora
- AnoReferencia: ano da tarifa
- ClasseConsumo: residencial, comercial, industrial
- TarifaMedia: R$/MWh
- DataVigencia: início da vigência

Volume: ~200 registros/ano
Uso: Tabela fato (silver.tarifas)
```

#### 1.3.4 - Consumidores e Consumo
```
Dataset: consumidores-energia-eletrica
URL: https://dadosabertos.aneel.gov.br/dataset/consumidores-energia-eletrica
Formato: CSV
Atualização: Mensal

Campos principais:
- CodAgente: código da distribuidora
- AnoReferencia, MesReferencia
- Classe: residencial, comercial, industrial, rural
- NumConsumidores: quantidade
- Consumo: MWh
- ReceitaFaturada: R$

Volume: ~2.000 registros/mês
Uso: Tabela fato (silver.consumidores)
```

#### 1.3.5 - Perdas (Complementar)
```
Dataset: perdas-de-energia
URL: https://dadosabertos.aneel.gov.br/dataset/perdas-de-energia
Formato: CSV
Atualização: Anual

Campos principais:
- CodAgente
- AnoReferencia
- PerdasTecnicas: % de perdas na rede
- PerdasNaoTecnicas: % de furtos
- PerdasTotais: %

Volume: ~54 registros/ano
Uso: Enriquecimento (silver.distribuidoras)
```

**Como acessar:**
1. Navegar no portal de dados abertos
2. Baixar CSV manualmente (para desenvolvimento)
3. Automatizar via script Python (requests + pandas)

**Limitações:**
- Sem API REST estruturada (apenas downloads)
- Atualizações com delay de 1-2 meses
- Formato CSV pode mudar sem aviso
- Dados de anos anteriores podem ter schemas diferentes

---

### 📊 Fonte 2: ONS - Geração CPFL (Complementar)

**URL:** https://dados.ons.org.br/

**Tipo:** Dados abertos CSV

**Autenticação:** Não requer

**Dataset Necessário:**

#### 1.3.6 - Geração por Usina
```
Dataset: Geração de Energia
URL: https://dados.ons.org.br/dataset/geracao-usina
Formato: CSV
Atualização: Diária

Campos principais:
- nom_usina: nome da usina
- cod_usina: código ONS
- din_instante: data/hora
- val_geracao: MW gerados
- tip_combustivel: hidro, eólica, solar, etc.

Filtro: Usinas do grupo CPFL
- CPFL Renováveis
- CPFL Geração

Volume: Milhares de registros/dia
Uso: Análise complementar de geração (opcional para MVP)
```

**Justificativa:**
Incluir dados de geração da CPFL para análise completa:
- Distribuidora + Geradora
- Matriz energética do grupo CPFL
- Investimentos em renováveis

---

### 📊 Fonte 3: IBGE/BCB (Enriquecimento)

**Uso:** Dados complementares para análises

#### 1.3.7 - IPCA (Inflação)
```
Fonte: Banco Central
API: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados
Uso: Correção de tarifas por inflação
```

#### 1.3.8 - População por UF
```
Fonte: IBGE
Uso: Normalização de consumo per capita
```

---

### 🧪 Teste de Acesso às Fontes

**Você deve fazer agora:**

1. **Acessar portal ANEEL**
```
https://dadosabertos.aneel.gov.br/dataset/agentes-de-distribuicao
→ Baixar CSV manualmente
→ Abrir no Excel/Pandas para ver estrutura