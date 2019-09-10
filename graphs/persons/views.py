# path = graph.run(
#     "MATCH (b1:Person {name: 'Jim'}),(b2:Person {name: 'superman'}), p = shortestPath((b1)-[*..15]-(b2)) RETURN p").to_ndarray()