class Tetrader:
    def __init__(self, line: float):
        if not self.validation(line):
            raise Exception('Это не может быть тетрайдером')
        
        self.line = line
    
    @staticmethod
    # Тут выяснилось, что isinstance(True, (int, float)) вернет True. В каких случаях имеет смысл использовать
    # isinstance() или type() in (кортеж объектов)?
    def validation(line: float) -> bool:
        return line >= 1 and type(line) in (int, float)
    
    def square(self) -> float:
        return round(3**0.5 * self.line**2, 2)
    
    def volume(self) -> float:
        return round((self.line**3 * 2**0.2) / 12, 2)


tet = Tetrader(100)
print(tet.square())
print(tet.volume())

# 17320.51
# 95724.86
