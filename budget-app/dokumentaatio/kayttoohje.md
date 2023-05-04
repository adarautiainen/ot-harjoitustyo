# Käyttöohje

Lataa viimeisin release projektista [täältä](https://github.com/adarautiainen/ot-harjoitustyo/releases).


## Käynnistäminen

Asenna riippuvuudet komennolla: ```poetry install```

Tee alustustoimenpiteet komennolla: ```poetry run invoke build```

Ohjelman voi käynnistää komennolla: ```poetry run invoke start```


## Kirjautuminen

Kun sovellus käynnistetään se avautuu kirjautumisnäkymään. Kirjautuminen onnistuu jo luodulla käyttäjätunnuksella ja salasanalla. Syötä käyttäjätunnus
ja salasana kenttiin ja paina "Login" painiketta.

## Uuden käyttäjän luominen

Uuden käyttäjän pääsee luomaan "Create user" painikkeella. Syötä kenttiin käyttäjätunnus ja salasana. Jos käyttäjätunnus on jo olemassa sovellus ilmoittaa tästä. Kun käyttäjä on onnistuneesti luotu siirrytään budjettinäkymään. 

## Budjettien luominen

Uuden budjetin voi luoda syöttämällä kenttiin kuukauden, tulot ja menot ja painamalla painiketta "Create". Sovellus ilmoittaa jos käyttäjän syöttämät arvot eivät kelpaa. Jo luotujen budjettien poistaminen onnistuu "Delete" painikkeella.
Uloskirjautuminen onnistuu "Logout" painikkeella.
