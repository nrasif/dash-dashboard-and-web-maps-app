import pandas as pd

class LogDataSchema:
    WELLBORE = "WELL_BORE_CODE"
    DEPTH = "DEPTH_MD"
    X     = "X_LOC"
    Y     = "Y_LOC"
    Z     = "Z_LOC"
    CALI  = "CALI"
    RDEP  = "RDEP"
    GR    = "GR"
    RHOB  = "RHOB"
    NPHI  = "NPHI"
    SP    = "SP"
    DTC   = "DTC"
    LITH  = "LITH"
    # WELL_BORE_CODE,DEPTH_MD,X_LOC,Y_LOC,Z_LOC,CALI,RDEP,GR,RHOB,NPHI,SP,DTC,LITH

def load_well_log_data(path: str) -> pd.DataFrame:
    
    log_data = pd.read_csv(
        path,
        dtype={
            LogDataSchema.WELLBORE: str,
            LogDataSchema.DEPTH: float,
            LogDataSchema.X: float,
            LogDataSchema.Y: float,
            LogDataSchema.Z: float,
            LogDataSchema.CALI: float,
            LogDataSchema.RDEP: float,
            LogDataSchema.GR  : float,
            LogDataSchema.RHOB: float,
            LogDataSchema.NPHI: float,
            LogDataSchema.SP  : float,
            LogDataSchema.DTC : float,
            LogDataSchema.LITH: str,
        }
    )
    
    return log_data

class ProductionDataSchema:
    DATE                  = "DATEPRD"
    MONTH                 = "MONTHPRD"
    YEAR                  = "YEARPRD"
    WELLBORE              = "WELL_BORE_CODE"
    ON_STREAM_HRS         = "ON_STREAM_HRS"
    AVG_DOWNHOLE_PRESSURE = "AVG_DOWNHOLE_PRESSURE"
    AVG_DP_TUBING         = "AVG_DP_TUBING"
    AVG_WHP_P             = "AVG_WHP_P"
    AVG_WHT_P             = "AVG_WHT_P"
    DP_CHOKE_SIZE         = "DP_CHOKE_SIZE"
    BORE_OIL_VOL          = "BORE_OIL_VOL"
    BORE_GAS_VOL          = "BORE_GAS_VOL"
    BORE_WAT_VOL          = "BORE_WAT_VOL"
    BORE_WI_VOL           = "BORE_WI_VOL"
    FLOW_KIND             = "FLOW_KIND"
    # DATEPRD,WELL_BORE_CODE,ON_STREAM_HRS,AVG_DOWNHOLE_PRESSURE,AVG_DP_TUBING,AVG_WHP_P,AVG_WHT_P,DP_CHOKE_SIZE,BORE_OIL_VOL,BORE_GAS_VOL,BORE_WAT_VOL,BORE_WI_VOL,FLOW_KIND


def load_well_production_data(path: str) -> pd.DataFrame:
    
    production_data = pd.read_csv(
        path,
        dtype={
            ProductionDataSchema.WELLBORE             : str,
            ProductionDataSchema.ON_STREAM_HRS        : float,
            ProductionDataSchema.AVG_DOWNHOLE_PRESSURE: float,
            ProductionDataSchema.AVG_DP_TUBING        : float,
            ProductionDataSchema.AVG_WHP_P            : float,
            ProductionDataSchema.AVG_WHT_P            : float,
            ProductionDataSchema.DP_CHOKE_SIZE        : float,
            ProductionDataSchema.BORE_OIL_VOL         : float,
            ProductionDataSchema.BORE_GAS_VOL         : float,
            ProductionDataSchema.BORE_WAT_VOL         : float,
            ProductionDataSchema.BORE_WI_VOL          : float,
            ProductionDataSchema.FLOW_KIND            : str,
        },
        parse_dates=[ProductionDataSchema.DATE]
    )
    
    return production_data

class ProductionDataMonthlySchema:
    DATE                  = "DATEPRD"
    MONTH                 = "MONTHPRD"
    YEAR                  = "YEARPRD"
    WELLBORE              = "WELL_BORE_CODE"
    ON_STREAM_HRS         = "ON_STREAM_HRS"
    OIL_SM3               = "OIL_SM3"
    GAS_SM3               = "GAS_SM3"
    WATER_SM3             = "WATER_SM3"
    GI_SM3                = "GI_SM3"
    WI_SM3                = "WI_SM3"
    # ,WELL_BORE_CODE,YEAR,MONTH,ON_STEAM_HRS,OIL_SM3,GAS_SM3,WATER_SM3,GI_SM3,WI_SM3


def load_well_production_data_monthly(path: str) -> pd.DataFrame:
    
    production_data_monthly = pd.read_csv(
        path,
        dtype={
            
            ProductionDataMonthlySchema.MONTH         : str,
            ProductionDataMonthlySchema.YEAR          : str,
            ProductionDataMonthlySchema.WELLBORE      : str,
            ProductionDataMonthlySchema.ON_STREAM_HRS : float,
            ProductionDataMonthlySchema.OIL_SM3       : float,
            ProductionDataMonthlySchema.GAS_SM3       : float,
            ProductionDataMonthlySchema.WATER_SM3     : float,
            ProductionDataMonthlySchema.GI_SM3        : float,
            ProductionDataMonthlySchema.WI_SM3        : float,
            
        },
        parse_dates=[ProductionDataMonthlySchema.DATE]
    )
    
    return production_data_monthly