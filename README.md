# Gatavošanās DB semināram

## Fork šo repositoriju

Pēc forkošanas - **clone** lokāli un aplūko doto kodu.

Pašlaik ir divi branchi - *master*, kur ir tikai vienkāršs savienojuma tests un *0.1-vardadienas* , kur ir jau nedaudz vairāk visa kā.

## ElephantSQL konts un piekļuve tam

[ElephantSQL](https://www.elephantsql.com/) piedāvā par brīvu iegūt 20 MB lielu PostgreSQL datubāzi, kas ir pietiekami mūsu mērķiem. Heroku 5MB/10k rindiņu iespējas ir par mazu.

1. Reģistrācija (iesaku reģistrēties ar GitHub kontu): <https://customer.elephantsql.com/signup>

1. Izveido jaunu instanci ar TinyTurtle plan un EU-North-1 atrašanās vietu

1. Aplūko jaunās DB informāciju - **host**, **User & Default database** un **password**. Šo informāciju iespējams lietot savā mīļotajā SQL pārlūkā. varianti: - <https://pgdash.io/blog/postgres-gui-tools.html>

## Piekļuve caur Flask aplikāciju

1. Ieraksta savus pieslēguma datus *master* zarā datnē `data.py`
  Palaiž programmu lokāli (komandas `python main.py` vai `heroku local`), notestē vai DB pieslēgums darbojas atverot pārlūkprogrammā <http://127.0.0.1:5000/>

1. Ieraksta savus pieslēguma datus datnē *.env* (piemērs ir zarā *0.1-vardadienas* datnē .piemera-env)

1. Heroku -> Settings -> Config Vars sadaļā izveido sekojošus mainīgos, kam piešķir attiecīgās vērtības:

  ELEPHANT_HOST
  ELEPHANT_NAME
  ELEPHANT_PASSWORD

1. Ielasa `.env` vērtības lokāli izmantojot *Git Bash* ar komandu: 

  `source .env`

   pārbauda vai programma strādā lokāli

1. Veic *deploy* uz Heroku zaram *0.1-vardadienas*
