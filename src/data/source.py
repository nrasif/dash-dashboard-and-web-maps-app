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
    
    #for summary card
    def abbreviate_value(self, value: float) -> str:
        units = ['', 'K', 'M', 'B', 'T']
        unit_index = 0
        while value >= 1000 and unit_index < len(units) - 1:
            value /= 1000
            unit_index += 1
        formatted_value = f'{value:,.2f}'.rstrip('0').rstrip('.')
        return print(f'{formatted_value}{units[unit_index]}')
    

    # def sum_oil(self, data: pd.DataFrame) -> float:
    #     return data[ProductionDataSchema.BORE_OIL_VOL].sum()
    
    
    # def sum_gas(self, data: pd.DataFrame) -> float:
    #     return data[ProductionDataSchema.BORE_GAS_VOL].sum()
    
    
    # def sum_wi(self, data: pd.DataFrame) -> float:
    #     return data[ProductionDataSchema.BORE_WI_VOL].sum()
    
    
    # def sum_on_hours(self, data: pd.DataFrame) -> float:
    #     return data[ProductionDataSchema.ON_STREAM_HRS].sum()
    
    # property for filtering data
    # property it's about something that we really need to do with all the properties of the dataframe:)
    @property
    def all_dates(self):
        return self._data[ProductionDataSchema.DATE]
    
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
    def sum_wi(self) -> float:
        return self._data[ProductionDataSchema.BORE_WI_VOL].sum()
    @property 
    def sum_on_hours(self) -> float:
        return self._data[ProductionDataSchema.ON_STREAM_HRS].sum()