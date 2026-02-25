from __future__ import annotations

import pandas as pd
from distribuidoras_energia_analise.ingestion.sources.base import FetchResult, SourceConfig, SourceInfo


class CKANCsvFetcher:
    def fetch(self, config: SourceConfig) -> FetchResult:
        resource_url = config.options["resource_url"]
        sep = config.options.get("sep", ";")
        encoding = config.options.get("encoding", "latin-1")

        df = pd.read_csv(resource_url, sep=sep, encoding=encoding)

        info = SourceInfo(
            source_type=config.type,
            dataset=config.dataset,
            origin=resource_url,
            request={"sep": sep, "encoding": encoding},
        )
        return FetchResult(df=df, info=info)
