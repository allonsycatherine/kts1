from math import factorial as fac
__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number > 1:
        if (fac(number - 1)+1)%number == 0:
            return True
    else:
        return False

