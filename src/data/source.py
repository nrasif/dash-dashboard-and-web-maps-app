from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from datetime import datetime, date
import json

import pandas as pd
import geopandas as gpd

from .loader import ProductionDataSchema, allBLOCKS

@dataclass
class DataSource:
    _data: Optional[pd.DataFrame] = None
    _geodata_blocks: Optional[gpd.GeoDataFrame] = None
    
    # main filter map
    def filter_block(
        self,
        name_block: Optional[list[str]] = None,
        status_block: Optional[list[str]] = None,
        operator_block: Optional[list[str]] = None,
        total_wellMin: Optional[int] = None,
        total_wellMax: Optional[int] = None,
        sq_kmMin: Optional[float] = None,
        sq_kmMax: Optional[float] = None,
        reserveMin: Optional[float] = None,
        reserveMax: Optional[float] = None
        
    ) -> DataSource:
        
        if name_block is None:
            name_block = self.all_name_blocks
        if status_block is None:
            status_block = self.all_status_block
        if operator_block is None:
            operator_block = self.all_operator_block
        if total_wellMin is None:
            total_wellMin = self.minimum_total_well
        if total_wellMax is None:
            total_wellMax = self.maximum_total_well
        if sq_kmMin is None:
            sq_kmMin = self.minimum_area_km
        if sq_kmMax is None:
            sq_kmMax = self.maximum_area_km
        if reserveMin is None:
            reserveMin = self.minimum_reserve
        if reserveMax is None:
            reserveMax = self.maximum_reserve
        
        filtered_block_data = self._geodata_blocks[
            (self._geodata_blocks[allBLOCKS.BLOCK_NAME].isin(name_block))           &
            (self._geodata_blocks[allBLOCKS.STATUS_BLOCK].isin(status_block))       &
            (self._geodata_blocks[allBLOCKS.OPERATOR_BLOCK].isin(operator_block))   &
            (self._geodata_blocks[allBLOCKS.TOTAL_WELL].between(total_wellMin, total_wellMax)) &
            (self._geodata_blocks[allBLOCKS.AREA_BLOCK].between(sq_kmMin, sq_kmMax)) &
            (self._geodata_blocks[allBLOCKS.RESERVE_BLOCK].between(reserveMin, reserveMax))
        ]
        return DataSource(filtered_block_data)
    
    # main filter productions
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
    
    # pivot table-ing
    # Date, Well - for Moving Average Chart
    def create_pivot_table_date_well_ma(self, column_name: str) -> pd.DataFrame:
        pt = self._data.pivot_table(
            values=[column_name],
            index=[ProductionDataSchema.DATE, ProductionDataSchema.WELLBORE],
            # aggfunc="sum",
            # fill_value=0,
            # dropna=False,
        )
        return pt.sort_values(ProductionDataSchema.DATE, ascending=True).reset_index()
    
    # Cumulative Amount based on Well - for Pie Chart
    def create_pivot_table_well(self, column_name: str, column_name2: Optional[str] = None) -> pd.DataFrame:
        if column_name2 is not None:
            pt = self._data.pivot_table(
                values=[column_name, column_name2],
                index=[ProductionDataSchema.WELLBORE],
                aggfunc="sum"
            )
            
        else:
            pt = self._data.pivot_table(
                values=[column_name],
                index=[ProductionDataSchema.WELLBORE],
                aggfunc="sum"
            )
            
        return pt.sort_values(ProductionDataSchema.WELLBORE, ascending=True).reset_index()
    
    # Cumulative Amount based on Dates - for Line Chart
    def create_pivot_table_date(self, column_name: str, column_name2: Optional[str] = None) -> pd.DataFrame:
        if column_name2 is not None:
            pt = self._data.pivot_table(
                values=[column_name, column_name2],
                index=[ProductionDataSchema.DATE],
                aggfunc="sum"
            )
            
        else:
            pt = self._data.pivot_table(
                values=[column_name],
                index=[ProductionDataSchema.DATE],
                aggfunc="sum"
            )
        return pt.sort_values(ProductionDataSchema.DATE, ascending=True).reset_index()
    
    # Cumulative amount based on Dates, fill value with 0, for Water Cut and Gas Oil Ratio
    def create_pivot_table_date_avg(self, column_name: str, column_name2: Optional[str] = None) -> pd.DataFrame:
        if column_name2 is not None:
            pt = self._data.pivot_table(
                values=[column_name, column_name2],
                index=[ProductionDataSchema.DATE],
                aggfunc="mean",
                dropna=False,
            )
            
        else:
            pt = self._data.pivot_table(
                values=[column_name],
                index=[ProductionDataSchema.DATE],
                aggfunc="mean",
                dropna=False,
            )
        return pt.sort_values(ProductionDataSchema.DATE, ascending=True).interpolate(method='backfill').reset_index()
    
    
    #for summary card
    def abbreviate_value(self, value: float) -> str:
        units = [
            '', 'K', 'M',
            # 'B', 'T'
        ]
        unit_index = 0
        while value >= 1000 and unit_index < len(units) - 1:
            value /= 1000
            unit_index += 1
        formatted_value = f'{value:,.2f}'.rstrip('0').rstrip('.')
        return f"{formatted_value}{units[unit_index]}"
    

    
    # property for filtering data
    # property it's about something that we really need to do with all the properties of the dataframe:)
    # basic = create dataframe of pandas to be called
    @property
    def to_dataframe(self):
        dataframe = pd.DataFrame(self._data)
        return dataframe
    
    @property
    def to_dataframe_geopandas(self):
        dataframe_geo = gpd.GeoDataFrame(self._geodata_blocks)
        return dataframe_geo
    
    @property #karena kegeser kalo cuma dimasukkin 1 dataframe
    def to_dataframe_geopandas_temp(self):
        dataframe_geo = gpd.GeoDataFrame(self._data)
        return dataframe_geo

    @property
    def to_json_(self):
        json_geo = self._geodata_blocks[allBLOCKS].to_json()
        return json_geo
    
    #Map Utilization
    @property
    def all_name_blocks(self) -> list[str]:
        return self._geodata_blocks[allBLOCKS.BLOCK_NAME].tolist()
    
    @property
    def all_status_block(self) -> list[str]:
        return self._geodata_blocks[allBLOCKS.STATUS_BLOCK].tolist()

    @property
    def unique_status(self) -> list[str]:
        return sorted(set(self.all_status_block))
    
    @property
    def all_operator_block(self) -> list[str]:
        return self._geodata_blocks[allBLOCKS.OPERATOR_BLOCK].tolist()
    
    @property
    def unique_operator(self) -> list[str]:
        return sorted(set(self.all_operator_block))
    
    @property
    def minimum_total_well(self) -> int:
        return self._geodata_blocks[allBLOCKS.TOTAL_WELL].min()
    
    @property
    def maximum_total_well(self) -> int:
        return self._geodata_blocks[allBLOCKS.TOTAL_WELL].max()
    
    @property
    def all_total_well(self) -> int:
        return self._geodata_blocks[allBLOCKS.TOTAL_WELL]
    
    @property
    def minimum_area_km(self) -> float:
        return self._geodata_blocks[allBLOCKS.AREA_BLOCK].min()
    
    @property
    def maximum_area_km(self) -> float:
        return self._geodata_blocks[allBLOCKS.AREA_BLOCK].max()
    
    @property
    def minimum_reserve(self) -> float:
        return self._geodata_blocks[allBLOCKS.RESERVE_BLOCK].min()
    
    @property
    def maximum_reserve(self) -> float:
        return self._geodata_blocks[allBLOCKS.RESERVE_BLOCK].max()
    
    @property
    def geometry_(self) -> str:
        return self._geodata_blocks[allBLOCKS.GEOMETRY_BLOCK].tolist()
    
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
    
    #property for oil rate line chart
    @property
    def moving_average(self):
        return self._data[ProductionDataSchema.MOVING_AVERAGE]