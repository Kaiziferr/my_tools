import seaborn as sns
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.metrics import silhouette_score


def plot_select_n_cluster(best_score, best_cluster, scores, clusters, **kwards):
  fig, ax = plt.subplots(1, 1, figsize=(6, 3.84))
  ax.plot(clusters, scores, marker='o')
  ax.plot(best_cluster, best_score, marker='o', color='r')
  ax.axvline(x=best_cluster,  color='r')
  ax.set_title(kwards['title'])
  ax.set_xlabel('Número clusters')
  ax.set_ylabel(kwards['y_label'])

  
def elbow(model, clusters, data, **kwards):
    """Metodo del codo"""
  range_n_clusters = range(clusters[0], clusters[1])
  inertia = {}
  for k in range_n_clusters:
    model.n_clusters= k
    model.fit(data)
    inertia[k] = model.inertia_
  
  x = list(range_n_clusters)
  y = list(inertia.values())
  kneedle = KneeLocator(x, y, S=1.0, curve="convex", direction="decreasing")
  best_inertia = inertia[kneedle.elbow]
  best_cluster = kneedle.elbow
  res_data = {
      'score': best_inertia,
      'cluster': best_cluster,
  }
  plot_select_n_cluster(best_inertia, best_cluster, y, range_n_clusters,
                        title = f'Evolución de la varianza intra-cluster total {kwards["name_model"]}',
                        y_label = 'Intra-cluster (inertia)')
  return res_data

def silhouette_select_cluster(model, clusters, data, **kwards):
  """Metodo silhouette"""
  range_n_clusters = range(clusters[0], clusters[1])
  valores_medios_silhouette = {}
  for k in range_n_clusters:
    model.n_clusters = k 
    model.fit(data)
    y_predict = model.predict(data)
    silhouette_avg = silhouette_score(data, y_predict)
    valores_medios_silhouette[k] = silhouette_avg
  
  x = list(range_n_clusters)
  y = list(valores_medios_silhouette.values())
  kneedle = KneeLocator(x, y, S=1.0, curve="concave", direction="increasing")

  best_score = valores_medios_silhouette[kneedle.elbow]
  best_cluster = kneedle.elbow

  res_data = {
      'score': best_score,
      'cluster': best_cluster,
  }
  plot_select_n_cluster(best_score, best_cluster, y, range_n_clusters,
                        title = f'Evolución de media de los índices silhouette {kwards["name_model"]}',
                        y_label = 'Media índices silhouette')
  
  return best_cluster, best_score




#model = KMeans(init='k-means++', max_iter=300, random_state=12354, n_init=10)
#_ = elbow(model, (2,30), cluster_df, name_model = 'Kmeans')