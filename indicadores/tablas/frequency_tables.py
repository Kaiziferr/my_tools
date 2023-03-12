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