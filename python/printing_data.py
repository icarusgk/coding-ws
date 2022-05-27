from pprint import pprint, PrettyPrinter

# It is used with more complex data structures
dogs = [
    {
        "name": "Max",
        "breed": "Yorkshire",
        "age": 1,
        "owners": ["Susan, Camila, Paul"]
    },
    {
        "name": "Duke",
        "breed": "Bulldog",
        "age": 4,
        "owners": ["Thomas, David, Lucia"]
    },
    {
        "name": "Bella",
        "breed": "Poodle",
        "age": 2,
        "owners": ["Katharina, Arthur"]
    }
]

pprint(dogs, sort_dicts=False, indent=2)


# Setting a default config
pp = PrettyPrinter(indent=4, depth=2, sort_dicts=False)

pp.pprint(dogs)