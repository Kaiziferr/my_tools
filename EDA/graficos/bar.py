sns.set(style="darkgrid")

def plot_bar(data, palette, figsize_x=8,figsize_y=8,fontsize=15, **kwards)->None:
  """Grafica un diagrama de barras con multiples caracteristicas"""
  v = kwards
  fig, ax = plt.subplots(figsize = (figsize_x, figsize_y))
  fig.suptitle(f'Diagrama de barras {v["title"]}', fontsize=fontsize)
  sns.barplot(x=v['ejeX'], y=v['ejey'], data=data, ci=None, ax=ax, palette=palette)
  ax.set_ylabel(v['ejey'], size = 12)
  ax.set_xlabel(v['ejeX'], size=fontsize-3)
  ax.set_xticklabels(ax.get_xticklabels(),fontsize = fontsize-3)
  for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x()+p.get_width()/2., height + 1,height, ha="center") 

palette = {
    'Lunes': '#ff6602ff',
    'Martes': '#0f7175ff',
    'Miercoles': '#c65dc9ff',
    'Jueves': "#a8329b",
    'Viernes': "#1d15bd",
    'Sabado': "#bd4215"
}

#plot_bar(data, palette, ejeX='dia',ejey='venta_refresco',title='Venta refrescos')
