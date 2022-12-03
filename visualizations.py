# Librerias
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
import statsmodels.api as sm
import numpy as np
from scipy import stats

# 1-Tareas divididas por perfil
## 1.1-Aspectos financieros
def grafica_velas(precios, symbol):
    fig = go.Figure(data=[go.Candlestick(x=precios['time'],
                          open=precios['open'], 
                          high=precios['high'], 
                          low=precios['low'], 
                          close=precios['close'])])
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_layout(title=symbol)
    return fig
## 1.2-Aspectos estadisticos
def grafica_fac(indicador):
    indicador = indicador.set_index('DateTime')
    plot_acf(indicador['Actual'])
    return
def grafica_facp(indicador):
    indicador = indicador.set_index('DateTime')
    plot_pacf(indicador['Actual'])
    return 
def grafica_estacionalidad(indicador):
    indicador = indicador.set_index('DateTime')
    estacionalidad = sm.tsa.seasonal_decompose(indicador['Actual'], model='additive', period=12)
    plt.rc("figure",figsize=(20,20))
    estacionalidad.plot()
    return 
def grafica_atipicos(indicador):
    fig, ax = plt.subplots()
    ax.set_title('Detección Atípicos')
    ax.boxplot(indicador['Actual'], labels=["Actual"])
    return fig
def grafica_normalidad(indicador):
    actual = indicador['Actual']
    mu, sigma = stats.norm.fit(actual)
    x_hat = np.linspace(min(actual), max(actual), num=100)
    y_hat = stats.norm.pdf(x_hat, mu, sigma)
    fig, ax = plt.subplots(figsize=(7,4))
    ax.plot(x_hat, y_hat, linewidth=2, label='normal')
    ax.hist(x=actual, density=True, bins=30, color="#3182bd", alpha=0.5)
    ax.plot(actual, np.full_like(actual, -0.01), '|k', markeredgewidth=1)
    ax.set_title('Distribución indicador')
    ax.set_xlabel('Actual')
    ax.set_ylabel('Densidad de probabilidad')
    ax.legend();
    return fig