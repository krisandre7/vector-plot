from db.database import *
from utils.functions import *

if __name__ == '__main__':
    # Obtém os dataframes de coordenadas e magnitude
    # a partir de suas respectivas tabelas
    df = get_coordenadas()
    df_mag = get_magnitude()
    
    # Concatena a magnitude com as coordenadas
    df.loc[:, 'mag'] = df_mag.loc[:, 'mag']

    # Limpa o valor das magnitudes
    df_clean = clean_df(df)

    # Obtém as configurações do plot a partir do config.yaml
    config = get_config()
    
    # Plota os dados
    show_plot(df_clean, **config)