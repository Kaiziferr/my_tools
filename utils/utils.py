from unicodedata import normalize

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

def normalize_word(word):
  """Normaliza palabras"""
  word = word.replace(' ', '')
  find_guion = word.find('_')
  list_word = []
  if find_guion:
    list_word = [w for w in word.split('_') if w != '']
  else:
    list_word = word
  word = list(map(lambda x: x.lower(), list_word))
  word = [normalize('NFKD', c).encode('ASCII', 'ignore').decode() for c in word]
  word = "_".join(word)
  return word

def normalize_name_columns(columns):
  """Normaliza columnas"""
  columns = list(map(lambda x: normalize_word(x), columns))
  return columns

