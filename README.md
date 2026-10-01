# AnyNasPy

## Universelle NAS-Verwaltung für macOS

AnyNasPy ist eine native macOS-Anwendung zur komfortablen Verwaltung von NAS-Systemen verschiedener Hersteller.

NAS aufwecken, Verbindungen herstellen, SMB-Volumes verwalten, das NAS sicher herunterfahren, zeitgesteuerte Aktionen planen und mehrere Serverprofile verwalten – alles über eine übersichtliche macOS-Oberfläche.

Seit Version 2.3.0 unterstützt AnyNasPy nicht mehr ausschließlich Synology, sondern eine Vielzahl verschiedener NAS-Plattformen.

⸻

✨ Funktionen im Überblick

Bereich	Funktionen
🖥️ NAS-Verwaltung	Wake-on-LAN, sicheres Herunterfahren, automatische Erkennung
🌍 Hersteller	13 NAS-Plattformen und generisches Linux/macOS/Windows Server
💾 Volumes	SMB-Volumes erkennen, mounten und auswerfen
⏰ Zeitsteuerung	Automatisches Herunterfahren, Countdown und Coffee-Modus
☕ Coffee-Modus	Mac wach halten, ohne NAS oder Mac herunterzufahren
👥 Profile	Beliebig viele NAS-Serverprofile
🔐 Sicherheit	SSH-Schlüssel, macOS-Schlüsselbund, lokale Kommunikation
🔊 Sprachausgabe	17 Sprachen mit passenden macOS-Stimmen
🌐 Netzwerk	Bonjour/mDNS, DNS, ARP, Netzwerksuche und manuelle IP
🌍 Sprache	17 vollständig unterstützte Benutzeroberflächensprachen
🍎 macOS	Native Benutzeroberfläche und macOS-Integration

⸻

📸 Screenshots

| Main Window | Einstellungen |
|-------------|----------|
| <img width="420" alt="Server Offline" src="https://github.com/user-attachments/assets/2598c7c9-7256-4ea4-94f7-800d95f60989"> | <img width="420" alt="Settings" src="https://github.com/user-attachments/assets/514809e4-b9a4-48c7-bb67-4d7039fc147c"> |

⸻

<details>
<summary><strong>🌍 Unterstützte NAS-Systeme</strong></summary>

AnyNasPy erkennt NAS-Systeme automatisch und verwendet nach Möglichkeit herstellerspezifische Befehle.

Unterstützte Hersteller

* Synology
* QNAP
* TrueNAS / FreeNAS
* Unraid
* OpenMediaVault
* Asustor
* Western Digital
* Buffalo
* Thecus
* Generisches Linux
* macOS Server
* Windows Server
* Benutzerdefiniert

Die Herstellererkennung erfolgt über SSH und wertet unter anderem folgende Informationen aus:

* /etc/os-release
* /etc/synoinfo.conf
* /etc/config/uLinux.conf
* uname -a

Bei der Erkennung wird eine Fallback-Kette verwendet. Wenn ein herstellerspezifischer Shutdown-Befehl nicht funktioniert, werden alternative Befehle versucht.

Damit kann AnyNasPy auch mit NAS-Systemen und Servern umgehen, die nicht explizit zu einem der unterstützten Hersteller gehören.

</details>

⸻

<details>
<summary><strong>🚀 NAS-Verwaltung</strong></summary>

Wake-on-LAN

* Wake-on-LAN-Unterstützung
* Automatische Ermittlung der IP-Adresse
* MAC-Adresserkennung per ping und arp
* Mehrere WOL-Methoden als Fallback
* Konfigurierbare Wartezeit nach dem Aufwecken

Herunterfahren

AnyNasPy verwendet je nach erkanntem System geeignete Shutdown-Befehle.

Zusätzlich können eigene Befehle hinterlegt werden:

Befehl1;Befehl2;Befehl3

Die Befehle werden nacheinander als Fallback-Kette ausgeführt.

Dies ermöglicht auch die Unterstützung exotischer oder individuell konfigurierter NAS-Systeme.

Herunterfahren des Mac

Das Herunterfahren des Macs kann optional nach dem erfolgreichen Herunterfahren des NAS erfolgen.

</details>

⸻

<details>
<summary><strong>💾 Volume-Verwaltung</strong></summary>

AnyNasPy erkennt SMB-Volumes abhängig vom verwendeten NAS-System automatisch.

Herstellerspezifische Pfade

Beispiele:

System	Typische Pfade
Synology	/volume1, /volume2, …
QNAP	/share, /share/CACHEDEV1_DATA
TrueNAS	/mnt
Unraid	/mnt/user

Falls die primäre Erkennung nicht erfolgreich ist, wird als Fallback smbclient verwendet.

Funktionen

* Automatische Volume-Erkennung
* Auswahl einzelner Volumes
* SMB-Volumes mounten
* Volumes sicher auswerfen
* Automatisches Mounten nach dem NAS-Start
* Erkennung von bereits vorhandenen Volumes
* Tolerierung spezieller System-Volumes wie home und homes

Die Auswurf-Logik verwendet mehrere Stufen:

diskutil unmount
        ↓
diskutil unmount force
        ↓
umount -f

Dadurch werden auch Situationen berücksichtigt, in denen macOS oder SMB Verbindungen nicht sofort freigibt.

</details>

⸻

<details>
<summary><strong>⏰ Zeitsteuerung & Automatisierung</strong></summary>

Zeitgesteuertes Herunterfahren

Über einen eigenen Dialog kann ein zeitgesteuerter Auftrag eingerichtet werden.

Mögliche Ziele:

* Mac + NAS
* Nur NAS
* Nur Mac
* Nichts herunterfahren

Die Wartezeit kann frei gewählt werden:

1 Minute bis 720 Stunden (30 Tage)

Während des Countdowns wird die verbleibende Zeit im Hauptfenster angezeigt.

Ein laufender Countdown kann durch erneutes Klicken auf den Timer-Button abgebrochen werden.

Echte Timer-Pause

Der automatische Timer kann pausiert und anschließend fortgesetzt werden.

Beim Fortsetzen wird die zuvor verbleibende Zeit verwendet – der Timer beginnt nicht wieder bei null.

Coffee-Modus

Der Coffee-Modus hält den Mac für einen definierten Zeitraum wach, ohne anschließend NAS oder Mac herunterzufahren.

Dabei wird Apples caffeinate verwendet.

Geeignet beispielsweise für:

* Backup-Skripte
* längere Datenübertragungen
* Exporte
* Downloads
* Wartungsarbeiten

Sprachausgabe

Die verbleibende Zeit kann regelmäßig angesagt werden.

Die Sprachausgabe:

* verwendet die zur Sprache passende macOS-Stimme
* spricht Zahlen in der jeweiligen Sprache aus
* entfernt Emojis automatisch
* kann vollständig deaktiviert werden

</details>

⸻

<details>
<summary><strong>👥 Mehrere NAS-Server verwalten</strong></summary>

AnyNasPy unterstützt beliebig viele Serverprofile.

Für jedes NAS können eigene Einstellungen gespeichert werden.

Profilfunktionen

* Neues Profil erstellen
* Profil duplizieren
* Profil umbenennen
* Profil löschen
* Profil aktivieren
* Standardprofil festlegen

Dadurch können beispielsweise NAS-Systeme zu Hause, im Büro oder an verschiedenen Standorten separat verwaltet werden.

</details>

⸻

<details>
<summary><strong>🔐 Sicherheit</strong></summary>

AnyNasPy verwendet SSH zur Kommunikation mit dem NAS.

SSH-Schlüssel

Unterstützt werden:

* SSH-Key-Authentifizierung
* vorhandene SSH-Schlüssel
* Erstellung eines neuen SSH-Schlüssels
* Schlüssel mit Passphrase
* Verwendung von ssh-add

Private Schlüssel verbleiben auf dem Mac.

macOS-Schlüsselbund

Für das Herunterfahren des Macs kann das Administratorpasswort sicher im macOS-Schlüsselbund gespeichert werden.

Das Passwort:

* wird nicht im Klartext in der Konfiguration gespeichert
* verlässt den Mac nicht
* kann jederzeit über die Einstellungen gelöscht bzw. zurückgesetzt werden

Keine Cloud-Abhängigkeit

AnyNasPy benötigt keinen Cloud-Dienst für die Kommunikation mit dem NAS.

Die Kommunikation erfolgt direkt zwischen Mac und NAS.

</details>

⸻

<details>
<summary><strong>🌐 Netzwerkfunktionen</strong></summary>

Für die Erkennung und Verbindung eines NAS stehen mehrere Methoden zur Verfügung:

* Bonjour / mDNS
* DNS-Auflösung
* ARP
* Ping
* Netzwerksuche als Fallback
* manuelle IP-Adresse

Dadurch kann AnyNasPy auch dann eine Verbindung herstellen, wenn eine einzelne Erkennungsmethode nicht funktioniert.

</details>

⸻

<details>
<summary><strong>🌍 Unterstützte Sprachen</strong></summary>

AnyNasPy unterstützt derzeit 17 Sprachen:

* 🇩🇪 Deutsch
* 🇬🇧 Englisch
* 🇸🇦 Arabisch
* 🇨🇿 Tschechisch
* 🇬🇷 Griechisch
* 🇪🇸 Spanisch
* 🇫🇷 Französisch
* 🇮🇹 Italienisch
* 🇳🇱 Niederländisch
* 🇳🇴 Norwegisch
* 🇵🇱 Polnisch
* 🇵🇹 Portugiesisch
* 🇷🇺 Russisch
* 🇫🇮 Finnisch
* 🇸🇪 Schwedisch
* 🇹🇷 Türkisch
* 🇻🇳 Vietnamesisch

Auch Dialoge, Meldungen, Tooltips und Sprachausgabe berücksichtigen die ausgewählte Sprache.

Hinweis: Die Übersetzungen wurden teilweise mit Unterstützung von KI erstellt. Trotz sorgfältiger Prüfung können einzelne sprachliche Ungenauigkeiten oder ungewöhnliche Formulierungen enthalten sein.

</details>

⸻

<details>
<summary><strong>🎨 Benutzeroberfläche</strong></summary>

AnyNasPy verwendet eine native macOS-Oberfläche mit Fokus auf eine übersichtliche Bedienung.

Hauptfenster

* Statusanzeige
* Fortschrittsanzeige
* NAS-Aktionen
* Timer-Anzeige
* Profil-Auswahl
* übersichtliche Aktionsbuttons

Einstellungen

Die Einstellungen sind in verschiedene Bereiche gegliedert:

Bereich	Inhalt
Allgemein	Sprache, NAS-Daten, SSH-Schlüssel
NAS-Hersteller	Hersteller, automatische Erkennung, eigene Shutdown-Befehle
Volumes	SMB-Volumes und automatische Volume-Erkennung
Zeitsteuerung	Timer, Wartezeiten und Mount-Verhalten
Serverprofile	Erstellen, Duplizieren, Umbenennen und Löschen

Die Benutzeroberfläche passt sich auch an kleinere Bildschirme an. Dialoge mit vielen Optionen verfügen über Scrollbereiche, während wichtige Aktionsbuttons sichtbar bleiben.

</details>

⸻

<details>
<summary><strong>⌨️ Tastaturkürzel</strong></summary>

Tastenkombination	Funktion
⌘ E	Einstellungen öffnen
Enter	Bestätigen
Esc	Abbrechen

</details>

⸻

<details>
<summary><strong>⚙️ Systemanforderungen</strong></summary>

Betriebssystem

* macOS
* Apple Silicon oder Intel

NAS

AnyNasPy kann mit verschiedenen NAS-Systemen und Serverplattformen verwendet werden.

Für die vollständige Funktionalität werden je nach verwendetem System benötigt:

* SSH-Zugriff
* SMB-Dateifreigabe für Volume-Verwaltung
* Wake-on-LAN für das Aufwecken des NAS

Die tatsächlich benötigten Voraussetzungen hängen vom verwendeten NAS-Hersteller und den gewünschten Funktionen ab.

</details>

⸻

<details>
<summary><strong>📦 Installation</strong></summary>

1. Die aktuelle Version aus den GitHub Releases herunterladen.
2. Das Archiv entpacken.
3. AnyNasPy.app in den Ordner Programme verschieben.
4. Anwendung starten. (Gatekeeper Info befolgen)
5. Ein NAS-Profil konfigurieren.
6. SSH-Zugriff und gewünschte Optionen einrichten.

Weitere Informationen zur jeweiligen Version befinden sich in den Release Notes.

</details>

⸻

<details>
<summary><strong>🔒 macOS Gatekeeper</strong></summary>

AnyNasPy ist derzeit nicht mit einem Apple-Developer-Zertifikat signiert.

Beim ersten Start kann macOS deshalb die Ausführung blockieren.

App über die Systemeinstellungen freigeben

1. AnyNasPy einmal starten.
2. Die Warnmeldung schließen.
3. Systemeinstellungen → Datenschutz & Sicherheit öffnen.
4. Nach unten scrollen.
5. Die Meldung über die blockierte Anwendung suchen.
6. „Dennoch öffnen“ auswählen.
7. Die Sicherheitsabfrage bestätigen.

Alternativ: Quarantäne-Attribut entfernen

Über das Terminal:

xattr -d com.apple.quarantine '/Users/username/Downloads/AnyNasPy.app'

Den Pfad gegebenenfalls an den tatsächlichen Speicherort der Anwendung anpassen.

</details>

⸻

<details>
<summary><strong>🛠️ Fehlerbehebung</strong></summary>

NAS wird nicht gefunden

* IP-Adresse über die Suchfunktion ermitteln.
* Prüfen, ob das NAS eingeschaltet ist.
* Netzwerkverbindung überprüfen.
* DNS-/Bonjour-Erkennung prüfen.
* IP-Adresse gegebenenfalls manuell eintragen.

Wake-on-LAN funktioniert nicht

* MAC-Adresse überprüfen.
* Wake-on-LAN am NAS aktivieren.
* Prüfen, ob das NAS Wake-on-LAN unterstützt.
* Netzwerkverbindung überprüfen.

AnyNasPy verwendet mehrere Methoden für Wake-on-LAN und kann dadurch unterschiedliche Netzwerkkonfigurationen berücksichtigen.

Volume kann nicht gemountet werden

* Prüfen, ob das NAS erreichbar ist.
* SMB-Dienst überprüfen.
* Namen des Volumes kontrollieren.
* Mount-Wiederholungen in den Einstellungen erhöhen.
* Prüfen, ob das Volume bereits gemountet ist.

SSH-Verbindung funktioniert nicht

Prüfen:

ssh-add ~/.ssh/id_rsa

Alternativ kann über den SSH-Schlüssel-Assistenten ein eigener Schlüssel erstellt werden.

Der öffentliche Schlüssel muss auf dem NAS hinterlegt sein.

Shutdown funktioniert nicht

Je nach NAS-System kann ein entsprechender Benutzer bzw. eine entsprechende Berechtigung erforderlich sein.

Bei Synology kann beispielsweise eine NOPASSWD-Regel für die entsprechenden Shutdown-Befehle notwendig sein.

</details>

⸻

<details>
<summary><strong>📁 Konfigurations- und Logdateien</strong></summary>

Die Konfigurationsdateien befinden sich unter:

~/Library/Application Support/AnyNasPy/

Typische Dateien:

AnyNasPy/
├── synaspy_config.json
├── server_profiles.json
└── Logs/
    ├── ...

Die Logdateien werden automatisch rotiert.

Die Anwendung verwendet sowohl zeit- als auch größenbasierte Mechanismen zur Begrenzung der Logdateien.

</details>

⸻

<details>
<summary><strong>🏗️ Projektstruktur</strong></summary>

Die Anwendung basiert auf Python und PyQt.

Beispielhafte Projektstruktur:

AnyNasPy/
├── AnyNasPy.py
├── requirements.txt
├── README.md
├── LICENSE
├── BinhDiez.png
├── AnyNasPy.png
└── .gitignore

Zentrale Komponenten

* LanguageManager – Mehrsprachigkeit
* ServerProfile – Daten eines NAS-Profils
* ServerProfileManager – Verwaltung und Speicherung der Profile
* Config – Zentrale Konfiguration
* AnyNasPy – Hauptfenster und Kernlogik
* ConfigDialog – Einstellungsdialog
* InfoDialog – Informationen, Lizenz und Update-Prüfung
* AppLogger – Protokollierung und Log-Rotation

</details>

⸻

🔄 Versionsverlauf

<details>
<summary><strong>AnyNasPy 2.3.0 – Universelle NAS-Unterstützung</strong></summary>

🌍 Universelle NAS-Unterstützung

Version 2.3.0 erweitert AnyNasPy von einer primär auf Synology ausgerichteten Anwendung zu einer universellen NAS-Verwaltungslösung.

Unterstützt werden jetzt:

* Synology
* QNAP
* TrueNAS / FreeNAS
* Unraid
* OpenMediaVault
* Asustor
* Western Digital
* Buffalo
* Thecus
* generisches Linux
* macOS Server
* Windows Server
* Benutzerdefinierte Systeme

🔧 Automatische Herstellererkennung

* Neuer Button „Auto-erkennen“
* SSH-basierte Erkennung
* Auswertung verschiedener Systemdateien
* Erkennung über uname -a
* Mustervergleich zur Herstellerbestimmung
* Rückfrage bei abweichender erkannter Konfiguration

📴 Herstellerabhängige Shutdown-Befehle

* Herstellerabhängige Befehle
* Automatische Fallback-Kette
* Benutzerdefinierte Befehle
* Mehrere eigene Befehle mit Semikolon möglich
* Hilfedialog mit typischen Befehlen

💾 Verbesserte Volume-Erkennung

Herstellerspezifische Pfade werden bevorzugt verwendet.

Zusätzlicher Fallback über smbclient.

Während der Erkennung werden verständliche Statusinformationen angezeigt:

* „Suche Volumes …“
* „X Volumes gefunden“
* „Keine Volumes gefunden“

🔍 MAC-Adresserkennung

Über einen neuen Button kann die MAC-Adresse automatisch über ping und arp ermittelt werden.

🛠️ Diagnose und Logging

Verbesserte Fehlermeldungen und detailliertere Logs, unter anderem für:

* nicht erreichbare NAS-Systeme
* nicht akzeptierte SSH-Schlüssel
* fehlende SSH-Schlüssel
* Probleme mit SSH-Schlüsseln mit Passphrase

💿 Verbesserte Auswurf-Logik

Der Auswurf erfolgt jetzt in mehreren Stufen:

diskutil unmount
        ↓
diskutil unmount force
        ↓
umount -f

Zusätzlich werden automatisch gemountete System-Volumes wie home und homes berücksichtigt.

🐛 Behobene Fehler

* ~ in SSH-Key-Pfaden wurde nicht korrekt expandiert.
* Bestimmte Zeichen in SSH-Befehlen konnten als Shell-Kommentare interpretiert werden.
* Fehlende NAS-Volumes konnten die Erkennung blockieren.
* Beim Duplizieren von Profilen gingen einzelne NAS-Einstellungen verloren.
* Persönliche Standard-Volume-Namen wurden entfernt.
* Der bisherige Hilfe-Button wurde durch die automatische Herstellererkennung ersetzt.

</details>

⸻

<details>
<summary><strong>SyNasPy 2.2.0 – Zeitsteuerung & Coffee-Modus</strong></summary>

⏰ Zeitgesteuertes Herunterfahren

* Neuer Timer für geplante Aktionen
* Zielauswahl:
    * Mac + NAS
    * Nur NAS
    * Nur Mac
    * Nichts herunterfahren
* Wartezeit von 1 Minute bis 720 Stunden
* Countdown im Hauptfenster
* Timer kann abgebrochen werden
* Stündliche Sprachausgabe der verbleibenden Zeit

☕ Coffee-Modus

Der Mac kann für eine definierte Zeit wach gehalten werden.

Dafür wird caffeinate verwendet.

⏸ Auto-Timer pausieren

Der automatische Timer kann pausiert und später exakt an der gespeicherten Position fortgesetzt werden.

🔐 Mac-Shutdown ohne Terminal-Konfiguration

Zwei Möglichkeiten stehen zur Verfügung:

1. NOPASSWD-sudoers-Regel
2. macOS-Schlüsselbund

Das Administratorpasswort wird verschlüsselt im Schlüsselbund gespeichert.

🌍 Verbesserte Sprachausgabe

* 17 Sprachen
* passende macOS-Stimmen
* lokalisierte Aussprache von Zahlen
* automatische Entfernung von Emojis
* abschaltbare Sprachausgabe

🛡️ Schutz vor versehentlichem Herunterfahren

Bei einem aktiven Timer wird vor manuellen Shutdown-Aktionen gewarnt.

🛠️ Verbesserte Stabilität

* Robusterer Exception-Handler
* Stacktrace im Terminal
* Crash-Datei als Fallback
* atexit-Handler
* SIGTERM-Behandlung
* sauberes Beenden von caffeinate
* keine zurückbleibenden Zombie-Prozesse

🎨 Verbesserte Benutzeroberfläche

* Dynamische Fensterhöhe
* zweizeilige Statusanzeige
* einheitliche Button-Größen
* Scrollbereich für kleine Bildschirme
* fixierte Dialogbuttons
* verbesserte Icons
* Vorschau für geplante Aktionen
* übersichtlichere Einstellungen

🌐 Übersetzungen

17 vollständig gepflegte Sprachen mit:

* lokalisierten Dialogen
* lokalisierten Ja/Nein-Schaltflächen
* verbessertem Fallback auf Englisch
* dynamischer Aktualisierung von Tooltips

🐛 Behobene Fehler

Unter anderem:

* Kollision zwischen Auto-Timer und aktivem Zeitgeber
* falsche Anzeige bei Coffee-Timern
* falsche Sprachausgabe
* fehlerhafte Pause-/Play-Funktion
* fehlerhafte Eject-Warnungen
* lokalisierte Startup-Dialoge
* unterschiedliche Zielwerte für den Coffee-Modus

</details>

⸻

<details>
<summary><strong>SyNasPy 2.0.0</strong></summary>

* Unterstützung mehrerer NAS-Serverprofile
* 17 Sprachen
* Profilverwaltung
* SSH-Schlüssel-Assistent
* konfigurierbare Shutdown-Verzögerung
* integrierte Update-Prüfung
* verbesserte Shutdown-Logik
* Entfernung der alten boQuitNASapp.txt-Lösung
* verbesserte Fortschrittsanzeige

</details>

⸻

<details>
<summary><strong>SyNasPy 1.0.0 – Legacy</strong></summary>

* Verwaltung eines einzelnen NAS
* Wake-on-LAN
* NAS-Herunterfahren
* SMB-Volume-Verwaltung
* grundlegender Einstellungsdialog

</details>

⸻

🔄 Namensänderung: SyNasPy → AnyNasPy

Ab Version 2.3.0 wurde der Funktionsumfang von SyNasPy grundlegend erweitert.

Die Anwendung ist nicht mehr ausschließlich auf Synology NAS-Systeme ausgerichtet.

Aus diesem Grund wird das Projekt unter dem neuen Namen AnyNasPy weitergeführt.

Die bisherige Versionshistorie bleibt Bestandteil des Projekts.

⸻

🤝 Mitwirken

Beiträge, Fehlerberichte, Verbesserungsvorschläge und Pull Requests sind willkommen.

Wenn du einen Fehler findest oder eine Idee für eine neue Funktion hast, erstelle bitte ein Issue im GitHub-Repository.

⸻

📄 Lizenz

Dieses Projekt steht unter der MIT License.

Copyright © 2026 BinhDiez64.

PyQt5

Diese Anwendung verwendet PyQt5.

PyQt5 steht unter der GNU General Public License (GPLv3).

Weitere Informationen:

https://www.gnu.org/licenses/gpl-3.0.html

⸻

🙏 Danksagung

Vielen Dank an:

* Synology für die hervorragende NAS-Hardware und DSM
* PyQt für die Qt-Bindings
* die macOS-Community für hilfreiche Informationen zur Systemintegration
* die Entwickler der verschiedenen NAS-Plattformen und Open-Source-Projekte

⸻

❤️ AnyNasPy

AnyNasPy macht die Verwaltung von NAS-Systemen unter macOS einfach, sicher und komfortabel.

Von Synology bis QNAP, TrueNAS, Unraid und weiteren Systemen – mit automatischer Erkennung, SMB-Management, Zeitsteuerung und mehreren Serverprofilen.

---

<details>
<summary>🖥️ Download-Info</summary>

### Download-Versiones

| Suffix | Betriebssystem |
|--------|-----------------|
| `_macOS_as` | Apple Silicon (M1–M4) |
| `_macOS_intel` | Intel Macs |

### Extract 7z-Archive

| Betriebssystem | Empfohlene App |
|---------------|----------------|
| 🍎 macOS | **Keka** – <https://www.keka.io/> |


</details>

---

<details>
<summary>🔑 7z Password</summary>

**BinhDiez**

</details>
