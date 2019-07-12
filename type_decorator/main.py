import functools

def typecheck(*inst: tuple):
    def wrapper(item):
        @functools.wraps(item)
        def deep(*args: tuple, **kwargs: dict):
            for idx, name in enumerate(inst):
                if name != type(args[idx]):
                    print(f'In function "{item.__name__}" type of '
                    f'"{item.__code__.co_varnames[idx]}" is not matching with '
                    f'decorated type "{inst[idx]}"')
            return item(*args, **kwargs)
        return deep
    return wrapper

@typecheck(int, tuple)
def set1(number: int, tp: tuple):
    return number, tp


@typecheck(int, tuple)
def set2(aa: int, bb: tuple):
    return aa, bb


print(set1([5,6], (1,2)))
print(set2(5, [1,2]))
#print(typecheck(5, (1,2)))
