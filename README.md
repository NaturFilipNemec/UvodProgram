Úvod do programování – úkol č. 2

Program by měl přečíst csv dokument s názvem vstup.csv. Následně by měl vypočítat roční týdenní průtok řeky a zapsat do dokumentů vystup_7dni.csv pro týdny a vystup_rok.csv pro roky. Navíc by měl určit největší a nejmenší denní průtok a vypsat chybějící a špatné vstupy. Sloupce ve vstupních datech by měl oddělovat ‘ , ‘ . 
Program nejprve pomocí try zkontroluje zda soubor existuje. Následně pomocí příkazů z knihovny csv načte soubor, vytvoří dva soubory a připraví na čtení a zapisovaní. V reader nejprve zkontroluje korektní vstupy. Pokud průtok není číslo oznámí to uživateli a zapíše špatné datum do seznamus chybami a tento řádek přeskočí. Proměnná aktualni_datum slouží ke kontrole děr v souboru, prochází postupně každý den. Řádek 49 až 55 určení minima a maxima. 61 řádek while cyklus pro řešení děr a vypočet průměru týdnů. Od řádku 81 až po 98 řešení bez chybějících datumu pro týdny. Pro rok řešeno úplně stejně jako pro týdny. Řádek 149 řeší a zapisuje špatné průtoky. Pro práci s datumy jsem používal z knihovny datetime příkazy  datime a  timedelta a nasledné porovnaní pouze roků (např. if aktualni_rok.year == aktualni_datum.year)./
Proměnné:
tyden_list – sem se zapisují jednotlivé průtoky pro vypočet průměru, po konci týden se vyčistí /
tyden_celkem – proměna pro výpočet průměru za týden/
rok_list – sem se zapisují jednotlivé průtoky pro výpočet průměru za rok, po konci roku se list vyčistí/
rok_celkem – proměnná pro výpočet průměru za rok /
aktualni_rok , aktualni_tyden – slouží pro pomoc při zápisu hodnot do seznamu (detekce děr)/=
