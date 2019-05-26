# Python pygame OOP project
simple game made with pygame

Celem projektu jest napisanie prostej gry w j ˛ezyku Python (z wykorzystaniem biblioteki pygame) z elementami algorytmiki.
• Gotowy program należy zaprezentować osobiście na konsultacjach oraz przesłać na platform ˛e Moodle.
• Wymagana jest bezwzgl ˛edna znajomość prezentowanego kodu źródłowego tzn.
trzeba umieć odpowiedzieć na pytanie: "Co to jest i do czego służy?".
• Program powinien działać poprawnie wykonuj ˛ac zamierzone przez programist ˛e
zadania.
• Program musi wykorzystywać paradygmat programowania obiektowego.
W tym:
– należy tworzyć własne klasy;
– wykorzystywać dziedziczenie (chociażby po klasach wbudowanych).
• Ponadto należy zadbać o:
– poprawne rozmieszczenie kodu w pliku źródłowym (lub plikach);
– czytelność kodu i konsekwentnie stosować styl nazewniczy;
– ogóln ˛a estetyk ˛e kodu i działanie programu.
• Możliwe s ˛a dwa typy projektu nr 1:
– Projekt typ I - gra napisana w j ˛ezyku Python 3.x z wykorzystaniem biblioteki pygame ilustruj ˛aca sortowanie b ˛abelkowe. Po uruchomianiu programu
gracz powinien ujrzeć ci ˛ag przypadkowo ułożonych liczb lub liter1
, które należy posortować w kolejności rosn ˛acej (lub odwrotnie) wykorzystuj ˛ac algorytm sortowania b ˛abelkowgo. Gracz powinien mieć możliwość przestawiania kolejności wskazanej pary s ˛asiednich elementów (tych które s ˛a w jakiś
sposób znaczone np. uj ˛etych w ramk ˛e). Jeżeli gracz dokona przestawienia
elementów w nieodpowiedniej kolejności, gra powinna zaczynać si ˛e od nowa (od pocz ˛atkowego ustawienia elementów). Gra powinna kończyć si ˛e gdy
1Mog ˛a to być również inne obiekty, które można sortować.
1
wszystkie elementy b ˛ed ˛a uporz ˛adkowane zgodnie z krokami wynikaj ˛acymi
z algorytmu sortowania b ˛abelkowgo.
Program może zawierać nast ˛epuj ˛ace klasy:
∗ Letter (lub Number) - klasa reprezentuj ˛aca obiekt litery (oparta na klasie pygame.sprite.Sprite), z takimi metodami jak __init__(), run(),
draw() i update();
∗ Frame - klasa reprezentuj ˛aca obiekt ramki;
∗ Button - klasa reprezentuj ˛aca obiekt przycisku;
∗ Game - główna klasa odpowiadaj ˛aca za cał ˛a rozgrywk ˛e z takimi metodami jak __init__(), draw(), update(), metod ˛a obsługuj ˛ac ˛a zdarzenia
oraz metod ˛a wyznaczaj ˛ac ˛a prawidłow ˛a kolejność ruchów (sortowania
liter);
∗ Text - klasa odpowiadaj ˛ac za obiekty tekstu wyświetlane na ekranie.
