# Projekt z Języków Symbolicznych

### Miłosz Okruta (GL2)

___

## Temat projektu

Projekt jest implementacją automatu z napojami w języku Python. W automacie można zakupić napoje, które się w nim
obecnie znajdują. Monety, które automat wydaje, są monetami, które poprzednio zostały do niego wrzucone. Interakcja z
automatem polega na wpisaniu numeru napoju, który mamy zamiar zakupić oraz na wrzuceniu monet do automatu. Dane można
wprowadzać, naciskając myszką wyświetlone przyciski.

## Funkcjonalność

1. Automat początkowo nie zawiera w sobie monet — zakup pierwszego produktu musi być tylko za odliczoną kwotę.
2. Automat wyświetla odpowiednie komunikaty, które zmieniają/aktualizują się zawsze po wrzuceniu monety, wpisaniu
   kolejnej cyfry numeru napoju oraz po przerwaniu transakcji.
3. Automat wydaje resztę z monet wrzuconych w poprzednich transakcjach.

___

## Uruchomienie projektu

Aby uruchomić projekt, należy wpisać w konsoli:

```shell
$ python3 ./app.py
```

Aby uruchomić testy, należy wpisać w konsoli:

```shell
$ python3 ./test.py
```

___

## Klasy i samodzielne funkcje zawarte w projekcie

### Klasa [Machine](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Machine.py#L4)

Odpowiada za inicjalizację automatu, przechowuje obiekty typu ItemStorage oraz CoinStorage odpowiadające za
przechowywanie produktów i monet w automacie, oraz za rozpoczęcie transakcji w automacie.

### Klasa [Transaction](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Transaction.py#L6)

Klasa reprezentująca transakcję odbywającą się w automacie. Posiada ona informacje o wrzuconych monetach i wybranym
produkcie, dokonuje zakupu produktu i wydaje resztę.

### Funkcja [get_machine](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/machine.py#L7)

Służy do uzyskania obecnej instancji klasy Machine.

### Funkcja [get_transaction](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/machine.py#L12)

Służy do uzyskania obecnej instancji klasy Transaction.

### Funkcja [reset_machine](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/machine.py#L17)

Służy do zresetowania używanych instancji Machine i Transaction.

### Funkcja [main w pliku app.py](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/app.py#L5)

Służy do uruchomienia projektu.

### Funkcja [main w pliku test.py](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/test.py#L3)

Służy do uruchomienia testów.

## Moduł Entity

### Funkcja [get_valid_coin_values](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/Coin.py#L4)

Funkcja zwracająca listę wartości, które moneta może posiadać.

### Klasa [Coin](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/Coin.py#L9)

Klasa reprezentuje każdą monetę, która może zostać wrzucona do automatu. Podczas tworzenia nowego jej obiektu, sprawdza,
czy podana wartość monety jest poprawna, w przeciwnym wypadu rzuca wyjątek InvalidCoinValueException.

### Klasa [CoinStorage](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/CoinStorage.py#L7)

Klasa przechowująca monety, informująca o wartości wszystkich monet w niej zawartych oraz obsługująca ich wypłatę.

### Klasa [ItemStorage](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/ItemStorage.py#L4)

Klasa przechowująca informacje o zawartych w niej produktach oraz ich cenach. Podczas tworzenia nowego jej obiektu,
generuje losowe ceny produktów. Obsługuje wydawanie produktów.

## Moduł Exception

### Klasa [InvalidCoinValueException](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/InvalidCoinValueException.py#L1)

Wyjątek rzucany w momencie, gdy wartość monety jest niepoprawna.

### Klasa [InvalidItemIdException](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/InvalidItemIdException.py#L1)

Wyjątek rzucany w momencie, gdy numer produktu jest niepoprawny (nie jest w przedziale <30,50>).

### Klasa [NoItemInTheMachineException](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/NoItemInTheMachineException.py#L1)

Wyjątek rzucany w momencie, gdy dochodzi do próby zakupu produktu, którego nie ma w maszynie.

### Klasa [NotEnoughCoinsToWithdrawException](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/NotEnoughCoinsToWithdrawException.py#L1)

Wyjątek rzucany w momencie, gdy podczas próby wydania reszty zabraknie monet.

### Klasa [OnlyCalculatedAmountException](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/OnlyCalculatedAmountException.py#L1)

Wyjątek rzucany w momencie, gdy zakup produktu za wrzuconą kwotę jest niemożliwy, ponieważ automat nie posiada monet do
wydania obliczonej reszty.

### Klasa [TooSmallMoneyAmountException](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/TooSmallMoneyAmountException.py#L1)

Wyjątek rzucany w momencie, gdy kwota wrzucona do automatu jest niewystarczająca do zakupu produktu.

## Moduł Presentation

### Funkcja [handle](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Presentation/Handler.py#L4)

Główna funkcja modułu Presentation. Odpowiada za obsługę wyświetlania GUI.

### Plik [InsertCoins](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Presentation/InsertCoins.py)

Plik zawierający funkcje obsługujące część GUI związaną z wrzucaniem i wypłatą monet.

### Plik [Messages](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Presentation/Messages.py)

Plik zawierający funkcje obsługujące część GUI związaną z wyświetlaniem, dodawaniem i czyszczeniem komunikatów.

### Plik [SelectProduct](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Presentation/SelectProduct.py)

Plik zawierający funkcje obsługujące część GUI związaną z wybraniem, zakupem produktu oraz przerwaniem transakcji.

## Moduł Utils

### Funkcja [give_change](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Utils/CoinUtils.py#L5)

Oblicza oraz zwraca resztę na podstawie listy dostępnych monet, typów monet oraz kwoty, którą z tych monet należy wydać.

### Funkcja [coins_to_string](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Utils/CoinUtils.py#L29)

Konwertuje listę monet w czytelny tekst.

### Funkcja [render_button](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Utils/PresentationUtils.py#L6)

Wyświetla przycisk w GUI.

___

## Testy

### Klasa [TestCheckProductPrice](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/tests/Functional/TestCheckProductPrice.py#L5) (1)

Test polegający na sprawdzeniu ceny jednego towaru. Oczekuje komunikatu o cenie.

### Klasa [TestInsertEqualAmountOfMoney](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/tests/Functional/TestInsertEqualAmountOfMoney.py#L6) (2)

Test polegający na wrzuceniu kwoty równej cenie wybranego produktu. Oczekuje zakupu towaru oraz braku wydanej reszty.

### Klasa [TestInsertBiggerAmountOfMoney](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/tests/Functional/TestInsertBiggerAmountOfMoney.py#L6) (3)

Test polegający na wrzuceniu większej kwoty od ceny wybranego produktu. Oczekuje zakupu towaru oraz wydanej reszty.

### Klasa [TestBuyAllProductsOfOneType](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/tests/Functional/TestBuyAllProductsOfOneType.py#L6) (4)

Test polegający na wykupieniu całego asortymentu danego towaru i próbie zakupu po wyczerpaniu towaru. Oczekuje
komunikatu o braku towaru.

### Klasa [TestCheckInvalidProductIds](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/tests/Functional/TestCheckInvalidProductIds.py#L5) (5)

Test polegający na sprawdzeniu ceny towaru o nieprawidłowym numerze (<30 oraz >50). Oczekuje komunikatu o niepoprawnym
numerze towaru.

### Klasa [TestAbortTransaction](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/tests/Functional/TestAbortTransaction.py#L5) (6)

Test polegający na wrzuceniu kilku monet i przerwaniu transakcji. Oczekuje zwrotu monet.

### Klasa [TestAddMoreMoneyToBuyProduct](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/tests/Functional/TestAddMoreMoneyToBuyProduct.py#L6) (7)

Test polegający na wrzuceniu za małej kwoty, wybraniu poprawnego numeru produktu i wrzuceniu reszty monet do odliczonej
kwoty. Oczekuje braku reszty i zakupu produktu.

### Test nr 8 z README.md

Test polegający na zakupie towaru jedynie przy pomocy monety 1gr jest zawarty m.in. w
teście [TestInsertEqualAmountOfMoney](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/tests/Functional/TestInsertEqualAmountOfMoney.py#L6)
— zakup towarów w testach jest dokonywany, wrzucając określoną ilość razy monetę 1gr.

___

## Istotne fragmenty kodu

### Wyrażenia lambda

1. [Link 1](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Presentation/InsertCoins.py#L49)
2. [Link 2](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Presentation/SelectProduct.py#L80)
3. [Link 3](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Presentation/SelectProduct.py#L84)

### List/dictionary comprehensions

1. [Link 1](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/CoinStorage.py#L16)
2. [Link 2](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/ItemStorage.py#L13)
3. [Link 3](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/ItemStorage.py#L17)

### Klasy

1. [Link 1](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/Coin.py)
2. [Link 2](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/CoinStorage.py)
3. [Link 3](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Entity/ItemStorage.py)

### Wyjątki

1. [Link 1](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/InvalidCoinValueException.py#L1)
2. [Link 2](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/InvalidItemIdException.py#L1)
3. [Link 3](https://github.com/pk-mo/Projekt-JS-nr-3/blob/master/src/Exception/NoItemInTheMachineException.py#L1)

### Moduły

1. [Link 1](https://github.com/pk-mo/Projekt-JS-nr-3/tree/master/src/Entity)
2. [Link 2](https://github.com/pk-mo/Projekt-JS-nr-3/tree/master/src/Exception)
3. [Link 3](https://github.com/pk-mo/Projekt-JS-nr-3/tree/master/src/Presentation)