# Requists Funcionals TapatAPP 

## Descripcio del projecte
Una cataracta congènita és l'opacitat del cristal·lí de l'ull que està present en néixer. La incidència de cataracta congènita està al voltant dels 3 / 10.000 nens, a l'any de vida. A l'Hospital de Sant Joan de Déu s'han operat en l'últim any al voltant de 100 cataractes infantils.

Les cataractes són la causa més freqüent de ceguesa tractable en la infància i es podria fer una estimació de 200.000 nens cecs per cataracta al món.

L'ull amb cataracta congènita, un cop operat, ha de seguir un exhaustiu règim de rehabilitació per evitar l'ambliopia, el que coneixem comunament com "ull gandul", i aquí és on pretén ajudar TapatApp! 

A part del tractament amb lents de contacte d’alta graduació i, posteriorment, lents intraoculars, el tractament més eficaç possible en aquesta patologia consisteix en l’aplicació d’un pedaç (parche) a l’ull dominant, fent que l’ull operat es vegi forçat a desenvolupar-se el màxim possible. El repte en aquest sentit, és aconseguir que l’aplicació d’aquest tractament sigui el més equilibrada possible, per aconseguir el màxim desenvolupament d’aquest ull operat, sense penalitzar el de l’ull dominant, que també ha «d’aprendre a veure» en el que s’anomena l’etapa plàstica del cervell, que finalitza entre els 6-8 anys.

Durant aquesta etapa, el tractament amb pedaç varia en funció de l’edat de l’infant, començant per aplicar-lo la meitat del temps que estigui despert en els primers mesos de vida, i continuant amb un temps fix diari que estableix l’oftalmòleg. La dificultat real d’aquesta gestió rau en controlar el nombre de minuts que porta o li queda per portar al nen aquest pedaç, ja que el seu son acostuma a ser variable i molt freqüent durant al dia. Moltes famílies manifesten la dificultat de controlar això per les freqüents migdiades que fan els petits, i per la incertesa de quan s’adormiran en el que queda de dia.

L’objectiu de TapatApp consisteix en proporcionar a totes les famílies afectades per cataracta congènita, o qualsevol patologia que faci servir pedaç ocular, una eina senzilla i gratuïta que els ajudi a portar aquest tractament de la forma més equilibrada possible i, com a conseqüència, obtenir el màxim desenvolupament d’agudesa visual.


## Objectiu del projecte

- Control del temps del pegat de l'infant.
- Control del tractament de la 1/2 del temps que l'infat està despert.
- Control del tractament d'un temps fix que l'infant està depert.
- Compartir Informació del tractament amb el servei mèdic.
- Acces restringit per tipus d'usauri al control del pegat.Aplicació Multiusuari.
- Desenvolupament una App mòbil.

## Actors de la App

- Administrador
- Servei Mèdic (Metges oftalmòlegs)
- Tutors (mares/pares)
- Cuidadors (mestres,avos,...)
- Infant
- "Part pública"

# Requisits Funcionals RF i Requisits No Funcionals
## Requisits Funcionals
### RF1: Login / Autenticació

Actors: Administrador, Metges, Tutors, Cuidadors, Infant.

Funcionalitats:
- Autenticació segura.
- Recuperació de contrasenya.
- Bloqueig temporal després de diversos intents fallits.

Descripció:
El sistema permetrà que tots els usuaris es puguin autenticar amb un usuari i contrasenya per accedir a les funcionalitats corresponents al seu rol.

### RF2: Registre d’usuari

Actors: Tutors, Administrador, Metges.

Funcionalitats:
- Formulario de registre amb dades personals i dades de l’infant.
- Validació de dades.
- Assignació de rol i permisos.
- Notificació de registre correcte o denegació.

Descripció:
Els tutors poden registrar-se a l’app introduint les dades personals i del pacient. L’administrador o el servei mèdic poden aprovar o gestionar els registres.

### RF3: Gestió dels usuaris i permisos

Actors: Administrador.

Funcionalitats:
- Gestió de comptes d’usuari.
- Assignació i modificació de rols (Metge, Tutor, Cuidador).
- Control d’accés a funcionalitats segons rol.

Descripció:
L’administrador pot crear, editar, eliminar i assignar rols als usuaris.

### RF4: Introducció i control del temps d’ús del pegat

Actors: Tutors, Cuidadors.

Funcionalitats:
- Botons per iniciar i aturar el comptador de temps d’ús.
- Ajust automàtic segons horari de son de l’infant.
- Visualització clara del temps d’ús actual i restant.

Descripció:
Els tutors i cuidadors poden registrar quan l’infant comença i acaba d’utilitzar el pegat. El sistema calcula el temps total d’ús i el temps restant segons el tractament prescrit.

### RF5: Configuració del tractament

Actors: Metges.

Funcionalitats:
- Definició de temps diari d’ús del pegat.
- Modificació del tractament segons evolució.
- Enviament automàtic de notificacions als tutors.

Descripció:
El metge estableix el règim de tractament segons l’edat i condició de l’infant (mitja part del temps despert, o temps fix diari).


### RF6: Sincronització i compartició de dades amb el servei mèdic

Actors: Metges, Tutors.

Funcionalitats:
- Accés del metge a informes dels pacients.
- Actualització en temps real o sincronitzada.
- Possibilitat de fer comentaris i indicacions.

Descripció:
Les dades del tractament (temps d’ús, percentatges, dificultats) es comparteixen amb els metges de forma segura i actualitzada.

### RF7: Multiusuari i control d’accés

Actors: Tutors, Cuidadors, Metges.

Funcionalitats:
- Invitació o assignació de cuidadors.
- Diferents nivells de permisos (visualització, modificació).
- Registre d’activitat per usuari.

Descripció:
La app permet diferents usuaris associats al mateix infant (mares, pares, cuidadors, mestres) amb permisos específics.

### RF8: Recordatoris i notificacions

Actors: Tutors, Cuidadors.

Funcionalitats:
- Notificacions programades i personalitzables.
- Alertes en cas de desviacions respecte al tractament.

Descripció:
El sistema envia notificacions als tutors i cuidadors per recordar l’aplicació o retirada del pegat segons el tractament.

### RF9: Visualització de l’evolució i informes

Actors: Tutors, Metges.

Funcionalitats:
- Gràfics diaris, setmanals, mensuals.
- Exportació d’informes en PDF o altres formats.
- Comparació amb el tractament prescrit.

Descripció:
Els tutors i metges poden consultar gràfics i informes del temps d’ús del pegat i evolució del tractament.

### RF10: Part pública

Actors: Públic en general.

Funcionalitats:
- Pàgina informativa amb consells.
- Preguntes freqüents.
- Contacte i ajuda.

Descripció:
La part pública ofereix informació general sobre la cataracta congènita i el tractament amb pegat, sense necessitat d’identificació.


## Requisits No Funcionals
### RNF1: Usabilitat

La app ha de ser fàcil d’utilitzar per usuaris amb poc coneixement tecnològic.

Interfície clara i intuïtiva.

### RNF2: Seguretat

Protecció de dades personals i mèdiques segons normatives (GDPR).

Comunicació xifrada (HTTPS, encriptació de dades).

Controls d’accés robustos.

### RNF3: Disponibilitat i rendiment

L’aplicació ha d’estar disponible 24/7 amb mínimes caigudes.

Temps de resposta inferior a 2 segons en operacions principals.

### RNF4: Compatibilitat

Compatible amb dispositius Android i iOS.

Adaptat a diferents mides de pantalla.

### RNF5: Mantenibilitat

Codi modular i documentat per facilitar futures millores.

Facilitat per actualitzar i corregir errors.
