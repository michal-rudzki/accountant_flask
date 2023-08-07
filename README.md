# accountant_flask
Accountant web app in flask

### Accountant
Bazując na aplikacji do zarządzania firmą, stwórz jej webowy odpowiednik.

Na stronie głównej wyświetl informację na temat stanu konta, magazynu oraz trzy formularze: zakup, sprzedaż, zmiana salda.

## Requirements:
- Formularz:
    - _zakupu_ powinien zawierać trzy pola: **nazwa** produktu, **cena** i **ilość**
    - _sprzedaży_ powinien zawierać dwa pola: **nazwa** produktu i **ilość**
    - _zmiany salda_ powinien zawierać jedno pole: **wartość zmiany salda**

Dodatkowo utwórz drugą podstronę zawierającą historię wykonanych operacji. Podstrona powinna być dostępna pod URL "/historia/" oraz "/historia/<start>/<koniec>"

W przypadku "/historia/" na stronie ma się pojawić cała dostępna historia.

W przypadku "/historia/<start>/<koniec>" zależnie od podanych wartości w <start> i <koniec>, mają się pojawić wskazane linie, np. od 3 do 12. W przypadku podania złego (lub nieistniejącego zakresu indeksów), program poinformuje o tym użytkownika i wyświetli możliwy do wybrania zakres historii.

Zadanie wciąż powinno korzystać z plików do przechowywania stanu konta, magazynu i historii.