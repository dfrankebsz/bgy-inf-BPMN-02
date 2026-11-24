# BPMN-Labor · UE 3 – Schleifen und Parallelisierung

## Ziel und Aufbau

Ein eigenständiger, digitaler Lernkurs für Informatik am Beruflichen Gymnasium (Jahrgangsstufe 11), der fachlich auf **UE 2** aufbaut. Schwerpunkt: **aus einer betrieblichen Textbeschreibung eigenständig ein BPMN-Diagramm in draw.io erstellen**.

Die Syntaxlegende enthält **alle fünf aus UE 2 bekannten Elemente** (Start, Task, Ende, Sequenzfluss, XOR) sowie **AND-Gateway und Rückführungsschleife aus UE 3**. Pool, Lane, Nachrichtenereignisse, Nachrichtenfluss, Datenobjekt und Terminierung werden nur als Ausblick auf UE 4 erwähnt.

**32 reguläre Aufgaben**, bedarfsorientiert auf die Kapitel **4 / 6 / 6 / 7 / 9** verteilt, **4 Bonusaufgaben** und **10 Testaufgaben**. AFB I/II/III unter den regulären Aufgaben: **8/16/8**.

## Bereitstellung über GitHub und Netlify

1. Den **Inhalt** dieses ZIP-Archivs (nicht den darüberliegenden Ordner) in ein eigenes GitHub-Repository hochladen.
2. Neues Netlify-Projekt über *Add new project* und *Import from Git* mit diesem Repository verknüpfen.
3. Netlify verwendet die Konfiguration in `netlify.toml`: Build `npm run build`, Publish-Ordner `dist`, Functions `netlify/functions`.
4. In **Site configuration → Environment variables** die Variable `TEACHER_ACCESS_CODE` (mindestens 16 Zeichen) hinterlegen und die Site erneut deployen. Den Lehrercode nur dem zuständigen Lehrpersonal geben. Keine allgemeine `AUTH`-Variable nötig.
5. Lehrkraft: auf der Kurswebsite registrieren, Klasse, selbst gewählten Nickname, Passwort und Rolle „Lehrkraft“ plus den Netlify-Lehrercode angeben. Schülerinnen und Schüler registrieren sich mit **derselben Klassenbezeichnung** und ihrem eigenen Nickname und Passwort. Beim Login ist die Klasse Pflicht.
6. Unangemeldete Nutzung bleibt möglich, Fortschritte im Gastmodus werden lokal im Browser gespeichert. Angemeldete Konten speichern ihre Fortschritte auf Netlify Blobs und können sie geräteübergreifend fortsetzen.

**Wichtig:** Dieser Kurs verwendet eigene UE-3-Stores und Cookies. Konten aus UE 2 werden **nicht automatisch übertragen**. Die ZIP-Datei ist **kein Update für die bestehende UE-2-Site**; richten Sie ein neues Netlify-Projekt ein.

## Lernaufgaben und Musterlösungen

- Kurze Aufgaben: Multiple Choice (einfach/mehrfach), Richtig/Falsch, Reihenfolgen, Drag & Drop und Symbole in BPMN-Diagrammlücken ziehen.
- Komplexe Aufgaben: eigenständige Diagramme in der auf den Schul-PCs installierten Anwendung **draw.io** anfertigen.
- Wo die Aufgabe ein vorhandenes Diagramm korrigieren oder erweitern soll, gibt es direkt an der Aufgabe einen Download-Button für eine **bearbeitbare `.drawio`-Datei**.
- Bei den eigenständigen Modellierungsaufgaben ist **absichtlich keine Vorlage** vorhanden. Die Musterlösung erscheint erst nach einer Sicherheitsabfrage.
- Danach entscheiden die Lernenden **selbst**, ob ihr lokales Diagramm fachlich mit der Musterlösung übereinstimmt. Kein Diagramm-Upload, keine automatische Bildbewertung.
- Das PDF-Lernportfolio umfasst bereits bearbeitete Aufgaben und schriftliche Notizen bzw. Selbstbewertungen; die lokalen `.drawio`-Dateien bleiben auf den Rechnern der Lernenden.

## Accounts und Datenschutz

Die Plattform speichert bei Anmeldung **Nickname, Klassenzuordnung, gesalzenen Passwort-Hash und Lernfortschritt** in Netlify Blobs. Lehrkräfte sehen nur die Schülerkonten ihrer Klasse und können Fortschritte zurücksetzen, Konten entfernen und Passwörter auf vorläufige Zugangsdaten zurücksetzen. Sessions werden über HttpOnly/Secure-Cookies verwaltet. Ein Passwort-Reset invalidiert ältere Sitzungen.

Vor schulischer Verwendung sind Datenschutz, Auftragsverarbeitung, Hosting-Region, Einwilligungs-/Informationspflichten und gegebenenfalls ein schulisches Datenschutzkonzept zu prüfen. Keine Klarnamen oder privaten E-Mail-Adressen nötig.

## Entwicklung und Tests

- `npm install`
- `npm run check` – fachliche und technische Datenkonsistenz, Aufgabenlösungen und Verteilung
- `npm test` – automatische Aufgaben- und API-Mock-Tests
- `npm run build` – veröffentlicht `dist/` und kopiert den Frontend-Code, Grafiken und Musterdiagramme

Der echte Login/Netlify-Blobs-Betrieb und die PDF-Erstellung müssen nach dem Deployment auf Netlify vollständig getestet werden. Die Lehrkraft muss die fachliche und redaktionelle Endprüfung vor Unterrichtseinsatz durchführen.

**Videoquelle:** GBTEC, BPMN-Tutorial. Die Links enthalten Start- und Endparameter; die konkreten Ausschnitte sind jeweils im Lernkurs beschrieben. Die Einbettung/Verfügbarkeit hängt von YouTube ab.

**Quelle für BPMN-Syntax:** Object Management Group, *Business Process Model and Notation (BPMN), Version 2.0.2* (`https://www.omg.org/spec/BPMN/2.0.2/PDF`).

**KI-Nachweis und Quellenhinweise** sind im Seitenfuß zu finden.
