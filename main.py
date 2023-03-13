from collections import defaultdict


class Flight:
    def __init__(self, origin, destination, fare):
        self.origin = origin
        self.destination = destination
        self.fare = fare


list_of_flights = [Flight("EDH", "BCN", 183),
                   Flight("EDH", "PAR", 120),
                   Flight("EDH", "SIN", 578),
                   Flight("PAR", "EDH", 120),
                   Flight("BCN", "EDH", 183),
                   Flight("SIN", "EDH", 578),
                   Flight("BCN", "MAR", 250),
                   Flight("BCN", "HEL", 200),
                   Flight("HEL", "BCN", 200),
                   Flight("HEL", "KYV", 147),
                   Flight("KYV", "HEL", 147),
                   Flight("MAR", "BCN", 250)]


def create_map_graph_from_list(list_to_transform):
    map_graph = defaultdict(dict)
    for flight in list_to_transform:
        origin = flight.origin
        destination = flight.destination
        fare = flight.fare
        map_graph[origin][destination] = fare
    return map_graph


def find_eligible_flights_with_given_budget(start, budget, flights_list):
    graph = create_map_graph_from_list(flights_list)
    fares = {node: float("inf") for node in graph}
    fares[start] = 0

    visited = []
    while len(visited) < len(graph):

        current_city = min((node for node in graph if node not in visited), key=fares.get)
        visited.append(current_city)

        for (destination, fare) in graph[current_city].items():
            fare_to_current_city = fares[current_city]
            total_fare_to_next_destination = fare_to_current_city + fare

            if total_fare_to_next_node < fares[destination]:
                fares[destination] = total_fare_to_next_destination
    eligible_destinations = [destination for destination, fare in fares.items() if
                             fare <= budget and destination != start]
    return eligible_destinations


print(f'Eligible flights: {find_eligible_flights_with_given_budget("EDH", 500, list_of_flights)}')
#   >>> Eligible flights: ['PAR', 'BCN', 'HEL', 'MAR']
