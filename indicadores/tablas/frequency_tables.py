def _number_intervals(data, feature, **kward):
  """Calcula el número de intervalos"""
  n_size = data[feature].size
  iqr = data[feature].quantile(0.75) - data[feature].quantile(0.25)
  freedman_diaconis = 2*iqr / n_size**(1/3)
  return freedman_diaconis