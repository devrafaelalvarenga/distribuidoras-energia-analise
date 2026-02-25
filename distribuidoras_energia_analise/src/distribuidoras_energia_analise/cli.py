from __future__ import annotations

import os

from distribuidoras_energia_analise.ingestion.sources.loader import build_registry, load_sources_config
from distribuidoras_energia_analise.ingestion.bronze.pipeline import run_bronze


def main() -> None:
    sources_path = os.getenv("SOURCES_YML", "configs/sources.yml")
    dataset = os.getenv("BRONZE_DATASET")  # ex.: "distribuidoras"
    dt_ref = os.getenv("BRONZE_DT_REF")    # opcional

    if not dataset:
        raise SystemExit("Defina BRONZE_DATASET (ex.: export BRONZE_DATASET='distribuidoras')")

    registry = build_registry()
    sources = load_sources_config(sources_path)

    if dataset not in sources:
        available = ", ".join(sorted(sources.keys()))
        raise SystemExit(f"Dataset '{dataset}' não encontrado em {sources_path}. Disponíveis: {available}")

    out_dir = run_bronze(registry=registry, source=sources[dataset], dt_ref=dt_ref)
    print(f"Bronze OK. Partição criada em: {out_dir}")


if __name__ == "__main__":
    main()
