from __future__ import annotations

import os

from distribuidoras_energia_analise.ingestion.bronze.pipeline import run_bronze_ckan_csv


def main() -> None:
    """
    Execução mínima via env vars (simples e suficiente pro Bronze inicial).
    """
    dataset = os.getenv("BRONZE_DATASET", "dataset_indicadores")
    resource_url = os.getenv("BRONZE_RESOURCE_URL", "https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/4493985c-baea-429c-9df5-3030422c71d7/download/indicadores-continuidade-coletivos-2020-2029.csv")
    dt_ref = os.getenv("BRONZE_DT_REF")  # opcional

    if not resource_url:
        raise SystemExit(
            "export BRONZE_RESOURCE_URL='https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/4493985c-baea-429c-9df5-3030422c71d7/download/indicadores-continuidade-coletivos-2020-2029.csv'"
        )

    out_dir = run_bronze_ckan_csv(dataset=dataset, resource_url=resource_url, dt_ref=dt_ref)
    print(f"Bronze OK. Partição criada em: {out_dir}")


if __name__ == "__main__":
    main()
