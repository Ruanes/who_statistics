Hjemmeoppgave

I denne oppgaven skal du få prøve deg på et Python-rammeverk som heter Beer Garden. Beer Garden er et verktøy for å enkelt lage et REST-api ved å bruke funksjoner i Python. Beer Garden inkluderer også et web-ui som er enkelt å bruke. I denne oppgaven skal du lage en plugin i Beer Garden som implementerer kommandoer som skal utforske et datasett kalt WHO Life Expectancy. Tanken er at du skal bruke ditt favorittdataanalyseverktøy i Python(pandas, numpy eller noe annet) til å lese datasettet fra fil og deretter lage kommandoene beskrevet under. Velg passende input og output typer for kommandoene dine. Statistikker vi er ute etter: stat = ["Life expectancy","Adult Mortality","Infant deaths","Alcohol","Percentage expenditure","Hepatitis B","Measles","BMI","Under-five deaths","Polio","Total expenditure","Diphtheria","HIV/AIDS","GDP","Population","Thinness 1-19 years","Thinness 5-9 years","Income composition of resources","Schooling"]. Vedlagt er de to datasettene ("Life Expectancy Data.csv", "countries of the world.csv") som du skal bruke i oppgaven.

Oppgaver:
1. Installer Docker Desktop. Instruksjoner finnes på: https://docs.docker.com/get-docker/
2. Installer Git. Instruksjoner finnes på: https://git-scm.com/downloads/
3. Installer Beer Garden. Instruksjoner finnes på: https://beer-garden.io/docs/startup/installation-guides/docker/
4. Følg oppskriften for å lage en remote plugin: https://beer-garden.io/docs/plugins/python/remote-guide
5. Lag en kommando 'ping' som ikke har input men returnerer strengen "pong".
- Parametere: Ingen
6. Lag en kommando 'get_stat' som returnerer en statistikk for et land for et gitt år.
- Parametere: country, year, stat
7. Lag en kommando 'get_latest' som returnerer siste statistikk for et land.
- Parametere: country, stat
8. Lag en kommando 'get_avg' som returner gjennomsnittlig statistikk for et land.
- Parametere: country, stat
9. Vi er også interessert i gjennomsnittet for regionen landet tilhører. Vi har lagt ved et annet datasett Countries of the world som du kan bruke til å joine med WHO Life Expectancy. Dette vil berike informasjon om land med region og andre kolonner. Lag en kommando som joiner Life Expectancy med Countries of the world ved å bruke en join-nøkkel på Country og returner gjennomsnittlig statistikk for en region for et gitt år. Noen land har ikke samme navn i begge datasett, ignorer disse. Kall kommandoen 'get_avg_region'.
- Parametere: region, year, stat
10. Legg ved pluginen din når du sender svaret på oppgaven til oss.
