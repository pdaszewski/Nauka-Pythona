#Przykład pobierania automatycznego strony internetowej
import urllib.request
sock = urllib.request.urlopen("https://geoportal360.pl/map/#l:52.8887,21.39935,17;p:MTQxMTA3XzQuMDAwMS4xNjIvMw==")  #(2)
htmlSource = sock.read()                             #(3)
sock.close()                                         #(4)

#Wynikiem jest kod HTML strony - czyli wynik strony - który możemy zapisać do pliku, lub dalej przetworzyć
#Tak budowane było pobieranie danych z geoportalu360.pl - przykład.
print(htmlSource)

