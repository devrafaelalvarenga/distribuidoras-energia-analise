from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import pandas as pd

from distribuidoras_energia_analise.ingestion.sources.ckan import CKANSource, fetch_csv
from distribuidoras_energia_analise.ingestion.bronze.writer import write_parquet
from distribuidoras_energia_analise.ingestion.bronze.metadata import build_and_write_meta


@dataclass(frozen=True)
class BronzeRunConfig:
    dataset: str
    dt_ref: str  # YYYY-MM-DD
    base_dir: Path = Path("data/bronze/raw")


def run_bronze_ckan_csv(
    *,
    dataset: str,
    resource_url: str,
    dt_ref: str | None = None,
) -> Path:
    """
    Pipeline Bronze mínimo:
    - baixa CSV
    - grava parquet em data/bronze/raw/<dataset>/dt_ref=YYYY-MM-DD/
    - grava _meta.json na mesma pasta
    Retorna o diretório da partição.
    """
    dt_ref = dt_ref or date.today().isoformat()
    cfg = BronzeRunConfig(dataset=dataset, dt_ref=dt_ref)

    out_dir = cfg.base_dir / cfg.dataset / f"dt_ref={cfg.dt_ref}"

    source = CKANSource(dataset=dataset, resource_url=resource_url)
    df: pd.DataFrame = fetch_csv(source)

    data_file = write_parquet(df, out_dir)
    build_and_write_meta(
        df=df,
        dataset=dataset,
        source_url=resource_url,
        data_file_path=data_file,
        out_dir=out_dir,
    )

    return out_dir
