from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from distribuidoras_energia_analise.ingestion.sources.base import SourceConfig, FetchResult
from distribuidoras_energia_analise.ingestion.sources.registry import SourceRegistry
from distribuidoras_energia_analise.ingestion.bronze.writer import write_parquet
from distribuidoras_energia_analise.ingestion.bronze.metadata import write_meta


@dataclass(frozen=True)
class BronzeRunConfig:
    dt_ref: str
    base_dir: Path = Path("data/bronze/raw")


def run_bronze(*, registry: SourceRegistry, source: SourceConfig, dt_ref: str | None = None) -> Path:
    dt_ref = dt_ref or date.today().isoformat()
    cfg = BronzeRunConfig(dt_ref=dt_ref)

    out_dir = cfg.base_dir / source.dataset / f"dt_ref={cfg.dt_ref}"

    fetcher = registry.get(source.type)
    result: FetchResult = fetcher.fetch(source)

    data_file = write_parquet(result.df, out_dir)
    write_meta(df=result.df, info=result.info, data_file_path=data_file, out_dir=out_dir)

    return out_dir
