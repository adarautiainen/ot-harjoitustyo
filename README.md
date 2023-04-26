# Budjetointisovellus

Sovelluksen avulla käyttäjät voivat tehdä omia budjetteja. Tämä sovellus on tehty Helsingin yliopiston kurssille Ohjelmistotekniikka. 

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/adarautiainen/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/arkkitehtuuri.md)
- [Release vko 5](https://github.com/adarautiainen/ot-harjoitustyo/releases/tag/viikko5)

## Asennus
- Riippuvuuksien asentaminen komennolla: ```poetry install```
- Alustustoimenpiteet komennolla: ```poetry run invoke build```

## Komennot
- Ohjelman suorittaminen onnistuu komennolla: ```poetry run invoke start```
- Ohjelman testien suorittaminen onnistuu komennolla: ```poetry run invoke test```
- Ohjelman testikattavuusraportin saa komennolla: ```poetry run invoke coverage-report```
- Tiedoston .pylintrc tarkistusten suorittaminen onnistuu komennolla: ```poetry run invoke lint```
