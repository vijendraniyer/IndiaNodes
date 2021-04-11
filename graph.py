import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

head = []
Nodes = nx.Graph()
colour_map = []

pd.set_option("display.max_rows", None, "display.max_columns", None)
df_nodes = pd.read_excel('graph.xlsx', sheet_name='Nodes')
df_edges = pd.read_excel('graph.xlsx', sheet_name='Edges')

for col in range(len(df_nodes.iloc[0, :])):
    nodes = df_nodes.iloc[:, col]
    [Nodes.add_node(nodes[i].strip()) for i in range(len(nodes)) if not pd.isna(nodes[i])]

for index, row in df_edges.iterrows():
    head = []
    for i in range(len(row)):
        if not pd.isna(row[i]):
            head.append(row[i])
    for line in range(len(head)):
        Nodes.add_edges_from([(head[0].strip(), head[line].strip())])

for node in Nodes:
    if df_nodes[df_nodes['States'] == node].index.values:
        colour_map.append('green')
    elif df_nodes[df_nodes['UTs'] == node].index.values:
        colour_map.append('yellow')
    elif df_nodes[df_nodes['Bordering Countries'] == node].index.values:
        colour_map.append('brown')
    else:
        colour_map.append('blue')

nx.draw_shell(Nodes, with_labels=True, node_color=colour_map, edge_color='black')
plt.show()
