our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_routes = our_routes.intersection(competitor_routes)  # routes provided by both airlines
print(f"Routes in both provided sets: {same_routes}")

unique_routes = our_routes.difference(competitor_routes) # routes provided by our airline
print(f"Routes provided unique to our airline: {unique_routes}")

unique_routes_comp = competitor_routes.difference(our_routes) # routes provided by competitor airline
print(f"Routes provided unique to competitor airline: {unique_routes_comp}")

provided_routes = our_routes.symmetric_difference(competitor_routes) # routes provided by one airline, but not both airlines
print(f"Routes provided by one airline, but not both: {provided_routes}")