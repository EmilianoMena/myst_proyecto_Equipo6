# Librerias 
import pandas as pd

# Indicador
indicador = pd.read_csv('files\Gross Domestic Product Annualized - United States')
indicador = indicador.drop('Revised', axis=1)
indicador['Consensus'] = indicador['Consensus'].fillna(indicador['Previous'].shift(0))
indicador['Previous'] = indicador['Previous'].fillna(indicador['Actual'].shift(1))