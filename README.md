# Rakenduste programmeerimine
## Discgolfi rakenduse API

#### Install

##### Eelnõuded

1. Python >= 3.4

##### Kasutamine

1. Klooni repo
2. Testserveri käivitamiseks olles command prompti/terminaliga projekti juurkaustas lokaalselt:

```
python3 manage.py runserver
```
Kohalikus võrgus kättesaadavana:

```
python3 manage.py runserver 0.0.0.0:8000
```
#### Endpointid

Kõik rajad
```
localhost:8000/dg/courses
```
Üks rada ID järgi
```
localhost:8000/dg/courses/<id>
```
Kõik korvid
```
localhost:8000/dg/holes
```
Kõik korvid id järgi
```
localhost:8000/dg/holes/<id>
```
Kõik raundid
```
localhost:8000/dg/rounds
```
Muster peaks mõistetav vist olema :D
```
localhost:8000/dg/rounds/<id>
```
Mängijad
```
localhost:8000/dg/players
```
```
localhost:8000/dg/players/<id>
```
Skoorid
```
localhost:8000/dg/scores
```
```
localhost:8000/dg/scores/<id>
```
