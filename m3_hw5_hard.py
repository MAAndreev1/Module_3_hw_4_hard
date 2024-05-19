data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(args):
    lens = 0
    if isinstance(args, list) is True:
        for i in args:
            lens += calculate_structure_sum(i)
    if isinstance(args, tuple) is True or isinstance(args, set) is True:
        lens += calculate_structure_sum(list(args))
    if isinstance(args, dict) is True:
        lens += calculate_structure_sum(list(args.items()))
    if isinstance(args, str) is True:
        lens += len(args)
    if isinstance(args, int) is True:
        lens += args
    return lens


result = calculate_structure_sum(data_structure)
print(result)
