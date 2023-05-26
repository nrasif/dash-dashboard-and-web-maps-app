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
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        wells: Optional[list[str]] = None,
    ) -> DataSource:

        if from_date is None:
            from_date = self.unique_from_date
        if to_date is None:
            to_date = self.unique_to_date
        if wells is None:
            wells = self.unique_wells
        
        filtered_data = self._data[
            (self._data[ProductionDataSchema.DATE] >= from_date)    &
            (self._data[ProductionDataSchema.DATE] <= to_date)      &
            (self._data[ProductionDataSchema.WELLBORE].isin(wells))
        ]
        
        return DataSource(filtered_data)
    
    def create_pivot_table(self) -> pd.DataFrame:
        # pt = self._data.pivot_table(
        #     values=
        # )
        pass
    
    # property for filtering data
    @property
    def earliest_date(self) -> str:
        return self._data[ProductionDataSchema.DATE].min()
    
    @property
    def latest_date(self) -> str:
        return self._data[ProductionDataSchema.DATE].max()
    
    @property
    def unique_from_date(self) -> str:
        return self._data[ProductionDataSchema.DATE]
    
    @property
    def unique_to_date(self) -> str:
        return self._data[ProductionDataSchema.DATE] 
    
    @property
    def all_wells(self) -> list[str]:
        return self._data[ProductionDataSchema.WELLBORE].tolist()
    
    @property
    def unique_wells(self) -> list[str]:
        return sorted(set(self.all_wells))
    
    #property for summary card
    @property
    def sum_oil(self) -> float:
        return self._data[ProductionDataSchema.BORE_OIL_VOL].sum()
    
    @property
    def sum_gas(self) -> float:
        return self._data[ProductionDataSchema.BORE_GAS_VOL].sum()
    
    @property
    def sum_water(self) -> float:
        return self._data[ProductionDataSchema.BORE_WI_VOL].sum()
    
    @property
    def sum_on_hours(self) -> float:
        return self.data[ProductionDataSchema.ON_STREAM_HRS].sum()
    