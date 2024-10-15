import folium
import osmnx as ox

import matplotlib.pyplot as plt

query = "Chuuouku,Saitama,Saitama,Japan"

G = ox.graph_from_place(query)
# G = ox.graph_from_place(query, network_type="drive")

fmap = ox.plot_graph_folium(G)
fmap.save(outfile="road_network.html")

# ox.plot_graph(G)
# plt.show()

# opts = {"node_size": 5, "bgcolor": "white", "node_color": "blue", "edge_color": "blue"}
# ox.plot_graph(G, show=False, save=True, filepath="road_network.png", **opts)

# 道路グラフネットワークの各ノード・エッジ取得・CSV出力
nodes, edges = ox.graph_to_gdfs(G)
nodes.to_csv("road_network_nodes.csv")
edges.to_csv("road_network_edges.csv")

# 最短経路探索
start_point = (35.891386126877585, 139.62379198653255)
start_node = ox.distance.nearest_nodes(G, start_point[1], start_point[0])
end_point = (35.892481023357426, 139.6148963212973)
end_node = ox.distance.nearest_nodes(G, end_point[1], end_point[0])

shortest_path = ox.shortest_path(G, start_node, end_node)

# # 最短経路探索結果の可視化
# new_fmap = ox.plot_route_folium(G, shortest_path, route_map=fmap, color="red")
# folium.Marker(location=start_point, tooltip="start").add_to(new_fmap)
# folium.Marker(location=end_point, tooltip="end").add_to(new_fmap)
# new_fmap.save(outfile="shortest_path_road_network.html")

outfile = "shortest_path_road_network.png"
opts = {"node_size": 5, "bgcolor": "white", "node_color": "blue", "edge_color": "blue"}
ox.plot_graph_route(G, shortest_path, show=False, save=True, filepath=outfile, **opts)
