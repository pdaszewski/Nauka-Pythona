#Wykonywanie prostych operacji matematycznych z formatowaniem wprowadzanych danych
#Formatowanie pozwala określać jaki rodzaj zmiennej mamy do dyspozycji.
print("Kalkulator:")
print()
print("Podaj wartość A: ")
a = input() #Tu wprowadzana wartość będzie od nowej linii
b = input(f"Podaj wartość B: ") #Tu wprowadzana wartość będzie w tej samej linii
c = int(a)*int(b)
print("Wynik mnożenia: ",c)
