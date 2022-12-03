# Librerias
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import MetaTrader5 as mt5
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
from scipy import stats
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
from scipy.stats import shapiro

# Consumo de Datos de MetaTrader5
def f_consumo_datos(account, password, server, symbol, start, end):
    # Establecer conexión con la terminal de MetaTrader5
    mt5.initialize()
    # Conectarse a la cuenta de FxPro
    mt5.login(account=account, password=password, server=server)
    # OHLC data
    bars = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_M1, start, end)
    # DataFrame del OHLC data	
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return(df)

# 1-Tareas divididas por perfil
## 1.1-Aspectos financieros
def validaciones(indicador, account, password, server, symbol):
    n = np.random.choice([i for i in range(len(indicador))])
    row = indicador.iloc[[n]]
    time = pd.to_datetime(row['DateTime']).dt.to_pydatetime()
    time_start = time - timedelta(minutes=30)
    time_end = time + timedelta(minutes=30)
    prices=f_consumo_datos(account, password, server,  symbol, time_start[0], time_end[0])
    diccionario={'prices':prices,'row':row}
    return diccionario

## 1.2-Aspectos estadisticos
def heterocedasticidad(indicador):
    indicador = indicador.set_index('DateTime')
    modelo = smf.ols('Actual ~ Consensus+Previous', data=indicador).fit()
    names = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
    test_result = sms.het_breuschpagan(modelo.resid, modelo.model.exog)
    return lzip(names, test_result)
def normalidad(indicador):
    indicador = indicador.set_index('DateTime')
    return shapiro(indicador)
def estacionariedad(indicador):
    result = adfuller(indicador['Actual'].values)
    names = ['ADF Statistic', 'p-value']
    resultados = [result[0], result[1]]
    df = pd.DataFrame({
        'Indice':names,
        'Valores':resultados
    })
    return df

## 1.3-Aspectos computacionales
def escenario1(indicador, account, password, server, symbol):
    row = indicador.iloc[[4]]
    time = pd.to_datetime(row['DateTime']).dt.to_pydatetime()
    time_start = time - timedelta(minutes=30)
    time_end = time + timedelta(minutes=30)
    prices=f_consumo_datos(account, password, server,  symbol, time_start[0], time_end[0])
    return prices
def escenario2(indicador, account, password, server, symbol):
    row = indicador.iloc[[3]]
    time = pd.to_datetime(row['DateTime']).dt.to_pydatetime()
    time_start = time - timedelta(minutes=30)
    time_end = time + timedelta(minutes=30)
    prices=f_consumo_datos(account, password, server,  symbol, time_start[0], time_end[0])
    return prices
def escenario3(indicador, account, password, server, symbol):
    row = indicador.iloc[[150]]
    time = pd.to_datetime(row['DateTime']).dt.to_pydatetime()
    time_start = time - timedelta(minutes=30)
    time_end = time + timedelta(minutes=30)
    prices=f_consumo_datos(account, password, server,  symbol, time_start[0], time_end[0])
    return prices
def escenario4(indicador, account, password, server, symbol):
    row = indicador.iloc[[154]]
    time = pd.to_datetime(row['DateTime']).dt.to_pydatetime()
    time_start = time - timedelta(minutes=30)
    time_end = time + timedelta(minutes=30)
    prices=f_consumo_datos(account, password, server,  symbol, time_start[0], time_end[0])
    return prices
def metricas(precio, pips):
    if precio['close'].iloc[-1]>precio['open'].iloc[0]:
        signo = 1
    else:
        signo = -1
    df = pd.DataFrame({
        'Dirección':[signo*(precio['close'].iloc[-1]-precio['open'].iloc[30])],
        'Pips Alcistas':[(precio['high'].iloc[30:-1].max() - precio['open'].iloc[30]) * pips],
        'Pips Bajistas':[(precio['open'].iloc[30] - precio['low'].iloc[30:-1].min()) * pips],
        'Volatilidad':[(precio['high'].max() - precio['low'].min()) * pips]
    })
    return df
# 3-Optimizacion y Backtest de sistema de trading

# 4-Rentabilidad