import data as d
import functions as fn
import visualizations as vs
from datetime import datetime
import pandas as pd

# Indicador
indicador = d.indicador

# 1-Tareas divididas por perfil
## 1.1-Aspectos financieros
### Datos
validacion1 = fn.validaciones(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
price1 = validacion1['prices']
indicador1 = validacion1['row']
validacion2 = fn.validaciones(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
price2 = validacion2['prices']
indicador2 = validacion2['row']
validacion3 = fn.validaciones(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
price3 = validacion3['prices']
indicador3 = validacion3['row']
validacion4 = fn.validaciones(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
price4 = validacion4['prices']
indicador4 = validacion4['row']
validacion5 = fn.validaciones(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
price5 = validacion5['prices']
indicador5 = validacion5['row']
### Validaciones Gráficas
gv1 = vs.grafica_velas(price1, 'USDJPY')
gv2 = vs.grafica_velas(price2, 'USDJPY')
gv3 = vs.grafica_velas(price3, 'USDJPY')
gv4 = vs.grafica_velas(price4, 'USDJPY')
gv5 = vs.grafica_velas(price5, 'USDJPY')

## 1.2-Aspectos estadisticos
### Pruebas
pe1 = fn.heterocedasticidad(indicador)
pe2 = fn.normalidad(indicador)
pe3 = fn.estacionariedad(indicador)
### Gráficas
gpe1 = vs.grafica_fac(indicador)
gpe2 = vs.grafica_facp(indicador)
gpe3 = vs.grafica_estacionalidad(indicador)
gpe4 = vs.grafica_normalidad(indicador)
gpe5 = vs.grafica_atipicos(indicador)

## 1.3-Aspectos computacionales
ohlc = fn.f_consumo_datos(5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY', datetime(2020, 1, 10), datetime(2022, 1, 1))
p1 = fn.escenario1(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
p2 = fn.escenario2(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
p3 = fn.escenario3(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
p4 = fn.escenario4(indicador, 5501031, '7BI4tSbJ', 'FxPro-MT5',  'USDJPY')
e1 = fn.metricas(p1, 100)
e2 = fn.metricas(p2, 100)
e3 = fn.metricas(p3, 100)
e4 = fn.metricas(p4, 100)
metricas = pd.concat([e1, e2, e3, e4])
metricas['Escenario'] = ['A', 'B', 'C', 'D']