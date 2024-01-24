def has_duplicate(self,temp: str, s: str) -> bool:
        char_list = [0]*300
        for char in s:
            if char_list[ord(char)] > 0:  
                return True
            char_list[ord(char)] += 1

        for char in temp:
            if char_list[ord(char)] > 0:
                return True
        return False
