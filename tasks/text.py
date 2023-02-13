from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    if re.fullmatch(r'\s+', text):
        return None, None
    else:
        text = re.sub(r'\s+', ' ', text)
        if len(text) > 0:
            txt = text.split()
            shortest = [txt[0]]
            longest = [txt[0]]
            for i in txt[1:]:
                if len(i) < len(shortest[0]):
                    shortest[0] = i
                elif len(i) == len(shortest[0]):
                    shortest.append(i)
                elif len(i) > len(longest[0]):  
                    longest[0] = i
                elif len(i) == len(longest[0]):  
                    longest.append(i)
            if len(shortest) == 1 and len(longest) == 1:
                return shortest[0], longest[0]
            elif len(shortest) == 1 and len(longest) != 1:
                return shortest[0], None
            elif len(shortest) != 1 and len(longest) == 1:
                return None, longest[0]
        else:
            return None, None
print(find_shortest_longest_word(''))