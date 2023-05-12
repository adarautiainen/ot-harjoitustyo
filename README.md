# Budjetointisovellus

Sovelluksen avulla käyttäjät voivat tehdä omia budjetteja. Tämä sovellus on tehty Helsingin yliopiston kurssille Ohjelmistotekniikka. 

## Dokumentaatio
- [Käyttöohje](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/testaus.md)
- [Changelog](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/changelog.md)
- [Tuntikirjanpito](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/tuntikirjanpito.md)
- [Lopullinen release]

## Asennus
- Riippuvuuksien asentaminen komennolla: ```poetry install```
- Alustustoimenpiteet komennolla: ```poetry run invoke build```

## Komennot
- Ohjelman suorittaminen onnistuu komennolla: ```poetry run invoke start```
- Ohjelman testien suorittaminen onnistuu komennolla: ```poetry run invoke test```
- Ohjelman testikattavuusraportin saa komennolla: ```poetry run invoke coverage-report```
- Tiedoston .pylintrc tarkistusten suorittaminen onnistuu komennolla: ```poetry run invoke lint```
