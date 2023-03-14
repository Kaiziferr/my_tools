def __number_intervals(data, feature, **kward):
  """Calcula el número de intervalos variables continuas"""
  n_size = 126
  iqr = data[feature].quantile(0.75) - data[feature].quantile(0.25)
  
  
  freedman_diaconis = 2*iqr / n_size**(1/3)
  regla_sturges = 1+3.3 * np.log10(n_size)
  raiz = np.sqrt(n_size)
  unknown = np.log(n_size)/np.log(2)

  resolve = {'freedman_diaconis':freedman_diaconis, 
             'sturges_rule':regla_sturges,
             'sqrt':raiz,
             'unknown':unknown}
  
  return resolve

def table_frecuency_dsicrete(data, category, values):
  """Tabla de frecuencia variable discreta"""
  table_frecuency = pd.DataFrame()
  table_frecuency['xi'] = data[category].values
  table_frecuency['ni'] = data[values].values
  table_frecuency['fi'] = round(table_frecuency['ni']/data[values].sum(), 3)
  table_frecuency['Ni'] = table_frecuency['ni'].cumsum()
  table_frecuency['Fi'] = round(table_frecuency['fi'].cumsum(), 3)
  temp = pd.Series(table_frecuency['Fi'])
  temp.iloc[-1] = round(temp.iloc[-1] , 0)
  table_frecuency['Fi'] = temp
  return table_frecuency

#table_frecuency = table_frecuency_dsicrete(data, 'dia', 'venta_refresco')