import networkx as nx
import heapq


class DijGraph(nx.Graph):
    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                break
            for _, neighbor, weight in self.edges.data('weight', nbunch=[current_vertex]):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

def main():
    # Граф головних автошляхів України
    G = DijGraph()
    G.graph['name'] = 'Ukrain_Roads_Graph'
    G.add_nodes_from(['Lviv', 'Kyiv', 'Dnipro', 'Kharkiv', 'Odessa', 'Uman'])
    G.add_edges_from([('Lviv', 'Kyiv'), ('Kyiv', 'Kharkiv'), ('Kyiv', 'Dnipro'),
                    ('Kharkiv', 'Dnipro'), ('Dnipro', 'Odessa'), ('Kyiv', 'Uman'),
                    ('Uman', 'Odessa'), ('Uman', 'Lviv'), ('Uman', 'Dnipro') 
                    ])
    G['Lviv']['Kyiv']['weight'] = 540
    G['Kyiv']['Kharkiv']['weight'] = 481
    G['Kyiv']['Dnipro']['weight'] = 453
    G['Kharkiv']['Dnipro']['weight'] = 221
    G['Dnipro']['Odessa']['weight'] = 480
    G['Kyiv']['Uman']['weight'] = 211
    G['Uman']['Odessa']['weight'] = 271
    G['Uman']['Lviv']['weight'] = 530
    G['Uman']['Dnipro']['weight'] = 417

    vertex = 'Kyiv'
    shortest_distances = G.dijkstra(vertex)

    print(f'\nНайменша відстань між вершиною {vertex} та іншими:')
    print('| До якого городу | Найкоротший шлях |')
    print('|-----------------|------------------|')
    for name, dist in shortest_distances.items():
        print(f'| {name:15} | {dist:^16} |')

if __name__ == '__main__':
    main()