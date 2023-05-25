from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd
from .loader import ProductionDataSchema

@dataclass
class DataSource:
    _data: pd.DataFrame
    
    def filter(
        self,
        
    ) -> DataSource:
        pass