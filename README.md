# Entorns de desenvolupament 25-26
Entorns de desenvolupament 25-26 / Prova

## Requisits Funcionals TapatAPP
[Requisits Funcionals TapatAPP](TapatAPP.md)

## Requisits Funcionals TapatAPP
[Requisits Funcionals TapatAPP](TapatAPPtec.md)

## Configuració Github VsCode
Aquí configurem VsCode

## Planificació Scrum
- Iteració 1: 12/11 - 17/12 (15h) - Connexió Client Server
- Iteració 2: 12/01 - 04/02 (12h) - End Point WebService, dades Tutor i Child
- Iteració 3: 09/02 - 04/03 (10h) - Digrames classes ,Login i Seguretat
- Iteració 4: 09/03 - 08/04 (11h) - Visites Wireframes i BBDD
- Iteració 5: 13/04 - 29/04 (09h) - Pegat i Testing

# Portatip 1
Connectar Client / Servidor. 
Consultar dades d'usuari per nom.

[Diagrama d'arquitectura prototip 1](charts/diagramaprototip1.mermaid)

# End-Points WebService

Definició del End-Point del WebService:

URL Server desenvolupament: http://localhost:5000/

| URL       |  Method       | Paràmetres                     | Descripció                | Output        |
------------|---------------|--------------------------------|---------------------------|---------------|
| /user     | Get           | username <String> (obligatori) | Retornem la informació de | {"code_response=1, descripcio="" , 
|-----------|---------------|--------------------------------|---------------------------|
name="Gustavo Lloris" username="glloris", password="12345", rol="tutor", email="glloris@xtec.cat"} |
---------------------------------------------------------------------------------------------------|
