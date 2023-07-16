import matplotlib.pyplot as plt
import yaml
from pandas import DataFrame

def clean_df(df: DataFrame):
    index_0 = df['mag'].between(0, 500, "neither")
    df.loc[index_0, 'mag'] = 0

    index_1000 = df['mag'].between(800, 1300, "neither")
    df.loc[index_1000, 'mag'] = 1000

    index_2000 = df['mag'].between(1720, 2152, "neither")
    df.loc[index_2000, 'mag'] = 2000

    index_3000 = df['mag'].between(2580, 3020, "neither")
    df.loc[index_3000, 'mag'] = 3000

    return df

def show_plot(df: DataFrame, show_id: int, 
              show_0: bool, show_1000: bool, 
              show_2000: bool, show_3000: bool):
    
    df_id = df.loc[df['id'] == show_id]
    
    if df_id.shape[0] == 0:
        raise Exception("ID não existe nos dados!")
    
    if (show_0 or show_1000 or show_2000 or show_3000) is False:
        raise Exception("Nenhuma magnitude escolhida! Escolha ao menos uma.")
    
    ax = plt.axes(projection ="3d")
    
    # frames de cad magnitude
    df_0 = df_id.loc[df_id['mag'] == 0]
    df_1000 = df_id.loc[df_id['mag'] == 1000]
    df_2000 = df_id.loc[df_id['mag'] == 2000]
    df_3000 = df_id.loc[df_id['mag'] == 3000]

    if show_0:
        ax.scatter3D(df_0['x'], df_0['y'], df_0['z'], label="0") # type: ignore
        
    if show_1000:
        ax.scatter3D(df_1000['x'], df_1000['y'], df_1000['z'], label="1000") # type: ignore
    
    if show_2000:
        ax.scatter3D(df_2000['x'], df_2000['y'], df_2000['z'], label="2000") # type: ignore
    
    if show_3000:
        ax.scatter3D(df_3000['x'], df_3000['y'], df_3000['z'], label="3000") # type: ignore

    ax.legend(loc=1)

    plt.show()
    
def get_config():
    plot_config = dict()
    with open("config.yaml", "r") as stream:
        try:
            plot_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc
            
    return plot_config
