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