__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    even = [i for i in arr if i%2 == 0]
    odd = [i for i in arr if i%2 != 0]
    if len(even) and len(odd) > 0:
        return sum(even)/sum(odd)    
    else:
        return 0
