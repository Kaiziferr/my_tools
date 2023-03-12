def feature_by_type(data):
  """Agrupa el nombre de las columnas por su tipo de dato""" 
  count_values = data.dtypes.value_counts()
  indices = count_values.index
  feature_by_type_res = {}
  for i in indices:
    data_type = data.dtypes == i
    data_type = [feature for feature in data_type.index if data_type[feature]]
    feature_by_type_res[str(i)] = data_type

  return feature_by_type_res, count_values