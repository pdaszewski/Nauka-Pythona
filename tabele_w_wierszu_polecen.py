#Nauka formatowania wartości i tekstów - generowanie tabele na ekranie - aplikacja konsolowa

szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| %6.3f | %-16s | %10s |" % (9.58, "Usain Bolt", "16.08.2009")) #tu inaczej formatuję wyrównanie 2 wartości (- wyrównuje do lewej).
print("| %6.3f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %6.3f | %16s | %10s |" % (9.74, "Asafa Powell", "02.09.2008"))
print("-" * szer)

print()

szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {0:6.3f} | {1:16s} | {2:10s} |" .format(9.74, "Asafa Powell", "02.09.2008"))
print("-" * szer)

input("\nAby zakończyć program wciśnij klawisz Enter.")
