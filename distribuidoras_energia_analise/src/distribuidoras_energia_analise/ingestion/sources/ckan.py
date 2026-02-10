from __future__ import annotations
from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class CKANSource:
    """
    Fonte CKAN simples para ingestão Bronze.
    Por enquanto, assume uma URL direta para CSV (download).
    """
    dataset: str
    resource_url: str

def fetch_csv(source: CKANSource, *, sep: str = ";", encoding: str = "latin-1") -> pd.DataFrame:
    """
    Baixa um CSV via URL e retorna um DataFrame.
    (Sem regra de negócio, sem persistência.)
    """
    df = pd.read_csv(source.resource_url, sep=sep, encoding=encoding)
    return df
