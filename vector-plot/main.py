from db.database import *
from utils.functions import *
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    df = get_coordenadas()
    df_mag = get_magnitude()
    
    # Concatena a magnitude com as coordenadas
    df.loc[:, 'mag'] = df_mag.loc[:, 'mag']

    # Limpa o valor das magnitudes
    df_clean = clean_df(df)

    show_plot(df_clean, **get_config())