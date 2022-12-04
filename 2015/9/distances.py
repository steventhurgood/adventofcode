import os
from collections import defaultdict
from typing import Dict, List, Sequence, Set, Tuple

from absl import app, flags, logging

from dataclasses import dataclass

FLAGS = flags.FLAGS

default_filename = os.path.join(
    os.path.dirname(__file__), "data/data.txt")

flags.DEFINE_string('input', default_filename, 'Input filename')


class NoValidPathException(Exception):
    pass


@dataclass
class Distances:
    edges: Dict[str, List]
    cities: Set[str]

    def __init__(self):
        self.edges = defaultdict(list)
        self.cities = set()

    def process(self, input: Sequence[str]):
        for line in input:
            # London to Dublin = 464
            parts = line.split()
            from_city: str = parts[0]
            to_city: str = parts[2]
            distance: int = int(parts[4])
            self.cities.add(from_city)
            self.cities.add(to_city)

            self.edges[from_city].append((distance, to_city))
            self.edges[from_city].sort()
            self.edges[to_city].append((distance, from_city))
            self.edges[to_city].sort()

    def find_all_routes(self) -> Sequence[Tuple[int, Sequence[Tuple[int, str, str]]]]:
        # enumerate all possible routes
        # if all cities are already visited:
        #   return []
        # for each starting city:
        #   for each route from that city:
        #     if all candidate cities are already visited:
        #       raise an exception
        #     recursively find all routes
        #     if there was an exception, move on to the next city

        all_routes = []
        for from_city in self.cities:
            for route in self.recursively_walk_cities(from_city):
                distance = sum([r[0] for r in route])
                all_routes.append((distance, route))
        all_routes.sort()
        return all_routes

    def recursively_walk_cities(self, from_city: str, visited_cities: Set[str] = None) -> Sequence[Tuple[int, str, str]]:
        if visited_cities is None:
            visited_cities = set([from_city])

        if len(visited_cities) == len(self.cities):
            # we have visited all cities
            return []

        candidate_edges = []
        for distance, to_city in self.edges[from_city]:
            if to_city in visited_cities:
                continue
            candidate_edges.append((distance, to_city))

        if len(candidate_edges) == 0:
            # there are no candidate edges, but we still have unvisited cities
            raise NoValidPathException()

        # recursively walk each candidate edge.

        found_valid_route = False
        valid_routes = []
        for distance, to_city in candidate_edges:
            new_visited_cities = visited_cities.copy()
            new_visited_cities.add(to_city)
            try:
                routes = self.recursively_walk_cities(
                    to_city, new_visited_cities)
            except NoValidPathException:
                continue
            found_valid_route = True
            if len(routes) == 0:
                valid_routes.append([(distance, from_city, to_city)])

            for route in routes:
                valid_routes.append([(distance, from_city, to_city)] + route)

        if len(valid_routes) == 0:
            raise NoValidPathException()

        return valid_routes

    def find_shortest_graph(self) -> int:
        candidate_edges: List[(Tuple[int, str, str])] = []

        # initial setup
        for from_city, edges in self.edges.items():
            for distance, to_city in edges:
                candidate_edges.append((distance, from_city, to_city))
        candidate_edges.sort()
        distance, from_city, to_city = candidate_edges[0]

        logging.info(f'Starting cities: {from_city} - {to_city} ({distance}')

        cities_visited: Set[str] = set([from_city, to_city])
        distance_travelled = distance

        while len(cities_visited) < len(self.cities):
            # find the next shortest route
            candidate_edges = []
            for from_city in cities_visited:
                for distance, to_city in self.edges[from_city]:
                    if to_city not in cities_visited:
                        candidate_edges.append((distance, from_city, to_city))
            if len(candidate_edges) == 0:
                # no candidate edges?
                logging.info(
                    f'No more candidate edges after {len(cities_visited)} have been visited')
                return distance_travelled
            candidate_edges.sort()
            distance, from_city, to_city = candidate_edges[0]
            distance_travelled += distance
            cities_visited.add(to_city)
            logging.info(
                f'Travelling from {from_city} to {to_city} ({distance}')

        return distance_travelled


def main(argv):
    d = Distances()
    with open(FLAGS.input) as f:
        d.process(f)

    routes = d.find_all_routes()

    for stop in routes[0][1]:
        print(stop)
    print(f'Shortest route distance: {routes[0][0]}')

    for stop in routes[-1][1]:
        print(stop)
    print(f'Longest route distance: {routes[-1][0]}')


if __name__ == '__main__':
    app.run(main)
