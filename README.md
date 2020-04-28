# Gatavošanās DB semināram

## Fork šo repositoriju

Pēc forkošanas - **clone** lokāli un aplūko doto kodu.

Pašlaik ir divi branchi - master, kur ir tikai vienkāršs savienojuma tests un 0.1, kur ir jau nedaudz vairāk visa kā.

## ElephantSQL konts un piekļuve lokāli un no Heroku

[ElephantSQL](https://www.elephantsql.com/) piedāvā par brīvu iegūt 20 MB lielu PostgreSQL datubāzi.

- Reģistrācija (iesaku reģistrēties ar GitHub kontu): <https://customer.elephantsql.com/signup>

- Izveido jaunu instanci ar TinyTurtle plan un EU-North-1 atrašanās vietu

- Aplūko jaunās DB informāciju - **host**, **User & Default database** un **password**. Šo informāciju iespējams lietot savā mīļotajā SQL pārlūkā. varianti: - <https://pgdash.io/blog/postgres-gui-tools.html>

- Ieraksta savus pieslēguma datus datnē *.env* (piemērs ir datnē .piemera-env)

- Heroku -> Settings -> Config Vars sadaļā izveido sekojošus mainīgos, kam piešķir attiecīgās vērtības:
  - ELEPHANT_HOST
  - ELEPHANT_NAME
  - ELEPHANT_PASSWORD
