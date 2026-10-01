#!/usr/bin/env python3
"""AnyNasPy - NAS Management Tool
    GUI-Anwendung zur Verwaltung eines Synology NAS-Servers
    Funktionen: Wake-on-LAN, Zeitgesteuertes Herunterfahren, Volume-Management, Caffeinate für den Mac

Version 2.3.0
    Universelle NAS-Unterstützung: AnyNasPy v2.3.0 unterstützt jetzt 13 NAS-Hersteller (Synology, QNAP, TrueNAS, Unraid, OpenMediaVault, Asustor, Western Digital, Buffalo, Thecus, generisches Linux, macOS Server, Windows Server). Shutdown-Befehle werden hersteller-spezifisch gewählt, mit automatischer Fallback-Kette — falls der erste Befehl nicht funktioniert, werden weitere probiert.

    Robusterer Volume-Auswurf: diskutil unmount (sanft) → diskutil unmount force → umount -f in drei Stufen. System-Volumes wie home werden automatisch erkannt und nicht-blockierend behandelt (macOS remountet sie ohnehin).

Version 2.2.0
    ## 🆕 Neue Funktionen

    ### ⏰ Zeitgesteuertes Herunterfahren
    - **Neuer Button** „🕐 Zeitgesteuert herunterfahren" im Hauptfenster
    - **Dialog** mit:
    - **Ziel-Auswahl:** Mac + NAS / Nur NAS / Nur Mac / Nichts herunterfahren (Coffee-Modus)
    - **Wartezeit:** frei wählbar von 1 Minute bis 720 Stunden (30 Tage)
    - **caffeinate-Optionen:** Auswahl zwischen 6 Varianten, inkl. Lern-Fact zur Verwendung im Terminal
    - **Countdown** wird im Status-Label angezeigt (gold hervorgehoben)
    - **Countdown abbrechen** per erneutem Klick auf den Button
    - **Stündliche Sprachausgabe** der verbleibenden Zeit

    ### ☕ Coffee-Modus (System wach halten)
    - **Neues Ziel** „Nichts herunterfahren" – der Mac bleibt wach, z. B. für Backup-Skripte
    - **caffeinate-Integration** mit verständlichen Beschreibungen pro Option
    - **Automatische Endzeit-Berechnung** und Vorschau im Dialog

    ### ⏸ Echte Pause für den Auto-Timer
    - **Pause-Button** (⏸) hält den Auto-Timer **wirklich an** – Zähler wird gemerkt
    - **Fortsetzen** (▶) startet an der pausierten Sekunde – nicht bei 0
    - **Status-Anzeige** mit verbleibender Zeit

    ### 🔐 Mac-Shutdown ohne Terminal-Setup
    - **Zwei-Wege-Authentifizierung:**
    1. **NOPASSWD-sudoers-Regel** (für Power-User)
    2. **macOS-Schlüsselbund** (Keychain) – für alle anderen
    - **Erstmalige Einrichtung** direkt beim App-Start, ohne Terminal
    - **Passwort-zurücksetzen-Button** in den Einstellungen
    - **Admin-Passwort verlässt nie das System** (im verschlüsselten Keychain)

    ### 🌍 Mehrsprachige Sprachausgabe
    - **17 Sprachen** werden jetzt mit den passenden **Stimmen** vorgelesen
    - **Zahlen werden in der Landessprache** ausgesprochen
    - **Emojis** werden automatisch aus der Sprachausgabe entfernt
    - **Checkbox „Sprachausgabe aktiviert"** in den Einstellungen – App kann stumm betrieben werden

    ---

    ## 🛡️ Sicherheit & Stabilität

    ### Neuer Schutz vor versehentlichem Herunterfahren
    - **Bei laufendem Shutdown-Timer oder Coffee-Timer** wird bei manuellen Shutdown-Aktionen nachgefragt
    - **Klarer Hinweis** mit verbleibender Zeit und geplantem Ziel
    - **Kein versehentliches Zerstören** eines laufenden Auftrags mehr

    ### Verbesserte Auswurf-Logik
    - **`home` / `homes`** (Synology-System-Volumes) werden jetzt toleriert, wenn sie sich nicht auswerfen lassen
    - **Sanfterer Auswurf** – erst `diskutil unmount` (ohne force), dann `force`, dann `umount -f`
    - **Zwei-Stufen-Endkontrolle** – SMB braucht manchmal länger, um Verbindungen zu schließen
    - **Eject-Warnung** nur bei echten Problemen mit normalen Volumes

    ### Robusterer Exception-Handler
    - **Stacktrace** wird jetzt immer im Terminal ausgegeben
    - **Fallback auf Crash-Datei**, falls der Logger nicht verfügbar ist
    - **`atexit`-Handler** für saubere Logs beim Beenden

    ### SIGTERM-Handler
    - **caffeinate** wird sauber beendet, wenn macOS die App herunterfährt
    - **Laufende Timer** werden gestoppt, keine Zombie-Prozesse mehr

    ---

    ## 🎨 Verbesserungen an der Oberfläche

    ### Hauptfenster
    - **Fensterhöhe** dynamisch an Bildschirm angepasst (max. 90 % der Bildschirmhöhe)
    - **Status-Label** zweizeilig mit Umbruch für längere Meldungen
    - **Einheitliche Schriftgröße** (14 px) für alle Aktionsbuttons
    - **Bessere Sichtbarkeit** durch konsistente Farbgebung

    ### Dialog „Zeitgesteuertes Herunterfahren"
    - **Scrollbereich** für kleine Bildschirme – nichts wird abgeschnitten
    - **Fixierte Buttons** (Abbrechen/Speichern) – immer sichtbar
    - **Große Icons** für Ziel (🎯), Zeit (🕐) und caffeinate (☕)
    - **Vorschau-Kasten** mit Wochentag-Hinweis (heute / morgen / in X Tagen)
    - **Lern-Fact** zur caffeinate-Nutzung im Terminal

    ### Einstellungen
    - **Neue Sektion** „Sprachausgabe aktiviert" mit Checkbox
    - **Neue Sektion** „Gespeichertes Passwort löschen" mit Reset-Button
    - **Konsistente Reihenfolge** aller Bereiche

    ### Info-Dialog
    - **Icons** für Version, Copyright, Lizenz und Drittanbieter
    - **Automatische Update-Prüfung** jetzt max. 1× pro 24 Stunden (statt bei jedem Start)

    ---

    ## 🌐 Übersetzungen

    - **17 Sprachen** vollständig gepflegt:
    - 🇩🇪 Deutsch, 🇬🇧 English, 🇸🇦 العربية, 🇨🇿 Čeština, 🇬🇷 Ελληνικά,
    - 🇪🇸 Español, 🇫🇷 Français, 🇮🇹 Italiano, 🇳🇱 Nederlands, 🇳🇴 Norsk,
    - 🇵🇱 Polski, 🇵🇹 Português, 🇷🇺 Русский, 🇫🇮 Suomi, 🇸🇪 Svenska,
    - 🇹🇷 Türkçe, 🇻🇳 Tiếng Việt
    - **Alle MessageBoxen** mit übersetzten Ja/Nein-Buttons
    - **Fallback auf Englisch** funktioniert jetzt auch bei einzelnen fehlenden Keys
    - **Tooltips** werden bei Sprachwechsel korrekt aktualisiert

    ---

    ## 🔧 Interne Verbesserungen

    - **DRY-Refactor** der NOPASSWD-Prüfung in eine zentrale Methode
    - **`_start_auto_timer_safe()`** – zentraler, geschützter Auto-Timer-Start
    - **Konsolidierte `closeEvent`**-Methoden in allen Dialogen
    - **Vereinheitlichte `say_message()`** mit Wait-Modus für saubere Ansagen
    - **Log-Rotation** jetzt zusätzlich größenbasiert
    - **Update-Check-Zeitstempel** in `~/Library/Application Support/AnyNasPy/last_update_check.txt`

    ---

    ## 🐛 Behobene Fehler

    - **Auto-Timer** feuerte während eines aktiven Zeitgebers (Kollision zweier Timer)
    - **Falsche Meldung** „Shutdown-Timer läuft" wurde für Coffee-Timer angezeigt
    - **Falsche Sprachausgabe** „Mac und NAS werden heruntergefahren", obwohl Coffee-Timer aktiv war
    - **Doppelter Code** in `handleChoice("mac_only")`, `nas_only` und `cancel`
    - **Fehlendes `return`** in `handleChoice("cancel")` nach „Nein"-Klick
    - **Pause-Button** zeigte „Play" an, funktionierte aber nicht (jetzt echte Pause)
    - **Zentrale Sprachausgabe** wurde bei zu schneller Folge unterdrückt (jetzt nur bei identischen Nachrichten)
    - **Eject-Warnung** kam fälschlich bei `home`/`homes`
    - **Startup-Dialog** akzeptierte Yes/No statt lokalisierter Buttons
    - **Zielwert-Mismatch** `"nothing"` vs. `"coffee"` im Code behoben

    ---

    ## ⚠️ Wichtige Hinweise

    ### Für Nutzer mit vorheriger NOPASSWD-Regel
    - Die Regel bleibt gültig, keine Änderung nötig.

    ### Für neue Nutzer
    - Beim ersten Start kann ein **Admin-Passwort** eingerichtet werden
    - Das Passwort wird **sicher im macOS-Schlüsselbund** gespeichert
    - **Kein Terminal-Setup** erforderlich

    ### Für Nutzer mit Sprachausgabe
    - Die Sprachausgabe kann in den **Einstellungen** deaktiviert werden
    - Stimmen werden **automatisch** basierend auf der aktuellen Sprache gewählt
    - Fehlende Stimmen können in **Systemeinstellungen → Bedienungshilfen → Gesprochene Inhalte** installiert werden

    ---

    ## 📦 Installation

    **Voraussetzungen:**
    - macOS 11 (Big Sur) oder neuer
    - Python 3.8+
    - PyQt5
    - Bei Erstinstallation: SSH-Key-Zugang zum NAS einrichten

    **Update von einer früheren Version:**
    - Einfach `Synaspy_07.py` ersetzen
    - Einstellungen und Profile bleiben erhalten

Version 2.1.0
    ERWEITERT: Mehrere Server-Profile verwalten
    · Server-Profile für mehrere NAS-Server
    · Schnelles Umschalten zwischen Profilen
    · Profil-Dropdown in der Hauptoberfläche
    · Profilverwaltung im Einstellungsdialog
    · Unbegrenzte Anzahl von Servern möglich (praktisch 10-20)
    · Volle Rückwärtskompatibilität
    · 17 Sprachen: Full UI translation (Deutsch, English, Español, Français, Ελληνικά, Italiano, Nederlands, Norsk, Polski, Português, Русский, Suomi, Svenska, Türkçe, Tiếng Việt, Čeština, العربية).

    Einstellungsdialog: Zugriff über Zahnrad-Button oder Cmd+E
    · NAS-Benutzername, DNS, IP, MAC
    · SSH-Key Pfad (SSH-Key Hilfe mit Erklärung, was zu tun ist)
    · Volume-Liste (mit Haupt-Volume an oberster Stelle)
    · Auto-Shutdown/Start Verzögerung
    · WOL und SMB Wartezeiten
    · Mount-Wiederholungen
    · Zeiteinstellungen: Alle Timeouts und Verzögerungen
    · Pfad zur Statusdatei
    · Server-Profile verwalten (neu)
    · Sprachauswahl (neu im Config Dialog)

    Speichert die Konfiguration in zwei Formaten:
    1. QSettings: Für plattformübergreifende Kompatibilität
    2. JSON-Datei (~/Library/Application Support/AnyNasPy/config.json): Für einfache manuelle Bearbeitung. (Die JSON-Datei hat Vorrang vor QSettings, falls beide vorhanden sind.)
    3. Server-Profile: (~/Library/Application Support/AnyNasPy/server_profiles.json) (neu)

    Kompatibilität
    · Funktioniert auf Intel und Apple Silicon Macs
"""

"""LICENSES
    MIT License

    Copyright (c) 2026 BinhDiez

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    ---

    This software uses PyQt5, which is Copyright (c) Riverbank Computing Limited.

    PyQt5 is free software: you can redistribute it and/or modify it under the
    terms of the GNU General Public License as published by the Free Software
    Foundation, either version 3 of the License, or (at your option) any later
    version.

    PyQt5 is distributed in the hope that it will be useful, but WITHOUT ANY
    WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
    FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
    details.

    You should have received a copy of the GNU General Public License along with
    PyQt5. If not, see <http://www.gnu.org/licenses/>.
"""

import getpass
import json
import os
import platform
import re
import signal
import socket
import urllib.request
import subprocess
import sys
import textwrap
import threading
import time
import traceback
import atexit
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

from PyQt5.QtCore import (
    Q_ARG,
    QMetaObject,
    QSettings,
    Qt,
    QTimer,
    pyqtSlot,
    QUrl,
)
from PyQt5.QtGui import QIcon, QPixmap, QDesktopServices
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QComboBox,
    QDesktopWidget,
    QDialog,
    QFileDialog,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpinBox,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QListWidgetItem,
    QSplitter,
    QInputDialog,
)

# =======================================
# MACOS KEYCHAIN HELPER
# =======================================


class MacKeychainHelper:
    """
    Hilfsklasse für den Zugriff auf den macOS-Schlüsselbund.
    Speichert und liest Passwörter verschlüsselt.

    Verwendet das 'security'-Kommando, das auf jedem macOS
    standardmäßig vorhanden ist.
    """

    # Eindeutiger Service-Name im Keychain
    SERVICE_NAME = "AnyNasPy-AdminPassword"
    ACCOUNT_NAME = "synaspy-admin"

    @classmethod
    def store_password(cls, password: str) -> bool:
        """
        Speichert das Passwort im macOS-Schlüsselbund.
        Überschreibt einen vorhandenen Eintrag.
        """
        try:
            # -U = update existing entry
            # -w = password (wird im Klartext übergeben, aber nur lokal, kein Log)
            cmd = [
                "security", "add-generic-password",
                "-s", cls.SERVICE_NAME,
                "-a", cls.ACCOUNT_NAME,
                "-w", password,
                "-U",
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,
                # Wichtig: Kein stdout/stderr in Logs schreiben!
            )
            return result.returncode == 0
        except Exception:
            return False

    @classmethod
    def get_password(cls) -> str:
        """
        Liest das Passwort aus dem macOS-Schlüsselbund.
        Gibt None zurück wenn nicht vorhanden.
        """
        try:
            cmd = [
                "security", "find-generic-password",
                "-s", cls.SERVICE_NAME,
                "-a", cls.ACCOUNT_NAME,
                "-w",   # nur das Passwort ausgeben
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
            return None
        except Exception:
            return None

    @classmethod
    def delete_password(cls) -> bool:
        """Löscht das gespeicherte Passwort aus dem Schlüsselbund."""
        try:
            cmd = [
                "security", "delete-generic-password",
                "-s", cls.SERVICE_NAME,
                "-a", cls.ACCOUNT_NAME,
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,
            )
            # returncode 0 = erfolgreich gelöscht
            # returncode 44 = Eintrag existierte nicht → auch ok
            return result.returncode in (0, 44)
        except Exception:
            return False

    @classmethod
    def has_password(cls) -> bool:
        """Prüft, ob ein Passwort gespeichert ist."""
        return cls.get_password() is not None


# =======================================
# LANGUAGE MANAGER
# =======================================


class LanguageManager:
    """Verwaltet die Mehrsprachigkeit der Anwendung."""

    # Verfügbare Sprachen mit Flaggen
    LANGUAGES = {
        "ar": "🇸🇦 العربية",  # Arabisch
        "cs": "🇨🇿 Čeština",  # Tschechisch
        "de": "🇩🇪 Deutsch",
        "el": "🇬🇷 Ελληνικά",  # Griechisch
        "en": "🇬🇧 English",
        "es": "🇪🇸 Español",
        "fr": "🇫🇷 Français",
        "it": "🇮🇹 Italiano",
        "nl": "🇳🇱 Nederlands",
        "no": "🇳🇴 Norsk",
        "pl": "🇵🇱 Polski",
        "pt": "🇵🇹 Português",
        "ru": "🇷🇺 Русский",  # Russisch
        "fi": "🇫🇮 Suomi",  # Finnisch
        "sv": "🇸🇪 Svenska",
        "tr": "🇹🇷 Türkçe",
        "vi": "🇻🇳 Tiếng Việt",
    }

    # Übersetzungen
    TRANSLATIONS = {
        # "🇸🇦 Arabisch"
        "ar": {
            "language": "اللغة:",
            "window_title": "إدارة NAS",
            "status_checking": "جاري التحقق من اتصال الخادم...",
            "status_online": "خادم NAS متصل ✓",
            "status_offline": "خادم NAS غير متصل",
            "status_settings": "فتحت الإعدادات - تم إيقاف المؤقت",
            "status_settings_saved": "تم حفظ الإعدادات",
            "status_settings_cancelled": "تم إلغاء الإعدادات",
            "status_shutdown": "جاري إيقاف تشغيل NAS و Mac...",
            "status_shutdown_nas": "جاري إيقاف تشغيل NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ تم إرسال أمر إيقاف NAS، سيتم إيقاف Mac الآن...",
            "status_shutdown_nas_failed_mac_still": "⚠️ فشل إيقاف NAS، جاري إيقاف Mac...",
            "status_starting": "جاري تشغيل NAS عبر Wake-on-LAN...",
            "status_waiting": "في انتظار بدء الخادم...",
            "status_wol_sent": "تم إرسال الحزمة السحرية",
            "status_wol_failed": "فشل WOL",
            "status_mounting": "جاري تركيب وحدات التخزين المحددة...",
            "status_mounting_volume": "جاري تركيب {}...",
            "status_mounted": "تم تركيب {} ✓",
            "status_unmounting": "جاري فك تركيب {}...",
            "status_unmounted": "تم فك تركيب {} ✓",
            "status_error": "خطأ: تعذر تركيب {}",
            "status_error_unmount": "خطأ: تعذر فك تركيب {}",
            "status_all_mounted": "تم تركيب جميع وحدات التخزين ✓",
            "status_all_unmounted": "تم فك تركيب جميع وحدات التخزين ✓",
            "status_mount_all": "جاري تركيب جميع وحدات التخزين...",
            "status_unmount_all": "جاري فك تركيب جميع وحدات التخزين...",
            "status_shutdown_cmd": "تم إرسال أمر إيقاف NAS ✓",
            "status_timeout": "انتهت المهلة - تعذر بدء الخادم",
            "status_no_volumes": "لا توجد وحدات تخزين مركبة",
            "status_mount_failed": "فشل التركيب",
            "status_cancelled": "تم الإلغاء - سيتم إغلاق التطبيق",
            "status_esc": "تم الضغط على ESC - سيتم إغلاق التطبيق",
            "status_server_online": "الخادم متصل - في انتظار خدمة SMB...",
            "status_profile_changed": "تم التبديل إلى الملف الشخصي: {}",
            "status_switching": "جاري التبديل إلى الملف الشخصي: {}...",
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "إلغاء",
            "btn_start_nas": "تشغيل NAS",
            "btn_settings": "الإعدادات (Cmd+E)",
            "btn_select_all": "الكل",
            "btn_save": "حفظ",
            "btn_reset": "إعادة تعيين",
            "btn_info": "ℹ",
            "btn_profile": "الملفات الشخصية",
            "tooltip_shutdown_both": "إيقاف Mac و NAS خلال دقيقتين",
            "tooltip_shutdown_nas": "إيقاف NAS فقط",
            "tooltip_cancel": "إغلاق التطبيق",
            "tooltip_start_nas": "تشغيل NAS عبر Wake-on-LAN",
            "tooltip_settings": "الإعدادات (Cmd+E)",
            "timer_shutdown": "إيقاف تلقائي بعد {} ثانية - ENTER لإيقاف NAS فقط",
            "timer_start": "بدء تلقائي بعد {} ثانية - ENTER للبدء الفوري",
            "volumes_title": "وحدات التخزين المتاحة",
            "volumes_title_offline": "تركيب وحدات التخزين عند البدء",
            "volumes_hint": "ملاحظة: تُعتبر أول وحدة تخزين في القائمة تلقائيًا وحدة رئيسية ولا يمكن تعطيلها.",
            "volumes_mount_tooltip": "تُركب تلقائيًا عند بدء الخادم",
            "config_title": "AnyNasPy - الإعدادات",
            "config_tab_profiles": "ملفات تعريف الخادم",
            "config_tab_general": "عام",
            "config_tab_volumes": "وحدات التخزين",
            "config_tab_timing": "إعدادات التوقيت",
            "config_language": "اللغة:",
            "config_nas_group": "إعدادات خادم NAS",
            "config_nas_user": "اسم المستخدم:",
            "config_nas_dns": "اسم DNS:",
            "config_nas_ip": "عنوان IP:",
            "config_nas_mac": "عنوان MAC:",
            "config_ssh_key": "مسار مفتاح SSH:",
            "config_volumes_group": "وحدات التخزين",
            "config_volumes_label": "وحدات التخزين (اسم واحد في كل سطر):",
            "config_time_group": "إعدادات التوقيت (بالثواني)",
            "config_auto_shutdown": "تأخير الإيقاف التلقائي:",
            "config_auto_start": "تأخير البدء التلقائي:",
            "config_wol_wait": "مدة انتظار WOL (الحد الأقصى):",
            "config_smb_wait": "مدة انتظار SMB:",
            "config_mount_retries": "عدد محاولات التركيب:",
            "config_status_file": "ملف الحالة",
            "config_json_path": "ملف تكوين JSON:",
            "config_profile_name": "اسم الملف الشخصي:",
            "config_profile_active": "الملف الشخصي النشط",
            "config_profile_set_active": "تعيين كملف شخصي نشط",
            "config_profile_list": "الملفات الشخصية الموجودة:",
            "config_profile_new": "ملف شخصي جديد",
            "config_profile_delete": "حذف الملف الشخصي",
            "config_profile_duplicate": "نسخ الملف الشخصي",
            "config_profile_rename": "إعادة تسمية",
            "config_profile_required": "اسم الملف الشخصي مطلوب.",
            "config_profile_exists": "يوجد بالفعل ملف شخصي بهذا الاسم.",
            "config_profile_deleted": "تم حذف الملف الشخصي '{}'.",
            "config_profile_duplicated": "تم نسخ الملف الشخصي '{}' كـ '{}'.",
            "config_profile_renamed": "تمت إعادة تسمية الملف الشخصي إلى '{}'.",
            "config_profile_activated": "الملف الشخصي '{}' نشط الآن.",
            "config_find_ip": "🔍 البحث عن IP",
            "config_find_ip_tooltip": "البحث التلقائي عن IP الخادم في الشبكة",
            "config_ssh_help": "? مساعدة",
            "config_mac_help": "? مساعدة",
            "config_mac_help_tooltip": "إرشادات للعثور على عنوان MAC",
            "msg_ip_found": "تم العثور على IP الخادم بنجاح:\n\n{}\n\nتم إدخال IP في الحقل.",
            "msg_ip_not_found": "تعذر العثور تلقائيًا على IP الخادم.\n\nيرجى إدخال عنوان IP يدويًا.\n\nنصائح:\n• تحقق من اسم DNS في الإعدادات\n• تأكد من أن NAS قيد التشغيل\n• يمكنك العثور على IP في واجهة DSM ضمن 'النظام > الشبكة'",
            "msg_reset_confirm": "هل تريد إعادة تعيين جميع الإعدادات إلى القيم الافتراضية؟",
            "msg_reset_title": "إعادة تعيين",
            "msg_reset_done": "تمت إعادة تعيين جميع الإعدادات إلى القيم الافتراضية.",
            "msg_delete_confirm": "هل أنت متأكد من حذف الملف الشخصي '{}'؟",
            "msg_delete_title": "حذف الملف الشخصي",
            "msg_no_active_profile": "لم يتم تحديد ملف شخصي نشط.",
            "info_title": "حول AnyNasPy",
            "info_version": "الإصدار",
            "info_copyright": "حقوق النشر",
            "info_license": "الترخيص",
            "info_impressum": "بيانات النشر",
            "info_developer": "المطور",
            "info_contact": "الاتصال",
            "info_license_text": "رخصة MIT",
            "say_timer_shutdown": "إيقاف تلقائي لـ Mac و NAS بعد {} ثانية - Enter لإيقاف NAS فقط - Escape للإلغاء",
            "say_timer_start": "سيتم تشغيل خادم NAS بعد {} ثانية - Enter للتشغيل الفوري",
            "say_server_online": "خادم NAS متاح",
            "say_server_offline": "خادم NAS غير متصل",
            "say_shutdown_started": "بدأ الإيقاف",
            "say_nas_shutdown": "جاري إيقاف NAS",
            "say_starting_nas": "جاري تشغيل NAS",
            "say_cancelled": "تم الإلغاء",
            "say_waiting_server": "في انتظار بدء الخادم",
            "say_wol_failed": "خطأ في الإرسال",
            "say_server_reachable": "الخادم متاح",
            "say_mount_volume": "{} جاهز",
            "say_unmount_volume": "جاري فك تركيب {}",
            "say_mount_all": "تركيب جميع وحدات التخزين",
            "say_unmount_all": "فك تركيب جميع وحدات التخزين",
            "say_mount_error": "خطأ في التركيب",
            "say_unmount_error": "خطأ في فك التركيب",
            "say_mount_failed": "لم يتم تركيب أي وحدات تخزين",
            "say_settings_opened": "تم فتح الإعدادات",
            "say_settings_saved": "تم حفظ الإعدادات",
            "say_settings_cancelled": "تم إلغاء الإعدادات",
            "say_workaround_deleted": "تم حذف ملف الحل البديل",
            "say_server_timeout": "انتهت مهلة بدء الخادم",
            "say_profile_changed": "تم التبديل إلى الملف الشخصي {}",
            "ssh_key_create_title": "إنشاء مفتاح SSH",
            "ssh_key_create_question": "هل تريد إنشاء زوج مفاتيح SSH جديد؟",
            "ssh_key_create_existing": "مفتاح SSH '{}' موجود بالفعل.\nهل تريد استبداله؟",
            "ssh_key_create_comment": "تعليق لمفتاح SSH (اختياري):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "تم إنشاء مفتاح SSH: {}",
            "ssh_key_create_error": "خطأ أثناء إنشاء مفتاح SSH",
            "ssh_key_create_timeout": "انتهت مهلة إنشاء المفتاح",
            "ssh_key_create_failed": "أرجع ssh-keygen خطأ:\n{}",
            "ssh_key_create_passphrase": "عبارة مرور لمفتاح SSH (اترك فارغًا بدون عبارة مرور):",
            "ssh_key_create_passphrase_confirm": "تأكيد عبارة المرور:",
            "ssh_key_create_passphrase_mismatch": "عبارات المرور غير متطابقة.",
            "ssh_key_create_info": "✅ تم إنشاء زوج مفاتيح SSH بنجاح:\n\n"
            "📁 المفتاح الخاص: {}\n"
            "📁 المفتاح العام: {}\n\n"
            "📋 المفتاح العام للنسخ:\n"
            "{}\n\n"
            "🔑 كيفية تثبيت المفتاح على NAS:\n"
            "1. انسخ المفتاح العام (أعلاه)\n"
            "2. ألصقه في الملف:\n"
            "   ~/.ssh/authorized_keys على NAS\n"
            "3. أو استخدم:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "يرجى إدخال اسم ملف آخر:",
            "ssh_key_exists_also": "المفتاح '{}' موجود أيضًا.\nيرجى حذفه أولاً أو اختيار اسم آخر.",
            "ssh_key_passphrase_title": "عبارة المرور",
            "ssh_key_passphrase_question": "هل تريد استخدام عبارة مرور لمفتاح SSH؟\n\nبدون عبارة مرور: اتصال تلقائي ممكن، أقل أمانًا.\nمع عبارة مرور: أكثر أمانًا، ولكن يتطلب إدخالًا في كل اتصال.",
            "ssh_key_passphrase_enter": "إدخال عبارة المرور",
            "ssh_key_passphrase_label": "عبارة المرور لمفتاح SSH (على الأقل 4 أحرف):",
            "ssh_key_passphrase_none": "بدون عبارة مرور",
            "ssh_key_passphrase_none_question": "لم تدخل عبارة مرور.\nهل تريد إنشاء المفتاح بدون عبارة مرور؟",
            "ssh_key_passphrase_short": "عبارة المرور قصيرة جدًا",
            "ssh_key_passphrase_short_message": "يجب أن تتكون عبارة المرور من 4 أحرف على الأقل.",
            "ssh_key_passphrase_confirm": "تأكيد عبارة المرور",
            "ssh_key_passphrase_confirm_label": "أدخل عبارة المرور مرة أخرى:",
            "ssh_key_passphrase_mismatch_title": "خطأ في عبارة المرور",
            "ssh_key_passphrase_mismatch_message": "عبارات المرور غير متطابقة.",
            "config_ssh_open": "فتح",
            "config_ssh_open_tooltip": "اختيار مفتاح SSH أو فتح المجلد",
            "config_ssh_create": "إنشاء",
            "config_ssh_create_tooltip": "إنشاء زوج مفاتيح SSH جديد",
            "config_ssh_help_tooltip": "عرض المساعدة حول مفتاح SSH",
            "config_ssh_select": "اختيار مفتاح SSH",
            "config_json_open": "فتح",
            "config_json_open_tooltip": "فتح مجلد تكوين JSON",
            "config_error": "خطأ",
            "config_shutdown_mac_delay": "مدة الانتظار بين إيقاف NAS و Mac:",
            "info_third_party": "مكتبات الطرف الثالث",
            "info_pyqt5_license": "يستخدم هذا التطبيق PyQt5 المرخص بموجب رخصة GNU General Public License v3 (GPLv3).\nحقوق النشر (c) Riverbank Computing Limited.\n\nيمكن الاطلاع على النص الكامل للرخصة على https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "اكتشاف وحدات التخزين",
            "volumes_add": "إضافة",
            "volumes_delete": "حذف",
            "volumes_move_up": "نقل لأعلى",
            "volumes_move_down": "نقل لأسفل",
            "volumes_available": "وحدات التخزين المتاحة:",
            "volumes_no_volumes": "لم يتم العثور على وحدات تخزين.",
            "volumes_detection_failed": "فشل في اكتشاف وحدات التخزين.",
            "volumes_detection_success": "تم اكتشاف وحدات التخزين بنجاح.",
            "volumes_confirm_delete": "هل تريد حقًا حذف وحدة التخزين '{}'؟",
            "volumes_enter_name": "الرجاء إدخال اسم وحدة التخزين الجديدة:",
            "volumes_name_exists": "توجد بالفعل وحدة تخزين بهذا الاسم.",
            "msg_invalid_ip": "عنوان IP المدخل غير صالح.\nالرجاء إدخال عنوان IPv4 صالح (مثال: 192.168.1.100).",
            "msg_select_volume": "الرجاء تحديد وحدة تخزين.",
            "msg_cannot_delete_main_volume": "لا يمكن حذف وحدة التخزين الأولى (وحدة التخزين الرئيسية).",
            "profile_cannot_delete_last": "لا يمكن حذف الملف الشخصي الأخير.",
            "status_wol_sending": "جاري إرسال الحزمة السحرية...",
            "status_wol_method_failed": "فشلت طريقة Python، جاري تجربة الطريقة التالية...",
            "status_trying_wakeonlan": "جاري تجربة wakeonlan...",
            "status_trying_etherwake": "جاري تجربة etherwake...",
            "ssh_key_system_key_warning": "تحذير أمني",
            "ssh_key_system_key_message": "الاسم '{}' هو مفتاح نظام ولن يتم استبداله.\nالرجاء اختيار اسم آخر (مثال: synaspy_rsa).",
            "profile_name_exists": "يوجد بالفعل ملف شخصي بالاسم '{}'.",
            "config_profile_created": "تم إنشاء الملف الشخصي '{}'.",
            "config_profile_create_failed": "فشل إنشاء الملف الشخصي.",
            "config_profile_rename_failed": "فشل إعادة التسمية.",
            "config_profile_duplicate_name": "اسم للملف الشخصي المكرر:",
            "config_profile_duplicate_failed": "فشل النسخ المكرر.",
            "config_profile_delete_failed": "فشل الحذف.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "يُغلق جهاز Mac فقط (يبقى NAS قيد التشغيل، بدون WOL)",
            "status_shutdown_mac_only": "جارٍ إغلاق جهاز Mac فقط...",
            "say_shutdown_mac_only": "يتم إغلاق جهاز Mac، ويبقى NAS قيد التشغيل",

            "btn_scheduled_shutdown": "🕐 إغلاق مجدول",
            "tooltip_scheduled_shutdown": "يُغلق بعد مدة يختارها المستخدم",
            "btn_scheduled_shutdown_offline": "🕐 إغلاق جهاز Mac بشكل مجدول",
            "tooltip_scheduled_shutdown_offline": "يُغلق جهاز Mac فقط بعد مدة محددة (NAS غير متصل)",
            "btn_cancel_scheduled": "⏹ إلغاء العد التنازلي",
            "tooltip_cancel_scheduled": "يُلغي العد التنازلي النشط",

            "sched_dialog_title": "إغلاق مجدول",
            "sched_target_label": "الهدف:",
            "sched_target_both": "🖥️ Mac + NAS  (إغلاق كامل)",
            "sched_target_nas": "🗄️ NAS فقط  (يبقى Mac قيد التشغيل)",
            "sched_target_mac": "💻 Mac فقط  (يبقى NAS قيد التشغيل)",

            "sched_wait_label": "مدة الانتظار حتى الإغلاق:",
            "sched_hours": "ساعات",
            "sched_minutes": "دقائق",

            "sched_caffeinate_label": "خيار caffeinate (يبقي جهاز Mac مستيقظًا):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "موصى به: النظام مستيقظ، يمكن للشاشة أن تُعتِم  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "منع الخمول والقرص فقط (تبقى الشاشة مضاءة)  (-i -m)",
            "sched_caffeinate_d": "تبقى الشاشة مضاءة أيضًا  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "محاكاة نشاط المستخدم (شاشة مضيئة، نظام مستيقظ)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "الحد الأقصى: الشاشة + النظام + القرص مستيقظة باستمرار  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "إيقاف (توفير طاقة عادي – يمكن للنظام أن ينام)",

            "sched_caffeinate_hint": (
                "💡 معلومة تعليمية: استخدم علامات caffeinate مباشرةً في الطرفية:\n"
                "   -i  يمنع خمول النظام\n"
                "   -m  يمنع خمول القرص (القرص الصلب لا ينام)\n"
                "   -s  يمنع خمول النظام (فقط عند توصيل الطاقة)\n"
                "   -d  يمنع خمول الشاشة (تبقى الشاشة مضاءة)\n"
                "   -u  يحاكي نشاط المستخدم (تبقى الشاشة مضيئة)\n"
                "   -w PID  ينهي caffeinate عند انتهاء العملية PID\n"
                "مثال:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "تم جدولة الإغلاق في: {}",
            "sched_countdown_label": "العد التنازلي: {} حتى الإغلاق ({})",
            "sched_started": "تم بدء المؤقّت.\n\nالهدف: {}\nالمدة: {}\nالنهاية: {}",
            "sched_cancelled": "تم إلغاء المؤقّت",
            "sched_already_active": "يوجد مؤقّت قيد التشغيل بالفعل. هل تريد إلغاءه أولًا؟",
            "sched_invalid_time": "يرجى إدخال مدة صالحة (دقيقة واحدة على الأقل).",
            "sched_max_time": "الحد الأقصى المسموح 720 ساعة (30 يومًا).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "تم بدء المؤقّت. سيتم إغلاق Mac و NAS خلال {}."
            ),
            "sched_voice_started_nas": (
                "تم بدء المؤقّت. سيتم إغلاق NAS فقط خلال {}. "
                "سيبقى Mac قيد التشغيل."
            ),
            "sched_voice_started_mac": (
                "تم بدء المؤقّت. سيتم إغلاق Mac فقط خلال {}. "
                "سيبقى NAS قيد التشغيل."
            ),
            "sched_voice_started_nothing": (
                "تم بدء المؤقّت. لن يتم تنفيذ أي شيء عند انتهاء المدة. "
                "سيبقى caffeinate نشطًا حتى ذلك الحين."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "سيبقى Mac مستيقظًا لمدة {}. "
                "يمكن للشاشة أن تُعتِم. "
                "لن يتم تنفيذ أي شيء عند انتهاء المدة."
            ),
            "sched_voice_nothing_im": (
                "سيبقى Mac مستيقظًا لمدة {}. "
                "ستبقى الشاشة مضاءة. "
                "لن يتم تنفيذ أي شيء عند انتهاء المدة."
            ),
            "sched_voice_nothing_d": (
                "سيبقى Mac والشاشة مضاءين لمدة {}. "
                "لن يتم تنفيذ أي شيء عند انتهاء المدة."
            ),
            "sched_voice_nothing_u": (
                "سيبقى Mac نشطًا لمدة {}. "
                "ستبقى الشاشة مضيئة. "
                "لن يتم تنفيذ أي شيء عند انتهاء المدة."
            ),
            "sched_voice_nothing_full": (
                "سيبقى Mac نشطًا بالكامل لمدة {} – الشاشة والنظام مستيقظان باستمرار. "
                "لن يتم تنفيذ أي شيء عند انتهاء المدة."
            ),
            "sched_voice_nothing_off": (
                "سيعمل المؤقّت لمدة {}. "
                "لن يتم تنفيذ أي شيء عند انتهاء المدة. "
                "تنبيه: قد ينتقل Mac إلى وضع السكون."
            ),
            "sched_voice_cancelled": "تم إلغاء المؤقّت",
            "sched_caffeinate_failed": "تعذّر تشغيل caffeinate:\n{}",
            "sched_target_required": "يرجى اختيار هدف.",
            "sched_tooltip_active": "المؤقّت قيد التشغيل – انقر للإلغاء",

            "status_scheduled_active": "المؤقّت نشط - {} متبقٍ",
            "status_scheduled_triggered": "انتهى المؤقّت - جارٍ بدء {}",
            "status_scheduled_cancelled": "تم إلغاء المؤقّت",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "المؤقّت نشط",
            "close_blocked_text": (
                "<b>لا يزال هناك مؤقّت قيد التشغيل!</b><br><br>"
                "مجدول: {}<br>"
                "المتبقي: <b>{}</b><br>"
                "في: {}<br><br>"
                "إذا أغلقت الآن، فلن يتم تنفيذ الإغلاق المجدول "
                "<b>بعد الآن</b>."
            ),
            "close_blocked_yes": "إغلاق على أي حال",
            "close_blocked_no": "إبقاء التطبيق قيد التشغيل",
            "close_blocked_cancel_text": (
                "لا يزال هناك مؤقّت قيد التشغيل.\n\n"
                "هل تريد فعلًا إغلاق التطبيق؟\n"
                "(سيتم عندئذٍ تجاهل الإغلاق المجدول.)"
            ),
            "close_blocked_log_aborted": "تم إلغاء الإغلاق (المؤقّت نشط)",
            "close_blocked_log_discarded": (
                "يتم إغلاق التطبيق على الرغم من المؤقّت النشط – تم تجاهل المؤقّت"
            ),
            "close_blocked_log_cancel_aborted": (
                "تم إلغاء إغلاق التطبيق عبر زر الإلغاء"
            ),
            "duration_day": "يوم",
            "duration_days": "أيام",
            "duration_hour": "ساعة",
            "duration_hours": "ساعات",
            "duration_minute": "دقيقة",
            "duration_minutes": "دقائق",
            "duration_connector_and": "و",
            "tooltip_pause_timer": "إيقاف مؤقت / استئناف المؤقت",
            "tooltip_stop_timer": "إيقاف المؤقت بالكامل",
            "tooltip_stop_timer_inactive": "لا يوجد مؤقت نشط",
            "timer_stopped_notice": "⏹ تم إيقاف المؤقت – جاهز لإعادة التشغيل",
            "say_timer_stopped": "تم إيقاف المؤقت",
            "say_timer_restarted": "تمت إعادة تشغيل المؤقت",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "مُصنّع NAS:",
            "vendor_tooltip": (
                "اختر مُصنّع NAS الخاص بك. يحدد أوامر الإيقاف والمسارات "
                "الافتراضية. 'الكشف التلقائي' يفحص NAS عبر SSH."
            ),
            "vendor_auto_detect": "🔄 الكشف التلقائي",
            "vendor_auto_detect_tooltip": (
                "الكشف التلقائي عن المُصنّع عبر SSH. "
                "الشرط: مفتاح SSH وعنوان IP مُهيّآن بشكل صحيح."
            ),
            "vendor_detect_in_progress": "🔄 جارٍ الكشف...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "لينكس عام",
            "vendor_macos_server": "خادم macOS",
            "vendor_windows_server": "خادم Windows",
            "vendor_custom": "مخصّص",
            "vendor_custom_hint": (
                "مخصّص: اضبط أوامر الإيقاف يدويًا. "
                "الافتراضي: 'sudo shutdown -h now' (يعمل على "
                "80% من أجهزة NAS التي تعمل بنظام لينكس)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "تم التعرّف على المُصنّع: {}",
            "vendor_detect_success_question": (
                "تم التعرّف على المُصنّع: {}\n\n"
                "هل تريد اعتماد هذا المُصنّع؟\n"
                "(القيمة الحالية: {})"
            ),
            "vendor_detect_failed": (
                "تعذّر التعرّف التلقائي على المُصنّع.\n\n"
                "يُرجى الاختيار يدويًا. معظم أجهزة NAS التي تعمل "
                "بلينكس تعمل مع 'لينكس عام'."
            ),
            "vendor_detect_no_ssh": (
                "يتطلب الكشف التلقائي الوصول عبر SSH.\n\n"
                "يُرجى التحقق من:\n"
                "• مسار مفتاح SSH صحيح\n"
                "• عنوان IP صحيح\n"
                "• SSH مُفعّل على NAS\n"
                "• مفتاح SSH مُثبّت على NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "يُرجى إدخال مفتاح SSH وعنوان IP أولاً."
            ),
            "vendor_detect_nas_offline": (
                "خادم NAS لا يستجيب.\n\n"
                "يُرجى التحقق من:\n"
                "• هل NAS قيد التشغيل؟\n"
                "• هل عنوان IP صحيح؟\n"
                "• هل NAS على نفس الشبكة؟\n\n"
                "شغّل NAS وحاول مرة أخرى."
            ),
            "vendor_detect_error": "خطأ أثناء الكشف التلقائي:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "لم يتم العثور على مفتاح SSH:\n\n{}\n\n"
                "يُرجى التحقق من المسار في الإعدادات."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "أمر الإيقاف:",
            "custom_cmd_tooltip": (
                "الأمر الذي يُرسل إلى NAS عبر SSH. "
                "افصل بين الأوامر المتعددة بفاصلة منقوطة."
            ),
            "custom_cmd_hint": (
                "💡 افصل بين الأوامر المتعددة بفاصلة منقوطة — "
                "سيُستخدم أول أمر ناجح. "
                "مثال: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "عرض المساعدة حول أوامر الإيقاف",
            "custom_cmd_help_title": "أوامر الإيقاف الشائعة",
            "custom_cmd_help_text": (
                "<h3>أوامر الإيقاف الشائعة حسب المُصنّع</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>لينكس (عام):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>خادم Windows:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>أوامر متعددة (سلسلة احتياطية)</h4>"
                "<p>إذا فشل الأمر الأول، يُجرَّب الأمر التالي. "
                "افصل بينها بفاصلة منقوطة:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>نصيحة:</b> اختر أولاً الأمر الأكثر احتمالاً، "
                "ثم البدائل كخطة احتياطية.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 جارٍ الكشف عن وحدات التخزين عبر SSH...",
            "volumes_detection_via_paths": (
                "🔍 البحث في المسارات الخاصة بالمُصنّع..."
            ),
            "volumes_detection_via_smb": (
                "🔍 بديل: البحث عبر smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 جارٍ البحث عن وحدات التخزين عبر SSH... قد يستغرق "
                "البحث بضع ثوانٍ."
            ),
            "volumes_detect_panel_success": (
                "تم العثور على {} وحدة تخزين — تمت إضافة {} جديدة، "
                "{} موجودة مسبقًا"
            ),
            "volumes_detect_panel_partial": (
                "تم العثور على {} وحدة تخزين — جميعها موجودة مسبقًا في القائمة"
            ),
            "volumes_detect_panel_failed": (
                "لم يتم العثور على أي وحدة تخزين. "
                "يُرجى إدخال وحدات التخزين يدويًا."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 جارٍ الكشف عن عنوان MAC...",
            "mac_detect_success": "✅ تم التعرّف على عنوان MAC: {}",
            "mac_detect_success_dialog": (
                "تم التعرّف على عنوان MAC بنجاح.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "تم إدخال القيمة في حقل MAC."
            ),
            "mac_detect_failed": (
                "⚠ تعذّر التعرّف التلقائي على عنوان MAC. "
                "سيتم عرض المساعدة."
            ),
            "config_mac_find": "🔍 البحث عن MAC",
            "config_mac_find_tooltip": (
                "الكشف التلقائي عن عنوان MAC. "
                "في حال الفشل، سيتم عرض دليل إرشادي."
            ),
        },
        # "🇨🇿 Tschechisch"
        "cs": {
            "language": "Jazyk:",
            "window_title": "Správa NAS",
            "status_checking": "Kontrola připojení k serveru...",
            "status_online": "Server NAS je online ✓",
            "status_offline": "Server NAS je offline",
            "status_settings": "Nastavení otevřeno - Časovač zastaven",
            "status_settings_saved": "Nastavení uloženo",
            "status_settings_cancelled": "Nastavení zrušeno",
            "status_shutdown": "Vypínání NAS a Mac...",
            "status_shutdown_nas": "Vypínání NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Příkaz k vypnutí NAS odeslán, Mac bude nyní vypnut...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Vypnutí NAS selhalo, vypínám Mac...",
            "status_starting": "Spouštění NAS přes Wake-on-LAN...",
            "status_waiting": "Čekání na spuštění serveru...",
            "status_wol_sent": "Magic Packet odeslán",
            "status_wol_failed": "WOL selhalo",
            "status_mounting": "Připojování vybraných svazků...",
            "status_mounting_volume": "Připojování {}...",
            "status_mounted": "{} připojen ✓",
            "status_unmounting": "Odpojování {}...",
            "status_unmounted": "{} odpojen ✓",
            "status_error": "Chyba: Nelze připojit {}",
            "status_error_unmount": "Chyba: Nelze odpojit {}",
            "status_all_mounted": "Všechny svazky připojeny ✓",
            "status_all_unmounted": "Všechny svazky odpojeny ✓",
            "status_mount_all": "Připojování všech svazků...",
            "status_unmount_all": "Odpojování všech svazků...",
            "status_shutdown_cmd": "Příkaz k vypnutí NAS odeslán ✓",
            "status_timeout": "Časový limit - Nelze spustit server",
            "status_no_volumes": "Žádné připojené svazky",
            "status_mount_failed": "Připojení selhalo",
            "status_cancelled": "Zrušeno - Aplikace se zavírá",
            "status_esc": "Stisknuto ESC - Aplikace se zavírá",
            "status_server_online": "Server online - čekání na službu SMB...",
            "status_profile_changed": "Profil změněn na: {}",
            "status_switching": "Přepínání na profil: {}...",
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Zrušit",
            "btn_start_nas": "Spustit NAS",
            "btn_settings": "Nastavení (Cmd+E)",
            "btn_select_all": "Vše",
            "btn_save": "Uložit",
            "btn_reset": "Obnovit",
            "btn_info": "ℹ",
            "btn_profile": "Profily",
            "tooltip_shutdown_both": "Vypne Mac a NAS za 2 minuty",
            "tooltip_shutdown_nas": "Vypne pouze NAS",
            "tooltip_cancel": "Zavře aplikaci",
            "tooltip_start_nas": "Spustí NAS přes Wake-on-LAN",
            "tooltip_settings": "Nastavení (Cmd+E)",
            "timer_shutdown": "Automatické vypnutí za {} sekund - ENTER pro pouze NAS",
            "timer_start": "Automatické spuštění za {} sekund - ENTER pro okamžité spuštění",
            "volumes_title": "Dostupné svazky",
            "volumes_title_offline": "Připojit svazky při spuštění",
            "volumes_hint": "Poznámka: První svazek v seznamu je automaticky považován za hlavní a nelze jej deaktivovat.",
            "volumes_mount_tooltip": "Připojí se automaticky při spuštění serveru",
            "config_title": "AnyNasPy - Nastavení",
            "config_tab_profiles": "Profily serveru",
            "config_tab_general": "Obecné",
            "config_tab_volumes": "Svazky",
            "config_tab_timing": "Časová nastavení",
            "config_language": "Jazyk:",
            "config_nas_group": "Nastavení serveru NAS",
            "config_nas_user": "Uživatelské jméno:",
            "config_nas_dns": "DNS název:",
            "config_nas_ip": "IP adresa:",
            "config_nas_mac": "MAC adresa:",
            "config_ssh_key": "Cesta k SSH klíči:",
            "config_volumes_group": "Svazky",
            "config_volumes_label": "Svazky (jeden název na řádek):",
            "config_time_group": "Časová nastavení (sekundy)",
            "config_auto_shutdown": "Zpoždění automatického vypnutí:",
            "config_auto_start": "Zpoždění automatického spuštění:",
            "config_wol_wait": "Čekací doba WOL (max):",
            "config_smb_wait": "Čekací doba SMB:",
            "config_mount_retries": "Počet pokusů o připojení:",
            "config_status_file": "Soubor stavu",
            "config_json_path": "JSON konfigurační soubor:",
            "config_profile_name": "Název profilu:",
            "config_profile_active": "Aktivní profil",
            "config_profile_set_active": "Nastavit jako aktivní profil",
            "config_profile_list": "Existující profily:",
            "config_profile_new": "Nový profil",
            "config_profile_delete": "Smazat profil",
            "config_profile_duplicate": "Duplikovat profil",
            "config_profile_rename": "Přejmenovat",
            "config_profile_required": "Název profilu je povinný.",
            "config_profile_exists": "Profil s tímto názvem již existuje.",
            "config_profile_deleted": "Profil '{}' byl smazán.",
            "config_profile_duplicated": "Profil '{}' byl duplikován jako '{}'.",
            "config_profile_renamed": "Profil byl přejmenován na '{}'.",
            "config_profile_activated": "Profil '{}' je nyní aktivní.",
            "config_find_ip": "🔍 Najít IP",
            "config_find_ip_tooltip": "Automaticky najít IP serveru v síti",
            "config_ssh_help": "? Nápověda",
            "config_mac_help": "? Nápověda",
            "config_mac_help_tooltip": "Návod na nalezení MAC adresy",
            "msg_ip_found": "IP adresa serveru byla úspěšně nalezena:\n\n{}\n\nIP byla vložena do pole.",
            "msg_ip_not_found": "IP adresu serveru nebylo možné automaticky zjistit.\n\nZadejte prosím IP adresu ručně.\n\nTipy:\n• Zkontrolujte DNS název v nastavení\n• Ujistěte se, že je NAS zapnutý\n• IP adresu najdete v rozhraní DSM v části 'Systém > Síť'",
            "msg_reset_confirm": "Obnovit všechna nastavení na výchozí hodnoty?",
            "msg_reset_title": "Obnovit",
            "msg_reset_done": "Všechna nastavení byla obnovena na výchozí hodnoty.",
            "msg_delete_confirm": "Opravdu chcete smazat profil '{}'?",
            "msg_delete_title": "Smazat profil",
            "msg_no_active_profile": "Není vybrán žádný aktivní profil.",
            "info_title": "O AnyNasPy",
            "info_version": "Verze",
            "info_copyright": "Autorská práva",
            "info_license": "Licence",
            "info_impressum": "Impresum",
            "info_developer": "Vývojář",
            "info_contact": "Kontakt",
            "info_license_text": "MIT licence",
            "say_timer_shutdown": "Automatické vypnutí Mac a NAS za {} sekund - Enter pro pouze NAS - Escape pro zrušení",
            "say_timer_start": "Server NAS bude spuštěn za {} sekund - Enter pro okamžité spuštění",
            "say_server_online": "Server NAS je dostupný",
            "say_server_offline": "Server NAS je offline",
            "say_shutdown_started": "Zahájeno vypínání",
            "say_nas_shutdown": "NAS se vypíná",
            "say_starting_nas": "Spouští se NAS",
            "say_cancelled": "Zrušeno",
            "say_waiting_server": "Čekání na spuštění serveru",
            "say_wol_failed": "Chyba při odesílání",
            "say_server_reachable": "Server je dostupný",
            "say_mount_volume": "{} připraven",
            "say_unmount_volume": "Odpojování {}",
            "say_mount_all": "Připojování všech svazků",
            "say_unmount_all": "Odpojování všech svazků",
            "say_mount_error": "Chyba připojování",
            "say_unmount_error": "Chyba odpojování",
            "say_mount_failed": "Žádné svazky nepřipojeny",
            "say_settings_opened": "Nastavení otevřeno",
            "say_settings_saved": "Nastavení uloženo",
            "say_settings_cancelled": "Nastavení zrušeno",
            "say_workaround_deleted": "Soubor workaround smazán",
            "say_server_timeout": "Časový limit spuštění serveru",
            "say_profile_changed": "Profil změněn na {}",
            "ssh_key_create_title": "Vytvoření SSH klíče",
            "ssh_key_create_question": "Chcete vytvořit nový pár SSH klíčů?",
            "ssh_key_create_existing": "SSH klíč '{}' již existuje.\nChcete jej přepsat?",
            "ssh_key_create_comment": "Komentář k SSH klíči (volitelný):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH klíč vytvořen: {}",
            "ssh_key_create_error": "Chyba při vytváření SSH klíče",
            "ssh_key_create_timeout": "Časový limit při vytváření klíče",
            "ssh_key_create_failed": "ssh-keygen vrátil chybu:\n{}",
            "ssh_key_create_passphrase": "Heslo pro SSH klíč (ponechte prázdné pro žádné heslo):",
            "ssh_key_create_passphrase_confirm": "Potvrďte heslo:",
            "ssh_key_create_passphrase_mismatch": "Hesla se neshodují.",
            "ssh_key_create_info": "✅ Pár SSH klíčů byl úspěšně vytvořen:\n\n"
            "📁 Soukromý klíč: {}\n"
            "📁 Veřejný klíč: {}\n\n"
            "📋 Veřejný klíč pro kopírování:\n"
            "{}\n\n"
            "🔑 Jak nainstalovat klíč na NAS:\n"
            "1. Zkopírujte veřejný klíč (výše)\n"
            "2. Vložte jej do souboru:\n"
            "   ~/.ssh/authorized_keys na NAS\n"
            "3. Nebo použijte:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Zadejte prosím jiný název souboru:",
            "ssh_key_exists_also": "Klíč '{}' také existuje.\nProsím smažte jej nejprve nebo zvolte jiný název.",
            "ssh_key_passphrase_title": "Heslo",
            "ssh_key_passphrase_question": "Chcete použít heslo pro SSH klíč?\n\nBez hesla: Možné automatické připojení, méně bezpečné.\nS heslem: Bezpečnější, ale vyžaduje zadání při každém připojení.",
            "ssh_key_passphrase_enter": "Zadejte heslo",
            "ssh_key_passphrase_label": "Heslo pro SSH klíč (alespoň 4 znaky):",
            "ssh_key_passphrase_none": "Žádné heslo",
            "ssh_key_passphrase_none_question": "Nezadali jste heslo.\nChcete vytvořit klíč bez hesla?",
            "ssh_key_passphrase_short": "Heslo je příliš krátké",
            "ssh_key_passphrase_short_message": "Heslo musí mít alespoň 4 znaky.",
            "ssh_key_passphrase_confirm": "Potvrďte heslo",
            "ssh_key_passphrase_confirm_label": "Zadejte heslo znovu:",
            "ssh_key_passphrase_mismatch_title": "Chyba hesla",
            "ssh_key_passphrase_mismatch_message": "Hesla se neshodují.",
            "config_ssh_open": "Otevřít",
            "config_ssh_open_tooltip": "Vybrat SSH klíč nebo otevřít složku",
            "config_ssh_create": "Vytvořit",
            "config_ssh_create_tooltip": "Vytvořit nový pár SSH klíčů",
            "config_ssh_help_tooltip": "Zobrazit nápovědu k SSH klíči",
            "config_ssh_select": "Vybrat SSH klíč",
            "config_json_open": "Otevřít",
            "config_json_open_tooltip": "Otevřít složku JSON konfigurace",
            "config_error": "Chyba",
            "config_shutdown_mac_delay": "Čekací doba mezi vypnutím NAS a Mac:",
            "info_third_party": "Knihovny třetích stran",
            "info_pyqt5_license": "Tato aplikace používá PyQt5, který je licencován pod GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nPlný text licence je k dispozici na https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Rozpoznat svazky",
            "volumes_add": "Přidat",
            "volumes_delete": "Smazat",
            "volumes_move_up": "Posunout nahoru",
            "volumes_move_down": "Posunout dolů",
            "volumes_available": "Dostupné svazky:",
            "volumes_no_volumes": "Nebyly nalezeny žádné svazky.",
            "volumes_detection_failed": "Chyba při rozpoznávání svazků.",
            "volumes_detection_success": "Svazky úspěšně rozpoznány.",
            "volumes_confirm_delete": "Opravdu smazat svazek '{}'?",
            "volumes_enter_name": "Zadejte název nového svazku:",
            "volumes_name_exists": "Svazek s tímto názvem již existuje.",
            "msg_invalid_ip": "Zadaná IP adresa není platná.\nZadejte platnou IPv4 adresu (např. 192.168.1.100).",
            "msg_select_volume": "Vyberte svazek.",
            "msg_cannot_delete_main_volume": "První svazek (hlavní) nelze smazat.",
            "profile_cannot_delete_last": "Poslední profil nelze smazat.",
            "status_wol_sending": "Odesílání magického paketu...",
            "status_wol_method_failed": "Metoda Python selhala, zkouším další...",
            "status_trying_wakeonlan": "Zkouším wakeonlan...",
            "status_trying_etherwake": "Zkouším etherwake...",
            "ssh_key_system_key_warning": "Bezpečnostní varování",
            "ssh_key_system_key_message": "Název '{}' je systémový klíč a nebude přepsán.\nZvolte jiný název (např. synaspy_rsa).",
            "profile_name_exists": "Profil s názvem '{}' již existuje.",
            "config_profile_created": "Profil '{}' byl vytvořen.",
            "config_profile_create_failed": "Profil se nepodařilo vytvořit.",
            "config_profile_rename_failed": "Přejmenování selhalo.",
            "config_profile_duplicate_name": "Název pro duplicitní profil:",
            "config_profile_duplicate_failed": "Duplikování selhalo.",
            "config_profile_delete_failed": "Smazání selhalo.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Vypne pouze Mac (NAS zůstane zapnutý, žádné WOL)",
            "status_shutdown_mac_only": "Vypínám pouze Mac...",
            "say_shutdown_mac_only": "Mac se vypíná, NAS zůstane zapnutý",

            "btn_scheduled_shutdown": "🕐 Časované vypnutí",
            "tooltip_scheduled_shutdown": "Vypne po uživatelem zvolené době",
            "btn_scheduled_shutdown_offline": "🕐 Časovaně vypnout Mac",
            "tooltip_scheduled_shutdown_offline": "Vypne pouze Mac po zvolené době (NAS je offline)",
            "btn_cancel_scheduled": "⏹ Zrušit odpočítávání",
            "tooltip_cancel_scheduled": "Zruší aktivní odpočítávání",

            "sched_dialog_title": "Časované vypnutí",
            "sched_target_label": "Cíl:",
            "sched_target_both": "🖥️ Mac + NAS  (úplné vypnutí)",
            "sched_target_nas": "🗄️ Pouze NAS  (Mac zůstane zapnutý)",
            "sched_target_mac": "💻 Pouze Mac  (NAS zůstane zapnutý)",

            "sched_wait_label": "Doba čekání do vypnutí:",
            "sched_hours": "Hodiny",
            "sched_minutes": "Minuty",

            "sched_caffeinate_label": "Volba caffeinate (udrží Mac vzhůru):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Doporučeno: Systém vzhůru, obrazovka může ztmavnout  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Zabránit pouze nečinnosti a disku (obrazovka zůstane zapnutá)  (-i -m)",
            "sched_caffeinate_d": "Obrazovka navíc zůstane zapnutá  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simulovat aktivitu uživatele (obrazovka jasná, systém vzhůru)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maximum: Obrazovka + systém + disk trvale vzhůru  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Vypnuto (normální spoření energie – systém může spát)",

            "sched_caffeinate_hint": (
                "💡 Výukový fakt: Používej přepínače caffeinate přímo v terminálu:\n"
                "   -i  zabrání nečinnému spánku systému\n"
                "   -m  zabrání spánku disku (pevný disk neusne)\n"
                "   -s  zabrání spánku systému (pouze na napájecím adaptéru)\n"
                "   -d  zabrání spánku displeje (obrazovka zůstane zapnutá)\n"
                "   -u  simuluje aktivitu uživatele (displej zůstane jasný)\n"
                "   -w PID  ukončí caffeinate, když proces PID skončí\n"
                "Příklad:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Vypnutí naplánováno na: {}",
            "sched_countdown_label": "Odpočítávání: {} do vypnutí ({})",
            "sched_started": "Časovač spuštěn.\n\nCíl: {}\nDoba: {}\nKonec: {}",
            "sched_cancelled": "Časovač zrušen",
            "sched_already_active": "Již běží časovač. Nejprve zrušit?",
            "sched_invalid_time": "Zadej prosím platnou dobu (minimálně 1 minuta).",
            "sched_max_time": "Maximálně povoleno 720 hodin (30 dní).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Časovač spuštěn. Mac a NAS se vypnou za {}."
            ),
            "sched_voice_started_nas": (
                "Časovač spuštěn. Pouze NAS se vypne za {}. "
                "Mac zůstane zapnutý."
            ),
            "sched_voice_started_mac": (
                "Časovač spuštěn. Pouze Mac se vypne za {}. "
                "NAS zůstane zapnutý."
            ),
            "sched_voice_started_nothing": (
                "Časovač spuštěn. Po uplynutí se nic neprovede. "
                "caffeinate zůstane do té doby aktivní."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Mac zůstane vzhůru po dobu {}. "
                "Obrazovka může ztmavnout. "
                "Po uplynutí se nic neprovede."
            ),
            "sched_voice_nothing_im": (
                "Mac zůstane vzhůru po dobu {}. "
                "Obrazovka přitom zůstane zapnutá. "
                "Po uplynutí se nic neprovede."
            ),
            "sched_voice_nothing_d": (
                "Mac a obrazovka zůstanou zapnuté po dobu {}. "
                "Po uplynutí se nic neprovede."
            ),
            "sched_voice_nothing_u": (
                "Mac zůstane aktivní po dobu {}. "
                "Obrazovka přitom zůstane jasná. "
                "Po uplynutí se nic neprovede."
            ),
            "sched_voice_nothing_full": (
                "Mac zůstane plně aktivní po dobu {} – obrazovka a systém trvale vzhůru. "
                "Po uplynutí se nic neprovede."
            ),
            "sched_voice_nothing_off": (
                "Časovač běží po dobu {}. "
                "Po uplynutí se nic neprovede. "
                "Pozor: Mac může přejít do režimu spánku."
            ),
            "sched_voice_cancelled": "Časovač zrušen",
            "sched_caffeinate_failed": "caffeinate se nepodařilo spustit:\n{}",
            "sched_target_required": "Vyber prosím cíl.",
            "sched_tooltip_active": "Časovač běží – klikni pro zrušení",

            "status_scheduled_active": "Časovač aktivní - zbývá {}",
            "status_scheduled_triggered": "Časovač vypršel - spouštím {}",
            "status_scheduled_cancelled": "Časovač zrušen",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Časovač aktivní",
            "close_blocked_text": (
                "<b>Stále běží časovač!</b><br><br>"
                "Naplánováno: {}<br>"
                "Zbývá: <b>{}</b><br>"
                "V: {}<br><br>"
                "Pokud nyní zavřeš, naplánované vypnutí se "
                "<b>již neprovede</b>."
            ),
            "close_blocked_yes": "Přesto zavřít",
            "close_blocked_no": "Nechat aplikaci běžet",
            "close_blocked_cancel_text": (
                "Stále běží časovač.\n\n"
                "Opravdu chceš aplikaci zavřít?\n"
                "(Naplánované vypnutí bude poté zrušeno.)"
            ),
            "close_blocked_log_aborted": "Zavření zrušeno (časovač aktivní)",
            "close_blocked_log_discarded": (
                "Aplikace se zavírá i přes aktivní časovač – časovač zrušen"
            ),
            "close_blocked_log_cancel_aborted": (
                "Zavření aplikace zrušeno tlačítkem Zrušit"
            ),
            "duration_day": "den",
            "duration_days": "dní",
            "duration_hour": "hodina",
            "duration_hours": "hodin",
            "duration_minute": "minuta",
            "duration_minutes": "minut",
            "duration_connector_and": "a",
            "tooltip_pause_timer": "Pozastavit / obnovit časovač",
            "tooltip_stop_timer_inactive": "Žádný časovač není aktivní",
            "timer_stopped_notice": "⏹ Časovač zastaven – připraven k restartu",
            "say_timer_stopped": "Časovač zastaven",
            "say_timer_restarted": "Časovač restartován",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "Výrobce NAS:",
            "vendor_tooltip": (
                "Vyberte výrobce svého NAS. Určuje příkazy pro vypnutí "
                "a výchozí cesty. 'Automatická detekce' zkontroluje NAS přes SSH."
            ),
            "vendor_auto_detect": "🔄 Automatická detekce",
            "vendor_auto_detect_tooltip": (
                "Automaticky rozpoznat výrobce přes SSH. "
                "Předpoklad: SSH klíč a IP jsou správně nakonfigurovány."
            ),
            "vendor_detect_in_progress": "🔄 Rozpoznávání...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Obecný Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Vlastní",
            "vendor_custom_hint": (
                "Vlastní: Upravte příkazy pro vypnutí ručně. "
                "Výchozí: 'sudo shutdown -h now' (funguje na "
                "80 % všech Linuxových NAS)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Výrobce rozpoznán: {}",
            "vendor_detect_success_question": (
                "Výrobce rozpoznán: {}\n\n"
                "Má být tento výrobce převzat?\n"
                "(Aktuální hodnota: {})"
            ),
            "vendor_detect_failed": (
                "Výrobce nemohl být automaticky rozpoznán.\n\n"
                "Vyberte prosím ručně. Většina Linuxových NAS "
                "funguje s 'Obecný Linux'."
            ),
            "vendor_detect_no_ssh": (
                "Automatická detekce vyžaduje přístup přes SSH.\n\n"
                "Zkontrolujte prosím:\n"
                "• Cesta k SSH klíči je správná\n"
                "• IP adresa je správná\n"
                "• SSH je na NAS aktivováno\n"
                "• SSH klíč je na NAS nainstalován "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Nejprve prosím zadejte SSH klíč a IP adresu."
            ),
            "vendor_detect_nas_offline": (
                "Server NAS neodpovídá.\n\n"
                "Zkontrolujte prosím:\n"
                "• Je NAS zapnutý?\n"
                "• Je IP adresa správná?\n"
                "• Je NAS ve stejné síti?\n\n"
                "Zapněte NAS a zkuste to znovu."
            ),
            "vendor_detect_error": "Chyba při automatické detekci:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH klíč nenalezen:\n\n{}\n\n"
                "Zkontrolujte prosím cestu v nastavení."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Příkaz pro vypnutí:",
            "custom_cmd_tooltip": (
                "Příkaz, který se odešle na NAS přes SSH. "
                "Více příkazů oddělte středníkem."
            ),
            "custom_cmd_hint": (
                "💡 Více příkazů oddělte středníkem — "
                "použije se první úspěšný. "
                "Příklad: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Zobrazit nápovědu k příkazům pro vypnutí",
            "custom_cmd_help_title": "Typické příkazy pro vypnutí",
            "custom_cmd_help_text": (
                "<h3>Typické příkazy pro vypnutí podle výrobce</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (obecný):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Více příkazů (záložní řetězec)</h4>"
                "<p>Pokud první příkaz selže, vyzkouší se další. "
                "Oddělte středníkem:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Tip:</b> Nejprve zvolte nejpravděpodobnější příkaz, "
                "poté alternativy jako zálohu.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Rozpoznávání svazků přes SSH...",
            "volumes_detection_via_paths": (
                "🔍 Hledání v cestách specifických pro výrobce..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Záložní možnost: Hledání přes smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Hledání svazků přes SSH... Hledání může "
                "trvat několik sekund."
            ),
            "volumes_detect_panel_success": (
                "Nalezeno {} svazků — {} nově přidáno, "
                "{} již existuje"
            ),
            "volumes_detect_panel_partial": (
                "Nalezeno {} svazků — všechny již v seznamu"
            ),
            "volumes_detect_panel_failed": (
                "Nebyly nalezeny žádné svazky. "
                "Zadejte svazky prosím ručně."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Rozpoznávání MAC adresy...",
            "mac_detect_success": "✅ MAC adresa rozpoznána: {}",
            "mac_detect_success_dialog": (
                "MAC adresa byla úspěšně rozpoznána.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Hodnota byla vložena do pole MAC."
            ),
            "mac_detect_failed": (
                "⚠ MAC adresu nebylo možné automaticky rozpoznat. "
                "Zobrazí se nápověda."
            ),
            "config_mac_find": "🔍 Najít MAC",
            "config_mac_find_tooltip": (
                "Automaticky rozpoznat MAC adresu. "
                "Pokud to selže, zobrazí se návod."
            ),
        },
        # "🇩🇪 Deutsch"
        "de": {
            "language": "Sprache:",
            # Hauptfenster
            "window_title": "NAS Management",
            "status_checking": "Prüfe Serververbindung...",
            "status_online": "NAS Server ist online ✓",
            "status_offline": "NAS Server ist offline",
            "status_settings": "Einstellungen geöffnet - Timer gestoppt",
            "status_settings_saved": "Einstellungen gespeichert",
            "status_settings_cancelled": "Einstellungen abgebrochen",
            "status_shutdown": "Fahre NAS und Mac herunter...",
            "status_shutdown_nas": "Fahre NAS herunter...",
            "status_shutdown_nas_sent_mac_follows": "✅ NAS-Shutdown gesendet, Mac wird jetzt heruntergefahren...",
            "status_shutdown_nas_failed_mac_still": "⚠️ NAS-Shutdown fehlgeschlagen, fahre Mac herunter...",
            "status_starting": "Starte NAS über Wake-on-LAN...",
            "status_waiting": "Warte auf Serverstart...",
            "status_wol_sent": "Magic Packet gesendet",
            "status_wol_failed": "WOL fehlgeschlagen",
            "status_mounting": "Mounte ausgewählte Volumes...",
            "status_mounting_volume": "Mounte {}...",
            "status_mounted": "{} gemountet ✓",
            "status_unmounting": "Werfe {} aus...",
            "status_unmounted": "{} ausgewerfen ✓",
            "status_error": "Fehler: {} konnte nicht gemountet werden",
            "status_error_unmount": "Fehler: {} konnte nicht ausgewerfen werden",
            "status_all_mounted": "Alle Volumes gemountet ✓",
            "status_all_unmounted": "Alle Volumes ausgewerfen ✓",
            "status_mount_all": "Mounte alle Volumes...",
            "status_unmount_all": "Werfe alle Volumes aus...",
            "status_shutdown_cmd": "NAS-Shutdown-Befehl gesendet ✓",
            "status_timeout": "Timeout - Server konnte nicht gestartet werden",
            "status_no_volumes": "Keine Volumes gemountet",
            "status_mount_failed": "Mounten fehlgeschlagen",
            "status_cancelled": "Abgebrochen - App wird geschlossen",
            "status_esc": "ESC gedrückt - App wird geschlossen",
            "status_server_online": "Server online - warte auf SMB-Dienst...",
            "status_profile_changed": "Profil gewechselt zu: {}",
            "status_switching": "Wechsle zu Profil: {}...",
            # Buttons
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Abbrechen",
            "btn_start_nas": "Start NAS",
            "btn_settings": "Einstellungen (Cmd+E)",
            "btn_select_all": "Alle",
            "btn_save": "Speichern",
            "btn_reset": "Zurücksetzen",
            "btn_info": "ℹ",
            "btn_profile": "Profile",
            # Tooltips
            "tooltip_shutdown_both": "Fährt Mac und NAS in 2min herunter",
            "tooltip_shutdown_nas": "Fährt nur NAS herunter",
            "tooltip_cancel": "Schließt die App",
            "tooltip_start_nas": "Startet NAS über Wake-on-LAN",
            "tooltip_settings": "Einstellungen (Cmd+E)",
            # Timer
            "timer_shutdown": "Auto-Shutdown in {} Sekunden - ENTER für nur NAS",
            "timer_start": "Auto-Start in {} Sekunden - ENTER für sofortigen Start",
            # Volumes
            "volumes_title": "Verfügbare Volumes",
            "volumes_title_offline": "Volumes bei Start mounten",
            "volumes_hint": "Hinweis: Das erste Volume in der Liste wird automatisch als Haupt-Volume behandelt und kann nicht deaktiviert werden.",
            "volumes_mount_tooltip": "Wird beim Serverstart automatisch gemountet",
            # Config Dialog
            "config_title": "AnyNasPy - Einstellungen",
            "config_tab_profiles": "Server-Profile",
            "config_tab_general": "Allgemein",
            "config_tab_volumes": "Volumes",
            "config_tab_timing": "Zeiteinstellungen",
            "config_language": "Sprache:",
            "config_nas_group": "NAS Server Einstellungen",
            "config_nas_user": "Benutzername:",
            "config_nas_dns": "DNS-Name:",
            "config_nas_ip": "IP-Adresse:",
            "config_nas_mac": "MAC-Adresse:",
            "config_ssh_key": "SSH-Key Pfad:",
            "config_volumes_group": "Volumes",
            "config_volumes_label": "Volumes (ein Name pro Zeile):",
            "config_time_group": "Zeiteinstellungen (Sekunden)",
            "config_auto_shutdown": "Auto-Shutdown Verzögerung:",
            "config_auto_start": "Auto-Start Verzögerung:",
            "config_wol_wait": "WOL Wartezeit (max):",
            "config_smb_wait": "SMB Wartezeit:",
            "config_mount_retries": "Mount Wiederholungen:",
            "config_status_file": "Statusdatei",
            "config_json_path": "JSON-Konfigurationsdatei:",
            "config_profile_name": "Profilname:",
            "config_profile_active": "Aktives Profil",
            "config_profile_set_active": "Als aktives Profil setzen",
            "config_profile_list": "Vorhandene Profile:",
            "config_profile_new": "Neues Profil",
            "config_profile_delete": "Profil löschen",
            "config_profile_duplicate": "Profil duplizieren",
            "config_profile_rename": "Umbenennen",
            "config_profile_required": "Profilname ist erforderlich.",
            "config_profile_exists": "Ein Profil mit diesem Namen existiert bereits.",
            "config_profile_deleted": "Profil '{}' wurde gelöscht.",
            "config_profile_duplicated": "Profil '{}' wurde als '{}' dupliziert.",
            "config_profile_renamed": "Profil wurde umbenannt in '{}'.",
            "config_profile_activated": "Profil '{}' ist jetzt aktiv.",
            # Config Buttons
            "config_find_ip": "🔍 IP finden",
            "config_find_ip_tooltip": "Automatisch die Server-IP im Netzwerk suchen",
            "config_ssh_help": "? Hilfe",
            "config_mac_help": "? Hilfe",
            "config_mac_help_tooltip": "Anleitung zum Finden der MAC-Adresse",
            # Messages
            "msg_ip_found": "Die Server-IP wurde erfolgreich ermittelt:\n\n{}\n\nDie IP wurde in das Feld eingetragen.",
            "msg_ip_not_found": "Die Server-IP konnte nicht automatisch ermittelt werden.\n\nBitte geben Sie die IP-Adresse manuell ein.\n\nTipps:\n• Prüfen Sie den DNS-Namen in den Einstellungen\n• Stellen Sie sicher, dass der NAS eingeschaltet ist\n• Die IP finden Sie in der DSM-Oberfläche unter 'System > Netzwerk'",
            "msg_reset_confirm": "Alle Einstellungen auf Standardwerte zurücksetzen?",
            "msg_reset_title": "Zurücksetzen",
            "msg_reset_done": "Alle Einstellungen wurden auf die Standardwerte zurückgesetzt.",
            "msg_delete_confirm": "Profil '{}' wirklich löschen?",
            "msg_delete_title": "Profil löschen",
            "msg_no_active_profile": "Kein aktives Profil ausgewählt.",
            # Info Dialog
            "info_title": "Über AnyNasPy",
            "info_version": "Version",
            "info_copyright": "Copyright",
            "info_license": "Lizenz",
            "info_impressum": "Impressum",
            "info_developer": "Entwickler",
            "info_contact": "Kontakt",
            "info_license_text": "MIT License",
            # Sonstiges
            "say_timer_shutdown": "Mac und NAS Auto Shutdown in {} Sekunden - Enter für nur NAS - Escape zum Abbrechen",
            "say_timer_start": "Der NAS Server wird in {} Sekunden gestartet - Enter zum sofortigen Start",
            "say_server_online": "NAS Server ist erreichbar",
            "say_server_offline": "NAS Server ist offline",
            "say_shutdown_started": "Herunterfahren gestartet",
            "say_nas_shutdown": "NAS wird heruntergefahren",
            "say_starting_nas": "Starte NAS",
            "say_cancelled": "Abgebrochen",
            "say_waiting_server": "Warte auf Serverstart",
            "say_wol_failed": "Fehler beim Senden",
            "say_server_reachable": "Server erreichbar",
            "say_mount_volume": "{} bereit",
            "say_unmount_volume": "Werfe {} aus",
            "say_mount_all": "Mounte alle Volumes",
            "say_unmount_all": "Werfe alle Volumes aus",
            "say_mount_error": "Fehler beim Mounten",
            "say_unmount_error": "Fehler beim Auswerfen",
            "say_mount_failed": "Keine Volumes gemountet",
            "say_settings_opened": "Einstellungen geöffnet",
            "say_settings_saved": "Einstellungen gespeichert",
            "say_settings_cancelled": "Einstellungen abgebrochen",
            "say_workaround_deleted": "Workaround Datei gelöscht",
            "say_server_timeout": "Server Start Zeitüberschreitung",
            "say_profile_changed": "Profil gewechselt zu {}",
            "ssh_key_create_title": "SSH-Key erstellen",
            "ssh_key_create_question": "Möchten Sie ein neues SSH-Key-Paar erstellen?",
            "ssh_key_create_existing": "Der SSH-Key '{}' existiert bereits.\nMöchten Sie ihn überschreiben?",
            "ssh_key_create_comment": "Kommentar für den SSH-Key (optional):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH-Key erstellt: {}",
            "ssh_key_create_error": "Fehler beim Erstellen des SSH-Keys",
            "ssh_key_create_timeout": "Zeitüberschreitung bei Key-Erstellung",
            "ssh_key_create_failed": "ssh-keygen gab einen Fehler zurück:\n{}",
            "ssh_key_create_passphrase": "Passphrase für den SSH-Key (leer lassen für keine Passphrase):",
            "ssh_key_create_passphrase_confirm": "Passphrase bestätigen:",
            "ssh_key_create_passphrase_mismatch": "Die Passphrases stimmen nicht überein.",
            "ssh_key_create_info": "✅ SSH-Key-Paar wurde erfolgreich erstellt:\n\n"
            "📁 Privater Key: {}\n"
            "📁 Öffentlicher Key: {}\n\n"
            "📋 Öffentlicher Key zum Kopieren:\n"
            "{}\n\n"
            "🔑 So installieren Sie den Key auf Ihrem NAS:\n"
            "1. Kopieren Sie den öffentlichen Key (oben)\n"
            "2. Fügen Sie ihn in die Datei ein:\n"
            "   ~/.ssh/authorized_keys auf dem NAS\n"
            "3. Oder verwenden Sie:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Bitte geben Sie einen anderen Dateinamen ein:",
            "ssh_key_exists_also": "Der Key '{}' existiert ebenfalls.\nBitte löschen Sie ihn zuerst oder wählen Sie einen anderen Namen.",
            "ssh_key_passphrase_title": "Passphrase",
            "ssh_key_passphrase_question": "Möchten Sie eine Passphrase für den SSH-Key verwenden?\n\nOhne Passphrase: Automatische Verbindung möglich, weniger sicher.\nMit Passphrase: Sicherer, aber bei jeder Verbindung Abfrage.",
            "ssh_key_passphrase_enter": "Passphrase eingeben",
            "ssh_key_passphrase_label": "Passphrase für den SSH-Key (mindestens 4 Zeichen):",
            "ssh_key_passphrase_none": "Keine Passphrase",
            "ssh_key_passphrase_none_question": "Sie haben keine Passphrase eingegeben.\nMöchten Sie den Key ohne Passphrase erstellen?",
            "ssh_key_passphrase_short": "Passphrase zu kurz",
            "ssh_key_passphrase_short_message": "Die Passphrase sollte mindestens 4 Zeichen lang sein.",
            "ssh_key_passphrase_confirm": "Passphrase bestätigen",
            "ssh_key_passphrase_confirm_label": "Passphrase erneut eingeben:",
            "ssh_key_passphrase_mismatch_title": "Passphrase Fehler",
            "ssh_key_passphrase_mismatch_message": "Die Passphrases stimmen nicht überein.",
            "config_ssh_open": "Öffnen",
            "config_ssh_open_tooltip": "SSH-Key auswählen oder Ordner öffnen",
            "config_ssh_create": "Erstellen",
            "config_ssh_create_tooltip": "Neues SSH-Key-Paar erstellen",
            "config_ssh_help_tooltip": "Hilfe zum SSH-Key anzeigen",
            "config_ssh_select": "SSH-Key auswählen",
            "config_json_open": "Öffnen",
            "config_json_open_tooltip": "JSON-Konfigurationsordner öffnen",
            "config_error": "Fehler",
            "config_shutdown_mac_delay": "Wartezeit zwischen NAS- und Mac-Shutdown:",
            "info_third_party": "Drittanbieter-Bibliotheken",
            "info_pyqt5_license": "Diese Anwendung verwendet PyQt5, das unter der GNU General Public License v3 (GPLv3) lizenziert ist.\nCopyright (c) Riverbank Computing Limited.\n\nDer vollständige Lizenztext kann unter https://www.gnu.org/licenses/gpl-3.0.html eingesehen werden.",
            # --> ab hier neu
            # Deutsch (de)
            "volumes_auto_detect": "Volumes erkennen",
            "volumes_add": "Hinzufügen",
            "volumes_delete": "Löschen",
            "volumes_move_up": "Nach oben",
            "volumes_move_down": "Nach unten",
            "volumes_available": "Verfügbare Volumes:",
            "volumes_no_volumes": "Keine Volumes gefunden.",
            "volumes_detection_failed": "Fehler bei der Volume-Erkennung.",
            "volumes_detection_success": "Volumes erfolgreich erkannt.",
            "volumes_confirm_delete": "Volume '{}' wirklich löschen?",
            "volumes_enter_name": "Bitte geben Sie den Namen des neuen Volumes ein:",
            "volumes_name_exists": "Ein Volume mit diesem Namen existiert bereits.",
            # Fehlermeldungen und weitere hartcodierte Texte
            "msg_invalid_ip": "Die eingegebene IP-Adresse ist nicht gültig.\nBitte geben Sie eine gültige IPv4-Adresse ein (z.B. 192.168.1.100).",
            "msg_select_volume": "Bitte wählen Sie ein Volume aus.",
            "msg_cannot_delete_main_volume": "Das erste Volume (Haupt-Volume) kann nicht gelöscht werden.",
            "profile_cannot_delete_last": "Das letzte Profil kann nicht gelöscht werden.",
            "status_wol_sending": "Sende Magic Packet...",
            "status_wol_method_failed": "Python-Methode fehlgeschlagen, versuche nächste...",
            "status_trying_wakeonlan": "Versuche wakeonlan...",
            "status_trying_etherwake": "Versuche etherwake...",
            "ssh_key_system_key_warning": "Sicherheitswarnung",
            "ssh_key_system_key_message": "Der Name '{}' ist ein System-Key und wird nicht überschrieben!\nBitte wählen Sie einen anderen Namen (z.B. synaspy_rsa).",
            "profile_name_exists": "Ein Profil mit dem Namen '{}' existiert bereits.",
            "profile_cannot_delete_last": "Das letzte Profil kann nicht gelöscht werden.",
            "config_profile_created": "Profil '{}' wurde erstellt.",
            "config_profile_create_failed": "Profil konnte nicht erstellt werden.",
            "config_profile_rename_failed": "Umbenennung fehlgeschlagen.",
            "config_profile_duplicate_name": "Name für das duplizierte Profil:",
            "config_profile_duplicate_failed": "Duplizieren fehlgeschlagen.",
            "config_profile_delete_failed": "Löschen fehlgeschlagen.",

            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Fährt nur den Mac herunter (NAS bleibt an, kein WOL)",
            "status_shutdown_mac_only": "Fahre nur Mac herunter...",
            "say_shutdown_mac_only": "Mac wird heruntergefahren, NAS bleibt an",

            "btn_scheduled_shutdown": "🕐 Zeitgesteuert herunterfahren",
            "tooltip_scheduled_shutdown": "Fährt nach einer vom Benutzer gewählten Zeit herunter",
            "btn_scheduled_shutdown_offline": "🕐 Mac zeitgesteuert herunterfahren",
            "tooltip_scheduled_shutdown_offline": "Fährt nur den Mac nach einer gewählten Zeit herunter (NAS ist offline)",
            "btn_cancel_scheduled": "⏹ Countdown abbrechen",
            "tooltip_cancel_scheduled": "Bricht den aktiven Countdown ab",

            "sched_dialog_title": "Zeitgesteuertes Herunterfahren",
            "sched_target_label": "Ziel:",
            "sched_target_both": "🖥️ Mac + NAS  (komplett herunterfahren)",
            "sched_target_nas": "🗄️ Nur NAS  (Mac bleibt an)",
            "sched_target_mac": "💻 Nur Mac  (NAS bleibt an)",

            "sched_wait_label": "Wartezeit bis zum Herunterfahren:",
            "sched_hours": "Stunden",
            "sched_minutes": "Minuten",

            "sched_caffeinate_label": "caffeinate-Option (hält den Mac wach):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Empfohlen: System wach, Bildschirm darf dunkel werden  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Nur Idle & Disk verhindern (Bildschirm bleibt an)  (-i -m)",
            "sched_caffeinate_d": "Bildschirm bleibt zusätzlich an  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "User aktiv simulieren (Bildschirm hell, System wach)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maximal: Bildschirm + System + Disk permanent wach  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Aus (normales Energiesparen – System kann schlafen)",

            "sched_caffeinate_hint": (
                "💡 Lern-Fact: caffeinate-Flags im Terminal selbst nutzen:\n"
                "   -i  verhindert Idle-Sleep des Systems\n"
                "   -m  verhindert Disk-Sleep (Festplatte schläft nicht ein)\n"
                "   -s  verhindert System-Sleep (nur am Netzteil)\n"
                "   -d  verhindert Display-Sleep (Bildschirm bleibt an)\n"
                "   -u  simuliert User-Aktivität (Display bleibt hell)\n"
                "   -w PID  beendet caffeinate, wenn Prozess PID endet\n"
                "Beispiel:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Herunterfahren geplant für: {}",
            "sched_countdown_label": "Countdown: {} bis zum Herunterfahren ({})",
            "sched_started": "Zeitgeber gestartet.\n\nZiel: {}\nDauer: {}\nEnde: {}",
            "sched_cancelled": "Zeitgeber abgebrochen",
            "sched_already_active": "Es läuft bereits ein Zeitgeber. Erst abbrechen?",
            "sched_invalid_time": "Bitte eine gültige Zeit eingeben (mindestens 1 Minute).",
            "sched_max_time": "Maximal 720 Stunden (30 Tage) erlaubt.",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Zeitgeber gestartet. Mac und NAS werden in {} heruntergefahren."
            ),
            "sched_voice_started_nas": (
                "Zeitgeber gestartet. Nur der NAS wird in {} heruntergefahren. "
                "Der Mac bleibt an."
            ),
            "sched_voice_started_mac": (
                "Zeitgeber gestartet. Nur der Mac wird in {} heruntergefahren. "
                "Der NAS bleibt an."
            ),
            "sched_voice_started_nothing": (
                "Zeitgeber gestartet. Nach Ablauf wird nichts ausgeführt. "
                "caffeinate bleibt bis dahin aktiv."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Der Mac bleibt für {} wach. "
                "Der Bildschirm darf dunkel werden. "
                "Nach Ablauf wird nichts ausgeführt."
            ),
            "sched_voice_nothing_im": (
                "Der Mac bleibt für {} wach. "
                "Der Bildschirm bleibt dabei an. "
                "Nach Ablauf wird nichts ausgeführt."
            ),
            "sched_voice_nothing_d": (
                "Der Mac und der Bildschirm bleiben für {} an. "
                "Nach Ablauf wird nichts ausgeführt."
            ),
            "sched_voice_nothing_u": (
                "Der Mac bleibt für {} aktiv. "
                "Der Bildschirm bleibt dabei hell. "
                "Nach Ablauf wird nichts ausgeführt."
            ),
            "sched_voice_nothing_full": (
                "Der Mac bleibt für {} voll aktiv – Bildschirm und System durchgehend wach. "
                "Nach Ablauf wird nichts ausgeführt."
            ),
            "sched_voice_nothing_off": (
                "Der Zeitgeber läuft für {}. "
                "Nach Ablauf wird nichts ausgeführt. "
                "Achtung: Der Mac kann in den Ruhezustand wechseln."
            ),
            "sched_voice_cancelled": "Zeitgeber abgebrochen",
            "sched_caffeinate_failed": "caffeinate konnte nicht gestartet werden:\n{}",
            "sched_target_required": "Bitte ein Ziel auswählen.",
            "sched_tooltip_active": "Zeitgeber läuft – klicken zum Abbrechen",

            "status_scheduled_active": "Zeitgeber aktiv - {} verbleibend",
            "status_scheduled_triggered": "Zeitgeber abgelaufen - starte {}",
            "status_scheduled_cancelled": "Zeitgeber abgebrochen",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Zeitgeber aktiv",
            "close_blocked_text": (
                "<b>Es läuft noch ein Zeitgeber!</b><br><br>"
                "Geplant: {}<br>"
                "Verbleibend: <b>{}</b><br>"
                "Um: {}<br><br>"
                "Wenn du jetzt schließt, wird der geplante Shutdown "
                "<b>nicht mehr ausgeführt</b>."
            ),
            "close_blocked_yes": "Trotzdem schließen",
            "close_blocked_no": "App weiterlaufen lassen",
            "close_blocked_cancel_text": (
                "Es läuft noch ein Zeitgeber.\n\n"
                "Möchtest du die App wirklich schließen?\n"
                "(Der geplante Shutdown wird dann verworfen.)"
            ),
            "close_blocked_log_aborted": "Schließen abgebrochen (Zeitgeber aktiv)",
            "close_blocked_log_discarded": (
                "App wird trotz aktivem Zeitgeber geschlossen – Zeitgeber verworfen"
            ),
            "close_blocked_log_cancel_aborted": (
                "App-Schließen via Cancel-Button abgebrochen"
            ),
            # Bausteine für die Sprachausgabe der Dauer
            "duration_day": "Tag",
            "duration_days": "Tagen",
            "duration_hour": "Stunde",
            "duration_hours": "Stunden",
            "duration_minute": "Minute",
            "duration_minutes": "Minuten",
            "duration_connector_and": "und",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Timer pausiert – noch {} Sekunden",
            "timer_resumed": "Timer fortgesetzt",
            "say_timer_paused": "Timer pausiert",
            "say_timer_resumed": "Timer fortgesetzt",
            "tooltip_pause_timer": "Timer pausieren/fortsetzen",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Sprachausgabe aktiviert",
            "speech_enabled_hint": (
                "Spricht Statusmeldungen, Volume-Quittungen und Timer-Info "
                "über die macOS-Sprachausgabe. Bei Deaktivierung läuft die "
                "App stumm."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Für das zeitgesteuerte Herunterfahren des Macs wird das "
                "Administrator-Passwort benötigt.\n\n"
                "Es wird sicher im macOS-Schlüsselbund gespeichert und nur "
                "beim Herunterfahren verwendet.\n\n"
                "Jetzt einrichten?"
            ),
            "mac_pw_dialog_title": "Administrator-Passwort",
            "mac_pw_dialog_message": (
                "Für das Herunterfahren des Macs wird das Administrator-Passwort "
                "benötigt.\n\n"
                "Es wird sicher im macOS-Schlüsselbund gespeichert und nur beim "
                "Herunterfahren verwendet."
            ),
            "mac_pw_wrong_password": (
                "Das Passwort ist falsch.\n\n"
                "Bitte erneut versuchen."
            ),
            "mac_pw_test_failed": (
                "Fehler bei der Passwort-Prüfung:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Der Zeitgeber wurde nicht gestartet, weil die "
                "Passwort-Eingabe abgebrochen wurde.\n\n"
                "Ohne Passwort kann der Mac nicht heruntergefahren werden."
            ),
            "clear_password_title": "Gespeichertes Passwort löschen",
            "clear_password_message": (
                "Das im Schlüsselbund gespeicherte Administrator-Passwort löschen?\n\n"
                "Beim nächsten zeitgesteuerten Herunterfahren wird das Passwort "
                "erneut abgefragt."
            ),
            "clear_password_success": "Passwort wurde aus dem Schlüsselbund entfernt.",
            "clear_password_failed": "Passwort konnte nicht gelöscht werden.",
            "clear_password_description": (
                "Entfernt das im macOS-Schlüsselbund gespeicherte "
                "Administrator-Passwort. Beim nächsten zeitgesteuerten "
                "Herunterfahren wird es erneut abgefragt."
            ),
            "clear_password_button": "Gespeichertes Passwort löschen",
            "shutdown_no_password_message": (
                "Der Mac konnte nicht heruntergefahren werden.\n\n"
                "Weder eine NOPASSWD-sudoers-Regel noch ein gespeichertes "
                "Passwort im Schlüsselbund sind vorhanden.\n\n"
                "Bitte richte den zeitgesteuerten Shutdown erneut ein."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Warnung",
            "warning_eject_failed_continue": (
                "Netzwerklaufwerke konnten nicht sauber ausgeworfen werden.\n\n"
                "Wenn noch Daten kopiert werden oder Dateien geöffnet sind, "
                "kann es zu Datenverlust kommen.\n\n"
                "Trotzdem mit dem Herunterfahren fortfahren?"
            ),
            "auto_timer_disabled_no_pw": (
                "Auto-Shutdown deaktiviert – kein Administrator-Passwort im Schlüsselbund vorhanden. Bitte bei der nächsten Aufforderung einmalig eingeben."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Ja",
            "btn_no": "Nein",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Nichts herunterfahren  (Mac bleibt wach – z.B. für Backup-Skripte)",
            "sched_countdown_coffee_label": "⏳ caffeinate aktiv: noch {} ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Coffee-Timer läuft noch",
            "coffee_conflict_message": (
                "Es läuft noch ein Coffee-Timer:\n\n"
                "Verbleibend: {}\n\n"
                "Wenn du jetzt herunterfährst, wird der Coffee-Timer abgebrochen "
                "und caffeinate beendet.\n\n"
                "Trotzdem herunterfahren?"
            ),
            "shutdown_timer_conflict_title": "Shutdown-Timer läuft noch",
            "shutdown_timer_conflict_message": (
                "Es läuft noch ein Shutdown-Timer:\n\n"
                "Geplant: {}\n"
                "Verbleibend: {}\n\n"
                "Wenn du jetzt manuell herunterfährst, wird der Timer abgebrochen "
                "und muss neu geplant werden.\n\n"
                "Trotzdem herunterfahren?"
            ),
            "tooltip_stop_timer": "Timer komplett stoppen",
            "tooltip_stop_timer_inactive": "Kein Timer aktiv",
            "timer_stopped_notice": "⏹ Timer gestoppt – bereit für Neustart",
            "say_timer_stopped": "Timer gestoppt",
            "say_timer_restarted": "Timer neu gestartet",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "NAS-Hersteller:",
            "vendor_tooltip": (
                "Wähle deinen NAS-Hersteller. Bestimmt die Shutdown-Befehle "
                "und Standard-Pfade. 'Auto-erkennen' prüft den NAS per SSH."
            ),
            "vendor_auto_detect": "🔄 Auto-erkennen",
            "vendor_auto_detect_tooltip": (
                "Hersteller automatisch per SSH erkennen. "
                "Voraussetzung: SSH-Key und IP sind korrekt konfiguriert."
            ),
            "vendor_detect_in_progress": "🔄 Erkenne...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Generisches Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Benutzerdefiniert",
            "vendor_custom_hint": (
                "Benutzerdefiniert: Passe die Shutdown-Befehle manuell an. "
                "Standard: 'sudo shutdown -h now' (funktioniert auf "
                "80 % aller Linux-NAS)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Hersteller erkannt: {}",
            "vendor_detect_success_question": (
                "Hersteller erkannt: {}\n\n"
                "Soll dieser Hersteller übernommen werden?\n"
                "(Aktueller Wert: {})"
            ),
            "vendor_detect_failed": (
                "Hersteller konnte nicht automatisch erkannt werden.\n\n"
                "Bitte manuell auswählen. Die meisten Linux-NAS "
                "funktionieren mit 'Generisches Linux'."
            ),
            "vendor_detect_no_ssh": (
                "Auto-Erkennung erfordert SSH-Zugriff.\n\n"
                "Bitte prüfe:\n"
                "• SSH-Key-Pfad ist korrekt\n"
                "• IP-Adresse ist korrekt\n"
                "• SSH ist auf dem NAS aktiviert\n"
                "• SSH-Key ist auf dem NAS installiert "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Bitte zuerst SSH-Key und IP-Adresse eintragen."
            ),
            "vendor_detect_nas_offline": (
                "Der NAS-Server antwortet nicht.\n\n"
                "Bitte prüfe:\n"
                "• Ist der NAS eingeschaltet?\n"
                "• Ist die IP-Adresse korrekt?\n"
                "• Ist der NAS im gleichen Netzwerk?\n\n"
                "Fahre den NAS hoch und versuche es erneut."
            ),
            "vendor_detect_error": "Fehler bei der Auto-Erkennung:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH-Key nicht gefunden:\n\n{}\n\n"
                "Bitte prüfe den Pfad in den Einstellungen."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Shutdown-Befehl:",
            "custom_cmd_tooltip": (
                "Der Befehl, der per SSH an den NAS gesendet wird. "
                "Mehrere Befehle durch Semikolon trennen."
            ),
            "custom_cmd_hint": (
                "💡 Mehrere Befehle durch Semikolon trennen — "
                "der erste erfolgreiche wird verwendet. "
                "Beispiel: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Hilfe zu Shutdown-Befehlen anzeigen",
            "custom_cmd_help_title": "Typische Shutdown-Befehle",
            "custom_cmd_help_text": (
                "<h3>Typische Shutdown-Befehle nach Hersteller</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (generisch):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Mehrere Befehle (Fallback-Kette)</h4>"
                "<p>Wenn der erste Befehl fehlschlägt, wird der nächste "
                "probiert. Trennung durch Semikolon:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Tipp:</b> Wähle zuerst den wahrscheinlichsten Befehl, "
                "dann Alternativen als Fallback.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Erkenne Volumes über SSH...",
            "volumes_detection_via_paths": (
                "🔍 Suche in hersteller-spezifischen Pfaden..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Fallback: Suche via smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Suche Volumes über SSH... Die Suche kann "
                "einige Sekunden dauern."
            ),
            "volumes_detect_panel_success": (
                "{} Volumes gefunden — {} neu hinzugefügt, "
                "{} bereits vorhanden"
            ),
            "volumes_detect_panel_partial": (
                "{} Volumes gefunden — alle bereits in der Liste"
            ),
            "volumes_detect_panel_failed": (
                "Keine Volumes gefunden. "
                "Bitte Volumes manuell eintragen."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Erkenne MAC-Adresse...",
            "mac_detect_success": "✅ MAC-Adresse erkannt: {}",
            "mac_detect_success_dialog": (
                "MAC-Adresse erfolgreich erkannt.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Der Wert wurde ins MAC-Feld eingetragen."
            ),
            "mac_detect_failed": (
                "⚠ MAC-Adresse konnte nicht automatisch erkannt werden. "
                "Hilfe wird angezeigt."
            ),
            "config_mac_find": "🔍 MAC finden",
            "config_mac_find_tooltip": (
                "MAC-Adresse automatisch erkennen. "
                "Falls das scheitert, wird eine Anleitung angezeigt."
            ),        },
        # "🇬🇷 Ελληνικά" (Griechisch)
        "el": {
            "language": "Γλώσσα:",
            "window_title": "Διαχείριση NAS",
            "status_checking": "Έλεγχος σύνδεσης διακομιστή...",
            "status_online": "Ο διακομιστής NAS είναι σε λειτουργία ✓",
            "status_offline": "Ο διακομιστής NAS είναι εκτός λειτουργίας",
            "status_settings": "Οι ρυθμίσεις άνοιξαν - Ο χρονοδιακόπτης σταμάτησε",
            "status_settings_saved": "Οι ρυθμίσεις αποθηκεύτηκαν",
            "status_settings_cancelled": "Οι ρυθμίσεις ακυρώθηκαν",
            "status_shutdown": "Τερματισμός NAS και Mac...",
            "status_shutdown_nas": "Τερματισμός NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Η εντολή τερματισμού NAS στάλθηκε, ο Mac θα τερματιστεί τώρα...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Αποτυχία τερματισμού NAS, τερματισμός Mac...",
            "status_starting": "Εκκίνηση NAS μέσω Wake-on-LAN...",
            "status_waiting": "Αναμονή για εκκίνηση διακομιστή...",
            "status_wol_sent": "Το Magic Packet στάλθηκε",
            "status_wol_failed": "Αποτυχία WOL",
            "status_mounting": "Προσάρτηση επιλεγμένων τόμων...",
            "status_mounting_volume": "Προσάρτηση {}...",
            "status_mounted": "{} προσαρτήθηκε ✓",
            "status_unmounting": "Αποπροσάρτηση {}...",
            "status_unmounted": "{} αποπροσαρτήθηκε ✓",
            "status_error": "Σφάλμα: Αδυναμία προσάρτησης {}",
            "status_error_unmount": "Σφάλμα: Αδυναμία αποπροσάρτησης {}",
            "status_all_mounted": "Όλοι οι τόμοι προσαρτήθηκαν ✓",
            "status_all_unmounted": "Όλοι οι τόμοι αποπροσαρτήθηκαν ✓",
            "status_mount_all": "Προσάρτηση όλων των τόμων...",
            "status_unmount_all": "Αποπροσάρτηση όλων των τόμων...",
            "status_shutdown_cmd": "Η εντολή τερματισμού NAS στάλθηκε ✓",
            "status_timeout": "Λήξη χρόνου - Αδυναμία εκκίνησης διακομιστή",
            "status_no_volumes": "Δεν προσαρτήθηκαν τόμοι",
            "status_mount_failed": "Αποτυχία προσάρτησης",
            "status_cancelled": "Ακυρώθηκε - Η εφαρμογή κλείνει",
            "status_esc": "Πατήθηκε ESC - Η εφαρμογή κλείνει",
            "status_server_online": "Ο διακομιστής είναι online - αναμονή για υπηρεσία SMB...",
            "status_profile_changed": "Αλλαγή προφίλ σε: {}",
            "status_switching": "Μετάβαση σε προφίλ: {}...",
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Ακύρωση",
            "btn_start_nas": "Εκκίνηση NAS",
            "btn_settings": "Ρυθμίσεις (Cmd+E)",
            "btn_select_all": "Όλα",
            "btn_save": "Αποθήκευση",
            "btn_reset": "Επαναφορά",
            "btn_info": "ℹ",
            "btn_profile": "Προφίλ",
            "tooltip_shutdown_both": "Τερματισμός Mac και NAS σε 2 λεπτά",
            "tooltip_shutdown_nas": "Τερματισμός μόνο NAS",
            "tooltip_cancel": "Κλείνει την εφαρμογή",
            "tooltip_start_nas": "Εκκίνηση NAS μέσω Wake-on-LAN",
            "tooltip_settings": "Ρυθμίσεις (Cmd+E)",
            "timer_shutdown": "Αυτόματος τερματισμός σε {} δευτερόλεπτα - ENTER για μόνο NAS",
            "timer_start": "Αυτόματη εκκίνηση σε {} δευτερόλεπτα - ENTER για άμεση εκκίνηση",
            "volumes_title": "Διαθέσιμοι τόμοι",
            "volumes_title_offline": "Προσάρτηση τόμων κατά την εκκίνηση",
            "volumes_hint": "Σημείωση: Ο πρώτος τόμος στη λίστα αντιμετωπίζεται αυτόματα ως κύριος τόμος και δεν μπορεί να απενεργοποιηθεί.",
            "volumes_mount_tooltip": "Προσαρτάται αυτόματα κατά την εκκίνηση του διακομιστή",
            "config_title": "AnyNasPy - Ρυθμίσεις",
            "config_tab_profiles": "Προφίλ διακομιστή",
            "config_tab_general": "Γενικά",
            "config_tab_volumes": "Τόμοι",
            "config_tab_timing": "Χρονικές ρυθμίσεις",
            "config_language": "Γλώσσα:",
            "config_nas_group": "Ρυθμίσεις διακομιστή NAS",
            "config_nas_user": "Όνομα χρήστη:",
            "config_nas_dns": "Όνομα DNS:",
            "config_nas_ip": "Διεύθυνση IP:",
            "config_nas_mac": "Διεύθυνση MAC:",
            "config_ssh_key": "Διαδρομή κλειδιού SSH:",
            "config_volumes_group": "Τόμοι",
            "config_volumes_label": "Τόμοι (ένα όνομα ανά γραμμή):",
            "config_time_group": "Χρονικές ρυθμίσεις (δευτερόλεπτα)",
            "config_auto_shutdown": "Καθυστέρηση αυτόματου τερματισμού:",
            "config_auto_start": "Καθυστέρηση αυτόματης εκκίνησης:",
            "config_wol_wait": "Χρόνος αναμονής WOL (μέγιστος):",
            "config_smb_wait": "Χρόνος αναμονής SMB:",
            "config_mount_retries": "Επαναλήψεις προσάρτησης:",
            "config_status_file": "Αρχείο κατάστασης",
            "config_json_path": "Αρχείο διαμόρφωσης JSON:",
            "config_profile_name": "Όνομα προφίλ:",
            "config_profile_active": "Ενεργό προφίλ",
            "config_profile_set_active": "Ορισμός ως ενεργό προφίλ",
            "config_profile_list": "Υπάρχοντα προφίλ:",
            "config_profile_new": "Νέο προφίλ",
            "config_profile_delete": "Διαγραφή προφίλ",
            "config_profile_duplicate": "Δημιουργία αντιγράφου προφίλ",
            "config_profile_rename": "Μετονομασία",
            "config_profile_required": "Απαιτείται όνομα προφίλ.",
            "config_profile_exists": "Υπάρχει ήδη προφίλ με αυτό το όνομα.",
            "config_profile_deleted": "Το προφίλ '{}' διαγράφηκε.",
            "config_profile_duplicated": "Το προφίλ '{}' αντιγράφηκε ως '{}'.",
            "config_profile_renamed": "Το προφίλ μετονομάστηκε σε '{}'.",
            "config_profile_activated": "Το προφίλ '{}' είναι τώρα ενεργό.",
            "config_find_ip": "🔍 Εύρεση IP",
            "config_find_ip_tooltip": "Αυτόματη εύρεση της IP του διακομιστή στο δίκτυο",
            "config_ssh_help": "? Βοήθεια",
            "config_mac_help": "? Βοήθεια",
            "config_mac_help_tooltip": "Οδηγίες για την εύρεση της διεύθυνσης MAC",
            "msg_ip_found": "Η IP του διακομιστή βρέθηκε επιτυχώς:\n\n{}\n\nΗ IP καταχωρήθηκε στο πεδίο.",
            "msg_ip_not_found": "Δεν ήταν δυνατή η αυτόματη εύρεση της IP του διακομιστή.\n\nΠαρακαλώ εισάγετε τη διεύθυνση IP χειροκίνητα.\n\nΣυμβουλές:\n• Ελέγξτε το όνομα DNS στις ρυθμίσεις\n• Βεβαιωθείτε ότι ο NAS είναι ενεργοποιημένος\n• Βρείτε την IP στη διεπαφή DSM στην ενότητα 'Σύστημα > Δίκτυο'",
            "msg_reset_confirm": "Επαναφορά όλων των ρυθμίσεων στις προεπιλεγμένες τιμές;",
            "msg_reset_title": "Επαναφορά",
            "msg_reset_done": "Όλες οι ρυθμίσεις επαναφέρθηκαν στις προεπιλεγμένες τιμές.",
            "msg_delete_confirm": "Θέλετε σίγουρα να διαγράψετε το προφίλ '{}';",
            "msg_delete_title": "Διαγραφή προφίλ",
            "msg_no_active_profile": "Δεν έχει επιλεγεί ενεργό προφίλ.",
            "info_title": "Σχετικά με το AnyNasPy",
            "info_version": "Έκδοση",
            "info_copyright": "Πνευματικά δικαιώματα",
            "info_license": "Άδεια χρήσης",
            "info_impressum": "Στοιχεία εκδότη",
            "info_developer": "Προγραμματιστής",
            "info_contact": "Επικοινωνία",
            "info_license_text": "Άδεια MIT",
            "say_timer_shutdown": "Αυτόματος τερματισμός Mac και NAS σε {} δευτερόλεπτα - Enter για μόνο NAS - Escape για ακύρωση",
            "say_timer_start": "Ο διακομιστής NAS θα εκκινηθεί σε {} δευτερόλεπτα - Enter για άμεση εκκίνηση",
            "say_server_online": "Ο διακομιστής NAS είναι προσβάσιμος",
            "say_server_offline": "Ο διακομιστής NAS είναι εκτός λειτουργίας",
            "say_shutdown_started": "Έναρξη τερματισμού",
            "say_nas_shutdown": "Ο NAS τερματίζεται",
            "say_starting_nas": "Εκκίνηση NAS",
            "say_cancelled": "Ακυρώθηκε",
            "say_waiting_server": "Αναμονή για εκκίνηση διακομιστή",
            "say_wol_failed": "Σφάλμα κατά την αποστολή",
            "say_server_reachable": "Ο διακομιστής είναι προσβάσιμος",
            "say_mount_volume": "{} έτοιμο",
            "say_unmount_volume": "Αποπροσάρτηση {}",
            "say_mount_all": "Προσάρτηση όλων των τόμων",
            "say_unmount_all": "Αποπροσάρτηση όλων των τόμων",
            "say_mount_error": "Σφάλμα κατά την προσάρτηση",
            "say_unmount_error": "Σφάλμα κατά την αποπροσάρτηση",
            "say_mount_failed": "Δεν προσαρτήθηκαν τόμοι",
            "say_settings_opened": "Οι ρυθμίσεις άνοιξαν",
            "say_settings_saved": "Οι ρυθμίσεις αποθηκεύτηκαν",
            "say_settings_cancelled": "Οι ρυθμίσεις ακυρώθηκαν",
            "say_workaround_deleted": "Το αρχείο workaround διαγράφηκε",
            "say_server_timeout": "Λήξη χρόνου εκκίνησης διακομιστή",
            "say_profile_changed": "Αλλαγή προφίλ σε {}",
            "ssh_key_create_title": "Δημιουργία κλειδιού SSH",
            "ssh_key_create_question": "Θέλετε να δημιουργήσετε ένα νέο ζεύγος κλειδιών SSH;",
            "ssh_key_create_existing": "Το κλειδί SSH '{}' υπάρχει ήδη.\nΘέλετε να το αντικαταστήσετε;",
            "ssh_key_create_comment": "Σχόλιο για το κλειδί SSH (προαιρετικό):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "Το κλειδί SSH δημιουργήθηκε: {}",
            "ssh_key_create_error": "Σφάλμα κατά τη δημιουργία του κλειδιού SSH",
            "ssh_key_create_timeout": "Λήξη χρόνου κατά τη δημιουργία κλειδιού",
            "ssh_key_create_failed": "Το ssh-keygen επέστρεψε σφάλμα:\n{}",
            "ssh_key_create_passphrase": "Φράση πρόσβασης για το κλειδί SSH (αφήστε κενό για καμία φράση πρόσβασης):",
            "ssh_key_create_passphrase_confirm": "Επιβεβαίωση φράσης πρόσβασης:",
            "ssh_key_create_passphrase_mismatch": "Οι φράσεις πρόσβασης δεν ταιριάζουν.",
            "ssh_key_create_info": "✅ Το ζεύγος κλειδιών SSH δημιουργήθηκε επιτυχώς:\n\n"
            "📁 Ιδιωτικό κλειδί: {}\n"
            "📁 Δημόσιο κλειδί: {}\n\n"
            "📋 Δημόσιο κλειδί για αντιγραφή:\n"
            "{}\n\n"
            "🔑 Πώς να εγκαταστήσετε το κλειδί στο NAS σας:\n"
            "1. Αντιγράψτε το δημόσιο κλειδί (παραπάνω)\n"
            "2. Επικολλήστε το στο αρχείο:\n"
            "   ~/.ssh/authorized_keys στο NAS\n"
            "3. Ή χρησιμοποιήστε:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Παρακαλώ εισάγετε άλλο όνομα αρχείου:",
            "ssh_key_exists_also": "Το κλειδί '{}' υπάρχει επίσης.\nΠαρακαλώ διαγράψτε το πρώτα ή επιλέξτε άλλο όνομα.",
            "ssh_key_passphrase_title": "Φράση πρόσβασης",
            "ssh_key_passphrase_question": "Θέλετε να χρησιμοποιήσετε φράση πρόσβασης για το κλειδί SSH;\n\nΧωρίς φράση πρόσβασης: Δυνατότητα αυτόματης σύνδεσης, λιγότερο ασφαλές.\nΜε φράση πρόσβασης: Πιο ασφαλές, αλλά απαιτείται εισαγωγή σε κάθε σύνδεση.",
            "ssh_key_passphrase_enter": "Εισαγωγή φράσης πρόσβασης",
            "ssh_key_passphrase_label": "Φράση πρόσβασης για το κλειδί SSH (τουλάχιστον 4 χαρακτήρες):",
            "ssh_key_passphrase_none": "Καμία φράση πρόσβασης",
            "ssh_key_passphrase_none_question": "Δεν εισαγάγατε φράση πρόσβασης.\nΘέλετε να δημιουργήσετε το κλειδί χωρίς φράση πρόσβασης;",
            "ssh_key_passphrase_short": "Η φράση πρόσβασης είναι πολύ σύντομη",
            "ssh_key_passphrase_short_message": "Η φράση πρόσβασης πρέπει να έχει τουλάχιστον 4 χαρακτήρες.",
            "ssh_key_passphrase_confirm": "Επιβεβαίωση φράσης πρόσβασης",
            "ssh_key_passphrase_confirm_label": "Εισαγάγετε ξανά τη φράση πρόσβασης:",
            "ssh_key_passphrase_mismatch_title": "Σφάλμα φράσης πρόσβασης",
            "ssh_key_passphrase_mismatch_message": "Οι φράσεις πρόσβασης δεν ταιριάζουν.",
            "config_ssh_open": "Άνοιγμα",
            "config_ssh_open_tooltip": "Επιλογή κλειδιού SSH ή άνοιγμα φακέλου",
            "config_ssh_create": "Δημιουργία",
            "config_ssh_create_tooltip": "Δημιουργία νέου ζεύγους κλειδιών SSH",
            "config_ssh_help_tooltip": "Εμφάνιση βοήθειας για το κλειδί SSH",
            "config_ssh_select": "Επιλογή κλειδιού SSH",
            "config_json_open": "Άνοιγμα",
            "config_json_open_tooltip": "Άνοιγμα φακέλου διαμόρφωσης JSON",
            "config_error": "Σφάλμα",
            "config_shutdown_mac_delay": "Χρόνος αναμονής μεταξύ τερματισμού NAS και Mac:",
            "info_third_party": "Βιβλιοθήκες τρίτων",
            "info_pyqt5_license": "Αυτή η εφαρμογή χρησιμοποιεί το PyQt5, το οποίο διατίθεται υπό την GNU General Public License v3 (GPLv3).\nΠνευματικά δικαιώματα (c) Riverbank Computing Limited.\n\nΤο πλήρες κείμενο της άδειας είναι διαθέσιμο στη διεύθυνση https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Ανίχνευση τόμων",
            "volumes_add": "Προσθήκη",
            "volumes_delete": "Διαγραφή",
            "volumes_move_up": "Μετακίνηση προς τα πάνω",
            "volumes_move_down": "Μετακίνηση προς τα κάτω",
            "volumes_available": "Διαθέσιμοι τόμοι:",
            "volumes_no_volumes": "Δεν βρέθηκαν τόμοι.",
            "volumes_detection_failed": "Αποτυχία ανίχνευσης τόμων.",
            "volumes_detection_success": "Οι τόμοι εντοπίστηκαν με επιτυχία.",
            "volumes_confirm_delete": "Διαγραφή του τόμου '{}' σίγουρα;",
            "volumes_enter_name": "Εισαγάγετε το όνομα του νέου τόμου:",
            "volumes_name_exists": "Υπάρχει ήδη τόμος με αυτό το όνομα.",
            "msg_invalid_ip": "Η διεύθυνση IP που εισήχθη δεν είναι έγκυρη.\nΠαρακαλώ εισάγετε μια έγκυρη διεύθυνση IPv4 (π.χ. 192.168.1.100).",
            "msg_select_volume": "Παρακαλώ επιλέξτε έναν τόμο.",
            "msg_cannot_delete_main_volume": "Ο πρώτος τόμος (κύριος τόμος) δεν μπορεί να διαγραφεί.",
            "profile_cannot_delete_last": "Το τελευταίο προφίλ δεν μπορεί να διαγραφεί.",
            "status_wol_sending": "Αποστολή μαγικού πακέτου...",
            "status_wol_method_failed": "Η μέθοδος Python απέτυχε, δοκιμή της επόμενης...",
            "status_trying_wakeonlan": "Δοκιμή wakeonlan...",
            "status_trying_etherwake": "Δοκιμή etherwake...",
            "ssh_key_system_key_warning": "Προειδοποίηση ασφαλείας",
            "ssh_key_system_key_message": "Το όνομα '{}' είναι κλειδί συστήματος και δεν θα αντικατασταθεί.\nΠαρακαλώ επιλέξτε άλλο όνομα (π.χ. synaspy_rsa).",
            "profile_name_exists": "Υπάρχει ήδη προφίλ με το όνομα '{}'.",
            "config_profile_created": "Το προφίλ '{}' δημιουργήθηκε.",
            "config_profile_create_failed": "Αποτυχία δημιουργίας προφίλ.",
            "config_profile_rename_failed": "Η μετονομασία απέτυχε.",
            "config_profile_duplicate_name": "Όνομα για το αντιγραμμένο προφίλ:",
            "config_profile_duplicate_failed": "Η αντιγραφή απέτυχε.",
            "config_profile_delete_failed": "Η διαγραφή απέτυχε.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Τερματίζει μόνο το Mac (το NAS παραμένει ενεργό, χωρίς WOL)",
            "status_shutdown_mac_only": "Τερματισμός μόνο του Mac...",
            "say_shutdown_mac_only": "Το Mac τερματίζεται, το NAS παραμένει ενεργό",

            "btn_scheduled_shutdown": "🕐 Προγραμματισμένος τερματισμός",
            "tooltip_scheduled_shutdown": "Τερματίζει μετά από χρόνο που επιλέγει ο χρήστης",
            "btn_scheduled_shutdown_offline": "🕐 Προγραμματισμένος τερματισμός Mac",
            "tooltip_scheduled_shutdown_offline": "Τερματίζει μόνο το Mac μετά από επιλεγμένο χρόνο (το NAS είναι εκτός σύνδεσης)",
            "btn_cancel_scheduled": "⏹ Ακύρωση αντίστροφης μέτρησης",
            "tooltip_cancel_scheduled": "Ακυρώνει την ενεργή αντίστροφη μέτρηση",

            "sched_dialog_title": "Προγραμματισμένος τερματισμός",
            "sched_target_label": "Στόχος:",
            "sched_target_both": "🖥️ Mac + NAS  (πλήρης τερματισμός)",
            "sched_target_nas": "🗄️ Μόνο NAS  (το Mac παραμένει ενεργό)",
            "sched_target_mac": "💻 Μόνο Mac  (το NAS παραμένει ενεργό)",

            "sched_wait_label": "Χρόνος αναμονής μέχρι τον τερματισμό:",
            "sched_hours": "Ώρες",
            "sched_minutes": "Λεπτά",

            "sched_caffeinate_label": "Επιλογή caffeinate (κρατά το Mac σε εγρήγορση):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Συνιστάται: Το σύστημα σε εγρήγορση, η οθόνη μπορεί να σβήσει  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Αποτροπή μόνο αδράνειας και δίσκου (η οθόνη παραμένει αναμμένη)  (-i -m)",
            "sched_caffeinate_d": "Η οθόνη παραμένει επίσης αναμμένη  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Προσομοίωση δραστηριότητας χρήστη (φωτεινή οθόνη, σύστημα σε εγρήγορση)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Μέγιστο: Οθόνη + σύστημα + δίσκος μόνιμα σε εγρήγορση  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Ανενεργό (κανονική εξοικονόμηση ενέργειας – το σύστημα μπορεί να κοιμηθεί)",

            "sched_caffeinate_hint": (
                "💡 Εκπαιδευτικό στοιχείο: Χρησιμοποίησε τις σημαίες caffeinate απευθείας στο τερματικό:\n"
                "   -i  αποτρέπει την αδράνεια του συστήματος\n"
                "   -m  αποτρέπει την αδράνεια του δίσκου (ο σκληρός δίσκος δεν κοιμάται)\n"
                "   -s  αποτρέπει την αδράνεια του συστήματος (μόνο με τροφοδοτικό)\n"
                "   -d  αποτρέπει την αδράνεια της οθόνης (η οθόνη παραμένει αναμμένη)\n"
                "   -u  προσομοιώνει τη δραστηριότητα του χρήστη (η οθόνη παραμένει φωτεινή)\n"
                "   -w PID  τερματίζει το caffeinate όταν τελειώσει η διεργασία PID\n"
                "Παράδειγμα:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Ο τερματισμός προγραμματίστηκε για: {}",
            "sched_countdown_label": "Αντίστροφη μέτρηση: {} μέχρι τον τερματισμό ({})",
            "sched_started": "Ο χρονοδιακόπτης ξεκίνησε.\n\nΣτόχος: {}\nΔιάρκεια: {}\nΤέλος: {}",
            "sched_cancelled": "Ο χρονοδιακόπτης ακυρώθηκε",
            "sched_already_active": "Εκτελείται ήδη ένας χρονοδιακόπτης. Να ακυρωθεί πρώτα;",
            "sched_invalid_time": "Εισήγαγε έγκυρο χρόνο (τουλάχιστον 1 λεπτό).",
            "sched_max_time": "Μέγιστο επιτρεπόμενο 720 ώρες (30 ημέρες).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Ο χρονοδιακόπτης ξεκίνησε. Το Mac και το NAS θα τερματιστούν σε {}."
            ),
            "sched_voice_started_nas": (
                "Ο χρονοδιακόπτης ξεκίνησε. Μόνο το NAS θα τερματιστεί σε {}. "
                "Το Mac παραμένει ενεργό."
            ),
            "sched_voice_started_mac": (
                "Ο χρονοδιακόπτης ξεκίνησε. Μόνο το Mac θα τερματιστεί σε {}. "
                "Το NAS παραμένει ενεργό."
            ),
            "sched_voice_started_nothing": (
                "Ο χρονοδιακόπτης ξεκίνησε. Όταν λήξει, δεν θα εκτελεστεί τίποτα. "
                "Το caffeinate παραμένει ενεργό μέχρι τότε."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Το Mac παραμένει σε εγρήγορση για {}. "
                "Η οθόνη μπορεί να σβήσει. "
                "Όταν λήξει, δεν θα εκτελεστεί τίποτα."
            ),
            "sched_voice_nothing_im": (
                "Το Mac παραμένει σε εγρήγορση για {}. "
                "Η οθόνη παραμένει αναμμένη. "
                "Όταν λήξει, δεν θα εκτελεστεί τίποτα."
            ),
            "sched_voice_nothing_d": (
                "Το Mac και η οθόνη παραμένουν αναμμένα για {}. "
                "Όταν λήξει, δεν θα εκτελεστεί τίποτα."
            ),
            "sched_voice_nothing_u": (
                "Το Mac παραμένει ενεργό για {}. "
                "Η οθόνη παραμένει φωτεινή. "
                "Όταν λήξει, δεν θα εκτελεστεί τίποτα."
            ),
            "sched_voice_nothing_full": (
                "Το Mac παραμένει πλήρως ενεργό για {} – οθόνη και σύστημα συνεχώς σε εγρήγορση. "
                "Όταν λήξει, δεν θα εκτελεστεί τίποτα."
            ),
            "sched_voice_nothing_off": (
                "Ο χρονοδιακόπτης εκτελείται για {}. "
                "Όταν λήξει, δεν θα εκτελεστεί τίποτα. "
                "Προσοχή: Το Mac μπορεί να μεταβεί σε κατάσταση αναμονής."
            ),
            "sched_voice_cancelled": "Ο χρονοδιακόπτης ακυρώθηκε",
            "sched_caffeinate_failed": "Δεν ήταν δυνατή η εκκίνηση του caffeinate:\n{}",
            "sched_target_required": "Επίλεξε έναν στόχο.",
            "sched_tooltip_active": "Ο χρονοδιακόπτης εκτελείται – κάνε κλικ για ακύρωση",

            "status_scheduled_active": "Ο χρονοδιακόπτης είναι ενεργός - απομένουν {}",
            "status_scheduled_triggered": "Ο χρονοδιακόπτης έληξε - εκκίνηση {}",
            "status_scheduled_cancelled": "Ο χρονοδιακόπτης ακυρώθηκε",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Ο χρονοδιακόπτης είναι ενεργός",
            "close_blocked_text": (
                "<b>Εκτελείται ακόμα ένας χρονοδιακόπτης!</b><br><br>"
                "Προγραμματισμένο: {}<br>"
                "Απομένουν: <b>{}</b><br>"
                "Στις: {}<br><br>"
                "Αν κλείσεις τώρα, ο προγραμματισμένος τερματισμός "
                "<b>δεν θα εκτελεστεί πλέον</b>."
            ),
            "close_blocked_yes": "Κλείσιμο οπωσδήποτε",
            "close_blocked_no": "Να συνεχίσει η εφαρμογή",
            "close_blocked_cancel_text": (
                "Εκτελείται ακόμα ένας χρονοδιακόπτης.\n\n"
                "Θέλεις πραγματικά να κλείσεις την εφαρμογή;\n"
                "(Ο προγραμματισμένος τερματισμός θα απορριφθεί.)"
            ),
            "close_blocked_log_aborted": "Το κλείσιμο ακυρώθηκε (χρονοδιακόπτης ενεργός)",
            "close_blocked_log_discarded": (
                "Η εφαρμογή κλείνει παρά τον ενεργό χρονοδιακόπτη – ο χρονοδιακόπτης απορρίφθηκε"
            ),
            "close_blocked_log_cancel_aborted": (
                "Το κλείσιμο της εφαρμογής ακυρώθηκε μέσω του κουμπιού Ακύρωση"
            ),
            "duration_day": "ημέρα",
            "duration_days": "ημέρες",
            "duration_hour": "ώρα",
            "duration_hours": "ώρες",
            "duration_minute": "λεπτό",
            "duration_minutes": "λεπτά",
            "duration_connector_and": "και",

            "tooltip_pause_timer": "Παύση / συνέχιση χρονοδιακόπτη",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Το χρονόμετρο σε παύση – απομένουν {} δευτερόλεπτα",
            "timer_resumed": "Το χρονόμετρο συνεχίστηκε",
            "say_timer_paused": "Το χρονόμετρο σε παύση",
            "say_timer_resumed": "Το χρονόμετρο συνεχίστηκε",
            "tooltip_pause_timer": "Παύση/συνέχιση χρονομέτρου",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Η φωνητική έξοδος ενεργοποιήθηκε",
            "speech_enabled_hint": (
                "Εκφωνεί μηνύματα κατάστασης, επιβεβαιώσεις έντασης και "
                "πληροφορίες χρονομέτρου μέσω της φωνητικής εξόδου του macOS. "
                "Όταν απενεργοποιηθεί, η εφαρμογή λειτουργεί σιωπηλά."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Για το προγραμματισμένο τερματισμό του Mac απαιτείται "
                "ο κωδικός πρόσβασης διαχειριστή.\n\n"
                "Αποθηκεύεται με ασφάλεια στο κλειδοθήκη του macOS και "
                "χρησιμοποιείται μόνο κατά τον τερματισμό.\n\n"
                "Ρύθμιση τώρα;"
            ),
            "mac_pw_dialog_title": "Κωδικός πρόσβασης διαχειριστή",
            "mac_pw_dialog_message": (
                "Για τον τερματισμό του Mac απαιτείται ο κωδικός πρόσβασης "
                "διαχειριστή.\n\n"
                "Αποθηκεύεται με ασφάλεια στο κλειδοθήκη του macOS και "
                "χρησιμοποιείται μόνο κατά τον τερματισμό."
            ),
            "mac_pw_wrong_password": (
                "Ο κωδικός πρόσβασης είναι λανθασμένος.\n\n"
                "Δοκιμάστε ξανά."
            ),
            "mac_pw_test_failed": (
                "Σφάλμα κατά τον έλεγχο κωδικού πρόσβασης:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Το χρονόμετρο δεν ξεκίνησε επειδή η "
                "εισαγωγή κωδικού πρόσβασης ακυρώθηκε.\n\n"
                "Χωρίς κωδικό πρόσβασης ο Mac δεν μπορεί να τερματιστεί."
            ),
            "clear_password_title": "Διαγραφή αποθηκευμένου κωδικού πρόσβασης",
            "clear_password_message": (
                "Διαγραφή του κωδικού πρόσβασης διαχειριστή που είναι "
                "αποθηκευμένος στο κλειδοθήκη;\n\n"
                "Κατά τον επόμενο προγραμματισμένο τερματισμό, ο κωδικός "
                "πρόσβασης θα ζητηθεί ξανά."
            ),
            "clear_password_success": "Ο κωδικός πρόσβασης αφαιρέθηκε από το κλειδοθήκη.",
            "clear_password_failed": "Δεν ήταν δυνατή η διαγραφή του κωδικού πρόσβασης.",
            "clear_password_description": (
                "Αφαιρεί τον κωδικό πρόσβασης διαχειριστή που είναι "
                "αποθηκευμένος στο κλειδοθήκη του macOS. Κατά τον επόμενο "
                "προγραμματισμένο τερματισμό θα ζητηθεί ξανά."
            ),
            "clear_password_button": "Διαγραφή αποθηκευμένου κωδικού πρόσβασης",
            "shutdown_no_password_message": (
                "Δεν ήταν δυνατός ο τερματισμός του Mac.\n\n"
                "Δεν υπάρχει ούτε κανόνας NOPASSWD στο sudoers ούτε "
                "αποθηκευμένος κωδικός πρόσβασης στο κλειδοθήκη.\n\n"
                "Ρυθμίστε ξανά τον προγραμματισμένο τερματισμό."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Προειδοποίηση",
            "warning_eject_failed_continue": (
                "Δεν ήταν δυνατή η σωστή εξαγωγή των δικτυακών μονάδων δίσκου.\n\n"
                "Εάν εξακολουθούν να αντιγράφονται δεδομένα ή υπάρχουν "
                "ανοιχτά αρχεία, ενδέχεται να προκληθεί απώλεια δεδομένων.\n\n"
                "Να συνεχιστεί ο τερματισμός παρ' όλα αυτά;"
            ),
            "auto_timer_disabled_no_pw": (
                "Ο αυτόματος τερματισμός απενεργοποιήθηκε – δεν υπάρχει "
                "κωδικός πρόσβασης διαχειριστή. Εισαγάγετέ τον μία φορά "
                "στην επόμενη προτροπή."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Ναι",
            "btn_no": "Όχι",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Να μην τερματιστεί τίποτα  (Ο Mac παραμένει σε εγρήγορση – π.χ. για σενάρια δημιουργίας αντιγράφων ασφαλείας)",
            "sched_countdown_coffee_label": "⏳ caffeinate ενεργό: απομένουν {} ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Ο χρονοδιακόπτης καφέ είναι ακόμα ενεργός",
            "coffee_conflict_message": (
                "Ένας χρονοδιακόπτης καφέ εκτελείται ακόμα:\n\n"
                "Υπόλοιπο: {}\n\n"
                "Αν τερματίσεις τώρα, ο χρονοδιακόπτης καφέ θα ακυρωθεί "
                "και το caffeinate θα σταματήσει.\n\n"
                "Να τερματιστεί ούτως ή άλλως;"
            ),
            "shutdown_timer_conflict_title": "Ο χρονοδιακόπτης τερματισμού είναι ακόμα ενεργός",
            "shutdown_timer_conflict_message": (
                "Ένας χρονοδιακόπτης τερματισμού εκτελείται ακόμα:\n\n"
                "Προγραμματισμένο: {}\n"
                "Υπόλοιπο: {}\n\n"
                "Αν τερματίσεις χειροκίνητα τώρα, ο χρονοδιακόπτης θα ακυρωθεί "
                "και θα πρέπει να προγραμματιστεί ξανά.\n\n"
                "Να τερματιστεί ούτως ή άλλως;"
            ),
            "tooltip_stop_timer": "Πλήρης διακοπή του χρονοδιακόπτη",
            "tooltip_stop_timer_inactive": "Κανένας χρονοδιακόπτης δεν είναι ενεργός",
            "timer_stopped_notice": "⏹ Ο χρονοδιακόπτης σταμάτησε – έτοιμος για επανεκκίνηση",
            "say_timer_stopped": "Ο χρονοδιακόπτης σταμάτησε",
            "say_timer_restarted": "Ο χρονοδιακόπτης επανεκκινήθηκε",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "Κατασκευαστής NAS:",
            "vendor_tooltip": (
                "Επιλέξτε τον κατασκευαστή του NAS σας. Καθορίζει τις εντολές "
                "τερματισμού και τις προεπιλεγμένες διαδρομές. Η 'Αυτόματη "
                "ανίχνευση' ελέγχει το NAS μέσω SSH."
            ),
            "vendor_auto_detect": "🔄 Αυτόματη ανίχνευση",
            "vendor_auto_detect_tooltip": (
                "Αυτόματη αναγνώριση κατασκευαστή μέσω SSH. "
                "Προϋπόθεση: Το κλειδί SSH και η διεύθυνση IP έχουν "
                "ρυθμιστεί σωστά."
            ),
            "vendor_detect_in_progress": "🔄 Ανίχνευση...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Γενικό Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Προσαρμοσμένο",
            "vendor_custom_hint": (
                "Προσαρμοσμένο: Προσαρμόστε τις εντολές τερματισμού χειροκίνητα. "
                "Προεπιλογή: 'sudo shutdown -h now' (λειτουργεί στο "
                "80 % όλων των NAS με Linux)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Ο κατασκευαστής αναγνωρίστηκε: {}",
            "vendor_detect_success_question": (
                "Ο κατασκευαστής αναγνωρίστηκε: {}\n\n"
                "Να χρησιμοποιηθεί αυτός ο κατασκευαστής;\n"
                "(Τρέχουσα τιμή: {})"
            ),
            "vendor_detect_failed": (
                "Ο κατασκευαστής δεν μπόρεσε να αναγνωριστεί αυτόματα.\n\n"
                "Παρακαλώ επιλέξτε χειροκίνητα. Τα περισσότερα NAS "
                "με Linux λειτουργούν με 'Γενικό Linux'."
            ),
            "vendor_detect_no_ssh": (
                "Η αυτόματη ανίχνευση απαιτεί πρόσβαση SSH.\n\n"
                "Παρακαλώ ελέγξτε:\n"
                "• Η διαδρομή του κλειδιού SSH είναι σωστή\n"
                "• Η διεύθυνση IP είναι σωστή\n"
                "• Το SSH είναι ενεργοποιημένο στο NAS\n"
                "• Το κλειδί SSH είναι εγκατεστημένο στο NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Παρακαλώ εισάγετε πρώτα το κλειδί SSH και τη διεύθυνση IP."
            ),
            "vendor_detect_nas_offline": (
                "Ο διακομιστής NAS δεν αποκρίνεται.\n\n"
                "Παρακαλώ ελέγξτε:\n"
                "• Είναι ενεργοποιημένο το NAS;\n"
                "• Είναι σωστή η διεύθυνση IP;\n"
                "• Βρίσκεται το NAS στο ίδιο δίκτυο;\n\n"
                "Ενεργοποιήστε το NAS και δοκιμάστε ξανά."
            ),
            "vendor_detect_error": "Σφάλμα κατά την αυτόματη ανίχνευση:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "Το κλειδί SSH δεν βρέθηκε:\n\n{}\n\n"
                "Παρακαλώ ελέγξτε τη διαδρομή στις ρυθμίσεις."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Εντολή τερματισμού:",
            "custom_cmd_tooltip": (
                "Η εντολή που αποστέλλεται στο NAS μέσω SSH. "
                "Διαχωρίστε πολλαπλές εντολές με ερωτηματικό."
            ),
            "custom_cmd_hint": (
                "💡 Διαχωρίστε πολλαπλές εντολές με ερωτηματικό — "
                "χρησιμοποιείται η πρώτη επιτυχής. "
                "Παράδειγμα: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Εμφάνιση βοήθειας για εντολές τερματισμού",
            "custom_cmd_help_title": "Τυπικές εντολές τερματισμού",
            "custom_cmd_help_text": (
                "<h3>Τυπικές εντολές τερματισμού ανά κατασκευαστή</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (γενικό):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Πολλαπλές εντολές (αλυσίδα εφεδρικών)</h4>"
                "<p>Εάν η πρώτη εντολή αποτύχει, δοκιμάζεται η επόμενη. "
                "Διαχωρισμός με ερωτηματικό:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Συμβουλή:</b> Επιλέξτε πρώτα την πιο πιθανή εντολή, "
                "μετά τις εναλλακτικές ως εφεδρικές.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Ανίχνευση τόμων μέσω SSH...",
            "volumes_detection_via_paths": (
                "🔍 Αναζήτηση σε διαδρομές ειδικές για τον κατασκευαστή..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Εφεδρική επιλογή: Αναζήτηση μέσω smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Αναζήτηση τόμων μέσω SSH... Η αναζήτηση μπορεί "
                "να διαρκέσει μερικά δευτερόλεπτα."
            ),
            "volumes_detect_panel_success": (
                "Βρέθηκαν {} τόμοι — {} προστέθηκαν νέοι, "
                "{} υπάρχουν ήδη"
            ),
            "volumes_detect_panel_partial": (
                "Βρέθηκαν {} τόμοι — όλοι υπάρχουν ήδη στη λίστα"
            ),
            "volumes_detect_panel_failed": (
                "Δεν βρέθηκαν τόμοι. "
                "Παρακαλώ εισάγετε τους τόμους χειροκίνητα."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Ανίχνευση διεύθυνσης MAC...",
            "mac_detect_success": "✅ Η διεύθυνση MAC αναγνωρίστηκε: {}",
            "mac_detect_success_dialog": (
                "Η διεύθυνση MAC αναγνωρίστηκε με επιτυχία.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Η τιμή εισήχθη στο πεδίο MAC."
            ),
            "mac_detect_failed": (
                "⚠ Η διεύθυνση MAC δεν μπόρεσε να αναγνωριστεί αυτόματα. "
                "Θα εμφανιστεί βοήθεια."
            ),
            "config_mac_find": "🔍 Εύρεση MAC",
            "config_mac_find_tooltip": (
                "Αυτόματη αναγνώριση της διεύθυνσης MAC. "
                "Εάν αποτύχει, θα εμφανιστεί οδηγός."
            ),
        },
        # "🇬🇧 English"
        "en": {
            "language": "Idioma:",
            # Main window
            "window_title": "NAS Management",
            "status_checking": "Checking server connection...",
            "status_online": "NAS Server is online ✓",
            "status_offline": "NAS Server is offline",
            "status_settings": "Settings opened - Timer stopped",
            "status_settings_saved": "Settings saved",
            "status_settings_cancelled": "Settings cancelled",
            "status_shutdown": "Shutting down NAS and Mac...",
            "status_shutdown_nas": "Shutting down NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ NAS shutdown sent, Mac is now shutting down...",
            "status_shutdown_nas_failed_mac_still": "⚠️ NAS shutdown failed, shutting down Mac anyway...",
            "status_starting": "Starting NAS via Wake-on-LAN...",
            "status_waiting": "Waiting for server to start...",
            "status_wol_sent": "Magic Packet sent",
            "status_wol_failed": "WOL failed",
            "status_mounting": "Mounting selected volumes...",
            "status_mounting_volume": "Mounting {}...",
            "status_mounted": "{} mounted ✓",
            "status_unmounting": "Ejecting {}...",
            "status_unmounted": "{} ejected ✓",
            "status_error": "Error: {} could not be mounted",
            "status_error_unmount": "Error: {} could not be ejected",
            "status_all_mounted": "All volumes mounted ✓",
            "status_all_unmounted": "All volumes ejected ✓",
            "status_mount_all": "Mounting all volumes...",
            "status_unmount_all": "Ejecting all volumes...",
            "status_shutdown_cmd": "NAS shutdown command sent ✓",
            "status_timeout": "Timeout - Server could not be started",
            "status_no_volumes": "No volumes mounted",
            "status_mount_failed": "Mounting failed",
            "status_cancelled": "Cancelled - App will close",
            "status_esc": "ESC pressed - App will close",
            "status_server_online": "Server online - waiting for SMB service...",
            "status_profile_changed": "Switched to profile: {}",
            "status_switching": "Switching to profile: {}...",
            # Buttons
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Cancel",
            "btn_start_nas": "Start NAS",
            "btn_settings": "Settings (Cmd+E)",
            "btn_select_all": "All",
            "btn_save": "Save",
            "btn_reset": "Reset",
            "btn_info": "ℹ",
            "btn_profile": "Profiles",
            # Tooltips
            "tooltip_shutdown_both": "Shuts down Mac and NAS in 2min",
            "tooltip_shutdown_nas": "Shuts down only NAS",
            "tooltip_cancel": "Closes the app",
            "tooltip_start_nas": "Starts NAS via Wake-on-LAN",
            "tooltip_settings": "Settings (Cmd+E)",
            # Timer
            "timer_shutdown": "Auto-shutdown in {} seconds - ENTER for NAS only",
            "timer_start": "Auto-start in {} seconds - ENTER for immediate start",
            # Volumes
            "volumes_title": "Available Volumes",
            "volumes_title_offline": "Volumes to mount on start",
            "volumes_hint": "Hint: The first volume in the list is automatically treated as the main volume and cannot be disabled.",
            "volumes_mount_tooltip": "Will be mounted automatically on server start",
            # Config Dialog
            "config_title": "AnyNasPy - Settings",
            "config_tab_profiles": "Server Profiles",
            "config_tab_general": "General",
            "config_tab_volumes": "Volumes",
            "config_tab_timing": "Timing",
            "config_language": "Language:",
            "config_nas_group": "NAS Server Settings",
            "config_nas_user": "Username:",
            "config_nas_dns": "DNS Name:",
            "config_nas_ip": "IP Address:",
            "config_nas_mac": "MAC Address:",
            "config_ssh_key": "SSH Key Path:",
            "config_volumes_group": "Volumes",
            "config_volumes_label": "Volumes (one name per line):",
            "config_time_group": "Time Settings (seconds)",
            "config_auto_shutdown": "Auto-shutdown delay:",
            "config_auto_start": "Auto-start delay:",
            "config_wol_wait": "WOL wait time (max):",
            "config_smb_wait": "SMB wait time:",
            "config_mount_retries": "Mount retries:",
            "config_status_file": "Status file",
            "config_json_path": "JSON configuration file:",
            "config_profile_name": "Profile name:",
            "config_profile_active": "Active Profile",
            "config_profile_set_active": "Set as active profile",
            "config_profile_list": "Existing Profiles:",
            "config_profile_new": "New Profile",
            "config_profile_delete": "Delete Profile",
            "config_profile_duplicate": "Duplicate Profile",
            "config_profile_rename": "Rename",
            "config_profile_required": "Profile name is required.",
            "config_profile_exists": "A profile with this name already exists.",
            "config_profile_deleted": "Profile '{}' was deleted.",
            "config_profile_duplicated": "Profile '{}' was duplicated as '{}'.",
            "config_profile_renamed": "Profile renamed to '{}'.",
            "config_profile_activated": "Profile '{}' is now active.",
            # Config Buttons
            "config_find_ip": "🔍 Find IP",
            "config_find_ip_tooltip": "Automatically find server IP in network",
            "config_ssh_help": "? Help",
            "config_mac_help": "? Help",
            "config_mac_help_tooltip": "Instructions to find MAC address",
            # Messages
            "msg_ip_found": "Server IP was successfully found:\n\n{}\n\nThe IP has been entered into the field.",
            "msg_ip_not_found": "Server IP could not be found automatically.\n\nPlease enter the IP address manually.\n\nTips:\n• Check the DNS name in settings\n• Make sure the NAS is turned on\n• Find the IP in DSM under 'System > Network'",
            "msg_reset_confirm": "Reset all settings to default values?",
            "msg_reset_title": "Reset",
            "msg_reset_done": "All settings have been reset to default values.",
            "msg_delete_confirm": "Really delete profile '{}'?",
            "msg_delete_title": "Delete Profile",
            "msg_no_active_profile": "No active profile selected.",
            # Info Dialog
            "info_title": "About AnyNasPy",
            "info_version": "Version",
            "info_copyright": "Copyright",
            "info_license": "License",
            "info_impressum": "Imprint",
            "info_developer": "Developer",
            "info_contact": "Contact",
            "info_license_text": "MIT License",
            # Language selection
            "language": "Language:",
            # Misc
            "say_timer_shutdown": "Mac and NAS Auto Shutdown in {} seconds - Enter for NAS only - Escape to cancel",
            "say_timer_start": "The NAS Server will start in {} seconds - Enter for immediate start",
            "say_server_online": "NAS Server is reachable",
            "say_server_offline": "NAS Server is offline",
            "say_shutdown_started": "Shutdown started",
            "say_nas_shutdown": "NAS is shutting down",
            "say_starting_nas": "Starting NAS",
            "say_cancelled": "Cancelled",
            "say_waiting_server": "Waiting for server start",
            "say_wol_failed": "Error sending",
            "say_server_reachable": "Server reachable",
            "say_mount_volume": "{} ready",
            "say_unmount_volume": "Ejecting {}",
            "say_mount_all": "Mounting all volumes",
            "say_unmount_all": "Ejecting all volumes",
            "say_mount_error": "Error mounting",
            "say_unmount_error": "Error ejecting",
            "say_mount_failed": "No volumes mounted",
            "say_settings_opened": "Settings opened",
            "say_settings_saved": "Settings saved",
            "say_settings_cancelled": "Settings cancelled",
            "say_workaround_deleted": "Workaround file deleted",
            "say_server_timeout": "Server start timeout",
            "say_profile_changed": "Switched to profile {}",
            "ssh_key_create_title": "Create SSH Key",
            "ssh_key_create_question": "Do you want to create a new SSH key pair?",
            "ssh_key_create_existing": "SSH key '{}' already exists.\nDo you want to overwrite it?",
            "ssh_key_create_comment": "Comment for the SSH key (optional):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH key created: {}",
            "ssh_key_create_error": "Error creating SSH key",
            "ssh_key_create_timeout": "SSH key creation timed out",
            "ssh_key_create_failed": "ssh-keygen returned an error:\n{}",
            "ssh_key_create_passphrase": "Passphrase for SSH key (leave empty for no passphrase):",
            "ssh_key_create_passphrase_confirm": "Confirm passphrase:",
            "ssh_key_create_passphrase_mismatch": "Passphrases do not match.",
            "ssh_key_create_info": "✅ SSH key pair created successfully:\n\n"
            "📁 Private Key: {}\n"
            "📁 Public Key: {}\n\n"
            "📋 Public Key to copy:\n"
            "{}\n\n"
            "🔑 How to install the key on your NAS:\n"
            "1. Copy the public key (above)\n"
            "2. Add it to the file:\n"
            "   ~/.ssh/authorized_keys on the NAS\n"
            "3. Or use:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Please enter a different filename:",
            "ssh_key_exists_also": "The key '{}' also exists.\nPlease delete it first or choose a different name.",
            "ssh_key_passphrase_title": "Passphrase",
            "ssh_key_passphrase_question": "Do you want to use a passphrase for the SSH key?\n\nWithout passphrase: Automatic connection possible, less secure.\nWith passphrase: More secure, but prompts on every connection.",
            "ssh_key_passphrase_enter": "Enter passphrase",
            "ssh_key_passphrase_label": "Passphrase for SSH key (at least 4 characters):",
            "ssh_key_passphrase_none": "No passphrase",
            "ssh_key_passphrase_none_question": "You did not enter a passphrase.\nDo you want to create the key without a passphrase?",
            "ssh_key_passphrase_short": "Passphrase too short",
            "ssh_key_passphrase_short_message": "The passphrase should be at least 4 characters long.",
            "ssh_key_passphrase_confirm": "Confirm passphrase",
            "ssh_key_passphrase_confirm_label": "Enter passphrase again:",
            "ssh_key_passphrase_mismatch_title": "Passphrase Error",
            "ssh_key_passphrase_mismatch_message": "The passphrases do not match.",
            "config_ssh_open": "Open",
            "config_ssh_open_tooltip": "Select SSH key or open folder",
            "config_ssh_create": "Create",
            "config_ssh_create_tooltip": "Create new SSH key pair",
            "config_ssh_help_tooltip": "Show SSH key help",
            "config_ssh_select": "Select SSH key",
            "config_json_open": "Open",
            "config_json_open_tooltip": "Open JSON configuration folder",
            "config_error": "Error",
            "config_shutdown_mac_delay": "Delay between NAS and Mac shutdown:",
            "info_third_party": "Third-Party Libraries",
            "info_pyqt5_license": "This application uses PyQt5, which is licensed under the GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nThe full license text can be viewed at https://www.gnu.org/licenses/gpl-3.0.html.",
            # --> ab hier neu
            "volumes_auto_detect": "Detect Volumes",
            "volumes_add": "Add",
            "volumes_delete": "Delete",
            "volumes_move_up": "Move Up",
            "volumes_move_down": "Move Down",
            "volumes_available": "Available volumes:",
            "volumes_no_volumes": "No volumes found.",
            "volumes_detection_failed": "Volume detection failed.",
            "volumes_detection_success": "Volumes successfully detected.",
            "volumes_confirm_delete": "Really delete volume '{}'?",
            "volumes_enter_name": "Please enter the name of the new volume:",
            "volumes_name_exists": "A volume with this name already exists.",
            "msg_invalid_ip": "The entered IP address is not valid.\nPlease enter a valid IPv4 address (e.g. 192.168.1.100).",
            "msg_select_volume": "Please select a volume.",
            "msg_cannot_delete_main_volume": "The first volume (main volume) cannot be deleted.",
            "profile_cannot_delete_last": "The last profile cannot be deleted.",
            "status_wol_sending": "Sending Magic Packet...",
            "status_wol_method_failed": "Python method failed, trying next...",
            "status_trying_wakeonlan": "Trying wakeonlan...",
            "status_trying_etherwake": "Trying etherwake...",
            "ssh_key_system_key_warning": "Security warning",
            "ssh_key_system_key_message": "The name '{}' is a system key and will not be overwritten!\nPlease choose a different name (e.g. synaspy_rsa).",
            "profile_name_exists": "A profile with the name '{}' already exists.",
            "profile_cannot_delete_last": "The last profile cannot be deleted.",
            "config_profile_created": "Profile '{}' has been created.",
            "config_profile_create_failed": "Failed to create profile.",
            "config_profile_rename_failed": "Rename failed.",
            "config_profile_duplicate_name": "Name for the duplicated profile:",
            "config_profile_duplicate_failed": "Duplicate failed.",
            "config_profile_delete_failed": "Delete failed.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Shuts down only the Mac (NAS stays on, no WOL)",
            "status_shutdown_mac_only": "Shutting down only the Mac...",
            "say_shutdown_mac_only": "Mac is shutting down, NAS stays on",

            "btn_scheduled_shutdown": "🕐 Scheduled shutdown",
            "tooltip_scheduled_shutdown": "Shuts down after a user-selected time",
            "btn_scheduled_shutdown_offline": "🕐 Schedule Mac shutdown",
            "tooltip_scheduled_shutdown_offline": "Shuts down only the Mac after a selected time (NAS is offline)",
            "btn_cancel_scheduled": "⏹ Cancel countdown",
            "tooltip_cancel_scheduled": "Cancels the active countdown",

            "sched_dialog_title": "Scheduled Shutdown",
            "sched_target_label": "Target:",
            "sched_target_both": "🖥️ Mac + NAS  (full shutdown)",
            "sched_target_nas": "🗄️ NAS only  (Mac stays on)",
            "sched_target_mac": "💻 Mac only  (NAS stays on)",

            "sched_wait_label": "Wait time until shutdown:",
            "sched_hours": "Hours",
            "sched_minutes": "Minutes",

            "sched_caffeinate_label": "caffeinate option (keeps the Mac awake):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Recommended: System awake, screen may dim  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Prevent idle & disk only (screen stays on)  (-i -m)",
            "sched_caffeinate_d": "Screen additionally stays on  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simulate user activity (screen bright, system awake)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maximum: Screen + system + disk permanently awake  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Off (normal power saving – system may sleep)",

            "sched_caffeinate_hint": (
                "💡 Learning fact: Use caffeinate flags directly in the terminal:\n"
                "   -i  prevents idle sleep of the system\n"
                "   -m  prevents disk sleep (hard drive does not sleep)\n"
                "   -s  prevents system sleep (only on power adapter)\n"
                "   -d  prevents display sleep (screen stays on)\n"
                "   -u  simulates user activity (display stays bright)\n"
                "   -w PID  terminates caffeinate when process PID ends\n"
                "Example:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Shutdown scheduled for: {}",
            "sched_countdown_label": "Countdown: {} until shutdown ({})",
            "sched_started": "Timer started.\n\nTarget: {}\nDuration: {}\nEnd: {}",
            "sched_cancelled": "Timer cancelled",
            "sched_already_active": "A timer is already running. Cancel it first?",
            "sched_invalid_time": "Please enter a valid time (at least 1 minute).",
            "sched_max_time": "Maximum 720 hours (30 days) allowed.",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Timer started. Mac and NAS will shut down in {}."
            ),
            "sched_voice_started_nas": (
                "Timer started. Only the NAS will shut down in {}. "
                "The Mac stays on."
            ),
            "sched_voice_started_mac": (
                "Timer started. Only the Mac will shut down in {}. "
                "The NAS stays on."
            ),
            "sched_voice_started_nothing": (
                "Timer started. Nothing will be executed when it expires. "
                "caffeinate remains active until then."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "The Mac stays awake for {}. "
                "The screen may dim. "
                "Nothing will be executed when it expires."
            ),
            "sched_voice_nothing_im": (
                "The Mac stays awake for {}. "
                "The screen stays on. "
                "Nothing will be executed when it expires."
            ),
            "sched_voice_nothing_d": (
                "The Mac and the screen stay on for {}. "
                "Nothing will be executed when it expires."
            ),
            "sched_voice_nothing_u": (
                "The Mac stays active for {}. "
                "The screen stays bright. "
                "Nothing will be executed when it expires."
            ),
            "sched_voice_nothing_full": (
                "The Mac stays fully active for {} – screen and system continuously awake. "
                "Nothing will be executed when it expires."
            ),
            "sched_voice_nothing_off": (
                "The timer runs for {}. "
                "Nothing will be executed when it expires. "
                "Caution: The Mac may enter sleep mode."
            ),
            "sched_voice_cancelled": "Timer cancelled",
            "sched_caffeinate_failed": "caffeinate could not be started:\n{}",
            "sched_target_required": "Please select a target.",
            "sched_tooltip_active": "Timer running – click to cancel",

            "status_scheduled_active": "Timer active - {} remaining",
            "status_scheduled_triggered": "Timer expired - starting {}",
            "status_scheduled_cancelled": "Timer cancelled",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Timer active",
            "close_blocked_text": (
                "<b>A timer is still running!</b><br><br>"
                "Scheduled: {}<br>"
                "Remaining: <b>{}</b><br>"
                "At: {}<br><br>"
                "If you close now, the scheduled shutdown "
                "will <b>no longer be executed</b>."
            ),
            "close_blocked_yes": "Close anyway",
            "close_blocked_no": "Keep app running",
            "close_blocked_cancel_text": (
                "A timer is still running.\n\n"
                "Do you really want to close the app?\n"
                "(The scheduled shutdown will then be discarded.)"
            ),
            "close_blocked_log_aborted": "Close aborted (timer active)",
            "close_blocked_log_discarded": (
                "App is closing despite active timer – timer discarded"
            ),
            "close_blocked_log_cancel_aborted": (
                "App close cancelled via Cancel button"
            ),
            # Building blocks for the spoken duration
            "duration_day": "day",
            "duration_days": "days",
            "duration_hour": "hour",
            "duration_hours": "hours",
            "duration_minute": "minute",
            "duration_minutes": "minutes",
            "duration_connector_and": "and",
            "tooltip_pause_timer": "Pause/resume timer",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Timer paused – {} seconds remaining",
            "timer_resumed": "Timer resumed",
            "say_timer_paused": "Timer paused",
            "say_timer_resumed": "Timer resumed",
            "tooltip_pause_timer": "Pause/resume timer",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Speech output enabled",
            "speech_enabled_hint": (
                "Speaks status messages, volume confirmations, and timer info "
                "via macOS speech output. When disabled, the "
                "app runs silently."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "The administrator password is required for scheduled "
                "Mac shutdown.\n\n"
                "It is stored securely in the macOS Keychain and only used "
                "during shutdown.\n\n"
                "Set up now?"
            ),
            "mac_pw_dialog_title": "Administrator password",
            "mac_pw_dialog_message": (
                "The administrator password is required for "
                "Mac shutdown.\n\n"
                "It is stored securely in the macOS Keychain and only used "
                "during shutdown."
            ),
            "mac_pw_wrong_password": (
                "The password is incorrect.\n\n"
                "Please try again."
            ),
            "mac_pw_test_failed": (
                "Error during password check:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "The timer was not started because the "
                "password entry was cancelled.\n\n"
                "Without a password, the Mac cannot be shut down."
            ),
            "clear_password_title": "Delete saved password",
            "clear_password_message": (
                "Delete the administrator password stored in the Keychain?\n\n"
                "On the next scheduled shutdown, the password will be "
                "requested again."
            ),
            "clear_password_success": "The password was removed from the Keychain.",
            "clear_password_failed": "The password could not be deleted.",
            "clear_password_description": (
                "Removes the administrator password stored in the macOS "
                "Keychain. On the next scheduled shutdown, "
                "it will be requested again."
            ),
            "clear_password_button": "Delete saved password",
            "shutdown_no_password_message": (
                "The Mac could not be shut down.\n\n"
                "Neither a NOPASSWD sudoers rule nor a saved "
                "password in the Keychain is available.\n\n"
                "Please set up the scheduled shutdown again."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Warning",
            "warning_eject_failed_continue": (
                "Network drives could not be ejected cleanly.\n\n"
                "If data is still being copied or files are open, "
                "data loss may occur.\n\n"
                "Continue with shutdown anyway?"
            ),
            "auto_timer_disabled_no_pw": (
                "Auto-shutdown disabled – no administrator password "
                "available. Please enter it once at the next prompt."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Yes",
            "btn_no": "No",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Don't shut down anything  (Mac stays awake – e.g. for backup scripts)",
            "sched_countdown_coffee_label": "⏳ caffeinate active: {} remaining ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Coffee timer still running",
            "coffee_conflict_message": (
                "A coffee timer is still running:\n\n"
                "Remaining: {}\n\n"
                "If you shut down now, the coffee timer will be cancelled "
                "and caffeinate will be stopped.\n\n"
                "Shut down anyway?"
            ),
            "shutdown_timer_conflict_title": "Shutdown timer still running",
            "shutdown_timer_conflict_message": (
                "A shutdown timer is still running:\n\n"
                "Scheduled: {}\n"
                "Remaining: {}\n\n"
                "If you shut down manually now, the timer will be cancelled "
                "and must be rescheduled.\n\n"
                "Shut down anyway?"
            ),
            "tooltip_stop_timer": "Stop timer completely",
            "tooltip_stop_timer_inactive": "No timer active",
            "timer_stopped_notice": "⏹ Timer stopped – ready to restart",
            "say_timer_stopped": "Timer stopped",
            "say_timer_restarted": "Timer restarted",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal for all vendors
            # ═══════════════════════════════════════════════════════════

            # ─── NAS vendor ───
            "vendor_label": "NAS vendor:",
            "vendor_tooltip": (
                "Choose your NAS vendor. Determines the shutdown commands "
                "and default paths. 'Auto-detect' checks the NAS via SSH."
            ),
            "vendor_auto_detect": "🔄 Auto-detect",
            "vendor_auto_detect_tooltip": (
                "Auto-detect the vendor via SSH. "
                "Requires: SSH key and IP are configured correctly."
            ),
            "vendor_detect_in_progress": "🔄 Detecting...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Generic Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Custom",
            "vendor_custom_hint": (
                "Custom: Adjust the shutdown commands manually. "
                "Default: 'sudo shutdown -h now' (works on "
                "80% of all Linux NAS)."
            ),

            # ─── Vendor detection (status messages) ───
            "vendor_detect_success": "Vendor detected: {}",
            "vendor_detect_success_question": (
                "Vendor detected: {}\n\n"
                "Should this vendor be applied?\n"
                "(Current value: {})"
            ),
            "vendor_detect_failed": (
                "Vendor could not be detected automatically.\n\n"
                "Please select manually. Most Linux NAS systems work "
                "with 'Generic Linux'."
            ),
            "vendor_detect_no_ssh": (
                "Auto-detection requires SSH access.\n\n"
                "Please check:\n"
                "• SSH key path is correct\n"
                "• IP address is correct\n"
                "• SSH is enabled on the NAS\n"
                "• SSH key is installed on the NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Please enter SSH key and IP address first."
            ),
            "vendor_detect_nas_offline": (
                "The NAS server is not responding.\n\n"
                "Please check:\n"
                "• Is the NAS powered on?\n"
                "• Is the IP address correct?\n"
                "• Is the NAS on the same network?\n\n"
                "Start the NAS and try again."
            ),
            "vendor_detect_error": "Error during auto-detection:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH key not found:\n\n{}\n\n"
                "Please check the path in the settings."
            ),

            # ─── Custom shutdown command ───
            "custom_cmd_label": "Shutdown command:",
            "custom_cmd_tooltip": (
                "The command sent to the NAS via SSH. "
                "Separate multiple commands with a semicolon."
            ),
            "custom_cmd_hint": (
                "💡 Separate multiple commands with a semicolon — "
                "the first successful one is used. "
                "Example: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Show help about shutdown commands",
            "custom_cmd_help_title": "Typical shutdown commands",
            "custom_cmd_help_text": (
                "<h3>Typical shutdown commands by vendor</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (generic):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Multiple commands (fallback chain)</h4>"
                "<p>If the first command fails, the next is tried. "
                "Separate with a semicolon:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Tip:</b> Choose the most likely command first, "
                "then alternatives as fallback.</p>"
            ),

            # ─── Volume detection ───
            "volumes_detection_in_progress": "🔄 Detecting volumes via SSH...",
            "volumes_detection_via_paths": (
                "🔍 Searching in vendor-specific paths..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Fallback: Searching via smbclient..."
            ),

            # ─── Volume detection panel ───
            "volumes_detect_panel_running": (
                "🔍 Searching for volumes via SSH... "
                "This may take a few seconds."
            ),
            "volumes_detect_panel_success": (
                "{} volumes found — {} new, {} already in list"
            ),
            "volumes_detect_panel_partial": (
                "{} volumes found — all already in list"
            ),
            "volumes_detect_panel_failed": (
                "No volumes found. Please add volumes manually."
            ),

            # ─── MAC address detection ───
            "mac_detect_in_progress": "🔄 Detecting MAC address...",
            "mac_detect_success": "✅ MAC address detected: {}",
            "mac_detect_success_dialog": (
                "MAC address successfully detected.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "The value has been entered in the MAC field."
            ),
            "mac_detect_failed": (
                "⚠ MAC address could not be detected automatically. "
                "Help will be shown."
            ),
            "config_mac_find": "🔍 Find MAC",
            "config_mac_find_tooltip": (
                "Auto-detect MAC address. "
                "If that fails, a guide will be shown."
            ),
        },
        # "🇪🇸 Español"
        "es": {
            "window_title": "Gestión NAS",
            "status_checking": "Comprobando conexión al servidor...",
            "status_online": "Servidor NAS en línea ✓",
            "status_offline": "Servidor NAS fuera de línea",
            "status_settings": "Configuración abierta - Temporizador detenido",
            "status_settings_saved": "Configuración guardada",
            "status_settings_cancelled": "Configuración cancelada",
            "status_shutdown": "Apagando NAS y Mac...",
            "status_shutdown_nas": "Apagando NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Apagado NAS enviado, Mac se apagará ahora...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Fallo al apagar NAS, apagando Mac de todos modos...",
            "status_starting": "Iniciando NAS vía Wake-on-LAN...",
            "status_waiting": "Esperando inicio del servidor...",
            "status_wol_sent": "Magic Packet enviado",
            "status_wol_failed": "WOL falló",
            "status_mounting": "Montando volúmenes seleccionados...",
            "status_mounting_volume": "Montando {}...",
            "status_mounted": "{} montado ✓",
            "status_unmounting": "Expulsando {}...",
            "status_unmounted": "{} expulsado ✓",
            "status_error": "Error: {} no se pudo montar",
            "status_error_unmount": "Error: {} no se pudo expulsar",
            "status_all_mounted": "Todos los volúmenes montados ✓",
            "status_all_unmounted": "Todos los volúmenes expulsados ✓",
            "status_mount_all": "Montando todos los volúmenes...",
            "status_unmount_all": "Expulsando todos los volúmenes...",
            "status_shutdown_cmd": "Comando de apagado NAS enviado ✓",
            "status_timeout": "Tiempo de espera agotado - El servidor no pudo iniciarse",
            "status_no_volumes": "Ningún volumen montado",
            "status_mount_failed": "Montaje fallido",
            "status_cancelled": "Cancelado - La aplicación se cerrará",
            "status_esc": "Tecla ESC presionada - La aplicación se cerrará",
            "status_server_online": "Servidor en línea - esperando servicio SMB...",
            "status_profile_changed": "Perfil cambiado a: {}",
            "status_switching": "Cambiando a perfil: {}...",
            "btn_shutdown_both": "Mac y NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Cancelar",
            "btn_start_nas": "Iniciar NAS",
            "btn_settings": "Configuración (Cmd+E)",
            "btn_select_all": "Todo",
            "btn_save": "Guardar",
            "btn_reset": "Restablecer",
            "btn_info": "ℹ",
            "btn_profile": "Perfiles",
            "tooltip_shutdown_both": "Apaga Mac y NAS en 2 min",
            "tooltip_shutdown_nas": "Apaga solo el NAS",
            "tooltip_cancel": "Cierra la aplicación",
            "tooltip_start_nas": "Inicia NAS vía Wake-on-LAN",
            "tooltip_settings": "Configuración (Cmd+E)",
            "timer_shutdown": "Apagado automático en {} segundos - ENTER solo NAS",
            "timer_start": "Inicio automático en {} segundos - ENTER para inicio inmediato",
            "volumes_title": "Volúmenes disponibles",
            "volumes_title_offline": "Volúmenes a montar al inicio",
            "volumes_hint": "Aviso: El primer volumen de la lista se trata automáticamente como volumen principal y no se puede desactivar.",
            "volumes_mount_tooltip": "Se montará automáticamente al iniciar el servidor",
            "config_title": "AnyNasPy - Configuración",
            "config_tab_profiles": "Perfiles del servidor",
            "config_tab_general": "General",
            "config_tab_volumes": "Volúmenes",
            "config_tab_timing": "Tiempos",
            "config_language": "Idioma:",
            "config_nas_group": "Configuración del servidor NAS",
            "config_nas_user": "Nombre de usuario:",
            "config_nas_dns": "Nombre DNS:",
            "config_nas_ip": "Dirección IP:",
            "config_nas_mac": "Dirección MAC:",
            "config_ssh_key": "Ruta de la clave SSH:",
            "config_volumes_group": "Volúmenes",
            "config_volumes_label": "Volúmenes (un nombre por línea):",
            "config_time_group": "Ajustes de tiempo (segundos)",
            "config_auto_shutdown": "Retardo de apagado automático:",
            "config_auto_start": "Retardo de inicio automático:",
            "config_wol_wait": "Tiempo de espera WOL (máx):",
            "config_smb_wait": "Tiempo de espera SMB:",
            "config_mount_retries": "Intentos de montaje:",
            "config_status_file": "Archivo de estado",
            "config_json_path": "Archivo de configuración JSON:",
            "config_profile_name": "Nombre del perfil:",
            "config_profile_active": "Perfil activo",
            "config_profile_set_active": "Establecer como perfil activo",
            "config_profile_list": "Perfiles existentes:",
            "config_profile_new": "Nuevo perfil",
            "config_profile_delete": "Eliminar perfil",
            "config_profile_duplicate": "Duplicar perfil",
            "config_profile_rename": "Renombrar",
            "config_profile_required": "El nombre del perfil es obligatorio.",
            "config_profile_exists": "Ya existe un perfil con este nombre.",
            "config_profile_deleted": "El perfil '{}' ha sido eliminado.",
            "config_profile_duplicated": "El perfil '{}' ha sido duplicado como '{}'.",
            "config_profile_renamed": "El perfil ha sido renombrado a '{}'.",
            "config_profile_activated": "El perfil '{}' está ahora activo.",
            "config_find_ip": "🔍 Encontrar IP",
            "config_find_ip_tooltip": "Buscar automáticamente la IP del servidor en la red",
            "config_ssh_help": "? Ayuda",
            "config_mac_help": "? Ayuda",
            "config_mac_help_tooltip": "Instrucciones para encontrar la dirección MAC",
            "msg_ip_found": "La IP del servidor se encontró exitosamente:\n\n{}\n\nLa IP se ha ingresado en el campo.",
            "msg_ip_not_found": "No se pudo encontrar automáticamente la IP del servidor.\n\nPor favor, introduzca la dirección IP manualmente.\n\nConsejos:\n• Verifique el nombre DNS en la configuración\n• Asegúrese de que el NAS esté encendido\n• Encuentre la IP en la interfaz DSM en 'Sistema > Red'",
            "msg_reset_confirm": "¿Restablecer todos los ajustes a los valores predeterminados?",
            "msg_reset_title": "Restablecer",
            "msg_reset_done": "Todos los ajustes se han restablecido a los valores predeterminados.",
            "msg_delete_confirm": "¿Realmente desea eliminar el perfil '{}'?",
            "msg_delete_title": "Eliminar perfil",
            "msg_no_active_profile": "No hay ningún perfil activo seleccionado.",
            "info_title": "Acerca de AnyNasPy",
            "info_version": "Versión",
            "info_copyright": "Copyright",
            "info_license": "Licencia",
            "info_impressum": "Aviso legal",
            "info_developer": "Desarrollador",
            "info_contact": "Contacto",
            "info_license_text": "Licencia MIT",
            "say_timer_shutdown": "Apagado automático de Mac y NAS en {} segundos - Enter solo NAS - Escape para cancelar",
            "say_timer_start": "El servidor NAS se iniciará en {} segundos - Enter para inicio inmediato",
            "say_server_online": "El servidor NAS es accesible",
            "say_server_offline": "El servidor NAS está fuera de línea",
            "say_shutdown_started": "Apagado iniciado",
            "say_nas_shutdown": "El NAS se está apagando",
            "say_starting_nas": "Iniciando NAS",
            "say_cancelled": "Cancelado",
            "say_waiting_server": "Esperando inicio del servidor",
            "say_wol_failed": "Error al enviar",
            "say_server_reachable": "Servidor accesible",
            "say_mount_volume": "{} listo",
            "say_unmount_volume": "Expulsando {}",
            "say_mount_all": "Montando todos los volúmenes",
            "say_unmount_all": "Expulsando todos los volúmenes",
            "say_mount_error": "Error al montar",
            "say_unmount_error": "Error al expulsar",
            "say_mount_failed": "No hay volúmenes montados",
            "say_settings_opened": "Configuración abierta",
            "say_settings_saved": "Configuración guardada",
            "say_settings_cancelled": "Configuración cancelada",
            "say_workaround_deleted": "Archivo de solución eliminado",
            "say_server_timeout": "Tiempo de espera de inicio del servidor agotado",
            "say_profile_changed": "Perfil cambiado a {}",
            "ssh_key_create_title": "Crear SSH Key",
            "ssh_key_create_question": "¿Quieres crear un nuevo par de claves SSH?",
            "ssh_key_create_existing": "La clave SSH '{}' ya existe.\n¿Quieres sobrescribirla?",
            "ssh_key_create_comment": "Comentario para la clave SSH (opcional):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "Clave SSH creada: {}",
            "ssh_key_create_error": "Error al crear la clave SSH",
            "ssh_key_create_timeout": "Tiempo de creación de clave SSH agotado",
            "ssh_key_create_failed": "ssh-keygen devolvió un error:\n{}",
            "ssh_key_create_passphrase": "Frase de contraseña para la clave SSH (dejar vacío para ninguna):",
            "ssh_key_create_passphrase_confirm": "Confirmar frase de contraseña:",
            "ssh_key_create_passphrase_mismatch": "Las frases de contraseña no coinciden.",
            "ssh_key_create_info": "✅ Par de claves SSH creado exitosamente:\n\n"
            "📁 Clave Privada: {}\n"
            "📁 Clave Pública: {}\n\n"
            "📋 Clave Pública para copiar:\n"
            "{}\n\n"
            "🔑 Cómo instalar la clave en tu NAS:\n"
            "1. Copia la clave pública (arriba)\n"
            "2. Agrégala al archivo:\n"
            "   ~/.ssh/authorized_keys en el NAS\n"
            "3. O usa:\n"
            "   ssh-copy-id {}@{}",   # ← Dieses Komma fehlt!
            "ssh_key_enter_name": "Por favor, introduzca un nombre de archivo diferente:",
            "ssh_key_exists_also": "La clave '{}' también existe.\nPor favor, bórrela primero o elija otro nombre.",
            "ssh_key_passphrase_title": "Frase de contraseña",
            "ssh_key_passphrase_question": "¿Quieres usar una frase de contraseña para la clave SSH?\n\nSin frase de contraseña: Conexión automática posible, menos segura.\nCon frase de contraseña: Más segura, pero pide en cada conexión.",
            "ssh_key_passphrase_enter": "Introducir frase de contraseña",
            "ssh_key_passphrase_label": "Frase de contraseña para la clave SSH (mínimo 4 caracteres):",
            "ssh_key_passphrase_none": "Sin frase de contraseña",
            "ssh_key_passphrase_none_question": "No ha introducido una frase de contraseña.\n¿Desea crear la clave sin frase de contraseña?",
            "ssh_key_passphrase_short": "Frase de contraseña demasiado corta",
            "ssh_key_passphrase_short_message": "La frase de contraseña debe tener al menos 4 caracteres.",
            "ssh_key_passphrase_confirm": "Confirmar frase de contraseña",
            "ssh_key_passphrase_confirm_label": "Introduzca la frase de contraseña nuevamente:",
            "ssh_key_passphrase_mismatch_title": "Error de frase de contraseña",
            "ssh_key_passphrase_mismatch_message": "Las frases de contraseña no coinciden.",
            "config_ssh_open": "Abrir",
            "config_ssh_open_tooltip": "Seleccionar clave SSH o abrir carpeta",
            "config_ssh_create": "Crear",
            "config_ssh_create_tooltip": "Crear nuevo par de claves SSH",
            "config_ssh_help_tooltip": "Mostrar ayuda de clave SSH",
            "config_ssh_select": "Seleccionar clave SSH",
            "config_json_open": "Abrir",
            "config_json_open_tooltip": "Abrir carpeta de configuración JSON",
            "config_error": "Error",
            "config_shutdown_mac_delay": "Tiempo de espera entre apagado NAS y Mac:",
            "info_third_party": "Bibliotecas de terceros",
            "info_pyqt5_license": "Esta aplicación utiliza PyQt5, que está licenciado bajo la GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nEl texto completo de la licencia se puede ver en https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Detectar volúmenes",
            "volumes_add": "Añadir",
            "volumes_delete": "Eliminar",
            "volumes_move_up": "Subir",
            "volumes_move_down": "Bajar",
            "volumes_available": "Volúmenes disponibles:",
            "volumes_no_volumes": "No se encontraron volúmenes.",
            "volumes_detection_failed": "Error en la detección de volúmenes.",
            "volumes_detection_success": "Volúmenes detectados con éxito.",
            "volumes_confirm_delete": "¿Eliminar realmente el volumen '{}'?",
            "volumes_enter_name": "Por favor, introduzca el nombre del nuevo volumen:",
            "volumes_name_exists": "Ya existe un volumen con este nombre.",
            "msg_invalid_ip": "La dirección IP introducida no es válida.\nPor favor, introduzca una dirección IPv4 válida (p.ej. 192.168.1.100).",
            "msg_select_volume": "Por favor, seleccione un volumen.",
            "msg_cannot_delete_main_volume": "No se puede eliminar el primer volumen (volumen principal).",
            "profile_cannot_delete_last": "No se puede eliminar el último perfil.",
            "status_wol_sending": "Enviando paquete mágico...",
            "status_wol_method_failed": "Falló el método Python, intentando el siguiente...",
            "status_trying_wakeonlan": "Intentando wakeonlan...",
            "status_trying_etherwake": "Intentando etherwake...",
            "ssh_key_system_key_warning": "Advertencia de seguridad",
            "ssh_key_system_key_message": "El nombre '{}' es una clave del sistema y no se sobrescribirá.\nPor favor, elija otro nombre (p.ej. synaspy_rsa).",
            "profile_name_exists": "Ya existe un perfil con el nombre '{}'.",
            "config_profile_created": "Se ha creado el perfil '{}'.",
            "config_profile_create_failed": "No se pudo crear el perfil.",
            "config_profile_rename_failed": "Fallo en el cambio de nombre.",
            "config_profile_duplicate_name": "Nombre para el perfil duplicado:",
            "config_profile_duplicate_failed": "Fallo al duplicar.",
            "config_profile_delete_failed": "Fallo al eliminar.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Apaga solo el Mac (el NAS permanece encendido, sin WOL)",
            "status_shutdown_mac_only": "Apagando solo el Mac...",
            "say_shutdown_mac_only": "El Mac se está apagando, el NAS permanece encendido",

            "btn_scheduled_shutdown": "🕐 Apagado programado",
            "tooltip_scheduled_shutdown": "Se apaga tras un tiempo elegido por el usuario",
            "btn_scheduled_shutdown_offline": "🕐 Apagar el Mac de forma programada",
            "tooltip_scheduled_shutdown_offline": "Apaga solo el Mac tras un tiempo seleccionado (el NAS está desconectado)",
            "btn_cancel_scheduled": "⏹ Cancelar cuenta atrás",
            "tooltip_cancel_scheduled": "Cancela la cuenta atrás activa",

            "sched_dialog_title": "Apagado programado",
            "sched_target_label": "Objetivo:",
            "sched_target_both": "🖥️ Mac + NAS  (apagado completo)",
            "sched_target_nas": "🗄️ Solo NAS  (el Mac permanece encendido)",
            "sched_target_mac": "💻 Solo Mac  (el NAS permanece encendido)",

            "sched_wait_label": "Tiempo de espera hasta el apagado:",
            "sched_hours": "Horas",
            "sched_minutes": "Minutos",

            "sched_caffeinate_label": "Opción caffeinate (mantiene el Mac despierto):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Recomendado: Sistema despierto, la pantalla puede oscurecerse  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Evitar solo inactividad y disco (la pantalla permanece encendida)  (-i -m)",
            "sched_caffeinate_d": "La pantalla también permanece encendida  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simular actividad del usuario (pantalla brillante, sistema despierto)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Máximo: Pantalla + sistema + disco permanentemente despiertos  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Desactivado (ahorro de energía normal – el sistema puede dormir)",

            "sched_caffeinate_hint": (
                "💡 Dato didáctico: Usa las banderas de caffeinate directamente en la terminal:\n"
                "   -i  evita el sueño por inactividad del sistema\n"
                "   -m  evita el sueño del disco (el disco duro no se duerme)\n"
                "   -s  evita el sueño del sistema (solo con adaptador de corriente)\n"
                "   -d  evita el sueño de la pantalla (la pantalla permanece encendida)\n"
                "   -u  simula actividad del usuario (la pantalla permanece brillante)\n"
                "   -w PID  finaliza caffeinate cuando termina el proceso PID\n"
                "Ejemplo:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Apagado programado para: {}",
            "sched_countdown_label": "Cuenta atrás: {} hasta el apagado ({})",
            "sched_started": "Temporizador iniciado.\n\nObjetivo: {}\nDuración: {}\nFin: {}",
            "sched_cancelled": "Temporizador cancelado",
            "sched_already_active": "Ya hay un temporizador en ejecución. ¿Cancelarlo primero?",
            "sched_invalid_time": "Introduce un tiempo válido (mínimo 1 minuto).",
            "sched_max_time": "Máximo permitido: 720 horas (30 días).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Temporizador iniciado. El Mac y el NAS se apagarán en {}."
            ),
            "sched_voice_started_nas": (
                "Temporizador iniciado. Solo el NAS se apagará en {}. "
                "El Mac permanece encendido."
            ),
            "sched_voice_started_mac": (
                "Temporizador iniciado. Solo el Mac se apagará en {}. "
                "El NAS permanece encendido."
            ),
            "sched_voice_started_nothing": (
                "Temporizador iniciado. No se ejecutará nada al expirar. "
                "caffeinate permanece activo hasta entonces."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "El Mac permanece despierto durante {}. "
                "La pantalla puede oscurecerse. "
                "No se ejecutará nada al expirar."
            ),
            "sched_voice_nothing_im": (
                "El Mac permanece despierto durante {}. "
                "La pantalla permanece encendida. "
                "No se ejecutará nada al expirar."
            ),
            "sched_voice_nothing_d": (
                "El Mac y la pantalla permanecen encendidos durante {}. "
                "No se ejecutará nada al expirar."
            ),
            "sched_voice_nothing_u": (
                "El Mac permanece activo durante {}. "
                "La pantalla permanece brillante. "
                "No se ejecutará nada al expirar."
            ),
            "sched_voice_nothing_full": (
                "El Mac permanece totalmente activo durante {} – pantalla y sistema despiertos continuamente. "
                "No se ejecutará nada al expirar."
            ),
            "sched_voice_nothing_off": (
                "El temporizador se ejecuta durante {}. "
                "No se ejecutará nada al expirar. "
                "Atención: El Mac puede entrar en modo de suspensión."
            ),
            "sched_voice_cancelled": "Temporizador cancelado",
            "sched_caffeinate_failed": "No se pudo iniciar caffeinate:\n{}",
            "sched_target_required": "Selecciona un objetivo.",
            "sched_tooltip_active": "Temporizador en ejecución – haz clic para cancelar",

            "status_scheduled_active": "Temporizador activo - {} restante",
            "status_scheduled_triggered": "Temporizador expirado - iniciando {}",
            "status_scheduled_cancelled": "Temporizador cancelado",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Temporizador activo",
            "close_blocked_text": (
                "<b>¡Todavía hay un temporizador en ejecución!</b><br><br>"
                "Programado: {}<br>"
                "Restante: <b>{}</b><br>"
                "A las: {}<br><br>"
                "Si cierras ahora, el apagado programado "
                "<b>ya no se ejecutará</b>."
            ),
            "close_blocked_yes": "Cerrar de todos modos",
            "close_blocked_no": "Mantener la app en ejecución",
            "close_blocked_cancel_text": (
                "Todavía hay un temporizador en ejecución.\n\n"
                "¿Realmente quieres cerrar la app?\n"
                "(El apagado programado se descartará.)"
            ),
            "close_blocked_log_aborted": "Cierre cancelado (temporizador activo)",
            "close_blocked_log_discarded": (
                "La app se cierra a pesar del temporizador activo – temporizador descartado"
            ),
            "close_blocked_log_cancel_aborted": (
                "Cierre de la app cancelado mediante el botón Cancelar"
            ),
            # "duration_day": "día",
            # "duration_days": "días",
            # "duration_hour": "hora",
            # "duration_hours": "horas",
            # "duration_minute": "minuto",
            # "duration_minutes": "minutos",
            "duration_connector_and": "y",
            "tooltip_pause_timer": "Pausar / reanudar temporizador",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Temporizador en pausa – quedan {} segundos",
            "timer_resumed": "Temporizador reanudado",
            "say_timer_paused": "Temporizador en pausa",
            "say_timer_resumed": "Temporizador reanudado",
            "tooltip_pause_timer": "Pausar/reanudar temporizador",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Salida de voz activada",
            "speech_enabled_hint": (
                "Pronuncia mensajes de estado, confirmaciones de volumen e "
                "información del temporizador a través de la salida de voz de "
                "macOS. Si se desactiva, la aplicación funciona en silencio."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Para el apagado programado del Mac se requiere la "
                "contraseña de administrador.\n\n"
                "Se guarda de forma segura en el llavero de macOS y solo se "
                "utiliza durante el apagado.\n\n"
                "¿Configurar ahora?"
            ),
            "mac_pw_dialog_title": "Contraseña de administrador",
            "mac_pw_dialog_message": (
                "Para el apagado del Mac se requiere la contraseña de "
                "administrador.\n\n"
                "Se guarda de forma segura en el llavero de macOS y solo se "
                "utiliza durante el apagado."
            ),
            "mac_pw_wrong_password": (
                "La contraseña es incorrecta.\n\n"
                "Por favor, inténtalo de nuevo."
            ),
            "mac_pw_test_failed": (
                "Error al verificar la contraseña:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "El temporizador no se inició porque se canceló la "
                "introducción de la contraseña.\n\n"
                "Sin contraseña, el Mac no se puede apagar."
            ),
            "clear_password_title": "Eliminar contraseña guardada",
            "clear_password_message": (
                "¿Eliminar la contraseña de administrador guardada en el llavero?\n\n"
                "En el próximo apagado programado, se solicitará la "
                "contraseña de nuevo."
            ),
            "clear_password_success": "La contraseña se ha eliminado del llavero.",
            "clear_password_failed": "No se pudo eliminar la contraseña.",
            "clear_password_description": (
                "Elimina la contraseña de administrador guardada en el llavero "
                "de macOS. En el próximo apagado programado, "
                "se solicitará de nuevo."
            ),
            "clear_password_button": "Eliminar contraseña guardada",
            "shutdown_no_password_message": (
                "No se pudo apagar el Mac.\n\n"
                "No hay disponible ni una regla NOPASSWD en sudoers ni una "
                "contraseña guardada en el llavero.\n\n"
                "Por favor, configura de nuevo el apagado programado."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Advertencia",
            "warning_eject_failed_continue": (
                "No se pudieron expulsar correctamente las unidades de red.\n\n"
                "Si todavía se están copiando datos o hay archivos abiertos, "
                "puede producirse pérdida de datos.\n\n"
                "¿Continuar con el apagado de todos modos?"
            ),
            "auto_timer_disabled_no_pw": (
                "Apagado automático desactivado – no hay contraseña de "
                "administrador disponible. Introdúcela una vez en el próximo aviso."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Sí",
            "btn_no": "No",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ No apagar nada  (El Mac permanece despierto – p. ej. para scripts de copia de seguridad)",
            "sched_countdown_coffee_label": "⏳ caffeinate activo: quedan {} ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Temporizador de café aún activo",
            "coffee_conflict_message": (
                "Aún hay un temporizador de café en marcha:\n\n"
                "Restante: {}\n\n"
                "Si apagas ahora, el temporizador de café se cancelará "
                "y caffeinate se detendrá.\n\n"
                "¿Apagar de todos modos?"
            ),
            "shutdown_timer_conflict_title": "Temporizador de apagado aún activo",
            "shutdown_timer_conflict_message": (
                "Aún hay un temporizador de apagado en marcha:\n\n"
                "Programado: {}\n"
                "Restante: {}\n\n"
                "Si apagas manualmente ahora, el temporizador se cancelará "
                "y habrá que programarlo de nuevo.\n\n"
                "¿Apagar de todos modos?"
            ),
            "tooltip_stop_timer": "Detener el temporizador por completo",
            "tooltip_stop_timer_inactive": "Ningún temporizador activo",
            "timer_stopped_notice": "⏹ Temporizador detenido – listo para reiniciar",
            "say_timer_stopped": "Temporizador detenido",
            "say_timer_restarted": "Temporizador reiniciado",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "Fabricante del NAS:",
            "vendor_tooltip": (
                "Selecciona el fabricante de tu NAS. Determina los comandos "
                "de apagado y las rutas predeterminadas. 'Detección automática' "
                "comprueba el NAS por SSH."
            ),
            "vendor_auto_detect": "🔄 Detección automática",
            "vendor_auto_detect_tooltip": (
                "Detectar el fabricante automáticamente por SSH. "
                "Requisito: la clave SSH y la IP están configuradas correctamente."
            ),
            "vendor_detect_in_progress": "🔄 Detectando...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Linux genérico",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Personalizado",
            "vendor_custom_hint": (
                "Personalizado: Ajusta los comandos de apagado manualmente. "
                "Predeterminado: 'sudo shutdown -h now' (funciona en el "
                "80 % de todos los NAS Linux)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Fabricante detectado: {}",
            "vendor_detect_success_question": (
                "Fabricante detectado: {}\n\n"
                "¿Quieres usar este fabricante?\n"
                "(Valor actual: {})"
            ),
            "vendor_detect_failed": (
                "No se pudo detectar el fabricante automáticamente.\n\n"
                "Selecciónalo manualmente. La mayoría de los NAS Linux "
                "funcionan con 'Linux genérico'."
            ),
            "vendor_detect_no_ssh": (
                "La detección automática requiere acceso SSH.\n\n"
                "Comprueba lo siguiente:\n"
                "• La ruta de la clave SSH es correcta\n"
                "• La dirección IP es correcta\n"
                "• SSH está activado en el NAS\n"
                "• La clave SSH está instalada en el NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Introduce primero la clave SSH y la dirección IP."
            ),
            "vendor_detect_nas_offline": (
                "El servidor NAS no responde.\n\n"
                "Comprueba lo siguiente:\n"
                "• ¿Está encendido el NAS?\n"
                "• ¿Es correcta la dirección IP?\n"
                "• ¿Está el NAS en la misma red?\n\n"
                "Enciende el NAS e inténtalo de nuevo."
            ),
            "vendor_detect_error": "Error en la detección automática:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "Clave SSH no encontrada:\n\n{}\n\n"
                "Comprueba la ruta en la configuración."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Comando de apagado:",
            "custom_cmd_tooltip": (
                "El comando que se envía al NAS por SSH. "
                "Separa varios comandos con punto y coma."
            ),
            "custom_cmd_hint": (
                "💡 Separa varios comandos con punto y coma — "
                "se usará el primero que tenga éxito. "
                "Ejemplo: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Mostrar ayuda sobre los comandos de apagado",
            "custom_cmd_help_title": "Comandos de apagado típicos",
            "custom_cmd_help_text": (
                "<h3>Comandos de apagado típicos por fabricante</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (genérico):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Varios comandos (cadena de respaldo)</h4>"
                "<p>Si el primer comando falla, se prueba el siguiente. "
                "Separación con punto y coma:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Consejo:</b> Elige primero el comando más probable, "
                "y luego alternativas como respaldo.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Detectando volúmenes por SSH...",
            "volumes_detection_via_paths": (
                "🔍 Buscando en rutas específicas del fabricante..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Respaldo: Buscando mediante smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Buscando volúmenes por SSH... La búsqueda puede "
                "tardar unos segundos."
            ),
            "volumes_detect_panel_success": (
                "{} volúmenes encontrados — {} añadidos nuevos, "
                "{} ya existentes"
            ),
            "volumes_detect_panel_partial": (
                "{} volúmenes encontrados — todos ya en la lista"
            ),
            "volumes_detect_panel_failed": (
                "No se encontraron volúmenes. "
                "Introduce los volúmenes manualmente."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Detectando dirección MAC...",
            "mac_detect_success": "✅ Dirección MAC detectada: {}",
            "mac_detect_success_dialog": (
                "Dirección MAC detectada correctamente.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "El valor se ha introducido en el campo MAC."
            ),
            "mac_detect_failed": (
                "⚠ No se pudo detectar la dirección MAC automáticamente. "
                "Se mostrará la ayuda."
            ),
            "config_mac_find": "🔍 Buscar MAC",
            "config_mac_find_tooltip": (
                "Detectar la dirección MAC automáticamente. "
                "Si falla, se mostrará una guía."
            ),
        },
        # "🇫🇷 Français"
        "fr": {
            "language": "Langue:",
            # Hauptfenster
            "window_title": "Gestion NAS",
            "status_checking": "Vérification de la connexion au serveur...",
            "status_online": "Serveur NAS en ligne ✓",
            "status_offline": "Serveur NAS hors ligne",
            "status_settings": "Paramètres ouverts - Minuteur arrêté",
            "status_settings_saved": "Paramètres enregistrés",
            "status_settings_cancelled": "Paramètres annulés",
            "status_shutdown": "Arrêt du NAS et du Mac...",
            "status_shutdown_nas": "Arrêt du NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Arrêt NAS envoyé, Mac va s'éteindre maintenant...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Échec de l'arrêt du NAS, arrêt du Mac quand même...",
            "status_starting": "Démarrage du NAS via Wake-on-LAN...",
            "status_waiting": "Attente du démarrage du serveur...",
            "status_wol_sent": "Magic Packet envoyé",
            "status_wol_failed": "WOL échoué",
            "status_mounting": "Montage des volumes sélectionnés...",
            "status_mounting_volume": "Montage de {}...",
            "status_mounted": "{} monté ✓",
            "status_unmounting": "Éjection de {}...",
            "status_unmounted": "{} éjecté ✓",
            "status_error": "Erreur : {} n'a pas pu être monté",
            "status_error_unmount": "Erreur : {} n'a pas pu être éjecté",
            "status_all_mounted": "Tous les volumes montés ✓",
            "status_all_unmounted": "Tous les volumes éjectés ✓",
            "status_mount_all": "Montage de tous les volumes...",
            "status_unmount_all": "Éjection de tous les volumes...",
            "status_shutdown_cmd": "Commande 'arrêt NAS envoyée ✓",
            "status_timeout": "Délai d'attente dépassé - Le serveur n'a pas pu démarrer",
            "status_no_volumes": "Aucun volume monté",
            "status_mount_failed": "Échec du montage",
            "status_cancelled": "Annulé - L'application va se fermer",
            "status_esc": "Touche ESC enfoncée - L'application va se fermer",
            "status_server_online": "Serveur en ligne - attente du service SMB...",
            "status_profile_changed": "Profil changé pour : {}",
            "status_switching": "Bascule vers le profil : {}...",
            # Buttons
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Annuler",
            "btn_start_nas": "Démarrer NAS",
            "btn_settings": "Paramètres (Cmd+E)",
            "btn_select_all": "Tout",
            "btn_save": "Enregistrer",
            "btn_reset": "Réinitialiser",
            "btn_info": "ℹ",
            "btn_profile": "Profils",
            # Tooltips
            "tooltip_shutdown_both": "Arrête le Mac et le NAS dans 2 min",
            "tooltip_shutdown_nas": "Arrête uniquement le NAS",
            "tooltip_cancel": "Ferme l'application",
            "tooltip_start_nas": "Démarre le NAS via Wake-on-LAN",
            "tooltip_settings": "Paramètres (Cmd+E)",
            # Timer
            "timer_shutdown": "Arrêt automatique dans {} secondes - ENTER pour NAS uniquement",
            "timer_start": "Démarrage automatique dans {} secondes - ENTER pour un démarrage immédiat",
            # Volumes
            "volumes_title": "Volumes disponibles",
            "volumes_title_offline": "Volumes à monter au démarrage",
            "volumes_hint": "Remarque : Le premier volume de la liste est automatiquement considéré comme le volume principal et ne peut pas être désactivé.",
            "volumes_mount_tooltip": "Sera monté automatiquement au démarrage du serveur",
            # Config Dialog
            "config_title": "AnyNasPy - Paramètres",
            "config_tab_profiles": "Profils serveur",
            "config_tab_general": "Général",
            "config_tab_volumes": "Volumes",
            "config_tab_timing": "Temporisation",
            "config_language": "Langue :",
            "config_nas_group": "Paramètres du serveur NAS",
            "config_nas_user": "Nom d'utilisateur :",
            "config_nas_dns": "Nom DNS :",
            "config_nas_ip": "Adresse IP :",
            "config_nas_mac": "Adresse MAC :",
            "config_ssh_key": "Chemin de la clé SSH :",
            "config_volumes_group": "Volumes",
            "config_volumes_label": "Volumes (un nom par ligne) :",
            "config_time_group": "Paramètres de temps (secondes)",
            "config_auto_shutdown": "Délai d'arrêt automatique :",
            "config_auto_start": "Délai de démarrage automatique :",
            "config_wol_wait": "Temps d'attente WOL (max) :",
            "config_smb_wait": "Temps d'attente SMB :",
            "config_mount_retries": "Tentatives de montage :",
            "config_status_file": "Fichier d'état",
            "config_json_path": "Fichier de configuration JSON :",
            "config_profile_name": "Nom du profil :",
            "config_profile_active": "Profil actif",
            "config_profile_set_active": "Définir comme profil actif",
            "config_profile_list": "Profils existants :",
            "config_profile_new": "Nouveau profil",
            "config_profile_delete": "Supprimer le profil",
            "config_profile_duplicate": "Dupliquer le profil",
            "config_profile_rename": "Renommer",
            "config_profile_required": "Le nom du profil est requis.",
            "config_profile_exists": "Un profil avec ce nom existe déjà.",
            "config_profile_deleted": "Le profil '{}' a été supprimé.",
            "config_profile_duplicated": "Le profil '{}' a été dupliqué sous le nom '{}'.",
            "config_profile_renamed": "Le profil a été renommé en '{}'.",
            "config_profile_activated": "Le profil '{}' est maintenant actif.",
            # Config Buttons
            "config_find_ip": "🔍 Trouver IP",
            "config_find_ip_tooltip": "Rechercher automatiquement l'IP du serveur sur le réseau",
            "config_ssh_help": "? Aide",
            "config_mac_help": "? Aide",
            "config_mac_help_tooltip": "Instructions pour trouver l'adresse MAC",
            # Messages
            "msg_ip_found": "L'IP du serveur a été trouvée :\n\n{}\n\nL'IP a été saisie dans le champ.",
            "msg_ip_not_found": "L'IP du serveur n'a pas pu être trouvée automatiquement.\n\nVeuillez entrer l'adresse IP manuellement.\n\nConseils :\n• Vérifiez le nom DNS dans les paramètres\n• Assurez-vous que le NAS est allumé\n• Trouvez l'IP dans l'interface DSM sous 'Système > Réseau'",
            "msg_reset_confirm": "Réinitialiser tous les paramètres aux valeurs par défaut ?",
            "msg_reset_title": "Réinitialiser",
            "msg_reset_done": "Tous les paramètres ont été réinitialisés aux valeurs par défaut.",
            "msg_delete_confirm": "Voulez-vous vraiment supprimer le profil '{}' ?",
            "msg_delete_title": "Supprimer le profil",
            "msg_no_active_profile": "Aucun profil actif sélectionné.",
            # Info Dialog
            "info_title": "À propos de AnyNasPy",
            "info_version": "Version",
            "info_copyright": "Copyright",
            "info_license": "Licence",
            "info_impressum": "Mentions légales",
            "info_developer": "Développeur",
            "info_contact": "Contact",
            "info_license_text": "Licence MIT",
            # Sonstiges
            "say_timer_shutdown": "Arrêt automatique du Mac et du NAS dans {} secondes - Entrée pour NAS uniquement - Échap pour annuler",
            "say_timer_start": "Le serveur NAS démarrera dans {} secondes - Entrée pour un démarrage immédiat",
            "say_server_online": "Le serveur NAS est accessible",
            "say_server_offline": "Le serveur NAS est hors ligne",
            "say_shutdown_started": "Arrêt lancé",
            "say_nas_shutdown": "Le NAS est en train de s'arrêter",
            "say_starting_nas": "Démarrage du NAS",
            "say_cancelled": "Annulé",
            "say_waiting_server": "Attente du démarrage du serveur",
            "say_wol_failed": "Erreur d'envoi",
            "say_server_reachable": "Serveur accessible",
            "say_mount_volume": "{} prêt",
            "say_unmount_volume": "Éjection de {}",
            "say_mount_all": "Montage de tous les volumes",
            "say_unmount_all": "Éjection de tous les volumes",
            "say_mount_error": "Erreur lors du montage",
            "say_unmount_error": "Erreur lors de l'éjection",
            "say_mount_failed": "Aucun volume monté",
            "say_settings_opened": "Paramètres ouverts",
            "say_settings_saved": "Paramètres enregistrés",
            "say_settings_cancelled": "Paramètres annulés",
            "say_workaround_deleted": "Fichier de contournement supprimé",
            "say_server_timeout": "Délai de démarrage du serveur dépassé",
            "say_profile_changed": "Profil changé pour {}",
            "ssh_key_create_title": "Créer une clé SSH",
            "ssh_key_create_question": "Voulez-vous créer une nouvelle paire de clés SSH ?",
            "ssh_key_create_existing": "La clé SSH '{}' existe déjà.\nVoulez-vous la remplacer ?",
            "ssh_key_create_comment": "Commentaire pour la clé SSH (optionnel) :",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "Clé SSH créée : {}",
            "ssh_key_create_error": "Erreur lors de la création de la clé SSH",
            "ssh_key_create_timeout": "Délai de création de la clé SSH dépassé",
            "ssh_key_create_failed": "ssh-keygen a retourné une erreur :\n{}",
            "ssh_key_create_passphrase": "Phrase de passe pour la clé SSH (laisser vide pour aucune) :",
            "ssh_key_create_passphrase_confirm": "Confirmer la phrase de passe :",
            "ssh_key_create_passphrase_mismatch": "Les phrases de passe ne correspondent pas.",
            "ssh_key_create_info": "✅ Paire de clés SSH créée avec succès :\n\n"
            "📁 Clé Privée : {}\n"
            "📁 Clé Publique : {}\n\n"
            "📋 Clé Publique à copier :\n"
            "{}\n\n"
            "🔑 Comment installer la clé sur votre NAS :\n"
            "1. Copiez la clé publique (ci-dessus)\n"
            "2. Ajoutez-la au fichier :\n"
            "   ~/.ssh/authorized_keys sur le NAS\n"
            "3. Ou utilisez :\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Veuillez saisir un nom de fichier différent :",
            "ssh_key_exists_also": "La clé '{}' existe également.\nVeuillez la supprimer d'abord ou choisir un autre nom.",
            "ssh_key_passphrase_title": "Phrase de passe",
            "ssh_key_passphrase_question": "Voulez-vous utiliser une phrase de passe pour la clé SSH ?\n\nSans phrase de passe : Connexion automatique possible, moins sécurisée.\nAvec phrase de passe : Plus sécurisée, mais demande à chaque connexion.",
            "ssh_key_passphrase_enter": "Saisir la phrase de passe",
            "ssh_key_passphrase_label": "Phrase de passe pour la clé SSH (au moins 4 caractères) :",
            "ssh_key_passphrase_none": "Pas de phrase de passe",
            "ssh_key_passphrase_none_question": "Vous n'avez pas saisi de phrase de passe.\nSouhaitez-vous créer la clé sans phrase de passe ?",
            "ssh_key_passphrase_short": "Phrase de passe trop courte",
            "ssh_key_passphrase_short_message": "La phrase de passe doit comporter au moins 4 caractères.",
            "ssh_key_passphrase_confirm": "Confirmer la phrase de passe",
            "ssh_key_passphrase_confirm_label": "Saisir à nouveau la phrase de passe :",
            "ssh_key_passphrase_mismatch_title": "Erreur de phrase de passe",
            "ssh_key_passphrase_mismatch_message": "Les phrases de passe ne correspondent pas.",
            "config_ssh_open": "Ouvrir",
            "config_ssh_open_tooltip": "Sélectionner la clé SSH ou ouvrir le dossier",
            "config_ssh_create": "Créer",
            "config_ssh_create_tooltip": "Créer une nouvelle paire de clés SSH",
            "config_ssh_help_tooltip": "Afficher l'aide de la clé SSH",
            "config_ssh_select": "Sélectionner la clé SSH",
            "config_json_open": "Ouvrir",
            "config_json_open_tooltip": "Ouvrir le dossier de configuration JSON",
            "config_error": "Erreur",
            "config_shutdown_mac_delay": "Délai entre l'arrêt du NAS et du Mac :",
            "info_third_party": "Bibliothèques tierces",
            "info_pyqt5_license": "Cette application utilise PyQt5, qui est sous licence GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nLe texte complet de la licence est disponible à l'adresse https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Détecter les volumes",
            "volumes_add": "Ajouter",
            "volumes_delete": "Supprimer",
            "volumes_move_up": "Monter",
            "volumes_move_down": "Descendre",
            "volumes_available": "Volumes disponibles :",
            "volumes_no_volumes": "Aucun volume trouvé.",
            "volumes_detection_failed": "Échec de la détection des volumes.",
            "volumes_detection_success": "Volumes détectés avec succès.",
            "volumes_confirm_delete": "Supprimer vraiment le volume '{}' ?",
            "volumes_enter_name": "Veuillez entrer le nom du nouveau volume :",
            "volumes_name_exists": "Un volume avec ce nom existe déjà.",
            "msg_invalid_ip": "L'adresse IP saisie n'est pas valide.\nVeuillez saisir une adresse IPv4 valide (ex. 192.168.1.100).",
            "msg_select_volume": "Veuillez sélectionner un volume.",
            "msg_cannot_delete_main_volume": "Le premier volume (volume principal) ne peut pas être supprimé.",
            "profile_cannot_delete_last": "Le dernier profil ne peut pas être supprimé.",
            "status_wol_sending": "Envoi du paquet magique...",
            "status_wol_method_failed": "Méthode Python échouée, tentative de la suivante...",
            "status_trying_wakeonlan": "Tentative avec wakeonlan...",
            "status_trying_etherwake": "Tentative avec etherwake...",
            "ssh_key_system_key_warning": "Avertissement de sécurité",
            "ssh_key_system_key_message": "Le nom '{}' est une clé système et ne sera pas écrasé.\nVeuillez choisir un autre nom (ex. synaspy_rsa).",
            "profile_name_exists": "Un profil avec le nom '{}' existe déjà.",
            "config_profile_created": "Le profil '{}' a été créé.",
            "config_profile_create_failed": "Échec de la création du profil.",
            "config_profile_rename_failed": "Échec du renommage.",
            "config_profile_duplicate_name": "Nom pour le profil dupliqué :",
            "config_profile_duplicate_failed": "Échec du duplicata.",
            "config_profile_delete_failed": "Échec de la suppression.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Éteint uniquement le Mac (le NAS reste allumé, pas de WOL)",
            "status_shutdown_mac_only": "Extinction du Mac uniquement...",
            "say_shutdown_mac_only": "Le Mac s'éteint, le NAS reste allumé",

            "btn_scheduled_shutdown": "🕐 Extinction programmée",
            "tooltip_scheduled_shutdown": "S'éteint après une durée choisie par l'utilisateur",
            "btn_scheduled_shutdown_offline": "🕐 Éteindre le Mac de façon programmée",
            "tooltip_scheduled_shutdown_offline": "Éteint uniquement le Mac après une durée choisie (le NAS est hors ligne)",
            "btn_cancel_scheduled": "⏹ Annuler le compte à rebours",
            "tooltip_cancel_scheduled": "Annule le compte à rebours actif",

            "sched_dialog_title": "Extinction programmée",
            "sched_target_label": "Cible :",
            "sched_target_both": "🖥️ Mac + NAS  (extinction complète)",
            "sched_target_nas": "🗄️ NAS uniquement  (le Mac reste allumé)",
            "sched_target_mac": "💻 Mac uniquement  (le NAS reste allumé)",

            "sched_wait_label": "Temps d'attente avant l'extinction :",
            "sched_hours": "Heures",
            "sched_minutes": "Minutes",

            "sched_caffeinate_label": "Option caffeinate (maintient le Mac éveillé) :",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Recommandé : Système éveillé, l'écran peut s'assombrir  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Empêcher uniquement l'inactivité et le disque (l'écran reste allumé)  (-i -m)",
            "sched_caffeinate_d": "L'écran reste également allumé  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simuler l'activité de l'utilisateur (écran lumineux, système éveillé)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maximum : Écran + système + disque éveillés en permanence  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Désactivé (économie d'énergie normale – le système peut dormir)",

            "sched_caffeinate_hint": (
                "💡 Fait pédagogique : Utilise les options de caffeinate directement dans le terminal :\n"
                "   -i  empêche la veille d'inactivité du système\n"
                "   -m  empêche la veille du disque (le disque dur ne dort pas)\n"
                "   -s  empêche la veille du système (uniquement sur secteur)\n"
                "   -d  empêche la veille de l'écran (l'écran reste allumé)\n"
                "   -u  simule l'activité de l'utilisateur (l'écran reste lumineux)\n"
                "   -w PID  termine caffeinate lorsque le processus PID se termine\n"
                "Exemple :  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Extinction programmée pour : {}",
            "sched_countdown_label": "Compte à rebours : {} avant l'extinction ({})",
            "sched_started": "Minuteur démarré.\n\nCible : {}\nDurée : {}\nFin : {}",
            "sched_cancelled": "Minuteur annulé",
            "sched_already_active": "Un minuteur est déjà en cours. L'annuler d'abord ?",
            "sched_invalid_time": "Veuillez saisir une durée valide (au moins 1 minute).",
            "sched_max_time": "Maximum autorisé : 720 heures (30 jours).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Minuteur démarré. Le Mac et le NAS s'éteindront dans {}."
            ),
            "sched_voice_started_nas": (
                "Minuteur démarré. Seul le NAS s'éteindra dans {}. "
                "Le Mac reste allumé."
            ),
            "sched_voice_started_mac": (
                "Minuteur démarré. Seul le Mac s'éteindra dans {}. "
                "Le NAS reste allumé."
            ),
            "sched_voice_started_nothing": (
                "Minuteur démarré. Rien ne sera exécuté à l'expiration. "
                "caffeinate reste actif jusque-là."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Le Mac reste éveillé pendant {}. "
                "L'écran peut s'assombrir. "
                "Rien ne sera exécuté à l'expiration."
            ),
            "sched_voice_nothing_im": (
                "Le Mac reste éveillé pendant {}. "
                "L'écran reste allumé. "
                "Rien ne sera exécuté à l'expiration."
            ),
            "sched_voice_nothing_d": (
                "Le Mac et l'écran restent allumés pendant {}. "
                "Rien ne sera exécuté à l'expiration."
            ),
            "sched_voice_nothing_u": (
                "Le Mac reste actif pendant {}. "
                "L'écran reste lumineux. "
                "Rien ne sera exécuté à l'expiration."
            ),
            "sched_voice_nothing_full": (
                "Le Mac reste pleinement actif pendant {} – écran et système éveillés en continu. "
                "Rien ne sera exécuté à l'expiration."
            ),
            "sched_voice_nothing_off": (
                "Le minuteur fonctionne pendant {}. "
                "Rien ne sera exécuté à l'expiration. "
                "Attention : Le Mac peut passer en mode veille."
            ),
            "sched_voice_cancelled": "Minuteur annulé",
            "sched_caffeinate_failed": "Impossible de démarrer caffeinate :\n{}",
            "sched_target_required": "Veuillez sélectionner une cible.",
            "sched_tooltip_active": "Minuteur en cours – cliquer pour annuler",

            "status_scheduled_active": "Minuteur actif - {} restant",
            "status_scheduled_triggered": "Minuteur expiré - démarrage de {}",
            "status_scheduled_cancelled": "Minuteur annulé",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Minuteur actif",
            "close_blocked_text": (
                "<b>Un minuteur est encore en cours !</b><br><br>"
                "Programmé : {}<br>"
                "Restant : <b>{}</b><br>"
                "À : {}<br><br>"
                "Si tu fermes maintenant, l'extinction programmée "
                "<b>ne sera plus exécutée</b>."
            ),
            "close_blocked_yes": "Fermer quand même",
            "close_blocked_no": "Laisser l'app continuer",
            "close_blocked_cancel_text": (
                "Un minuteur est encore en cours.\n\n"
                "Veux-tu vraiment fermer l'application ?\n"
                "(L'extinction programmée sera alors abandonnée.)"
            ),
            "close_blocked_log_aborted": "Fermeture annulée (minuteur actif)",
            "close_blocked_log_discarded": (
                "L'app se ferme malgré un minuteur actif – minuteur abandonné"
            ),
            "close_blocked_log_cancel_aborted": (
                "Fermeture de l'app annulée via le bouton Annuler"
            ),
            "duration_day": "jour",
            "duration_days": "jours",
            "duration_hour": "heure",
            "duration_hours": "heures",
            "duration_minute": "minute",
            "duration_minutes": "minutes",
            "duration_connector_and": "et",
            "tooltip_pause_timer": "Mettre en pause / reprendre le minuteur",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Minuteur en pause – {} secondes restantes",
            "timer_resumed": "Minuteur repris",
            "say_timer_paused": "Minuteur en pause",
            "say_timer_resumed": "Minuteur repris",
            "tooltip_pause_timer": "Mettre en pause/reprendre le minuteur",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Sortie vocale activée",
            "speech_enabled_hint": (
                "Prononce les messages d'état, les confirmations de volume et "
                "les informations du minuteur via la sortie vocale de macOS. "
                "Lorsqu'elle est désactivée, l'application fonctionne en silence."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Le mot de passe administrateur est requis pour "
                "l'arrêt programmé du Mac.\n\n"
                "Il est stocké en toute sécurité dans le trousseau macOS et "
                "utilisé uniquement lors de l'arrêt.\n\n"
                "Configurer maintenant ?"
            ),
            "mac_pw_dialog_title": "Mot de passe administrateur",
            "mac_pw_dialog_message": (
                "Le mot de passe administrateur est requis pour "
                "l'arrêt du Mac.\n\n"
                "Il est stocké en toute sécurité dans le trousseau macOS et "
                "utilisé uniquement lors de l'arrêt."
            ),
            "mac_pw_wrong_password": (
                "Le mot de passe est incorrect.\n\n"
                "Veuillez réessayer."
            ),
            "mac_pw_test_failed": (
                "Erreur lors de la vérification du mot de passe :\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Le minuteur n'a pas été démarré car la saisie du "
                "mot de passe a été annulée.\n\n"
                "Sans mot de passe, le Mac ne peut pas être éteint."
            ),
            "clear_password_title": "Supprimer le mot de passe enregistré",
            "clear_password_message": (
                "Supprimer le mot de passe administrateur stocké dans le trousseau ?\n\n"
                "Lors du prochain arrêt programmé, le mot de passe sera "
                "à nouveau demandé."
            ),
            "clear_password_success": "Le mot de passe a été supprimé du trousseau.",
            "clear_password_failed": "Le mot de passe n'a pas pu être supprimé.",
            "clear_password_description": (
                "Supprime le mot de passe administrateur stocké dans le "
                "trousseau macOS. Lors du prochain arrêt programmé, "
                "il sera à nouveau demandé."
            ),
            "clear_password_button": "Supprimer le mot de passe enregistré",
            "shutdown_no_password_message": (
                "Le Mac n'a pas pu être éteint.\n\n"
                "Ni une règle NOPASSWD dans sudoers ni un mot de passe "
                "enregistré dans le trousseau ne sont disponibles.\n\n"
                "Veuillez reconfigurer l'arrêt programmé."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Avertissement",
            "warning_eject_failed_continue": (
                "Les lecteurs réseau n'ont pas pu être éjectés correctement.\n\n"
                "Si des données sont encore en cours de copie ou si des "
                "fichiers sont ouverts, une perte de données est possible.\n\n"
                "Continuer quand même l'arrêt ?"
            ),
            "auto_timer_disabled_no_pw": (
                "Arrêt automatique désactivé – aucun mot de passe "
                "administrateur disponible. Veuillez le saisir une fois "
                "lors de la prochaine invite."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Oui",
            "btn_no": "Non",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Ne rien éteindre  (Le Mac reste éveillé – p. ex. pour les scripts de sauvegarde)",
            "sched_countdown_coffee_label": "⏳ caffeinate actif : {} restantes ({})",


            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Minuteur café toujours actif",
            "coffee_conflict_message": (
                "Un minuteur café est encore actif :\n\n"
                "Restant : {}\n\n"
                "Si tu éteins maintenant, le minuteur café sera annulé "
                "et caffeinate sera arrêté.\n\n"
                "Éteindre quand même ?"
            ),
            "shutdown_timer_conflict_title": "Minuteur d'arrêt toujours actif",
            "shutdown_timer_conflict_message": (
                "Un minuteur d'arrêt est encore actif :\n\n"
                "Programmé : {}\n"
                "Restant : {}\n\n"
                "Si tu éteins manuellement maintenant, le minuteur sera annulé "
                "et devra être reprogrammé.\n\n"
                "Éteindre quand même ?"
            ),
            "tooltip_stop_timer": "Arrêter complètement le minuteur",
            "tooltip_stop_timer_inactive": "Aucun minuteur actif",
            "timer_stopped_notice": "⏹ Minuteur arrêté – prêt à redémarrer",
            "say_timer_stopped": "Minuteur arrêté",
            "say_timer_restarted": "Minuteur redémarré",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "Fabricant du NAS :",
            "vendor_tooltip": (
                "Choisis le fabricant de ton NAS. Détermine les commandes "
                "d'arrêt et les chemins par défaut. « Détection automatique » "
                "vérifie le NAS via SSH."
            ),
            "vendor_auto_detect": "🔄 Détection automatique",
            "vendor_auto_detect_tooltip": (
                "Détecter automatiquement le fabricant via SSH. "
                "Condition : la clé SSH et l'IP sont correctement configurées."
            ),
            "vendor_detect_in_progress": "🔄 Détection en cours...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Linux générique",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Personnalisé",
            "vendor_custom_hint": (
                "Personnalisé : Adapte manuellement les commandes d'arrêt. "
                "Par défaut : 'sudo shutdown -h now' (fonctionne sur "
                "80 % de tous les NAS Linux)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Fabricant détecté : {}",
            "vendor_detect_success_question": (
                "Fabricant détecté : {}\n\n"
                "Faut-il utiliser ce fabricant ?\n"
                "(Valeur actuelle : {})"
            ),
            "vendor_detect_failed": (
                "Le fabricant n'a pas pu être détecté automatiquement.\n\n"
                "Sélectionne-le manuellement. La plupart des NAS Linux "
                "fonctionnent avec « Linux générique »."
            ),
            "vendor_detect_no_ssh": (
                "La détection automatique nécessite un accès SSH.\n\n"
                "Vérifie les points suivants :\n"
                "• Le chemin de la clé SSH est correct\n"
                "• L'adresse IP est correcte\n"
                "• SSH est activé sur le NAS\n"
                "• La clé SSH est installée sur le NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Saisis d'abord la clé SSH et l'adresse IP."
            ),
            "vendor_detect_nas_offline": (
                "Le serveur NAS ne répond pas.\n\n"
                "Vérifie les points suivants :\n"
                "• Le NAS est-il allumé ?\n"
                "• L'adresse IP est-elle correcte ?\n"
                "• Le NAS est-il sur le même réseau ?\n\n"
                "Démarre le NAS et réessaie."
            ),
            "vendor_detect_error": "Erreur lors de la détection automatique :\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "Clé SSH introuvable :\n\n{}\n\n"
                "Vérifie le chemin dans les paramètres."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Commande d'arrêt :",
            "custom_cmd_tooltip": (
                "La commande envoyée au NAS via SSH. "
                "Sépare plusieurs commandes par un point-virgule."
            ),
            "custom_cmd_hint": (
                "💡 Sépare plusieurs commandes par un point-virgule — "
                "la première qui réussit est utilisée. "
                "Exemple : sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Afficher l'aide sur les commandes d'arrêt",
            "custom_cmd_help_title": "Commandes d'arrêt typiques",
            "custom_cmd_help_text": (
                "<h3>Commandes d'arrêt typiques par fabricant</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (générique) :</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology :</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP :</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid :</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS :</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server :</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Plusieurs commandes (chaîne de secours)</h4>"
                "<p>Si la première commande échoue, la suivante est essayée. "
                "Séparation par point-virgule :</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Astuce :</b> Choisis d'abord la commande la plus probable, "
                "puis des alternatives en secours.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Détection des volumes via SSH...",
            "volumes_detection_via_paths": (
                "🔍 Recherche dans les chemins spécifiques au fabricant..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Solution de secours : recherche via smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Recherche des volumes via SSH... La recherche peut "
                "prendre quelques secondes."
            ),
            "volumes_detect_panel_success": (
                "{} volumes trouvés — {} ajoutés, "
                "{} déjà présents"
            ),
            "volumes_detect_panel_partial": (
                "{} volumes trouvés — tous déjà dans la liste"
            ),
            "volumes_detect_panel_failed": (
                "Aucun volume trouvé. "
                "Saisis les volumes manuellement."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Détection de l'adresse MAC...",
            "mac_detect_success": "✅ Adresse MAC détectée : {}",
            "mac_detect_success_dialog": (
                "Adresse MAC détectée avec succès.\n\n"
                "IP : {1}\n"
                "MAC : {0}\n\n"
                "La valeur a été saisie dans le champ MAC."
            ),
            "mac_detect_failed": (
                "⚠ L'adresse MAC n'a pas pu être détectée automatiquement. "
                "L'aide va s'afficher."
            ),
            "config_mac_find": "🔍 Trouver la MAC",
            "config_mac_find_tooltip": (
                "Détecter automatiquement l'adresse MAC. "
                "En cas d'échec, un guide s'affichera."
            ),
        },
        # "🇮🇹 Italiano"
        "it": {
            "language": "Lingua:",
            "window_title": "Gestione NAS",
            "status_checking": "Controllo connessione al server...",
            "status_online": "Server NAS online ✓",
            "status_offline": "Server NAS offline",
            "status_settings": "Impostazioni aperte - Timer fermo",
            "status_settings_saved": "Impostazioni salvate",
            "status_settings_cancelled": "Impostazioni annullate",
            "status_shutdown": "Spegnimento NAS e Mac...",
            "status_shutdown_nas": "Spegnimento NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Spegnimento NAS inviato, Mac si spegnerà ora...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Spegnimento NAS fallito, spegnimento Mac comunque...",
            "status_starting": "Avvio NAS tramite Wake-on-LAN...",
            "status_waiting": "Attesa avvio server...",
            "status_wol_sent": "Magic Packet inviato",
            "status_wol_failed": "WOL fallito",
            "status_mounting": "Montaggio volumi selezionati...",
            "status_mounting_volume": "Montaggio {}...",
            "status_mounted": "{} montato ✓",
            "status_unmounting": "Espulsione {}...",
            "status_unmounted": "{} espulso ✓",
            "status_error": "Errore: {} non può essere montato",
            "status_error_unmount": "Errore: {} non può essere espulso",
            "status_all_mounted": "Tutti i volumi montati ✓",
            "status_all_unmounted": "Tutti i volumi espulsi ✓",
            "status_mount_all": "Montaggio tutti i volumi...",
            "status_unmount_all": "Espulsione tutti i volumi...",
            "status_shutdown_cmd": "Comando spegnimento NAS inviato ✓",
            "status_timeout": "Timeout - Il server non può essere avviato",
            "status_no_volumes": "Nessun volume montato",
            "status_mount_failed": "Montaggio fallito",
            "status_cancelled": "Annullato - L'applicazione si chiuderà",
            "status_esc": "Tasto ESC premuto - L'applicazione si chiuderà",
            "status_server_online": "Server online - attesa servizio SMB...",
            "status_profile_changed": "Profilo cambiato in: {}",
            "status_switching": "Passaggio al profilo: {}...",
            "btn_shutdown_both": "Mac e NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Annulla",
            "btn_start_nas": "Avvia NAS",
            "btn_settings": "Impostazioni (Cmd+E)",
            "btn_select_all": "Tutti",
            "btn_save": "Salva",
            "btn_reset": "Ripristina",
            "btn_info": "ℹ",
            "btn_profile": "Profili",
            "tooltip_shutdown_both": "Spegne Mac e NAS in 2 min",
            "tooltip_shutdown_nas": "Spegne solo il NAS",
            "tooltip_cancel": "Chiude l'applicazione",
            "tooltip_start_nas": "Avvia NAS tramite Wake-on-LAN",
            "tooltip_settings": "Impostazioni (Cmd+E)",
            "timer_shutdown": "Spegnimento automatico in {} secondi - INVIO solo NAS",
            "timer_start": "Avvio automatico in {} secondi - INVIO per avvio immediato",
            "volumes_title": "Volumi disponibili",
            "volumes_title_offline": "Volumi da montare all'avvio",
            "volumes_hint": "Nota: Il primo volume nell'elenco viene automaticamente considerato come volume principale e non può essere disabilitato.",
            "volumes_mount_tooltip": "Verrà montato automaticamente all'avvio del server",
            "config_title": "AnyNasPy - Impostazioni",
            "config_tab_profiles": "Profili server",
            "config_tab_general": "Generale",
            "config_tab_volumes": "Volumi",
            "config_tab_timing": "Tempi",
            "config_language": "Lingua:",
            "config_nas_group": "Impostazioni server NAS",
            "config_nas_user": "Nome utente:",
            "config_nas_dns": "Nome DNS:",
            "config_nas_ip": "Indirizzo IP:",
            "config_nas_mac": "Indirizzo MAC:",
            "config_ssh_key": "Percorso chiave SSH:",
            "config_volumes_group": "Volumi",
            "config_volumes_label": "Volumi (un nome per riga):",
            "config_time_group": "Impostazioni temporali (secondi)",
            "config_auto_shutdown": "Ritardo spegnimento automatico:",
            "config_auto_start": "Ritardo avvio automatico:",
            "config_wol_wait": "Tempo attesa WOL (max):",
            "config_smb_wait": "Tempo attesa SMB:",
            "config_mount_retries": "Tentativi di montaggio:",
            "config_status_file": "File di stato",
            "config_json_path": "File di configurazione JSON:",
            "config_profile_name": "Nome profilo:",
            "config_profile_active": "Profilo attivo",
            "config_profile_set_active": "Imposta come profilo attivo",
            "config_profile_list": "Profili esistenti:",
            "config_profile_new": "Nuovo profilo",
            "config_profile_delete": "Elimina profilo",
            "config_profile_duplicate": "Duplica profilo",
            "config_profile_rename": "Rinomina",
            "config_profile_required": "Il nome del profilo è obbligatorio.",
            "config_profile_exists": "Un profilo con questo nome esiste già.",
            "config_profile_deleted": "Il profilo '{}' è stato eliminato.",
            "config_profile_duplicated": "Il profilo '{}' è stato duplicato come '{}'.",
            "config_profile_renamed": "Il profilo è stato rinominato in '{}'.",
            "config_profile_activated": "Il profilo '{}' è ora attivo.",
            "config_find_ip": "🔍 Trova IP",
            "config_find_ip_tooltip": "Trova automaticamente l'IP del server nella rete",
            "config_ssh_help": "? Aiuto",
            "config_mac_help": "? Aiuto",
            "config_mac_help_tooltip": "Istruzioni per trovare l'indirizzo MAC",
            "msg_ip_found": "L'IP del server è stato trovato con successo:\n\n{}\n\nL'IP è stato inserito nel campo.",
            "msg_ip_not_found": "Non è stato possibile trovare automaticamente l'IP del server.\n\nInserisci manualmente l'indirizzo IP.\n\nSuggerimenti:\n• Controlla il nome DNS nelle impostazioni\n• Assicurati che il NAS sia acceso\n• Trova l'IP nell'interfaccia DSM in 'Sistema > Rete'",
            "msg_reset_confirm": "Ripristinare tutte le impostazioni ai valori predefiniti?",
            "msg_reset_title": "Ripristina",
            "msg_reset_done": "Tutte le impostazioni sono state ripristinate ai valori predefiniti.",
            "msg_delete_confirm": "Eliminare realmente il profilo '{}'?",
            "msg_delete_title": "Elimina profilo",
            "msg_no_active_profile": "Nessun profilo attivo selezionato.",
            "info_title": "Informazioni su AnyNasPy",
            "info_version": "Versione",
            "info_copyright": "Copyright",
            "info_license": "Licenza",
            "info_impressum": "Note legali",
            "info_developer": "Sviluppatore",
            "info_contact": "Contatti",
            "info_license_text": "Licenza MIT",
            "say_timer_shutdown": "Spegnimento automatico Mac e NAS in {} secondi - Invio solo NAS - Esc per annullare",
            "say_timer_start": "Il server NAS si avvierà in {} secondi - Invio per avvio immediato",
            "say_server_online": "Il server NAS è raggiungibile",
            "say_server_offline": "Il server NAS è offline",
            "say_shutdown_started": "Spegnimento avviato",
            "say_nas_shutdown": "Il NAS si sta spegnendo",
            "say_starting_nas": "Avvio NAS",
            "say_cancelled": "Annullato",
            "say_waiting_server": "Attesa avvio server",
            "say_wol_failed": "Errore durante l'invio",
            "say_server_reachable": "Server raggiungibile",
            "say_mount_volume": "{} pronto",
            "say_unmount_volume": "Espulsione {}",
            "say_mount_all": "Montaggio tutti i volumi",
            "say_unmount_all": "Espulsione tutti i volumi",
            "say_mount_error": "Errore durante il montaggio",
            "say_unmount_error": "Errore durante l'espulsione",
            "say_mount_failed": "Nessun volume montato",
            "say_settings_opened": "Impostazioni aperte",
            "say_settings_saved": "Impostazioni salvate",
            "say_settings_cancelled": "Impostazioni annullate",
            "say_workaround_deleted": "File di workaround eliminato",
            "say_server_timeout": "Timeout avvio server",
            "say_profile_changed": "Profilo cambiato in {}",
            "ssh_key_create_title": "Crea Chiave SSH",
            "ssh_key_create_question": "Vuoi creare una nuova coppia di chiavi SSH?",
            "ssh_key_create_existing": "La chiave SSH '{}' esiste già.\nVuoi sovrascriverla?",
            "ssh_key_create_comment": "Commento per la chiave SSH (opzionale):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "Chiave SSH creata: {}",
            "ssh_key_create_error": "Errore durante la creazione della chiave SSH",
            "ssh_key_create_timeout": "Tempo di creazione della chiave SSH scaduto",
            "ssh_key_create_failed": "ssh-keygen ha restituito un errore:\n{}",
            "ssh_key_create_passphrase": "Passphrase per la chiave SSH (lasciare vuoto per nessuna):",
            "ssh_key_create_passphrase_confirm": "Conferma passphrase:",
            "ssh_key_create_passphrase_mismatch": "Le passphrase non corrispondono.",
            "ssh_key_create_info": "✅ Coppia di chiavi SSH creata con successo:\n\n"
            "📁 Chiave Privata: {}\n"
            "📁 Chiave Pubblica: {}\n\n"
            "📋 Chiave Pubblica da copiare:\n"
            "{}\n\n"
            "🔑 Come installare la chiave sul tuo NAS:\n"
            "1. Copia la chiave pubblica (sopra)\n"
            "2. Aggiungila al file:\n"
            "   ~/.ssh/authorized_keys sul NAS\n"
            "3. Oppure usa:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Inserisci un nome file diverso:",
            "ssh_key_exists_also": "La chiave '{}' esiste anch'essa.\nPer favore eliminala prima o scegli un nome diverso.",
            "ssh_key_passphrase_title": "Passphrase",
            "ssh_key_passphrase_question": "Vuoi usare una passphrase per la chiave SSH?\n\nSenza passphrase: Connessione automatica possibile, meno sicura.\nCon passphrase: Più sicura, ma richiesta ad ogni connessione.",
            "ssh_key_passphrase_enter": "Inserisci passphrase",
            "ssh_key_passphrase_label": "Passphrase per la chiave SSH (almeno 4 caratteri):",
            "ssh_key_passphrase_none": "Nessuna passphrase",
            "ssh_key_passphrase_none_question": "Non hai inserito una passphrase.\nVuoi creare la chiave senza passphrase?",
            "ssh_key_passphrase_short": "Passphrase troppo corta",
            "ssh_key_passphrase_short_message": "La passphrase deve essere di almeno 4 caratteri.",
            "ssh_key_passphrase_confirm": "Conferma passphrase",
            "ssh_key_passphrase_confirm_label": "Inserisci nuovamente la passphrase:",
            "ssh_key_passphrase_mismatch_title": "Errore passphrase",
            "ssh_key_passphrase_mismatch_message": "Le passphrase non corrispondono.",
            "config_ssh_open": "Apri",
            "config_ssh_open_tooltip": "Seleziona chiave SSH o apri cartella",
            "config_ssh_create": "Crea",
            "config_ssh_create_tooltip": "Crea nuova coppia di chiavi SSH",
            "config_ssh_help_tooltip": "Mostra aiuto chiave SSH",
            "config_ssh_select": "Seleziona chiave SSH",
            "config_json_open": "Apri",
            "config_json_open_tooltip": "Apri cartella di configurazione JSON",
            "config_error": "Errore",
            "config_shutdown_mac_delay": "Tempo di attesa tra spegnimento NAS e Mac:",
            "info_third_party": "Librerie di terze parti",
            "info_pyqt5_license": "Questa applicazione utilizza PyQt5, concesso in licenza secondo la GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nIl testo completo della licenza è disponibile all'indirizzo https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Rileva volumi",
            "volumes_add": "Aggiungi",
            "volumes_delete": "Elimina",
            "volumes_move_up": "Sposta su",
            "volumes_move_down": "Sposta giù",
            "volumes_available": "Volumi disponibili:",
            "volumes_no_volumes": "Nessun volume trovato.",
            "volumes_detection_failed": "Errore nel rilevamento dei volumi.",
            "volumes_detection_success": "Volumi rilevati con successo.",
            "volumes_confirm_delete": "Eliminare realmente il volume '{}'?",
            "volumes_enter_name": "Inserisci il nome del nuovo volume:",
            "volumes_name_exists": "Esiste già un volume con questo nome.",
            "msg_invalid_ip": "L'indirizzo IP inserito non è valido.\nInserisci un indirizzo IPv4 valido (es. 192.168.1.100).",
            "msg_select_volume": "Seleziona un volume.",
            "msg_cannot_delete_main_volume": "Non è possibile eliminare il primo volume (volume principale).",
            "profile_cannot_delete_last": "Non è possibile eliminare l'ultimo profilo.",
            "status_wol_sending": "Invio pacchetto magico...",
            "status_wol_method_failed": "Metodo Python fallito, tentativo del successivo...",
            "status_trying_wakeonlan": "Tentativo con wakeonlan...",
            "status_trying_etherwake": "Tentativo con etherwake...",
            "ssh_key_system_key_warning": "Avviso di sicurezza",
            "ssh_key_system_key_message": "Il nome '{}' è una chiave di sistema e non verrà sovrascritto.\nScegli un altro nome (es. synaspy_rsa).",
            "profile_name_exists": "Esiste già un profilo con il nome '{}'.",
            "config_profile_created": "Profilo '{}' creato.",
            "config_profile_create_failed": "Impossibile creare il profilo.",
            "config_profile_rename_failed": "Rinominazione fallita.",
            "config_profile_duplicate_name": "Nome per il profilo duplicato:",
            "config_profile_duplicate_failed": "Duplicazione fallita.",
            "config_profile_delete_failed": "Eliminazione fallita.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Spegne solo il Mac (il NAS resta acceso, nessun WOL)",
            "status_shutdown_mac_only": "Spegnimento solo del Mac...",
            "say_shutdown_mac_only": "Il Mac si sta spegnendo, il NAS resta acceso",

            "btn_scheduled_shutdown": "🕐 Spegnimento programmato",
            "tooltip_scheduled_shutdown": "Si spegne dopo un tempo scelto dall'utente",
            "btn_scheduled_shutdown_offline": "🕐 Spegnere il Mac in modo programmato",
            "tooltip_scheduled_shutdown_offline": "Spegne solo il Mac dopo un tempo selezionato (il NAS è offline)",
            "btn_cancel_scheduled": "⏹ Annulla conto alla rovescia",
            "tooltip_cancel_scheduled": "Annulla il conto alla rovescia attivo",

            "sched_dialog_title": "Spegnimento programmato",
            "sched_target_label": "Destinazione:",
            "sched_target_both": "🖥️ Mac + NAS  (spegnimento completo)",
            "sched_target_nas": "🗄️ Solo NAS  (il Mac resta acceso)",
            "sched_target_mac": "💻 Solo Mac  (il NAS resta acceso)",

            "sched_wait_label": "Tempo di attesa fino allo spegnimento:",
            "sched_hours": "Ore",
            "sched_minutes": "Minuti",

            "sched_caffeinate_label": "Opzione caffeinate (mantiene il Mac sveglio):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Consigliato: Sistema sveglio, lo schermo può oscurarsi  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Impedisci solo inattività e disco (lo schermo resta acceso)  (-i -m)",
            "sched_caffeinate_d": "Anche lo schermo resta acceso  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simula attività utente (schermo luminoso, sistema sveglio)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Massimo: Schermo + sistema + disco permanentemente svegli  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Disattivato (normale risparmio energetico – il sistema può dormire)",

            "sched_caffeinate_hint": (
                "💡 Curiosità didattica: Usa i flag di caffeinate direttamente nel terminale:\n"
                "   -i  impedisce il sonno per inattività del sistema\n"
                "   -m  impedisce il sonno del disco (il disco rigido non dorme)\n"
                "   -s  impedisce il sonno del sistema (solo con alimentatore)\n"
                "   -d  impedisce il sonno dello schermo (lo schermo resta acceso)\n"
                "   -u  simula l'attività dell'utente (lo schermo resta luminoso)\n"
                "   -w PID  termina caffeinate quando il processo PID termina\n"
                "Esempio:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Spegnimento programmato per: {}",
            "sched_countdown_label": "Conto alla rovescia: {} fino allo spegnimento ({})",
            "sched_started": "Timer avviato.\n\nDestinazione: {}\nDurata: {}\nFine: {}",
            "sched_cancelled": "Timer annullato",
            "sched_already_active": "È già in esecuzione un timer. Annullarlo prima?",
            "sched_invalid_time": "Inserisci un tempo valido (almeno 1 minuto).",
            "sched_max_time": "Massimo consentito 720 ore (30 giorni).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Timer avviato. Mac e NAS si spegneranno tra {}."
            ),
            "sched_voice_started_nas": (
                "Timer avviato. Solo il NAS si spegnerà tra {}. "
                "Il Mac resta acceso."
            ),
            "sched_voice_started_mac": (
                "Timer avviato. Solo il Mac si spegnerà tra {}. "
                "Il NAS resta acceso."
            ),
            "sched_voice_started_nothing": (
                "Timer avviato. Alla scadenza non verrà eseguito nulla. "
                "caffeinate resta attivo fino ad allora."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Il Mac resta sveglio per {}. "
                "Lo schermo può oscurarsi. "
                "Alla scadenza non verrà eseguito nulla."
            ),
            "sched_voice_nothing_im": (
                "Il Mac resta sveglio per {}. "
                "Lo schermo resta acceso. "
                "Alla scadenza non verrà eseguito nulla."
            ),
            "sched_voice_nothing_d": (
                "Il Mac e lo schermo restano accesi per {}. "
                "Alla scadenza non verrà eseguito nulla."
            ),
            "sched_voice_nothing_u": (
                "Il Mac resta attivo per {}. "
                "Lo schermo resta luminoso. "
                "Alla scadenza non verrà eseguito nulla."
            ),
            "sched_voice_nothing_full": (
                "Il Mac resta completamente attivo per {} – schermo e sistema svegli continuamente. "
                "Alla scadenza non verrà eseguito nulla."
            ),
            "sched_voice_nothing_off": (
                "Il timer funziona per {}. "
                "Alla scadenza non verrà eseguito nulla. "
                "Attenzione: Il Mac può entrare in modalità sospensione."
            ),
            "sched_voice_cancelled": "Timer annullato",
            "sched_caffeinate_failed": "Impossibile avviare caffeinate:\n{}",
            "sched_target_required": "Seleziona una destinazione.",
            "sched_tooltip_active": "Timer in esecuzione – clicca per annullare",

            "status_scheduled_active": "Timer attivo - {} rimanente",
            "status_scheduled_triggered": "Timer scaduto - avvio di {}",
            "status_scheduled_cancelled": "Timer annullato",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Timer attivo",
            "close_blocked_text": (
                "<b>È ancora in esecuzione un timer!</b><br><br>"
                "Programmato: {}<br>"
                "Rimanente: <b>{}</b><br>"
                "Alle: {}<br><br>"
                "Se chiudi ora, lo spegnimento programmato "
                "<b>non verrà più eseguito</b>."
            ),
            "close_blocked_yes": "Chiudi comunque",
            "close_blocked_no": "Lascia l'app in esecuzione",
            "close_blocked_cancel_text": (
                "È ancora in esecuzione un timer.\n\n"
                "Vuoi davvero chiudere l'app?\n"
                "(Lo spegnimento programmato verrà scartato.)"
            ),
            "close_blocked_log_aborted": "Chiusura annullata (timer attivo)",
            "close_blocked_log_discarded": (
                "L'app si chiude nonostante il timer attivo – timer scartato"
            ),
            "close_blocked_log_cancel_aborted": (
                "Chiusura dell'app annullata tramite il pulsante Annulla"
            ),
            "duration_day": "giorno",
            "duration_days": "giorni",
            "duration_hour": "ora",
            "duration_hours": "ore",
            "duration_minute": "minuto",
            "duration_minutes": "minuti",
            "duration_connector_and": "e",
            "tooltip_pause_timer": "Pausa / riprendi timer",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Timer in pausa – {} secondi rimanenti",
            "timer_resumed": "Timer ripreso",
            "say_timer_paused": "Timer in pausa",
            "say_timer_resumed": "Timer ripreso",
            "tooltip_pause_timer": "Metti in pausa/riprendi il timer",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Uscita vocale attivata",
            "speech_enabled_hint": (
                "Pronuncia messaggi di stato, conferme del volume e "
                "informazioni sul timer tramite l'uscita vocale di macOS. "
                "Se disattivata, l'app funziona in silenzio."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Per lo spegnimento programmato del Mac è richiesta la "
                "password di amministratore.\n\n"
                "Viene salvata in modo sicuro nel portachiavi di macOS e "
                "utilizzata solo durante lo spegnimento.\n\n"
                "Configurare ora?"
            ),
            "mac_pw_dialog_title": "Password di amministratore",
            "mac_pw_dialog_message": (
                "Per lo spegnimento del Mac è richiesta la password di "
                "amministratore.\n\n"
                "Viene salvata in modo sicuro nel portachiavi di macOS e "
                "utilizzata solo durante lo spegnimento."
            ),
            "mac_pw_wrong_password": (
                "La password è errata.\n\n"
                "Riprova."
            ),
            "mac_pw_test_failed": (
                "Errore durante la verifica della password:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Il timer non è stato avviato perché l'inserimento della "
                "password è stato annullato.\n\n"
                "Senza password il Mac non può essere spento."
            ),
            "clear_password_title": "Elimina password salvata",
            "clear_password_message": (
                "Eliminare la password di amministratore salvata nel portachiavi?\n\n"
                "Al prossimo spegnimento programmato la password "
                "verrà richiesta di nuovo."
            ),
            "clear_password_success": "La password è stata rimossa dal portachiavi.",
            "clear_password_failed": "Non è stato possibile eliminare la password.",
            "clear_password_description": (
                "Rimuove la password di amministratore salvata nel "
                "portachiavi di macOS. Al prossimo spegnimento programmato "
                "verrà richiesta di nuovo."
            ),
            "clear_password_button": "Elimina password salvata",
            "shutdown_no_password_message": (
                "Non è stato possibile spegnere il Mac.\n\n"
                "Non è disponibile né una regola NOPASSWD in sudoers né una "
                "password salvata nel portachiavi.\n\n"
                "Configura di nuovo lo spegnimento programmato."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Avviso",
            "warning_eject_failed_continue": (
                "Non è stato possibile espellere correttamente le unità di rete.\n\n"
                "Se sono ancora in corso copie di dati o ci sono file aperti, "
                "potrebbero verificarsi perdite di dati.\n\n"
                "Continuare comunque con lo spegnimento?"
            ),
            "auto_timer_disabled_no_pw": (
                "Spegnimento automatico disattivato – nessuna password di "
                "amministratore disponibile. Inseriscila una volta al prossimo avviso."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Sì",
            "btn_no": "No",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Non spegnere nulla  (Il Mac resta sveglio – ad es. per script di backup)",
            "sched_countdown_coffee_label": "⏳ caffeinate attivo: {} rimanenti ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Timer caffè ancora attivo",
            "coffee_conflict_message": (
                "Un timer caffè è ancora in esecuzione:\n\n"
                "Rimanente: {}\n\n"
                "Se spegni adesso, il timer caffè verrà annullato "
                "e caffeinate sarà fermato.\n\n"
                "Spegnere comunque?"
            ),
            "shutdown_timer_conflict_title": "Timer di spegnimento ancora attivo",
            "shutdown_timer_conflict_message": (
                "Un timer di spegnimento è ancora in esecuzione:\n\n"
                "Programmato: {}\n"
                "Rimanente: {}\n\n"
                "Se spegni manualmente adesso, il timer verrà annullato "
                "e dovrà essere riprogrammato.\n\n"
                "Spegnere comunque?"
            ),
            "tooltip_stop_timer": "Ferma completamente il timer",
            "tooltip_stop_timer_inactive": "Nessun timer attivo",
            "timer_stopped_notice": "⏹ Timer fermato – pronto per il riavvio",
            "say_timer_stopped": "Timer fermato",
            "say_timer_restarted": "Timer riavviato",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "Produttore NAS:",
            "vendor_tooltip": (
                "Seleziona il produttore del tuo NAS. Determina i comandi "
                "di spegnimento e i percorsi predefiniti. 'Rilevamento "
                "automatico' controlla il NAS via SSH."
            ),
            "vendor_auto_detect": "🔄 Rilevamento automatico",
            "vendor_auto_detect_tooltip": (
                "Rileva automaticamente il produttore via SSH. "
                "Requisito: la chiave SSH e l'IP sono configurati correttamente."
            ),
            "vendor_detect_in_progress": "🔄 Rilevamento in corso...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Linux generico",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Personalizzato",
            "vendor_custom_hint": (
                "Personalizzato: adatta manualmente i comandi di spegnimento. "
                "Predefinito: 'sudo shutdown -h now' (funziona sull'"
                "80 % di tutti i NAS Linux)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Produttore rilevato: {}",
            "vendor_detect_success_question": (
                "Produttore rilevato: {}\n\n"
                "Vuoi utilizzare questo produttore?\n"
                "(Valore attuale: {})"
            ),
            "vendor_detect_failed": (
                "Impossibile rilevare automaticamente il produttore.\n\n"
                "Selezionalo manualmente. La maggior parte dei NAS Linux "
                "funziona con 'Linux generico'."
            ),
            "vendor_detect_no_ssh": (
                "Il rilevamento automatico richiede l'accesso SSH.\n\n"
                "Controlla quanto segue:\n"
                "• Il percorso della chiave SSH è corretto\n"
                "• L'indirizzo IP è corretto\n"
                "• SSH è attivo sul NAS\n"
                "• La chiave SSH è installata sul NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Inserisci prima la chiave SSH e l'indirizzo IP."
            ),
            "vendor_detect_nas_offline": (
                "Il server NAS non risponde.\n\n"
                "Controlla quanto segue:\n"
                "• Il NAS è acceso?\n"
                "• L'indirizzo IP è corretto?\n"
                "• Il NAS è sulla stessa rete?\n\n"
                "Accendi il NAS e riprova."
            ),
            "vendor_detect_error": "Errore durante il rilevamento automatico:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "Chiave SSH non trovata:\n\n{}\n\n"
                "Controlla il percorso nelle impostazioni."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Comando di spegnimento:",
            "custom_cmd_tooltip": (
                "Il comando inviato al NAS via SSH. "
                "Separa più comandi con un punto e virgola."
            ),
            "custom_cmd_hint": (
                "💡 Separa più comandi con un punto e virgola — "
                "viene utilizzato il primo che ha successo. "
                "Esempio: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Mostra la guida sui comandi di spegnimento",
            "custom_cmd_help_title": "Comandi di spegnimento tipici",
            "custom_cmd_help_text": (
                "<h3>Comandi di spegnimento tipici per produttore</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (generico):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Più comandi (catena di riserva)</h4>"
                "<p>Se il primo comando fallisce, viene provato il successivo. "
                "Separazione con punto e virgola:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Suggerimento:</b> scegli prima il comando più probabile, "
                "poi le alternative come riserva.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Rilevamento dei volumi via SSH...",
            "volumes_detection_via_paths": (
                "🔍 Ricerca nei percorsi specifici del produttore..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Riserva: ricerca tramite smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Ricerca dei volumi via SSH... La ricerca può "
                "richiedere alcuni secondi."
            ),
            "volumes_detect_panel_success": (
                "{} volumi trovati — {} aggiunti nuovi, "
                "{} già presenti"
            ),
            "volumes_detect_panel_partial": (
                "{} volumi trovati — tutti già presenti nella lista"
            ),
            "volumes_detect_panel_failed": (
                "Nessun volume trovato. "
                "Inserisci i volumi manualmente."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Rilevamento dell'indirizzo MAC...",
            "mac_detect_success": "✅ Indirizzo MAC rilevato: {}",
            "mac_detect_success_dialog": (
                "Indirizzo MAC rilevato con successo.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Il valore è stato inserito nel campo MAC."
            ),
            "mac_detect_failed": (
                "⚠ Impossibile rilevare automaticamente l'indirizzo MAC. "
                "Verrà mostrata la guida."
            ),
            "config_mac_find": "🔍 Trova MAC",
            "config_mac_find_tooltip": (
                "Rileva automaticamente l'indirizzo MAC. "
                "Se fallisce, verrà mostrata una guida."
            ),
        },
        "🇳🇱 Nederlands"
        "nl": {
            "language": "Taal:",
            "window_title": "NAS Beheer",
            "status_checking": "Serververbinding controleren...",
            "status_online": "NAS Server is online ✓",
            "status_offline": "NAS Server is offline",
            "status_settings": "Instellingen geopend - Timer gestopt",
            "status_settings_saved": "Instellingen opgeslagen",
            "status_settings_cancelled": "Instellingen geannuleerd",
            "status_shutdown": "NAS en Mac uitschakelen...",
            "status_shutdown_nas": "NAS uitschakelen...",
            "status_shutdown_nas_sent_mac_follows": "✅ NAS-uitschakeling verzonden, Mac wordt nu uitgeschakeld...",
            "status_shutdown_nas_failed_mac_still": "⚠️ NAS-uitschakeling mislukt, Mac wordt toch uitgeschakeld...",
            "status_starting": "NAS starten via Wake-on-LAN...",
            "status_waiting": "Wachten op serverstart...",
            "status_wol_sent": "Magic Packet verzonden",
            "status_wol_failed": "WOL mislukt",
            "status_mounting": "Geselecteerde volumes koppelen...",
            "status_mounting_volume": "{} koppelen...",
            "status_mounted": "{} gekoppeld ✓",
            "status_unmounting": "{} ontkoppelen...",
            "status_unmounted": "{} ontkoppeld ✓",
            "status_error": "Fout: {} kon niet worden gekoppeld",
            "status_error_unmount": "Fout: {} kon niet worden ontkoppeld",
            "status_all_mounted": "Alle volumes gekoppeld ✓",
            "status_all_unmounted": "Alle volumes ontkoppeld ✓",
            "status_mount_all": "Alle volumes koppelen...",
            "status_unmount_all": "Alle volumes ontkoppelen...",
            "status_shutdown_cmd": "NAS-uitschakelopdracht verzonden ✓",
            "status_timeout": "Time-out - Server kon niet starten",
            "status_no_volumes": "Geen volumes gekoppeld",
            "status_mount_failed": "Koppelen mislukt",
            "status_cancelled": "Geannuleerd - App wordt gesloten",
            "status_esc": "ESC ingedrukt - App wordt gesloten",
            "status_server_online": "Server online - wachten op SMB-service...",
            "status_profile_changed": "Profiel gewijzigd naar: {}",
            "status_switching": "Overschakelen naar profiel: {}...",
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Annuleren",
            "btn_start_nas": "Start NAS",
            "btn_settings": "Instellingen (Cmd+E)",
            "btn_select_all": "Alles",
            "btn_save": "Opslaan",
            "btn_reset": "Reset",
            "btn_info": "ℹ",
            "btn_profile": "Profielen",
            "tooltip_shutdown_both": "Schakelt Mac en NAS uit in 2 min",
            "tooltip_shutdown_nas": "Schakelt alleen NAS uit",
            "tooltip_cancel": "Sluit de app",
            "tooltip_start_nas": "Start NAS via Wake-on-LAN",
            "tooltip_settings": "Instellingen (Cmd+E)",
            "timer_shutdown": "Automatisch uitschakelen in {} seconden - ENTER alleen NAS",
            "timer_start": "Automatisch starten in {} seconden - ENTER voor onmiddellijke start",
            "volumes_title": "Beschikbare volumes",
            "volumes_title_offline": "Volumes om te koppelen bij opstart",
            "volumes_hint": "Opmerking: Het eerste volume in de lijst wordt automatisch als hoofdvolume behandeld en kan niet worden uitgeschakeld.",
            "volumes_mount_tooltip": "Wordt automatisch gekoppeld bij serverstart",
            "config_title": "AnyNasPy - Instellingen",
            "config_tab_profiles": "Serverprofielen",
            "config_tab_general": "Algemeen",
            "config_tab_volumes": "Volumes",
            "config_tab_timing": "Timing",
            "config_language": "Taal:",
            "config_nas_group": "NAS Server Instellingen",
            "config_nas_user": "Gebruikersnaam:",
            "config_nas_dns": "DNS-naam:",
            "config_nas_ip": "IP-adres:",
            "config_nas_mac": "MAC-adres:",
            "config_ssh_key": "SSH-sleutelpad:",
            "config_volumes_group": "Volumes",
            "config_volumes_label": "Volumes (één naam per regel):",
            "config_time_group": "Tijdinstellingen (seconden)",
            "config_auto_shutdown": "Vertraging automatisch uitschakelen:",
            "config_auto_start": "Vertraging automatisch starten:",
            "config_wol_wait": "WOL-wachttijd (max):",
            "config_smb_wait": "SMB-wachttijd:",
            "config_mount_retries": "Koppelpogingen:",
            "config_status_file": "Statusbestand",
            "config_json_path": "JSON-configuratiebestand:",
            "config_profile_name": "Profielnaam:",
            "config_profile_active": "Actief profiel",
            "config_profile_set_active": "Instellen als actief profiel",
            "config_profile_list": "Bestaande profielen:",
            "config_profile_new": "Nieuw profiel",
            "config_profile_delete": "Profiel verwijderen",
            "config_profile_duplicate": "Profiel dupliceren",
            "config_profile_rename": "Hernoemen",
            "config_profile_required": "Profielnaam is verplicht.",
            "config_profile_exists": "Er bestaat al een profiel met deze naam.",
            "config_profile_deleted": "Profiel '{}' is verwijderd.",
            "config_profile_duplicated": "Profiel '{}' is gedupliceerd als '{}'.",
            "config_profile_renamed": "Profiel is hernoemd naar '{}'.",
            "config_profile_activated": "Profiel '{}' is nu actief.",
            "config_find_ip": "🔍 IP zoeken",
            "config_find_ip_tooltip": "Automatisch server-IP in netwerk zoeken",
            "config_ssh_help": "? Help",
            "config_mac_help": "? Help",
            "config_mac_help_tooltip": "Instructies om MAC-adres te vinden",
            "msg_ip_found": "Server-IP is succesvol gevonden:\n\n{}\n\nHet IP is in het veld ingevoerd.",
            "msg_ip_not_found": "Server-IP kon niet automatisch worden gevonden.\n\nVoer het IP-adres handmatig in.\n\nTips:\n• Controleer de DNS-naam in instellingen\n• Zorg dat de NAS is ingeschakeld\n• Vind het IP in DSM onder 'Systeem > Netwerk'",
            "msg_reset_confirm": "Alle instellingen terugzetten naar standaardwaarden?",
            "msg_reset_title": "Reset",
            "msg_reset_done": "Alle instellingen zijn teruggezet naar standaardwaarden.",
            "msg_delete_confirm": "Weet u zeker dat u profiel '{}' wilt verwijderen?",
            "msg_delete_title": "Profiel verwijderen",
            "msg_no_active_profile": "Geen actief profiel geselecteerd.",
            "info_title": "Over AnyNasPy",
            "info_version": "Versie",
            "info_copyright": "Copyright",
            "info_license": "Licentie",
            "info_impressum": "Impressum",
            "info_developer": "Ontwikkelaar",
            "info_contact": "Contact",
            "info_license_text": "MIT-licentie",
            "say_timer_shutdown": "Automatisch uitschakelen Mac en NAS in {} seconden - Enter alleen NAS - Escape om te annuleren",
            "say_timer_start": "De NAS-server start in {} seconden - Enter voor onmiddellijke start",
            "say_server_online": "NAS-server is bereikbaar",
            "say_server_offline": "NAS-server is offline",
            "say_shutdown_started": "Uitschakelen gestart",
            "say_nas_shutdown": "NAS wordt uitgeschakeld",
            "say_starting_nas": "NAS starten",
            "say_cancelled": "Geannuleerd",
            "say_waiting_server": "Wachten op serverstart",
            "say_wol_failed": "Fout bij verzenden",
            "say_server_reachable": "Server bereikbaar",
            "say_mount_volume": "{} klaar",
            "say_unmount_volume": "{} ontkoppelen",
            "say_mount_all": "Alle volumes koppelen",
            "say_unmount_all": "Alle volumes ontkoppelen",
            "say_mount_error": "Fout bij koppelen",
            "say_unmount_error": "Fout bij ontkoppelen",
            "say_mount_failed": "Geen volumes gekoppeld",
            "say_settings_opened": "Instellingen geopend",
            "say_settings_saved": "Instellingen opgeslagen",
            "say_settings_cancelled": "Instellingen geannuleerd",
            "say_workaround_deleted": "Workaround-bestand verwijderd",
            "say_server_timeout": "Server-start time-out",
            "say_profile_changed": "Profiel gewijzigd naar {}",
            "ssh_key_create_title": "SSH-sleutel aanmaken",
            "ssh_key_create_question": "Wil je een nieuw SSH-sleutelpaar aanmaken?",
            "ssh_key_create_existing": "SSH-sleutel '{}' bestaat al.\nWil je deze overschrijven?",
            "ssh_key_create_comment": "Opmerking voor de SSH-sleutel (optioneel):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH-sleutel aangemaakt: {}",
            "ssh_key_create_error": "Fout bij het aanmaken van SSH-sleutel",
            "ssh_key_create_timeout": "Tijd voor aanmaken SSH-sleutel verlopen",
            "ssh_key_create_failed": "ssh-keygen gaf een fout terug:\n{}",
            "ssh_key_create_passphrase": "Wachtzin voor SSH-sleutel (laat leeg voor geen):",
            "ssh_key_create_passphrase_confirm": "Bevestig wachtzin:",
            "ssh_key_create_passphrase_mismatch": "De wachtzinnen komen niet overeen.",
            "ssh_key_create_info": "✅ SSH-sleutelpaar succesvol aangemaakt:\n\n"
            "📁 Privésleutel: {}\n"
            "📁 Publieke Sleutel: {}\n\n"
            "📋 Publieke Sleutel om te kopiëren:\n"
            "{}\n\n"
            "🔑 Hoe installeer je de sleutel op je NAS:\n"
            "1. Kopieer de publieke sleutel (hierboven)\n"
            "2. Voeg deze toe aan het bestand:\n"
            "   ~/.ssh/authorized_keys op de NAS\n"
            "3. Of gebruik:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Voer een andere bestandsnaam in:",
            "ssh_key_exists_also": "De sleutel '{}' bestaat ook.\nVerwijder deze eerst of kies een andere naam.",
            "ssh_key_passphrase_title": "Wachtzin",
            "ssh_key_passphrase_question": "Wil je een wachtzin gebruiken voor de SSH-sleutel?\n\nZonder wachtzin: Automatische verbinding mogelijk, minder veilig.\nMet wachtzin: Veiliger, maar vraagt bij elke verbinding.",
            "ssh_key_passphrase_enter": "Voer wachtzin in",
            "ssh_key_passphrase_label": "Wachtzin voor SSH-sleutel (minimaal 4 tekens):",
            "ssh_key_passphrase_none": "Geen wachtzin",
            "ssh_key_passphrase_none_question": "Je hebt geen wachtzin ingevoerd.\nWil je de sleutel zonder wachtzin aanmaken?",
            "ssh_key_passphrase_short": "Wachtzin te kort",
            "ssh_key_passphrase_short_message": "De wachtzin moet minimaal 4 tekens lang zijn.",
            "ssh_key_passphrase_confirm": "Bevestig wachtzin",
            "ssh_key_passphrase_confirm_label": "Voer wachtzin opnieuw in:",
            "ssh_key_passphrase_mismatch_title": "Wachtzin fout",
            "ssh_key_passphrase_mismatch_message": "De wachtzinnen komen niet overeen.",
            "config_ssh_open": "Openen",
            "config_ssh_open_tooltip": "Selecteer SSH-sleutel of open map",
            "config_ssh_create": "Aanmaken",
            "config_ssh_create_tooltip": "Nieuw SSH-sleutelpaar aanmaken",
            "config_ssh_help_tooltip": "Toon SSH-sleutel hulp",
            "config_ssh_select": "Selecteer SSH-sleutel",
            "config_json_open": "Openen",
            "config_json_open_tooltip": "Open JSON-configuratiemap",
            "config_error": "Fout",
            "config_shutdown_mac_delay": "Vertraging tussen NAS en Mac uitschakelen:",
            "info_third_party": "Bibliotheken van derden",
            "info_pyqt5_license": "Deze applicatie gebruikt PyQt5, dat is gelicentieerd onder de GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nDe volledige licentietekst is te vinden op https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Volumes detecteren",
            "volumes_add": "Toevoegen",
            "volumes_delete": "Verwijderen",
            "volumes_move_up": "Naar boven",
            "volumes_move_down": "Naar beneden",
            "volumes_available": "Beschikbare volumes:",
            "volumes_no_volumes": "Geen volumes gevonden.",
            "volumes_detection_failed": "Fout bij detecteren van volumes.",
            "volumes_detection_success": "Volumes succesvol gedetecteerd.",
            "volumes_confirm_delete": "Volume '{}' echt verwijderen?",
            "volumes_enter_name": "Voer de naam van het nieuwe volume in:",
            "volumes_name_exists": "Er bestaat al een volume met deze naam.",
            "msg_invalid_ip": "Het ingevoerde IP-adres is ongeldig.\nVoer een geldig IPv4-adres in (bijv. 192.168.1.100).",
            "msg_select_volume": "Selecteer een volume.",
            "msg_cannot_delete_main_volume": "Het eerste volume (hoofdvolume) kan niet worden verwijderd.",
            "profile_cannot_delete_last": "Het laatste profiel kan niet worden verwijderd.",
            "status_wol_sending": "Verzenden magisch pakket...",
            "status_wol_method_failed": "Python-methode mislukt, volgende proberen...",
            "status_trying_wakeonlan": "Probeer wakeonlan...",
            "status_trying_etherwake": "Probeer etherwake...",
            "ssh_key_system_key_warning": "Veiligheids waarschuwing",
            "ssh_key_system_key_message": "De naam '{}' is een systeemsleutel en wordt niet overschreven.\nKies een andere naam (bijv. synaspy_rsa).",
            "profile_name_exists": "Er bestaat al een profiel met de naam '{}'.",
            "config_profile_created": "Profiel '{}' is aangemaakt.",
            "config_profile_create_failed": "Profiel kon niet worden aangemaakt.",
            "config_profile_rename_failed": "Hernoemen mislukt.",
            "config_profile_duplicate_name": "Naam voor het gedupliceerde profiel:",
            "config_profile_duplicate_failed": "Dupliceren mislukt.",
            "config_profile_delete_failed": "Verwijderen mislukt.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Zet alleen de Mac uit (NAS blijft aan, geen WOL)",
            "status_shutdown_mac_only": "Alleen de Mac wordt afgesloten...",
            "say_shutdown_mac_only": "Mac wordt afgesloten, NAS blijft aan",

            "btn_scheduled_shutdown": "🕐 Gepland afsluiten",
            "tooltip_scheduled_shutdown": "Sluit af na een door de gebruiker gekozen tijd",
            "btn_scheduled_shutdown_offline": "🕐 Mac gepland afsluiten",
            "tooltip_scheduled_shutdown_offline": "Zet alleen de Mac uit na een gekozen tijd (NAS is offline)",
            "btn_cancel_scheduled": "⏹ Aftellen annuleren",
            "tooltip_cancel_scheduled": "Annuleert het actieve aftellen",

            "sched_dialog_title": "Gepland afsluiten",
            "sched_target_label": "Doel:",
            "sched_target_both": "🖥️ Mac + NAS  (volledig afsluiten)",
            "sched_target_nas": "🗄️ Alleen NAS  (Mac blijft aan)",
            "sched_target_mac": "💻 Alleen Mac  (NAS blijft aan)",

            "sched_wait_label": "Wachttijd tot afsluiten:",
            "sched_hours": "Uren",
            "sched_minutes": "Minuten",

            "sched_caffeinate_label": "caffeinate-optie (houdt de Mac wakker):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Aanbevolen: Systeem wakker, scherm mag dimmen  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Alleen idle & disk voorkomen (scherm blijft aan)  (-i -m)",
            "sched_caffeinate_d": "Scherm blijft bovendien aan  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Gebruikersactiviteit simuleren (scherm helder, systeem wakker)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maximaal: Scherm + systeem + disk permanent wakker  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Uit (normale energiebesparing – systeem kan slapen)",

            "sched_caffeinate_hint": (
                "💡 Leerfeit: Gebruik caffeinate-flags direct in de terminal:\n"
                "   -i  voorkomt idle-sleep van het systeem\n"
                "   -m  voorkomt disk-sleep (harde schijf gaat niet slapen)\n"
                "   -s  voorkomt system-sleep (alleen op netstroom)\n"
                "   -d  voorkomt display-sleep (scherm blijft aan)\n"
                "   -u  simuleert gebruikersactiviteit (display blijft helder)\n"
                "   -w PID  beëindigt caffeinate wanneer proces PID eindigt\n"
                "Voorbeeld:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Afsluiten gepland voor: {}",
            "sched_countdown_label": "Aftellen: {} tot afsluiten ({})",
            "sched_started": "Timer gestart.\n\nDoel: {}\nDuur: {}\nEinde: {}",
            "sched_cancelled": "Timer geannuleerd",
            "sched_already_active": "Er loopt al een timer. Eerst annuleren?",
            "sched_invalid_time": "Voer een geldige tijd in (minimaal 1 minuut).",
            "sched_max_time": "Maximaal 720 uur (30 dagen) toegestaan.",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Timer gestart. Mac en NAS worden over {} afgesloten."
            ),
            "sched_voice_started_nas": (
                "Timer gestart. Alleen de NAS wordt over {} afgesloten. "
                "De Mac blijft aan."
            ),
            "sched_voice_started_mac": (
                "Timer gestart. Alleen de Mac wordt over {} afgesloten. "
                "De NAS blijft aan."
            ),
            "sched_voice_started_nothing": (
                "Timer gestart. Na afloop wordt niets uitgevoerd. "
                "caffeinate blijft tot dan actief."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "De Mac blijft {} wakker. "
                "Het scherm mag dimmen. "
                "Na afloop wordt niets uitgevoerd."
            ),
            "sched_voice_nothing_im": (
                "De Mac blijft {} wakker. "
                "Het scherm blijft aan. "
                "Na afloop wordt niets uitgevoerd."
            ),
            "sched_voice_nothing_d": (
                "De Mac en het scherm blijven {} aan. "
                "Na afloop wordt niets uitgevoerd."
            ),
            "sched_voice_nothing_u": (
                "De Mac blijft {} actief. "
                "Het scherm blijft helder. "
                "Na afloop wordt niets uitgevoerd."
            ),
            "sched_voice_nothing_full": (
                "De Mac blijft {} volledig actief – scherm en systeem continu wakker. "
                "Na afloop wordt niets uitgevoerd."
            ),
            "sched_voice_nothing_off": (
                "De timer loopt {}. "
                "Na afloop wordt niets uitgevoerd. "
                "Let op: De Mac kan in slaapstand gaan."
            ),
            "sched_voice_cancelled": "Timer geannuleerd",
            "sched_caffeinate_failed": "caffeinate kon niet worden gestart:\n{}",
            "sched_target_required": "Selecteer een doel.",
            "sched_tooltip_active": "Timer actief – klik om te annuleren",

            "status_scheduled_active": "Timer actief - {} resterend",
            "status_scheduled_triggered": "Timer verlopen - {} wordt gestart",
            "status_scheduled_cancelled": "Timer geannuleerd",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Timer actief",
            "close_blocked_text": (
                "<b>Er loopt nog een timer!</b><br><br>"
                "Gepland: {}<br>"
                "Resterend: <b>{}</b><br>"
                "Om: {}<br><br>"
                "Als je nu sluit, wordt de geplande shutdown "
                "<b>niet meer uitgevoerd</b>."
            ),
            "close_blocked_yes": "Toch sluiten",
            "close_blocked_no": "App laten doorlopen",
            "close_blocked_cancel_text": (
                "Er loopt nog een timer.\n\n"
                "Wil je de app echt sluiten?\n"
                "(De geplande shutdown wordt dan verworpen.)"
            ),
            "close_blocked_log_aborted": "Sluiten geannuleerd (timer actief)",
            "close_blocked_log_discarded": (
                "App wordt gesloten ondanks actieve timer – timer verworpen"
            ),
            "close_blocked_log_cancel_aborted": (
                "App sluiten geannuleerd via Annuleren-knop"
            ),
            "duration_day": "dag",
            "duration_days": "dagen",
            "duration_hour": "uur",
            "duration_hours": "uur",
            "duration_minute": "minuut",
            "duration_minutes": "minuten",
            "duration_connector_and": "en",
            "tooltip_pause_timer": "Timer pauzeren / hervatten",
            "tooltip_pause_timer": "Timer pauzeren / hervatten",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Timer gepauzeerd – nog {} seconden",
            "timer_resumed": "Timer hervat",
            "say_timer_paused": "Timer gepauzeerd",
            "say_timer_resumed": "Timer hervat",
            "tooltip_pause_timer": "Timer pauzeren/hervatten",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Spraakuitvoer ingeschakeld",
            "speech_enabled_hint": (
                "Spreekt statusberichten, volume-bevestigingen en timer-info "
                "uit via de macOS-spraakuitvoer. Bij deactivering draait "
                "de app stil."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Voor het geplande afsluiten van de Mac is het "
                "beheerderswachtwoord nodig.\n\n"
                "Het wordt veilig opgeslagen in de macOS-sleutelhanger en "
                "alleen gebruikt bij het afsluiten.\n\n"
                "Nu instellen?"
            ),
            "mac_pw_dialog_title": "Beheerderswachtwoord",
            "mac_pw_dialog_message": (
                "Voor het afsluiten van de Mac is het beheerderswachtwoord "
                "nodig.\n\n"
                "Het wordt veilig opgeslagen in de macOS-sleutelhanger en "
                "alleen gebruikt bij het afsluiten."
            ),
            "mac_pw_wrong_password": (
                "Het wachtwoord is onjuist.\n\n"
                "Probeer het opnieuw."
            ),
            "mac_pw_test_failed": (
                "Fout bij het controleren van het wachtwoord:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "De timer is niet gestart omdat de "
                "wachtwoordinvoer is geannuleerd.\n\n"
                "Zonder wachtwoord kan de Mac niet worden afgesloten."
            ),
            "clear_password_title": "Opgeslagen wachtwoord verwijderen",
            "clear_password_message": (
                "Het in de sleutelhanger opgeslagen beheerderswachtwoord verwijderen?\n\n"
                "Bij de volgende geplande afsluiting wordt het wachtwoord "
                "opnieuw gevraagd."
            ),
            "clear_password_success": "Het wachtwoord is uit de sleutelhanger verwijderd.",
            "clear_password_failed": "Het wachtwoord kon niet worden verwijderd.",
            "clear_password_description": (
                "Verwijdert het in de macOS-sleutelhanger opgeslagen "
                "beheerderswachtwoord. Bij de volgende geplande "
                "afsluiting wordt het opnieuw gevraagd."
            ),
            "clear_password_button": "Opgeslagen wachtwoord verwijderen",
            "shutdown_no_password_message": (
                "De Mac kon niet worden afgesloten.\n\n"
                "Er is noch een NOPASSWD-sudoers-regel noch een opgeslagen "
                "wachtwoord in de sleutelhanger beschikbaar.\n\n"
                "Stel de geplande afsluiting opnieuw in."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Waarschuwing",
            "warning_eject_failed_continue": (
                "Netwerkschijven konden niet correct worden uitgeworpen.\n\n"
                "Als er nog gegevens worden gekopieerd of bestanden open staan, "
                "kan er gegevensverlies optreden.\n\n"
                "Toch doorgaan met afsluiten?"
            ),
            "auto_timer_disabled_no_pw": (
                "Automatisch afsluiten uitgeschakeld – geen beheerderswachtwoord "
                "beschikbaar. Voer het eenmalig in bij de volgende prompt."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Ja",
            "btn_no": "Nee",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Niets afsluiten  (Mac blijft wakker – bijv. voor back-upscripts)",
            "sched_countdown_coffee_label": "⏳ caffeinate actief: nog {} ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Koffie-timer nog actief",
            "coffee_conflict_message": (
                "Er loopt nog een koffie-timer:\n\n"
                "Resterend: {}\n\n"
                "Als je nu afsluit, wordt de koffie-timer geannuleerd "
                "en caffeinate gestopt.\n\n"
                "Toch afsluiten?"
            ),
            "shutdown_timer_conflict_title": "Afsluit-timer nog actief",
            "shutdown_timer_conflict_message": (
                "Er loopt nog een afsluit-timer:\n\n"
                "Gepland: {}\n"
                "Resterend: {}\n\n"
                "Als je nu handmatig afsluit, wordt de timer geannuleerd "
                "en moet opnieuw worden ingesteld.\n\n"
                "Toch afsluiten?"
            ),
            "tooltip_stop_timer": "Timer volledig stoppen",
            "tooltip_stop_timer_inactive": "Geen timer actief",
            "timer_stopped_notice": "⏹ Timer gestopt – klaar voor herstart",
            "say_timer_stopped": "Timer gestopt",
            "say_timer_restarted": "Timer opnieuw gestart",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "NAS-fabrikant:",
            "vendor_tooltip": (
                "Kies je NAS-fabrikant. Bepaalt de afsluitcommando's "
                "en standaardpaden. 'Automatisch detecteren' controleert "
                "de NAS via SSH."
            ),
            "vendor_auto_detect": "🔄 Automatisch detecteren",
            "vendor_auto_detect_tooltip": (
                "Fabrikant automatisch detecteren via SSH. "
                "Voorwaarde: SSH-sleutel en IP zijn correct geconfigureerd."
            ),
            "vendor_detect_in_progress": "🔄 Detecteren...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Algemene Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Aangepast",
            "vendor_custom_hint": (
                "Aangepast: pas de afsluitcommando's handmatig aan. "
                "Standaard: 'sudo shutdown -h now' (werkt op "
                "80 % van alle Linux-NAS'en)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Fabrikant gedetecteerd: {}",
            "vendor_detect_success_question": (
                "Fabrikant gedetecteerd: {}\n\n"
                "Wil je deze fabrikant overnemen?\n"
                "(Huidige waarde: {})"
            ),
            "vendor_detect_failed": (
                "Fabrikant kon niet automatisch worden gedetecteerd.\n\n"
                "Selecteer handmatig. De meeste Linux-NAS'en "
                "werken met 'Algemene Linux'."
            ),
            "vendor_detect_no_ssh": (
                "Automatische detectie vereist SSH-toegang.\n\n"
                "Controleer het volgende:\n"
                "• SSH-sleutelpad is correct\n"
                "• IP-adres is correct\n"
                "• SSH is geactiveerd op de NAS\n"
                "• SSH-sleutel is geïnstalleerd op de NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Voer eerst de SSH-sleutel en het IP-adres in."
            ),
            "vendor_detect_nas_offline": (
                "De NAS-server reageert niet.\n\n"
                "Controleer het volgende:\n"
                "• Is de NAS ingeschakeld?\n"
                "• Is het IP-adres correct?\n"
                "• Bevindt de NAS zich in hetzelfde netwerk?\n\n"
                "Start de NAS op en probeer het opnieuw."
            ),
            "vendor_detect_error": "Fout bij automatische detectie:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH-sleutel niet gevonden:\n\n{}\n\n"
                "Controleer het pad in de instellingen."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Afsluitcommando:",
            "custom_cmd_tooltip": (
                "Het commando dat via SSH naar de NAS wordt verzonden. "
                "Scheid meerdere commando's met een puntkomma."
            ),
            "custom_cmd_hint": (
                "💡 Scheid meerdere commando's met een puntkomma — "
                "het eerste succesvolle commando wordt gebruikt. "
                "Voorbeeld: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Help over afsluitcommando's weergeven",
            "custom_cmd_help_title": "Typische afsluitcommando's",
            "custom_cmd_help_text": (
                "<h3>Typische afsluitcommando's per fabrikant</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (algemeen):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Meerdere commando's (fallback-keten)</h4>"
                "<p>Als het eerste commando mislukt, wordt het volgende "
                "geprobeerd. Scheiding met puntkomma:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Tip:</b> Kies eerst het meest waarschijnlijke commando, "
                "daarna alternatieven als fallback.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Volumes detecteren via SSH...",
            "volumes_detection_via_paths": (
                "🔍 Zoeken in fabrikantspecifieke paden..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Fallback: zoeken via smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Volumes zoeken via SSH... Het zoeken kan "
                "enkele seconden duren."
            ),
            "volumes_detect_panel_success": (
                "{} volumes gevonden — {} nieuw toegevoegd, "
                "{} al aanwezig"
            ),
            "volumes_detect_panel_partial": (
                "{} volumes gevonden — allemaal al in de lijst"
            ),
            "volumes_detect_panel_failed": (
                "Geen volumes gevonden. "
                "Voer de volumes handmatig in."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 MAC-adres detecteren...",
            "mac_detect_success": "✅ MAC-adres gedetecteerd: {}",
            "mac_detect_success_dialog": (
                "MAC-adres succesvol gedetecteerd.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "De waarde is ingevoerd in het MAC-veld."
            ),
            "mac_detect_failed": (
                "⚠ MAC-adres kon niet automatisch worden gedetecteerd. "
                "Er wordt hulp weergegeven."
            ),
            "config_mac_find": "🔍 MAC vinden",
            "config_mac_find_tooltip": (
                "MAC-adres automatisch detecteren. "
                "Als dit mislukt, wordt een handleiding weergegeven."
            ),
        },
        # Norwegisch "🇳🇴 Norsk"
        "no": {
            "language": "Språk:",
            "window_title": "NAS-administrasjon",
            "status_checking": "Sjekker servertilkobling...",
            "status_online": "NAS-server er online ✓",
            "status_offline": "NAS-server er offline",
            "status_settings": "Innstillinger åpnet - Tidtaker stoppet",
            "status_settings_saved": "Innstillinger lagret",
            "status_settings_cancelled": "Innstillinger avbrutt",
            "status_shutdown": "Slår av NAS og Mac...",
            "status_shutdown_nas": "Slår av NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ NAS-nedstenging sendt, Mac slår seg nå av...",
            "status_shutdown_nas_failed_mac_still": "⚠️ NAS-nedstenging mislyktes, slår av Mac likevel...",
            "status_starting": "Starter NAS via Wake-on-LAN...",
            "status_waiting": "Venter på serverstart...",
            "status_wol_sent": "Magic Packet sendt",
            "status_wol_failed": "WOL mislyktes",
            "status_mounting": "Monterer valgte volumer...",
            "status_mounting_volume": "Monterer {}...",
            "status_mounted": "{} montert ✓",
            "status_unmounting": "Kobler ut {}...",
            "status_unmounted": "{} koblet ut ✓",
            "status_error": "Feil: {} kunne ikke monteres",
            "status_error_unmount": "Feil: {} kunne ikke kobles ut",
            "status_all_mounted": "Alle volumer montert ✓",
            "status_all_unmounted": "Alle volumer koblet ut ✓",
            "status_mount_all": "Monterer alle volumer...",
            "status_unmount_all": "Kobler ut alle volumer...",
            "status_shutdown_cmd": "NAS-avslutningskommando sendt ✓",
            "status_timeout": "Tidsavbrudd - Serveren kunne ikke startes",
            "status_no_volumes": "Ingen volumer montert",
            "status_mount_failed": "Montering mislyktes",
            "status_cancelled": "Avbrutt - Appen vil lukkes",
            "status_esc": "ESC trykket - Appen vil lukkes",
            "status_server_online": "Server online - venter på SMB-tjeneste...",
            "status_profile_changed": "Profil endret til: {}",
            "status_switching": "Bytter til profil: {}...",
            "btn_shutdown_both": "Mac og NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Avbryt",
            "btn_start_nas": "Start NAS",
            "btn_settings": "Innstillinger (Cmd+E)",
            "btn_select_all": "Alle",
            "btn_save": "Lagre",
            "btn_reset": "Tilbakestill",
            "btn_info": "ℹ",
            "btn_profile": "Profiler",
            "tooltip_shutdown_both": "Slår av Mac og NAS om 2 min",
            "tooltip_shutdown_nas": "Slår av kun NAS",
            "tooltip_cancel": "Lukker appen",
            "tooltip_start_nas": "Starter NAS via Wake-on-LAN",
            "tooltip_settings": "Innstillinger (Cmd+E)",
            "timer_shutdown": "Automatisk avslutning om {} sekunder - ENTER kun NAS",
            "timer_start": "Automatisk start om {} sekunder - ENTER for umiddelbar start",
            "volumes_title": "Tilgjengelige volumer",
            "volumes_title_offline": "Volumer å montere ved oppstart",
            "volumes_hint": "Merk: Det første volumet i listen blir automatisk behandlet som hovedvolum og kan ikke deaktiveres.",
            "volumes_mount_tooltip": "Vil bli montert automatisk ved serverstart",
            "config_title": "AnyNasPy - Innstillinger",
            "config_tab_profiles": "Serverprofiler",
            "config_tab_general": "Generelt",
            "config_tab_volumes": "Volumer",
            "config_tab_timing": "Tidsinnstillinger",
            "config_language": "Språk:",
            "config_nas_group": "NAS-serverinnstillinger",
            "config_nas_user": "Brukernavn:",
            "config_nas_dns": "DNS-navn:",
            "config_nas_ip": "IP-adresse:",
            "config_nas_mac": "MAC-adresse:",
            "config_ssh_key": "SSH-nøkkelsti:",
            "config_volumes_group": "Volumer",
            "config_volumes_label": "Volumer (ett navn per linje):",
            "config_time_group": "Tidsinnstillinger (sekunder)",
            "config_auto_shutdown": "Forsinkelse automatisk avslutning:",
            "config_auto_start": "Forsinkelse automatisk start:",
            "config_wol_wait": "WOL-ventetid (maks):",
            "config_smb_wait": "SMB-ventetid:",
            "config_mount_retries": "Monteringsforsøk:",
            "config_status_file": "Statusfil",
            "config_json_path": "JSON-konfigurasjonsfil:",
            "config_profile_name": "Profilnavn:",
            "config_profile_active": "Aktiv profil",
            "config_profile_set_active": "Sett som aktiv profil",
            "config_profile_list": "Eksisterende profiler:",
            "config_profile_new": "Ny profil",
            "config_profile_delete": "Slett profil",
            "config_profile_duplicate": "Dupliser profil",
            "config_profile_rename": "Gi nytt navn",
            "config_profile_required": "Profilnavn er påkrevd.",
            "config_profile_exists": "Det finnes allerede en profil med dette navnet.",
            "config_profile_deleted": "Profil '{}' ble slettet.",
            "config_profile_duplicated": "Profil '{}' ble duplisert som '{}'.",
            "config_profile_renamed": "Profilen ble omdøpt til '{}'.",
            "config_profile_activated": "Profil '{}' er nå aktiv.",
            "config_find_ip": "🔍 Finn IP",
            "config_find_ip_tooltip": "Finn automatisk server-IP i nettverket",
            "config_ssh_help": "? Hjelp",
            "config_mac_help": "? Hjelp",
            "config_mac_help_tooltip": "Instruksjoner for å finne MAC-adresse",
            "msg_ip_found": "Server-IP ble funnet:\n\n{}\n\nIP-en er fylt inn i feltet.",
            "msg_ip_not_found": "Kunne ikke finne server-IP automatisk.\n\nVennligst angi IP-adressen manuelt.\n\nTips:\n• Sjekk DNS-navnet i innstillingene\n• Sørg for at NAS-en er påslått\n• Finn IP-en i DSM-grensesnittet under 'System > Nettverk'",
            "msg_reset_confirm": "Tilbakestill alle innstillinger til standardverdier?",
            "msg_reset_title": "Tilbakestill",
            "msg_reset_done": "Alle innstillinger er tilbakestilt til standardverdier.",
            "msg_delete_confirm": "Vil du virkelig slette profil '{}'?",
            "msg_delete_title": "Slett profil",
            "msg_no_active_profile": "Ingen aktiv profil valgt.",
            "info_title": "Om AnyNasPy",
            "info_version": "Versjon",
            "info_copyright": "Opphavsrett",
            "info_license": "Lisens",
            "info_impressum": "Impressum",
            "info_developer": "Utvikler",
            "info_contact": "Kontakt",
            "info_license_text": "MIT-lisens",
            "say_timer_shutdown": "Automatisk avslutning av Mac og NAS om {} sekunder - Enter kun NAS - Escape for å avbryte",
            "say_timer_start": "NAS-serveren starter om {} sekunder - Enter for umiddelbar start",
            "say_server_online": "NAS-serveren er tilgjengelig",
            "say_server_offline": "NAS-serveren er offline",
            "say_shutdown_started": "Avslutning startet",
            "say_nas_shutdown": "NAS slås av",
            "say_starting_nas": "Starter NAS",
            "say_cancelled": "Avbrutt",
            "say_waiting_server": "Venter på serverstart",
            "say_wol_failed": "Feil ved sending",
            "say_server_reachable": "Server tilgjengelig",
            "say_mount_volume": "{} klar",
            "say_unmount_volume": "Kobler ut {}",
            "say_mount_all": "Monterer alle volumer",
            "say_unmount_all": "Kobler ut alle volumer",
            "say_mount_error": "Feil ved montering",
            "say_unmount_error": "Feil ved utkobling",
            "say_mount_failed": "Ingen volumer montert",
            "say_settings_opened": "Innstillinger åpnet",
            "say_settings_saved": "Innstillinger lagret",
            "say_settings_cancelled": "Innstillinger avbrutt",
            "say_workaround_deleted": "Workaround-fil slettet",
            "say_server_timeout": "Server-start tidsavbrudd",
            "say_profile_changed": "Profil endret til {}",
            "ssh_key_create_title": "Opprett SSH-nøkkel",
            "ssh_key_create_question": "Vil du opprette et nytt SSH-nøkkelpar?",
            "ssh_key_create_existing": "SSH-nøkkel '{}' finnes allerede.\nVil du overskrive den?",
            "ssh_key_create_comment": "Kommentar for SSH-nøkkelen (valgfritt):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH-nøkkel opprettet: {}",
            "ssh_key_create_error": "Feil ved opprettelse av SSH-nøkkel",
            "ssh_key_create_timeout": "Tidsavbrudd ved opprettelse av SSH-nøkkel",
            "ssh_key_create_failed": "ssh-keygen returnerte en feil:\n{}",
            "ssh_key_create_passphrase": "Passfrase for SSH-nøkkel (la stå tom for ingen):",
            "ssh_key_create_passphrase_confirm": "Bekreft passfrase:",
            "ssh_key_create_passphrase_mismatch": "Passfrasene stemmer ikke overens.",
            "ssh_key_create_info": "✅ SSH-nøkkelpar opprettet:\n\n"
            "📁 Privat Nøkkel: {}\n"
            "📁 Offentlig Nøkkel: {}\n\n"
            "📋 Offentlig Nøkkel å kopiere:\n"
            "{}\n\n"
            "🔑 Slik installerer du nøkkelen på NAS-en din:\n"
            "1. Kopier den offentlige nøkkelen (ovenfor)\n"
            "2. Legg den til i filen:\n"
            "   ~/.ssh/authorized_keys på NAS-en\n"
            "3. Eller bruk:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Vennligst skriv inn et annet filnavn:",
            "ssh_key_exists_also": "Nøkkelen '{}' finnes også.\nVennligst slett den først eller velg et annet navn.",
            "ssh_key_passphrase_title": "Passfrase",
            "ssh_key_passphrase_question": "Vil du bruke en passfrase for SSH-nøkkelen?\n\nUten passfrase: Automatisk tilkobling mulig, mindre sikker.\nMed passfrase: Sikrere, men spør ved hver tilkobling.",
            "ssh_key_passphrase_enter": "Skriv inn passfrase",
            "ssh_key_passphrase_label": "Passfrase for SSH-nøkkel (minst 4 tegn):",
            "ssh_key_passphrase_none": "Ingen passfrase",
            "ssh_key_passphrase_none_question": "Du har ikke skrevet inn en passfrase.\nVil du opprette nøkkelen uten passfrase?",
            "ssh_key_passphrase_short": "Passfrase for kort",
            "ssh_key_passphrase_short_message": "Passfrasen må være minst 4 tegn lang.",
            "ssh_key_passphrase_confirm": "Bekreft passfrase",
            "ssh_key_passphrase_confirm_label": "Skriv inn passfrase på nytt:",
            "ssh_key_passphrase_mismatch_title": "Passfrase feil",
            "ssh_key_passphrase_mismatch_message": "Passfrasene stemmer ikke overens.",
            "config_ssh_open": "Åpne",
            "config_ssh_open_tooltip": "Velg SSH-nøkkel eller åpne mappe",
            "config_ssh_create": "Opprett",
            "config_ssh_create_tooltip": "Opprett nytt SSH-nøkkelpar",
            "config_ssh_help_tooltip": "Vis SSH-nøkkel hjelp",
            "config_ssh_select": "Velg SSH-nøkkel",
            "config_json_open": "Åpne",
            "config_json_open_tooltip": "Åpne JSON-konfigurasjonsmappe",
            "config_error": "Feil",
            "config_shutdown_mac_delay": "Forsinkelse mellom NAS- og Mac-nedstenging:",
            "info_third_party": "Tredjepartsbiblioteker",
            "info_pyqt5_license": "Denne applikasjonen bruker PyQt5, som er lisensiert under GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nDen fullstendige lisensteksten finner du på https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Oppdag volumer",
            "volumes_add": "Legg til",
            "volumes_delete": "Slett",
            "volumes_move_up": "Flytt opp",
            "volumes_move_down": "Flytt ned",
            "volumes_available": "Tilgjengelige volumer:",
            "volumes_no_volumes": "Ingen volumer funnet.",
            "volumes_detection_failed": "Feil ved oppdagelse av volumer.",
            "volumes_detection_success": "Volumer oppdaget vellykket.",
            "volumes_confirm_delete": "Slett virkelig volum '{}'?",
            "volumes_enter_name": "Vennligst skriv inn navnet på det nye volumet:",
            "volumes_name_exists": "Et volum med dette navnet finnes allerede.",
            "msg_invalid_ip": "Den angitte IP-adressen er ugyldig.\nVennligst angi en gyldig IPv4-adresse (f.eks. 192.168.1.100).",
            "msg_select_volume": "Vennligst velg et volum.",
            "msg_cannot_delete_main_volume": "Det første volumet (hovedvolum) kan ikke slettes.",
            "profile_cannot_delete_last": "Den siste profilen kan ikke slettes.",
            "status_wol_sending": "Sender magisk pakke...",
            "status_wol_method_failed": "Python-metoden mislyktes, prøver neste...",
            "status_trying_wakeonlan": "Prøver wakeonlan...",
            "status_trying_etherwake": "Prøver etherwake...",
            "ssh_key_system_key_warning": "Sikkerhetsadvarsel",
            "ssh_key_system_key_message": "Navnet '{}' er en systemnøkkel og vil ikke bli overskrevet.\nVennligst velg et annet navn (f.eks. synaspy_rsa).",
            "profile_name_exists": "En profil med navnet '{}' finnes allerede.",
            "config_profile_created": "Profilen '{}' ble opprettet.",
            "config_profile_create_failed": "Kunne ikke opprette profilen.",
            "config_profile_rename_failed": "Omdøping mislyktes.",
            "config_profile_duplicate_name": "Navn for den dupliserte profilen:",
            "config_profile_duplicate_failed": "Duplisering mislyktes.",
            "config_profile_delete_failed": "Sletting mislyktes.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Slår av kun Macen (NAS forblir på, ingen WOL)",
            "status_shutdown_mac_only": "Slår av kun Macen...",
            "say_shutdown_mac_only": "Macen slås av, NAS forblir på",

            "btn_scheduled_shutdown": "🕐 Planlagt avslåing",
            "tooltip_scheduled_shutdown": "Slår av etter en brukervalg tid",
            "btn_scheduled_shutdown_offline": "🕐 Planlagt avslåing av Mac",
            "tooltip_scheduled_shutdown_offline": "Slår av kun Macen etter en valgt tid (NAS er offline)",
            "btn_cancel_scheduled": "⏹ Avbryt nedtelling",
            "tooltip_cancel_scheduled": "Avbryter den aktive nedtellingen",

            "sched_dialog_title": "Planlagt avslåing",
            "sched_target_label": "Mål:",
            "sched_target_both": "🖥️ Mac + NAS  (fullstendig avslåing)",
            "sched_target_nas": "🗄️ Kun NAS  (Mac forblir på)",
            "sched_target_mac": "💻 Kun Mac  (NAS forblir på)",

            "sched_wait_label": "Ventetid til avslåing:",
            "sched_hours": "Timer",
            "sched_minutes": "Minutter",

            "sched_caffeinate_label": "caffeinate-alternativ (holder Macen våken):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Anbefalt: Systemet våkent, skjermen kan dimmes  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Hindre kun inaktivitet og disk (skjermen forblir på)  (-i -m)",
            "sched_caffeinate_d": "Skjermen forblir i tillegg på  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simuler brukeraktivitet (skjermen lys, systemet våkent)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maksimum: Skjerm + system + disk permanent våkne  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Av (normal strømsparing – systemet kan sove)",

            "sched_caffeinate_hint": (
                "💡 Læringsfakta: Bruk caffeinate-flagg direkte i terminalen:\n"
                "   -i  forhindrer inaktiv søvn i systemet\n"
                "   -m  forhindrer disksøvn (harddisken sover ikke)\n"
                "   -s  forhindrer systemsøvn (kun på strømadapter)\n"
                "   -d  forhindrer skjermsøvn (skjermen forblir på)\n"
                "   -u  simulerer brukeraktivitet (skjermen forblir lys)\n"
                "   -w PID  avslutter caffeinate når prosessen PID avsluttes\n"
                "Eksempel:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Avslåing planlagt for: {}",
            "sched_countdown_label": "Nedtelling: {} til avslåing ({})",
            "sched_started": "Tidsur startet.\n\nMål: {}\nVarighet: {}\nSlutt: {}",
            "sched_cancelled": "Tidsur avbrutt",
            "sched_already_active": "Et tidsur kjører allerede. Avbryte først?",
            "sched_invalid_time": "Vennligst oppgi en gyldig tid (minst 1 minutt).",
            "sched_max_time": "Maksimalt 720 timer (30 dager) tillatt.",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Tidsur startet. Macen og NAS vil slås av om {}."
            ),
            "sched_voice_started_nas": (
                "Tidsur startet. Kun NAS vil slås av om {}. "
                "Macen forblir på."
            ),
            "sched_voice_started_mac": (
                "Tidsur startet. Kun Macen vil slås av om {}. "
                "NAS forblir på."
            ),
            "sched_voice_started_nothing": (
                "Tidsur startet. Ingenting vil bli utført når det utløper. "
                "caffeinate forblir aktivt til da."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Macen forblir våken i {}. "
                "Skjermen kan dimmes. "
                "Ingenting vil bli utført når det utløper."
            ),
            "sched_voice_nothing_im": (
                "Macen forblir våken i {}. "
                "Skjermen forblir på. "
                "Ingenting vil bli utført når det utløper."
            ),
            "sched_voice_nothing_d": (
                "Macen og skjermen forblir på i {}. "
                "Ingenting vil bli utført når det utløper."
            ),
            "sched_voice_nothing_u": (
                "Macen forblir aktiv i {}. "
                "Skjermen forblir lys. "
                "Ingenting vil bli utført når det utløper."
            ),
            "sched_voice_nothing_full": (
                "Macen forblir fullt aktiv i {} – skjerm og system kontinuerlig våkne. "
                "Ingenting vil bli utført når det utløper."
            ),
            "sched_voice_nothing_off": (
                "Tidsuret kjører i {}. "
                "Ingenting vil bli utført når det utløper. "
                "Advarsel: Macen kan gå i dvale."
            ),
            "sched_voice_cancelled": "Tidsur avbrutt",
            "sched_caffeinate_failed": "caffeinate kunne ikke startes:\n{}",
            "sched_target_required": "Vennligst velg et mål.",
            "sched_tooltip_active": "Tidsur kjører – klikk for å avbryte",

            "status_scheduled_active": "Tidsur aktivt - {} gjenstår",
            "status_scheduled_triggered": "Tidsur utløpt - starter {}",
            "status_scheduled_cancelled": "Tidsur avbrutt",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Tidsur aktivt",
            "close_blocked_text": (
                "<b>Et tidsur kjører fortsatt!</b><br><br>"
                "Planlagt: {}<br>"
                "Gjenstår: <b>{}</b><br>"
                "Kl.: {}<br><br>"
                "Hvis du lukker nå, vil den planlagte avslåingen "
                "<b>ikke lenger bli utført</b>."
            ),
            "close_blocked_yes": "Lukk likevel",
            "close_blocked_no": "La appen fortsette",
            "close_blocked_cancel_text": (
                "Et tidsur kjører fortsatt.\n\n"
                "Vil du virkelig lukke appen?\n"
                "(Den planlagte avslåingen blir da forkastet.)"
            ),
            "close_blocked_log_aborted": "Lukking avbrutt (tidsur aktivt)",
            "close_blocked_log_discarded": (
                "Appen lukkes til tross for aktivt tidsur – tidsur forkastet"
            ),
            "close_blocked_log_cancel_aborted": (
                "App-lukking avbrutt via Avbryt-knappen"
            ),
            "duration_day": "dag",
            "duration_days": "dager",
            "duration_hour": "time",
            "duration_hours": "timer",
            "duration_minute": "minutt",
            "duration_minutes": "minutter",
            "duration_connector_and": "og",
            "tooltip_pause_timer": "Pause / gjenoppta tidtaker",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Tidtaker satt på pause – {} sekunder gjenstår",
            "timer_resumed": "Tidtaker gjenopptatt",
            "say_timer_paused": "Tidtaker satt på pause",
            "say_timer_resumed": "Tidtaker gjenopptatt",
            "tooltip_pause_timer": "Pause/gjenoppta tidtaker",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Taleutgang aktivert",
            "speech_enabled_hint": (
                "Leser opp statusmeldinger, volumbekreftelser og "
                "tidtakerinformasjon via macOS taleutgang. Når deaktivert "
                "kjører appen stille."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "For planlagt avslutning av Macen kreves "
                "administratorpassordet.\n\n"
                "Det lagres sikkert i macOS-nøkkelringen og brukes bare "
                "ved avslutning.\n\n"
                "Sette opp nå?"
            ),
            "mac_pw_dialog_title": "Administratorpassord",
            "mac_pw_dialog_message": (
                "For avslutning av Macen kreves administratorpassordet.\n\n"
                "Det lagres sikkert i macOS-nøkkelringen og brukes bare "
                "ved avslutning."
            ),
            "mac_pw_wrong_password": (
                "Passordet er feil.\n\n"
                "Prøv igjen."
            ),
            "mac_pw_test_failed": (
                "Feil ved passordkontroll:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Tidtakeren ble ikke startet fordi "
                "passordinntastingen ble avbrutt.\n\n"
                "Uten passord kan ikke Macen slås av."
            ),
            "clear_password_title": "Slett lagret passord",
            "clear_password_message": (
                "Slette administratorpassordet som er lagret i nøkkelringen?\n\n"
                "Ved neste planlagte avslutning vil passordet "
                "bli spurt om på nytt."
            ),
            "clear_password_success": "Passordet ble fjernet fra nøkkelringen.",
            "clear_password_failed": "Passordet kunne ikke slettes.",
            "clear_password_description": (
                "Fjerner administratorpassordet som er lagret i "
                "macOS-nøkkelringen. Ved neste planlagte avslutning "
                "vil det bli spurt om på nytt."
            ),
            "clear_password_button": "Slett lagret passord",
            "shutdown_no_password_message": (
                "Macen kunne ikke slås av.\n\n"
                "Verken en NOPASSWD-sudoers-regel eller et lagret "
                "passord i nøkkelringen er tilgjengelig.\n\n"
                "Sett opp den planlagte avslutningen på nytt."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Advarsel",
            "warning_eject_failed_continue": (
                "Nettverksstasjoner kunne ikke løses ut på riktig måte.\n\n"
                "Hvis data fortsatt kopieres eller filer er åpne, "
                "kan det oppstå datatap.\n\n"
                "Fortsette med avslutning likevel?"
            ),
            "auto_timer_disabled_no_pw": (
                "Automatisk avslutning deaktivert – ingen administratorpassord "
                "tilgjengelig. Vennligst skriv det inn én gang ved neste forespørsel."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Ja",
            "btn_no": "Nei",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Ikke slå av noe  (Macen holder seg våken – f.eks. for sikkerhetskopiskript)",
            "sched_countdown_coffee_label": "⏳ caffeinate aktiv: {} gjenstår ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Kaffe-tidtakeren er fortsatt aktiv",
            "coffee_conflict_message": (
                "En kaffe-tidtaker kjører fortsatt:\n\n"
                "Gjenstår: {}\n\n"
                "Hvis du slår av nå, avbrytes kaffe-tidtakeren "
                "og caffeinate stoppes.\n\n"
                "Slå av likevel?"
            ),
            "shutdown_timer_conflict_title": "Avslutningstidtaker er fortsatt aktiv",
            "shutdown_timer_conflict_message": (
                "En avslutningstidtaker kjører fortsatt:\n\n"
                "Planlagt: {}\n"
                "Gjenstår: {}\n\n"
                "Hvis du slår av manuelt nå, avbrytes tidtakeren "
                "og må planlegges på nytt.\n\n"
                "Slå av likevel?"
            ),
            "tooltip_stop_timer": "Stopp tidtakeren helt",
            "tooltip_stop_timer_inactive": "Ingen tidtaker aktiv",
            "timer_stopped_notice": "⏹ Tidtakeren stoppet – klar for omstart",
            "say_timer_stopped": "Tidtakeren stoppet",
            "say_timer_restarted": "Tidtakeren startet på nytt",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "NAS-produsent:",
            "vendor_tooltip": (
                "Velg NAS-produsenten din. Bestemmer avslutningskommandoene "
                "og standardbanene. 'Automatisk gjenkjenning' sjekker "
                "NAS-en via SSH."
            ),
            "vendor_auto_detect": "🔄 Automatisk gjenkjenning",
            "vendor_auto_detect_tooltip": (
                "Gjenkjenn produsenten automatisk via SSH. "
                "Forutsetning: SSH-nøkkel og IP er riktig konfigurert."
            ),
            "vendor_detect_in_progress": "🔄 Gjenkjenner...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Generisk Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Egendefinert",
            "vendor_custom_hint": (
                "Egendefinert: Tilpass avslutningskommandoene manuelt. "
                "Standard: 'sudo shutdown -h now' (fungerer på "
                "80 % av alle Linux-NAS-er)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Produsent gjenkjent: {}",
            "vendor_detect_success_question": (
                "Produsent gjenkjent: {}\n\n"
                "Vil du bruke denne produsenten?\n"
                "(Nåværende verdi: {})"
            ),
            "vendor_detect_failed": (
                "Produsenten kunne ikke gjenkjennes automatisk.\n\n"
                "Velg manuelt. De fleste Linux-NAS-er "
                "fungerer med 'Generisk Linux'."
            ),
            "vendor_detect_no_ssh": (
                "Automatisk gjenkjenning krever SSH-tilgang.\n\n"
                "Sjekk følgende:\n"
                "• SSH-nøkkelbanen er riktig\n"
                "• IP-adressen er riktig\n"
                "• SSH er aktivert på NAS-en\n"
                "• SSH-nøkkelen er installert på NAS-en "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Skriv inn SSH-nøkkel og IP-adresse først."
            ),
            "vendor_detect_nas_offline": (
                "NAS-serveren svarer ikke.\n\n"
                "Sjekk følgende:\n"
                "• Er NAS-en slått på?\n"
                "• Er IP-adressen riktig?\n"
                "• Er NAS-en på samme nettverk?\n\n"
                "Slå på NAS-en og prøv igjen."
            ),
            "vendor_detect_error": "Feil under automatisk gjenkjenning:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH-nøkkel ikke funnet:\n\n{}\n\n"
                "Sjekk banen i innstillingene."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Avslutningskommando:",
            "custom_cmd_tooltip": (
                "Kommandoen som sendes til NAS-en via SSH. "
                "Skill flere kommandoer med semikolon."
            ),
            "custom_cmd_hint": (
                "💡 Skill flere kommandoer med semikolon — "
                "den første vellykkede brukes. "
                "Eksempel: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Vis hjelp om avslutningskommandoer",
            "custom_cmd_help_title": "Typiske avslutningskommandoer",
            "custom_cmd_help_text": (
                "<h3>Typiske avslutningskommandoer per produsent</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (generisk):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Flere kommandoer (reservekjede)</h4>"
                "<p>Hvis den første kommandoen mislykkes, prøves den neste. "
                "Skille med semikolon:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Tips:</b> Velg den mest sannsynlige kommandoen først, "
                "deretter alternativer som reserve.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Gjenkjenner volumer via SSH...",
            "volumes_detection_via_paths": (
                "🔍 Søker i produsentspesifikke baner..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Reserve: Søker via smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Søker etter volumer via SSH... Søket kan "
                "ta noen sekunder."
            ),
            "volumes_detect_panel_success": (
                "{} volumer funnet — {} nye lagt til, "
                "{} allerede til stede"
            ),
            "volumes_detect_panel_partial": (
                "{} volumer funnet — alle allerede i listen"
            ),
            "volumes_detect_panel_failed": (
                "Ingen volumer funnet. "
                "Skriv inn volumene manuelt."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Gjenkjenner MAC-adresse...",
            "mac_detect_success": "✅ MAC-adresse gjenkjent: {}",
            "mac_detect_success_dialog": (
                "MAC-adressen ble gjenkjent.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Verdien ble satt inn i MAC-feltet."
            ),
            "mac_detect_failed": (
                "⚠ MAC-adressen kunne ikke gjenkjennes automatisk. "
                "Hjelp vises."
            ),
            "config_mac_find": "🔍 Finn MAC",
            "config_mac_find_tooltip": (
                "Gjenkjenn MAC-adressen automatisk. "
                "Hvis det mislykkes, vises en veiledning."
            ),
        },
        # "🇵🇱 Polnisch"
        "pl": {
            "language": "Język:",
            "window_title": "Zarządzanie NAS",
            "status_checking": "Sprawdzanie połączenia z serwerem...",
            "status_online": "Serwer NAS jest online ✓",
            "status_offline": "Serwer NAS jest offline",
            "status_settings": "Otworzono ustawienia - Zatrzymano timer",
            "status_settings_saved": "Zapisano ustawienia",
            "status_settings_cancelled": "Anulowano ustawienia",
            "status_shutdown": "Wyłączanie NAS i Mac...",
            "status_shutdown_nas": "Wyłączanie NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Wysłano polecenie wyłączenia NAS, Mac zostanie teraz wyłączony...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Nie udało się wyłączyć NAS, wyłączanie Mac...",
            "status_starting": "Uruchamianie NAS przez Wake-on-LAN...",
            "status_waiting": "Oczekiwanie na uruchomienie serwera...",
            "status_wol_sent": "Wysłano Magic Packet",
            "status_wol_failed": "Nie udało się WOL",
            "status_mounting": "Montowanie wybranych woluminów...",
            "status_mounting_volume": "Montowanie {}...",
            "status_mounted": "{} zamontowany ✓",
            "status_unmounting": "Odmontowywanie {}...",
            "status_unmounted": "{} odmontowany ✓",
            "status_error": "Błąd: Nie można zamontować {}",
            "status_error_unmount": "Błąd: Nie można odmontować {}",
            "status_all_mounted": "Wszystkie woluminy zamontowane ✓",
            "status_all_unmounted": "Wszystkie woluminy odmontowane ✓",
            "status_mount_all": "Montowanie wszystkich woluminów...",
            "status_unmount_all": "Odmontowywanie wszystkich woluminów...",
            "status_shutdown_cmd": "Wysłano polecenie wyłączenia NAS ✓",
            "status_timeout": "Limit czasu - Nie można uruchomić serwera",
            "status_no_volumes": "Brak zamontowanych woluminów",
            "status_mount_failed": "Nie udało się zamontować",
            "status_cancelled": "Anulowano - Zamykanie aplikacji",
            "status_esc": "Naciśnięto ESC - Zamykanie aplikacji",
            "status_server_online": "Serwer online - oczekiwanie na usługę SMB...",
            "status_profile_changed": "Zmieniono profil na: {}",
            "status_switching": "Przełączanie na profil: {}...",
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Anuluj",
            "btn_start_nas": "Uruchom NAS",
            "btn_settings": "Ustawienia (Cmd+E)",
            "btn_select_all": "Wszystkie",
            "btn_save": "Zapisz",
            "btn_reset": "Resetuj",
            "btn_info": "ℹ",
            "btn_profile": "Profile",
            "tooltip_shutdown_both": "Wyłącza Mac i NAS za 2 minuty",
            "tooltip_shutdown_nas": "Wyłącza tylko NAS",
            "tooltip_cancel": "Zamyka aplikację",
            "tooltip_start_nas": "Uruchamia NAS przez Wake-on-LAN",
            "tooltip_settings": "Ustawienia (Cmd+E)",
            "timer_shutdown": "Automatyczne wyłączenie za {} sekund - ENTER dla tylko NAS",
            "timer_start": "Automatyczne uruchomienie za {} sekund - ENTER dla natychmiastowego uruchomienia",
            "volumes_title": "Dostępne woluminy",
            "volumes_title_offline": "Montuj woluminy przy starcie",
            "volumes_hint": "Uwaga: Pierwszy wolumin na liście jest automatycznie traktowany jako główny i nie można go wyłączyć.",
            "volumes_mount_tooltip": "Montowany automatycznie przy starcie serwera",
            "config_title": "AnyNasPy - Ustawienia",
            "config_tab_profiles": "Profile serwera",
            "config_tab_general": "Ogólne",
            "config_tab_volumes": "Woluminy",
            "config_tab_timing": "Ustawienia czasowe",
            "config_language": "Język:",
            "config_nas_group": "Ustawienia serwera NAS",
            "config_nas_user": "Nazwa użytkownika:",
            "config_nas_dns": "Nazwa DNS:",
            "config_nas_ip": "Adres IP:",
            "config_nas_mac": "Adres MAC:",
            "config_ssh_key": "Ścieżka klucza SSH:",
            "config_volumes_group": "Woluminy",
            "config_volumes_label": "Woluminy (jedna nazwa na linię):",
            "config_time_group": "Ustawienia czasowe (sekundy)",
            "config_auto_shutdown": "Opóźnienie automatycznego wyłączenia:",
            "config_auto_start": "Opóźnienie automatycznego uruchomienia:",
            "config_wol_wait": "Czas oczekiwania WOL (max):",
            "config_smb_wait": "Czas oczekiwania SMB:",
            "config_mount_retries": "Liczba prób montowania:",
            "config_status_file": "Plik stanu",
            "config_json_path": "Plik konfiguracyjny JSON:",
            "config_profile_name": "Nazwa profilu:",
            "config_profile_active": "Aktywny profil",
            "config_profile_set_active": "Ustaw jako aktywny profil",
            "config_profile_list": "Istniejące profile:",
            "config_profile_new": "Nowy profil",
            "config_profile_delete": "Usuń profil",
            "config_profile_duplicate": "Duplikuj profil",
            "config_profile_rename": "Zmień nazwę",
            "config_profile_required": "Nazwa profilu jest wymagana.",
            "config_profile_exists": "Profil o tej nazwie już istnieje.",
            "config_profile_deleted": "Profil '{}' został usunięty.",
            "config_profile_duplicated": "Profil '{}' został zduplikowany jako '{}'.",
            "config_profile_renamed": "Profil został zmieniony na '{}'.",
            "config_profile_activated": "Profil '{}' jest teraz aktywny.",
            "config_find_ip": "🔍 Znajdź IP",
            "config_find_ip_tooltip": "Automatyczne wyszukanie IP serwera w sieci",
            "config_ssh_help": "? Pomoc",
            "config_mac_help": "? Pomoc",
            "config_mac_help_tooltip": "Instrukcje dotyczące znajdowania adresu MAC",
            "msg_ip_found": "Adres IP serwera został pomyślnie znaleziony:\n\n{}\n\nIP zostało wpisane w polu.",
            "msg_ip_not_found": "Nie można automatycznie znaleźć adresu IP serwera.\n\nProszę wprowadzić adres IP ręcznie.\n\nWskazówki:\n• Sprawdź nazwę DNS w ustawieniach\n• Upewnij się, że NAS jest włączony\n• Znajdź IP w interfejsie DSM w sekcji 'System > Sieć'",
            "msg_reset_confirm": "Przywrócić wszystkie ustawienia do wartości domyślnych?",
            "msg_reset_title": "Resetuj",
            "msg_reset_done": "Wszystkie ustawienia zostały przywrócone do wartości domyślnych.",
            "msg_delete_confirm": "Czy na pewno usunąć profil '{}'?",
            "msg_delete_title": "Usuń profil",
            "msg_no_active_profile": "Nie wybrano aktywnego profilu.",
            "info_title": "O AnyNasPy",
            "info_version": "Wersja",
            "info_copyright": "Prawa autorskie",
            "info_license": "Licencja",
            "info_impressum": "Impressum",
            "info_developer": "Programista",
            "info_contact": "Kontakt",
            "info_license_text": "Licencja MIT",
            "say_timer_shutdown": "Automatyczne wyłączenie Mac i NAS za {} sekund - Enter dla tylko NAS - Escape aby anulować",
            "say_timer_start": "Serwer NAS zostanie uruchomiony za {} sekund - Enter aby uruchomić natychmiast",
            "say_server_online": "Serwer NAS jest dostępny",
            "say_server_offline": "Serwer NAS jest offline",
            "say_shutdown_started": "Rozpoczęto wyłączanie",
            "say_nas_shutdown": "NAS jest wyłączany",
            "say_starting_nas": "Uruchamianie NAS",
            "say_cancelled": "Anulowano",
            "say_waiting_server": "Oczekiwanie na uruchomienie serwera",
            "say_wol_failed": "Błąd podczas wysyłania",
            "say_server_reachable": "Serwer jest dostępny",
            "say_mount_volume": "{} gotowy",
            "say_unmount_volume": "Odmontowywanie {}",
            "say_mount_all": "Montowanie wszystkich woluminów",
            "say_unmount_all": "Odmontowywanie wszystkich woluminów",
            "say_mount_error": "Błąd montowania",
            "say_unmount_error": "Błąd odmontowywania",
            "say_mount_failed": "Nie zamontowano żadnych woluminów",
            "say_settings_opened": "Otworzono ustawienia",
            "say_settings_saved": "Zapisano ustawienia",
            "say_settings_cancelled": "Anulowano ustawienia",
            "say_workaround_deleted": "Plik obejścia usunięty",
            "say_server_timeout": "Przekroczono czas uruchamiania serwera",
            "say_profile_changed": "Zmieniono profil na {}",
            "ssh_key_create_title": "Tworzenie klucza SSH",
            "ssh_key_create_question": "Czy chcesz utworzyć nową parę kluczy SSH?",
            "ssh_key_create_existing": "Klucz SSH '{}' już istnieje.\nCzy chcesz go zastąpić?",
            "ssh_key_create_comment": "Komentarz do klucza SSH (opcjonalny):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "Utworzono klucz SSH: {}",
            "ssh_key_create_error": "Błąd podczas tworzenia klucza SSH",
            "ssh_key_create_timeout": "Przekroczono czas tworzenia klucza",
            "ssh_key_create_failed": "ssh-keygen zwrócił błąd:\n{}",
            "ssh_key_create_passphrase": "Hasło dla klucza SSH (pozostaw puste dla braku hasła):",
            "ssh_key_create_passphrase_confirm": "Potwierdź hasło:",
            "ssh_key_create_passphrase_mismatch": "Hasła nie są zgodne.",
            "ssh_key_create_info": "✅ Para kluczy SSH została pomyślnie utworzona:\n\n"
            "📁 Klucz prywatny: {}\n"
            "📁 Klucz publiczny: {}\n\n"
            "📋 Klucz publiczny do skopiowania:\n"
            "{}\n\n"
            "🔑 Jak zainstalować klucz na NAS:\n"
            "1. Skopiuj klucz publiczny (powyżej)\n"
            "2. Wklej go do pliku:\n"
            "   ~/.ssh/authorized_keys na NAS\n"
            "3. Lub użyj:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Proszę podać inną nazwę pliku:",
            "ssh_key_exists_also": "Klucz '{}' również istnieje.\nProszę go najpierw usunąć lub wybrać inną nazwę.",
            "ssh_key_passphrase_title": "Hasło",
            "ssh_key_passphrase_question": "Czy chcesz użyć hasła dla klucza SSH?\n\nBez hasła: Możliwe automatyczne połączenie, mniej bezpieczne.\nZ hasłem: Bezpieczniejsze, ale wymaga podania przy każdym połączeniu.",
            "ssh_key_passphrase_enter": "Wprowadź hasło",
            "ssh_key_passphrase_label": "Hasło dla klucza SSH (co najmniej 4 znaki):",
            "ssh_key_passphrase_none": "Bez hasła",
            "ssh_key_passphrase_none_question": "Nie wprowadziłeś hasła.\nCzy chcesz utworzyć klucz bez hasła?",
            "ssh_key_passphrase_short": "Hasło jest za krótkie",
            "ssh_key_passphrase_short_message": "Hasło musi mieć co najmniej 4 znaki.",
            "ssh_key_passphrase_confirm": "Potwierdź hasło",
            "ssh_key_passphrase_confirm_label": "Wprowadź hasło ponownie:",
            "ssh_key_passphrase_mismatch_title": "Błąd hasła",
            "ssh_key_passphrase_mismatch_message": "Hasła nie są zgodne.",
            "config_ssh_open": "Otwórz",
            "config_ssh_open_tooltip": "Wybierz klucz SSH lub otwórz folder",
            "config_ssh_create": "Utwórz",
            "config_ssh_create_tooltip": "Utwórz nową parę kluczy SSH",
            "config_ssh_help_tooltip": "Pokaż pomoc dotyczącą klucza SSH",
            "config_ssh_select": "Wybierz klucz SSH",
            "config_json_open": "Otwórz",
            "config_json_open_tooltip": "Otwórz folder konfiguracyjny JSON",
            "config_error": "Błąd",
            "config_shutdown_mac_delay": "Czas oczekiwania między wyłączeniem NAS a Mac:",
            "info_third_party": "Biblioteki zewnętrzne",
            "info_pyqt5_license": "Ta aplikacja używa PyQt5, który jest licencjonowany na warunkach GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nPełny tekst licencji można znaleźć pod adresem https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Wykryj woluminy",
            "volumes_add": "Dodaj",
            "volumes_delete": "Usuń",
            "volumes_move_up": "Przenieś w górę",
            "volumes_move_down": "Przenieś w dół",
            "volumes_available": "Dostępne woluminy:",
            "volumes_no_volumes": "Nie znaleziono woluminów.",
            "volumes_detection_failed": "Błąd wykrywania woluminów.",
            "volumes_detection_success": "Woluminy wykryte pomyślnie.",
            "volumes_confirm_delete": "Czy na pewno usunąć wolumin '{}'?",
            "volumes_enter_name": "Wprowadź nazwę nowego woluminu:",
            "volumes_name_exists": "Wolumin o tej nazwie już istnieje.",
            "msg_invalid_ip": "Wprowadzony adres IP jest nieprawidłowy.\nWprowadź poprawny adres IPv4 (np. 192.168.1.100).",
            "msg_select_volume": "Wybierz wolumin.",
            "msg_cannot_delete_main_volume": "Pierwszy wolumin (główny) nie może zostać usunięty.",
            "profile_cannot_delete_last": "Ostatni profil nie może zostać usunięty.",
            "status_wol_sending": "Wysyłanie magicznego pakietu...",
            "status_wol_method_failed": "Metoda Python nie powiodła się, próba następnej...",
            "status_trying_wakeonlan": "Próba wakeonlan...",
            "status_trying_etherwake": "Próba etherwake...",
            "ssh_key_system_key_warning": "Ostrzeżenie bezpieczeństwa",
            "ssh_key_system_key_message": "Nazwa '{}' jest kluczem systemowym i nie zostanie nadpisana.\nWybierz inną nazwę (np. synaspy_rsa).",
            "profile_name_exists": "Profil o nazwie '{}' już istnieje.",
            "config_profile_created": "Profil '{}' został utworzony.",
            "config_profile_create_failed": "Nie udało się utworzyć profilu.",
            "config_profile_rename_failed": "Zmiana nazwy nie powiodła się.",
            "config_profile_duplicate_name": "Nazwa dla duplikowanego profilu:",
            "config_profile_duplicate_failed": "Duplikowanie nie powiodło się.",
            "config_profile_delete_failed": "Usunięcie nie powiodło się.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Wyłącza tylko Maca (NAS pozostaje włączony, bez WOL)",
            "status_shutdown_mac_only": "Wyłączanie tylko Maca...",
            "say_shutdown_mac_only": "Mac jest wyłączany, NAS pozostaje włączony",

            "btn_scheduled_shutdown": "🕐 Zaplanowane wyłączenie",
            "tooltip_scheduled_shutdown": "Wyłącza po wybranym przez użytkownika czasie",
            "btn_scheduled_shutdown_offline": "🕐 Zaplanowane wyłączenie Maca",
            "tooltip_scheduled_shutdown_offline": "Wyłącza tylko Maca po wybranym czasie (NAS jest offline)",
            "btn_cancel_scheduled": "⏹ Anuluj odliczanie",
            "tooltip_cancel_scheduled": "Anuluje aktywne odliczanie",

            "sched_dialog_title": "Zaplanowane wyłączenie",
            "sched_target_label": "Cel:",
            "sched_target_both": "🖥️ Mac + NAS  (pełne wyłączenie)",
            "sched_target_nas": "🗄️ Tylko NAS  (Mac pozostaje włączony)",
            "sched_target_mac": "💻 Tylko Mac  (NAS pozostaje włączony)",

            "sched_wait_label": "Czas oczekiwania do wyłączenia:",
            "sched_hours": "Godziny",
            "sched_minutes": "Minuty",

            "sched_caffeinate_label": "Opcja caffeinate (utrzymuje Maca w stanie czuwania):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Zalecane: System czuwa, ekran może przygasnąć  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Zapobiegaj tylko bezczynności i uśpieniu dysku (ekran pozostaje włączony)  (-i -m)",
            "sched_caffeinate_d": "Ekran dodatkowo pozostaje włączony  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Symuluj aktywność użytkownika (ekran jasny, system czuwa)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maksimum: Ekran + system + dysk stale czuwają  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Wyłączone (normalne oszczędzanie energii – system może spać)",

            "sched_caffeinate_hint": (
                "💡 Ciekawostka edukacyjna: Używaj flag caffeinate bezpośrednio w terminalu:\n"
                "   -i  zapobiega uśpieniu systemu z powodu bezczynności\n"
                "   -m  zapobiega uśpieniu dysku (dysk twardy nie zasypia)\n"
                "   -s  zapobiega uśpieniu systemu (tylko na zasilaczu)\n"
                "   -d  zapobiega uśpieniu ekranu (ekran pozostaje włączony)\n"
                "   -u  symuluje aktywność użytkownika (ekran pozostaje jasny)\n"
                "   -w PID  kończy caffeinate, gdy proces PID się zakończy\n"
                "Przykład:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Wyłączenie zaplanowane na: {}",
            "sched_countdown_label": "Odliczanie: {} do wyłączenia ({})",
            "sched_started": "Uruchomiono licznik czasu.\n\nCel: {}\nCzas trwania: {}\nKoniec: {}",
            "sched_cancelled": "Licznik czasu anulowany",
            "sched_already_active": "Licznik czasu już działa. Najpierw anulować?",
            "sched_invalid_time": "Podaj prawidłowy czas (co najmniej 1 minuta).",
            "sched_max_time": "Maksymalnie dozwolone 720 godzin (30 dni).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Licznik czasu uruchomiony. Mac i NAS zostaną wyłączone za {}."
            ),
            "sched_voice_started_nas": (
                "Licznik czasu uruchomiony. Tylko NAS zostanie wyłączony za {}. "
                "Mac pozostaje włączony."
            ),
            "sched_voice_started_mac": (
                "Licznik czasu uruchomiony. Tylko Mac zostanie wyłączony za {}. "
                "NAS pozostaje włączony."
            ),
            "sched_voice_started_nothing": (
                "Licznik czasu uruchomiony. Po upływie nic nie zostanie wykonane. "
                "caffeinate pozostaje aktywny do tego czasu."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Mac pozostaje w stanie czuwania przez {}. "
                "Ekran może przygasnąć. "
                "Po upływie nic nie zostanie wykonane."
            ),
            "sched_voice_nothing_im": (
                "Mac pozostaje w stanie czuwania przez {}. "
                "Ekran pozostaje włączony. "
                "Po upływie nic nie zostanie wykonane."
            ),
            "sched_voice_nothing_d": (
                "Mac i ekran pozostają włączeni przez {}. "
                "Po upływie nic nie zostanie wykonane."
            ),
            "sched_voice_nothing_u": (
                "Mac pozostaje aktywny przez {}. "
                "Ekran pozostaje jasny. "
                "Po upływie nic nie zostanie wykonane."
            ),
            "sched_voice_nothing_full": (
                "Mac pozostaje w pełni aktywny przez {} – ekran i system nieprzerwanie czuwają. "
                "Po upływie nic nie zostanie wykonane."
            ),
            "sched_voice_nothing_off": (
                "Licznik czasu działa przez {}. "
                "Po upływie nic nie zostanie wykonane. "
                "Uwaga: Mac może przejść w tryb uśpienia."
            ),
            "sched_voice_cancelled": "Licznik czasu anulowany",
            "sched_caffeinate_failed": "Nie udało się uruchomić caffeinate:\n{}",
            "sched_target_required": "Wybierz cel.",
            "sched_tooltip_active": "Licznik czasu działa – kliknij, aby anulować",

            "status_scheduled_active": "Licznik czasu aktywny - pozostało {}",
            "status_scheduled_triggered": "Licznik czasu upłynął - uruchamianie {}",
            "status_scheduled_cancelled": "Licznik czasu anulowany",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Licznik czasu aktywny",
            "close_blocked_text": (
                "<b>Nadal działa licznik czasu!</b><br><br>"
                "Zaplanowano: {}<br>"
                "Pozostało: <b>{}</b><br>"
                "O: {}<br><br>"
                "Jeśli teraz zamkniesz, zaplanowane wyłączenie "
                "<b>nie zostanie już wykonane</b>."
            ),
            "close_blocked_yes": "Mimo to zamknij",
            "close_blocked_no": "Pozostaw aplikację uruchomioną",
            "close_blocked_cancel_text": (
                "Nadal działa licznik czasu.\n\n"
                "Czy naprawdę chcesz zamknąć aplikację?\n"
                "(Zaplanowane wyłączenie zostanie wtedy odrzucone.)"
            ),
            "close_blocked_log_aborted": "Zamknięcie anulowane (licznik czasu aktywny)",
            "close_blocked_log_discarded": (
                "Aplikacja zamyka się mimo aktywnego licznika czasu – licznik odrzucony"
            ),
            "close_blocked_log_cancel_aborted": (
                "Zamknięcie aplikacji anulowane przyciskiem Anuluj"
            ),
            "duration_day": "dzień",
            "duration_days": "dni",
            "duration_hour": "godzina",
            "duration_hours": "godzin",
            "duration_minute": "minuta",
            "duration_minutes": "minut",
            "duration_connector_and": "i",
            "tooltip_pause_timer": "Wstrzymaj / wznów minutnik",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Timer wstrzymany – pozostało {} sekund",
            "timer_resumed": "Timer wznowiony",
            "say_timer_paused": "Timer wstrzymany",
            "say_timer_resumed": "Timer wznowiony",
            "tooltip_pause_timer": "Wstrzymaj/wznów timer",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Wyjście mowy włączone",
            "speech_enabled_hint": (
                "Wypowiada komunikaty statusu, potwierdzenia głośności i "
                "informacje o timerze za pomocą wyjścia mowy macOS. "
                "Po wyłączeniu aplikacja działa cicho."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Do zaplanowanego wyłączenia Maca wymagane jest "
                "hasło administratora.\n\n"
                "Jest ono bezpiecznie przechowywane w pęku kluczy macOS i "
                "używane tylko podczas wyłączania.\n\n"
                "Skonfigurować teraz?"
            ),
            "mac_pw_dialog_title": "Hasło administratora",
            "mac_pw_dialog_message": (
                "Do wyłączenia Maca wymagane jest hasło administratora.\n\n"
                "Jest ono bezpiecznie przechowywane w pęku kluczy macOS i "
                "używane tylko podczas wyłączania."
            ),
            "mac_pw_wrong_password": (
                "Hasło jest nieprawidłowe.\n\n"
                "Spróbuj ponownie."
            ),
            "mac_pw_test_failed": (
                "Błąd podczas sprawdzania hasła:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Timer nie został uruchomiony, ponieważ wprowadzanie "
                "hasła zostało anulowane.\n\n"
                "Bez hasła nie można wyłączyć Maca."
            ),
            "clear_password_title": "Usuń zapisane hasło",
            "clear_password_message": (
                "Usunąć hasło administratora przechowywane w pęku kluczy?\n\n"
                "Przy następnym zaplanowanym wyłączeniu hasło "
                "zostanie ponownie wyświetlone."
            ),
            "clear_password_success": "Hasło zostało usunięte z pęku kluczy.",
            "clear_password_failed": "Nie udało się usunąć hasła.",
            "clear_password_description": (
                "Usuwa hasło administratora przechowywane w pęku kluczy "
                "macOS. Przy następnym zaplanowanym wyłączeniu "
                "zostanie ono ponownie wyświetlone."
            ),
            "clear_password_button": "Usuń zapisane hasło",
            "shutdown_no_password_message": (
                "Nie udało się wyłączyć Maca.\n\n"
                "Nie jest dostępna ani reguła NOPASSWD w sudoers, ani "
                "zapisane hasło w pęku kluczy.\n\n"
                "Skonfiguruj ponownie zaplanowane wyłączenie."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Ostrzeżenie",
            "warning_eject_failed_continue": (
                "Nie udało się prawidłowo wysunąć dysków sieciowych.\n\n"
                "Jeśli dane są jeszcze kopiowane lub pliki są otwarte, "
                "może dojść do utraty danych.\n\n"
                "Kontynuować wyłączanie mimo to?"
            ),
            "auto_timer_disabled_no_pw": (
                "Automatyczne wyłączanie wyłączone – brak hasła "
                "administratora. Wprowadź je jednorazowo przy następnym monicie."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Tak",
            "btn_no": "Nie",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Nic nie wyłączaj  (Mac pozostaje wybudzony – np. dla skryptów kopii zapasowych)",
            "sched_countdown_coffee_label": "⏳ caffeinate aktywne: pozostało {} ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Minutnik kawy wciąż aktywny",
            "coffee_conflict_message": (
                "Minutnik kawy jest wciąż aktywny:\n\n"
                "Pozostało: {}\n\n"
                "Jeśli wyłączysz teraz, minutnik kawy zostanie anulowany "
                "i caffeinate zostanie zatrzymany.\n\n"
                "Wyłączyć mimo to?"
            ),
            "shutdown_timer_conflict_title": "Minutnik wyłączania wciąż aktywny",
            "shutdown_timer_conflict_message": (
                "Minutnik wyłączania jest wciąż aktywny:\n\n"
                "Zaplanowano: {}\n"
                "Pozostało: {}\n\n"
                "Jeśli wyłączysz ręcznie teraz, minutnik zostanie anulowany "
                "i trzeba będzie go zaplanować ponownie.\n\n"
                "Wyłączyć mimo to?"
            ),
            "tooltip_stop_timer": "Całkowicie zatrzymaj minutnik",
            "tooltip_stop_timer_inactive": "Brak aktywnego minutnika",
            "timer_stopped_notice": "⏹ Minutnik zatrzymany – gotowy do ponownego uruchomienia",
            "say_timer_stopped": "Minutnik zatrzymany",
            "say_timer_restarted": "Minutnik uruchomiony ponownie",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "Producent NAS:",
            "vendor_tooltip": (
                "Wybierz producenta swojego NAS. Określa polecenia "
                "wyłączania i ścieżki domyślne. 'Automatyczne wykrywanie' "
                "sprawdza NAS przez SSH."
            ),
            "vendor_auto_detect": "🔄 Automatyczne wykrywanie",
            "vendor_auto_detect_tooltip": (
                "Automatycznie rozpoznaj producenta przez SSH. "
                "Wymaganie: klucz SSH i IP są poprawnie skonfigurowane."
            ),
            "vendor_detect_in_progress": "🔄 Wykrywanie...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Ogólny Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Niestandardowy",
            "vendor_custom_hint": (
                "Niestandardowy: Dostosuj polecenia wyłączania ręcznie. "
                "Domyślnie: 'sudo shutdown -h now' (działa na "
                "80 % wszystkich NAS-ów z Linuxem)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Rozpoznano producenta: {}",
            "vendor_detect_success_question": (
                "Rozpoznano producenta: {}\n\n"
                "Czy chcesz użyć tego producenta?\n"
                "(Aktualna wartość: {})"
            ),
            "vendor_detect_failed": (
                "Nie udało się automatycznie rozpoznać producenta.\n\n"
                "Wybierz ręcznie. Większość NAS-ów z Linuxem "
                "działa z 'Ogólny Linux'."
            ),
            "vendor_detect_no_ssh": (
                "Automatyczne wykrywanie wymaga dostępu SSH.\n\n"
                "Sprawdź:\n"
                "• Ścieżka klucza SSH jest poprawna\n"
                "• Adres IP jest poprawny\n"
                "• SSH jest włączony na NAS-ie\n"
                "• Klucz SSH jest zainstalowany na NAS-ie "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Najpierw wprowadź klucz SSH i adres IP."
            ),
            "vendor_detect_nas_offline": (
                "Serwer NAS nie odpowiada.\n\n"
                "Sprawdź:\n"
                "• Czy NAS jest włączony?\n"
                "• Czy adres IP jest poprawny?\n"
                "• Czy NAS jest w tej samej sieci?\n\n"
                "Włącz NAS i spróbuj ponownie."
            ),
            "vendor_detect_error": "Błąd podczas automatycznego wykrywania:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "Nie znaleziono klucza SSH:\n\n{}\n\n"
                "Sprawdź ścieżkę w ustawieniach."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Polecenie wyłączania:",
            "custom_cmd_tooltip": (
                "Polecenie wysyłane do NAS-a przez SSH. "
                "Oddziel wiele poleceń średnikiem."
            ),
            "custom_cmd_hint": (
                "💡 Oddziel wiele poleceń średnikiem — "
                "użyte zostanie pierwsze udane. "
                "Przykład: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Pokaż pomoc dotyczącą poleceń wyłączania",
            "custom_cmd_help_title": "Typowe polecenia wyłączania",
            "custom_cmd_help_text": (
                "<h3>Typowe polecenia wyłączania według producenta</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (ogólny):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Wiele poleceń (łańcuch zapasowy)</h4>"
                "<p>Jeśli pierwsze polecenie zawiedzie, próbowane jest następne. "
                "Oddzielenie średnikiem:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Wskazówka:</b> Najpierw wybierz najbardziej prawdopodobne "
                "polecenie, potem alternatywy jako zabezpieczenie.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Wykrywanie wolumenów przez SSH...",
            "volumes_detection_via_paths": (
                "🔍 Szukam w ścieżkach specyficznych dla producenta..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Zapasowo: Szukam przez smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Szukam wolumenów przez SSH... Wyszukiwanie może "
                "potrwać kilka sekund."
            ),
            "volumes_detect_panel_success": (
                "Znaleziono {} wolumenów — {} nowych dodano, "
                "{} już istnieje"
            ),
            "volumes_detect_panel_partial": (
                "Znaleziono {} wolumenów — wszystkie już na liście"
            ),
            "volumes_detect_panel_failed": (
                "Nie znaleziono żadnych wolumenów. "
                "Wprowadź wolumeny ręcznie."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Wykrywanie adresu MAC...",
            "mac_detect_success": "✅ Wykryto adres MAC: {}",
            "mac_detect_success_dialog": (
                "Pomyślnie wykryto adres MAC.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Wartość została wpisana w pole MAC."
            ),
            "mac_detect_failed": (
                "⚠ Nie udało się automatycznie wykryć adresu MAC. "
                "Zostanie wyświetlona pomoc."
            ),
            "config_mac_find": "🔍 Znajdź MAC",
            "config_mac_find_tooltip": (
                "Automatycznie wykryj adres MAC. "
                "Jeśli się nie powiedzie, zostanie wyświetlony przewodnik."
            ),
        },
        # "🇵🇹 Português"
        "pt": {
            "language": "Idioma:",
            "window_title": "Gestão NAS",
            "status_checking": "A verificar ligação ao servidor...",
            "status_online": "Servidor NAS online ✓",
            "status_offline": "Servidor NAS offline",
            "status_settings": "Definições abertas - Temporizador parado",
            "status_settings_saved": "Definições guardadas",
            "status_settings_cancelled": "Definições canceladas",
            "status_shutdown": "A desligar NAS e Mac...",
            "status_shutdown_nas": "A desligar NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Desligamento NAS enviado, Mac será desligado agora...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Falha no desligamento do NAS, desligando Mac mesmo assim...",
            "status_starting": "A iniciar NAS via Wake-on-LAN...",
            "status_waiting": "A aguardar início do servidor...",
            "status_wol_sent": "Magic Packet enviado",
            "status_wol_failed": "WOL falhou",
            "status_mounting": "A montar volumes selecionados...",
            "status_mounting_volume": "A montar {}...",
            "status_mounted": "{} montado ✓",
            "status_unmounting": "A ejetar {}...",
            "status_unmounted": "{} ejetado ✓",
            "status_error": "Erro: {} não pôde ser montado",
            "status_error_unmount": "Erro: {} não pôde ser ejetado",
            "status_all_mounted": "Todos os volumes montados ✓",
            "status_all_unmounted": "Todos os volumes ejetados ✓",
            "status_mount_all": "A montar todos os volumes...",
            "status_unmount_all": "A ejetar todos os volumes...",
            "status_shutdown_cmd": "Comando de desligamento NAS enviado ✓",
            "status_timeout": "Tempo limite excedido - O servidor não pôde ser iniciado",
            "status_no_volumes": "Nenhum volume montado",
            "status_mount_failed": "Montagem falhou",
            "status_cancelled": "Cancelado - A aplicação vai fechar",
            "status_esc": "Tecla ESC pressionada - A aplicação vai fechar",
            "status_server_online": "Servidor online - à espera do serviço SMB...",
            "status_profile_changed": "Perfil alterado para: {}",
            "status_switching": "A mudar para perfil: {}...",
            "btn_shutdown_both": "Mac e NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Cancelar",
            "btn_start_nas": "Iniciar NAS",
            "btn_settings": "Definições (Cmd+E)",
            "btn_select_all": "Todos",
            "btn_save": "Guardar",
            "btn_reset": "Repor",
            "btn_info": "ℹ",
            "btn_profile": "Perfis",
            "tooltip_shutdown_both": "Desliga Mac e NAS em 2 min",
            "tooltip_shutdown_nas": "Desliga apenas o NAS",
            "tooltip_cancel": "Fecha a aplicação",
            "tooltip_start_nas": "Inicia NAS via Wake-on-LAN",
            "tooltip_settings": "Definições (Cmd+E)",
            "timer_shutdown": "Desligamento automático em {} segundos - ENTER apenas NAS",
            "timer_start": "Início automático em {} segundos - ENTER para início imediato",
            "volumes_title": "Volumes disponíveis",
            "volumes_title_offline": "Volumes a montar no início",
            "volumes_hint": "Nota: O primeiro volume da lista é automaticamente tratado como volume principal e não pode ser desativado.",
            "volumes_mount_tooltip": "Será montado automaticamente no início do servidor",
            "config_title": "AnyNasPy - Definições",
            "config_tab_profiles": "Perfis do servidor",
            "config_tab_general": "Geral",
            "config_tab_volumes": "Volumes",
            "config_tab_timing": "Temporização",
            "config_language": "Idioma:",
            "config_nas_group": "Definições do servidor NAS",
            "config_nas_user": "Nome de utilizador:",
            "config_nas_dns": "Nome DNS:",
            "config_nas_ip": "Endereço IP:",
            "config_nas_mac": "Endereço MAC:",
            "config_ssh_key": "Caminho da chave SSH:",
            "config_volumes_group": "Volumes",
            "config_volumes_label": "Volumes (um nome por linha):",
            "config_time_group": "Definições de tempo (segundos)",
            "config_auto_shutdown": "Atraso de desligamento automático:",
            "config_auto_start": "Atraso de início automático:",
            "config_wol_wait": "Tempo de espera WOL (máx):",
            "config_smb_wait": "Tempo de espera SMB:",
            "config_mount_retries": "Tentativas de montagem:",
            "config_status_file": "Ficheiro de estado",
            "config_json_path": "Ficheiro de configuração JSON:",
            "config_profile_name": "Nome do perfil:",
            "config_profile_active": "Perfil ativo",
            "config_profile_set_active": "Definir como perfil ativo",
            "config_profile_list": "Perfis existentes:",
            "config_profile_new": "Novo perfil",
            "config_profile_delete": "Eliminar perfil",
            "config_profile_duplicate": "Duplicar perfil",
            "config_profile_rename": "Renomear",
            "config_profile_required": "O nome do perfil é obrigatório.",
            "config_profile_exists": "Já existe um perfil com este nome.",
            "config_profile_deleted": "O perfil '{}' foi eliminado.",
            "config_profile_duplicated": "O perfil '{}' foi duplicado como '{}'.",
            "config_profile_renamed": "O perfil foi renomeado para '{}'.",
            "config_profile_activated": "O perfil '{}' está agora ativo.",
            "config_find_ip": "🔍 Encontrar IP",
            "config_find_ip_tooltip": "Encontrar automaticamente o IP do servidor na rede",
            "config_ssh_help": "? Ajuda",
            "config_mac_help": "? Ajuda",
            "config_mac_help_tooltip": "Instruções para encontrar o endereço MAC",
            "msg_ip_found": "O IP do servidor foi encontrado com sucesso:\n\n{}\n\nO IP foi inserido no campo.",
            "msg_ip_not_found": "Não foi possível encontrar automaticamente o IP do servidor.\n\nPor favor, insira o endereço IP manualmente.\n\nDicas:\n• Verifique o nome DNS nas definições\n• Certifique-se de que o NAS está ligado\n• Encontre o IP na interface DSM em 'Sistema > Rede'",
            "msg_reset_confirm": "Repor todas as definições para os valores padrão?",
            "msg_reset_title": "Repor",
            "msg_reset_done": "Todas as definições foram repostas para os valores padrão.",
            "msg_delete_confirm": "Deseja realmente eliminar o perfil '{}'?",
            "msg_delete_title": "Eliminar perfil",
            "msg_no_active_profile": "Nenhum perfil ativo selecionado.",
            "info_title": "Sobre o AnyNasPy",
            "info_version": "Versão",
            "info_copyright": "Copyright",
            "info_license": "Licença",
            "info_impressum": "Impressum",
            "info_developer": "Desenvolvedor",
            "info_contact": "Contato",
            "info_license_text": "Licença MIT",
            "say_timer_shutdown": "Desligamento automático do Mac e NAS em {} segundos - Enter apenas NAS - Escape para cancelar",
            "say_timer_start": "O servidor NAS será iniciado em {} segundos - Enter para início imediato",
            "say_server_online": "O servidor NAS está acessível",
            "say_server_offline": "O servidor NAS está offline",
            "say_shutdown_started": "Desligamento iniciado",
            "say_nas_shutdown": "O NAS está a desligar",
            "say_starting_nas": "A iniciar NAS",
            "say_cancelled": "Cancelado",
            "say_waiting_server": "A aguardar início do servidor",
            "say_wol_failed": "Erro ao enviar",
            "say_server_reachable": "Servidor acessível",
            "say_mount_volume": "{} pronto",
            "say_unmount_volume": "A ejetar {}",
            "say_mount_all": "A montar todos os volumes",
            "say_unmount_all": "A ejetar todos os volumes",
            "say_mount_error": "Erro ao montar",
            "say_unmount_error": "Erro ao ejetar",
            "say_mount_failed": "Nenhum volume montado",
            "say_settings_opened": "Definições abertas",
            "say_settings_saved": "Definições guardadas",
            "say_settings_cancelled": "Definições canceladas",
            "say_workaround_deleted": "Ficheiro de solução alternativa eliminado",
            "say_server_timeout": "Tempo limite de início do servidor excedido",
            "say_profile_changed": "Perfil alterado para {}",
            "ssh_key_create_title": "Criar Chave SSH",
            "ssh_key_create_question": "Deseja criar um novo par de chaves SSH?",
            "ssh_key_create_existing": "A chave SSH '{}' já existe.\nDeseja sobrescrevê-la?",
            "ssh_key_create_comment": "Comentário para a chave SSH (opcional):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "Chave SSH criada: {}",
            "ssh_key_create_error": "Erro ao criar chave SSH",
            "ssh_key_create_timeout": "Tempo limite para criação da chave SSH excedido",
            "ssh_key_create_failed": "ssh-keygen retornou um erro:\n{}",
            "ssh_key_create_passphrase": "Frase de acesso para a chave SSH (deixar vazio para nenhuma):",
            "ssh_key_create_passphrase_confirm": "Confirmar frase de acesso:",
            "ssh_key_create_passphrase_mismatch": "As frases de acesso não coincidem.",
            "ssh_key_create_info": "✅ Par de chaves SSH criado com sucesso:\n\n"
            "📁 Chave Privada: {}\n"
            "📁 Chave Pública: {}\n\n"
            "📋 Chave Pública para copiar:\n"
            "{}\n\n"
            "🔑 Como instalar a chave no seu NAS:\n"
            "1. Copie a chave pública (acima)\n"
            "2. Adicione ao arquivo:\n"
            "   ~/.ssh/authorized_keys no NAS\n"
            "3. Ou use:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Por favor, insira um nome de ficheiro diferente:",
            "ssh_key_exists_also": "A chave '{}' também existe.\nPor favor, elimine-a primeiro ou escolha outro nome.",
            "ssh_key_passphrase_title": "Frase de acesso",
            "ssh_key_passphrase_question": "Deseja usar uma frase de acesso para a chave SSH?\n\nSem frase de acesso: Ligação automática possível, menos segura.\nCom frase de acesso: Mais segura, mas pede em cada ligação.",
            "ssh_key_passphrase_enter": "Inserir frase de acesso",
            "ssh_key_passphrase_label": "Frase de acesso para chave SSH (mínimo 4 caracteres):",
            "ssh_key_passphrase_none": "Sem frase de acesso",
            "ssh_key_passphrase_none_question": "Não inseriu uma frase de acesso.\nDeseja criar a chave sem frase de acesso?",
            "ssh_key_passphrase_short": "Frase de acesso muito curta",
            "ssh_key_passphrase_short_message": "A frase de acesso deve ter pelo menos 4 caracteres.",
            "ssh_key_passphrase_confirm": "Confirmar frase de acesso",
            "ssh_key_passphrase_confirm_label": "Inserir frase de acesso novamente:",
            "ssh_key_passphrase_mismatch_title": "Erro de frase de acesso",
            "ssh_key_passphrase_mismatch_message": "As frases de acesso não coincidem.",
            "config_ssh_open": "Abrir",
            "config_ssh_open_tooltip": "Selecionar chave SSH ou abrir pasta",
            "config_ssh_create": "Criar",
            "config_ssh_create_tooltip": "Criar novo par de chaves SSH",
            "config_ssh_help_tooltip": "Mostrar ajuda da chave SSH",
            "config_ssh_select": "Selecionar chave SSH",
            "config_json_open": "Abrir",
            "config_json_open_tooltip": "Abrir pasta de configuração JSON",
            "config_error": "Erro",
            "config_shutdown_mac_delay": "Atraso entre desligamento NAS e Mac:",
            "info_third_party": "Bibliotecas de terceiros",
            "info_pyqt5_license": "Este aplicativo usa PyQt5, licenciado sob a GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nO texto completo da licença pode ser visto em https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Detectar volumes",
            "volumes_add": "Adicionar",
            "volumes_delete": "Excluir",
            "volumes_move_up": "Mover para cima",
            "volumes_move_down": "Mover para baixo",
            "volumes_available": "Volumes disponíveis:",
            "volumes_no_volumes": "Nenhum volume encontrado.",
            "volumes_detection_failed": "Falha na detecção de volumes.",
            "volumes_detection_success": "Volumes detectados com sucesso.",
            "volumes_confirm_delete": "Excluir realmente o volume '{}'?",
            "volumes_enter_name": "Por favor, insira o nome do novo volume:",
            "volumes_name_exists": "Já existe um volume com este nome.",
            "msg_invalid_ip": "O endereço IP inserido não é válido.\nPor favor, insira um endereço IPv4 válido (ex. 192.168.1.100).",
            "msg_select_volume": "Por favor, selecione um volume.",
            "msg_cannot_delete_main_volume": "O primeiro volume (volume principal) não pode ser excluído.",
            "profile_cannot_delete_last": "O último perfil não pode ser excluído.",
            "status_wol_sending": "Enviando pacote mágico...",
            "status_wol_method_failed": "Método Python falhou, tentando próximo...",
            "status_trying_wakeonlan": "Tentando wakeonlan...",
            "status_trying_etherwake": "Tentando etherwake...",
            "ssh_key_system_key_warning": "Aviso de segurança",
            "ssh_key_system_key_message": "O nome '{}' é uma chave de sistema e não será sobrescrito.\nPor favor, escolha outro nome (ex. synaspy_rsa).",
            "profile_name_exists": "Já existe um perfil com o nome '{}'.",
            "config_profile_created": "Perfil '{}' foi criado.",
            "config_profile_create_failed": "Não foi possível criar o perfil.",
            "config_profile_rename_failed": "Falha ao renomear.",
            "config_profile_duplicate_name": "Nome para o perfil duplicado:",
            "config_profile_duplicate_failed": "Falha ao duplicar.",
            "config_profile_delete_failed": "Falha ao excluir.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Desliga apenas o Mac (o NAS permanece ligado, sem WOL)",
            "status_shutdown_mac_only": "A desligar apenas o Mac...",
            "say_shutdown_mac_only": "O Mac está a desligar, o NAS permanece ligado",

            "btn_scheduled_shutdown": "🕐 Desligamento agendado",
            "tooltip_scheduled_shutdown": "Desliga após um tempo escolhido pelo utilizador",
            "btn_scheduled_shutdown_offline": "🕐 Desligar o Mac de forma agendada",
            "tooltip_scheduled_shutdown_offline": "Desliga apenas o Mac após um tempo selecionado (o NAS está offline)",
            "btn_cancel_scheduled": "⏹ Cancelar contagem decrescente",
            "tooltip_cancel_scheduled": "Cancela a contagem decrescente ativa",

            "sched_dialog_title": "Desligamento agendado",
            "sched_target_label": "Destino:",
            "sched_target_both": "🖥️ Mac + NAS  (desligamento completo)",
            "sched_target_nas": "🗄️ Apenas NAS  (o Mac permanece ligado)",
            "sched_target_mac": "💻 Apenas Mac  (o NAS permanece ligado)",

            "sched_wait_label": "Tempo de espera até ao desligamento:",
            "sched_hours": "Horas",
            "sched_minutes": "Minutos",

            "sched_caffeinate_label": "Opção caffeinate (mantém o Mac acordado):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Recomendado: Sistema acordado, o ecrã pode escurecer  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Impedir apenas inatividade e disco (o ecrã permanece ligado)  (-i -m)",
            "sched_caffeinate_d": "O ecrã permanece adicionalmente ligado  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simular atividade do utilizador (ecrã brilhante, sistema acordado)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Máximo: Ecrã + sistema + disco permanentemente acordados  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Desligado (poupança de energia normal – o sistema pode dormir)",

            "sched_caffeinate_hint": (
                "💡 Curiosidade didática: Usa os flags do caffeinate diretamente no terminal:\n"
                "   -i  impede o sono por inatividade do sistema\n"
                "   -m  impede o sono do disco (o disco rígido não dorme)\n"
                "   -s  impede o sono do sistema (apenas com adaptador de corrente)\n"
                "   -d  impede o sono do ecrã (o ecrã permanece ligado)\n"
                "   -u  simula a atividade do utilizador (o ecrã permanece brilhante)\n"
                "   -w PID  termina o caffeinate quando o processo PID terminar\n"
                "Exemplo:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Desligamento agendado para: {}",
            "sched_countdown_label": "Contagem decrescente: {} até ao desligamento ({})",
            "sched_started": "Temporizador iniciado.\n\nDestino: {}\nDuração: {}\nFim: {}",
            "sched_cancelled": "Temporizador cancelado",
            "sched_already_active": "Já está um temporizador em execução. Cancelar primeiro?",
            "sched_invalid_time": "Introduz um tempo válido (pelo menos 1 minuto).",
            "sched_max_time": "Máximo permitido: 720 horas (30 dias).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Temporizador iniciado. O Mac e o NAS serão desligados em {}."
            ),
            "sched_voice_started_nas": (
                "Temporizador iniciado. Apenas o NAS será desligado em {}. "
                "O Mac permanece ligado."
            ),
            "sched_voice_started_mac": (
                "Temporizador iniciado. Apenas o Mac será desligado em {}. "
                "O NAS permanece ligado."
            ),
            "sched_voice_started_nothing": (
                "Temporizador iniciado. Nada será executado quando terminar. "
                "caffeinate permanece ativo até lá."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "O Mac permanece acordado durante {}. "
                "O ecrã pode escurecer. "
                "Nada será executado quando terminar."
            ),
            "sched_voice_nothing_im": (
                "O Mac permanece acordado durante {}. "
                "O ecrã permanece ligado. "
                "Nada será executado quando terminar."
            ),
            "sched_voice_nothing_d": (
                "O Mac e o ecrã permanecem ligados durante {}. "
                "Nada será executado quando terminar."
            ),
            "sched_voice_nothing_u": (
                "O Mac permanece ativo durante {}. "
                "O ecrã permanece brilhante. "
                "Nada será executado quando terminar."
            ),
            "sched_voice_nothing_full": (
                "O Mac permanece totalmente ativo durante {} – ecrã e sistema continuamente acordados. "
                "Nada será executado quando terminar."
            ),
            "sched_voice_nothing_off": (
                "O temporizador funciona durante {}. "
                "Nada será executado quando terminar. "
                "Atenção: O Mac pode entrar em modo de suspensão."
            ),
            "sched_voice_cancelled": "Temporizador cancelado",
            "sched_caffeinate_failed": "Não foi possível iniciar o caffeinate:\n{}",
            "sched_target_required": "Seleciona um destino.",
            "sched_tooltip_active": "Temporizador em execução – clica para cancelar",

            "status_scheduled_active": "Temporizador ativo - {} restante",
            "status_scheduled_triggered": "Temporizador expirado - a iniciar {}",
            "status_scheduled_cancelled": "Temporizador cancelado",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Temporizador ativo",
            "close_blocked_text": (
                "<b>Ainda está um temporizador em execução!</b><br><br>"
                "Agendado: {}<br>"
                "Restante: <b>{}</b><br>"
                "Às: {}<br><br>"
                "Se fechares agora, o desligamento agendado "
                "<b>já não será executado</b>."
            ),
            "close_blocked_yes": "Fechar mesmo assim",
            "close_blocked_no": "Manter a app em execução",
            "close_blocked_cancel_text": (
                "Ainda está um temporizador em execução.\n\n"
                "Queres mesmo fechar a app?\n"
                "(O desligamento agendado será então descartado.)"
            ),
            "close_blocked_log_aborted": "Fecho cancelado (temporizador ativo)",
            "close_blocked_log_discarded": (
                "A app fecha apesar do temporizador ativo – temporizador descartado"
            ),
            "close_blocked_log_cancel_aborted": (
                "Fecho da app cancelado através do botão Cancelar"
            ),
            "duration_day": "dia",
            "duration_days": "dias",
            "duration_hour": "hora",
            "duration_hours": "horas",
            "duration_minute": "minuto",
            "duration_minutes": "minutos",
            "duration_connector_and": "e",
            "tooltip_pause_timer": "Pausar / retomar temporizador",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Temporizador em pausa – {} segundos restantes",
            "timer_resumed": "Temporizador retomado",
            "say_timer_paused": "Temporizador em pausa",
            "say_timer_resumed": "Temporizador retomado",
            "tooltip_pause_timer": "Pausar/retomar temporizador",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Saída de voz ativada",
            "speech_enabled_hint": (
                "Pronuncia mensagens de estado, confirmações de volume e "
                "informações do temporizador através da saída de voz do macOS. "
                "Quando desativada, a aplicação funciona em silêncio."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Para o encerramento programado do Mac é necessária a "
                "palavra-passe de administrador.\n\n"
                "É guardada em segurança no porta-chaves do macOS e "
                "utilizada apenas durante o encerramento.\n\n"
                "Configurar agora?"
            ),
            "mac_pw_dialog_title": "Palavra-passe de administrador",
            "mac_pw_dialog_message": (
                "Para o encerramento do Mac é necessária a palavra-passe "
                "de administrador.\n\n"
                "É guardada em segurança no porta-chaves do macOS e "
                "utilizada apenas durante o encerramento."
            ),
            "mac_pw_wrong_password": (
                "A palavra-passe está incorreta.\n\n"
                "Tente novamente."
            ),
            "mac_pw_test_failed": (
                "Erro ao verificar a palavra-passe:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "O temporizador não foi iniciado porque a introdução da "
                "palavra-passe foi cancelada.\n\n"
                "Sem palavra-passe, o Mac não pode ser encerrado."
            ),
            "clear_password_title": "Eliminar palavra-passe guardada",
            "clear_password_message": (
                "Eliminar a palavra-passe de administrador guardada no porta-chaves?\n\n"
                "No próximo encerramento programado, a palavra-passe "
                "será novamente solicitada."
            ),
            "clear_password_success": "A palavra-passe foi removida do porta-chaves.",
            "clear_password_failed": "Não foi possível eliminar a palavra-passe.",
            "clear_password_description": (
                "Remove a palavra-passe de administrador guardada no "
                "porta-chaves do macOS. No próximo encerramento programado "
                "será novamente solicitada."
            ),
            "clear_password_button": "Eliminar palavra-passe guardada",
            "shutdown_no_password_message": (
                "Não foi possível encerrar o Mac.\n\n"
                "Não está disponível nem uma regra NOPASSWD no sudoers nem "
                "uma palavra-passe guardada no porta-chaves.\n\n"
                "Configure novamente o encerramento programado."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Aviso",
            "warning_eject_failed_continue": (
                "Não foi possível ejetar corretamente as unidades de rede.\n\n"
                "Se ainda estiverem a ser copiados dados ou se houver "
                "ficheiros abertos, pode ocorrer perda de dados.\n\n"
                "Continuar mesmo assim com o encerramento?"
            ),
            "auto_timer_disabled_no_pw": (
                "Encerramento automático desativado – não há palavra-passe "
                "de administrador disponível. Introduza-a uma vez no próximo aviso."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Sim",
            "btn_no": "Não",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Não encerrar nada  (O Mac permanece acordado – por ex. para scripts de backup)",
            "sched_countdown_coffee_label": "⏳ caffeinate ativo: {} restantes ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Temporizador de café ainda ativo",
            "coffee_conflict_message": (
                "Um temporizador de café ainda está em execução:\n\n"
                "Restante: {}\n\n"
                "Se desligar agora, o temporizador de café será cancelado "
                "e o caffeinate será parado.\n\n"
                "Desligar mesmo assim?"
            ),
            "shutdown_timer_conflict_title": "Temporizador de desligamento ainda ativo",
            "shutdown_timer_conflict_message": (
                "Um temporizador de desligamento ainda está em execução:\n\n"
                "Programado: {}\n"
                "Restante: {}\n\n"
                "Se desligar manualmente agora, o temporizador será cancelado "
                "e terá de ser reprogramado.\n\n"
                "Desligar mesmo assim?"
            ),
            "tooltip_stop_timer": "Parar o temporizador completamente",
            "tooltip_stop_timer_inactive": "Nenhum temporizador ativo",
            "timer_stopped_notice": "⏹ Temporizador parado – pronto para reiniciar",
            "say_timer_stopped": "Temporizador parado",
            "say_timer_restarted": "Temporizador reiniciado",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "Fabricante do NAS:",
            "vendor_tooltip": (
                "Seleciona o fabricante do teu NAS. Determina os comandos "
                "de desligamento e os caminhos predefinidos. 'Deteção "
                "automática' verifica o NAS via SSH."
            ),
            "vendor_auto_detect": "🔄 Deteção automática",
            "vendor_auto_detect_tooltip": (
                "Detetar o fabricante automaticamente via SSH. "
                "Requisito: a chave SSH e o IP estão configurados corretamente."
            ),
            "vendor_detect_in_progress": "🔄 A detetar...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Linux genérico",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Personalizado",
            "vendor_custom_hint": (
                "Personalizado: ajusta os comandos de desligamento manualmente. "
                "Predefinido: 'sudo shutdown -h now' (funciona em "
                "80 % de todos os NAS Linux)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Fabricante detetado: {}",
            "vendor_detect_success_question": (
                "Fabricante detetado: {}\n\n"
                "Queres usar este fabricante?\n"
                "(Valor atual: {})"
            ),
            "vendor_detect_failed": (
                "Não foi possível detetar o fabricante automaticamente.\n\n"
                "Seleciona manualmente. A maioria dos NAS Linux "
                "funciona com 'Linux genérico'."
            ),
            "vendor_detect_no_ssh": (
                "A deteção automática requer acesso SSH.\n\n"
                "Verifica o seguinte:\n"
                "• O caminho da chave SSH está correto\n"
                "• O endereço IP está correto\n"
                "• O SSH está ativado no NAS\n"
                "• A chave SSH está instalada no NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Introduz primeiro a chave SSH e o endereço IP."
            ),
            "vendor_detect_nas_offline": (
                "O servidor NAS não responde.\n\n"
                "Verifica o seguinte:\n"
                "• O NAS está ligado?\n"
                "• O endereço IP está correto?\n"
                "• O NAS está na mesma rede?\n\n"
                "Liga o NAS e tenta novamente."
            ),
            "vendor_detect_error": "Erro na deteção automática:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "Chave SSH não encontrada:\n\n{}\n\n"
                "Verifica o caminho nas configurações."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Comando de desligamento:",
            "custom_cmd_tooltip": (
                "O comando enviado ao NAS via SSH. "
                "Separa vários comandos com ponto e vírgula."
            ),
            "custom_cmd_hint": (
                "💡 Separa vários comandos com ponto e vírgula — "
                "é usado o primeiro bem-sucedido. "
                "Exemplo: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Mostrar ajuda sobre comandos de desligamento",
            "custom_cmd_help_title": "Comandos de desligamento típicos",
            "custom_cmd_help_text": (
                "<h3>Comandos de desligamento típicos por fabricante</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (genérico):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Vários comandos (cadeia de reserva)</h4>"
                "<p>Se o primeiro comando falhar, é tentado o seguinte. "
                "Separação por ponto e vírgula:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Dica:</b> Escolhe primeiro o comando mais provável, "
                "depois alternativas como reserva.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 A detetar volumes via SSH...",
            "volumes_detection_via_paths": (
                "🔍 A procurar em caminhos específicos do fabricante..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Reserva: A procurar via smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 A procurar volumes via SSH... A procura pode "
                "demorar alguns segundos."
            ),
            "volumes_detect_panel_success": (
                "{} volumes encontrados — {} adicionados novos, "
                "{} já existentes"
            ),
            "volumes_detect_panel_partial": (
                "{} volumes encontrados — todos já na lista"
            ),
            "volumes_detect_panel_failed": (
                "Nenhum volume encontrado. "
                "Introduz os volumes manualmente."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 A detetar endereço MAC...",
            "mac_detect_success": "✅ Endereço MAC detetado: {}",
            "mac_detect_success_dialog": (
                "Endereço MAC detetado com sucesso.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "O valor foi introduzido no campo MAC."
            ),
            "mac_detect_failed": (
                "⚠ Não foi possível detetar o endereço MAC automaticamente. "
                "A ajuda será apresentada."
            ),
            "config_mac_find": "🔍 Encontrar MAC",
            "config_mac_find_tooltip": (
                "Detetar o endereço MAC automaticamente. "
                "Se falhar, será apresentado um guia."
            ),
        },
        # "🇷🇺 Russisch"
        "ru": {
            "language": "Язык:",
            "window_title": "Управление NAS",
            "status_checking": "Проверка подключения к серверу...",
            "status_online": "Сервер NAS онлайн ✓",
            "status_offline": "Сервер NAS офлайн",
            "status_settings": "Настройки открыты - Таймер остановлен",
            "status_settings_saved": "Настройки сохранены",
            "status_settings_cancelled": "Настройки отменены",
            "status_shutdown": "Выключение NAS и Mac...",
            "status_shutdown_nas": "Выключение NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Команда выключения NAS отправлена, Mac будет выключен сейчас...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Не удалось выключить NAS, выключаем Mac...",
            "status_starting": "Запуск NAS через Wake-on-LAN...",
            "status_waiting": "Ожидание запуска сервера...",
            "status_wol_sent": "Magic Packet отправлен",
            "status_wol_failed": "Ошибка WOL",
            "status_mounting": "Монтирование выбранных томов...",
            "status_mounting_volume": "Монтирование {}...",
            "status_mounted": "{} смонтирован ✓",
            "status_unmounting": "Извлечение {}...",
            "status_unmounted": "{} извлечён ✓",
            "status_error": "Ошибка: не удалось смонтировать {}",
            "status_error_unmount": "Ошибка: не удалось извлечь {}",
            "status_all_mounted": "Все тома смонтированы ✓",
            "status_all_unmounted": "Все тома извлечены ✓",
            "status_mount_all": "Монтирование всех томов...",
            "status_unmount_all": "Извлечение всех томов...",
            "status_shutdown_cmd": "Команда выключения NAS отправлена ✓",
            "status_timeout": "Тайм-аут - не удалось запустить сервер",
            "status_no_volumes": "Нет смонтированных томов",
            "status_mount_failed": "Ошибка монтирования",
            "status_cancelled": "Отменено - Приложение закрывается",
            "status_esc": "Нажата ESC - Приложение закрывается",
            "status_server_online": "Сервер онлайн - ожидание службы SMB...",
            "status_profile_changed": "Профиль изменён на: {}",
            "status_switching": "Переключение на профиль: {}...",
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Отмена",
            "btn_start_nas": "Запустить NAS",
            "btn_settings": "Настройки (Cmd+E)",
            "btn_select_all": "Все",
            "btn_save": "Сохранить",
            "btn_reset": "Сброс",
            "btn_info": "ℹ",
            "btn_profile": "Профили",
            "tooltip_shutdown_both": "Выключает Mac и NAS через 2 минуты",
            "tooltip_shutdown_nas": "Выключает только NAS",
            "tooltip_cancel": "Закрывает приложение",
            "tooltip_start_nas": "Запускает NAS через Wake-on-LAN",
            "tooltip_settings": "Настройки (Cmd+E)",
            "timer_shutdown": "Автовыключение через {} секунд - ENTER только для NAS",
            "timer_start": "Автозапуск через {} секунд - ENTER для немедленного запуска",
            "volumes_title": "Доступные тома",
            "volumes_title_offline": "Монтировать тома при запуске",
            "volumes_hint": "Примечание: первый том в списке автоматически считается основным и не может быть отключён.",
            "volumes_mount_tooltip": "Монтируется автоматически при запуске сервера",
            "config_title": "AnyNasPy - Настройки",
            "config_tab_profiles": "Профили сервера",
            "config_tab_general": "Общие",
            "config_tab_volumes": "Тома",
            "config_tab_timing": "Настройки времени",
            "config_language": "Язык:",
            "config_nas_group": "Настройки сервера NAS",
            "config_nas_user": "Имя пользователя:",
            "config_nas_dns": "DNS-имя:",
            "config_nas_ip": "IP-адрес:",
            "config_nas_mac": "MAC-адрес:",
            "config_ssh_key": "Путь к SSH-ключу:",
            "config_volumes_group": "Тома",
            "config_volumes_label": "Тома (одно имя в строке):",
            "config_time_group": "Настройки времени (секунды)",
            "config_auto_shutdown": "Задержка автовыключения:",
            "config_auto_start": "Задержка автозапуска:",
            "config_wol_wait": "Время ожидания WOL (макс):",
            "config_smb_wait": "Время ожидания SMB:",
            "config_mount_retries": "Количество попыток монтирования:",
            "config_status_file": "Файл состояния",
            "config_json_path": "Файл конфигурации JSON:",
            "config_profile_name": "Имя профиля:",
            "config_profile_active": "Активный профиль",
            "config_profile_set_active": "Установить как активный профиль",
            "config_profile_list": "Существующие профили:",
            "config_profile_new": "Новый профиль",
            "config_profile_delete": "Удалить профиль",
            "config_profile_duplicate": "Дублировать профиль",
            "config_profile_rename": "Переименовать",
            "config_profile_required": "Имя профиля обязательно.",
            "config_profile_exists": "Профиль с таким именем уже существует.",
            "config_profile_deleted": "Профиль '{}' удалён.",
            "config_profile_duplicated": "Профиль '{}' дублирован как '{}'.",
            "config_profile_renamed": "Профиль переименован в '{}'.",
            "config_profile_activated": "Профиль '{}' теперь активен.",
            "config_find_ip": "🔍 Найти IP",
            "config_find_ip_tooltip": "Автоматически найти IP сервера в сети",
            "config_ssh_help": "? Помощь",
            "config_mac_help": "? Помощь",
            "config_mac_help_tooltip": "Инструкция по поиску MAC-адреса",
            "msg_ip_found": "IP-адрес сервера успешно найден:\n\n{}\n\nIP вставлен в поле.",
            "msg_ip_not_found": "Не удалось автоматически определить IP-адрес сервера.\n\nПожалуйста, введите IP-адрес вручную.\n\nСоветы:\n• Проверьте DNS-имя в настройках\n• Убедитесь, что NAS включён\n• IP-адрес можно найти в интерфейсе DSM в разделе 'Система > Сеть'",
            "msg_reset_confirm": "Сбросить все настройки к значениям по умолчанию?",
            "msg_reset_title": "Сброс",
            "msg_reset_done": "Все настройки сброшены к значениям по умолчанию.",
            "msg_delete_confirm": "Действительно удалить профиль '{}'?",
            "msg_delete_title": "Удалить профиль",
            "msg_no_active_profile": "Активный профиль не выбран.",
            "info_title": "О AnyNasPy",
            "info_version": "Версия",
            "info_copyright": "Авторские права",
            "info_license": "Лицензия",
            "info_impressum": "Выходные данные",
            "info_developer": "Разработчик",
            "info_contact": "Контакты",
            "info_license_text": "Лицензия MIT",
            "say_timer_shutdown": "Автовыключение Mac и NAS через {} секунд - Enter только для NAS - Escape для отмены",
            "say_timer_start": "Сервер NAS будет запущен через {} секунд - Enter для немедленного запуска",
            "say_server_online": "Сервер NAS доступен",
            "say_server_offline": "Сервер NAS офлайн",
            "say_shutdown_started": "Запущено выключение",
            "say_nas_shutdown": "NAS выключается",
            "say_starting_nas": "Запуск NAS",
            "say_cancelled": "Отменено",
            "say_waiting_server": "Ожидание запуска сервера",
            "say_wol_failed": "Ошибка отправки",
            "say_server_reachable": "Сервер доступен",
            "say_mount_volume": "{} готов",
            "say_unmount_volume": "Извлечение {}",
            "say_mount_all": "Монтирование всех томов",
            "say_unmount_all": "Извлечение всех томов",
            "say_mount_error": "Ошибка монтирования",
            "say_unmount_error": "Ошибка извлечения",
            "say_mount_failed": "Ни один том не смонтирован",
            "say_settings_opened": "Настройки открыты",
            "say_settings_saved": "Настройки сохранены",
            "say_settings_cancelled": "Настройки отменены",
            "say_workaround_deleted": "Файл обходного пути удалён",
            "say_server_timeout": "Превышено время запуска сервера",
            "say_profile_changed": "Профиль изменён на {}",
            "ssh_key_create_title": "Создание SSH-ключа",
            "ssh_key_create_question": "Хотите создать новую пару SSH-ключей?",
            "ssh_key_create_existing": "SSH-ключ '{}' уже существует.\nХотите перезаписать его?",
            "ssh_key_create_comment": "Комментарий к SSH-ключу (необязательно):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH-ключ создан: {}",
            "ssh_key_create_error": "Ошибка при создании SSH-ключа",
            "ssh_key_create_timeout": "Превышено время создания ключа",
            "ssh_key_create_failed": "ssh-keygen вернул ошибку:\n{}",
            "ssh_key_create_passphrase": "Парольная фраза для SSH-ключа (оставьте пустым для отсутствия пароля):",
            "ssh_key_create_passphrase_confirm": "Подтвердите парольную фразу:",
            "ssh_key_create_passphrase_mismatch": "Парольные фразы не совпадают.",
            "ssh_key_create_info": "✅ Пара SSH-ключей успешно создана:\n\n"
            "📁 Приватный ключ: {}\n"
            "📁 Публичный ключ: {}\n\n"
            "📋 Публичный ключ для копирования:\n"
            "{}\n\n"
            "🔑 Как установить ключ на NAS:\n"
            "1. Скопируйте публичный ключ (выше)\n"
            "2. Вставьте его в файл:\n"
            "   ~/.ssh/authorized_keys на NAS\n"
            "3. Или используйте:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Пожалуйста, введите другое имя файла:",
            "ssh_key_exists_also": "Ключ '{}' также существует.\nПожалуйста, сначала удалите его или выберите другое имя.",
            "ssh_key_passphrase_title": "Парольная фраза",
            "ssh_key_passphrase_question": "Хотите использовать парольную фразу для SSH-ключа?\n\nБез пароля: возможно автоматическое подключение, менее безопасно.\nС паролем: безопаснее, но требуется ввод при каждом подключении.",
            "ssh_key_passphrase_enter": "Введите парольную фразу",
            "ssh_key_passphrase_label": "Парольная фраза для SSH-ключа (минимум 4 символа):",
            "ssh_key_passphrase_none": "Без парольной фразы",
            "ssh_key_passphrase_none_question": "Вы не ввели парольную фразу.\nХотите создать ключ без парольной фразы?",
            "ssh_key_passphrase_short": "Парольная фраза слишком короткая",
            "ssh_key_passphrase_short_message": "Парольная фраза должна содержать минимум 4 символа.",
            "ssh_key_passphrase_confirm": "Подтверждение парольной фразы",
            "ssh_key_passphrase_confirm_label": "Введите парольную фразу снова:",
            "ssh_key_passphrase_mismatch_title": "Ошибка парольной фразы",
            "ssh_key_passphrase_mismatch_message": "Парольные фразы не совпадают.",
            "config_ssh_open": "Открыть",
            "config_ssh_open_tooltip": "Выбрать SSH-ключ или открыть папку",
            "config_ssh_create": "Создать",
            "config_ssh_create_tooltip": "Создать новую пару SSH-ключей",
            "config_ssh_help_tooltip": "Показать справку по SSH-ключу",
            "config_ssh_select": "Выбрать SSH-ключ",
            "config_json_open": "Открыть",
            "config_json_open_tooltip": "Открыть папку конфигурации JSON",
            "config_error": "Ошибка",
            "config_shutdown_mac_delay": "Задержка между выключением NAS и Mac:",
            "info_third_party": "Сторонние библиотеки",
            "info_pyqt5_license": "Это приложение использует PyQt5, который распространяется под лицензией GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nПолный текст лицензии доступен по адресу https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Обнаружить тома",
            "volumes_add": "Добавить",
            "volumes_delete": "Удалить",
            "volumes_move_up": "Вверх",
            "volumes_move_down": "Вниз",
            "volumes_available": "Доступные тома:",
            "volumes_no_volumes": "Тома не найдены.",
            "volumes_detection_failed": "Ошибка обнаружения томов.",
            "volumes_detection_success": "Тома успешно обнаружены.",
            "volumes_confirm_delete": "Действительно удалить том '{}'?",
            "volumes_enter_name": "Пожалуйста, введите имя нового тома:",
            "volumes_name_exists": "Том с таким именем уже существует.",
            "msg_invalid_ip": "Введённый IP-адрес недействителен.\nПожалуйста, введите действительный IPv4-адрес (например, 192.168.1.100).",
            "msg_select_volume": "Пожалуйста, выберите том.",
            "msg_cannot_delete_main_volume": "Первый том (основной) не может быть удалён.",
            "profile_cannot_delete_last": "Последний профиль не может быть удалён.",
            "status_wol_sending": "Отправка магического пакета...",
            "status_wol_method_failed": "Метод Python не сработал, пробуем следующий...",
            "status_trying_wakeonlan": "Пробуем wakeonlan...",
            "status_trying_etherwake": "Пробуем etherwake...",
            "ssh_key_system_key_warning": "Предупреждение безопасности",
            "ssh_key_system_key_message": "Имя '{}' является системным ключом и не будет перезаписано.\nПожалуйста, выберите другое имя (например, synaspy_rsa).",
            "profile_name_exists": "Профиль с именем '{}' уже существует.",
            "config_profile_created": "Профиль '{}' создан.",
            "config_profile_create_failed": "Не удалось создать профиль.",
            "config_profile_rename_failed": "Переименование не удалось.",
            "config_profile_duplicate_name": "Имя для дублированного профиля:",
            "config_profile_duplicate_failed": "Дублирование не удалось.",
            "config_profile_delete_failed": "Удаление не удалось.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Выключает только Mac (NAS остаётся включённым, без WOL)",
            "status_shutdown_mac_only": "Выключение только Mac...",
            "say_shutdown_mac_only": "Mac выключается, NAS остаётся включённым",

            "btn_scheduled_shutdown": "🕐 Запланированное выключение",
            "tooltip_scheduled_shutdown": "Выключает через выбранное пользователем время",
            "btn_scheduled_shutdown_offline": "🕐 Запланированное выключение Mac",
            "tooltip_scheduled_shutdown_offline": "Выключает только Mac через выбранное время (NAS офлайн)",
            "btn_cancel_scheduled": "⏹ Отменить обратный отсчёт",
            "tooltip_cancel_scheduled": "Отменяет активный обратный отсчёт",

            "sched_dialog_title": "Запланированное выключение",
            "sched_target_label": "Цель:",
            "sched_target_both": "🖥️ Mac + NAS  (полное выключение)",
            "sched_target_nas": "🗄️ Только NAS  (Mac остаётся включённым)",
            "sched_target_mac": "💻 Только Mac  (NAS остаётся включённым)",

            "sched_wait_label": "Время ожидания до выключения:",
            "sched_hours": "Часы",
            "sched_minutes": "Минуты",

            "sched_caffeinate_label": "Опция caffeinate (удерживает Mac в бодрствующем состоянии):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Рекомендуется: Система бодрствует, экран может затемниться  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Предотвратить только простой и сон диска (экран остаётся включённым)  (-i -m)",
            "sched_caffeinate_d": "Экран дополнительно остаётся включённым  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Имитировать активность пользователя (экран яркий, система бодрствует)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Максимум: Экран + система + диск постоянно бодрствуют  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Выключено (обычное энергосбережение – система может спать)",

            "sched_caffeinate_hint": (
                "💡 Познавательный факт: Используй флаги caffeinate прямо в терминале:\n"
                "   -i  предотвращает сон системы из-за простоя\n"
                "   -m  предотвращает сон диска (жёсткий диск не засыпает)\n"
                "   -s  предотвращает сон системы (только при питании от сети)\n"
                "   -d  предотвращает сон экрана (экран остаётся включённым)\n"
                "   -u  имитирует активность пользователя (экран остаётся ярким)\n"
                "   -w PID  завершает caffeinate, когда процесс PID завершается\n"
                "Пример:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Выключение запланировано на: {}",
            "sched_countdown_label": "Обратный отсчёт: {} до выключения ({})",
            "sched_started": "Таймер запущен.\n\nЦель: {}\nДлительность: {}\nОкончание: {}",
            "sched_cancelled": "Таймер отменён",
            "sched_already_active": "Таймер уже запущен. Сначала отменить?",
            "sched_invalid_time": "Введи корректное время (минимум 1 минута).",
            "sched_max_time": "Максимум допускается 720 часов (30 дней).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Таймер запущен. Mac и NAS будут выключены через {}."
            ),
            "sched_voice_started_nas": (
                "Таймер запущен. Только NAS будет выключен через {}. "
                "Mac остаётся включённым."
            ),
            "sched_voice_started_mac": (
                "Таймер запущен. Только Mac будет выключен через {}. "
                "NAS остаётся включённым."
            ),
            "sched_voice_started_nothing": (
                "Таймер запущен. По истечении ничего не будет выполнено. "
                "caffeinate остаётся активным до этого момента."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Mac остаётся бодрствующим в течение {}. "
                "Экран может затемниться. "
                "По истечении ничего не будет выполнено."
            ),
            "sched_voice_nothing_im": (
                "Mac остаётся бодрствующим в течение {}. "
                "Экран остаётся включённым. "
                "По истечении ничего не будет выполнено."
            ),
            "sched_voice_nothing_d": (
                "Mac и экран остаются включёнными в течение {}. "
                "По истечении ничего не будет выполнено."
            ),
            "sched_voice_nothing_u": (
                "Mac остаётся активным в течение {}. "
                "Экран остаётся ярким. "
                "По истечении ничего не будет выполнено."
            ),
            "sched_voice_nothing_full": (
                "Mac остаётся полностью активным в течение {} – экран и система непрерывно бодрствуют. "
                "По истечении ничего не будет выполнено."
            ),
            "sched_voice_nothing_off": (
                "Таймер работает в течение {}. "
                "По истечении ничего не будет выполнено. "
                "Внимание: Mac может перейти в режим сна."
            ),
            "sched_voice_cancelled": "Таймер отменён",
            "sched_caffeinate_failed": "Не удалось запустить caffeinate:\n{}",
            "sched_target_required": "Выбери цель.",
            "sched_tooltip_active": "Таймер активен – нажми для отмены",

            "status_scheduled_active": "Таймер активен - осталось {}",
            "status_scheduled_triggered": "Таймер истёк - запуск {}",
            "status_scheduled_cancelled": "Таймер отменён",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Таймер активен",
            "close_blocked_text": (
                "<b>Таймер всё ещё работает!</b><br><br>"
                "Запланировано: {}<br>"
                "Осталось: <b>{}</b><br>"
                "В: {}<br><br>"
                "Если закрыть сейчас, запланированное выключение "
                "<b>больше не будет выполнено</b>."
            ),
            "close_blocked_yes": "Всё равно закрыть",
            "close_blocked_no": "Оставить приложение работать",
            "close_blocked_cancel_text": (
                "Таймер всё ещё работает.\n\n"
                "Действительно закрыть приложение?\n"
                "(Запланированное выключение будет отменено.)"
            ),
            "close_blocked_log_aborted": "Закрытие отменено (таймер активен)",
            "close_blocked_log_discarded": (
                "Приложение закрывается несмотря на активный таймер – таймер отменён"
            ),
            "close_blocked_log_cancel_aborted": (
                "Закрытие приложения отменено кнопкой Отмена"
            ),
            "duration_day": "день",
            "duration_days": "дней",
            "duration_hour": "час",
            "duration_hours": "часов",
            "duration_minute": "минута",
            "duration_minutes": "минут",
            "duration_connector_and": "и",
            "tooltip_pause_timer": "Пауза / возобновить таймер",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Таймер приостановлен – осталось {} секунд",
            "timer_resumed": "Таймер возобновлён",
            "say_timer_paused": "Таймер приостановлен",
            "say_timer_resumed": "Таймер возобновлён",
            "tooltip_pause_timer": "Приостановить/возобновить таймер",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Речевой вывод включён",
            "speech_enabled_hint": (
                "Озвучивает сообщения о состоянии, подтверждения громкости и "
                "информацию о таймере через речевой вывод macOS. "
                "При отключении приложение работает беззвучно."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Для запланированного выключения Mac требуется "
                "пароль администратора.\n\n"
                "Он безопасно хранится в связке ключей macOS и "
                "используется только при выключении.\n\n"
                "Настроить сейчас?"
            ),
            "mac_pw_dialog_title": "Пароль администратора",
            "mac_pw_dialog_message": (
                "Для выключения Mac требуется пароль администратора.\n\n"
                "Он безопасно хранится в связке ключей macOS и "
                "используется только при выключении."
            ),
            "mac_pw_wrong_password": (
                "Неверный пароль.\n\n"
                "Попробуйте ещё раз."
            ),
            "mac_pw_test_failed": (
                "Ошибка при проверке пароля:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Таймер не был запущен, так как ввод "
                "пароля был отменён.\n\n"
                "Без пароля Mac не может быть выключен."
            ),
            "clear_password_title": "Удалить сохранённый пароль",
            "clear_password_message": (
                "Удалить пароль администратора, сохранённый в связке ключей?\n\n"
                "При следующем запланированном выключении пароль "
                "будет запрошен снова."
            ),
            "clear_password_success": "Пароль был удалён из связки ключей.",
            "clear_password_failed": "Не удалось удалить пароль.",
            "clear_password_description": (
                "Удаляет пароль администратора, сохранённый в связке "
                "ключей macOS. При следующем запланированном выключении "
                "он будет запрошен снова."
            ),
            "clear_password_button": "Удалить сохранённый пароль",
            "shutdown_no_password_message": (
                "Не удалось выключить Mac.\n\n"
                "Отсутствует как правило NOPASSWD в sudoers, так и "
                "сохранённый пароль в связке ключей.\n\n"
                "Пожалуйста, настройте запланированное выключение заново."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Предупреждение",
            "warning_eject_failed_continue": (
                "Не удалось корректно извлечь сетевые диски.\n\n"
                "Если данные всё ещё копируются или файлы открыты, "
                "возможна потеря данных.\n\n"
                "Всё равно продолжить выключение?"
            ),
            "auto_timer_disabled_no_pw": (
                "Автоматическое выключение отключено – нет пароля "
                "администратора. Пожалуйста, введите его один раз "
                "при следующем запросе."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Да",
            "btn_no": "Нет",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Ничего не выключать  (Mac остаётся активным – например, для скриптов резервного копирования)",
            "sched_countdown_coffee_label": "⏳ caffeinate активен: осталось {} ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Таймер кофе всё ещё работает",
            "coffee_conflict_message": (
                "Таймер кофе всё ещё работает:\n\n"
                "Осталось: {}\n\n"
                "Если выключить сейчас, таймер кофе будет отменён, "
                "а caffeinate остановлен.\n\n"
                "Всё равно выключить?"
            ),
            "shutdown_timer_conflict_title": "Таймер выключения всё ещё работает",
            "shutdown_timer_conflict_message": (
                "Таймер выключения всё ещё работает:\n\n"
                "Запланировано: {}\n"
                "Осталось: {}\n\n"
                "Если выключить вручную сейчас, таймер будет отменён "
                "и его нужно будет запланировать заново.\n\n"
                "Всё равно выключить?"
            ),
            "tooltip_stop_timer": "Полностью остановить таймер",
            "tooltip_stop_timer_inactive": "Таймер не активен",
            "timer_stopped_notice": "⏹ Таймер остановлен – готов к перезапуску",
            "say_timer_stopped": "Таймер остановлен",
            "say_timer_restarted": "Таймер перезапущен",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "Производитель NAS:",
            "vendor_tooltip": (
                "Выберите производителя вашего NAS. Определяет команды "
                "завершения работы и стандартные пути. «Автоопределение» "
                "проверяет NAS через SSH."
            ),
            "vendor_auto_detect": "🔄 Автоопределение",
            "vendor_auto_detect_tooltip": (
                "Автоматически определить производителя через SSH. "
                "Условие: SSH-ключ и IP настроены правильно."
            ),
            "vendor_detect_in_progress": "🔄 Определение...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Универсальный Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Пользовательский",
            "vendor_custom_hint": (
                "Пользовательский: настройте команды завершения работы вручную. "
                "По умолчанию: 'sudo shutdown -h now' (работает на "
                "80 % всех Linux-NAS)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Производитель определён: {}",
            "vendor_detect_success_question": (
                "Производитель определён: {}\n\n"
                "Использовать этого производителя?\n"
                "(Текущее значение: {})"
            ),
            "vendor_detect_failed": (
                "Не удалось автоматически определить производителя.\n\n"
                "Выберите вручную. Большинство Linux-NAS "
                "работают с «Универсальный Linux»."
            ),
            "vendor_detect_no_ssh": (
                "Автоопределение требует доступа по SSH.\n\n"
                "Проверьте:\n"
                "• Путь к SSH-ключу указан верно\n"
                "• IP-адрес указан верно\n"
                "• SSH включён на NAS\n"
                "• SSH-ключ установлен на NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Сначала введите SSH-ключ и IP-адрес."
            ),
            "vendor_detect_nas_offline": (
                "Сервер NAS не отвечает.\n\n"
                "Проверьте:\n"
                "• Включён ли NAS?\n"
                "• Правильный ли IP-адрес?\n"
                "• Находится ли NAS в той же сети?\n\n"
                "Включите NAS и попробуйте снова."
            ),
            "vendor_detect_error": "Ошибка при автоопределении:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH-ключ не найден:\n\n{}\n\n"
                "Проверьте путь в настройках."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Команда завершения работы:",
            "custom_cmd_tooltip": (
                "Команда, отправляемая на NAS через SSH. "
                "Несколько команд разделяйте точкой с запятой."
            ),
            "custom_cmd_hint": (
                "💡 Несколько команд разделяйте точкой с запятой — "
                "используется первая успешная. "
                "Пример: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Показать справку по командам завершения работы",
            "custom_cmd_help_title": "Типичные команды завершения работы",
            "custom_cmd_help_text": (
                "<h3>Типичные команды завершения работы по производителям</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (универсальный):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Несколько команд (резервная цепочка)</h4>"
                "<p>Если первая команда не сработает, будет опробована следующая. "
                "Разделение точкой с запятой:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Совет:</b> Сначала выберите наиболее вероятную команду, "
                "затем альтернативы как резерв.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Определение томов через SSH...",
            "volumes_detection_via_paths": (
                "🔍 Поиск в специфичных для производителя путях..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Резерв: поиск через smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Поиск томов через SSH... Поиск может "
                "занять несколько секунд."
            ),
            "volumes_detect_panel_success": (
                "Найдено {} томов — {} добавлено новых, "
                "{} уже присутствуют"
            ),
            "volumes_detect_panel_partial": (
                "Найдено {} томов — все уже в списке"
            ),
            "volumes_detect_panel_failed": (
                "Тома не найдены. "
                "Введите тома вручную."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Определение MAC-адреса...",
            "mac_detect_success": "✅ MAC-адрес определён: {}",
            "mac_detect_success_dialog": (
                "MAC-адрес успешно определён.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Значение введено в поле MAC."
            ),
            "mac_detect_failed": (
                "⚠ Не удалось автоматически определить MAC-адрес. "
                "Будет показана справка."
            ),
            "config_mac_find": "🔍 Найти MAC",
            "config_mac_find_tooltip": (
                "Автоматически определить MAC-адрес. "
                "Если не удастся, будет показано руководство."
            ),
        },
        # "🇫🇮 Suomi" (Finnisch)
        "fi": {
            "language": "Kieli:",
            "window_title": "NAS-hallinta",
            "status_checking": "Tarkistetaan palvelinyhteyttä...",
            "status_online": "NAS-palvelin on verkossa ✓",
            "status_offline": "NAS-palvelin ei ole verkossa",
            "status_settings": "Asetukset avattu - Ajastin pysäytetty",
            "status_settings_saved": "Asetukset tallennettu",
            "status_settings_cancelled": "Asetukset peruttu",
            "status_shutdown": "Sammutetaan NAS ja Mac...",
            "status_shutdown_nas": "Sammutetaan NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ NAS-sammutus lähetetty, Mac sammuu nyt...",
            "status_shutdown_nas_failed_mac_still": "⚠️ NAS-sammutus epäonnistui, sammutetaan Mac silti...",
            "status_starting": "Käynnistetään NAS Wake-on-LANilla...",
            "status_waiting": "Odotetaan palvelimen käynnistystä...",
            "status_wol_sent": "Magic Packet lähetetty",
            "status_wol_failed": "WOL epäonnistui",
            "status_mounting": "Liitetään valitut levyt...",
            "status_mounting_volume": "Liitetään {}...",
            "status_mounted": "{} liitetty ✓",
            "status_unmounting": "Irrotetaan {}...",
            "status_unmounted": "{} irrotettu ✓",
            "status_error": "Virhe: {} ei voitu liittää",
            "status_error_unmount": "Virhe: {} ei voitu irrottaa",
            "status_all_mounted": "Kaikki levyt liitetty ✓",
            "status_all_unmounted": "Kaikki levyt irrotettu ✓",
            "status_mount_all": "Liitetään kaikki levyt...",
            "status_unmount_all": "Irrotetaan kaikki levyt...",
            "status_shutdown_cmd": "NAS-sammutuskäsky lähetetty ✓",
            "status_timeout": "Aikakatkaisu - Palvelinta ei voitu käynnistää",
            "status_no_volumes": "Ei liitettyjä levyjä",
            "status_mount_failed": "Liittäminen epäonnistui",
            "status_cancelled": "Peruttu - Sovellus suljetaan",
            "status_esc": "ESC painettu - Sovellus suljetaan",
            "status_server_online": "Palvelin verkossa - odotetaan SMB-palvelua...",
            "status_profile_changed": "Profiili vaihdettu: {}",
            "status_switching": "Vaihdetaan profiiliin: {}...",
            "btn_shutdown_both": "Mac ja NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Peruuta",
            "btn_start_nas": "Käynnistä NAS",
            "btn_settings": "Asetukset (Cmd+E)",
            "btn_select_all": "Kaikki",
            "btn_save": "Tallenna",
            "btn_reset": "Palauta",
            "btn_info": "ℹ",
            "btn_profile": "Profiilit",
            "tooltip_shutdown_both": "Sammuttaa Macin ja NASin 2 minuutin kuluttua",
            "tooltip_shutdown_nas": "Sammuttaa vain NASin",
            "tooltip_cancel": "Sulkee sovelluksen",
            "tooltip_start_nas": "Käynnistää NASin Wake-on-LANilla",
            "tooltip_settings": "Asetukset (Cmd+E)",
            "timer_shutdown": "Automaattinen sammutus {} sekunnin kuluttua - ENTER vain NAS",
            "timer_start": "Automaattinen käynnistys {} sekunnin kuluttua - ENTER välittömään käynnistykseen",
            "volumes_title": "Käytettävissä olevat levyt",
            "volumes_title_offline": "Käynnistyksessä liitettävät levyt",
            "volumes_hint": "Huomautus: Listan ensimmäinen levyke käsitellään automaattisesti päälevykkeenä eikä sitä voi poistaa käytöstä.",
            "volumes_mount_tooltip": "Liitetään automaattisesti palvelimen käynnistyessä",
            "config_title": "AnyNasPy - Asetukset",
            "config_tab_profiles": "Palvelinprofiilit",
            "config_tab_general": "Yleinen",
            "config_tab_volumes": "Levyt",
            "config_tab_timing": "Ajoitus",
            "config_language": "Kieli:",
            "config_nas_group": "NAS-palvelimen asetukset",
            "config_nas_user": "Käyttäjätunnus:",
            "config_nas_dns": "DNS-nimi:",
            "config_nas_ip": "IP-osoite:",
            "config_nas_mac": "MAC-osoite:",
            "config_ssh_key": "SSH-avaimen polku:",
            "config_volumes_group": "Levyt",
            "config_volumes_label": "Levyt (yksi nimi per rivi):",
            "config_time_group": "Aika-asetukset (sekuntia)",
            "config_auto_shutdown": "Automaattisen sammutuksen viive:",
            "config_auto_start": "Automaattisen käynnistyksen viive:",
            "config_wol_wait": "WOL-odotusaika (max):",
            "config_smb_wait": "SMB-odotusaika:",
            "config_mount_retries": "Liityntäyritykset:",
            "config_status_file": "Tilatiedosto",
            "config_json_path": "JSON-konfigurointitiedosto:",
            "config_profile_name": "Profiilin nimi:",
            "config_profile_active": "Aktiivinen profiili",
            "config_profile_set_active": "Aseta aktiiviseksi profiiliksi",
            "config_profile_list": "Olemassa olevat profiilit:",
            "config_profile_new": "Uusi profiili",
            "config_profile_delete": "Poista profiili",
            "config_profile_duplicate": "Kopioi profiili",
            "config_profile_rename": "Nimeä uudelleen",
            "config_profile_required": "Profiilin nimi on pakollinen.",
            "config_profile_exists": "Tällä nimellä on jo profiili.",
            "config_profile_deleted": "Profiili '{}' poistettiin.",
            "config_profile_duplicated": "Profiili '{}' kopioitiin nimellä '{}'.",
            "config_profile_renamed": "Profiili nimettiin uudelleen '{}'.",
            "config_profile_activated": "Profiili '{}' on nyt aktiivinen.",
            "config_find_ip": "🔍 Etsi IP",
            "config_find_ip_tooltip": "Etsi automaattisesti palvelimen IP-osoite verkosta",
            "config_ssh_help": "? Ohje",
            "config_mac_help": "? Ohje",
            "config_mac_help_tooltip": "Ohjeet MAC-osoitteen löytämiseen",
            "msg_ip_found": "Palvelimen IP-osoite löytyi:\n\n{}\n\nIP on täytetty kenttään.",
            "msg_ip_not_found": "Palvelimen IP-osoitetta ei löytynyt automaattisesti.\n\nSyötä IP-osoite manuaalisesti.\n\nVihjeitä:\n• Tarkista DNS-nimi asetuksista\n• Varmista, että NAS on päällä\n• Löydä IP DSM-käyttöliittymästä kohdasta 'Järjestelmä > Verkko'",
            "msg_reset_confirm": "Palautetaanko kaikki asetukset oletusarvoihin?",
            "msg_reset_title": "Palauta",
            "msg_reset_done": "Kaikki asetukset on palautettu oletusarvoihin.",
            "msg_delete_confirm": "Haluatko varmasti poistaa profiilin '{}'?",
            "msg_delete_title": "Poista profiili",
            "msg_no_active_profile": "Aktiivista profiilia ei ole valittu.",
            "info_title": "Tietoja AnyNasPystä",
            "info_version": "Versio",
            "info_copyright": "Tekijänoikeus",
            "info_license": "Lisenssi",
            "info_impressum": "Impressum",
            "info_developer": "Kehittäjä",
            "info_contact": "Yhteystiedot",
            "info_license_text": "MIT-lisenssi",
            "say_timer_shutdown": "Macin ja NASin automaattinen sammutus {} sekunnin kuluttua - Enter vain NAS - Escape peruuttaa",
            "say_timer_start": "NAS-palvelin käynnistyy {} sekunnin kuluttua - Enter välittömään käynnistykseen",
            "say_server_online": "NAS-palvelin on tavoitettavissa",
            "say_server_offline": "NAS-palvelin ei ole verkossa",
            "say_shutdown_started": "Sammutus aloitettu",
            "say_nas_shutdown": "NAS sammutetaan",
            "say_starting_nas": "Käynnistetään NAS",
            "say_cancelled": "Peruttu",
            "say_waiting_server": "Odotetaan palvelimen käynnistystä",
            "say_wol_failed": "Virhe lähetyksessä",
            "say_server_reachable": "Palvelin tavoitettavissa",
            "say_mount_volume": "{} valmis",
            "say_unmount_volume": "Irrotetaan {}",
            "say_mount_all": "Liitetään kaikki levyt",
            "say_unmount_all": "Irrotetaan kaikki levyt",
            "say_mount_error": "Virhe liitettäessä",
            "say_unmount_error": "Virhe irrotettaessa",
            "say_mount_failed": "Ei liitettyjä levyjä",
            "say_settings_opened": "Asetukset avattu",
            "say_settings_saved": "Asetukset tallennettu",
            "say_settings_cancelled": "Asetukset peruttu",
            "say_workaround_deleted": "Työratkaisutiedosto poistettu",
            "say_server_timeout": "Palvelimen käynnistys aikakatkaistu",
            "say_profile_changed": "Profiili vaihdettu {}",
            "ssh_key_create_title": "Luo SSH-avain",
            "ssh_key_create_question": "Haluatko luoda uuden SSH-avainparin?",
            "ssh_key_create_existing": "SSH-avain '{}' on jo olemassa.\nHaluatko korvata sen?",
            "ssh_key_create_comment": "Kommentti SSH-avaimelle (valinnainen):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH-avain luotu: {}",
            "ssh_key_create_error": "Virhe SSH-avaimen luonnissa",
            "ssh_key_create_timeout": "SSH-avaimen luonti aikakatkaistiin",
            "ssh_key_create_failed": "ssh-keygen palautti virheen:\n{}",
            "ssh_key_create_passphrase": "SSH-avaimen salalause (jätä tyhjäksi jos ei halua):",
            "ssh_key_create_passphrase_confirm": "Vahvista salalause:",
            "ssh_key_create_passphrase_mismatch": "Salalauseet eivät täsmää.",
            "ssh_key_create_info": "✅ SSH-avainpari luotu onnistuneesti:\n\n"
            "📁 Yksityinen Avain: {}\n"
            "📁 Julkinen Avain: {}\n\n"
            "📋 Julkinen Avain kopioitavaksi:\n"
            "{}\n\n"
            "🔑 Näin asennat avaimen NAS-laitteellesi:\n"
            "1. Kopioi julkinen avain (ylhäällä)\n"
            "2. Lisää se tiedostoon:\n"
            "   ~/.ssh/authorized_keys NAS-laitteella\n"
            "3. Tai käytä:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Anna toinen tiedostonimi:",
            "ssh_key_exists_also": "Avain '{}' on olemassa myös.\nPoista se ensin tai valitse toinen nimi.",
            "ssh_key_passphrase_title": "Salalause",
            "ssh_key_passphrase_question": "Haluatko käyttää salalausetta SSH-avaimelle?\n\nIlman salalausetta: Automaattinen yhteys mahdollinen, vähemmän turvallinen.\nSalalauseella: Turvallisempi, mutta kysyy jokaisessa yhteydessä.",
            "ssh_key_passphrase_enter": "Anna salalause",
            "ssh_key_passphrase_label": "Salalause SSH-avaimelle (vähintään 4 merkkiä):",
            "ssh_key_passphrase_none": "Ei salalausetta",
            "ssh_key_passphrase_none_question": "Et antanut salalausetta.\nHaluatko luoda avaimen ilman salalausetta?",
            "ssh_key_passphrase_short": "Salalause liian lyhyt",
            "ssh_key_passphrase_short_message": "Salalauseen on oltava vähintään 4 merkkiä pitkä.",
            "ssh_key_passphrase_confirm": "Vahvista salalause",
            "ssh_key_passphrase_confirm_label": "Anna salalause uudelleen:",
            "ssh_key_passphrase_mismatch_title": "Salalause virhe",
            "ssh_key_passphrase_mismatch_message": "Salalauseet eivät täsmää.",
            "config_ssh_open": "Avaa",
            "config_ssh_open_tooltip": "Valitse SSH-avain tai avaa kansio",
            "config_ssh_create": "Luo",
            "config_ssh_create_tooltip": "Luo uusi SSH-avainpari",
            "config_ssh_help_tooltip": "Näytä SSH-avaimen ohje",
            "config_ssh_select": "Valitse SSH-avain",
            "config_json_open": "Avaa",
            "config_json_open_tooltip": "Avaa JSON-konfiguraatiokansio",
            "config_error": "Virhe",
            "config_shutdown_mac_delay": "Viive NAS- ja Mac-sammutuksen välillä:",
            "info_third_party": "Kolmannen osapuolen kirjastot",
            "info_pyqt5_license": "Tämä sovellus käyttää PyQt5:ä, joka on lisensoitu GNU General Public License v3 (GPLv3) -lisenssillä.\nTekijänoikeus (c) Riverbank Computing Limited.\n\nKoko lisenssiteksti on nähtävissä osoitteessa https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Tunnista levyt",
            "volumes_add": "Lisää",
            "volumes_delete": "Poista",
            "volumes_move_up": "Siirrä ylös",
            "volumes_move_down": "Siirrä alas",
            "volumes_available": "Käytettävissä olevat levyt:",
            "volumes_no_volumes": "Levyjä ei löytynyt.",
            "volumes_detection_failed": "Levyjen tunnistus epäonnistui.",
            "volumes_detection_success": "Levyt tunnistettu onnistuneesti.",
            "volumes_confirm_delete": "Poistetaanko levy '{}' varmasti?",
            "volumes_enter_name": "Anna uuden levyn nimi:",
            "volumes_name_exists": "Tällä nimellä oleva levy on jo olemassa.",
            "msg_invalid_ip": "Annettu IP-osoite ei ole kelvollinen.\nAnna kelvollinen IPv4-osoite (esim. 192.168.1.100).",
            "msg_select_volume": "Valitse levy.",
            "msg_cannot_delete_main_volume": "Ensimmäistä levyä (päälevyä) ei voi poistaa.",
            "profile_cannot_delete_last": "Viimeistä profiilia ei voi poistaa.",
            "status_wol_sending": "Lähetetään taikapakettia...",
            "status_wol_method_failed": "Python-menetelmä epäonnistui, yritetään seuraavaa...",
            "status_trying_wakeonlan": "Yritetään wakeonlan...",
            "status_trying_etherwake": "Yritetään etherwake...",
            "ssh_key_system_key_warning": "Turvallisuusvaroitus",
            "ssh_key_system_key_message": "Nimi '{}' on järjestelmäavain, eikä sitä kirjoiteta yli.\nValitse toinen nimi (esim. synaspy_rsa).",
            "profile_name_exists": "Profiili nimellä '{}' on jo olemassa.",
            "config_profile_created": "Profiili '{}' luotiin.",
            "config_profile_create_failed": "Profiilin luominen epäonnistui.",
            "config_profile_rename_failed": "Uudelleennimeäminen epäonnistui.",
            "config_profile_duplicate_name": "Nimi kopioidulle profiilille:",
            "config_profile_duplicate_failed": "Kopiointi epäonnistui.",
            "config_profile_delete_failed": "Poistaminen epäonnistui.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Sammuttaa vain Macin (NAS pysyy päällä, ei WOL)",
            "status_shutdown_mac_only": "Sammutetaan vain Macia...",
            "say_shutdown_mac_only": "Mac sammuu, NAS pysyy päällä",

            "btn_scheduled_shutdown": "🕐 Ajastettu sammutus",
            "tooltip_scheduled_shutdown": "Sammuttaa käyttäjän valitseman ajan jälkeen",
            "btn_scheduled_shutdown_offline": "🕐 Sammuta Mac ajastetusti",
            "tooltip_scheduled_shutdown_offline": "Sammuttaa vain Macin valitun ajan jälkeen (NAS on offline)",
            "btn_cancel_scheduled": "⏹ Peruuta lähtölaskenta",
            "tooltip_cancel_scheduled": "Peruuttaa aktiivisen lähtölaskennan",

            "sched_dialog_title": "Ajastettu sammutus",
            "sched_target_label": "Kohde:",
            "sched_target_both": "🖥️ Mac + NAS  (täysi sammutus)",
            "sched_target_nas": "🗄️ Vain NAS  (Mac pysyy päällä)",
            "sched_target_mac": "💻 Vain Mac  (NAS pysyy päällä)",

            "sched_wait_label": "Odotusaika sammutukseen:",
            "sched_hours": "Tunnit",
            "sched_minutes": "Minuutit",

            "sched_caffeinate_label": "caffeinate-vaihtoehto (pitää Macin hereillä):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Suositeltu: Järjestelmä hereillä, näyttö saa himmetä  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Estä vain joutokäynti ja levyn nukkuminen (näyttö pysyy päällä)  (-i -m)",
            "sched_caffeinate_d": "Näyttö pysyy lisäksi päällä  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simuloi käyttäjän aktiivisuutta (näyttö kirkas, järjestelmä hereillä)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maksimi: Näyttö + järjestelmä + levy pysyvästi hereillä  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Pois (normaali virransäästö – järjestelmä voi nukkua)",

            "sched_caffeinate_hint": (
                "💡 Oppimistieto: Käytä caffeinate-lippuja suoraan terminaalissa:\n"
                "   -i  estää järjestelmän joutokäyntinukkumisen\n"
                "   -m  estää levyn nukkumisen (kiintolevy ei nuku)\n"
                "   -s  estää järjestelmän nukkumisen (vain virtalähteellä)\n"
                "   -d  estää näytön nukkumisen (näyttö pysyy päällä)\n"
                "   -u  simuloi käyttäjän aktiivisuutta (näyttö pysyy kirkkaana)\n"
                "   -w PID  lopettaa caffeinate, kun prosessi PID päättyy\n"
                "Esimerkki:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Sammutus ajastettu: {}",
            "sched_countdown_label": "Lähtölaskenta: {} sammutukseen ({})",
            "sched_started": "Ajastin käynnistetty.\n\nKohde: {}\nKesto: {}\nLoppu: {}",
            "sched_cancelled": "Ajastin peruutettu",
            "sched_already_active": "Ajastin on jo käynnissä. Peruutetaanko ensin?",
            "sched_invalid_time": "Anna kelvollinen aika (vähintään 1 minuutti).",
            "sched_max_time": "Enintään 720 tuntia (30 päivää) sallittu.",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Ajastin käynnistetty. Mac ja NAS sammuvat {} kuluttua."
            ),
            "sched_voice_started_nas": (
                "Ajastin käynnistetty. Vain NAS sammuu {} kuluttua. "
                "Mac pysyy päällä."
            ),
            "sched_voice_started_mac": (
                "Ajastin käynnistetty. Vain Mac sammuu {} kuluttua. "
                "NAS pysyy päällä."
            ),
            "sched_voice_started_nothing": (
                "Ajastin käynnistetty. Mitään ei suoriteta, kun se päättyy. "
                "caffeinate pysyy aktiivisena siihen asti."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Mac pysyy hereillä {} ajan. "
                "Näyttö saa himmetä. "
                "Mitään ei suoriteta, kun se päättyy."
            ),
            "sched_voice_nothing_im": (
                "Mac pysyy hereillä {} ajan. "
                "Näyttö pysyy päällä. "
                "Mitään ei suoriteta, kun se päättyy."
            ),
            "sched_voice_nothing_d": (
                "Mac ja näyttö pysyvät päällä {} ajan. "
                "Mitään ei suoriteta, kun se päättyy."
            ),
            "sched_voice_nothing_u": (
                "Mac pysyy aktiivisena {} ajan. "
                "Näyttö pysyy kirkkaana. "
                "Mitään ei suoriteta, kun se päättyy."
            ),
            "sched_voice_nothing_full": (
                "Mac pysyy täysin aktiivisena {} ajan – näyttö ja järjestelmä jatkuvasti hereillä. "
                "Mitään ei suoriteta, kun se päättyy."
            ),
            "sched_voice_nothing_off": (
                "Ajastin on käynnissä {} ajan. "
                "Mitään ei suoriteta, kun se päättyy. "
                "Huomio: Mac voi siirtyä lepotilaan."
            ),
            "sched_voice_cancelled": "Ajastin peruutettu",
            "sched_caffeinate_failed": "caffeinate-tilaa ei voitu käynnistää:\n{}",
            "sched_target_required": "Valitse kohde.",
            "sched_tooltip_active": "Ajastin käynnissä – napsauta peruuttaaksesi",

            "status_scheduled_active": "Ajastin aktiivinen - {} jäljellä",
            "status_scheduled_triggered": "Ajastin päättyi - käynnistetään {}",
            "status_scheduled_cancelled": "Ajastin peruutettu",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Ajastin aktiivinen",
            "close_blocked_text": (
                "<b>Ajastin on vielä käynnissä!</b><br><br>"
                "Ajastettu: {}<br>"
                "Jäljellä: <b>{}</b><br>"
                "Klo: {}<br><br>"
                "Jos suljet nyt, ajastettua sammutusta "
                "<b>ei enää suoriteta</b>."
            ),
            "close_blocked_yes": "Sulje silti",
            "close_blocked_no": "Jätä sovellus käyntiin",
            "close_blocked_cancel_text": (
                "Ajastin on vielä käynnissä.\n\n"
                "Haluatko todella sulkea sovelluksen?\n"
                "(Ajastettu sammutus hylätään silloin.)"
            ),
            "close_blocked_log_aborted": "Sulkeminen peruutettu (ajastin aktiivinen)",
            "close_blocked_log_discarded": (
                "Sovellus suljetaan aktiivisesta ajastimesta huolimatta – ajastin hylätty"
            ),
            "close_blocked_log_cancel_aborted": (
                "Sovelluksen sulkeminen peruutettu Peruuta-painikkeella"
            ),
            "duration_day": "päivä",
            "duration_days": "päivää",
            "duration_hour": "tunti",
            "duration_hours": "tuntia",
            "duration_minute": "minuutti",
            "duration_minutes": "minuuttia",
            "duration_connector_and": "ja",
            "tooltip_pause_timer": "Keskeytä / jatka ajastinta",
            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Ajastin keskeytetty – {} sekuntia jäljellä",
            "timer_resumed": "Ajastin jatkettu",
            "say_timer_paused": "Ajastin keskeytetty",
            "say_timer_resumed": "Ajastin jatkettu",
            "tooltip_pause_timer": "Keskeytä/jatka ajastinta",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Puheentoisto käytössä",
            "speech_enabled_hint": (
                "Lukee tilailmoitukset, äänenvoimakkuuden vahvistukset ja "
                "ajastintiedot macOS:n puheentoiston kautta. Kun se on "
                "poistettu käytöstä, sovellus toimii äänettömästi."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Macin ajastettua sammuttamista varten tarvitaan "
                "järjestelmänvalvojan salasana.\n\n"
                "Se tallennetaan turvallisesti macOS:n avainnippuun ja sitä "
                "käytetään vain sammuttamisen yhteydessä.\n\n"
                "Määritetäänkö nyt?"
            ),
            "mac_pw_dialog_title": "Järjestelmänvalvojan salasana",
            "mac_pw_dialog_message": (
                "Macin sammuttamista varten tarvitaan järjestelmänvalvojan "
                "salasana.\n\n"
                "Se tallennetaan turvallisesti macOS:n avainnippuun ja sitä "
                "käytetään vain sammuttamisen yhteydessä."
            ),
            "mac_pw_wrong_password": (
                "Salasana on väärä.\n\n"
                "Yritä uudelleen."
            ),
            "mac_pw_test_failed": (
                "Virhe salasanan tarkistuksessa:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Ajastinta ei käynnistetty, koska salasanan "
                "syöttö peruutettiin.\n\n"
                "Ilman salasanaa Macia ei voi sammuttaa."
            ),
            "clear_password_title": "Poista tallennettu salasana",
            "clear_password_message": (
                "Poistetaanko avainnippuun tallennettu järjestelmänvalvojan salasana?\n\n"
                "Seuraavassa ajastetussa sammutuksessa salasana "
                "kysytään uudelleen."
            ),
            "clear_password_success": "Salasana poistettiin avainnipusta.",
            "clear_password_failed": "Salasanaa ei voitu poistaa.",
            "clear_password_description": (
                "Poistaa macOS:n avainnippuun tallennetun "
                "järjestelmänvalvojan salasanan. Seuraavassa "
                "ajastetussa sammutuksessa se kysytään uudelleen."
            ),
            "clear_password_button": "Poista tallennettu salasana",
            "shutdown_no_password_message": (
                "Macia ei voitu sammuttaa.\n\n"
                "Käytettävissä ei ole NOPASSWD-sudoers-sääntöä eikä "
                "avainnippuun tallennettua salasanaa.\n\n"
                "Määritä ajastettu sammutus uudelleen."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Varoitus",
            "warning_eject_failed_continue": (
                "Verkkoasemia ei voitu poistaa oikein.\n\n"
                "Jos tietoja kopioidaan edelleen tai tiedostoja on auki, "
                "tietoja voi kadota.\n\n"
                "Jatketaanko sammutusta silti?"
            ),
            "auto_timer_disabled_no_pw": (
                "Automaattinen sammutus poistettu käytöstä – "
                "järjestelmänvalvojan salasanaa ei ole. Anna se kerran "
                "seuraavassa kehotteessa."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Kyllä",
            "btn_no": "Ei",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Älä sammuta mitään  (Mac pysyy hereillä – esim. varmuuskopiointiskriptejä varten)",
            "sched_countdown_coffee_label": "⏳ caffeinate aktiivinen: {} jäljellä ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Kahviajastin on edelleen käytössä",
            "coffee_conflict_message": (
                "Kahviajastin on edelleen käynnissä:\n\n"
                "Jäljellä: {}\n\n"
                "Jos sammutat nyt, kahviajastin peruutetaan "
                "ja caffeinate pysäytetään.\n\n"
                "Sammuta silti?"
            ),
            "shutdown_timer_conflict_title": "Sammutusajastin on edelleen käytössä",
            "shutdown_timer_conflict_message": (
                "Sammutusajastin on edelleen käynnissä:\n\n"
                "Ajoitettu: {}\n"
                "Jäljellä: {}\n\n"
                "Jos sammutat manuaalisesti nyt, ajastin peruutetaan "
                "ja se on ajastettava uudelleen.\n\n"
                "Sammuta silti?"
            ),
            "tooltip_stop_timer": "Pysäytä ajastin kokonaan",
            "tooltip_stop_timer_inactive": "Ei aktiivista ajastinta",
            "timer_stopped_notice": "⏹ Ajastin pysäytetty – valmis uudelleenkäynnistykseen",
            "say_timer_stopped": "Ajastin pysäytetty",
            "say_timer_restarted": "Ajastin käynnistetty uudelleen",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "NAS-valmistaja:",
            "vendor_tooltip": (
                "Valitse NAS-laitteesi valmistaja. Määrittää "
                "sammutuskomennot ja oletuspolut. 'Automaattinen tunnistus' "
                "tarkistaa NAS-laitteen SSH:n kautta."
            ),
            "vendor_auto_detect": "🔄 Automaattinen tunnistus",
            "vendor_auto_detect_tooltip": (
                "Tunnista valmistaja automaattisesti SSH:n kautta. "
                "Edellytys: SSH-avain ja IP on määritetty oikein."
            ),
            "vendor_detect_in_progress": "🔄 Tunnistetaan...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Yleinen Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Mukautettu",
            "vendor_custom_hint": (
                "Mukautettu: Mukauta sammutuskomennot manuaalisesti. "
                "Oletus: 'sudo shutdown -h now' (toimii "
                "80 %:ssa kaikista Linux-NAS-laitteista)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Valmistaja tunnistettu: {}",
            "vendor_detect_success_question": (
                "Valmistaja tunnistettu: {}\n\n"
                "Otetaanko tämä valmistaja käyttöön?\n"
                "(Nykyinen arvo: {})"
            ),
            "vendor_detect_failed": (
                "Valmistajaa ei voitu tunnistaa automaattisesti.\n\n"
                "Valitse manuaalisesti. Useimmat Linux-NAS-laitteet "
                "toimivat 'Yleinen Linux' -valinnalla."
            ),
            "vendor_detect_no_ssh": (
                "Automaattinen tunnistus edellyttää SSH-yhteyttä.\n\n"
                "Tarkista seuraavat:\n"
                "• SSH-avaimen polku on oikein\n"
                "• IP-osoite on oikein\n"
                "• SSH on aktivoitu NAS-laitteessa\n"
                "• SSH-avain on asennettu NAS-laitteeseen "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Syötä ensin SSH-avain ja IP-osoite."
            ),
            "vendor_detect_nas_offline": (
                "NAS-palvelin ei vastaa.\n\n"
                "Tarkista seuraavat:\n"
                "• Onko NAS päällä?\n"
                "• Onko IP-osoite oikein?\n"
                "• Onko NAS samassa verkossa?\n\n"
                "Käynnistä NAS ja yritä uudelleen."
            ),
            "vendor_detect_error": "Virhe automaattisessa tunnistuksessa:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH-avainta ei löytynyt:\n\n{}\n\n"
                "Tarkista polku asetuksista."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Sammutuskäsky:",
            "custom_cmd_tooltip": (
                "Komento, joka lähetetään NAS-laitteeseen SSH:n kautta. "
                "Erota useat komennot puolipisteellä."
            ),
            "custom_cmd_hint": (
                "💡 Erota useat komennot puolipisteellä — "
                "ensimmäinen onnistunut käytetään. "
                "Esimerkki: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Näytä ohje sammutuskäskyistä",
            "custom_cmd_help_title": "Tyypilliset sammutuskäskyt",
            "custom_cmd_help_text": (
                "<h3>Tyypilliset sammutuskäskyt valmistajittain</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (yleinen):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Useita komentoja (varaketju)</h4>"
                "<p>Jos ensimmäinen komento epäonnistuu, seuraavaa yritetään. "
                "Erottelu puolipisteellä:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Vinkki:</b> Valitse ensin todennäköisin komento, "
                "sitten vaihtoehdot varalle.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Tunnistetaan taltioita SSH:n kautta...",
            "volumes_detection_via_paths": (
                "🔍 Etsitään valmistajakohtaisista poluista..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Varasuunnitelma: Etsitään smbclientin kautta..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Etsitään taltioita SSH:n kautta... Haku voi "
                "kestää muutaman sekunnin."
            ),
            "volumes_detect_panel_success": (
                "Löydettiin {} taltiota — {} lisätty uutena, "
                "{} jo olemassa"
            ),
            "volumes_detect_panel_partial": (
                "Löydettiin {} taltiota — kaikki jo luettelossa"
            ),
            "volumes_detect_panel_failed": (
                "Taltioita ei löytynyt. "
                "Syötä taltiot manuaalisesti."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Tunnistetaan MAC-osoitetta...",
            "mac_detect_success": "✅ MAC-osoite tunnistettu: {}",
            "mac_detect_success_dialog": (
                "MAC-osoite tunnistettu onnistuneesti.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Arvo on syötetty MAC-kenttään."
            ),
            "mac_detect_failed": (
                "⚠ MAC-osoitetta ei voitu tunnistaa automaattisesti. "
                "Ohje näytetään."
            ),
            "config_mac_find": "🔍 Etsi MAC",
            "config_mac_find_tooltip": (
                "Tunnista MAC-osoite automaattisesti. "
                "Jos se epäonnistuu, opas näytetään."
            ),
        },
        # "🇸🇪 Svenska (sv)" # Schwedisch
        "sv": {
            "language": "Språk:",
            "window_title": "NAS-hantering",
            "status_checking": "Kontrollerar serveranslutning...",
            "status_online": "NAS-server är online ✓",
            "status_offline": "NAS-server är offline",
            "status_settings": "Inställningar öppnade - Timer stoppad",
            "status_settings_saved": "Inställningar sparade",
            "status_settings_cancelled": "Inställningar avbrutna",
            "status_shutdown": "Stänger av NAS och Mac...",
            "status_shutdown_nas": "Stänger av NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ NAS-avstängning skickad, Mac stängs nu av...",
            "status_shutdown_nas_failed_mac_still": "⚠️ NAS-avstängning misslyckades, stänger av Mac ändå...",
            "status_starting": "Startar NAS via Wake-on-LAN...",
            "status_waiting": "Väntar på serverstart...",
            "status_wol_sent": "Magic Packet skickat",
            "status_wol_failed": "WOL misslyckades",
            "status_mounting": "Monterar valda volymer...",
            "status_mounting_volume": "Monterar {}...",
            "status_mounted": "{} monterad ✓",
            "status_unmounting": "Kopplar ur {}...",
            "status_unmounted": "{} urkopplad ✓",
            "status_error": "Fel: {} kunde inte monteras",
            "status_error_unmount": "Fel: {} kunde inte kopplas ur",
            "status_all_mounted": "Alla volymer monterade ✓",
            "status_all_unmounted": "Alla volymer urkopplade ✓",
            "status_mount_all": "Monterar alla volymer...",
            "status_unmount_all": "Kopplar ur alla volymer...",
            "status_shutdown_cmd": "NAS-avstängningskommando skickat ✓",
            "status_timeout": "Tidsgräns överskriden - Servern kunde inte startas",
            "status_no_volumes": "Inga volymer monterade",
            "status_mount_failed": "Montering misslyckades",
            "status_cancelled": "Avbrutet - Appen stängs",
            "status_esc": "ESC tryckt - Appen stängs",
            "status_server_online": "Server online - väntar på SMB-tjänst...",
            "status_profile_changed": "Profil ändrad till: {}",
            "status_switching": "Byter till profil: {}...",
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Avbryt",
            "btn_start_nas": "Starta NAS",
            "btn_settings": "Inställningar (Cmd+E)",
            "btn_select_all": "Alla",
            "btn_save": "Spara",
            "btn_reset": "Återställ",
            "btn_info": "ℹ",
            "btn_profile": "Profiler",
            "tooltip_shutdown_both": "Stänger av Mac och NAS om 2 min",
            "tooltip_shutdown_nas": "Stänger endast av NAS",
            "tooltip_cancel": "Stänger appen",
            "tooltip_start_nas": "Startar NAS via Wake-on-LAN",
            "tooltip_settings": "Inställningar (Cmd+E)",
            "timer_shutdown": "Automatisk avstängning om {} sekunder - ENTER endast NAS",
            "timer_start": "Automatisk start om {} sekunder - ENTER för omedelbar start",
            "volumes_title": "Tillgängliga volymer",
            "volumes_title_offline": "Volymer att montera vid start",
            "volumes_hint": "Obs! Den första volymen i listan behandlas automatiskt som huvudvolym och kan inte inaktiveras.",
            "volumes_mount_tooltip": "Kommer att monteras automatiskt vid serverstart",
            "config_title": "AnyNasPy - Inställningar",
            "config_tab_profiles": "Serverprofiler",
            "config_tab_general": "Allmänt",
            "config_tab_volumes": "Volymer",
            "config_tab_timing": "Tidsinställningar",
            "config_language": "Språk:",
            "config_nas_group": "NAS-serverinställningar",
            "config_nas_user": "Användarnamn:",
            "config_nas_dns": "DNS-namn:",
            "config_nas_ip": "IP-adress:",
            "config_nas_mac": "MAC-adress:",
            "config_ssh_key": "SSH-nyckelns sökväg:",
            "config_volumes_group": "Volymer",
            "config_volumes_label": "Volymer (ett namn per rad):",
            "config_time_group": "Tidsinställningar (sekunder)",
            "config_auto_shutdown": "Fördröjning automatisk avstängning:",
            "config_auto_start": "Fördröjning automatisk start:",
            "config_wol_wait": "WOL-väntetid (max):",
            "config_smb_wait": "SMB-väntetid:",
            "config_mount_retries": "Monteringsförsök:",
            "config_status_file": "Statusfil",
            "config_json_path": "JSON-konfigurationsfil:",
            "config_profile_name": "Profilnamn:",
            "config_profile_active": "Aktiv profil",
            "config_profile_set_active": "Ange som aktiv profil",
            "config_profile_list": "Befintliga profiler:",
            "config_profile_new": "Ny profil",
            "config_profile_delete": "Ta bort profil",
            "config_profile_duplicate": "Duplicera profil",
            "config_profile_rename": "Byt namn",
            "config_profile_required": "Profilnamn krävs.",
            "config_profile_exists": "Det finns redan en profil med detta namn.",
            "config_profile_deleted": "Profil '{}' togs bort.",
            "config_profile_duplicated": "Profil '{}' duplicerades som '{}'.",
            "config_profile_renamed": "Profilen bytte namn till '{}'.",
            "config_profile_activated": "Profil '{}' är nu aktiv.",
            "config_find_ip": "🔍 Hitta IP",
            "config_find_ip_tooltip": "Hitta automatiskt serverns IP i nätverket",
            "config_ssh_help": "? Hjälp",
            "config_mac_help": "? Hjälp",
            "config_mac_help_tooltip": "Instruktioner för att hitta MAC-adress",
            "msg_ip_found": "Serverns IP hittades:\n\n{}\n\nIP-adressen har fyllts i fältet.",
            "msg_ip_not_found": "Kunde inte hitta serverns IP automatiskt.\n\nAnge IP-adressen manuellt.\n\nTips:\n• Kontrollera DNS-namnet i inställningarna\n• Se till att NAS är påslagen\n• Hitta IP i DSM-gränssnittet under 'System > Nätverk'",
            "msg_reset_confirm": "Återställ alla inställningar till standardvärden?",
            "msg_reset_title": "Återställ",
            "msg_reset_done": "Alla inställningar har återställts till standardvärden.",
            "msg_delete_confirm": "Vill du verkligen ta bort profilen '{}'?",
            "msg_delete_title": "Ta bort profil",
            "msg_no_active_profile": "Ingen aktiv profil vald.",
            "info_title": "Om AnyNasPy",
            "info_version": "Version",
            "info_copyright": "Upphovsrätt",
            "info_license": "Licens",
            "info_impressum": "Impressum",
            "info_developer": "Utvecklare",
            "info_contact": "Kontakt",
            "info_license_text": "MIT-licens",
            "say_timer_shutdown": "Automatisk avstängning av Mac och NAS om {} sekunder - Enter endast NAS - Escape för att avbryta",
            "say_timer_start": "NAS-servern startar om {} sekunder - Enter för omedelbar start",
            "say_server_online": "NAS-servern är tillgänglig",
            "say_server_offline": "NAS-servern är offline",
            "say_shutdown_started": "Avstängning påbörjad",
            "say_nas_shutdown": "NAS stängs av",
            "say_starting_nas": "Startar NAS",
            "say_cancelled": "Avbrutet",
            "say_waiting_server": "Väntar på serverstart",
            "say_wol_failed": "Fel vid sändning",
            "say_server_reachable": "Server tillgänglig",
            "say_mount_volume": "{} redo",
            "say_unmount_volume": "Kopplar ur {}",
            "say_mount_all": "Monterar alla volymer",
            "say_unmount_all": "Kopplar ur alla volymer",
            "say_mount_error": "Fel vid montering",
            "say_unmount_error": "Fel vid urkoppling",
            "say_mount_failed": "Inga volymer monterade",
            "say_settings_opened": "Inställningar öppnade",
            "say_settings_saved": "Inställningar sparade",
            "say_settings_cancelled": "Inställningar avbrutna",
            "say_workaround_deleted": "Workaround-fil borttagen",
            "say_server_timeout": "Serverstart tidsgräns överskriden",
            "say_profile_changed": "Profil ändrad till {}",
            "ssh_key_create_title": "Skapa SSH-nyckel",
            "ssh_key_create_question": "Vill du skapa ett nytt SSH-nyckelpar?",
            "ssh_key_create_existing": "SSH-nyckeln '{}' finns redan.\nVill du skriva över den?",
            "ssh_key_create_comment": "Kommentar för SSH-nyckeln (valfritt):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH-nyckel skapad: {}",
            "ssh_key_create_error": "Fel vid skapande av SSH-nyckel",
            "ssh_key_create_timeout": "Tidsgräns för SSH-nyckel skapande överskriden",
            "ssh_key_create_failed": "ssh-keygen returnerade ett fel:\n{}",
            "ssh_key_create_passphrase": "Lösenfras för SSH-nyckel (lämna tom för ingen):",
            "ssh_key_create_passphrase_confirm": "Bekräfta lösenfras:",
            "ssh_key_create_passphrase_mismatch": "Lösenfraserna matchar inte.",
            "ssh_key_create_info": "✅ SSH-nyckelpar skapat:\n\n"
            "📁 Privat Nyckel: {}\n"
            "📁 Offentlig Nyckel: {}\n\n"
            "📋 Offentlig Nyckel att kopiera:\n"
            "{}\n\n"
            "🔑 Så här installerar du nyckeln på din NAS:\n"
            "1. Kopiera den offentliga nyckeln (ovan)\n"
            "2. Lägg till den i filen:\n"
            "   ~/.ssh/authorized_keys på NAS-en\n"
            "3. Eller använd:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Ange ett annat filnamn:",
            "ssh_key_exists_also": "Nyckeln '{}' finns också.\nVänligen ta bort den först eller välj ett annat namn.",
            "ssh_key_passphrase_title": "Lösenfras",
            "ssh_key_passphrase_question": "Vill du använda en lösenfras för SSH-nyckeln?\n\nUtan lösenfras: Automatisk anslutning möjlig, mindre säker.\nMed lösenfras: Säkerare, men frågar vid varje anslutning.",
            "ssh_key_passphrase_enter": "Ange lösenfras",
            "ssh_key_passphrase_label": "Lösenfras för SSH-nyckel (minst 4 tecken):",
            "ssh_key_passphrase_none": "Ingen lösenfras",
            "ssh_key_passphrase_none_question": "Du har inte angett en lösenfras.\nVill du skapa nyckeln utan lösenfras?",
            "ssh_key_passphrase_short": "Lösenfras för kort",
            "ssh_key_passphrase_short_message": "Lösenfrasen måste vara minst 4 tecken lång.",
            "ssh_key_passphrase_confirm": "Bekräfta lösenfras",
            "ssh_key_passphrase_confirm_label": "Ange lösenfras igen:",
            "ssh_key_passphrase_mismatch_title": "Lösenfras fel",
            "ssh_key_passphrase_mismatch_message": "Lösenfraserna matchar inte.",
            "config_ssh_open": "Öppna",
            "config_ssh_open_tooltip": "Välj SSH-nyckel eller öppna mapp",
            "config_ssh_create": "Skapa",
            "config_ssh_create_tooltip": "Skapa nytt SSH-nyckelpar",
            "config_ssh_help_tooltip": "Visa SSH-nyckelhjälp",
            "config_ssh_select": "Välj SSH-nyckel",
            "config_json_open": "Öppna",
            "config_json_open_tooltip": "Öppna JSON-konfigurationsmapp",
            "config_error": "Fel",
            "config_shutdown_mac_delay": "Fördröjning mellan NAS- och Mac-avstängning:",
            "info_third_party": "Tredjepartsbibliotek",
            "info_pyqt5_license": "Denna applikation använder PyQt5, som är licensierad under GNU General Public License v3 (GPLv3).\nCopyright (c) Riverbank Computing Limited.\n\nDen fullständiga licenstexten finns på https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Upptäck volymer",
            "volumes_add": "Lägg till",
            "volumes_delete": "Ta bort",
            "volumes_move_up": "Flytta upp",
            "volumes_move_down": "Flytta ner",
            "volumes_available": "Tillgängliga volymer:",
            "volumes_no_volumes": "Inga volymer hittades.",
            "volumes_detection_failed": "Misslyckades med att upptäcka volymer.",
            "volumes_detection_success": "Volymer upptäckta framgångsrikt.",
            "volumes_confirm_delete": "Ta verkligen bort volym '{}'?",
            "volumes_enter_name": "Ange namnet på den nya volymen:",
            "volumes_name_exists": "En volym med detta namn finns redan.",
            "msg_invalid_ip": "Den angivna IP-adressen är ogiltig.\nAnge en giltig IPv4-adress (t.ex. 192.168.1.100).",
            "msg_select_volume": "Välj en volym.",
            "msg_cannot_delete_main_volume": "Den första volymen (huvudvolym) kan inte tas bort.",
            "profile_cannot_delete_last": "Den sista profilen kan inte tas bort.",
            "status_wol_sending": "Skickar magiskt paket...",
            "status_wol_method_failed": "Python-metoden misslyckades, försöker nästa...",
            "status_trying_wakeonlan": "Försöker wakeonlan...",
            "status_trying_etherwake": "Försöker etherwake...",
            "ssh_key_system_key_warning": "Säkerhetsvarning",
            "ssh_key_system_key_message": "Namnet '{}' är en systemnyckel och kommer inte att skrivas över.\nVälj ett annat namn (t.ex. synaspy_rsa).",
            "profile_name_exists": "En profil med namnet '{}' finns redan.",
            "config_profile_created": "Profilen '{}' har skapats.",
            "config_profile_create_failed": "Det gick inte att skapa profilen.",
            "config_profile_rename_failed": "Namnbyte misslyckades.",
            "config_profile_duplicate_name": "Namn för den duplicerade profilen:",
            "config_profile_duplicate_failed": "Duplicering misslyckades.",
            "config_profile_delete_failed": "Borttagning misslyckades.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Stänger endast av Macen (NAS förblir på, ingen WOL)",
            "status_shutdown_mac_only": "Stänger endast av Macen...",
            "say_shutdown_mac_only": "Macen stängs av, NAS förblir på",

            "btn_scheduled_shutdown": "🕐 Schemalagd avstängning",
            "tooltip_scheduled_shutdown": "Stänger av efter en användarvald tid",
            "btn_scheduled_shutdown_offline": "🕐 Stäng av Macen schemalagt",
            "tooltip_scheduled_shutdown_offline": "Stänger endast av Macen efter en vald tid (NAS är offline)",
            "btn_cancel_scheduled": "⏹ Avbryt nedräkning",
            "tooltip_cancel_scheduled": "Avbryter den aktiva nedräkningen",

            "sched_dialog_title": "Schemalagd avstängning",
            "sched_target_label": "Mål:",
            "sched_target_both": "🖥️ Mac + NAS  (fullständig avstängning)",
            "sched_target_nas": "🗄️ Endast NAS  (Mac förblir på)",
            "sched_target_mac": "💻 Endast Mac  (NAS förblir på)",

            "sched_wait_label": "Väntetid till avstängning:",
            "sched_hours": "Timmar",
            "sched_minutes": "Minuter",

            "sched_caffeinate_label": "caffeinate-alternativ (håller Macen vaken):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Rekommenderat: Systemet vaket, skärmen får dimmas  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Förhindra endast inaktivitet och disk (skärmen förblir på)  (-i -m)",
            "sched_caffeinate_d": "Skärmen förblir dessutom på  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Simulera användaraktivitet (skärmen ljus, systemet vaket)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maximalt: Skärm + system + disk permanent vakna  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Av (normal energisparning – systemet kan sova)",

            "sched_caffeinate_hint": (
                "💡 Lärfakta: Använd caffeinate-flaggor direkt i terminalen:\n"
                "   -i  förhindrar systemets inaktivitetsviloläge\n"
                "   -m  förhindrar diskviloläge (hårddisken sover inte)\n"
                "   -s  förhindrar systemviloläge (endast på strömadapter)\n"
                "   -d  förhindrar skärmviloläge (skärmen förblir på)\n"
                "   -u  simulerar användaraktivitet (skärmen förblir ljus)\n"
                "   -w PID  avslutar caffeinate när processen PID avslutas\n"
                "Exempel:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Avstängning schemalagd till: {}",
            "sched_countdown_label": "Nedräkning: {} till avstängning ({})",
            "sched_started": "Timer startad.\n\nMål: {}\nVaraktighet: {}\nSlut: {}",
            "sched_cancelled": "Timer avbruten",
            "sched_already_active": "En timer körs redan. Avbryta först?",
            "sched_invalid_time": "Ange en giltig tid (minst 1 minut).",
            "sched_max_time": "Maximalt 720 timmar (30 dagar) tillåtna.",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Timer startad. Macen och NAS stängs av om {}."
            ),
            "sched_voice_started_nas": (
                "Timer startad. Endast NAS stängs av om {}. "
                "Macen förblir på."
            ),
            "sched_voice_started_mac": (
                "Timer startad. Endast Macen stängs av om {}. "
                "NAS förblir på."
            ),
            "sched_voice_started_nothing": (
                "Timer startad. Ingenting kommer att utföras när den löper ut. "
                "caffeinate förblir aktivt till dess."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Macen förblir vaken i {}. "
                "Skärmen får dimmas. "
                "Ingenting kommer att utföras när den löper ut."
            ),
            "sched_voice_nothing_im": (
                "Macen förblir vaken i {}. "
                "Skärmen förblir på. "
                "Ingenting kommer att utföras när den löper ut."
            ),
            "sched_voice_nothing_d": (
                "Macen och skärmen förblir på i {}. "
                "Ingenting kommer att utföras när den löper ut."
            ),
            "sched_voice_nothing_u": (
                "Macen förblir aktiv i {}. "
                "Skärmen förblir ljus. "
                "Ingenting kommer att utföras när den löper ut."
            ),
            "sched_voice_nothing_full": (
                "Macen förblir fullt aktiv i {} – skärm och system kontinuerligt vakna. "
                "Ingenting kommer att utföras när den löper ut."
            ),
            "sched_voice_nothing_off": (
                "Timern körs i {}. "
                "Ingenting kommer att utföras när den löper ut. "
                "Varning: Macen kan gå i viloläge."
            ),
            "sched_voice_cancelled": "Timer avbruten",
            "sched_caffeinate_failed": "caffeinate kunde inte startas:\n{}",
            "sched_target_required": "Välj ett mål.",
            "sched_tooltip_active": "Timer körs – klicka för att avbryta",

            "status_scheduled_active": "Timer aktiv - {} återstår",
            "status_scheduled_triggered": "Timer har löpt ut - startar {}",
            "status_scheduled_cancelled": "Timer avbruten",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Timer aktiv",
            "close_blocked_text": (
                "<b>En timer körs fortfarande!</b><br><br>"
                "Schemalagd: {}<br>"
                "Återstår: <b>{}</b><br>"
                "Kl.: {}<br><br>"
                "Om du stänger nu kommer den schemalagda avstängningen "
                "<b>inte längre att utföras</b>."
            ),
            "close_blocked_yes": "Stäng ändå",
            "close_blocked_no": "Låt appen fortsätta köra",
            "close_blocked_cancel_text": (
                "En timer körs fortfarande.\n\n"
                "Vill du verkligen stänga appen?\n"
                "(Den schemalagda avstängningen förkastas då.)"
            ),
            "close_blocked_log_aborted": "Stängning avbruten (timer aktiv)",
            "close_blocked_log_discarded": (
                "Appen stängs trots aktiv timer – timern förkastad"
            ),
            "close_blocked_log_cancel_aborted": (
                "Appstängning avbruten via Avbryt-knappen"
            ),
            "duration_day": "dag",
            "duration_days": "dagar",
            "duration_hour": "timme",
            "duration_hours": "timmar",
            "duration_minute": "minut",
            "duration_minutes": "minuter",
            "duration_connector_and": "och",
            "tooltip_pause_timer": "Pausa / återuppta timer",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Timer pausad – {} sekunder kvar",
            "timer_resumed": "Timer återupptagen",
            "say_timer_paused": "Timer pausad",
            "say_timer_resumed": "Timer återupptagen",
            "tooltip_pause_timer": "Pausa/återuppta timer",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Taluppläsning aktiverad",
            "speech_enabled_hint": (
                "Läser upp statusmeddelanden, volymbekräftelser och "
                "timerinformation via macOS taluppläsning. När den är "
                "inaktiverad körs appen tyst."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "För schemalagd avstängning av Macen krävs "
                "administratörslösenordet.\n\n"
                "Det lagras säkert i macOS-nyckelringen och används bara "
                "vid avstängning.\n\n"
                "Ställa in nu?"
            ),
            "mac_pw_dialog_title": "Administratörslösenord",
            "mac_pw_dialog_message": (
                "För avstängning av Macen krävs administratörslösenordet.\n\n"
                "Det lagras säkert i macOS-nyckelringen och används bara "
                "vid avstängning."
            ),
            "mac_pw_wrong_password": (
                "Lösenordet är felaktigt.\n\n"
                "Försök igen."
            ),
            "mac_pw_test_failed": (
                "Fel vid lösenordskontroll:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Timern startades inte eftersom "
                "lösenordsinmatningen avbröts.\n\n"
                "Utan lösenord kan Macen inte stängas av."
            ),
            "clear_password_title": "Ta bort sparat lösenord",
            "clear_password_message": (
                "Ta bort administratörslösenordet som sparats i nyckelringen?\n\n"
                "Vid nästa schemalagda avstängning kommer lösenordet "
                "att efterfrågas igen."
            ),
            "clear_password_success": "Lösenordet togs bort från nyckelringen.",
            "clear_password_failed": "Lösenordet kunde inte tas bort.",
            "clear_password_description": (
                "Tar bort administratörslösenordet som sparats i "
                "macOS-nyckelringen. Vid nästa schemalagda avstängning "
                "kommer det att efterfrågas igen."
            ),
            "clear_password_button": "Ta bort sparat lösenord",
            "shutdown_no_password_message": (
                "Macen kunde inte stängas av.\n\n"
                "Varken en NOPASSWD-sudoers-regel eller ett sparat "
                "lösenord i nyckelringen är tillgängligt.\n\n"
                "Ställ in den schemalagda avstängningen igen."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Varning",
            "warning_eject_failed_continue": (
                "Nätverksdiskar kunde inte matas ut korrekt.\n\n"
                "Om data fortfarande kopieras eller filer är öppna "
                "kan dataförlust uppstå.\n\n"
                "Fortsätta med avstängningen ändå?"
            ),
            "auto_timer_disabled_no_pw": (
                "Automatisk avstängning inaktiverad – inget "
                "administratörslösenord tillgängligt. Ange det en gång "
                "vid nästa uppmaning."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Ja",
            "btn_no": "Nej",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Stäng inte av något  (Macen hålls vaken – t.ex. för säkerhetskopieringsskript)",
            "sched_countdown_coffee_label": "⏳ caffeinate aktiv: {} kvar ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Kaffe-timern är fortfarande aktiv",
            "coffee_conflict_message": (
                "En kaffe-timer körs fortfarande:\n\n"
                "Återstår: {}\n\n"
                "Om du stänger av nu avbryts kaffe-timern "
                "och caffeinate stoppas.\n\n"
                "Stäng av ändå?"
            ),
            "shutdown_timer_conflict_title": "Avstängningstimern är fortfarande aktiv",
            "shutdown_timer_conflict_message": (
                "En avstängningstimer körs fortfarande:\n\n"
                "Schemalagd: {}\n"
                "Återstår: {}\n\n"
                "Om du stänger av manuellt nu avbryts timern "
                "och måste schemaläggas igen.\n\n"
                "Stäng av ändå?"
            ),
            "tooltip_stop_timer": "Stoppa timern helt",
            "tooltip_stop_timer_inactive": "Ingen timer aktiv",
            "timer_stopped_notice": "⏹ Timern stoppad – redo att starta om",
            "say_timer_stopped": "Timern stoppad",
            "say_timer_restarted": "Timern omstartad",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "NAS-tillverkare:",
            "vendor_tooltip": (
                "Välj tillverkare för din NAS. Bestämmer avstängningskommandon "
                "och standardökvägar. 'Automatisk identifiering' kontrollerar "
                "NAS:en via SSH."
            ),
            "vendor_auto_detect": "🔄 Automatisk identifiering",
            "vendor_auto_detect_tooltip": (
                "Identifiera tillverkaren automatiskt via SSH. "
                "Förutsättning: SSH-nyckeln och IP:t är korrekt konfigurerade."
            ),
            "vendor_detect_in_progress": "🔄 Identifierar...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Generisk Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Anpassad",
            "vendor_custom_hint": (
                "Anpassad: Justera avstängningskommandona manuellt. "
                "Standard: 'sudo shutdown -h now' (fungerar på "
                "80 % av alla Linux-NAS:er)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Tillverkare identifierad: {}",
            "vendor_detect_success_question": (
                "Tillverkare identifierad: {}\n\n"
                "Vill du använda denna tillverkare?\n"
                "(Aktuellt värde: {})"
            ),
            "vendor_detect_failed": (
                "Tillverkaren kunde inte identifieras automatiskt.\n\n"
                "Välj manuellt. De flesta Linux-NAS:er "
                "fungerar med 'Generisk Linux'."
            ),
            "vendor_detect_no_ssh": (
                "Automatisk identifiering kräver SSH-åtkomst.\n\n"
                "Kontrollera följande:\n"
                "• Sökvägen till SSH-nyckeln är korrekt\n"
                "• IP-adressen är korrekt\n"
                "• SSH är aktiverat på NAS:en\n"
                "• SSH-nyckeln är installerad på NAS:en "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Ange först SSH-nyckel och IP-adress."
            ),
            "vendor_detect_nas_offline": (
                "NAS-servern svarar inte.\n\n"
                "Kontrollera följande:\n"
                "• Är NAS:en påslagen?\n"
                "• Är IP-adressen korrekt?\n"
                "• Är NAS:en i samma nätverk?\n\n"
                "Starta NAS:en och försök igen."
            ),
            "vendor_detect_error": "Fel vid automatisk identifiering:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH-nyckeln hittades inte:\n\n{}\n\n"
                "Kontrollera sökvägen i inställningarna."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Avstängningskommando:",
            "custom_cmd_tooltip": (
                "Kommandot som skickas till NAS:en via SSH. "
                "Separera flera kommandon med semikolon."
            ),
            "custom_cmd_hint": (
                "💡 Separera flera kommandon med semikolon — "
                "det första lyckade används. "
                "Exempel: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Visa hjälp om avstängningskommandon",
            "custom_cmd_help_title": "Typiska avstängningskommandon",
            "custom_cmd_help_text": (
                "<h3>Typiska avstängningskommandon per tillverkare</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (generisk):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Flera kommandon (reservkedja)</h4>"
                "<p>Om det första kommandot misslyckas provas nästa. "
                "Separera med semikolon:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Tips:</b> Välj först det mest sannolika kommandot, "
                "sedan alternativ som reserv.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Identifierar volymer via SSH...",
            "volumes_detection_via_paths": (
                "🔍 Söker i tillverkarspecifika sökvägar..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Reserv: Söker via smbclient..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Söker efter volymer via SSH... Sökningen kan "
                "ta några sekunder."
            ),
            "volumes_detect_panel_success": (
                "{} volymer hittades — {} nya tillagda, "
                "{} redan befintliga"
            ),
            "volumes_detect_panel_partial": (
                "{} volymer hittades — alla redan i listan"
            ),
            "volumes_detect_panel_failed": (
                "Inga volymer hittades. "
                "Ange volymerna manuellt."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 Identifierar MAC-adress...",
            "mac_detect_success": "✅ MAC-adress identifierad: {}",
            "mac_detect_success_dialog": (
                "MAC-adressen identifierades framgångsrikt.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Värdet har förts in i MAC-fältet."
            ),
            "mac_detect_failed": (
                "⚠ MAC-adressen kunde inte identifieras automatiskt. "
                "Hjälp visas."
            ),
            "config_mac_find": "🔍 Hitta MAC",
            "config_mac_find_tooltip": (
                "Identifiera MAC-adressen automatiskt. "
                "Om det misslyckas visas en guide."
            ),
        },
        # "🇹🇷 Türkçe (Türkisch)
        "tr": {
            "language": "Dil:",
            "window_title": "NAS Yönetimi",
            "status_checking": "Sunucu bağlantısı kontrol ediliyor...",
            "status_online": "NAS sunucusu çevrimiçi ✓",
            "status_offline": "NAS sunucusu çevrimdışı",
            "status_settings": "Ayarlar açıldı - Zamanlayıcı durduruldu",
            "status_settings_saved": "Ayarlar kaydedildi",
            "status_settings_cancelled": "Ayarlar iptal edildi",
            "status_shutdown": "NAS ve Mac kapatılıyor...",
            "status_shutdown_nas": "NAS kapatılıyor...",
            "status_shutdown_nas_sent_mac_follows": "✅ NAS kapatma komutu gönderildi, Mac şimdi kapatılacak...",
            "status_shutdown_nas_failed_mac_still": "⚠️ NAS kapatma başarısız, Mac kapatılıyor...",
            "status_starting": "NAS Wake-on-LAN ile başlatılıyor...",
            "status_waiting": "Sunucu başlangıcı bekleniyor...",
            "status_wol_sent": "Magic Packet gönderildi",
            "status_wol_failed": "WOL başarısız",
            "status_mounting": "Seçili birimler bağlanıyor...",
            "status_mounting_volume": "{} bağlanıyor...",
            "status_mounted": "{} bağlandı ✓",
            "status_unmounting": "{} çıkarılıyor...",
            "status_unmounted": "{} çıkarıldı ✓",
            "status_error": "Hata: {} bağlanamadı",
            "status_error_unmount": "Hata: {} çıkarılamadı",
            "status_all_mounted": "Tüm birimler bağlandı ✓",
            "status_all_unmounted": "Tüm birimler çıkarıldı ✓",
            "status_mount_all": "Tüm birimler bağlanıyor...",
            "status_unmount_all": "Tüm birimler çıkarılıyor...",
            "status_shutdown_cmd": "NAS kapatma komutu gönderildi ✓",
            "status_timeout": "Zaman aşımı - Sunucu başlatılamadı",
            "status_no_volumes": "Bağlı birim yok",
            "status_mount_failed": "Bağlama başarısız",
            "status_cancelled": "İptal edildi - Uygulama kapatılıyor",
            "status_esc": "ESC tuşuna basıldı - Uygulama kapatılıyor",
            "status_server_online": "Sunucu çevrimiçi - SMB hizmeti bekleniyor...",
            "status_profile_changed": "Profile geçildi: {}",
            "status_switching": "Profile geçiliyor: {}...",
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "İptal",
            "btn_start_nas": "NAS'ı Başlat",
            "btn_settings": "Ayarlar (Cmd+E)",
            "btn_select_all": "Tümü",
            "btn_save": "Kaydet",
            "btn_reset": "Sıfırla",
            "btn_info": "ℹ",
            "btn_profile": "Profiller",
            "tooltip_shutdown_both": "Mac ve NAS'ı 2 dakika içinde kapatır",
            "tooltip_shutdown_nas": "Yalnızca NAS'ı kapatır",
            "tooltip_cancel": "Uygulamayı kapatır",
            "tooltip_start_nas": "NAS'ı Wake-on-LAN ile başlatır",
            "tooltip_settings": "Ayarlar (Cmd+E)",
            "timer_shutdown": "Otomatik kapatma {} saniye içinde - ENTER yalnızca NAS için",
            "timer_start": "Otomatik başlatma {} saniye içinde - ENTER hemen başlatmak için",
            "volumes_title": "Kullanılabilir Birimler",
            "volumes_title_offline": "Başlangıçta birimleri bağla",
            "volumes_hint": "Not: Listedeki ilk birim otomatik olarak ana birim olarak kabul edilir ve devre dışı bırakılamaz.",
            "volumes_mount_tooltip": "Sunucu başlatıldığında otomatik olarak bağlanır",
            "config_title": "AnyNasPy - Ayarlar",
            "config_tab_profiles": "Sunucu Profilleri",
            "config_tab_general": "Genel",
            "config_tab_volumes": "Birimler",
            "config_tab_timing": "Zaman Ayarları",
            "config_language": "Dil:",
            "config_nas_group": "NAS Sunucu Ayarları",
            "config_nas_user": "Kullanıcı adı:",
            "config_nas_dns": "DNS adı:",
            "config_nas_ip": "IP adresi:",
            "config_nas_mac": "MAC adresi:",
            "config_ssh_key": "SSH Anahtar Yolu:",
            "config_volumes_group": "Birimler",
            "config_volumes_label": "Birimler (her satırda bir ad):",
            "config_time_group": "Zaman Ayarları (saniye)",
            "config_auto_shutdown": "Otomatik kapatma gecikmesi:",
            "config_auto_start": "Otomatik başlatma gecikmesi:",
            "config_wol_wait": "WOL bekleme süresi (maks):",
            "config_smb_wait": "SMB bekleme süresi:",
            "config_mount_retries": "Bağlama deneme sayısı:",
            "config_status_file": "Durum dosyası",
            "config_json_path": "JSON yapılandırma dosyası:",
            "config_profile_name": "Profil adı:",
            "config_profile_active": "Aktif profil",
            "config_profile_set_active": "Aktif profil olarak ayarla",
            "config_profile_list": "Mevcut profiller:",
            "config_profile_new": "Yeni profil",
            "config_profile_delete": "Profili sil",
            "config_profile_duplicate": "Profili kopyala",
            "config_profile_rename": "Yeniden adlandır",
            "config_profile_required": "Profil adı gereklidir.",
            "config_profile_exists": "Bu ada sahip bir profil zaten var.",
            "config_profile_deleted": "'{}' profili silindi.",
            "config_profile_duplicated": "'{}' profili '{}' olarak kopyalandı.",
            "config_profile_renamed": "Profil '{}' olarak yeniden adlandırıldı.",
            "config_profile_activated": "'{}' profili artık aktif.",
            "config_find_ip": "🔍 IP bul",
            "config_find_ip_tooltip": "Sunucu IP'sini ağda otomatik olarak bul",
            "config_ssh_help": "? Yardım",
            "config_mac_help": "? Yardım",
            "config_mac_help_tooltip": "MAC adresini bulmak için talimatlar",
            "msg_ip_found": "Sunucu IP'si başarıyla bulundu:\n\n{}\n\nIP alana girildi.",
            "msg_ip_not_found": "Sunucu IP'si otomatik olarak bulunamadı.\n\nLütfen IP adresini manuel olarak girin.\n\nİpuçları:\n• Ayarlardaki DNS adını kontrol edin\n• NAS'ın açık olduğundan emin olun\n• IP'yi DSM arayüzünde 'Sistem > Ağ' bölümünde bulabilirsiniz",
            "msg_reset_confirm": "Tüm ayarlar varsayılan değerlere sıfırlansın mı?",
            "msg_reset_title": "Sıfırla",
            "msg_reset_done": "Tüm ayarlar varsayılan değerlere sıfırlandı.",
            "msg_delete_confirm": "'{}' profili gerçekten silinsin mi?",
            "msg_delete_title": "Profili sil",
            "msg_no_active_profile": "Aktif profil seçilmedi.",
            "info_title": "AnyNasPy Hakkında",
            "info_version": "Sürüm",
            "info_copyright": "Telif hakkı",
            "info_license": "Lisans",
            "info_impressum": "Künye",
            "info_developer": "Geliştirici",
            "info_contact": "İletişim",
            "info_license_text": "MIT Lisansı",
            "say_timer_shutdown": "Mac ve NAS otomatik kapatma {} saniye içinde - Enter yalnızca NAS için - Escape iptal etmek için",
            "say_timer_start": "NAS sunucusu {} saniye içinde başlatılacak - Enter hemen başlatmak için",
            "say_server_online": "NAS sunucusuna erişilebilir",
            "say_server_offline": "NAS sunucusu çevrimdışı",
            "say_shutdown_started": "Kapatma başlatıldı",
            "say_nas_shutdown": "NAS kapatılıyor",
            "say_starting_nas": "NAS başlatılıyor",
            "say_cancelled": "İptal edildi",
            "say_waiting_server": "Sunucu başlangıcı bekleniyor",
            "say_wol_failed": "Gönderme hatası",
            "say_server_reachable": "Sunucuya erişilebilir",
            "say_mount_volume": "{} hazır",
            "say_unmount_volume": "{} çıkarılıyor",
            "say_mount_all": "Tüm birimler bağlanıyor",
            "say_unmount_all": "Tüm birimler çıkarılıyor",
            "say_mount_error": "Bağlama hatası",
            "say_unmount_error": "Çıkarma hatası",
            "say_mount_failed": "Hiçbir birim bağlanmadı",
            "say_settings_opened": "Ayarlar açıldı",
            "say_settings_saved": "Ayarlar kaydedildi",
            "say_settings_cancelled": "Ayarlar iptal edildi",
            "say_workaround_deleted": "Geçici çözüm dosyası silindi",
            "say_server_timeout": "Sunucu başlatma zaman aşımı",
            "say_profile_changed": "Profile geçildi: {}",
            "ssh_key_create_title": "SSH Anahtarı Oluştur",
            "ssh_key_create_question": "Yeni bir SSH anahtar çifti oluşturmak ister misiniz?",
            "ssh_key_create_existing": "'{}' SSH anahtarı zaten mevcut.\nÜzerine yazmak ister misiniz?",
            "ssh_key_create_comment": "SSH anahtarı için yorum (isteğe bağlı):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "SSH anahtarı oluşturuldu: {}",
            "ssh_key_create_error": "SSH anahtarı oluşturulurken hata",
            "ssh_key_create_timeout": "Anahtar oluşturma zaman aşımı",
            "ssh_key_create_failed": "ssh-keygen hata döndürdü:\n{}",
            "ssh_key_create_passphrase": "SSH anahtarı için parola (parola yoksa boş bırakın):",
            "ssh_key_create_passphrase_confirm": "Parolayı onaylayın:",
            "ssh_key_create_passphrase_mismatch": "Parolalar eşleşmiyor.",
            "ssh_key_create_info": "✅ SSH anahtar çifti başarıyla oluşturuldu:\n\n"
            "📁 Özel anahtar: {}\n"
            "📁 Genel anahtar: {}\n\n"
            "📋 Kopyalamak için genel anahtar:\n"
            "{}\n\n"
            "🔑 Anahtarı NAS'ınıza nasıl kurarsınız:\n"
            "1. Genel anahtarı (yukarıdaki) kopyalayın\n"
            "2. Dosyaya yapıştırın:\n"
            "   ~/.ssh/authorized_keys NAS üzerinde\n"
            "3. Veya şunu kullanın:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Lütfen başka bir dosya adı girin:",
            "ssh_key_exists_also": "'{}' anahtarı da mevcut.\nLütfen önce silin veya başka bir ad seçin.",
            "ssh_key_passphrase_title": "Parola",
            "ssh_key_passphrase_question": "SSH anahtarı için parola kullanmak ister misiniz?\n\nParolasız: Otomatik bağlantı mümkün, daha az güvenli.\nParolalı: Daha güvenli, ancak her bağlantıda sorulur.",
            "ssh_key_passphrase_enter": "Parola girin",
            "ssh_key_passphrase_label": "SSH anahtarı için parola (en az 4 karakter):",
            "ssh_key_passphrase_none": "Parola yok",
            "ssh_key_passphrase_none_question": "Parola girmediniz.\nAnahtarı parolasız oluşturmak ister misiniz?",
            "ssh_key_passphrase_short": "Parola çok kısa",
            "ssh_key_passphrase_short_message": "Parola en az 4 karakter olmalıdır.",
            "ssh_key_passphrase_confirm": "Parolayı onaylayın",
            "ssh_key_passphrase_confirm_label": "Parolayı tekrar girin:",
            "ssh_key_passphrase_mismatch_title": "Parola hatası",
            "ssh_key_passphrase_mismatch_message": "Parolalar eşleşmiyor.",
            "config_ssh_open": "Aç",
            "config_ssh_open_tooltip": "SSH anahtarı seç veya klasörü aç",
            "config_ssh_create": "Oluştur",
            "config_ssh_create_tooltip": "Yeni SSH anahtar çifti oluştur",
            "config_ssh_help_tooltip": "SSH anahtarı hakkında yardım göster",
            "config_ssh_select": "SSH anahtarı seç",
            "config_json_open": "Aç",
            "config_json_open_tooltip": "JSON yapılandırma klasörünü aç",
            "config_error": "Hata",
            "config_shutdown_mac_delay": "NAS ve Mac kapatma arasındaki bekleme süresi:",
            "info_third_party": "Üçüncü taraf kütüphaneler",
            "info_pyqt5_license": "Bu uygulama, GNU General Public License v3 (GPLv3) ile lisanslanmış PyQt5'i kullanır.\nTelif hakkı (c) Riverbank Computing Limited.\n\nLisans metninin tamamına https://www.gnu.org/licenses/gpl-3.0.html adresinden ulaşılabilir.",
            "volumes_auto_detect": "Birimleri algıla",
            "volumes_add": "Ekle",
            "volumes_delete": "Sil",
            "volumes_move_up": "Yukarı taşı",
            "volumes_move_down": "Aşağı taşı",
            "volumes_available": "Mevcut birimler:",
            "volumes_no_volumes": "Birim bulunamadı.",
            "volumes_detection_failed": "Birim algılama hatası.",
            "volumes_detection_success": "Birimler başarıyla algılandı.",
            "volumes_confirm_delete": "'{}' birimini gerçekten silmek istiyor musunuz?",
            "volumes_enter_name": "Lütfen yeni birimin adını girin:",
            "volumes_name_exists": "Bu ada sahip bir birim zaten mevcut.",
            "msg_invalid_ip": "Girilen IP adresi geçerli değil.\nLütfen geçerli bir IPv4 adresi girin (ör. 192.168.1.100).",
            "msg_select_volume": "Lütfen bir birim seçin.",
            "msg_cannot_delete_main_volume": "İlk birim (ana birim) silinemez.",
            "profile_cannot_delete_last": "Son profil silinemez.",
            "status_wol_sending": "Sihirli paket gönderiliyor...",
            "status_wol_method_failed": "Python yöntemi başarısız, sonrakine geçiliyor...",
            "status_trying_wakeonlan": "wakeonlan deneniyor...",
            "status_trying_etherwake": "etherwake deneniyor...",
            "ssh_key_system_key_warning": "Güvenlik uyarısı",
            "ssh_key_system_key_message": "'{}' adı bir sistem anahtarıdır ve üzerine yazılmayacaktır.\nLütfen başka bir ad seçin (ör. synaspy_rsa).",
            "profile_name_exists": "'{}' adında bir profil zaten mevcut.",
            "config_profile_created": "'{}' profili oluşturuldu.",
            "config_profile_create_failed": "Profil oluşturulamadı.",
            "config_profile_rename_failed": "Yeniden adlandırma başarısız.",
            "config_profile_duplicate_name": "Kopyalanan profil için ad:",
            "config_profile_duplicate_failed": "Kopyalama başarısız.",
            "config_profile_delete_failed": "Silme başarısız.",
            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Yalnızca Mac'i kapatır (NAS açık kalır, WOL yok)",
            "status_shutdown_mac_only": "Yalnızca Mac kapatılıyor...",
            "say_shutdown_mac_only": "Mac kapatılıyor, NAS açık kalıyor",

            "btn_scheduled_shutdown": "🕐 Zamanlanmış kapatma",
            "tooltip_scheduled_shutdown": "Kullanıcının seçtiği süre sonunda kapatır",
            "btn_scheduled_shutdown_offline": "🕐 Mac'i zamanlanmış olarak kapat",
            "tooltip_scheduled_shutdown_offline": "Seçilen süre sonunda yalnızca Mac'i kapatır (NAS çevrimdışı)",
            "btn_cancel_scheduled": "⏹ Geri sayımı iptal et",
            "tooltip_cancel_scheduled": "Etkin geri sayımı iptal eder",

            "sched_dialog_title": "Zamanlanmış Kapatma",
            "sched_target_label": "Hedef:",
            "sched_target_both": "🖥️ Mac + NAS  (tamamen kapat)",
            "sched_target_nas": "🗄️ Yalnızca NAS  (Mac açık kalır)",
            "sched_target_mac": "💻 Yalnızca Mac  (NAS açık kalır)",

            "sched_wait_label": "Kapatmaya kadar bekleme süresi:",
            "sched_hours": "Saat",
            "sched_minutes": "Dakika",

            "sched_caffeinate_label": "caffeinate seçeneği (Mac'i uyanık tutar):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Önerilen: Sistem uyanık, ekran kararabilir  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Yalnızca boşta ve diski engelle (ekran açık kalır)  (-i -m)",
            "sched_caffeinate_d": "Ekran ayrıca açık kalır  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Kullanıcı etkinliğini simüle et (ekran parlak, sistem uyanık)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Maksimum: Ekran + sistem + disk sürekli uyanık  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Kapalı (normal enerji tasarrufu – sistem uyuyabilir)",

            "sched_caffeinate_hint": (
                "💡 Öğrenme Notu: caffeinate bayraklarını doğrudan terminalde kullan:\n"
                "   -i  sistemin boşta uyumasını engeller\n"
                "   -m  disk uykusunu engeller (sabit disk uyumaz)\n"
                "   -s  sistem uykusunu engeller (yalnızca güç adaptöründe)\n"
                "   -d  ekran uykusunu engeller (ekran açık kalır)\n"
                "   -u  kullanıcı etkinliğini simüle eder (ekran parlak kalır)\n"
                "   -w PID  PID süreci sona erdiğinde caffeinate'i sonlandırır\n"
                "Örnek:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Kapatma planlandı: {}",
            "sched_countdown_label": "Geri sayım: {} kapatmaya kadar ({})",
            "sched_started": "Zamanlayıcı başlatıldı.\n\nHedef: {}\nSüre: {}\nBitiş: {}",
            "sched_cancelled": "Zamanlayıcı iptal edildi",
            "sched_already_active": "Zaten bir zamanlayıcı çalışıyor. Önce iptal edilsin mi?",
            "sched_invalid_time": "Lütfen geçerli bir süre girin (en az 1 dakika).",
            "sched_max_time": "En fazla 720 saat (30 gün) izin verilir.",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Zamanlayıcı başlatıldı. Mac ve NAS {} sonra kapatılacak."
            ),
            "sched_voice_started_nas": (
                "Zamanlayıcı başlatıldı. Yalnızca NAS {} sonra kapatılacak. "
                "Mac açık kalır."
            ),
            "sched_voice_started_mac": (
                "Zamanlayıcı başlatıldı. Yalnızca Mac {} sonra kapatılacak. "
                "NAS açık kalır."
            ),
            "sched_voice_started_nothing": (
                "Zamanlayıcı başlatıldı. Süre dolduğunda hiçbir şey yapılmayacak. "
                "caffeinate o zamana kadar etkin kalır."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Mac {} boyunca uyanık kalır. "
                "Ekran kararabilir. "
                "Süre dolduğunda hiçbir şey yapılmayacak."
            ),
            "sched_voice_nothing_im": (
                "Mac {} boyunca uyanık kalır. "
                "Ekran açık kalır. "
                "Süre dolduğunda hiçbir şey yapılmayacak."
            ),
            "sched_voice_nothing_d": (
                "Mac ve ekran {} boyunca açık kalır. "
                "Süre dolduğunda hiçbir şey yapılmayacak."
            ),
            "sched_voice_nothing_u": (
                "Mac {} boyunca etkin kalır. "
                "Ekran parlak kalır. "
                "Süre dolduğunda hiçbir şey yapılmayacak."
            ),
            "sched_voice_nothing_full": (
                "Mac {} boyunca tamamen etkin kalır – ekran ve sistem sürekli uyanık. "
                "Süre dolduğunda hiçbir şey yapılmayacak."
            ),
            "sched_voice_nothing_off": (
                "Zamanlayıcı {} boyunca çalışır. "
                "Süre dolduğunda hiçbir şey yapılmayacak. "
                "Dikkat: Mac uyku moduna geçebilir."
            ),
            "sched_voice_cancelled": "Zamanlayıcı iptal edildi",
            "sched_caffeinate_failed": "caffeinate başlatılamadı:\n{}",
            "sched_target_required": "Lütfen bir hedef seçin.",
            "sched_tooltip_active": "Zamanlayıcı çalışıyor – iptal etmek için tıkla",

            "status_scheduled_active": "Zamanlayıcı etkin - {} kaldı",
            "status_scheduled_triggered": "Zamanlayıcı doldu - {} başlatılıyor",
            "status_scheduled_cancelled": "Zamanlayıcı iptal edildi",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Zamanlayıcı etkin",
            "close_blocked_text": (
                "<b>Hâlâ bir zamanlayıcı çalışıyor!</b><br><br>"
                "Planlandı: {}<br>"
                "Kalan: <b>{}</b><br>"
                "Zaman: {}<br><br>"
                "Şimdi kapatırsan, planlanan kapatma "
                "<b>artık yürütülmeyecek</b>."
            ),
            "close_blocked_yes": "Yine de kapat",
            "close_blocked_no": "Uygulamayı çalışmaya devam ettir",
            "close_blocked_cancel_text": (
                "Hâlâ bir zamanlayıcı çalışıyor.\n\n"
                "Uygulamayı gerçekten kapatmak istiyor musun?\n"
                "(Planlanan kapatma o zaman iptal edilir.)"
            ),
            "close_blocked_log_aborted": "Kapatma iptal edildi (zamanlayıcı etkin)",
            "close_blocked_log_discarded": (
                "Uygulama etkin zamanlayıcıya rağmen kapatılıyor – zamanlayıcı iptal edildi"
            ),
            "close_blocked_log_cancel_aborted": (
                "Uygulama kapatma, İptal düğmesiyle iptal edildi"
            ),
            "duration_day": "gün",
            "duration_days": "gün",
            "duration_hour": "saat",
            "duration_hours": "saat",
            "duration_minute": "dakika",
            "duration_minutes": "dakika",
            "duration_connector_and": "ve",
            "tooltip_pause_timer": "Zamanlayıcıyı duraklat / devam ettir",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Zamanlayıcı duraklatıldı – {} saniye kaldı",
            "timer_resumed": "Zamanlayıcı devam ettirildi",
            "say_timer_paused": "Zamanlayıcı duraklatıldı",
            "say_timer_resumed": "Zamanlayıcı devam ettirildi",
            "tooltip_pause_timer": "Zamanlayıcıyı duraklat/devam ettir",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Sesli çıkış etkinleştirildi",
            "speech_enabled_hint": (
                "Durum mesajlarını, ses düzeyi onaylarını ve zamanlayıcı "
                "bilgilerini macOS sesli çıkışı aracılığıyla seslendirir. "
                "Devre dışı bırakıldığında uygulama sessiz çalışır."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Mac'in zamanlanmış olarak kapatılması için "
                "yönetici parolası gereklidir.\n\n"
                "macOS Anahtar Zincirinde güvenli bir şekilde saklanır ve "
                "yalnızca kapatma sırasında kullanılır.\n\n"
                "Şimdi ayarlansın mı?"
            ),
            "mac_pw_dialog_title": "Yönetici parolası",
            "mac_pw_dialog_message": (
                "Mac'in kapatılması için yönetici parolası gereklidir.\n\n"
                "macOS Anahtar Zincirinde güvenli bir şekilde saklanır ve "
                "yalnızca kapatma sırasında kullanılır."
            ),
            "mac_pw_wrong_password": (
                "Parola yanlış.\n\n"
                "Lütfen tekrar deneyin."
            ),
            "mac_pw_test_failed": (
                "Parola kontrolünde hata:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Zamanlayıcı başlatılamadı çünkü parola "
                "girişi iptal edildi.\n\n"
                "Parola olmadan Mac kapatılamaz."
            ),
            "clear_password_title": "Kayıtlı parolayı sil",
            "clear_password_message": (
                "Anahtar Zincirinde saklanan yönetici parolası silinsin mi?\n\n"
                "Bir sonraki zamanlanmış kapatmada parola "
                "tekrar sorulacaktır."
            ),
            "clear_password_success": "Parola Anahtar Zincirinden kaldırıldı.",
            "clear_password_failed": "Parola silinemedi.",
            "clear_password_description": (
                "macOS Anahtar Zincirinde saklanan yönetici parolasını "
                "kaldırır. Bir sonraki zamanlanmış kapatmada "
                "tekrar sorulacaktır."
            ),
            "clear_password_button": "Kayıtlı parolayı sil",
            "shutdown_no_password_message": (
                "Mac kapatılamadı.\n\n"
                "Ne sudoers'da bir NOPASSWD kuralı ne de Anahtar Zincirinde "
                "kayıtlı bir parola mevcut.\n\n"
                "Lütfen zamanlanmış kapatmayı yeniden ayarlayın."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Uyarı",
            "warning_eject_failed_continue": (
                "Ağ sürücüleri düzgün bir şekilde çıkarılamadı.\n\n"
                "Veriler hâlâ kopyalanıyorsa veya dosyalar açıksa "
                "veri kaybı meydana gelebilir.\n\n"
                "Yine de kapatmaya devam edilsin mi?"
            ),
            "auto_timer_disabled_no_pw": (
                "Otomatik kapatma devre dışı bırakıldı – yönetici parolası "
                "mevcut değil. Lütfen bir sonraki istemde bir kez girin."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Evet",
            "btn_no": "Hayır",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Hiçbir şeyi kapatma  (Mac uyanık kalır – örn. yedekleme betikleri için)",
            "sched_countdown_coffee_label": "⏳ caffeinate etkin: {} kaldı ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Kahve zamanlayıcısı hâlâ çalışıyor",
            "coffee_conflict_message": (
                "Bir kahve zamanlayıcısı hâlâ çalışıyor:\n\n"
                "Kalan: {}\n\n"
                "Şimdi kapatırsan, kahve zamanlayıcısı iptal edilir "
                "ve caffeinate durdurulur.\n\n"
                "Yine de kapatılsın mı?"
            ),
            "shutdown_timer_conflict_title": "Kapatma zamanlayıcısı hâlâ çalışıyor",
            "shutdown_timer_conflict_message": (
                "Bir kapatma zamanlayıcısı hâlâ çalışıyor:\n\n"
                "Planlanan: {}\n"
                "Kalan: {}\n\n"
                "Şimdi manuel olarak kapatırsan, zamanlayıcı iptal edilir "
                "ve yeniden planlanması gerekir.\n\n"
                "Yine de kapatılsın mı?"
            ),
            "tooltip_stop_timer": "Zamanlayıcıyı tamamen durdur",
            "tooltip_stop_timer_inactive": "Aktif zamanlayıcı yok",
            "timer_stopped_notice": "⏹ Zamanlayıcı durduruldu – yeniden başlatmaya hazır",
            "say_timer_stopped": "Zamanlayıcı durduruldu",
            "say_timer_restarted": "Zamanlayıcı yeniden başlatıldı",
            # ═══════════════════════════════════════════════════════════
            # Version 2.3.0 — Universal für alle Hersteller
            # ═══════════════════════════════════════════════════════════

            # ─── NAS-Hersteller ───
            "vendor_label": "NAS üreticisi:",
            "vendor_tooltip": (
                "NAS üreticinizi seçin. Kapatma komutlarını ve varsayılan "
                "yolları belirler. 'Otomatik algıla' NAS'ı SSH üzerinden "
                "kontrol eder."
            ),
            "vendor_auto_detect": "🔄 Otomatik algıla",
            "vendor_auto_detect_tooltip": (
                "Üreticiyi SSH üzerinden otomatik algıla. "
                "Ön koşul: SSH anahtarı ve IP doğru yapılandırılmış olmalı."
            ),
            "vendor_detect_in_progress": "🔄 Algılanıyor...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Genel Linux",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Özel",
            "vendor_custom_hint": (
                "Özel: Kapatma komutlarını manuel olarak uyarlayın. "
                "Varsayılan: 'sudo shutdown -h now' (tüm Linux NAS'ların "
                "%80'inde çalışır)."
            ),

            # ─── Hersteller-Erkennung (Statusmeldungen) ───
            "vendor_detect_success": "Üretici algılandı: {}",
            "vendor_detect_success_question": (
                "Üretici algılandı: {}\n\n"
                "Bu üretici kullanılsın mı?\n"
                "(Mevcut değer: {})"
            ),
            "vendor_detect_failed": (
                "Üretici otomatik olarak algılanamadı.\n\n"
                "Lütfen manuel olarak seçin. Çoğu Linux NAS "
                "'Genel Linux' ile çalışır."
            ),
            "vendor_detect_no_ssh": (
                "Otomatik algılama SSH erişimi gerektirir.\n\n"
                "Lütfen kontrol edin:\n"
                "• SSH anahtar yolu doğru\n"
                "• IP adresi doğru\n"
                "• NAS'ta SSH etkin\n"
                "• SSH anahtarı NAS'a kurulu "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Lütfen önce SSH anahtarını ve IP adresini girin."
            ),
            "vendor_detect_nas_offline": (
                "NAS sunucusu yanıt vermiyor.\n\n"
                "Lütfen kontrol edin:\n"
                "• NAS açık mı?\n"
                "• IP adresi doğru mu?\n"
                "• NAS aynı ağda mı?\n\n"
                "NAS'ı açın ve tekrar deneyin."
            ),
            "vendor_detect_error": "Otomatik algılamada hata:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "SSH anahtarı bulunamadı:\n\n{}\n\n"
                "Lütfen ayarlardaki yolu kontrol edin."
            ),

            # ─── Benutzerdefinierter Shutdown-Befehl ───
            "custom_cmd_label": "Kapatma komutu:",
            "custom_cmd_tooltip": (
                "NAS'a SSH üzerinden gönderilen komut. "
                "Birden fazla komutu noktalı virgülle ayırın."
            ),
            "custom_cmd_hint": (
                "💡 Birden fazla komutu noktalı virgülle ayırın — "
                "ilk başarılı olan kullanılır. "
                "Örnek: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Kapatma komutları hakkında yardım göster",
            "custom_cmd_help_title": "Tipik kapatma komutları",
            "custom_cmd_help_text": (
                "<h3>Üreticiye göre tipik kapatma komutları</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (genel):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Birden fazla komut (yedek zinciri)</h4>"
                "<p>İlk komut başarısız olursa bir sonraki denenir. "
                "Noktalı virgülle ayırma:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>İpucu:</b> Önce en olası komutu seçin, "
                "sonra alternatifleri yedek olarak ekleyin.</p>"
            ),

            # ─── Volume-Erkennung ───
            "volumes_detection_in_progress": "🔄 Birimler SSH üzerinden algılanıyor...",
            "volumes_detection_via_paths": (
                "🔍 Üreticiye özel yollarda aranıyor..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Yedek: smbclient üzerinden aranıyor..."
            ),

            # ─── Volume-Erkennungs-Panel ───
            "volumes_detect_panel_running": (
                "🔍 Birimler SSH üzerinden aranıyor... Arama "
                "birkaç saniye sürebilir."
            ),
            "volumes_detect_panel_success": (
                "{} birim bulundu — {} yeni eklendi, "
                "{} zaten mevcut"
            ),
            "volumes_detect_panel_partial": (
                "{} birim bulundu — hepsi zaten listede"
            ),
            "volumes_detect_panel_failed": (
                "Hiçbir birim bulunamadı. "
                "Lütfen birimleri manuel olarak girin."
            ),

            # ─── MAC-Adresserkennung ───
            "mac_detect_in_progress": "🔄 MAC adresi algılanıyor...",
            "mac_detect_success": "✅ MAC adresi algılandı: {}",
            "mac_detect_success_dialog": (
                "MAC adresi başarıyla algılandı.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Değer MAC alanına girildi."
            ),
            "mac_detect_failed": (
                "⚠ MAC adresi otomatik olarak algılanamadı. "
                "Yardım gösterilecek."
            ),
            "config_mac_find": "🔍 MAC bul",
            "config_mac_find_tooltip": (
                "MAC adresini otomatik algıla. "
                "Başarısız olursa bir kılavuz gösterilir."
            ),
        },
        # "🇻🇳 Tiếng Việt"
        "vi": {
            # Main window
            "window_title": "Quản lý NAS",
            "status_checking": "Đang kiểm tra kết nối máy chủ...",
            "status_online": "Máy chủ NAS đang trực tuyến ✓",
            "status_offline": "Máy chủ NAS đang ngoại tuyến",
            "status_settings": "Đã mở cài đặt - Đã dừng hẹn giờ",
            "status_settings_saved": "Đã lưu cài đặt",
            "status_settings_cancelled": "Đã hủy cài đặt",
            "status_shutdown": "Đang tắt NAS và Mac...",
            "status_shutdown_nas": "Đang tắt NAS...",
            "status_shutdown_nas_sent_mac_follows": "✅ Đã gửi lệnh tắt NAS, Mac sẽ tắt ngay bây giờ...",
            "status_shutdown_nas_failed_mac_still": "⚠️ Lệnh tắt NAS thất bại, vẫn tắt Mac...",
            "status_starting": "Đang khởi động NAS qua Wake-on-LAN...",
            "status_waiting": "Đang đợi máy chủ khởi động...",
            "status_wol_sent": "Đã gửi Magic Packet",
            "status_wol_failed": "WOL thất bại",
            "status_mounting": "Đang gắn kết các volume đã chọn...",
            "status_mounting_volume": "Đang gắn kết {}...",
            "status_mounted": "{} đã được gắn kết ✓",
            "status_unmounting": "Đang ngắt kết nối {}...",
            "status_unmounted": "{} đã được ngắt kết nối ✓",
            "status_error": "Lỗi: Không thể gắn kết {}",
            "status_error_unmount": "Lỗi: Không thể ngắt kết nối {}",
            "status_all_mounted": "Tất cả volume đã được gắn kết ✓",
            "status_all_unmounted": "Tất cả volume đã được ngắt kết nối ✓",
            "status_mount_all": "Đang gắn kết tất cả volume...",
            "status_unmount_all": "Đang ngắt kết nối tất cả volume...",
            "status_shutdown_cmd": "Đã gửi lệnh tắt NAS ✓",
            "status_timeout": "Hết thời gian chờ - Không thể khởi động máy chủ",
            "status_no_volumes": "Không có volume nào được gắn kết",
            "status_mount_failed": "Gắn kết thất bại",
            "status_cancelled": "Đã hủy - Ứng dụng sẽ đóng",
            "status_esc": "Đã nhấn ESC - Ứng dụng sẽ đóng",
            "status_server_online": "Máy chủ trực tuyến - đang đợi dịch vụ SMB...",
            "status_profile_changed": "Đã chuyển sang hồ sơ: {}",
            "status_switching": "Đang chuyển sang hồ sơ: {}...",
            # Buttons
            "btn_shutdown_both": "Mac + NAS",
            "btn_shutdown_nas": "NAS",
            "btn_cancel": "Hủy",
            "btn_start_nas": "Khởi động NAS",
            "btn_settings": "Cài đặt (Cmd+E)",
            "btn_select_all": "Tất cả",
            "btn_save": "Lưu",
            "btn_reset": "Đặt lại",
            "btn_info": "ℹ",
            "btn_profile": "Hồ sơ",
            # Tooltips
            "tooltip_shutdown_both": "Tắt Mac và NAS trong 2 phút",
            "tooltip_shutdown_nas": "Chỉ tắt NAS",
            "tooltip_cancel": "Đóng ứng dụng",
            "tooltip_start_nas": "Khởi động NAS qua Wake-on-LAN",
            "tooltip_settings": "Cài đặt (Cmd+E)",
            # Timer
            "timer_shutdown": "Tự động tắt trong {} giây - ENTER để chỉ tắt NAS",
            "timer_start": "Tự động khởi động trong {} giây - ENTER để khởi động ngay",
            # Volumes
            "volumes_title": "Các Volume khả dụng",
            "volumes_title_offline": "Volume sẽ gắn kết khi khởi động",
            "volumes_hint": "Gợi ý: Volume đầu tiên trong danh sách được tự động coi là volume chính và không thể bỏ chọn.",
            "volumes_mount_tooltip": "Sẽ được tự động gắn kết khi máy chủ khởi động",
            # Config Dialog
            "config_title": "AnyNasPy - Cài đặt",
            "config_tab_profiles": "Hồ sơ máy chủ",
            "config_tab_general": "Tổng quan",
            "config_tab_volumes": "Volumes",
            "config_tab_timing": "Thời gian",
            "config_language": "Ngôn ngữ:",
            "config_nas_group": "Cài đặt máy chủ NAS",
            "config_nas_user": "Tên người dùng:",
            "config_nas_dns": "Tên DNS:",
            "config_nas_ip": "Địa chỉ IP:",
            "config_nas_mac": "Địa chỉ MAC:",
            "config_ssh_key": "Đường dẫn SSH Key:",
            "config_volumes_group": "Volumes",
            "config_volumes_label": "Volumes (một tên mỗi dòng):",
            "config_time_group": "Cài đặt thời gian (giây)",
            "config_auto_shutdown": "Độ trễ tự động tắt:",
            "config_auto_start": "Độ trễ tự động khởi động:",
            "config_wol_wait": "Thời gian đợi WOL (tối đa):",
            "config_smb_wait": "Thời gian đợi SMB:",
            "config_mount_retries": "Số lần thử gắn kết:",
            "config_status_file": "Tệp trạng thái",
            "config_json_path": "Tệp cấu hình JSON:",
            "config_profile_name": "Tên hồ sơ:",
            "config_profile_active": "Hồ sơ hoạt động",
            "config_profile_set_active": "Đặt làm hồ sơ hoạt động",
            "config_profile_list": "Hồ sơ hiện có:",
            "config_profile_new": "Hồ sơ mới",
            "config_profile_delete": "Xóa hồ sơ",
            "config_profile_duplicate": "Nhân đôi hồ sơ",
            "config_profile_rename": "Đổi tên",
            "config_profile_required": "Tên hồ sơ là bắt buộc.",
            "config_profile_exists": "Hồ sơ với tên này đã tồn tại.",
            "config_profile_deleted": "Hồ sơ '{}' đã bị xóa.",
            "config_profile_duplicated": "Hồ sơ '{}' đã được nhân đôi thành '{}'.",
            "config_profile_renamed": "Hồ sơ đã được đổi tên thành '{}'.",
            "config_profile_activated": "Hồ sơ '{}' hiện đang hoạt động.",
            # Config Buttons
            "config_find_ip": "🔍 Tìm IP",
            "config_find_ip_tooltip": "Tự động tìm IP máy chủ trong mạng",
            "config_ssh_help": "? Trợ giúp",
            "config_mac_help": "? Trợ giúp",
            "config_mac_help_tooltip": "Hướng dẫn tìm địa chỉ MAC",
            # Messages
            "msg_ip_found": "Đã tìm thấy IP máy chủ:\n\n{}\n\nIP đã được nhập vào trường.",
            "msg_ip_not_found": "Không thể tự động tìm thấy IP máy chủ.\n\nVui lòng nhập địa chỉ IP thủ công.\n\nGợi ý:\n• Kiểm tra tên DNS trong cài đặt\n• Đảm bảo NAS đã bật\n• Tìm IP trong DSM tại 'Hệ thống > Mạng'",
            "msg_reset_confirm": "Đặt lại tất cả cài đặt về giá trị mặc định?",
            "msg_reset_title": "Đặt lại",
            "msg_reset_done": "Tất cả cài đặt đã được đặt lại về giá trị mặc định.",
            "msg_delete_confirm": "Bạn có chắc chắn muốn xóa hồ sơ '{}'?",
            "msg_delete_title": "Xóa hồ sơ",
            "msg_no_active_profile": "Không có hồ sơ hoạt động nào được chọn.",
            # Info Dialog
            "info_title": "Giới thiệu về AnyNasPy",
            "info_version": "Phiên bản",
            "info_copyright": "Bản quyền",
            "info_license": "Giấy phép",
            "info_impressum": "Thông tin pháp lý",
            "info_developer": "Nhà phát triển",
            "info_contact": "Liên hệ",
            "info_license_text": "Giấy phép MIT",
            # Language selection
            "language": "Ngôn ngữ:",
            # Misc
            "say_timer_shutdown": "Tự động tắt Mac và NAS trong {} giây - Enter để chỉ tắt NAS - Escape để hủy",
            "say_timer_start": "Máy chủ NAS sẽ khởi động trong {} giây - Enter để khởi động ngay",
            "say_server_online": "Máy chủ NAS đang hoạt động",
            "say_server_offline": "Máy chủ NAS đang ngoại tuyến",
            "say_shutdown_started": "Đã bắt đầu tắt",
            "say_nas_shutdown": "NAS đang tắt",
            "say_starting_nas": "Đang khởi động NAS",
            "say_cancelled": "Đã hủy",
            "say_waiting_server": "Đang đợi máy chủ khởi động",
            "say_wol_failed": "Lỗi khi gửi",
            "say_server_reachable": "Máy chủ hoạt động",
            "say_mount_volume": "{} đã sẵn sàng",
            "say_unmount_volume": "Đang ngắt kết nối {}",
            "say_mount_all": "Đang gắn kết tất cả volume",
            "say_unmount_all": "Đang ngắt kết nối tất cả volume",
            "say_mount_error": "Lỗi khi gắn kết",
            "say_unmount_error": "Lỗi khi ngắt kết nối",
            "say_mount_failed": "Không có volume nào được gắn kết",
            "say_settings_opened": "Đã mở cài đặt",
            "say_settings_saved": "Đã lưu cài đặt",
            "say_settings_cancelled": "Đã hủy cài đặt",
            "say_workaround_deleted": "Đã xóa tệp giải pháp thay thế",
            "say_server_timeout": "Hết thời gian chờ khởi động máy chủ",
            "say_profile_changed": "Đã chuyển sang hồ sơ {}",
            "ssh_key_create_title": "Tạo SSH Key",
            "ssh_key_create_question": "Bạn có muốn tạo cặp SSH key mới không?",
            "ssh_key_create_existing": "SSH key '{}' đã tồn tại.\nBạn có muốn ghi đè không?",
            "ssh_key_create_comment": "Nhận xét cho SSH key (không bắt buộc):",
            "ssh_key_create_comment_default": "synaspy-{}",
            "ssh_key_create_success": "Đã tạo SSH key: {}",
            "ssh_key_create_error": "Lỗi khi tạo SSH key",
            "ssh_key_create_timeout": "Quá thời gian tạo SSH key",
            "ssh_key_create_failed": "ssh-keygen trả về lỗi:\n{}",
            "ssh_key_create_passphrase": "Passphrase cho SSH key (để trống nếu không muốn):",
            "ssh_key_create_passphrase_confirm": "Xác nhận passphrase:",
            "ssh_key_create_passphrase_mismatch": "Passphrases không khớp.",
            "ssh_key_create_info": "✅ Đã tạo cặp SSH key thành công:\n\n"
            "📁 Private Key: {}\n"
            "📁 Public Key: {}\n\n"
            "📋 Public Key để sao chép:\n"
            "{}\n\n"
            "🔑 Cách cài đặt key trên NAS:\n"
            "1. Sao chép public key (ở trên)\n"
            "2. Thêm vào file:\n"
            "   ~/.ssh/authorized_keys trên NAS\n"
            "3. Hoặc sử dụng:\n"
            "   ssh-copy-id {}@{}",
            "ssh_key_enter_name": "Vui lòng nhập tên tệp khác:",
            "ssh_key_exists_also": "Key '{}' cũng tồn tại.\nVui lòng xóa nó trước hoặc chọn tên khác.",
            "ssh_key_passphrase_title": "Passphrase",
            "ssh_key_passphrase_question": "Bạn có muốn sử dụng passphrase cho SSH key?\n\nKhông có passphrase: Kết nối tự động, ít bảo mật hơn.\nCó passphrase: Bảo mật hơn, nhưng yêu cầu nhập mỗi lần kết nối.",
            "ssh_key_passphrase_enter": "Nhập passphrase",
            "ssh_key_passphrase_label": "Passphrase cho SSH key (ít nhất 4 ký tự):",
            "ssh_key_passphrase_none": "Không có passphrase",
            "ssh_key_passphrase_none_question": "Bạn chưa nhập passphrase.\nBạn có muốn tạo key mà không có passphrase không?",
            "ssh_key_passphrase_short": "Passphrase quá ngắn",
            "ssh_key_passphrase_short_message": "Passphrase phải có ít nhất 4 ký tự.",
            "ssh_key_passphrase_confirm": "Xác nhận passphrase",
            "ssh_key_passphrase_confirm_label": "Nhập lại passphrase:",
            "ssh_key_passphrase_mismatch_title": "Lỗi Passphrase",
            "ssh_key_passphrase_mismatch_message": "Các passphrase không khớp.",
            "config_ssh_open": "Mở",
            "config_ssh_open_tooltip": "Chọn SSH key hoặc mở thư mục",
            "config_ssh_create": "Tạo",
            "config_ssh_create_tooltip": "Tạo cặp SSH key mới",
            "config_ssh_help_tooltip": "Hiển thị trợ giúp SSH key",
            "config_ssh_select": "Chọn SSH key",
            "config_json_open": "Mở",
            "config_json_open_tooltip": "Mở thư mục cấu hình JSON",
            "config_error": "Lỗi",
            "config_shutdown_mac_delay": "Thời gian chờ giữa tắt NAS và Mac:",
            "info_third_party": "Thư viện bên thứ ba",
            "info_pyqt5_license": "Ứng dụng này sử dụng PyQt5, được cấp phép theo GNU General Public License v3 (GPLv3).\nBản quyền (c) Riverbank Computing Limited.\n\nVăn bản giấy phép đầy đủ có thể được xem tại https://www.gnu.org/licenses/gpl-3.0.html.",
            "volumes_auto_detect": "Phát hiện ổ đĩa",
            "volumes_add": "Thêm",
            "volumes_delete": "Xóa",
            "volumes_move_up": "Di chuyển lên",
            "volumes_move_down": "Di chuyển xuống",
            "volumes_available": "Ổ đĩa có sẵn:",
            "volumes_no_volumes": "Không tìm thấy ổ đĩa nào.",
            "volumes_detection_failed": "Lỗi phát hiện ổ đĩa.",
            "volumes_detection_success": "Phát hiện ổ đĩa thành công.",
            "volumes_confirm_delete": "Xóa ổ đĩa '{}'?",
            "volumes_enter_name": "Vui lòng nhập tên ổ đĩa mới:",
            "volumes_name_exists": "Một ổ đĩa với tên này đã tồn tại.",
            "msg_invalid_ip": "Địa chỉ IP nhập vào không hợp lệ.\nVui lòng nhập địa chỉ IPv4 hợp lệ (ví dụ: 192.168.1.100).",
            "msg_select_volume": "Vui lòng chọn một ổ đĩa.",
            "msg_cannot_delete_main_volume": "Không thể xóa ổ đĩa đầu tiên (ổ đĩa chính).",
            "profile_cannot_delete_last": "Không thể xóa hồ sơ cuối cùng.",
            "status_wol_sending": "Đang gửi gói tin ma thuật...",
            "status_wol_method_failed": "Phương thức Python thất bại, thử phương thức tiếp theo...",
            "status_trying_wakeonlan": "Đang thử wakeonlan...",
            "status_trying_etherwake": "Đang thử etherwake...",
            "ssh_key_system_key_warning": "Cảnh báo bảo mật",
            "ssh_key_system_key_message": "Tên '{}' là khóa hệ thống và sẽ không bị ghi đè.\nVui lòng chọn tên khác (ví dụ: synaspy_rsa).",
            "profile_name_exists": "Hồ sơ với tên '{}' đã tồn tại.",
            "config_profile_created": "Hồ sơ '{}' đã được tạo.",
            "config_profile_create_failed": "Không thể tạo hồ sơ.",
            "config_profile_rename_failed": "Đổi tên thất bại.",
            "config_profile_duplicate_name": "Tên cho hồ sơ được sao chép:",
            "config_profile_duplicate_failed": "Sao chép thất bại.",
            "config_profile_delete_failed": "Xóa thất bại.",

            # ═══════════════════════════════════════════
            # NEU v2.2.0: Zeitgesteuertes Herunterfahren
            # ═══════════════════════════════════════════
            "btn_shutdown_mac_only": "Mac",
            "tooltip_shutdown_mac_only": "Chỉ tắt Mac (NAS vẫn bật, không WOL)",
            "status_shutdown_mac_only": "Đang chỉ tắt Mac...",
            "say_shutdown_mac_only": "Mac đang tắt, NAS vẫn bật",

            "btn_scheduled_shutdown": "🕐 Tắt theo lịch",
            "tooltip_scheduled_shutdown": "Tắt sau khoảng thời gian do người dùng chọn",
            "btn_scheduled_shutdown_offline": "🕐 Tắt Mac theo lịch",
            "tooltip_scheduled_shutdown_offline": "Chỉ tắt Mac sau khoảng thời gian đã chọn (NAS đang ngoại tuyến)",
            "btn_cancel_scheduled": "⏹ Hủy đếm ngược",
            "tooltip_cancel_scheduled": "Hủy đếm ngược đang hoạt động",

            "sched_dialog_title": "Tắt theo lịch",
            "sched_target_label": "Mục tiêu:",
            "sched_target_both": "🖥️ Mac + NAS  (tắt hoàn toàn)",
            "sched_target_nas": "🗄️ Chỉ NAS  (Mac vẫn bật)",
            "sched_target_mac": "💻 Chỉ Mac  (NAS vẫn bật)",

            "sched_wait_label": "Thời gian chờ đến khi tắt:",
            "sched_hours": "Giờ",
            "sched_minutes": "Phút",

            "sched_caffeinate_label": "Tùy chọn caffeinate (giữ Mac thức):",
            # ─── caffeinate Optionen mit Lern-Fact ───
            "sched_caffeinate_ims": "Khuyến nghị: Hệ thống thức, màn hình có thể mờ đi  (caffeinate -i -m -s)",
            "sched_caffeinate_im": "Chỉ ngăn chế độ chờ & ổ đĩa (màn hình vẫn bật)  (-i -m)",
            "sched_caffeinate_d": "Màn hình cũng vẫn bật  (caffeinate -i -m -s -d)",
            "sched_caffeinate_u": "Mô phỏng hoạt động người dùng (màn hình sáng, hệ thống thức)  (caffeinate -i -m -s -u)",
            "sched_caffeinate_full": "Tối đa: Màn hình + hệ thống + ổ đĩa thức liên tục  (caffeinate -d -i -m -s -u)",
            "sched_caffeinate_off": "Tắt (tiết kiệm điện bình thường – hệ thống có thể ngủ)",

            "sched_caffeinate_hint": (
                "💡 Kiến thức học tập: Dùng trực tiếp các cờ caffeinate trong terminal:\n"
                "   -i  ngăn hệ thống ngủ do không hoạt động\n"
                "   -m  ngăn ổ đĩa ngủ (đĩa cứng không ngủ)\n"
                "   -s  ngăn hệ thống ngủ (chỉ khi dùng adapter nguồn)\n"
                "   -d  ngăn màn hình ngủ (màn hình vẫn bật)\n"
                "   -u  mô phỏng hoạt động người dùng (màn hình vẫn sáng)\n"
                "   -w PID  kết thúc caffeinate khi tiến trình PID kết thúc\n"
                "Ví dụ:  caffeinate -i -m -s -w $$"
            ),

            "sched_info_scheduled": "Đã lên lịch tắt vào: {}",
            "sched_countdown_label": "Đếm ngược: {} đến khi tắt ({})",
            "sched_started": "Đã khởi động hẹn giờ.\n\nMục tiêu: {}\nThời lượng: {}\nKết thúc: {}",
            "sched_cancelled": "Đã hủy hẹn giờ",
            "sched_already_active": "Đã có một hẹn giờ đang chạy. Hủy trước không?",
            "sched_invalid_time": "Vui lòng nhập thời gian hợp lệ (ít nhất 1 phút).",
            "sched_max_time": "Tối đa cho phép 720 giờ (30 ngày).",
            # Ziel-spezifische Sprachausgabe beim Start
            "sched_voice_started_both": (
                "Đã khởi động hẹn giờ. Mac và NAS sẽ tắt sau {}."
            ),
            "sched_voice_started_nas": (
                "Đã khởi động hẹn giờ. Chỉ NAS sẽ tắt sau {}. "
                "Mac vẫn bật."
            ),
            "sched_voice_started_mac": (
                "Đã khởi động hẹn giờ. Chỉ Mac sẽ tắt sau {}. "
                "NAS vẫn bật."
            ),
            "sched_voice_started_nothing": (
                "Đã khởi động hẹn giờ. Sẽ không thực hiện gì khi hết giờ. "
                "caffeinate vẫn hoạt động cho đến lúc đó."
            ),
            # Konkrete Sprachausgabe für "Nichts tun" – je nach caffeinate-Option
            "sched_voice_nothing_ims": (
                "Mac vẫn thức trong {}. "
                "Màn hình có thể mờ đi. "
                "Sẽ không thực hiện gì khi hết giờ."
            ),
            "sched_voice_nothing_im": (
                "Mac vẫn thức trong {}. "
                "Màn hình vẫn bật. "
                "Sẽ không thực hiện gì khi hết giờ."
            ),
            "sched_voice_nothing_d": (
                "Mac và màn hình vẫn bật trong {}. "
                "Sẽ không thực hiện gì khi hết giờ."
            ),
            "sched_voice_nothing_u": (
                "Mac vẫn hoạt động trong {}. "
                "Màn hình vẫn sáng. "
                "Sẽ không thực hiện gì khi hết giờ."
            ),
            "sched_voice_nothing_full": (
                "Mac vẫn hoạt động hoàn toàn trong {} – màn hình và hệ thống thức liên tục. "
                "Sẽ không thực hiện gì khi hết giờ."
            ),
            "sched_voice_nothing_off": (
                "Hẹn giờ chạy trong {}. "
                "Sẽ không thực hiện gì khi hết giờ. "
                "Lưu ý: Mac có thể chuyển sang chế độ ngủ."
            ),
            "sched_voice_cancelled": "Đã hủy hẹn giờ",
            "sched_caffeinate_failed": "Không thể khởi động caffeinate:\n{}",
            "sched_target_required": "Vui lòng chọn mục tiêu.",
            "sched_tooltip_active": "Hẹn giờ đang chạy – nhấp để hủy",

            "status_scheduled_active": "Hẹn giờ đang hoạt động - còn {}",
            "status_scheduled_triggered": "Hẹn giờ đã hết - đang khởi động {}",
            "status_scheduled_cancelled": "Đã hủy hẹn giờ",

            # Schließen-Schutz bei aktivem Zeitgeber
            "close_blocked_title": "Hẹn giờ đang hoạt động",
            "close_blocked_text": (
                "<b>Vẫn còn một hẹn giờ đang chạy!</b><br><br>"
                "Đã lên lịch: {}<br>"
                "Còn lại: <b>{}</b><br>"
                "Lúc: {}<br><br>"
                "Nếu bạn đóng bây giờ, việc tắt theo lịch "
                "<b>sẽ không còn được thực hiện nữa</b>."
            ),
            "close_blocked_yes": "Vẫn đóng",
            "close_blocked_no": "Để ứng dụng tiếp tục chạy",
            "close_blocked_cancel_text": (
                "Vẫn còn một hẹn giờ đang chạy.\n\n"
                "Bạn có thực sự muốn đóng ứng dụng không?\n"
                "(Việc tắt theo lịch sẽ bị hủy bỏ.)"
            ),
            "close_blocked_log_aborted": "Đã hủy việc đóng (hẹn giờ đang hoạt động)",
            "close_blocked_log_discarded": (
                "Ứng dụng đóng dù hẹn giờ đang hoạt động – đã hủy bỏ hẹn giờ"
            ),
            "close_blocked_log_cancel_aborted": (
                "Đã hủy việc đóng ứng dụng qua nút Hủy"
            ),

            "duration_day": "ngày",
            "duration_days": "ngày",
            "duration_hour": "giờ",
            "duration_hours": "giờ",
            "duration_minute": "phút",
            "duration_minutes": "phút",
            "duration_connector_and": "và",
            "tooltip_pause_timer": "Tạm dừng / tiếp tục hẹn giờ",

            # =========================================
            # PAUSE / FORTSETZEN
            # =========================================
            "timer_paused": "Đã tạm dừng hẹn giờ – còn {} giây",
            "timer_resumed": "Đã tiếp tục hẹn giờ",
            "say_timer_paused": "Đã tạm dừng hẹn giờ",
            "say_timer_resumed": "Đã tiếp tục hẹn giờ",
            "tooltip_pause_timer": "Tạm dừng/tiếp tục hẹn giờ",

            # =========================================
            # SPRACHAUSGABE
            # =========================================
            "speech_enabled_label": "Đã bật đầu ra giọng nói",
            "speech_enabled_hint": (
                "Đọc to các thông báo trạng thái, xác nhận âm lượng và "
                "thông tin hẹn giờ thông qua đầu ra giọng nói của macOS. "
                "Khi tắt, ứng dụng sẽ chạy im lặng."
            ),

            # ================================
            # Mac-Shutdown Passwort
            # ################################
            "startup_no_pw_message": (
                "Để tắt Mac theo lịch trình, cần có "
                "mật khẩu quản trị viên.\n\n"
                "Mật khẩu được lưu trữ an toàn trong Chuỗi khóa macOS và "
                "chỉ được sử dụng khi tắt máy.\n\n"
                "Thiết lập ngay bây giờ?"
            ),
            "mac_pw_dialog_title": "Mật khẩu quản trị viên",
            "mac_pw_dialog_message": (
                "Để tắt Mac, cần có mật khẩu quản trị viên.\n\n"
                "Mật khẩu được lưu trữ an toàn trong Chuỗi khóa macOS và "
                "chỉ được sử dụng khi tắt máy."
            ),
            "mac_pw_wrong_password": (
                "Mật khẩu không đúng.\n\n"
                "Vui lòng thử lại."
            ),
            "mac_pw_test_failed": (
                "Lỗi khi kiểm tra mật khẩu:\n\n{}"
            ),
            "sched_cancelled_no_password": (
                "Hẹn giờ không được khởi động vì việc nhập "
                "mật khẩu đã bị hủy bỏ.\n\n"
                "Không có mật khẩu, không thể tắt Mac."
            ),
            "clear_password_title": "Xóa mật khẩu đã lưu",
            "clear_password_message": (
                "Xóa mật khẩu quản trị viên được lưu trong Chuỗi khóa?\n\n"
                "Trong lần tắt máy theo lịch trình tiếp theo, mật khẩu "
                "sẽ được yêu cầu lại."
            ),
            "clear_password_success": "Mật khẩu đã được xóa khỏi Chuỗi khóa.",
            "clear_password_failed": "Không thể xóa mật khẩu.",
            "clear_password_description": (
                "Xóa mật khẩu quản trị viên được lưu trong Chuỗi khóa "
                "macOS. Trong lần tắt máy theo lịch trình tiếp theo, "
                "mật khẩu sẽ được yêu cầu lại."
            ),
            "clear_password_button": "Xóa mật khẩu đã lưu",
            "shutdown_no_password_message": (
                "Không thể tắt Mac.\n\n"
                "Không có sẵn quy tắc NOPASSWD trong sudoers cũng như "
                "mật khẩu đã lưu trong Chuỗi khóa.\n\n"
                "Vui lòng thiết lập lại lịch tắt máy."
            ),
            # Fehler beim Auswerfen
            "warning_title": "Cảnh báo",
            "warning_eject_failed_continue": (
                "Không thể đẩy các ổ đĩa mạng ra một cách sạch sẽ.\n\n"
                "Nếu dữ liệu vẫn đang được sao chép hoặc tệp đang mở, "
                "có thể xảy ra mất dữ liệu.\n\n"
                "Vẫn tiếp tục tắt máy?"
            ),
            "auto_timer_disabled_no_pw": (
                "Đã tắt tự động tắt máy – không có mật khẩu quản trị viên. "
                "Vui lòng nhập một lần khi được nhắc ở lần tiếp theo."
            ),
            # =========================================
            # BUTTON JA NEIN
            # =========================================
            "btn_yes": "Có",
            "btn_no": "Không",

            # =========================================
            # caffeinate Option
            # =========================================
            "sched_target_coffee": "☕ Không tắt bất cứ thứ gì  (Mac vẫn thức – ví dụ: cho các script sao lưu)",
            "sched_countdown_coffee_label": "⏳ caffeinate đang hoạt động: còn {} ({})",

            # =========================================
            # TIMER KONFLIKT WARNUNG
            # =========================================
            "coffee_conflict_title": "Hẹn giờ cà phê vẫn đang chạy",
            "coffee_conflict_message": (
                "Một hẹn giờ cà phê vẫn đang chạy:\n\n"
                "Còn lại: {}\n\n"
                "Nếu bạn tắt máy bây giờ, hẹn giờ cà phê sẽ bị hủy "
                "và caffeinate sẽ dừng lại.\n\n"
                "Vẫn tắt máy?"
            ),
            "shutdown_timer_conflict_title": "Hẹn giờ tắt máy vẫn đang chạy",
            "shutdown_timer_conflict_message": (
                "Một hẹn giờ tắt máy vẫn đang chạy:\n\n"
                "Đã lên lịch: {}\n"
                "Còn lại: {}\n\n"
                "Nếu bạn tắt thủ công bây giờ, hẹn giờ sẽ bị hủy "
                "và cần phải lên lịch lại.\n\n"
                "Vẫn tắt máy?"
            ),
            "tooltip_stop_timer": "Dừng hẹn giờ hoàn toàn",
            "tooltip_stop_timer_inactive": "Không có hẹn giờ nào hoạt động",
            "timer_stopped_notice": "⏹ Hẹn giờ đã dừng – sẵn sàng khởi động lại",
            "say_timer_stopped": "Hẹn giờ đã dừng",
            "say_timer_restarted": "Hẹn giờ đã khởi động lại",
            # ═══════════════════════════════════════════════════════════
            # Phiên bản 2.3.0 — Đa nền tảng cho mọi nhà sản xuất
            # ═══════════════════════════════════════════════════════════

            # ─── Nhà sản xuất NAS ───
            "vendor_label": "Nhà sản xuất NAS:",
            "vendor_tooltip": (
                "Chọn nhà sản xuất NAS của bạn. Quyết định lệnh tắt máy "
                "và đường dẫn mặc định. 'Tự động phát hiện' kiểm tra "
                "NAS qua SSH."
            ),
            "vendor_auto_detect": "🔄 Tự động phát hiện",
            "vendor_auto_detect_tooltip": (
                "Tự động phát hiện nhà sản xuất qua SSH. "
                "Yêu cầu: khóa SSH và IP được cấu hình đúng."
            ),
            "vendor_detect_in_progress": "🔄 Đang phát hiện...",

            "vendor_synology": "Synology",
            "vendor_qnap": "QNAP",
            "vendor_truenas": "TrueNAS / FreeNAS",
            "vendor_unraid": "Unraid",
            "vendor_openmediavault": "OpenMediaVault",
            "vendor_asustor": "Asustor",
            "vendor_wd": "Western Digital",
            "vendor_buffalo": "Buffalo",
            "vendor_thecus": "Thecus",
            "vendor_linux_generic": "Linux thông thường",
            "vendor_macos_server": "macOS Server",
            "vendor_windows_server": "Windows Server",
            "vendor_custom": "Tùy chỉnh",
            "vendor_custom_hint": (
                "Tùy chỉnh: Điều chỉnh lệnh tắt máy theo cách thủ công. "
                "Mặc định: 'sudo shutdown -h now' (hoạt động trên "
                "80% các NAS Linux)."
            ),

            # ─── Phát hiện nhà sản xuất (thông báo trạng thái) ───
            "vendor_detect_success": "Đã phát hiện nhà sản xuất: {}",
            "vendor_detect_success_question": (
                "Đã phát hiện nhà sản xuất: {}\n\n"
                "Bạn có muốn áp dụng nhà sản xuất này không?\n"
                "(Giá trị hiện tại: {})"
            ),
            "vendor_detect_failed": (
                "Không thể tự động phát hiện nhà sản xuất.\n\n"
                "Vui lòng chọn thủ công. Hầu hết các NAS Linux hoạt động "
                "với 'Linux thông thường'."
            ),
            "vendor_detect_no_ssh": (
                "Tự động phát hiện yêu cầu quyền truy cập SSH.\n\n"
                "Vui lòng kiểm tra:\n"
                "• Đường dẫn khóa SSH chính xác\n"
                "• Địa chỉ IP chính xác\n"
                "• SSH được bật trên NAS\n"
                "• Khóa SSH được cài đặt trên NAS "
                "(~/.ssh/authorized_keys)"
            ),
            "vendor_detect_no_ssh_configured": (
                "Vui lòng nhập khóa SSH và địa chỉ IP trước."
            ),
            "vendor_detect_nas_offline": (
                "Máy chủ NAS không phản hồi.\n\n"
                "Vui lòng kiểm tra:\n"
                "• NAS đã được bật chưa?\n"
                "• Địa chỉ IP có chính xác không?\n"
                "• NAS có cùng mạng không?\n\n"
                "Khởi động NAS và thử lại."
            ),
            "vendor_detect_error": "Lỗi khi tự động phát hiện:\n\n{}",
            "vendor_detect_ssh_key_missing": (
                "Không tìm thấy khóa SSH:\n\n{}\n\n"
                "Vui lòng kiểm tra đường dẫn trong cài đặt."
            ),

            # ─── Lệnh tắt máy tùy chỉnh ───
            "custom_cmd_label": "Lệnh tắt máy:",
            "custom_cmd_tooltip": (
                "Lệnh được gửi đến NAS qua SSH. "
                "Phân tách nhiều lệnh bằng dấu chấm phẩy."
            ),
            "custom_cmd_hint": (
                "💡 Phân tách nhiều lệnh bằng dấu chấm phẩy — "
                "lệnh đầu tiên thành công sẽ được sử dụng. "
                "Ví dụ: sudo shutdown -h now; sudo poweroff"
            ),
            "custom_cmd_help_tooltip": "Hiển trợ giúp về lệnh tắt máy",
            "custom_cmd_help_title": "Các lệnh tắt máy thông dụng",
            "custom_cmd_help_text": (
                "<h3>Các lệnh tắt máy thông dụng theo nhà sản xuất</h3>"
                "<table cellpadding='4'>"
                "<tr><td><b>Linux (thông thường):</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code><br>"
                "<code>sudo halt -p</code></td></tr>"
                "<tr><td><b>Synology:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo synopoweroff</code></td></tr>"
                "<tr><td><b>QNAP:</b></td>"
                "<td><code>sudo shutdown -h now</code><br>"
                "<code>sudo poweroff</code></td></tr>"
                "<tr><td><b>Unraid:</b></td>"
                "<td><code>powerdown</code><br>"
                "<code>sudo powerdown</code></td></tr>"
                "<tr><td><b>TrueNAS:</b></td>"
                "<td><code>sudo shutdown -h now</code></td></tr>"
                "<tr><td><b>Windows Server:</b></td>"
                "<td><code>shutdown /s /t 0</code></td></tr>"
                "</table>"
                "<h4>Nhiều lệnh (chuỗi dự phòng)</h4>"
                "<p>Nếu lệnh đầu tiên thất bại, lệnh tiếp theo sẽ được thử. "
                "Phân tách bằng dấu chấm phẩy:</p>"
                "<p><code>sudo shutdown -h now; sudo poweroff; sudo halt -p</code></p>"
                "<p><b>Mẹo:</b> Chọn lệnh có khả năng thành công nhất trước, "
                "sau đó là các lựa chọn thay thế.</p>"
            ),

            # ─── Phát hiện ổ đĩa ───
            "volumes_detection_in_progress": "🔄 Đang phát hiện ổ đĩa qua SSH...",
            "volumes_detection_via_paths": (
                "🔍 Đang tìm kiếm trong đường dẫn của nhà sản xuất..."
            ),
            "volumes_detection_via_smb": (
                "🔍 Dự phòng: Đang tìm kiếm qua smbclient..."
            ),

            # ─── Bảng phát hiện ổ đĩa ───
            "volumes_detect_panel_running": (
                "🔍 Đang tìm kiếm ổ đĩa qua SSH... "
                "Quá trình này có thể mất vài giây."
            ),
            "volumes_detect_panel_success": (
                "Đã tìm thấy {} ổ đĩa — {} mới, {} đã có trong danh sách"
            ),
            "volumes_detect_panel_partial": (
                "Đã tìm thấy {} ổ đĩa — tất cả đã có trong danh sách"
            ),
            "volumes_detect_panel_failed": (
                "Không tìm thấy ổ đĩa nào. "
                "Vui lòng thêm ổ đĩa thủ công."
            ),

            # ─── Phát hiện địa chỉ MAC ───
            "mac_detect_in_progress": "🔄 Đang phát hiện địa chỉ MAC...",
            "mac_detect_success": "✅ Đã phát hiện địa chỉ MAC: {}",
            "mac_detect_success_dialog": (
                "Đã phát hiện địa chỉ MAC thành công.\n\n"
                "IP: {1}\n"
                "MAC: {0}\n\n"
                "Giá trị đã được nhập vào trường MAC."
            ),
            "mac_detect_failed": (
                "⚠ Không thể tự động phát hiện địa chỉ MAC. "
                "Trợ giúp sẽ được hiển thị."
            ),
            "config_mac_find": "🔍 Tìm MAC",
            "config_mac_find_tooltip": (
                "Tự động phát hiện địa chỉ MAC. "
                "Nếu thất bại, hướng dẫn sẽ được hiển thị."
            ),
        },
    }

    def __init__(self):
        self.current_language = "de"
        self._listeners = []
        self.load_language_setting()

    def load_language_setting(self):
        """Lädt die gespeicherte Spracheinstellung."""
        try:
            settings = QSettings("AnyNasPy", "AnyNasPy")
            lang = settings.value("language", "de")
            if lang in self.LANGUAGES:
                self.current_language = lang
                print(f"✅ Sprache aus QSettings geladen: {lang}")
            else:
                print(f"⚠️ Ungültige Sprache in QSettings: {lang}, verwende 'de'")
                self.current_language = "de"
        except Exception as e:
            print(f"❌ Fehler beim Laden der Sprache: {e}")
            self.current_language = "de"

    def save_language_setting(self):
        """Speichert die Spracheinstellung."""
        try:
            settings = QSettings("AnyNasPy", "AnyNasPy")
            settings.setValue("language", self.current_language)
            settings.sync()
            print(f"✅ Sprache in QSettings gespeichert: {self.current_language}")
        except Exception as e:
            print(f"❌ Fehler beim Speichern der Sprache: {e}")

    def add_listener(self, callback):
        if callback not in self._listeners:
            self._listeners.append(callback)

    def remove_listener(self, callback):
        if callback in self._listeners:
            self._listeners.remove(callback)

    def set_language(self, lang_code):
        if lang_code in self.LANGUAGES:
            self.current_language = lang_code
            self.save_language_setting()
            for callback in self._listeners:
                try:
                    callback()
                except Exception as e:
                    print(f"Fehler beim Benachrichtigen des Listeners: {e}")
            return True
        return False

    def get_language(self):
        return self.current_language

    def tr(self, key):
        """Gibt die Übersetzung für einen Schlüssel zurück."""
        translations = self.TRANSLATIONS.get(self.current_language)
        # Fallback auf Englisch, wenn die Sprache nicht in TRANSLATIONS definiert ist
        if translations is None:
            translations = self.TRANSLATIONS.get("en", {})
        return translations.get(key, key)

    def get_language_name(self, lang_code):
        """Gibt den angezeigten Namen (inkl. Flagge) zurück."""
        return self.LANGUAGES.get(lang_code, lang_code)


# Globaler Sprachmanager
LANG = LanguageManager()


def tr(key):
    """Globale Übersetzungsfunktion."""
    return LANG.tr(key)

# =======================================
# LOGGING KLASSE (TXT-Dateien)
# =======================================


class AppLogger:
    """Logging-Klasse mit TXT-Dateien und Rotation (max 5 Dateien)"""
    MAX_LOG_SIZE_BYTES = 5 * 1024 * 1024   # 5 MB

    def __init__(self, log_dir=None):
        if log_dir is None:
            log_dir = os.path.expanduser("~/Library/Application Support/AnyNasPy/Logs")

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.max_files = 5
        self.current_log_file = None
        self.log_buffer = []
        self.buffer_size = 10  # Nach 10 Einträgen wird geschrieben

        # Sicherstellen, dass der Buffer auch bei unerwartetem Ende geschrieben wird
        atexit.register(self._finalize)

        # Alte Logs aufräumen
        self.cleanup_old_logs()

        # Neues Log erstellen
        self.create_new_log()

    def cleanup_old_logs(self):
        """Löscht die ältesten Log-Dateien, wenn mehr als max_files vorhanden"""
        try:
            log_files = sorted(
                self.log_dir.glob("AnyNasPy_*.txt"), key=lambda x: x.stat().st_mtime
            )

            # Älteste löschen wenn mehr als max_files
            while len(log_files) >= self.max_files:
                oldest = log_files.pop(0)
                oldest.unlink()
                print(f"  Alte Log-Datei gelöscht: {oldest.name}")

        except Exception as e:
            print(f"Fehler beim Aufräumen der Logs: {e}")

    def create_new_log(self):
        """Erstellt eine neue Log-Datei mit Zeitstempel"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.current_log_file = self.log_dir / f"AnyNasPy_{timestamp}.txt"

        # Header schreiben
        with open(self.current_log_file, "w", encoding="utf-8") as f:
            f.write("=" * 80 + "\n")
            f.write(f"AnyNasPy Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"System: {platform.system()} {platform.release()}\n")
            f.write(f"Python: {sys.version}\n")
            f.write(f"Architektur: {platform.machine()}\n")
            f.write(f"Prozess-ID: {os.getpid()}\n")
            f.write("-" * 80 + "\n\n")

        # Log-Start schreiben
        self.log("=== SYNASPY GESTARTET ===", "START")

    def _rotate_if_too_big(self):
        if self.current_log_file and self.current_log_file.exists():
            if self.current_log_file.stat().st_size > self.MAX_LOG_SIZE_BYTES:
                self.cleanup_old_logs()
                self.create_new_log()

    def _write_buffer(self):
        """Schreibt den Buffer in die Log-Datei"""
        if not self.log_buffer:
            return

        # Prüfen ob die Log-Datei definiert ist
        if self.current_log_file is None:
            print("Fehler: current_log_file ist nicht definiert")
            return

        try:
            with open(self.current_log_file, "a", encoding="utf-8") as f:
                for entry in self.log_buffer:
                    f.write(entry)
            self.log_buffer = []
            self._rotate_if_too_big()
        except Exception as e:
            print(f"Fehler beim Schreiben ins Log: {e}")

    def log(self, message, level="INFO"):
        """Schreibt eine Nachricht ins Log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        # In Buffer speichern
        self.log_buffer.append(log_entry)

        # Wenn Buffer voll, schreiben
        if len(self.log_buffer) >= self.buffer_size:
            self._write_buffer()

    def log_action(self, action, details=""):
        """Loggt eine Aktion mit Details"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ACTION] {action}"
        if details:
            log_entry += f" - {details}"
        log_entry += "\n"

        self.log_buffer.append(log_entry)
        if len(self.log_buffer) >= self.buffer_size:
            self._write_buffer()

    def log_error(self, error, details="", exception=None):
        """Loggt einen Fehler mit Stacktrace"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ERROR] {error}"
        if details:
            log_entry += f" - {details}"
        log_entry += "\n"

        # Wenn Exception übergeben, Stacktrace hinzufügen
        if exception:
            log_entry += f"[{timestamp}] [TRACE] {traceback.format_exc()}\n"

        self.log_buffer.append(log_entry)
        if len(self.log_buffer) >= self.buffer_size:
            self._write_buffer()

    def log_crash(self, exception):
        """Loggt einen Absturz mit vollständigem Stacktrace"""
        # Prüfen ob die Log-Datei definiert ist
        if self.current_log_file is None:
            print(
                "Fehler: current_log_file ist nicht definiert, Crash-Log kann nicht geschrieben werden"
            )
            # Fallback: Zumindest auf der Konsole ausgeben
            print(f"CRASH: {exception}")
            traceback.print_exc()
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"""
    {'='*80}
    [{timestamp}] [CRASH] ANWENDUNG ABGESTÜRZT!
    {'='*80}
    Fehler: {str(exception)}
    Typ: {type(exception).__name__}

    Stacktrace:
    {traceback.format_exc()}
    {'='*80}
    """
        try:
            # Direkt schreiben, nicht über Buffer
            with open(self.current_log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Fehler beim Schreiben des Crash-Logs: {e}")
            # Im Fehlerfall trotzdem Stacktrace ausgeben
            traceback.print_exc()

    def log_config(self, config_dict):
        """Loggt die aktuelle Konfiguration (ohne sensible Daten)."""
        try:
            log_entry = "--- CONFIGURATION ---\n"
            for key, value in config_dict.items():
                if key in ["nas_user", "nas_ip", "nas_mac", "ssh_key_path", "nas_dns"]:
                    # Sensible Daten kürzen
                    if isinstance(value, str) and len(value) > 10:
                        value = value[:8] + "..."
                if isinstance(value, list):
                    if value and isinstance(value[0], dict):
                        # Liste von Dictionaries (volume_list_with_state)
                        names = [v.get("name", "") for v in value[:3]]
                        if len(value) > 3:
                            names.append("...")
                        log_entry += f"  {key}: [{', '.join(names)}]\n"
                    else:
                        # Liste von Strings
                        if len(value) > 3:
                            log_entry += f"  {key}: [{', '.join(value[:3])} ...]\n"
                        else:
                            log_entry += f"  {key}: [{', '.join(value)}]\n"
                elif isinstance(value, dict):
                    log_entry += f"  {key}: {{...}}\n"
                else:
                    log_entry += f"  {key}: {value}\n"
            self.log(log_entry, "CONFIG")
        except Exception as e:
            self.log_error("Fehler beim Loggen der Konfiguration", str(e), e)

    def log_system_info(self):
        """Loggt Systeminformationen"""
        info = f"""
        System-Informationen:
        Betriebssystem: {platform.system()} {platform.release()} ({platform.version()})
        Architektur: {platform.machine()}
        Prozessor: {platform.processor()}
        Python: {sys.version}
        Python Pfad: {sys.executable}
        Arbeitsverzeichnis: {os.getcwd()}
        Umgebungsvariablen:
            PATH: {os.environ.get('PATH', 'N/A')[:200]}...
            HOME: {os.environ.get('HOME', 'N/A')}
            USER: {os.environ.get('USER', 'N/A')}
        """
        self.log(info, "SYSTEM")

    def flush(self):
        """Schreibt alle gepufferten Log-Einträge"""
        self._write_buffer()

    def _finalize(self):
        """Wird beim Programmende automatisch aufgerufen (atexit)."""
        try:
            self.flush()
            self.log("=== SYNASPY BEENDET (atexit) ===", "STOP")
            self.flush()
        except Exception:
            # Niemals beim Beenden crashen
            pass


# =======================================
# GLOBALER EXCEPTION-HANDLER
# =======================================


def global_exception_handler(exc_type, exc_value, exc_traceback):
    """Globaler Exception-Handler für nicht abgefangene Exceptions."""
    # KeyboardInterrupt nicht abfangen – Python-Standard beibehalten
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logged = False

    try:
        # Versuche Logger über laufende Frames zu finden
        logger = None
        try:
            for frame in sys._current_frames().values():
                if "self" in frame.f_locals:
                    candidate = frame.f_locals["self"]
                    if hasattr(candidate, "logger"):
                        logger = candidate.logger
                        break
        except Exception:
            logger = None

        # Versuch 1: Logger schreiben
        if logger is not None:
            try:
                logger.log_crash(exc_value)
                logger.flush()
                logged = True
            except Exception:
                logged = False

        # Versuch 2: Direkt in eine Crash-Datei schreiben
        if not logged:
            try:
                crash_log = (
                    Path.home()
                    / "Library/Application Support/AnyNasPy/Logs/crash.txt"
                )
                crash_log.parent.mkdir(parents=True, exist_ok=True)
                with open(crash_log, "a", encoding="utf-8") as f:
                    f.write(f"\n{'='*80}\n")
                    f.write(
                        f"CRASH - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    )
                    f.write(f"Fehler: {exc_value}\n")
                    f.write(f"Typ: {exc_type.__name__}\n")
                    f.write(f"Stacktrace:\n{traceback.format_exc()}\n")
                    f.write(f"{'='*80}\n")
                logged = True
            except Exception:
                logged = False
    except Exception:
        # Wenn schon der Handler selbst crasht – niemals aufgeben
        logged = False
    finally:
        # ⬇️ WICHTIG: Immer den Stacktrace auf stderr ausgeben,
        #    damit Fehler im Terminal sichtbar sind – auch wenn das Log
        #    nicht geschrieben werden konnte.
        try:
            traceback.print_exception(exc_type, exc_value, exc_traceback)
        except Exception:
            # Letzte Rettung
            print(f"FATAL: {exc_type.__name__}: {exc_value}")

    # Standard-Exception-Handler aufrufen (gibt bei Bedarf weiteren Kontext aus)
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


# Exception-Handler setzen
sys.excepthook = global_exception_handler

# =======================================
# NAS-HERSTELLER-DEFINITIONEN
# =======================================


class NasVendor:
    """
    Zentrale Definition aller unterstützten NAS-Hersteller.

    Jeder Hersteller hat:
      - `key`              : Eindeutiger interner Schlüssel (lowercase)
      - `display_name`     : Anzeigename (übersetzt in TRANSLATIONS)
      - `shutdown_commands`: Liste der Shutdown-Befehle (in Reihenfolge)
      - `volume_paths`     : SSH-Pfade zu den Freigaben (für Detection)
      - `os_patterns`      : Textmuster in /etc/os-release oder uname
      - `notes`            : Hinweise für den User
    """

    # ═══════════════════════════════════════════════════════════════
    # Alle bekannten Hersteller mit ihren spezifischen Befehlen
    # ═══════════════════════════════════════════════════════════════
    VENDORS = {
        "synology": {
            "key": "synology",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo synopoweroff",
                "sudo poweroff",
                "sudo /usr/syno/bin/synopoweroff",
            ],
            "volume_paths": ["/volume1", "/volume2", "/volume3", "/volume4"],
            "os_patterns": ["synology", "dsm"],
            "notes": "Synology DSM",
        },
        "qnap": {
            "key": "qnap",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo poweroff",
                "poweroff",
                "sudo /sbin/poweroff",
            ],
            "volume_paths": ["/share", "/share/CACHEDEV1_DATA"],
            "os_patterns": ["qnap", "qts"],
            "notes": "QNAP QTS",
        },
        "truenas": {
            "key": "truenas",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo poweroff",
                "sudo /sbin/shutdown -h now",
            ],
            "volume_paths": ["/mnt"],
            "os_patterns": ["truenas", "freenas"],
            "notes": "TrueNAS / FreeNAS",
        },
        "unraid": {
            "key": "unraid",
            "shutdown_commands": [
                "powerdown",
                "sudo powerdown",
                "sudo shutdown -h now",
                "sudo /sbin/poweroff",
            ],
            "volume_paths": ["/mnt/user", "/mnt"],
            "os_patterns": ["unraid"],
            "notes": "Unraid",
        },
        "openmediavault": {
            "key": "openmediavault",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo poweroff",
            ],
            "volume_paths": ["/srv", "/export"],
            "os_patterns": ["openmediavault", "omv"],
            "notes": "OpenMediaVault",
        },
        "asustor": {
            "key": "asustor",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo poweroff",
            ],
            "volume_paths": ["/volume1", "/volume2"],
            "os_patterns": ["asustor", "asus"],
            "notes": "Asustor ADM",
        },
        "wd": {
            "key": "wd",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo poweroff",
                "sudo /sbin/poweroff",
            ],
            "volume_paths": ["/mnt", "/shares"],
            "os_patterns": ["western digital", "wd", "my cloud"],
            "notes": "Western Digital My Cloud",
        },
        "buffalo": {
            "key": "buffalo",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo poweroff",
            ],
            "volume_paths": ["/mnt", "/array1", "/array2"],
            "os_patterns": ["buffalo", "terastation"],
            "notes": "Buffalo TeraStation / LinkStation",
        },
        "thecus": {
            "key": "thecus",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo poweroff",
            ],
            "volume_paths": ["/raid", "/volume"],
            "os_patterns": ["thecus"],
            "notes": "Thecus NAS",
        },
        "linux_generic": {
            "key": "linux_generic",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo poweroff",
                "sudo /sbin/shutdown -h now",
                "sudo /sbin/poweroff",
                "sudo halt -p",
            ],
            "volume_paths": ["/mnt", "/media", "/srv"],
            "os_patterns": ["linux"],
            "notes": "Generisches Linux",
        },
        "macos_server": {
            "key": "macos_server",
            "shutdown_commands": [
                "sudo shutdown -h now",
                "sudo /sbin/shutdown -h now",
            ],
            "volume_paths": ["/Volumes"],
            "os_patterns": ["darwin", "macos", "mac os"],
            "notes": "macOS als Server",
        },
        "windows_server": {
            "key": "windows_server",
            "shutdown_commands": [
                "shutdown /s /t 0",
                "powershell -Command \"Stop-Computer -Force\"",
            ],
            "volume_paths": ["C:\\", "D:\\"],
            "os_patterns": ["windows"],
            "notes": "Windows Server (SSH-Server erforderlich)",
        },
        "custom": {
            "key": "custom",
            "shutdown_commands": [
                "sudo shutdown -h now",
            ],
            "volume_paths": [],
            "os_patterns": [],
            "notes": "Benutzerdefinierter Befehl",
        },
    }

    @classmethod
    def get_vendor(cls, key: str) -> dict:
        """Gibt die Definition eines Herstellers zurück (oder None)."""
        return cls.VENDORS.get(key.lower())

    @classmethod
    def get_all_keys(cls) -> list:
        """Gibt alle Hersteller-Keys zurück."""
        return list(cls.VENDORS.keys())

    @classmethod
    def detect_vendor_from_os_info(cls, os_info_text: str) -> str:
        """
        Erkennt den Hersteller anhand des Texts (z.B. aus /etc/os-release).

        Rückgabe: Hersteller-Key oder None.
        """
        if not os_info_text:
            return None
        text_lower = os_info_text.lower()
        for vendor_key, vendor_data in cls.VENDORS.items():
            for pattern in vendor_data.get("os_patterns", []):
                if pattern.lower() in text_lower:
                    return vendor_key
        return None


# =======================================
# SERVER PROFILE KLASSEN
# =======================================


class ServerProfile:
    """Einzelnes Server-Profil mit allen NAS-spezifischen Einstellungen."""

    # Standardwerte für ein Profil
    DEFAULTS = {
        "name": "NAS-Server",
        "nas_user": "nasuser",
        "nas_dns": "NAS-Synology",
        "nas_ip": "192.168.1.100",
        "nas_mac": "00:11:22:33:44:55",
        "ssh_key_path": "~/.ssh/id_rsa",
        "nas_vendor": "synology",
        "custom_shutdown_command": "sudo shutdown -h now",
        "volume_list": [],   # ⬅️ LEER — User trägt seine Volumes selbst ein
        "auto_shutdown_delay": 120,
        "auto_start_delay": 120,
        "wol_wait_time": 180,
        "smb_wait_time": 30,
        "mount_retries": 3,
        "shutdown_mac_delay": 5,
        "enabled": True,
    }

    def __init__(self, profile_id: Optional[str] = None):
        self.id = profile_id if profile_id else str(uuid.uuid4())
        self.name = "NAS-Server"
        self.nas_user = "nasuser"
        self.nas_dns = "NAS-Synology"
        self.nas_ip = "192.168.1.100"
        self.nas_mac = "00:11:22:33:44:55"
        self.ssh_key_path = "~/.ssh/id_rsa"
        self.nas_vendor = "synology"
        self.custom_shutdown_command = "sudo shutdown -h now"
        self.volume_list = []   # ⬅️ LEER
        # volume_list_with_state aus volume_list generieren
        self.volume_list_with_state = [
            {"name": v, "checked": True} for v in self.volume_list
        ]
        self.auto_shutdown_delay = 120
        self.auto_start_delay = 120
        self.wol_wait_time = 180
        self.smb_wait_time = 30
        self.mount_retries = 3
        self.shutdown_mac_delay = 5  # Sekunden zwischen NAS- und Mac-Shutdown
        self.enabled = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "nas_user": self.nas_user,
            "nas_dns": self.nas_dns,
            "nas_ip": self.nas_ip,
            "nas_mac": self.nas_mac,
            "ssh_key_path": self.ssh_key_path,
            "nas_vendor": self.nas_vendor,
            "custom_shutdown_command": self.custom_shutdown_command,
            "volume_list": self.volume_list,
            "volume_list_with_state": self.volume_list_with_state,  # NEU
            "auto_shutdown_delay": self.auto_shutdown_delay,
            "auto_start_delay": self.auto_start_delay,
            "wol_wait_time": self.wol_wait_time,
            "smb_wait_time": self.smb_wait_time,
            "mount_retries": self.mount_retries,
            "shutdown_mac_delay": self.shutdown_mac_delay,
            "enabled": self.enabled,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ServerProfile":
        profile = cls(data.get("id"))
        profile.name = data.get("name", "NAS-Server")
        profile.nas_user = data.get("nas_user", "nasuser")
        profile.nas_dns = data.get("nas_dns", "NAS-Synology")
        profile.nas_ip = data.get("nas_ip", "192.168.1.100")
        profile.nas_mac = data.get("nas_mac", "00:11:22:33:44:55")
        profile.ssh_key_path = data.get("ssh_key_path", "~/.ssh/id_rsa")
        profile.nas_vendor = data.get("nas_vendor", "synology")
        profile.custom_shutdown_command = data.get(
            "custom_shutdown_command", "sudo shutdown -h now"
        )
        profile.volume_list = data.get("volume_list", cls.DEFAULTS["volume_list"])
        profile.volume_list_with_state = data.get(
            "volume_list_with_state",
            [{"name": v, "checked": True} for v in profile.volume_list],
        )
        profile.auto_shutdown_delay = data.get("auto_shutdown_delay", 120)
        profile.auto_start_delay = data.get("auto_start_delay", 120)
        profile.wol_wait_time = data.get("wol_wait_time", 180)
        profile.smb_wait_time = data.get("smb_wait_time", 30)
        profile.mount_retries = data.get("mount_retries", 3)
        profile.shutdown_mac_delay = data.get("shutdown_mac_delay", 5)
        profile.enabled = data.get("enabled", True)
        return profile

    def get_config_dict(self) -> Dict[str, Any]:
        return {
            "nas_user": self.nas_user,
            "nas_dns": self.nas_dns,
            "nas_ip": self.nas_ip,
            "nas_mac": self.nas_mac,
            "ssh_key_path": self.ssh_key_path,
            "nas_vendor": self.nas_vendor,
            "custom_shutdown_command": self.custom_shutdown_command,
            # "volume_list": self.volume_list,
            "volume_list_with_state": self.volume_list_with_state,  # WICHTIG
            "auto_shutdown_delay": self.auto_shutdown_delay,
            "auto_start_delay": self.auto_start_delay,
            "wol_wait_time": self.wol_wait_time,
            "smb_wait_time": self.smb_wait_time,
            "mount_retries": self.mount_retries,
            "shutdown_mac_delay": self.shutdown_mac_delay,
        }


class ServerProfileManager:
    """Verwaltung aller Server-Profile."""

    def __init__(self):
        self.profiles: List[ServerProfile] = []
        self.active_profile_id: Optional[str] = None
        self.config_dir = Path.home() / "Library/Application Support/AnyNasPy"
        self.profiles_file = self.config_dir / "server_profiles.json"
        self._listeners: List[callable] = []
        self.load_profiles()

    def add_listener(self, callback):
        """Fügt einen Listener für Profiländerungen hinzu."""
        if callback not in self._listeners:
            self._listeners.append(callback)

    def remove_listener(self, callback):
        """Entfernt einen Listener."""
        if callback in self._listeners:
            self._listeners.remove(callback)

    def notify_listeners(self):
        """Benachrichtigt alle Listener über Änderungen."""
        for callback in self._listeners:
            try:
                callback()
            except Exception as e:
                print(f"Fehler beim Benachrichtigen des Profil-Listeners: {e}")

    def load_profiles(self):
        """Lädt die Profile aus der JSON-Datei."""
        if not self.profiles_file.exists():
            self._create_default_profile()
            return

        try:
            with open(self.profiles_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.profiles = []
            for profile_data in data.get("profiles", []):
                try:
                    profile = ServerProfile.from_dict(profile_data)
                    self.profiles.append(profile)
                except Exception as e:
                    print(f"Fehler beim Laden eines Profils: {e}")

            self.active_profile_id = data.get("active_profile_id")

            # Doppelte Namen korrigieren
            name_counts = {}
            for p in self.profiles:
                name_counts[p.name] = name_counts.get(p.name, 0) + 1

            renamed = False
            for name, count in name_counts.items():
                if count > 1:
                    idx = 0
                    for p in self.profiles:
                        if p.name == name:
                            if idx == 0:
                                idx += 1
                                continue
                            new_name = f"{name} ({idx})"
                            while new_name in name_counts:
                                idx += 1
                                new_name = f"{name} ({idx})"
                            p.name = new_name
                            renamed = True
                            idx += 1
                            name_counts[new_name] = name_counts.get(new_name, 0) + 1

            if renamed:
                self.save_profiles()

            if not self.profiles:
                self._create_default_profile()
                return

            if not self.get_profile(self.active_profile_id):
                self.active_profile_id = self.profiles[0].id
                self.save_profiles()

        except Exception as e:
            print(f"Fehler beim Laden der Profile: {e}")
            self._create_default_profile()

    def save_profiles(self):
        """Speichert die Profile in der JSON-Datei."""
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
            data = {
                "profiles": [p.to_dict() for p in self.profiles],
                "active_profile_id": self.active_profile_id,
            }
            # Atomares Schreiben
            temp_file = self.profiles_file.with_suffix(".tmp")
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            temp_file.replace(self.profiles_file)
            self.notify_listeners()
        except Exception as e:
            print(f"Fehler beim Speichern der Profile: {e}")

    def _create_default_profile(self):
        """Erstellt ein Standard-Profil mit eindeutigem Namen."""
        profile = ServerProfile()
        profile.name = "NAS-Server"
        counter = 1
        while self.get_profile_by_name(profile.name):
            profile.name = f"NAS-Server ({counter})"
            counter += 1
        self.profiles = [profile]
        self.active_profile_id = profile.id
        self.save_profiles()

    def get_profile(self, profile_id: str) -> Optional[ServerProfile]:
        """Gibt ein Profil anhand der ID zurück."""
        for p in self.profiles:
            if p.id == profile_id:
                return p
        return None

    def get_profile_by_name(self, name: str) -> Optional[ServerProfile]:
        """Gibt ein Profil anhand des Namens zurück."""
        for p in self.profiles:
            if p.name == name:
                return p
        return None

    def get_active_profile(self) -> Optional[ServerProfile]:
        """Gibt das aktive Profil zurück."""
        if self.active_profile_id:
            profile = self.get_profile(self.active_profile_id)
            if profile:
                return profile
            else:
                print(
                    f"WARNUNG: Aktive Profil-ID {self.active_profile_id} nicht gefunden!"
                )
        if self.profiles:
            # Verwende das erste Profil als Fallback, aber setze die ID richtig
            self.active_profile_id = self.profiles[0].id
            print(
                f"  Fallback: Aktives Profil auf '{self.profiles[0].name}' (ID: {self.active_profile_id}) gesetzt"
            )
            self.save_profiles()
            return self.profiles[0]
        return None

    def set_active_profile(self, profile_id: str) -> bool:
        """Setzt ein Profil als aktiv."""
        if self.get_profile(profile_id):
            self.active_profile_id = profile_id
            self.save_profiles()
            return True
        return False

    def add_profile(self, profile: ServerProfile) -> bool:
        """Fügt ein neues Profil hinzu, wenn der Name eindeutig ist."""
        if self.get_profile_by_name(profile.name):
            return False
        self.profiles.append(profile)
        self.save_profiles()
        return True

    def rename_profile(self, profile_id: str, new_name: str) -> bool:
        """Benennt ein Profil um, wenn der neue Name eindeutig ist."""
        if self.get_profile_by_name(new_name):
            return False
        profile = self.get_profile(profile_id)
        if not profile:
            return False
        profile.name = new_name
        self.save_profiles()
        return True

    def duplicate_profile(
        self, profile_id: str, new_name: str
    ) -> Optional[ServerProfile]:
        """Dupliziert ein Profil, wenn der neue Name eindeutig ist."""
        if self.get_profile_by_name(new_name):
            return None
        original = self.get_profile(profile_id)
        if not original:
            return None

        new_profile = ServerProfile()
        new_profile.name = new_name
        new_profile.nas_user = original.nas_user
        new_profile.nas_dns = original.nas_dns
        new_profile.nas_ip = original.nas_ip
        new_profile.nas_mac = original.nas_mac
        new_profile.ssh_key_path = original.ssh_key_path
        new_profile.nas_vendor = original.nas_vendor   # ⬅️ NEU
        new_profile.custom_shutdown_command = (
            original.custom_shutdown_command
        )   # ⬅️ NEU
        new_profile.volume_list = original.volume_list.copy()
        new_profile.volume_list_with_state = original.volume_list_with_state.copy()
        new_profile.auto_shutdown_delay = original.auto_shutdown_delay
        new_profile.auto_start_delay = original.auto_start_delay
        new_profile.wol_wait_time = original.wol_wait_time
        new_profile.smb_wait_time = original.smb_wait_time
        new_profile.mount_retries = original.mount_retries
        new_profile.shutdown_mac_delay = original.shutdown_mac_delay
        new_profile.enabled = original.enabled

        self.profiles.append(new_profile)
        self.save_profiles()
        return new_profile

    def remove_profile(self, profile_id: str) -> bool:
        """Entfernt ein Profil."""
        if len(self.profiles) <= 1:
            return False

        profile = self.get_profile(profile_id)
        if not profile:
            return False

        self.profiles = [p for p in self.profiles if p.id != profile_id]

        if self.active_profile_id == profile_id:
            self.active_profile_id = self.profiles[0].id

        self.save_profiles()
        return True

    def update_profile_from_config(
        self, profile_id: str, config_dict: Dict[str, Any]
    ) -> bool:
        """Aktualisiert ein Profil mit Werten aus einem Config-Dictionary."""
        profile = self.get_profile(profile_id)
        if not profile:
            print(f"❌ Profil mit ID {profile_id} nicht gefunden!")
            return False

        # Direkte Zuweisung aller Werte (kein hasattr)
        profile.nas_user = config_dict.get("nas_user", profile.nas_user)
        profile.nas_dns = config_dict.get("nas_dns", profile.nas_dns)
        profile.nas_ip = config_dict.get("nas_ip", profile.nas_ip)
        profile.nas_mac = config_dict.get("nas_mac", profile.nas_mac)
        profile.ssh_key_path = config_dict.get("ssh_key_path", profile.ssh_key_path)
        profile.nas_vendor = config_dict.get("nas_vendor", profile.nas_vendor)
        profile.custom_shutdown_command = config_dict.get(
            "custom_shutdown_command", profile.custom_shutdown_command
        )   # ⬅️ NEU
        profile.volume_list = config_dict.get("volume_list", profile.volume_list)
        profile.volume_list_with_state = config_dict.get(
            "volume_list_with_state", profile.volume_list_with_state
        )
        profile.auto_shutdown_delay = config_dict.get(
            "auto_shutdown_delay", profile.auto_shutdown_delay
        )
        profile.auto_start_delay = config_dict.get(
            "auto_start_delay", profile.auto_start_delay
        )
        profile.wol_wait_time = config_dict.get("wol_wait_time", profile.wol_wait_time)
        profile.smb_wait_time = config_dict.get("smb_wait_time", profile.smb_wait_time)
        profile.mount_retries = config_dict.get("mount_retries", profile.mount_retries)
        profile.shutdown_mac_delay = config_dict.get(
            "shutdown_mac_delay", profile.shutdown_mac_delay
        )

        print(f"✅ Profil '{profile.name}' aktualisiert:")
        print(f"  nas_user: {profile.nas_user}")
        print(f"  nas_ip: {profile.nas_ip}")
        print(f"  nas_mac: {profile.nas_mac}")

        self.save_profiles()
        return True

    def get_active_config(self) -> Dict[str, Any]:
        """Gibt die Konfiguration des aktiven Profils zurück."""
        profile = self.get_active_profile()
        if profile:
            return profile.get_config_dict()
        return {}

    def get_profile_names(self) -> List[str]:
        """Gibt eine Liste aller Profilnamen zurück."""
        return [p.name for p in self.profiles]

    def get_profile_list(self) -> List[Dict[str, Any]]:
        """Gibt eine Liste aller Profile als Dictionaries zurück."""
        return [
            {
                "id": p.id,
                "name": p.name,
                "is_active": p.id == self.active_profile_id,
                "enabled": p.enabled,
            }
            for p in self.profiles
        ]


# =======================================
# KONFIGURATIONSKLASSEN
# =======================================


class Config:
    """Zentrale Konfigurationsverwaltung mit QSettings, JSON-Datei und Server-Profilen."""

    # Standardwerte (NUR für globale Einstellungen)
    DEFAULTS = {
        "logo_file": "BinhDiez.png",
        "app_icon_file": "AnyNasPy.png",
        "speech_enabled": True,
    }

    def __init__(self):
        self.app_name = "AnyNasPy"
        self.org_name = "AnyNasPy"
        self.settings = QSettings(self.org_name, self.app_name)
        self.config_dir = Path.home() / "Library/Application Support/AnyNasPy"
        self.config_file = self.config_dir / "synaspy_config.json"
        self.profile_manager = ServerProfileManager()
        self.config = {}
        self.load_config()

    def load_config(self):
        """Lädt die Konfiguration aus QSettings, JSON und Profil."""
        self.config = self.DEFAULTS.copy()

        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    json_config = json.load(f)
                    for key in self.DEFAULTS.keys():
                        if key in json_config:
                            self.config[key] = json_config[key]
            except Exception as e:
                print(f"Fehler beim Laden der JSON-Konfiguration: {e}")

        for key in self.DEFAULTS.keys():
            value = self.settings.value(key)
            if value is not None:
                self.config[key] = value

        active_profile = self.profile_manager.get_active_profile()

        if active_profile:
            self.config["nas_user"] = active_profile.nas_user
            self.config["nas_dns"] = active_profile.nas_dns
            self.config["nas_ip"] = active_profile.nas_ip
            self.config["nas_mac"] = active_profile.nas_mac
            self.config["ssh_key_path"] = active_profile.ssh_key_path
            self.config["nas_vendor"] = active_profile.nas_vendor
            self.config["custom_shutdown_command"] = (
                active_profile.custom_shutdown_command
            )
            self.config["volume_list"] = active_profile.volume_list
            self.config["volume_list_with_state"] = (
                active_profile.volume_list_with_state
            )
            self.config["auto_shutdown_delay"] = active_profile.auto_shutdown_delay
            self.config["auto_start_delay"] = active_profile.auto_start_delay
            self.config["wol_wait_time"] = active_profile.wol_wait_time
            self.config["smb_wait_time"] = active_profile.smb_wait_time
            self.config["mount_retries"] = active_profile.mount_retries
            self.config["shutdown_mac_delay"] = active_profile.shutdown_mac_delay

            if "ssh_key_path" in self.config:
                self.config["ssh_key_path"] = os.path.expanduser(
                    self.config["ssh_key_path"]
                )
        else:
            self.config.update(ServerProfile.DEFAULTS)
            for key in ["name", "enabled", "id"]:
                self.config.pop(key, None)

        volume_state = self.config.get("volume_list_with_state")
        if volume_state is None:
            volume_names = self.config.get(
                "volume_list", ServerProfile.DEFAULTS["volume_list"]
            )
            volume_state = [{"name": v, "checked": True} for v in volume_names]
            self.config["volume_list_with_state"] = volume_state
        self.config["volume_list"] = [v["name"] for v in volume_state]

    def save_config(self):
        """Speichert die Konfiguration in QSettings, JSON und Profil."""
        for key in self.DEFAULTS.keys():
            if key in self.config:
                self.settings.setValue(key, self.config[key])

        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
            save_config = {}
            for key in self.DEFAULTS.keys():
                if key in self.config:
                    save_config[key] = self.config[key]
            with open(self.config_file, "w") as f:
                json.dump(save_config, f, indent=2)
        except Exception as e:
            print(f"Fehler beim Speichern der JSON-Konfiguration: {e}")

        active_profile = self.profile_manager.get_active_profile()
        if active_profile:
            active_profile.nas_user = self.config.get("nas_user", "")
            active_profile.nas_dns = self.config.get("nas_dns", "")
            active_profile.nas_ip = self.config.get("nas_ip", "")
            active_profile.nas_mac = self.config.get("nas_mac", "")
            active_profile.ssh_key_path = self.config.get("ssh_key_path", "")
            active_profile.nas_vendor = self.config.get("nas_vendor", "synology")
            active_profile.custom_shutdown_command = self.config.get(
                "custom_shutdown_command", "sudo shutdown -h now"
            )
            active_profile.volume_list = self.config.get("volume_list", [])
            active_profile.volume_list_with_state = self.config.get(
                "volume_list_with_state", []
            )
            active_profile.auto_shutdown_delay = self.config.get(
                "auto_shutdown_delay", 120
            )
            active_profile.auto_start_delay = self.config.get("auto_start_delay", 120)
            active_profile.wol_wait_time = self.config.get("wol_wait_time", 180)
            active_profile.smb_wait_time = self.config.get("smb_wait_time", 30)
            active_profile.mount_retries = self.config.get("mount_retries", 3)
            active_profile.shutdown_mac_delay = self.config.get("shutdown_mac_delay", 5)
            self.profile_manager.save_profiles()

    def get(self, key, default=None):
        """Gibt einen Konfigurationswert zurück."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Setzt einen Konfigurationswert."""
        self.config[key] = value
        self.save_config()

    def get_volumes_with_state(self):
        """Gibt die Volume-Liste mit Zuständen zurück."""
        volume_state = self.config.get("volume_list_with_state")
        if volume_state:
            return volume_state
        # Fallback: aus volume_list generieren
        volume_names = self.config.get(
            "volume_list", ServerProfile.DEFAULTS["volume_list"]
        )
        return [{"name": v, "checked": True} for v in volume_names]

    def get_volumes(self):
        """Gibt die Liste der Volume-Namen zurück (für Kompatibilität)."""
        volume_state = self.config.get("volume_list_with_state")
        if volume_state:
            return [v["name"] for v in volume_state]
        # Fallback auf alte volume_list
        return self.config.get("volume_list", ServerProfile.DEFAULTS["volume_list"])

    def get_json_path(self):
        """Gibt den Pfad zur JSON-Konfigurationsdatei zurück."""
        return str(self.config_file)

    def get_active_profile_id(self) -> Optional[str]:
        """Gibt die ID des aktiven Profils zurück."""
        return self.profile_manager.active_profile_id

    def get_active_profile_name(self) -> Optional[str]:
        """Gibt den Namen des aktiven Profils zurück."""
        profile = self.profile_manager.get_active_profile()
        return profile.name if profile else None


class ConfigDialog(QDialog):
    """Dialog zur Konfiguration der NAS-Einstellungen mit Multi-Server Unterstützung."""

    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self._updating_language = False
        self._debug = True
        self._updating_profile = False
        # Referenzen für Sprachaktualisierung speichern
        self.profile_header_label = None  # wird in initUI gesetzt
        self.language_group = None
        self.json_group = None

        # Logger vom Parent übernehmen
        if parent and hasattr(parent, "logger"):
            self.logger = parent.logger
        else:
            self.logger = AppLogger()

        # Sprach-Listener registrieren
        LANG.add_listener(self.update_ui_language)
        self.debug_log(
            f"Listener registriert, aktuelle Sprache: {LANG.current_language}"
        )

        self.initUI()
        self.load_values()

    def debug_log(self, message):
        """Debug-Ausgabe mit Zeitstempel."""
        if self._debug:
            from datetime import datetime

            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] [DEBUG] {message}")
            if hasattr(self, "logger"):
                self.logger.log(f"DEBUG: {message}", "DEBUG")

    def initUI(self):
        """Initialisiert die Dialog-Benutzeroberfläche."""
        self.setWindowTitle(tr("config_title"))
        self.setFixedSize(700, 750)

        self.setStyleSheet("""
            QDialog, QWidget {
                background-color: #000000;
            }
            QLabel {
                color: #ffffff;
                font-family: Helvetica, Arial, sans-serif;
            }
            QLineEdit, QSpinBox, QComboBox {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 4px;
                padding: 6px;
                font-family: Helvetica, Arial, sans-serif;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px 16px;
                margin: 4px;
                border-radius: 4px;
                border: 1px solid #333;
                background-color: #2a2a2a;
                color: white;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_save {
                background-color: #007AFF;
            }
            QPushButton#btn_save:hover {
                background-color: #0055CC;
            }
            QPushButton#btn_cancel {
                background-color: #555;
            }
            QPushButton#btn_cancel:hover {
                background-color: #666;
            }
            /* Volumes-Buttons (dunkelblau) – für schmale GUI optimiert */
            QPushButton#vol_detect,
            QPushButton#vol_add,
            QPushButton#vol_up,
            QPushButton#vol_down {
                background-color: #1565c0;
                color: #ffffff;
                border: 1px solid #0d47a1;
                margin: 4px;
                min-width: 80px;
            }
            QPushButton#vol_detect:hover,
            QPushButton#vol_add:hover,
            QPushButton#vol_up:hover,
            QPushButton#vol_down:hover {
                background-color: #0d47a1;
                border: 1px solid #007AFF;
            }
            /* Speziell für den Löschen-Button – rot */
            QPushButton#vol_delete {
                background-color: #d32f2f;
                color: #ffffff;
                border: 1px solid #b71c1c;
                margin: 4px;
                min-width: 80px;
            }
            QPushButton#vol_delete:hover {
                background-color: #b71c1c;
                border: 1px solid #007AFF;
            }
            /* Profile-Buttons (dunkelblau) */
            QPushButton#btn_activate,
            QPushButton#btn_rename,
            QPushButton#btn_duplicate {
                background-color: #1a237e;
                color: #ffffff;
                border: 1px solid #283593;
                margin: 4px;
            }
            QPushButton#btn_activate:hover,
            QPushButton#btn_rename:hover,
            QPushButton#btn_duplicate:hover {
                background-color: #283593;
                border: 1px solid #007AFF;
            }
            QGroupBox {
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #cccccc;
            }
            QScrollArea {
                border: none;
                background: transparent;
            }
            QTextEdit {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 4px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
            QComboBox {
                padding: 4px 8px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #888;
                margin-right: 8px;
            }
            QComboBox QAbstractItemView {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333;
                selection-background-color: #007AFF;
            }
            QTabWidget::pane {
                border: 1px solid #333;
                border-radius: 4px;
                background-color: #000000;
            }
            QTabBar::tab {
                background-color: #1a1a1a;
                color: #ffffff;
                padding: 8px 16px;
                margin-right: 2px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #2a2a2a;
                border-bottom: 2px solid #007AFF;
            }
            QTabBar::tab:hover {
                background-color: #2a2a2a;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Header mit Logo
        header_layout = QHBoxLayout()
        header_layout.setSpacing(10)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(script_dir, "BinhDiez.png")

        if os.path.exists(logo_path):
            try:
                pixmap = QPixmap(logo_path)
                if not pixmap.isNull():
                    logo_label = QLabel()
                    logo_label.setPixmap(
                        pixmap.scaled(
                            80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation
                        )
                    )
                    logo_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    header_layout.addStretch()
                    header_layout.addWidget(logo_label)
                    header_layout.addStretch()
            except:
                pass

        title_label = QLabel("Synology NAS Management")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #ffffff;")
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label)

        icon_path = os.path.join(script_dir, "AnyNasPy.png")
        if os.path.exists(icon_path):
            try:
                pixmap = QPixmap(icon_path)
                if not pixmap.isNull():
                    icon_label = QLabel()
                    icon_label.setPixmap(
                        pixmap.scaled(
                            60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation
                        )
                    )
                    icon_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    header_layout.addStretch()
                    header_layout.addWidget(icon_label)
                    header_layout.addStretch()
            except:
                pass

        main_layout.addLayout(header_layout)

        # Aktives Profil anzeigen
        profile_name = self.config.get_active_profile_name() or "Kein Profil"
        profile_label = QLabel(f"📌 {tr('config_profile_active')}: {profile_name}")
        profile_label.setStyleSheet(
            "color: #4CAF50; font-size: 13px; padding: 5px; background-color: #1a1a1a; border-radius: 4px;"
        )
        profile_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(profile_label)

        self.profile_header_label = profile_label

        # Tab-Widget
        self.tab_widget = QTabWidget()

        # Tab 1: Allgemein (NAS Einstellungen + Sprache)
        self.general_tab = QWidget()
        self._init_general_tab()
        self.tab_widget.addTab(self.general_tab, tr("config_tab_general"))

        # Tab 2: Volumes
        self.volumes_tab = QWidget()
        self._init_volumes_tab()
        self.tab_widget.addTab(self.volumes_tab, tr("config_tab_volumes"))

        # Tab 3: Zeiteinstellungen
        self.timing_tab = QWidget()
        self._init_timing_tab()
        self.tab_widget.addTab(self.timing_tab, tr("config_tab_timing"))

        # Tab 4: Profile
        self.profiles_tab = QWidget()
        self._init_profiles_tab()
        self.tab_widget.addTab(self.profiles_tab, tr("config_tab_profiles"))

        main_layout.addWidget(self.tab_widget)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.save_btn = QPushButton(tr("btn_save"))
        self.save_btn.setObjectName("btn_save")
        self.save_btn.clicked.connect(self.save_and_accept)
        button_layout.addWidget(self.save_btn)

        self.reset_btn = QPushButton(tr("btn_reset"))
        self.reset_btn.clicked.connect(self.reset_defaults)
        button_layout.addWidget(self.reset_btn)

        self.cancel_btn = QPushButton(tr("btn_cancel"))
        self.cancel_btn.setObjectName("btn_cancel")
        self.cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_btn)

        main_layout.addLayout(button_layout)

        self.status_label = QLabel("")
        self.status_label.setStyleSheet(
            "color: #888888; font-size: 11px; padding: 5px;"
        )
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # Dialog zentrieren
        parent = self.parent()
        if parent and isinstance(parent, QWidget):
            self.move(
                parent.x() + (parent.width() - self.width()) // 2,
                parent.y() + (parent.height() - self.height()) // 2,
            )

    ### Tab Allgemein

    def _init_general_tab(self):
        """Initialisiert den Allgemein-Tab."""
        layout = QVBoxLayout(self.general_tab)
        layout.setSpacing(15)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setSpacing(15)

        # === Sprachauswahl ===
        self.language_group = QGroupBox(tr("language"))  # Referenz speichern
        lang_layout = QHBoxLayout()
        self.lang_combo = QComboBox()
        for code, name in LanguageManager.LANGUAGES.items():
            self.lang_combo.addItem(name, code)
        current_lang = LANG.current_language
        current_index = self.lang_combo.findData(current_lang)
        self.lang_combo.setCurrentIndex(current_index)
        self.lang_combo.currentIndexChanged.connect(self.on_language_changed)
        lang_layout.addWidget(self.lang_combo)
        lang_layout.addStretch()
        self.language_group.setLayout(lang_layout)
        scroll_layout.addWidget(self.language_group)

        # ═══════════════════════════════════════════════════════
        # Sprachausgabe-Checkbox
        # ═══════════════════════════════════════════════════════
        self.speech_group = QGroupBox(tr("speech_enabled_label"))
        speech_layout = QVBoxLayout()

        self.speech_checkbox = QCheckBox(tr("speech_enabled_label"))
        self.speech_checkbox.setStyleSheet("""
            QCheckBox {
                color: #ffffff;
                font-size: 13px;
                padding: 4px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 1px solid #555;
                border-radius: 3px;
                background-color: #1a1a1a;
            }
            QCheckBox::indicator:checked {
                background-color: #007AFF;
                border: 1px solid #007AFF;
            }
        """)
        self.speech_checkbox.setChecked(
            self.config.get("speech_enabled", True)
        )
        speech_layout.addWidget(self.speech_checkbox)

        # Beschreibung
        self.speech_hint_label = QLabel(tr("speech_enabled_hint"))
        self.speech_hint_label.setStyleSheet(
            "color: #888888; font-size: 11px; padding: 4px 4px 4px 26px;"
        )
        self.speech_hint_label.setWordWrap(True)
        speech_layout.addWidget(self.speech_hint_label)

        self.speech_group.setLayout(speech_layout)
        scroll_layout.addWidget(self.speech_group)

        # === NAS Einstellungen ===
        self.nas_group = QGroupBox(tr("config_nas_group"))
        nas_layout = QGridLayout()
        nas_layout.setSpacing(10)
        nas_layout.setColumnStretch(0, 0)
        nas_layout.setColumnStretch(1, 1)

        self.nas_labels = {}

        row = 0

        # ═══════════════════════════════════════════════════════
        # NAS-Hersteller mit Auto-Erkennung + Benutzerdefiniert
        # ═══════════════════════════════════════════════════════
        label = QLabel(tr("vendor_label"))
        self.nas_labels["nas_vendor"] = label
        nas_layout.addWidget(label, row, 0)

        # Container für Combobox + Auto-Erkennen-Button
        vendor_container = QWidget()
        vendor_layout = QHBoxLayout(vendor_container)
        vendor_layout.setContentsMargins(0, 0, 0, 0)
        vendor_layout.setSpacing(6)

        self.nas_vendor_combo = QComboBox()
        self.nas_vendor_combo.setToolTip(tr("vendor_tooltip"))

        # Alle Hersteller aus NasVendor laden
        for vendor_key in NasVendor.get_all_keys():
            display_name = tr(f"vendor_{vendor_key}")
            self.nas_vendor_combo.addItem(display_name, vendor_key)

        # Signal für Wechsel auf "Benutzerdefiniert"
        self.nas_vendor_combo.currentIndexChanged.connect(
            self.on_vendor_changed
        )

        vendor_layout.addWidget(self.nas_vendor_combo, stretch=1)

        # Auto-Erkennen-Button
        self.vendor_auto_btn = QPushButton(tr("vendor_auto_detect"))
        self.vendor_auto_btn.setObjectName("btn_vendor_auto")
        self.vendor_auto_btn.setToolTip(tr("vendor_auto_detect_tooltip"))
        self.vendor_auto_btn.clicked.connect(self.auto_detect_vendor)
        self.vendor_auto_btn.setStyleSheet("""
            QPushButton#btn_vendor_auto {
                background-color: #007AFF;
                color: white;
                font-weight: bold;
                padding: 6px 12px;
                min-width: 120px;
            }
            QPushButton#btn_vendor_auto:hover {
                background-color: #0055CC;
                border: 1px solid #ffffff;
            }
            QPushButton#btn_vendor_auto:disabled {
                background-color: #333;
                color: #888;
                border: 1px solid #444;
            }
        """)

        vendor_layout.addWidget(self.vendor_auto_btn)

        nas_layout.addWidget(vendor_container, row, 1)

        # ═══════════════════════════════════════════════════════
        # Benutzerdefinierter Shutdown-Befehl (nur bei "custom")
        # ═══════════════════════════════════════════════════════
        row += 1
        self.custom_cmd_label = QLabel(tr("custom_cmd_label"))
        self.nas_labels["custom_cmd"] = self.custom_cmd_label
        nas_layout.addWidget(self.custom_cmd_label, row, 0)

        custom_cmd_container = QWidget()
        custom_cmd_layout = QHBoxLayout(custom_cmd_container)
        custom_cmd_layout.setContentsMargins(0, 0, 0, 0)
        custom_cmd_layout.setSpacing(6)

        self.custom_command_edit = QLineEdit()
        self.custom_command_edit.setPlaceholderText(
            "sudo shutdown -h now; sudo poweroff"
        )
        self.custom_command_edit.setToolTip(tr("custom_cmd_tooltip"))
        custom_cmd_layout.addWidget(self.custom_command_edit, stretch=1)

        # Hilfe-Button
        self.custom_cmd_help_btn = QPushButton("?")
        self.custom_cmd_help_btn.setObjectName("btn_custom_cmd_help")
        self.custom_cmd_help_btn.setToolTip(tr("custom_cmd_help_tooltip"))
        self.custom_cmd_help_btn.setFixedSize(30, 30)
        self.custom_cmd_help_btn.clicked.connect(self.show_shutdown_help)
        self.custom_cmd_help_btn.setStyleSheet("""
            QPushButton#btn_custom_cmd_help {
                background-color: #555;
                color: white;
                font-weight: bold;
                border-radius: 15px;
            }
            QPushButton#btn_custom_cmd_help:hover {
                background-color: #007AFF;
                border: 1px solid #ffffff;
            }
        """)
        custom_cmd_layout.addWidget(self.custom_cmd_help_btn)

        nas_layout.addWidget(custom_cmd_container, row, 1)

        # Hinweis-Text darunter
        row += 1
        self.custom_cmd_hint = QLabel(tr("custom_cmd_hint"))
        self.custom_cmd_hint.setStyleSheet(
            "color: #888888; font-size: 10px; padding: 2px 2px 2px 4px;"
        )
        self.custom_cmd_hint.setWordWrap(True)
        # Wird dynamisch ein-/ausgeblendet
        self.custom_cmd_hint_row = row
        nas_layout.addWidget(self.custom_cmd_hint, row, 0, 1, 2)

        # Referenzen für dynamisches Ein-/Ausblenden speichern
        self.custom_cmd_widgets = [
            self.custom_cmd_label,
            custom_cmd_container,
            self.custom_cmd_hint,
        ]

        row += 1
        label = QLabel(tr("config_nas_user"))
        self.nas_labels["nas_user"] = label
        nas_layout.addWidget(label, row, 0)
        self.nas_user_edit = QLineEdit()
        self.nas_user_edit.setPlaceholderText("z.B. nasuser")
        nas_layout.addWidget(self.nas_user_edit, row, 1)

        row += 1
        label = QLabel(tr("config_nas_dns"))
        self.nas_labels["nas_dns"] = label
        nas_layout.addWidget(label, row, 0)
        self.nas_dns_edit = QLineEdit()
        self.nas_dns_edit.setPlaceholderText("z.B. NAS-Synology.local")
        nas_layout.addWidget(self.nas_dns_edit, row, 1)

        row += 1
        label = QLabel(tr("config_nas_ip"))
        self.nas_labels["nas_ip"] = label
        nas_layout.addWidget(label, row, 0)
        ip_layout = QHBoxLayout()
        self.nas_ip_edit = QLineEdit()
        self.nas_ip_edit.setPlaceholderText("z.B. 192.168.1.100")
        ip_layout.addWidget(self.nas_ip_edit)
        self.find_ip_btn = QPushButton(tr("config_find_ip"))
        self.find_ip_btn.setObjectName("btn_find_ip")
        self.find_ip_btn.setToolTip(tr("config_find_ip_tooltip"))
        self.find_ip_btn.clicked.connect(self.find_server_ip)
        ip_layout.addWidget(self.find_ip_btn)
        nas_layout.addLayout(ip_layout, row, 1)

        row += 1
        label = QLabel(tr("config_nas_mac"))
        self.nas_labels["nas_mac"] = label
        nas_layout.addWidget(label, row, 0)
        mac_layout = QHBoxLayout()
        self.nas_mac_edit = QLineEdit()
        self.nas_mac_edit.setPlaceholderText("xx:xx:xx:xx:xx:xx")
        mac_layout.addWidget(self.nas_mac_edit)
        self.mac_find_btn = QPushButton(tr("config_mac_find"))
        self.mac_find_btn.setObjectName("btn_mac_help")
        self.mac_find_btn.setToolTip(tr("config_mac_find_tooltip"))
        # ⭐ Auto-Erkennung + Fallback auf Hilfe
        self.mac_find_btn.clicked.connect(self.auto_detect_mac_address)
        mac_layout.addWidget(self.mac_find_btn)
        nas_layout.addLayout(mac_layout, row, 1)

        row += 1
        label = QLabel(tr("config_ssh_key"))
        self.nas_labels["ssh_key"] = label
        nas_layout.addWidget(label, row, 0)
        self.ssh_key_edit = QLineEdit()
        self.ssh_key_edit.setPlaceholderText("~/.ssh/id_rsa")
        nas_layout.addWidget(self.ssh_key_edit, row, 1)

        row += 1
        empty_label = QLabel("")
        nas_layout.addWidget(empty_label, row, 0)

        ssh_btn_container = QWidget()
        ssh_btn_layout = QHBoxLayout(ssh_btn_container)
        ssh_btn_layout.setContentsMargins(0, 0, 0, 0)
        ssh_btn_layout.setSpacing(6)

        self.ssh_open_btn = QPushButton("📂 " + tr("config_ssh_open"))
        self.ssh_open_btn.setToolTip(tr("config_ssh_open_tooltip"))
        self.ssh_open_btn.clicked.connect(self.open_ssh_key_path)
        ssh_btn_layout.addWidget(self.ssh_open_btn)

        self.ssh_create_btn = QPushButton("🔑 " + tr("config_ssh_create"))
        self.ssh_create_btn.setToolTip(tr("config_ssh_create_tooltip"))
        self.ssh_create_btn.clicked.connect(self.create_ssh_keypair)
        ssh_btn_layout.addWidget(self.ssh_create_btn)

        self.ssh_help_btn = QPushButton(tr("config_ssh_help"))
        self.ssh_help_btn.setToolTip(tr("config_ssh_help_tooltip"))
        self.ssh_help_btn.clicked.connect(self.show_ssh_help)
        ssh_btn_layout.addWidget(self.ssh_help_btn)

        ssh_btn_layout.addStretch()
        nas_layout.addWidget(ssh_btn_container, row, 1)

        self.nas_group.setLayout(nas_layout)
        scroll_layout.addWidget(self.nas_group)

        # === JSON-Pfad ===
        self.json_group = QGroupBox(tr("config_json_path"))  # Referenz speichern
        json_layout = QHBoxLayout()
        self.json_path_label = QLabel(str(self.config.get_json_path()))
        self.json_path_label.setStyleSheet(
            "color: #888888; font-size: 11px; padding: 4px;"
        )
        self.json_path_label.setWordWrap(True)
        json_layout.addWidget(self.json_path_label, stretch=1)

        self.json_open_btn = QPushButton("📂 " + tr("config_json_open"))
        self.json_open_btn.setToolTip(tr("config_json_open_tooltip"))
        self.json_open_btn.clicked.connect(self.open_json_folder)
        json_layout.addWidget(self.json_open_btn)

        self.json_group.setLayout(json_layout)
        scroll_layout.addWidget(self.json_group)


        # ═══════════════ PASSWORT-VERWALTUNG ═══════════════
        self.password_group = QGroupBox(tr("clear_password_title"))
        password_layout = QHBoxLayout() # Button neben der Erklärung

        # Beschreibung
        self.pw_desc_label = QLabel(tr("clear_password_description"))
        self.pw_desc_label.setStyleSheet(
            "color: #888888; font-size: 11px; padding: 4px;"
        )
        self.pw_desc_label.setWordWrap(True)
        password_layout.addWidget(self.pw_desc_label)

        # Button
        self.clear_password_btn = QPushButton(tr("clear_password_button")
        )
        self.clear_password_btn.setObjectName("btn_clear_password")
        self.clear_password_btn.clicked.connect(self.clear_stored_password)
        # self.clear_password_btn.setStyleSheet(
        #     "QPushButton#btn_clear_password {"
        #     "  background-color: #d32f2f;"
        #     "  color: white;"
        #     "  font-weight: bold;"
        #     "  padding: 8px 16px;"
        #     "  min-width: 200px;"
        #     "}"
        #     "QPushButton#btn_clear_password:hover {"
        #     "  background-color: #b71c1c;"
        #     "  border: 1px solid #ffffff;"
        #     "}"
        # )

        password_layout.addWidget(self.clear_password_btn)

        self.password_group.setLayout(password_layout)
        scroll_layout.addWidget(self.password_group)

        scroll_layout.addStretch()

        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll)

    def auto_detect_vendor(self):
        """
        Erkennt den NAS-Hersteller per SSH und setzt die Combobox.
        Zeigt dem User eine Bestätigung, bevor der Wert übernommen wird.
        """
        # ─── Voraussetzungen prüfen ───
        nas_user = self.nas_user_edit.text().strip()
        nas_ip = self.nas_ip_edit.text().strip()
        ssh_key = self.ssh_key_edit.text().strip()

        if not nas_user or not nas_ip or not ssh_key:
            QMessageBox.warning(
                self,
                tr("vendor_label"),
                tr("vendor_detect_no_ssh_configured"),
            )
            return

        # ─── Button deaktivieren während Erkennung ───
        self.vendor_auto_btn.setEnabled(False)
        self.vendor_auto_btn.setText(tr("vendor_detect_in_progress"))

        # Text-Änderung sichtbar machen BEVOR der blockierende
        # SSH-Aufruf startet.
        self.vendor_auto_btn.repaint()
        self.vendor_auto_btn.update()
        QApplication.processEvents()
        QApplication.processEvents()
        time.sleep(0.1)
        QApplication.processEvents()

        # ─── Konfiguration vorübergehend setzen (für detect_nas_vendor) ───
        # Wir übergeben die aktuellen Werte aus den Eingabefeldern
        # (nicht aus self.config, weil der User sie gerade geändert haben könnte)
        original_user = self.config.get("nas_user", "")
        original_ip = self.config.get("nas_ip", "")
        original_key = self.config.get("ssh_key_path", "")

        self.config.set("nas_user", nas_user)
        self.config.set("nas_ip", nas_ip)
        self.config.set("ssh_key_path", ssh_key)

        try:
            # ─── GUI aktualisieren vor Erkennung ───
            QApplication.processEvents()

            # ─── Erkennung durchführen ───
            parent = self.parent()
            if parent and hasattr(parent, "detect_nas_vendor"):
                vendor_key, raw_output = parent.detect_nas_vendor()
            else:
                vendor_key, raw_output = None, "Parent hat keine detect_nas_vendor()"

            # ─── GUI aktualisieren nach Erkennung ───
            QApplication.processEvents()

            # ─── Sonderfall: SSH-Key fehlt ───
            if raw_output and raw_output.startswith("SSH-Key nicht gefunden:"):
                missing_path = raw_output.replace("SSH-Key nicht gefunden: ", "")
                QMessageBox.warning(
                    self,
                    tr("vendor_label"),
                    tr("vendor_detect_ssh_key_missing").format(missing_path),
                )
                self.logger.log_error(
                    "Auto-Erkennung: SSH-Key fehlt", missing_path
                )
            elif vendor_key:
                # ─── Erkennung erfolgreich ───
                # Aktuellen Wert ermitteln
                current_index = self.nas_vendor_combo.currentIndex()
                current_vendor_key = self.nas_vendor_combo.itemData(current_index)
                current_vendor_display = tr(f"vendor_{current_vendor_key}")

                detected_display = tr(f"vendor_{vendor_key}")

                # Wenn schon derselbe → nur Info
                if vendor_key == current_vendor_key:
                    QMessageBox.information(
                        self,
                        tr("vendor_label"),
                        tr("vendor_detect_success").format(detected_display),
                    )
                else:
                    # ⭐ Anderer Wert → mit übersetzten Ja/Nein-Buttons nachfragen
                    if self._msgbox_question(
                        tr("vendor_label"),
                        tr("vendor_detect_success_question").format(
                            detected_display, current_vendor_display
                        ),
                    ):
                        # Combobox setzen
                        new_index = self.nas_vendor_combo.findData(vendor_key)
                        if new_index >= 0:
                            self.nas_vendor_combo.setCurrentIndex(new_index)
                            self.status_label.setText(
                                tr("vendor_detect_success").format(detected_display)
                            )
                            self.status_label.setStyleSheet(
                                "color: #4CAF50; font-size: 11px; padding: 5px;"
                            )
            else:
                # ─── Erkennung fehlgeschlagen ───
                error_detail = raw_output if raw_output else ""
                error_lower = error_detail.lower()

                # Fallunterscheidung nach Fehlertyp (erweiterte Muster)
                ssh_key_errors = [
                    "permission denied",
                    "publickey",
                    "no supported authentication",
                    "host key verification failed",
                    "bad permissions",
                ]
                nas_offline_errors = [
                    "connection refused",
                    "no route to host",
                    "connection timed out",
                    "operation timed out",
                    "connection timeout",
                    "network is unreachable",
                    "could not resolve hostname",
                    "name or service not known",
                    "timeout",
                    "timed out",
                ]

                if any(p in error_lower for p in ssh_key_errors):
                    # SSH-Key nicht akzeptiert
                    QMessageBox.warning(
                        self,
                        tr("vendor_label"),
                        tr("vendor_detect_no_ssh"),
                    )
                elif any(p in error_lower for p in nas_offline_errors):
                    # NAS nicht erreichbar
                    QMessageBox.warning(
                        self,
                        tr("vendor_label"),
                        tr("vendor_detect_nas_offline"),
                    )
                else:
                    # Unbekannter Fehler
                    QMessageBox.warning(
                        self,
                        tr("vendor_label"),
                        tr("vendor_detect_failed"),
                    )

                self.logger.log_action(
                    "Auto-Erkennung fehlgeschlagen",
                    f"Detail: {error_detail[:300]}",
                )

        except Exception as e:
            self.logger.log_error(
                "Fehler bei Auto-Erkennung", str(e), e
            )
            QMessageBox.warning(
                self,
                tr("vendor_label"),
                tr("vendor_detect_error").format(str(e)),
            )
        finally:
            # ─── Button reaktivieren ───
            self.vendor_auto_btn.setEnabled(True)
            self.vendor_auto_btn.setText(tr("vendor_auto_detect"))

    def on_vendor_changed(self, index: int):
        """
        Wird aufgerufen, wenn der Hersteller in der Combobox geändert wird.
        Blendet das Benutzerdefiniert-Feld ein oder aus.
        """
        try:
            vendor_key = self.nas_vendor_combo.itemData(index)
            is_custom = (vendor_key == "custom")

            # Alle Custom-Widgets ein-/ausblenden
            for widget in self.custom_cmd_widgets:
                widget.setVisible(is_custom)

            self.logger.log_action(
                "Hersteller geändert",
                f"Neu: {vendor_key} (Benutzerdefiniert: {is_custom})",
            )
        except Exception as e:
            self.logger.log_error(
                "Fehler bei on_vendor_changed", str(e), e
            )

    def show_shutdown_help(self):
        """Zeigt einen Dialog mit typischen Shutdown-Befehlen."""
        help_text = tr("custom_cmd_help_text")
        QMessageBox.information(
            self,
            tr("custom_cmd_help_title"),
            help_text,
        )

    def _init_volumes_tab(self):
        """Initialisiert den Volumes-Tab mit Liste, Checkboxen und zweizeiligen Buttons."""
        layout = QVBoxLayout(self.volumes_tab)
        layout.setSpacing(10)

        self.volumes_group = QGroupBox(tr("config_volumes_group"))
        volumes_layout = QVBoxLayout()

        # Titelzeile
        title_layout = QHBoxLayout()
        self.volumes_title_label = QLabel(tr("volumes_title"))
        self.volumes_title_label.setObjectName("volumes_title")
        title_layout.addWidget(self.volumes_title_label)
        title_layout.addStretch()
        self.select_all_btn_vol = QPushButton(tr("btn_select_all"))
        self.select_all_btn_vol.setCheckable(True)
        self.select_all_btn_vol.clicked.connect(self.toggle_all_volumes_dialog)
        title_layout.addWidget(self.select_all_btn_vol)
        volumes_layout.addLayout(title_layout)

        # ═══════════════════════════════════════════════════════
        # Info-Panel für Volume-Erkennungs-Status (nur bei Erkennung sichtbar)
        # ═══════════════════════════════════════════════════════
        self.volume_detect_panel = QFrame()
        self.volume_detect_panel.setObjectName("volume_detect_panel")
        self.volume_detect_panel.setStyleSheet("""
            QFrame#volume_detect_panel {
                background-color: #1a1a1a;
                border: 1px solid #333;
                border-radius: 4px;
                padding: 8px;
            }
        """)
        detect_panel_layout = QHBoxLayout(self.volume_detect_panel)
        detect_panel_layout.setContentsMargins(10, 8, 10, 8)
        detect_panel_layout.setSpacing(10)

        # Icon/Label links
        self.volume_detect_icon = QLabel("")
        self.volume_detect_icon.setStyleSheet(
            "font-size: 16px; padding: 0; background: transparent;"
        )
        self.volume_detect_icon.setFixedWidth(24)
        self.volume_detect_icon.setAlignment(Qt.AlignCenter)
        detect_panel_layout.addWidget(self.volume_detect_icon)

        # Status-Text
        self.volume_detect_label = QLabel("")
        self.volume_detect_label.setStyleSheet(
            "color: #ffffff; font-size: 12px; background: transparent;"
        )
        self.volume_detect_label.setWordWrap(True)
        detect_panel_layout.addWidget(self.volume_detect_label, stretch=1)

        # Fortschrittsbalken (nur während Erkennung sichtbar)
        self.volume_detect_progress = QProgressBar()
        self.volume_detect_progress.setRange(0, 0)  # Indeterminate
        self.volume_detect_progress.setFixedWidth(120)
        self.volume_detect_progress.setFixedHeight(8)
        self.volume_detect_progress.setTextVisible(False)
        self.volume_detect_progress.setStyleSheet("""
            QProgressBar {
                border: none;
                border-radius: 4px;
                background-color: #333;
            }
            QProgressBar::chunk {
                background-color: #007AFF;
                border-radius: 4px;
            }
        """)
        detect_panel_layout.addWidget(self.volume_detect_progress)

        # Standardmäßig unsichtbar
        self.volume_detect_panel.setVisible(False)
        volumes_layout.addWidget(self.volume_detect_panel)

        # Liste
        self.volume_list_widget = QListWidget()
        self.volume_list_widget.setSelectionMode(QListWidget.SingleSelection)
        self.volume_list_widget.setDragDropMode(QListWidget.InternalMove)
        self.volume_list_widget.setStyleSheet("""
            QListWidget::item { padding: 5px; }
            QListWidget::item:selected { background-color: #007AFF; color: white; }
        """)
        volumes_layout.addWidget(self.volume_list_widget)

        # Buttons in 2 Zeilen (GridLayout) – für schmale GUI geeignet
        btn_grid = QGridLayout()
        btn_grid.setSpacing(8)
        btn_grid.setColumnStretch(0, 1)
        btn_grid.setColumnStretch(1, 1)
        btn_grid.setColumnStretch(2, 1)

        # Zeile 1
        self.move_up_btn = QPushButton("↑ " + tr("volumes_move_up"))
        self.move_up_btn.setObjectName("vol_up")
        self.move_up_btn.clicked.connect(self.move_volume_up)
        btn_grid.addWidget(self.move_up_btn, 0, 0)

        self.move_down_btn = QPushButton("↓ " + tr("volumes_move_down"))
        self.move_down_btn.setObjectName("vol_down")
        self.move_down_btn.clicked.connect(self.move_volume_down)
        btn_grid.addWidget(self.move_down_btn, 0, 1)  # 0=1.Zeile und 1=2. Button

        # Zeile 2
        self.detect_btn = QPushButton(tr("volumes_auto_detect"))
        self.detect_btn.setObjectName("vol_detect")
        self.detect_btn.clicked.connect(self.detect_volumes)
        btn_grid.addWidget(self.detect_btn, 1, 0)

        self.add_btn = QPushButton(tr("volumes_add"))
        self.add_btn.setObjectName("vol_add")
        self.add_btn.clicked.connect(self.add_volume)
        btn_grid.addWidget(self.add_btn, 1, 1)

        self.delete_btn = QPushButton(tr("volumes_delete"))
        self.delete_btn.setObjectName("vol_delete")
        self.delete_btn.clicked.connect(self.delete_volume)
        btn_grid.addWidget(self.delete_btn, 1, 2)

        volumes_layout.addLayout(btn_grid)

        # Hinweis
        self.volumes_hint = QLabel(tr("volumes_hint"))
        self.volumes_hint.setStyleSheet("color: #888888; font-size: 11px;")
        self.volumes_hint.setWordWrap(True)
        volumes_layout.addWidget(self.volumes_hint)

        self.volumes_group.setLayout(volumes_layout)
        layout.addWidget(self.volumes_group)
        layout.addStretch()

        self.load_volumes_into_list()

    def load_volumes_into_list(self):
        """Lädt die Volume-Liste aus der Konfiguration in die QListWidget."""
        self.volume_list_widget.clear()
        volume_state = self.config.get("volume_list_with_state", [])
        if not volume_state:
            # Fallback: aus volume_list eine Liste mit aktiv erstellen
            volume_names = self.config.get("volume_list", [])
            volume_state = [{"name": v, "checked": True} for v in volume_names]
        for entry in volume_state:
            name = entry.get("name", "")
            checked = entry.get("checked", True)
            item = QListWidgetItem(name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked if checked else Qt.Unchecked)
            # Erstes Item ist immer aktiv und nicht deaktivierbar
            if self.volume_list_widget.count() == 0:
                item.setFlags(item.flags() & ~Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Checked)
            self.volume_list_widget.addItem(item)
        self.update_select_all_button_state()

    def update_select_all_button_state(self):
        """Aktualisiert den Zustand des 'Alle'-Buttons basierend auf den Checkboxen."""
        count = self.volume_list_widget.count()
        if count == 0:
            self.select_all_btn_vol.setChecked(False)
            self.select_all_btn_vol.setEnabled(False)
            return
        all_checked = True
        for i in range(1, count):  # erstes überspringen
            item = self.volume_list_widget.item(i)
            if item.checkState() != Qt.Checked:
                all_checked = False
                break
        self.select_all_btn_vol.setChecked(all_checked)
        self.select_all_btn_vol.setEnabled(True)

    def toggle_all_volumes_dialog(self, checked):
        """Setzt alle deaktivierbaren Volumes auf den Zustand von checked."""
        count = self.volume_list_widget.count()
        for i in range(1, count):  # erstes überspringen
            item = self.volume_list_widget.item(i)
            item.setCheckState(Qt.Checked if checked else Qt.Unchecked)
        self.update_select_all_button_state()

    def detect_volumes(self):
        """
        Erkennt verfügbare Volumes auf dem NAS und fügt sie der Liste hinzu.
        """
        try:
            # ─── Info-Panel + Button-Feedback sofort ───
            self._set_volume_detect_status("running")

            self.detect_btn.setEnabled(False)
            original_btn_text = self.detect_btn.text()
            self.detect_btn.setText(tr("volumes_detection_in_progress"))
            self.detect_btn.repaint()
            self.detect_btn.update()
            QApplication.processEvents()

            # ─── Aktuelle Dialogwerte in die Config übernehmen ───
            current_vendor = self.nas_vendor_combo.currentData() or "synology"
            current_user = self.nas_user_edit.text().strip()
            current_ip = self.nas_ip_edit.text().strip()
            current_key = self.ssh_key_edit.text().strip()

            self.config.set("nas_vendor", current_vendor)
            self.config.set("nas_user", current_user)
            self.config.set("nas_ip", current_ip)
            self.config.set("ssh_key_path", current_key)

            self.logger.log_action(
                "Volume-Erkennung: Nutze aktuelle Dialogwerte",
                f"Hersteller: {current_vendor}, IP: {current_ip}",
            )

            # ─── Erkennung via AnyNasPy ───
            detected = []
            parent = self.parent()
            if parent and hasattr(parent, "detect_nas_volumes"):
                QApplication.processEvents()
                detected = parent.detect_nas_volumes() or []
                QApplication.processEvents()
                self.logger.log_action(
                    "Volume-Erkennung über AnyNasPy",
                    f"{len(detected)} Volumes gefunden",
                )

            # ─── Fallback smbclient ───
            if not detected:
                self.logger.log_action(
                    "Volume-Erkennung Fallback smbclient (in ConfigDialog)"
                )
                detected = self._detect_volumes_via_smbclient()

            # ─── Volumes zur Liste hinzufügen ───
            if detected:
                existing_names = set()
                for i in range(self.volume_list_widget.count()):
                    existing_names.add(self.volume_list_widget.item(i).text())

                added = 0
                for name in detected:
                    if name not in existing_names:
                        item = QListWidgetItem(name)
                        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                        item.setCheckState(Qt.Checked)
                        if self.volume_list_widget.count() == 0:
                            item.setFlags(item.flags() & ~Qt.ItemIsUserCheckable)
                            item.setCheckState(Qt.Checked)
                        self.volume_list_widget.addItem(item)
                        added += 1

                existing_count = len(detected) - added

                if added > 0:
                    self._set_volume_detect_status(
                        "success",
                        found=len(detected),
                        added=added,
                        existing=existing_count,
                    )
                    self.logger.log_action(
                        "Volumes hinzugefügt", f"{added} neue Volumes"
                    )
                else:
                    # Keine neuen — aber welche gefunden
                    self._set_volume_detect_status(
                        "partial",
                        found=len(detected),
                        existing=existing_count,
                    )
                    self.logger.log_action(
                        "Keine neuen Volumes",
                        f"Alle {len(detected)} bereits in der Liste",
                    )
            else:
                self._set_volume_detect_status("failed")
                self.logger.log_error(
                    "Volume-Erkennung fehlgeschlagen",
                    "Weder SSH-Pfade noch smbclient haben Volumes gefunden",
                )

        except Exception as e:
            self.logger.log_error("Volume detection failed", str(e), e)
            self._set_volume_detect_status("failed")
        finally:
            # Button wieder aktivieren
            self.detect_btn.setEnabled(True)
            if 'original_btn_text' in locals():
                self.detect_btn.setText(original_btn_text)
            self.detect_btn.repaint()
            QApplication.processEvents()

        self.update_select_all_button_state()

    def _detect_volumes_via_smbclient(self) -> list:
        """
        Fallback-Methode: Erkennt Volumes via smbclient über SSH.
        """
        try:
            nas_ip = self.config.get("nas_ip")
            nas_user = self.config.get("nas_user")
            ssh_key = self.config.get("ssh_key_path")

            # SSH-Key expandieren (~ → /Users/...)
            expanded_key = os.path.expanduser(ssh_key)

            if not os.path.exists(expanded_key):
                self.logger.log_error(
                    "Fallback smbclient: SSH-Key nicht gefunden",
                    f"Pfad: {expanded_key}",
                )
                return []

            self.logger.log_action(
                "Fallback smbclient: SSH-Aufruf",
                f"{nas_user}@{nas_ip}",
            )

            cmd = [
                "ssh",
                "-i", expanded_key,
                "-o", "ConnectTimeout=5",
                "-o", "BatchMode=yes",
                "-o", "StrictHostKeyChecking=no",
                f"{nas_user}@{nas_ip}",
                "smbclient -L localhost -N 2>/dev/null | "
                "grep -E '^[A-Za-z0-9_]+[[:space:]]+Disk' | awk '{print $1}'",
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=15
            )

            self.logger.log_action(
                "Fallback smbclient Ergebnis",
                f"rc={result.returncode}, "
                f"stdout_len={len(result.stdout)}, "
                f"stderr='{result.stderr.strip()[:100]}'",
            )

            if result.returncode == 0 and result.stdout.strip():
                volumes = [
                    line.strip()
                    for line in result.stdout.splitlines()
                    if line.strip()
                ]
                return volumes
            return []
        except Exception as e:
            self.logger.log_error(
                "Fallback smbclient fehlgeschlagen", str(e), e
            )
            return []

    def _set_volume_detect_status(self, state: str, found: int = 0,
                                   added: int = 0, existing: int = 0):
        """
        Aktualisiert das Info-Panel für die Volume-Erkennung.

        Args:
            state: "running" | "success" | "partial" | "failed" | "hidden"
            found: Anzahl gefundener Volumes
            added: Anzahl neu hinzugefügter Volumes
            existing: Anzahl bereits vorhandener Volumes
        """
        try:
            if state == "hidden":
                self.volume_detect_panel.setVisible(False)
                return

            # Panel sichtbar machen
            self.volume_detect_panel.setVisible(True)

            if state == "running":
                self.volume_detect_icon.setText("🔄")
                self.volume_detect_label.setText(
                    tr("volumes_detect_panel_running")
                )
                self.volume_detect_progress.setVisible(True)
                self.volume_detect_panel.setStyleSheet("""
                    QFrame#volume_detect_panel {
                        background-color: #2a1f00;
                        border: 1px solid #554400;
                        border-radius: 4px;
                        padding: 8px;
                    }
                """)

            elif state == "success":
                self.volume_detect_icon.setText("✅")
                self.volume_detect_label.setText(
                    tr("volumes_detect_panel_success").format(
                        found, added, existing
                    )
                )
                self.volume_detect_progress.setVisible(False)
                self.volume_detect_panel.setStyleSheet("""
                    QFrame#volume_detect_panel {
                        background-color: #1a3a1a;
                        border: 1px solid #2e5c2e;
                        border-radius: 4px;
                        padding: 8px;
                    }
                """)

            elif state == "partial":
                self.volume_detect_icon.setText("⚠")
                self.volume_detect_label.setText(
                    tr("volumes_detect_panel_partial").format(
                        found, existing
                    )
                )
                self.volume_detect_progress.setVisible(False)
                self.volume_detect_panel.setStyleSheet("""
                    QFrame#volume_detect_panel {
                        background-color: #2a1f00;
                        border: 1px solid #554400;
                        border-radius: 4px;
                        padding: 8px;
                    }
                """)

            elif state == "failed":
                self.volume_detect_icon.setText("❌")
                self.volume_detect_label.setText(
                    tr("volumes_detect_panel_failed")
                )
                self.volume_detect_progress.setVisible(False)
                self.volume_detect_panel.setStyleSheet("""
                    QFrame#volume_detect_panel {
                        background-color: #3a1a1a;
                        border: 1px solid #5c2e2e;
                        border-radius: 4px;
                        padding: 8px;
                    }
                """)

            QApplication.processEvents()
        except Exception as e:
            self.logger.log_error(
                "Fehler beim Aktualisieren des Volume-Status-Panels",
                str(e),
                e,
            )

    def add_volume(self):
        """Fügt manuell ein neues Volume hinzu."""
        name, ok = QInputDialog.getText(
            self, tr("volumes_add"), tr("volumes_enter_name"), QLineEdit.Normal, ""
        )
        if not ok or not name.strip():
            return
        name = name.strip()
        for i in range(self.volume_list_widget.count()):
            if self.volume_list_widget.item(i).text() == name:
                QMessageBox.warning(self, tr("volumes_add"), tr("volumes_name_exists"))
                return
        item = QListWidgetItem(name)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Checked)
        if self.volume_list_widget.count() == 0:
            item.setFlags(item.flags() & ~Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked)
        self.volume_list_widget.addItem(item)
        self.update_select_all_button_state()

    def delete_volume(self):
        """Löscht das ausgewählte Volume (außer dem ersten)."""
        current_row = self.volume_list_widget.currentRow()
        if current_row < 0:
            QMessageBox.information(self, tr("volumes_delete"), tr("msg_select_volume"))
            return
        if current_row == 0:
            QMessageBox.warning(
                self, tr("volumes_delete"), tr("msg_cannot_delete_main_volume")
            )
            return
        item = self.volume_list_widget.item(current_row)
        reply = QMessageBox.question(
            self,
            tr("volumes_delete"),
            tr("volumes_confirm_delete").format(item.text()),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.volume_list_widget.takeItem(current_row)
            self.update_select_all_button_state()

    def move_volume_up(self):
        """Verschiebt das ausgewählte Volume eine Position nach oben."""
        row = self.volume_list_widget.currentRow()
        if row <= 0:
            return
        item = self.volume_list_widget.takeItem(row)
        self.volume_list_widget.insertItem(row - 1, item)
        self.volume_list_widget.setCurrentRow(row - 1)
        self._fix_first_item_flags()

    def move_volume_down(self):
        """Verschiebt das ausgewählte Volume eine Position nach unten."""
        row = self.volume_list_widget.currentRow()
        if row < 0 or row >= self.volume_list_widget.count() - 1:
            return
        item = self.volume_list_widget.takeItem(row)
        self.volume_list_widget.insertItem(row + 1, item)
        self.volume_list_widget.setCurrentRow(row + 1)
        self._fix_first_item_flags()

    def _fix_first_item_flags(self):
        """Stellt sicher, dass das erste Item immer aktiv und nicht deaktivierbar ist."""
        if self.volume_list_widget.count() > 0:
            first = self.volume_list_widget.item(0)
            first.setFlags(first.flags() & ~Qt.ItemIsUserCheckable)
            first.setCheckState(Qt.Checked)
            for i in range(1, self.volume_list_widget.count()):
                item = self.volume_list_widget.item(i)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)

    ### Tab Zeiteinstellungen

    def _init_timing_tab(self):
        """Initialisiert den Timing-Tab."""
        layout = QVBoxLayout(self.timing_tab)
        layout.setSpacing(15)

        self.time_group = QGroupBox(tr("config_time_group"))
        time_layout = QGridLayout()
        time_layout.setSpacing(10)

        self.time_labels = {}

        row = 0
        label = QLabel(tr("config_auto_shutdown"))
        self.time_labels["auto_shutdown"] = label
        time_layout.addWidget(label, row, 0)
        self.auto_shutdown_spin = QSpinBox()
        self.auto_shutdown_spin.setRange(10, 600)
        self.auto_shutdown_spin.setSuffix(" s")
        time_layout.addWidget(self.auto_shutdown_spin, row, 1)

        row += 1
        label = QLabel(tr("config_auto_start"))
        self.time_labels["auto_start"] = label
        time_layout.addWidget(label, row, 0)
        self.auto_start_spin = QSpinBox()
        self.auto_start_spin.setRange(10, 600)
        self.auto_start_spin.setSuffix(" s")
        time_layout.addWidget(self.auto_start_spin, row, 1)

        row += 1
        label = QLabel(tr("config_wol_wait"))
        self.time_labels["wol_wait"] = label
        time_layout.addWidget(label, row, 0)
        self.wol_wait_spin = QSpinBox()
        self.wol_wait_spin.setRange(30, 600)
        self.wol_wait_spin.setSuffix(" s")
        time_layout.addWidget(self.wol_wait_spin, row, 1)

        row += 1
        label = QLabel(tr("config_smb_wait"))
        self.time_labels["smb_wait"] = label
        time_layout.addWidget(label, row, 0)
        self.smb_wait_spin = QSpinBox()
        self.smb_wait_spin.setRange(5, 120)
        self.smb_wait_spin.setSuffix(" s")
        time_layout.addWidget(self.smb_wait_spin, row, 1)

        row += 1
        label = QLabel(tr("config_mount_retries"))
        self.time_labels["mount_retries"] = label
        time_layout.addWidget(label, row, 0)
        self.mount_retries_spin = QSpinBox()
        self.mount_retries_spin.setRange(1, 10)
        time_layout.addWidget(self.mount_retries_spin, row, 1)

        # Zeile für shutdown_mac_delay
        row = 5  # nach mount_retries
        label = QLabel(tr("config_shutdown_mac_delay"))
        self.time_labels["shutdown_mac_delay"] = label
        time_layout.addWidget(label, row, 0)
        self.shutdown_mac_delay_spin = QSpinBox()
        self.shutdown_mac_delay_spin.setRange(0, 30)  # 0-30 Sekunden
        self.shutdown_mac_delay_spin.setSuffix(" s")
        time_layout.addWidget(self.shutdown_mac_delay_spin, row, 1)

        self.time_group.setLayout(time_layout)
        layout.addWidget(self.time_group)
        layout.addStretch()

    def _init_profiles_tab(self):
        """Initialisiert den Profile-Tab."""
        layout = QVBoxLayout(self.profiles_tab)
        layout.setContentsMargins(0, 0, 0, 0)

        # Profile-Management-Widget einbetten
        self.profile_dialog = ProfileDialog(self.config.profile_manager, self)
        # Wir verwenden den Dialog als Widget
        layout.addWidget(self.profile_dialog)

    def on_language_changed(self, index):
        """Wird aufgerufen, wenn die Sprache in der ComboBox geändert wird."""
        if index < 0:
            return

        lang_code = self.lang_combo.itemData(index)
        if lang_code and lang_code != LANG.current_language:
            LANG.set_language(lang_code)
            self.status_label.setText(f"✓ Sprache: {LANG.get_language_name(lang_code)}")
            self.status_label.setStyleSheet(
                "color: #00FF00; font-size: 11px; padding: 5px;"
            )
            QTimer.singleShot(2000, lambda: self.status_label.setText(""))

    def update_ui_language(self):
        if self._updating_language:
            return
        self._updating_language = True
        try:
            # Fenstertitel
            self.setWindowTitle(tr("config_title"))

            # Tab-Titel
            self.tab_widget.setTabText(0, tr("config_tab_general"))
            self.tab_widget.setTabText(1, tr("config_tab_volumes"))
            self.tab_widget.setTabText(2, tr("config_tab_timing"))
            self.tab_widget.setTabText(3, tr("config_tab_profiles"))

            # Sprache-Gruppe
            if self.language_group:
                self.language_group.setTitle(tr("language"))

            # Sprachausgabe-Gruppe
            if hasattr(self, "speech_group"):
                self.speech_group.setTitle(tr("speech_enabled_label"))
            if hasattr(self, "speech_checkbox"):
                self.speech_checkbox.setText(tr("speech_enabled_label"))
            if hasattr(self, "speech_hint_label"):
                self.speech_hint_label.setText(tr("speech_enabled_hint"))
                self.language_group.setTitle(tr("language"))

            # Allgemein - NAS
            self.nas_group.setTitle(tr("config_nas_group"))
            if "nas_vendor" in self.nas_labels:
                self.nas_labels["nas_vendor"].setText(tr("vendor_label"))
            if "nas_user" in self.nas_labels:
                self.nas_labels["nas_user"].setText(tr("config_nas_user"))
                self.nas_labels["nas_user"].setText(tr("config_nas_user"))
            if "nas_dns" in self.nas_labels:
                self.nas_labels["nas_dns"].setText(tr("config_nas_dns"))
            if "nas_ip" in self.nas_labels:
                self.nas_labels["nas_ip"].setText(tr("config_nas_ip"))
            if "nas_mac" in self.nas_labels:
                self.nas_labels["nas_mac"].setText(tr("config_nas_mac"))
            if "ssh_key" in self.nas_labels:
                self.nas_labels["ssh_key"].setText(tr("config_ssh_key"))

            self.find_ip_btn.setText(tr("config_find_ip"))
            self.find_ip_btn.setToolTip(tr("config_find_ip_tooltip"))
            self.mac_find_btn.setText(tr("config_mac_find"))
            self.mac_find_btn.setToolTip(tr("config_mac_find_tooltip"))

            # SSH-Buttons
            self.ssh_open_btn.setText("📂 " + tr("config_ssh_open"))
            self.ssh_open_btn.setToolTip(tr("config_ssh_open_tooltip"))
            self.ssh_create_btn.setText("🔑 " + tr("config_ssh_create"))
            self.ssh_create_btn.setToolTip(tr("config_ssh_create_tooltip"))
            self.ssh_help_btn.setText(tr("config_ssh_help"))
            self.ssh_help_btn.setToolTip(tr("config_ssh_help_tooltip"))

            # JSON-Gruppe
            if self.json_group:
                self.json_group.setTitle(tr("config_json_path"))
            self.json_open_btn.setText("📂 " + tr("config_json_open"))
            self.json_open_btn.setToolTip(tr("config_json_open_tooltip"))

            # Passwort-Verwaltung
            if hasattr(self, "password_group"):
                self.password_group.setTitle(tr("clear_password_title"))
            if hasattr(self, "clear_password_btn"):
                self.clear_password_btn.setText(
                    "🗑  " + tr("clear_password_button")
                )
            # Beschreibung neu setzen (falls Referenz vorhanden)
            if hasattr(self, "pw_desc_label"):
                self.pw_desc_label.setText(tr("clear_password_description"))

            # Volumes-Tab
            self.volumes_group.setTitle(tr("config_volumes_group"))
            self.volumes_title_label.setText(tr("volumes_title"))
            self.volumes_hint.setText(tr("volumes_hint"))
            self.detect_btn.setText(tr("volumes_auto_detect"))
            self.add_btn.setText(tr("volumes_add"))
            self.delete_btn.setText(tr("volumes_delete"))
            self.move_up_btn.setText("↑ " + tr("volumes_move_up"))
            self.move_down_btn.setText("↓ " + tr("volumes_move_down"))
            self.select_all_btn_vol.setText(tr("btn_select_all"))

            # Timing
            self.time_group.setTitle(tr("config_time_group"))
            if "auto_shutdown" in self.time_labels:
                self.time_labels["auto_shutdown"].setText(tr("config_auto_shutdown"))
            if "auto_start" in self.time_labels:
                self.time_labels["auto_start"].setText(tr("config_auto_start"))
            if "wol_wait" in self.time_labels:
                self.time_labels["wol_wait"].setText(tr("config_wol_wait"))
            if "smb_wait" in self.time_labels:
                self.time_labels["smb_wait"].setText(tr("config_smb_wait"))
            if "mount_retries" in self.time_labels:
                self.time_labels["mount_retries"].setText(tr("config_mount_retries"))
            if "shutdown_mac_delay" in self.time_labels:
                self.time_labels["shutdown_mac_delay"].setText(
                    tr("config_shutdown_mac_delay")
                )

            # ⭐ Hersteller-Namen in der Combobox aktualisieren
            if hasattr(self, "nas_vendor_combo"):
                # Aktuellen Wert merken
                current_vendor = self.nas_vendor_combo.currentData()
                # Alle Items neu setzen
                for i in range(self.nas_vendor_combo.count()):
                    vendor_key = self.nas_vendor_combo.itemData(i)
                    display_name = tr(f"vendor_{vendor_key}")
                    self.nas_vendor_combo.setItemText(i, display_name)
                # Aktuellen Wert wiederherstellen
                if current_vendor:
                    idx = self.nas_vendor_combo.findData(current_vendor)
                    if idx >= 0:
                        self.nas_vendor_combo.setCurrentIndex(idx)
                # Tooltip aktualisieren
                self.nas_vendor_combo.setToolTip(tr("vendor_tooltip"))

            # ⭐ Auto-Erkennen-Button aktualisieren
            if hasattr(self, "vendor_auto_btn"):
                self.vendor_auto_btn.setText(tr("vendor_auto_detect"))
                self.vendor_auto_btn.setToolTip(
                    tr("vendor_auto_detect_tooltip")
                )

            # ⭐ Benutzerdefiniert-Labels aktualisieren
            if hasattr(self, "custom_cmd_label"):
                self.custom_cmd_label.setText(tr("custom_cmd_label"))
            if hasattr(self, "custom_command_edit"):
                self.custom_command_edit.setToolTip(tr("custom_cmd_tooltip"))
            if hasattr(self, "custom_cmd_help_btn"):
                self.custom_cmd_help_btn.setToolTip(
                    tr("custom_cmd_help_tooltip")
                )
            if hasattr(self, "custom_cmd_hint"):
                self.custom_cmd_hint.setText(tr("custom_cmd_hint"))
                self.vendor_auto_btn.setText(tr("vendor_auto_detect"))
                self.vendor_auto_btn.setToolTip(
                    tr("vendor_auto_detect_tooltip")
                )
                # Aktuellen Wert merken
                current_vendor = self.nas_vendor_combo.currentData()
                # Alle Items neu setzen
                for i in range(self.nas_vendor_combo.count()):
                    vendor_key = self.nas_vendor_combo.itemData(i)
                    display_name = tr(f"vendor_{vendor_key}")
                    self.nas_vendor_combo.setItemText(i, display_name)
                # Aktuellen Wert wiederherstellen
                if current_vendor:
                    idx = self.nas_vendor_combo.findData(current_vendor)
                    if idx >= 0:
                        self.nas_vendor_combo.setCurrentIndex(idx)
                # Tooltip aktualisieren
                self.nas_vendor_combo.setToolTip(tr("vendor_tooltip"))

            # Aktives Profil-Label direkt setzen
            if self.profile_header_label:
                profile_name = self.config.get_active_profile_name() or "Kein Profil"
                self.profile_header_label.setText(
                    f"📌 {tr('config_profile_active')}: {profile_name}"
                )

            # Profile-Tab wird über den eingebetteten Dialog aktualisiert
            if hasattr(self, "profile_dialog"):
                self.profile_dialog.update_ui_language()

            # NEU v2.2.0: Nur-Mac-Button
            self.button_mac_only.setText(f"⏼ {tr('btn_shutdown_mac_only')}")
            self.button_mac_only.setToolTip(tr("tooltip_shutdown_mac_only"))

            # NEU v2.2.0: Zeitgeber-Button (abhängig von online/offline/aktiv)
            self._update_scheduled_button_text()
            self.button_scheduled.setText(tr("btn_scheduled_shutdown"))
            self.button_scheduled.setToolTip(tr("tooltip_scheduled_shutdown"))

        except Exception as e:
            self.debug_log(f"EXCEPTION in update_ui_language: {e}")
            import traceback

            self.debug_log(traceback.format_exc())
        finally:
            self._updating_language = False

    def closeEvent(self, event):
        """Entfernt den Listener beim Schließen."""
        # self.debug_log("=== closeEvent ===")
        LANG.remove_listener(self.update_ui_language)
        super().closeEvent(event)

    def load_values(self):
        """Lädt die aktuellen Konfigurationswerte in die GUI."""
        # ⭐ NAS-Hersteller setzen (NEU in v2.3.0)
        saved_vendor = self.config.get("nas_vendor", "synology")
        vendor_index = self.nas_vendor_combo.findData(saved_vendor)
        if vendor_index >= 0:
            self.nas_vendor_combo.setCurrentIndex(vendor_index)
        else:
            # Fallback: synology
            fallback_index = self.nas_vendor_combo.findData("synology")
            if fallback_index >= 0:
                self.nas_vendor_combo.setCurrentIndex(fallback_index)

        # ⭐ Benutzerdefinierter Befehl laden
        self.custom_command_edit.setText(
            self.config.get("custom_shutdown_command", "sudo shutdown -h now")
        )

        # ⭐ Custom-Widgets ein-/ausblenden (je nach Vendor)
        self.on_vendor_changed(self.nas_vendor_combo.currentIndex())
        # Fallback: synology
        fallback_index = self.nas_vendor_combo.findData("synology")
        if fallback_index >= 0:
            self.nas_vendor_combo.setCurrentIndex(fallback_index)

        self.nas_user_edit.setText(self.config.get("nas_user", ""))
        self.nas_dns_edit.setText(self.config.get("nas_dns", ""))
        self.nas_ip_edit.setText(self.config.get("nas_ip", ""))
        self.nas_mac_edit.setText(self.config.get("nas_mac", ""))
        self.ssh_key_edit.setText(self.config.get("ssh_key_path", ""))
        self.load_volumes_into_list()

        self.auto_shutdown_spin.setValue(self.config.get("auto_shutdown_delay", 120))
        self.auto_start_spin.setValue(self.config.get("auto_start_delay", 120))
        self.wol_wait_spin.setValue(self.config.get("wol_wait_time", 180))
        self.smb_wait_spin.setValue(self.config.get("smb_wait_time", 30))
        self.mount_retries_spin.setValue(self.config.get("mount_retries", 3))
        self.shutdown_mac_delay_spin.setValue(self.config.get("shutdown_mac_delay", 5))

        self.json_path_label.setText(str(self.config.get_json_path()))

        profile_name = self.config.get_active_profile_name() or "Kein Profil"
        if self.profile_header_label:
            self.profile_header_label.setText(
                f"📌 {tr('config_profile_active')}: {profile_name}"
            )

        current_lang = LANG.current_language
        index = self.lang_combo.findData(current_lang)
        if index >= 0:
            self.lang_combo.setCurrentIndex(index)

    def save_and_accept(self):
        """Speichert die Werte und schließt den Dialog."""
        print("=" * 60)
        print("SAVE_AND_ACCEPT - START")
        print("=" * 60)

        # ⭐ NAS-Hersteller auslesen (NEU in v2.3.0)
        nas_vendor = self.nas_vendor_combo.currentData() or "synology"
        self.logger.log_action(
            "NAS-Hersteller aus Combobox gelesen",
            f"Wert: {nas_vendor}",
        )

        # ⭐ Benutzerdefinierter Befehl
        custom_shutdown_command = self.custom_command_edit.text().strip()
        if not custom_shutdown_command:
            custom_shutdown_command = "sudo shutdown -h now"

        # Werte aus GUI holen
        nas_user = self.nas_user_edit.text().strip()
        nas_dns = self.nas_dns_edit.text().strip()
        nas_ip = self.nas_ip_edit.text().strip()
        nas_mac = self.nas_mac_edit.text().strip()
        ssh_key = self.ssh_key_edit.text().strip()

        print(f"  GUI-Werte:")
        print(f"    nas_user: {nas_user}")
        print(f"    nas_ip: {nas_ip}")
        print(f"    nas_mac: {nas_mac}")

        # IP-Validierung
        if nas_ip and not self.validate_ip(nas_ip):
            QMessageBox.warning(
                self,
                tr("config_error"),
                tr("msg_invalid_ip"),
            )
            return

        # Volumes mit Zustand sammeln
        volume_data = []
        for i in range(self.volume_list_widget.count()):
            item = self.volume_list_widget.item(i)
            volume_data.append(
                {"name": item.text(), "checked": (item.checkState() == Qt.Checked)}
            )

        # Zeiteinstellungen
        auto_shutdown = self.auto_shutdown_spin.value()
        auto_start = self.auto_start_spin.value()
        wol_wait = self.wol_wait_spin.value()
        smb_wait = self.smb_wait_spin.value()
        mount_retries = self.mount_retries_spin.value()
        shutdown_mac_delay = self.shutdown_mac_delay_spin.value()

        # ⭐ NEU: Sprachausgabe-Option speichern
        speech_enabled = self.speech_checkbox.isChecked()
        self.config.set("speech_enabled", speech_enabled)

        # In self.config speichern
        self.config.set("nas_vendor", nas_vendor)
        self.config.set("custom_shutdown_command", custom_shutdown_command)   # ⭐ NEU
        self.config.set("nas_user", nas_user)
        self.config.set("nas_dns", nas_dns)
        self.config.set("nas_ip", nas_ip)
        self.config.set("nas_mac", nas_mac)
        self.config.set("ssh_key_path", ssh_key)
        self.config.set("volume_list", [v["name"] for v in volume_data])
        self.config.set("volume_list_with_state", volume_data)
        self.config.set("auto_shutdown_delay", auto_shutdown)
        self.config.set("auto_start_delay", auto_start)
        self.config.set("wol_wait_time", wol_wait)
        self.config.set("smb_wait_time", smb_wait)
        self.config.set("mount_retries", mount_retries)
        self.config.set("shutdown_mac_delay", shutdown_mac_delay)

        print(f"  self.config Werte gesetzt:")
        print(f"    nas_user: {self.config.get('nas_user')}")
        print(f"    nas_ip: {self.config.get('nas_ip')}")

        # Speichern in QSettings, JSON und Profil
        self.config.save_config()

        print("SAVE_AND_ACCEPT - ENDE")
        print("=" * 60)

        self.accept()

    def reset_defaults(self):
        """Setzt alle Werte auf die Standardwerte zurück."""
        if self._msgbox_question(
            tr("msg_reset_title"),
            tr("msg_reset_confirm"),
        ):
            # Server-spezifische Standardwerte
            for key, value in ServerProfile.DEFAULTS.items():
                self.config.set(key, value)

            # Globale Standardwerte
            for key, value in Config.DEFAULTS.items():
                self.config.set(key, value)

            self.load_values()

            QMessageBox.information(
                self,
                tr("msg_reset_title"),
                tr("msg_reset_done"),
            )

    def show_ssh_help(self):
        """Zeigt Hilfe zum SSH-Key an."""
        help_text = """
        <h2>SSH-Key für NAS-Zugriff</h2>

        <p><b>Was ist ein SSH-Key?</b></p>
        <p>Ein SSH-Key ist ein digitaler Schlüssel, der eine sichere Verbindung
        zu Ihrem NAS-Server ermöglicht, ohne dass Sie jedes Mal ein Passwort
        eingeben müssen.</p>

        <p><b>So erstellen Sie einen SSH-Key:</b></p>
        <ol>
            <li>Öffnen Sie das Terminal</li>
            <li>Führen Sie aus: <code>ssh-keygen -t rsa -b 4096</code></li>
            <li>Drücken Sie Enter für den Standardpfad (~/.ssh/id_rsa)</li>
            <li>Geben Sie eine Passphrase ein (optional, aber empfohlen)</li>
        </ol>

        <p><b>So installieren Sie den Key auf dem NAS:</b></p>
        <ol>
            <li>Kopieren Sie den öffentlichen Key:
                <code>cat ~/.ssh/id_rsa.pub</code></li>
            <li>Fügen Sie ihn in die Datei ein:
                <code>~/.ssh/authorized_keys</code> auf dem NAS</li>
            <li>Oder verwenden Sie:
                <code>ssh-copy-id nasuser@NAS-Synology</code></li>
        </ol>

        <p><b>Wichtige Hinweise:</b></p>
        <ul>
            <li>Der private Key muss auf Ihrem Mac bleiben (id_rsa)</li>
            <li>Der öffentliche Key (id_rsa.pub) kommt auf den NAS</li>
            <li>Schützen Sie Ihren privaten Key immer gut!</li>
        </ul>
        """

        QMessageBox.information(self, "SSH-Key Hilfe", help_text)

    # MAC Adresse Finden - Methoden
    def _is_synology_mac(self, mac):
        """Prüft ob die MAC-Adresse zu Synology gehört (OUI)."""
        synology_ouis = [
            "00:11:32",
            "00:17:42",
            "00:19:99",
            "00:25:90",
            "00:26:09",
            "00:26:2C",
            "00:50:8B",
            "00:0C:29",
            "00:1B:21",
        ]
        mac_upper = mac.upper()
        for oui in synology_ouis:
            if mac_upper.startswith(oui):
                return True
        return False

    def find_mac_address(self):
        """Zeigt eine Anleitung zum Finden der MAC-Adresse."""
        help_text = """
        <h2>So finden Sie die MAC-Adresse Ihres Synology NAS</h2>

        <p><b>Methode 1: Über die FRITZ!Box-Oberfläche (Empfohlen - Einfachste Methode)</b></p>
        <ol>
            <li>Öffnen Sie die FRITZ!Box-Oberfläche im Browser: <b>http://fritz.box</b></li>
            <li>Melden Sie sich mit Ihrem FRITZ!Box-Passwort an</li>
            <li>Gehen Sie zu <b>Heimnetz</b> → <b>Netzwerk</b></li>
            <li>Suchen Sie Ihr Synology NAS in der Geräteliste</li>
            <li>Die MAC-Adresse wird in der Spalte <b>MAC-Adresse</b> angezeigt</li>
        </ol>

        <p><b>Methode 2: Über die DSM-Oberfläche</b></p>
        <ol>
            <li>Öffnen Sie die DSM-Oberfläche Ihres NAS im Browser</li>
            <li>Gehen Sie zu <b>Systemsteuerung</b></li>
            <li>Wählen Sie <b>Netzwerk</b> → <b>Netzwerkschnittstelle</b></li>
            <li>Die MAC-Adresse wird dort angezeigt (Format: XX:XX:XX:XX:XX:XX)</li>
        </ol>

        <p><b>Methode 3: Über das Terminal (wenn SSH aktiviert ist)</b></p>
        <ol>
            <li>Öffnen Sie das Terminal</li>
            <li>Führen Sie aus: <code>ssh nasuser@IHRE-NAS-IP</code></li>
            <li>Geben Sie dann ein: <code>ifconfig | grep ether</code></li>
            <li>Die MAC-Adresse wird angezeigt</li>
        </ol>

        <p><b>Methode 4: Über die NAS-App (DS Finder)</b></p>
        <ul>
            <li>Öffnen Sie die DS Finder App auf Ihrem Smartphone</li>
            <li>Wählen Sie Ihr NAS aus</li>
            <li>Die MAC-Adresse wird in den Geräteinformationen angezeigt</li>
        </ul>

        <p><b>Methode 5: Auf dem NAS-Gehäuse</b></p>
        <ul>
            <li>Bei vielen NAS-Modellen ist die MAC auf einem Aufkleber auf der Rückseite</li>
        </ul>

        <p><b>Wichtige Hinweise:</b></p>
        <ul>
            <li>Die MAC-Adresse ist eine eindeutige Hardware-Kennung</li>
            <li>Sie besteht aus 12 Hexadezimal-Ziffern (0-9, A-F)</li>
            <li>Im Feld muss sie im Format <b>XX:XX:XX:XX:XX:XX</b> eingegeben werden</li>
            <li>Die MAC-Adresse ändert sich nie und ist fest mit der Hardware verbunden</li>
            <li>Bei der FRITZ!Box sehen Sie auch die aktuelle IP-Adresse des NAS</li>
        </ul>

        <p style="color: #FF6B00;"><b>💡 Tipp:</b> Schreiben Sie sich die MAC-Adresse auf,
        Sie benötigen sie nur einmal für die Einrichtung.</p>
        """

        QMessageBox.information(self, "MAC-Adresse finden", help_text)

    def find_server_ip(self):
        """Sucht automatisch die IP-Adresse des NAS im Netzwerk."""
        self.status_label.setText("🔍 Suche nach Server-IP...")
        self.status_label.setStyleSheet(
            "color: #FFA500; font-size: 12px; padding: 5px;"
        )
        QApplication.processEvents()

        try:
            ips_found = []
            nas_dns = self.nas_dns_edit.text().strip()

            # Methode 1: Bonjour/mDNS
            if nas_dns:
                ip = self._resolve_mdns(nas_dns)
                if ip:
                    ips_found.append(ip)
                    self.logger.log_action(
                        "IP via Bonjour gefunden", f"{nas_dns} -> {ip}"
                    )

            # Methode 2: DNS-Auflösung
            if nas_dns and not ips_found:
                ip = self._resolve_dns(nas_dns)
                if ip:
                    ips_found.append(ip)
                    self.logger.log_action("IP via DNS gefunden", f"{nas_dns} -> {ip}")

            # Methode 3: ARP-Tabelle
            if not ips_found:
                ip = self._find_synology_ip_in_arp()
                if ip:
                    ips_found.append(ip)
                    self.logger.log_action("IP via ARP gefunden", ip)

            # Methode 4: Ping-Sweep
            if not ips_found:
                ip = self._scan_for_synology_ip()
                if ip:
                    ips_found.append(ip)
                    self.logger.log_action("IP via Scan gefunden", ip)

            if ips_found:
                ip = ips_found[0]
                self.nas_ip_edit.setText(ip)
                self.status_label.setText(f"✅ Server-IP gefunden: {ip}")
                self.status_label.setStyleSheet(
                    "color: #00FF00; font-size: 12px; padding: 5px;"
                )

                QMessageBox.information(
                    self,
                    "Server-IP gefunden",
                    tr("msg_ip_found").format(ip),
                )
            else:
                self.status_label.setText("❌ Server-IP konnte nicht gefunden werden")
                self.status_label.setStyleSheet(
                    "color: #FF0000; font-size: 12px; padding: 5px;"
                )

                QMessageBox.warning(
                    self,
                    "Server-IP nicht gefunden",
                    tr("msg_ip_not_found"),
                )

        except Exception as e:
            self.logger.log_error("Fehler bei IP-Suche", str(e), e)
            self.status_label.setText(f"❌ Fehler bei der IP-Suche: {str(e)[:50]}")
            self.status_label.setStyleSheet(
                "color: #FF0000; font-size: 12px; padding: 5px;"
            )

    def auto_detect_mac_address(self):
        """
        Erkennt die MAC-Adresse des NAS automatisch.

        Ablauf:
          1. Ping die IP → füllt ARP-Cache
          2. Lies MAC aus `arp -a <ip>`
          3. Falls erfolgreich → ins MAC-Feld eintragen
          4. Falls fehlgeschlagen → Hilfe-Dialog anzeigen
        """
        ip = self.nas_ip_edit.text().strip()

        if not ip or not self.validate_ip(ip):
            # Keine gültige IP → direkt Hilfe zeigen
            self.logger.log_action(
                "MAC-Erkennung: Keine gültige IP im Feld"
            )
            self.find_mac_address()
            return

        self.status_label.setText(tr("mac_detect_in_progress"))
        self.status_label.setStyleSheet(
            "color: #FFA500; font-size: 11px; padding: 5px;"
        )
        QApplication.processEvents()

        try:
            # ─── Schritt 1: Ping (füllt ARP-Cache) ───
            subprocess.run(
                ["ping", "-c", "1", "-t", "2", ip],
                capture_output=True,
                text=True,
                timeout=3,
            )
            QApplication.processEvents()

            # ─── Schritt 2: MAC aus ARP-Tabelle ───
            result = subprocess.run(
                ["arp", "-n", ip],
                capture_output=True,
                text=True,
                timeout=3,
            )
            output = result.stdout

            # ─── Schritt 3: MAC-Adresse mit Regex extrahieren ───
            mac_match = re.search(
                r"([0-9a-fA-F]{1,2}[:-]){5}[0-9a-fA-F]{1,2}",
                output,
            )

            if mac_match:
                mac = mac_match.group(0)
                # Normalisieren: führende Nullen ergänzen, Doppelpunkt
                mac_parts = re.split(r"[:-]", mac)
                mac_normalized = ":".join(
                    p.zfill(2).upper() for p in mac_parts
                )

                # Ins Feld eintragen
                self.nas_mac_edit.setText(mac_normalized)

                self.status_label.setText(
                    tr("mac_detect_success").format(mac_normalized)
                )
                self.status_label.setStyleSheet(
                    "color: #4CAF50; font-size: 11px; padding: 5px;"
                )
                self.logger.log_action(
                    "MAC-Adresse erkannt", mac_normalized
                )

                # Kurze Bestätigung als Dialog
                QMessageBox.information(
                    self,
                    tr("config_mac_help"),
                    tr("mac_detect_success_dialog").format(
                        mac_normalized, ip
                    ),
                )
            else:
                # Kein Treffer → Hilfe zeigen
                self.logger.log_action(
                    "MAC-Erkennung: Keine MAC in ARP gefunden",
                    f"arp-Ausgabe: {output[:100]}",
                )
                self.status_label.setText(tr("mac_detect_failed"))
                self.status_label.setStyleSheet(
                    "color: #FF6B00; font-size: 11px; padding: 5px;"
                )
                self.find_mac_address()

        except Exception as e:
            self.logger.log_error(
                "MAC-Erkennung Fehler", str(e), e
            )
            self.status_label.setText(tr("mac_detect_failed"))
            self.status_label.setStyleSheet(
                "color: #FF6B00; font-size: 11px; padding: 5px;"
            )
            # Fehler → Hilfe anzeigen
            self.find_mac_address()

    def _resolve_mdns(self, dns_name):
        """Löst über mDNS/Bonjour auf."""
        try:
            result = subprocess.run(
                ["dns-sd", "-G", "v4", dns_name],
                capture_output=True,
                text=True,
                timeout=3,
            )

            ip_match = re.search(r"(\d{1,3}\.){3}\d{1,3}", result.stdout)
            if ip_match:
                return ip_match.group(0)

            return None
        except Exception as e:
            self.logger.log_error(
                "mDNS-Auflösung fehlgeschlagen", f"{dns_name}: {e}", e
            )
            return None

    def _resolve_dns(self, dns_name):
        """Löst DNS-Namen auf."""
        try:
            result = subprocess.run(
                ["dig", "+short", dns_name], capture_output=True, text=True, timeout=2
            )

            lines = result.stdout.splitlines()
            for line in lines:
                if re.match(r"(\d{1,3}\.){3}\d{1,3}", line.strip()):
                    return line.strip()

            return None
        except Exception as e:
            self.logger.log_error("DNS-Auflösung fehlgeschlagen", f"{dns_name}: {e}", e)
            return None

    def _find_synology_ip_in_arp(self):
        """Sucht in der ARP-Tabelle nach Synology-IPs."""
        try:
            result = subprocess.run(
                ["arp", "-a"], capture_output=True, text=True, timeout=3
            )

            synology_ouis = [
                "00:11:32",
                "00:17:42",
                "00:19:99",
                "00:25:90",
                "00:26:09",
                "00:26:2C",
                "00:50:8B",
                "00:0C:29",
                "00:1B:21",
            ]

            for line in result.stdout.splitlines():
                mac_match = re.search(
                    r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", line, re.IGNORECASE
                )
                if mac_match:
                    mac = mac_match.group(0).upper()
                    for oui in synology_ouis:
                        if mac.startswith(oui):
                            ip_match = re.search(r"(\d{1,3}\.){3}\d{1,3}", line)
                            if ip_match:
                                return ip_match.group(0)

            return None
        except Exception as e:
            self.logger.log_error("ARP-Suche fehlgeschlagen", str(e), e)
            return None

    def _scan_for_synology_ip(self):
        """Scannt das Netzwerk nach Synology-IPs."""
        try:
            current_ip = self._get_current_ip()
            if not current_ip:
                return None

            network_parts = current_ip.split(".")
            if len(network_parts) != 4:
                return None

            base_ip = ".".join(network_parts[:3])

            self.status_label.setText("🔍 Scanne Netzwerk nach Synology...")
            QApplication.processEvents()

            synology_ouis = [
                "00:11:32",
                "00:17:42",
                "00:19:99",
                "00:25:90",
                "00:26:09",
                "00:26:2C",
                "00:50:8B",
                "00:0C:29",
                "00:1B:21",
            ]

            for i in range(1, 51):
                if i % 10 == 0:
                    self.status_label.setText(f"🔍 Scanne IP {base_ip}.{i}/50...")
                    QApplication.processEvents()

                ip = f"{base_ip}.{i}"

                result = subprocess.run(
                    ["ping", "-c", "1", "-t", "1", ip], capture_output=True, timeout=1
                )

                if result.returncode == 0:
                    mac = self._get_mac_from_arp(ip)
                    if mac:
                        mac_upper = mac.upper()
                        for oui in synology_ouis:
                            if mac_upper.startswith(oui):
                                self.status_label.setText(f"✅ Synology gefunden: {ip}")
                                return ip

                    try:
                        result = subprocess.run(
                            ["host", ip], capture_output=True, text=True, timeout=1
                        )
                        if result.returncode == 0:
                            hostname = result.stdout.strip().split()[-1].rstrip(".")
                            if hostname and (
                                "synology" in hostname.lower()
                                or "nas" in hostname.lower()
                            ):
                                return ip
                    except:
                        pass

            return None
        except Exception as e:
            self.logger.log_error("Netzwerk-Scan fehlgeschlagen", str(e), e)
            return None

    def _get_mac_from_arp(self, ip):
        """Holt MAC für eine IP aus der ARP-Tabelle."""
        try:
            result = subprocess.run(
                ["arp", "-a", ip], capture_output=True, text=True, timeout=2
            )

            mac_match = re.search(
                r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", result.stdout, re.IGNORECASE
            )
            if mac_match:
                return mac_match.group(0)

            return None
        except:
            return None

    def _get_current_ip(self):
        """Ermittelt die aktuelle IP-Adresse."""
        try:
            result = subprocess.run(
                ["ipconfig", "getifaddr", "en0"],
                capture_output=True,
                text=True,
                timeout=2,
            )
            ip = result.stdout.strip()
            if ip and re.match(r"(\d{1,3}\.){3}\d{1,3}", ip):
                return ip

            return None
        except Exception as e:
            self.logger.log_error("IP-Ermittlung fehlgeschlagen", str(e), e)
            return None

    def validate_ip(self, ip):
        """Prüft, ob die IP-Adresse ein gültiges IPv4-Format hat."""
        import re

        pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
        if not pattern.match(ip):
            return False
        octets = ip.split(".")
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                return False
        return True

    def open_json_folder(self):
        """Öffnet den Ordner der JSON-Konfigurationsdatei im Finder. Erstellt den Ordner falls nötig."""
        path = (
            self.config.get_json_path()
        )  # z.B. /Users/macbinh/Library/Application Support/AnyNasPy/synaspy_config.json
        folder = os.path.dirname(
            path
        )  # /Users/macbinh/Library/Application Support/AnyNasPy

        # Ordner erstellen falls nicht vorhanden
        if not os.path.exists(folder):
            try:
                os.makedirs(folder, exist_ok=True)
                if hasattr(self, "logger"):
                    self.logger.log_action("JSON-Ordner erstellt", folder)
            except Exception as e:
                if hasattr(self, "logger"):
                    self.logger.log_error(
                        "Fehler beim Erstellen des JSON-Ordners", str(e), e
                    )
                QMessageBox.warning(
                    self,
                    tr("config_error"),
                    f"Konnte JSON-Ordner nicht erstellen:\n{e}",
                )
                return

        # Ordner im Finder öffnen
        subprocess.run(["open", folder])
        if hasattr(self, "logger"):
            self.logger.log_action("JSON-Ordner geöffnet", folder)

    def clear_stored_password(self):
        """Löscht das im Keychain gespeicherte Admin-Passwort."""
        if not self._msgbox_question(
            tr("clear_password_title"),
            tr("clear_password_message"),
        ):
            return

        try:
            if MacKeychainHelper.delete_password():
                self.logger.log_action(
                    "Admin-Passwort aus Keychain gelöscht"
                )
                QMessageBox.information(
                    self,
                    tr("clear_password_title"),
                    tr("clear_password_success"),
                )
            else:
                self.logger.log_error(
                    "Keychain-Löschung fehlgeschlagen",
                    "delete_password() gab False zurück",
                )
                QMessageBox.warning(
                    self,
                    tr("clear_password_title"),
                    tr("clear_password_failed"),
                )
        except Exception as e:
            self.logger.log_error(
                "Fehler beim Löschen des Keychain-Passworts", str(e), e
            )
            QMessageBox.warning(
                self,
                tr("clear_password_title"),
                tr("clear_password_failed"),
            )

    def open_ssh_key_path(self):
        """Öffnet einen Dateidialog zum Auswählen des SSH-Keys oder den Ordner."""
        current_path = self.ssh_key_edit.text().strip()
        if not current_path:
            current_path = os.path.expanduser("~/.ssh/id_rsa")

        # Datei auswählen
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            tr("config_ssh_select"),
            (
                os.path.dirname(current_path)
                if os.path.exists(current_path)
                else os.path.expanduser("~")
            ),
            "Alle Dateien (*);;SSH-Key Dateien (*.pem *.key *.pub);;Privater Key (id_rsa, id_ed25519, id_ecdsa)",
        )
        if file_path:
            self.ssh_key_edit.setText(file_path)
        else:
            # Falls abgebrochen, öffne den Ordner im Finder
            folder = (
                os.path.dirname(current_path)
                if os.path.exists(current_path)
                else os.path.expanduser("~/.ssh")
            )
            if not os.path.exists(folder):
                try:
                    os.makedirs(folder, mode=0o700, exist_ok=True)
                except Exception as e:
                    QMessageBox.warning(self, tr("config_error"), f"{e}")
                    return
            subprocess.run(["open", folder])

    def create_ssh_keypair(self):
        """Erstellt ein neues SSH-Key-Paar mit individuellem Namen und Passphrase."""
        ssh_dir = os.path.expanduser("~/.ssh")
        base_name = "synaspy_rsa"
        private_key = os.path.join(ssh_dir, base_name)

        if not os.path.exists(ssh_dir):
            try:
                os.makedirs(ssh_dir, mode=0o700, exist_ok=True)
            except Exception as e:
                QMessageBox.warning(self, tr("config_error"), f"{e}")
                return

        if os.path.exists(private_key):
            reply = QMessageBox.question(
                self,
                tr("ssh_key_create_title"),
                tr("ssh_key_create_existing").format(base_name),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if reply == QMessageBox.No:
                new_name, ok = QInputDialog.getText(
                    self,
                    tr("ssh_key_create_title"),
                    tr("ssh_key_enter_name"),
                    QLineEdit.Normal,
                    "synaspy_rsa_2",
                )
                if ok and new_name.strip():
                    if new_name.strip().endswith(".pub"):
                        new_name = new_name.strip()[:-4]
                    private_key = os.path.join(ssh_dir, new_name.strip())
                    base_name = os.path.basename(private_key)
                    if base_name in ["id_rsa", "id_ed25519", "id_ecdsa", "id_dsa"]:
                        QMessageBox.warning(
                            self,
                            tr("ssh_key_system_key_warning"),
                            tr("ssh_key_system_key_message").format(base_name),
                        )
                        return
                    if os.path.exists(private_key):
                        QMessageBox.warning(
                            self,
                            tr("ssh_key_create_title"),
                            tr("ssh_key_exists_also").format(base_name),
                        )
                        return
                else:
                    return

        comment, ok = QInputDialog.getText(
            self,
            tr("ssh_key_create_title"),
            tr("ssh_key_create_comment"),
            QLineEdit.Normal,
            tr("ssh_key_create_comment_default").format(
                datetime.now().strftime("%Y%m%d")
            ),
        )
        if not ok:
            comment = tr("ssh_key_create_comment_default").format(
                datetime.now().strftime("%Y%m%d")
            )

        passphrase = ""
        use_passphrase = QMessageBox.question(
            self,
            tr("ssh_key_passphrase_title"),
            tr("ssh_key_passphrase_question"),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if use_passphrase == QMessageBox.Yes:
            passphrase, ok = QInputDialog.getText(
                self,
                tr("ssh_key_passphrase_enter"),
                tr("ssh_key_passphrase_label"),
                QLineEdit.Password,
                "",
            )
            if not ok:
                return
            if not passphrase:
                reply = QMessageBox.question(
                    self,
                    tr("ssh_key_passphrase_none"),
                    tr("ssh_key_passphrase_none_question"),
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes,
                )
                if reply == QMessageBox.No:
                    return
                passphrase = ""
            else:
                if len(passphrase) < 4:
                    QMessageBox.warning(
                        self,
                        tr("ssh_key_passphrase_short"),
                        tr("ssh_key_passphrase_short_message"),
                    )
                    return
                confirm, ok = QInputDialog.getText(
                    self,
                    tr("ssh_key_passphrase_confirm"),
                    tr("ssh_key_passphrase_confirm_label"),
                    QLineEdit.Password,
                    "",
                )
                if not ok:
                    return
                if passphrase != confirm:
                    QMessageBox.warning(
                        self,
                        tr("ssh_key_passphrase_mismatch_title"),
                        tr("ssh_key_passphrase_mismatch_message"),
                    )
                    return

        try:
            self.status_label.setText("🔄 " + tr("ssh_key_create_title") + "...")
            QApplication.processEvents()

            cmd = [
                "ssh-keygen",
                "-t",
                "rsa",
                "-b",
                "4096",
                "-C",
                comment,
                "-f",
                private_key,
            ]
            if passphrase:
                cmd.extend(["-N", passphrase])
            else:
                cmd.extend(["-N", ""])

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            if result.returncode == 0:
                self.ssh_key_edit.setText(private_key)
                self.status_label.setText(
                    f"✅ {tr('ssh_key_create_success').format(base_name)}"
                )
                self.status_label.setStyleSheet(
                    "color: #00FF00; font-size: 12px; padding: 5px;"
                )

                public_key = private_key + ".pub"
                public_key_content = ""
                if os.path.exists(public_key):
                    with open(public_key, "r") as f:
                        public_key_content = f.read().strip()

                nas_user = self.nas_user_edit.text().strip() or "nasuser"
                nas_ip = self.nas_ip_edit.text().strip() or "NAS-IP"

                QMessageBox.information(
                    self,
                    tr("ssh_key_create_title"),
                    tr("ssh_key_create_info").format(
                        private_key, public_key, public_key_content, nas_user, nas_ip
                    ),
                )

                try:
                    subprocess.run(
                        ["ssh-add", private_key], capture_output=True, timeout=5
                    )
                    self.logger.log_action("SSH-Key zum Agent hinzugefügt", private_key)
                except:
                    pass

                self.logger.log_action("SSH-Key-Paar erstellt", private_key)
            else:
                error_msg = result.stderr if result.stderr else "Unbekannter Fehler"
                QMessageBox.warning(
                    self,
                    tr("ssh_key_create_error"),
                    tr("ssh_key_create_failed").format(error_msg),
                )
                self.status_label.setText("❌ " + tr("ssh_key_create_error"))
                self.status_label.setStyleSheet(
                    "color: #FF0000; font-size: 12px; padding: 5px;"
                )
                self.logger.log_error("SSH-Key-Erstellung fehlgeschlagen", error_msg)

        except subprocess.TimeoutExpired:
            QMessageBox.warning(
                self, tr("ssh_key_create_error"), tr("ssh_key_create_timeout")
            )
            self.status_label.setText("❌ " + tr("ssh_key_create_timeout"))
        except Exception as e:
            QMessageBox.warning(self, tr("ssh_key_create_error"), f"{e}")
            self.logger.log_error("Fehler bei SSH-Key-Erstellung", str(e), e)
            self.status_label.setText(f"❌ {str(e)[:50]}")

    """Notlösung wenn NAS Shutdown nicht mehr funktioniert:
        falls einmal der ssh key nicht mehr akzeptiert wird hilf u.U. folgendes im Terminal:
        # 1. Prüfen ob SSH-Key existiert und korrekte Berechtigungen hat
        ls -la ~/.ssh/id_rsa
        # Sollte sein: -rw------- (600)

        # 2. Prüfen ob der Key im SSH-Agent geladen ist
        # Sollte den Fingerprint des Keys anzeigen
        ssh-add -l

        # falls nicht
        # 3. SSH-Key zum SSH-Agent hinzufügen
        ssh-add ~/.ssh/id_rsa

        # 4. Prüfen ob der Key jetzt geladen ist
        ssh-add -l
        # Sollte jetzt den Fingerprint des Keys anzeigen
    """

    def _msgbox_question(self, title: str, text: str,
                         default_no: bool = True) -> bool:
        """Übersetzte Ja/Nein-MessageBox (Dialog-Variante)."""
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Question)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No if default_no else QMessageBox.Yes)
        msg.button(QMessageBox.Yes).setText(tr("btn_yes"))
        msg.button(QMessageBox.No).setText(tr("btn_no"))
        return msg.exec_() == QMessageBox.Yes

# =======================================
# PROFIL-DIALOG
# =======================================


class ProfileDialog(QDialog):
    """Dialog zur Verwaltung von Server-Profilen."""

    def __init__(self, profile_manager: ServerProfileManager, parent=None):
        super().__init__(parent)
        self.profile_manager = profile_manager
        self.parent_app = parent
        self._updating = False
        self._current_profile_id = None

        if parent and hasattr(parent, "logger"):
            self.logger = parent.logger
        else:
            self.logger = AppLogger()

        LANG.add_listener(self.update_ui_language)
        self.initUI()
        self.load_profiles()
        self.logger.log_action("ProfileDialog geöffnet")

    def initUI(self):
        """Initialisiert die Dialog-Benutzeroberfläche."""
        self.setWindowTitle(tr("config_tab_profiles"))
        self.setFixedSize(700, 550)

        # Stylesheet erweitert – dunkelblaue Buttons
        self.setStyleSheet("""
            QDialog, QWidget {
                background-color: #000000;
            }
            QLabel {
                color: #ffffff;
                font-family: Helvetica, Arial, sans-serif;
            }
            QListWidget {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 4px;
                font-size: 13px;
                outline: none;
            }
            QListWidget::item {
                padding: 8px;
                border: none;
            }
            QListWidget::item:selected {
                background-color: #007AFF;
                color: white;
            }
            QListWidget::item:hover:!selected {
                background-color: #2a2a2a;
            }
            QListWidget::item:focus {
                outline: none;
            }
            QLineEdit, QSpinBox {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 4px;
                padding: 6px;
                font-family: Helvetica, Arial, sans-serif;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px 16px;
                margin: 2px;
                border-radius: 4px;
                border: 1px solid #333;
                background-color: #2a2a2a;
                color: white;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_new {
                background-color: #1565c0;
            }
            QPushButton#btn_new:hover {
                background-color: #0055CC;
            }
            QPushButton#btn_delete {
                background-color: #d32f2f;
            }
            QPushButton#btn_delete:hover {
                background-color: #b71c1c;
            }
            /* Dunkelblaue Buttons für Aktivieren, Umbenennen, Duplizieren */
            QPushButton#btn_activate,
            QPushButton#btn_rename,
            QPushButton#btn_duplicate {
                background-color: #1565c0;
                color: #ffffff;
                border: 1px solid #283593;
            }
            QPushButton#btn_activate:hover,
            QPushButton#btn_rename:hover,
            QPushButton#btn_duplicate:hover {
                background-color: #283593;
                border: 1px solid #007AFF;
            }
            QGroupBox {
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #cccccc;
            }
            QLabel#status_label {
                color: #888888;
                font-size: 11px;
                padding: 5px;
            }
            QLabel#active_label {
                color: #4CAF50;
                font-weight: bold;
            }
            QCheckBox {
                color: #ffffff;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        header_label = QLabel(tr("config_tab_profiles"))
        header_label.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #ffffff;"
        )
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)

        splitter = QSplitter(Qt.Horizontal)

        # --- Linke Seite: Profil-Liste (30%) ---
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 5, 0)

        list_label = QLabel(tr("config_profile_list"))
        list_label.setStyleSheet("color: #cccccc; font-weight: bold;")
        left_layout.addWidget(list_label)

        self.profile_list = QListWidget()
        self.profile_list.setSelectionMode(QListWidget.SingleSelection)
        self.profile_list.itemSelectionChanged.connect(self.on_profile_selected)
        left_layout.addWidget(self.profile_list)

        list_buttons = QHBoxLayout()
        self.btn_new = QPushButton(tr("config_profile_new"))
        self.btn_new.setObjectName("btn_new")
        self.btn_new.clicked.connect(self.create_new_profile)

        self.btn_delete = QPushButton(tr("config_profile_delete"))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.delete_profile)
        self.btn_delete.setEnabled(False)

        list_buttons.addWidget(self.btn_new)
        list_buttons.addWidget(self.btn_delete)
        left_layout.addLayout(list_buttons)

        splitter.addWidget(left_widget)

        # --- Rechte Seite: Profil-Details (70%) ---
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(10, 0, 0, 0)

        # Name-Zeile (Label + Edit)
        name_line = QHBoxLayout()
        name_label = QLabel(tr("config_profile_name"))
        name_label.setStyleSheet("color: #cccccc; min-width: 80px;")
        name_line.addWidget(name_label)

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("z.B. NAS-Büro")
        self.name_edit.textChanged.connect(self.on_name_changed)
        name_line.addWidget(self.name_edit)
        right_layout.addLayout(name_line)

        # Container für Buttons + Active-Label (gleiche Breite)
        button_container = QWidget()
        button_layout = QVBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(8)

        # Rename-Button
        self.btn_rename = QPushButton(tr("config_profile_rename"))
        self.btn_rename.setObjectName("btn_rename")
        self.btn_rename.clicked.connect(self.rename_profile)
        self.btn_rename.setEnabled(False)
        self.btn_rename.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button_layout.addWidget(self.btn_rename)

        button_layout.addSpacing(5)

        # Aktiver Status (Label)
        self.active_label = QLabel(tr("config_profile_active"))
        self.active_label.setObjectName("active_label")
        button_layout.addWidget(self.active_label)

        # Activate-Button
        self.btn_activate = QPushButton(tr("config_profile_set_active"))
        self.btn_activate.setObjectName("btn_activate")
        self.btn_activate.clicked.connect(self.activate_profile)
        self.btn_activate.setEnabled(False)
        self.btn_activate.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button_layout.addWidget(self.btn_activate)

        # Duplicate-Button
        self.btn_duplicate = QPushButton(tr("config_profile_duplicate"))
        self.btn_duplicate.setObjectName("btn_duplicate")
        self.btn_duplicate.clicked.connect(self.duplicate_profile)
        self.btn_duplicate.setEnabled(False)
        self.btn_duplicate.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button_layout.addWidget(self.btn_duplicate)

        right_layout.addWidget(button_container)

        # Separator
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: #333;")
        right_layout.addWidget(line)

        # Hinweis
        hint_label = QLabel(
            "💡 Tipp: Änderungen an den Servereinstellungen werden automatisch "
            "im aktiven Profil gespeichert."
        )
        hint_label.setStyleSheet("color: #888888; font-size: 11px;")
        hint_label.setWordWrap(True)
        right_layout.addWidget(hint_label)

        right_layout.addStretch()

        splitter.addWidget(right_widget)
        splitter.setSizes([240, 560])

        main_layout.addWidget(splitter)

        # Status
        self.status_label = QLabel("")
        self.status_label.setObjectName("status_label")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # Schließen-Button
        button_layout_close = QHBoxLayout()
        button_layout_close.addStretch()
        close_btn = QPushButton(tr("btn_cancel"))
        close_btn.setObjectName("btn_cancel")
        close_btn.clicked.connect(self.accept)
        button_layout_close.addWidget(close_btn)
        main_layout.addLayout(button_layout_close)

        # Dialog zentrieren
        parent = self.parent()
        if parent and isinstance(parent, QWidget):
            self.move(
                parent.x() + (parent.width() - self.width()) // 2,
                parent.y() + (parent.height() - self.height()) // 2,
            )

    def update_ui_language(self):
        """Aktualisiert die UI-Texte bei Sprachwechsel."""
        self.setWindowTitle(tr("config_tab_profiles"))
        self.btn_new.setText(tr("config_profile_new"))
        self.btn_delete.setText(tr("config_profile_delete"))
        self.btn_rename.setText(tr("config_profile_rename"))
        self.btn_activate.setText(tr("config_profile_set_active"))
        self.btn_duplicate.setText(tr("config_profile_duplicate"))
        self.active_label.setText(tr("config_profile_active"))
        # Liste neu laden für aktualisierte Texte
        self.load_profiles()

    def load_profiles(self):
        """Lädt die Profile in die Liste – aktives zuerst, dann alphabetisch."""
        self._updating = True
        self.profile_list.clear()

        all_profiles = self.profile_manager.get_profile_list()

        # Trenne aktives und inaktive
        active = [p for p in all_profiles if p.get("is_active")]
        inactive = [p for p in all_profiles if not p.get("is_active")]

        # Sortiere inaktive alphabetisch
        inactive.sort(key=lambda p: p["name"].lower())

        # Kombinieren
        sorted_profiles = active + inactive

        for profile_info in sorted_profiles:
            item = QListWidgetItem(profile_info["name"])
            item.setData(Qt.UserRole, profile_info["id"])

            if profile_info["is_active"]:
                item.setData(Qt.UserRole + 1, True)
                item.setBackground(Qt.darkGreen)
                item.setText(f"⭐ {profile_info['name']}")

            self.profile_list.addItem(item)

        self._updating = False
        self.update_buttons()

        if self.profile_list.count() > 0:
            self.profile_list.setCurrentRow(0)

    def on_profile_selected(self):
        """Wird aufgerufen, wenn ein Profil in der Liste ausgewählt wird."""
        if self._updating:
            return

        self.update_buttons()
        self.load_selected_profile()

    def load_selected_profile(self):
        """Lädt das ausgewählte Profil in die Detail-Ansicht."""
        current_item = self.profile_list.currentItem()
        if not current_item:
            self.name_edit.clear()
            self.btn_rename.setEnabled(False)
            self.btn_activate.setEnabled(False)
            self.btn_delete.setEnabled(False)
            self.btn_duplicate.setEnabled(False)
            self._current_profile_id = None
            return

        profile_id = current_item.data(Qt.UserRole)
        if not profile_id:
            return

        self._current_profile_id = profile_id
        profile = self.profile_manager.get_profile(profile_id)
        if not profile:
            return

        self.name_edit.setText(profile.name)
        self.btn_rename.setEnabled(True)
        self.btn_duplicate.setEnabled(True)
        self.btn_delete.setEnabled(len(self.profile_manager.profiles) > 1)

        # Activate-Button aktivieren, wenn nicht bereits aktiv
        is_active = profile.id == self.profile_manager.active_profile_id
        self.btn_activate.setEnabled(not is_active)

        if is_active:
            self.active_label.setText(f"✅ {tr('config_profile_active')}")
            self.active_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
        else:
            self.active_label.setText(tr("config_profile_active"))
            self.active_label.setStyleSheet("color: #888888;")

    def update_buttons(self):
        """Aktualisiert den Zustand der Buttons."""
        current_item = self.profile_list.currentItem()
        has_selection = current_item is not None

        self.btn_delete.setEnabled(
            has_selection and len(self.profile_manager.profiles) > 1
        )
        self.btn_rename.setEnabled(has_selection)
        self.btn_activate.setEnabled(has_selection)
        self.btn_duplicate.setEnabled(has_selection)  # NEU: Kopieren-Button aktivieren

    def on_name_changed(self, text):
        """Wird aufgerufen, wenn der Profilname geändert wird."""
        self.btn_rename.setEnabled(
            bool(text.strip()) and self._current_profile_id is not None
        )

    def create_new_profile(self):
        """Erstellt ein neues Profil mit eindeutigem Namen."""
        name, ok = QInputDialog.getText(
            self,
            tr("config_profile_new"),
            tr("config_profile_name"),
            QLineEdit.Normal,
            f"NAS-{len(self.profile_manager.profiles) + 1:02d}",
        )

        if not ok or not name.strip():
            return

        name = name.strip()

        if self.profile_manager.get_profile_by_name(name):
            QMessageBox.warning(
                self, tr("config_profile_new"), tr("profile_name_exists").format(name)
            )
            return

        active = self.profile_manager.get_active_profile()
        if active:
            new_profile = ServerProfile()
            new_profile.name = name
            new_profile.nas_user = active.nas_user
            new_profile.nas_dns = active.nas_dns
            new_profile.nas_ip = active.nas_ip
            new_profile.nas_mac = active.nas_mac
            new_profile.ssh_key_path = active.ssh_key_path
            new_profile.volume_list = active.volume_list.copy()
            new_profile.volume_list_with_state = active.volume_list_with_state.copy()
            new_profile.auto_shutdown_delay = active.auto_shutdown_delay
            new_profile.auto_start_delay = active.auto_start_delay
            new_profile.wol_wait_time = active.wol_wait_time
            new_profile.smb_wait_time = active.smb_wait_time
            new_profile.mount_retries = active.mount_retries
            new_profile.shutdown_mac_delay = active.shutdown_mac_delay
            new_profile.enabled = True
        else:
            new_profile = ServerProfile()
            new_profile.name = name

        if self.profile_manager.add_profile(new_profile):
            self.load_profiles()
            for i in range(self.profile_list.count()):
                item = self.profile_list.item(i)
                if item.data(Qt.UserRole) == new_profile.id:
                    self.profile_list.setCurrentRow(i)
                    break

            self.status_label.setText(tr("config_profile_created").format(name))
            self.status_label.setStyleSheet("color: #4CAF50;")
            self.logger.log_action("Profil erstellt", name)
        else:
            self.status_label.setText(tr("config_profile_create_failed"))
            self.status_label.setStyleSheet("color: #FF0000;")

    def delete_profile(self):
        """Löscht das ausgewählte Profil."""
        current_item = self.profile_list.currentItem()
        if not current_item:
            return

        profile_name = current_item.text().replace("⭐ ", "")
        profile_id = current_item.data(Qt.UserRole)

        if len(self.profile_manager.profiles) <= 1:
            QMessageBox.warning(
                self, tr("msg_delete_title"), tr("profile_cannot_delete_last")
            )
            return

        if self._msgbox_question(
            tr("msg_delete_title"),
            tr("msg_delete_confirm").format(profile_name),
        ):
            if self.profile_manager.remove_profile(profile_id):
                self.load_profiles()
                self.status_label.setText(
                    tr("config_profile_deleted").format(profile_name)
                )
                self.status_label.setStyleSheet("color: #FF6B00;")
                self.logger.log_action("Profil gelöscht", profile_name)
            else:
                self.status_label.setText(tr("config_profile_delete_failed"))
                self.status_label.setStyleSheet("color: #FF0000;")

    def rename_profile(self):
        """Benennt das ausgewählte Profil um."""
        if not self._current_profile_id:
            return

        current_item = self.profile_list.currentItem()
        if not current_item:
            return

        old_name = current_item.text().replace("⭐ ", "")
        new_name = self.name_edit.text().strip()

        if not new_name:
            self.status_label.setText(tr("config_profile_required"))
            self.status_label.setStyleSheet("color: #FF6B00;")
            return

        if new_name == old_name:
            return

        if self.profile_manager.get_profile_by_name(new_name):
            self.status_label.setText(tr("profile_name_exists").format(new_name))
            self.status_label.setStyleSheet("color: #FF0000;")
            return

        if self.profile_manager.rename_profile(self._current_profile_id, new_name):
            self.load_profiles()
            for i in range(self.profile_list.count()):
                item = self.profile_list.item(i)
                if item.data(Qt.UserRole) == self._current_profile_id:
                    self.profile_list.setCurrentRow(i)
                    break

            self.status_label.setText(tr("config_profile_renamed").format(new_name))
            self.status_label.setStyleSheet("color: #4CAF50;")
            self.logger.log_action("Profil umbenannt", f"{old_name} -> {new_name}")

            if self.parent_app and hasattr(self.parent_app, "refresh_ui"):
                self.parent_app.refresh_ui()
        else:
            self.status_label.setText(tr("config_profile_rename_failed"))
            self.status_label.setStyleSheet("color: #FF0000;")

    def duplicate_profile(self):
        """Dupliziert das ausgewählte Profil mit eindeutigem Namen."""
        if not self._current_profile_id:
            return

        current_item = self.profile_list.currentItem()
        if not current_item:
            return

        old_name = current_item.text().replace("⭐ ", "")

        base_name = old_name
        counter = 1
        while self.profile_manager.get_profile_by_name(f"{base_name} ({counter})"):
            counter += 1
        suggested = f"{base_name} ({counter})"

        new_name, ok = QInputDialog.getText(
            self,
            tr("config_profile_duplicate"),
            tr("config_profile_duplicate_name"),
            QLineEdit.Normal,
            suggested,
        )

        if not ok or not new_name.strip():
            return

        new_name = new_name.strip()

        if self.profile_manager.get_profile_by_name(new_name):
            QMessageBox.warning(
                self,
                tr("config_profile_duplicate"),
                tr("profile_name_exists").format(new_name),
            )
            return

        new_profile = self.profile_manager.duplicate_profile(
            self._current_profile_id, new_name
        )
        if new_profile:
            self.load_profiles()
            for i in range(self.profile_list.count()):
                item = self.profile_list.item(i)
                if item.data(Qt.UserRole) == new_profile.id:
                    self.profile_list.setCurrentRow(i)
                    break

            self.status_label.setText(
                tr("config_profile_duplicated").format(old_name, new_name)
            )
            self.status_label.setStyleSheet("color: #4CAF50;")
            self.logger.log_action("Profil dupliziert", f"{old_name} -> {new_name}")
        else:
            self.status_label.setText(tr("config_profile_duplicate_failed"))
            self.status_label.setStyleSheet("color: #FF0000;")

    def activate_profile(self):
        """Setzt das ausgewählte Profil als aktiv."""
        if not self._current_profile_id:
            return

        current_item = self.profile_list.currentItem()
        if not current_item:
            return

        profile = self.profile_manager.get_profile(self._current_profile_id)
        if not profile:
            return

        if self.profile_manager.set_active_profile(self._current_profile_id):
            self.load_profiles()
            # Ausgewähltes Profil markieren
            for i in range(self.profile_list.count()):
                item = self.profile_list.item(i)
                if item.data(Qt.UserRole) == self._current_profile_id:
                    self.profile_list.setCurrentRow(i)
                    break

            self.status_label.setText(
                tr("config_profile_activated").format(profile.name)
            )
            self.status_label.setStyleSheet("color: #4CAF50;")
            self.logger.log_action("Profil aktiviert", profile.name)

            # Parent aktualisieren
            if self.parent_app and hasattr(self.parent_app, "refresh_ui"):
                self.parent_app.refresh_ui()
                if hasattr(self.parent_app, "say_message"):
                    self.parent_app.say_message(
                        tr("say_profile_changed").format(profile.name)
                    )
        else:
            self.status_label.setText("❌ Aktivieren fehlgeschlagen.")
            self.status_label.setStyleSheet("color: #FF0000;")

    def _msgbox_question(self, title: str, text: str,
                         default_no: bool = True) -> bool:
        """Übersetzte Ja/Nein-MessageBox (Profil-Dialog)."""
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Question)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No if default_no else QMessageBox.Yes)
        msg.button(QMessageBox.Yes).setText(tr("btn_yes"))
        msg.button(QMessageBox.No).setText(tr("btn_no"))
        return msg.exec_() == QMessageBox.Yes

    def closeEvent(self, event):
        """Entfernt den Listener beim Schließen."""
        LANG.remove_listener(self.update_ui_language)
        super().closeEvent(event)


# =======================================
# VERSIONSMANAGER
# =======================================


class VersionManager:
    """Verwaltet die Versionsprüfung und Updates."""

    CURRENT_VERSION = "2.3.0"
    GITHUB_API_URL = "https://api.github.com/repos/BinhDiez/AnyNasPy----Synology-NAS-Management-Tool/releases/latest"
    GITHUB_RELEASES_URL = (
        "https://github.com/BinhDiez/AnyNasPy----Synology-NAS-Management-Tool/releases"
    )

    @staticmethod
    def check_for_updates(parent=None, show_no_update=True):
        """
        Prüft auf Updates.

        Rückgabe:
            True  → Update verfügbar, User wurde informiert
            False → Kein Update (aktuelle Version) oder User hat "Später" gewählt
            None  → Fehler (keine Internetverbindung, GitHub nicht erreichbar, ...)
        """
        try:
            # Verbesserte Internetprüfung
            if not VersionManager._has_internet_connection():
                if show_no_update:
                    QMessageBox.information(
                        parent,
                        "Keine Internetverbindung",
                        "Es konnte keine Verbindung zum Internet hergestellt werden.\n"
                        "Bitte überprüfen Sie Ihre Netzwerkverbindung.",
                    )
                # Fehler: Netzwerk offline → None
                return None

            latest_version, release_url, release_notes = (
                VersionManager._fetch_latest_version()
            )
            if not latest_version:
                if show_no_update:
                    QMessageBox.warning(
                        parent,
                        "Fehler bei der Versionsprüfung",
                        "Die Versionsinformationen konnten nicht von GitHub geladen werden.\n"
                        "Bitte versuchen Sie es später erneut.",
                    )
                # Fehler: API-Antwort fehlerhaft → None
                return None

            current = VersionManager._parse_version(
                VersionManager.CURRENT_VERSION
            )
            latest = VersionManager._parse_version(latest_version)

            if latest > current:
                # Update verfügbar
                msg = QMessageBox(parent)
                msg.setWindowTitle("Update verfügbar!")
                msg.setIcon(QMessageBox.Information)
                message = f"<h2>Neue Version verfügbar!</h2>"
                message += (
                    f"<p><b>Aktuelle Version:</b> "
                    f"{VersionManager.CURRENT_VERSION}</p>"
                )
                message += f"<p><b>Neue Version:</b> {latest_version}</p>"
                if release_notes:
                    if len(release_notes) > 500:
                        release_notes = release_notes[:500] + "..."
                    message += f"<p><b>Release Notes:</b></p>"
                    message += (
                        f"<p style='background-color:#1a1a1a; padding:10px; "
                        f"border-radius:5px;'>{release_notes}</p>"
                    )
                message += f"<p>Möchten Sie zur Download-Seite wechseln?</p>"
                msg.setText(message)
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg.setDefaultButton(QMessageBox.Yes)
                msg.button(QMessageBox.Yes).setText("Zur Download-Seite")
                msg.button(QMessageBox.No).setText("Später")

                if msg.exec_() == QMessageBox.Yes:
                    QDesktopServices.openUrl(QUrl(release_url))

                # Update verfügbar → True
                return True
            else:
                # Kein Update nötig
                if show_no_update:
                    QMessageBox.information(
                        parent,
                        "Keine Updates verfügbar",
                        f"Sie verwenden bereits die neueste Version "
                        f"{VersionManager.CURRENT_VERSION}.",
                    )
                # Aktuelle Version → False
                return False

        except Exception as e:
            print(f"Fehler bei der Versionsprüfung: {e}")
            if show_no_update:
                QMessageBox.warning(
                    parent,
                    "Fehler bei der Versionsprüfung",
                    f"Es ist ein Fehler aufgetreten:\n{str(e)}",
                )
            # Exception → None
            return None

    @staticmethod
    def _has_internet_connection():
        """Prüft Internetverbindung über Socket (zuverlässiger)."""
        try:
            # Versuche Verbindung zu GitHub auf Port 443 (HTTPS) oder 80
            socket.create_connection(("github.com", 443), timeout=5)
            return True
        except:
            try:
                socket.create_connection(("github.com", 80), timeout=5)
                return True
            except:
                return False

    @staticmethod
    def _fetch_latest_version():
        try:
            req = urllib.request.Request(
                VersionManager.GITHUB_API_URL,
                headers={"User-Agent": "AnyNasPy", "Accept": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode("utf-8"))
                tag = data.get("tag_name", "")
                version = tag
                if version.startswith("v."):
                    version = version[2:]
                elif version.startswith("v"):
                    version = version[1:]
                release_url = data.get("html_url", VersionManager.GITHUB_RELEASES_URL)
                release_notes = data.get("body", "")
                return version, release_url, release_notes
        except Exception as e:
            print(f"Fehler beim Abrufen der Version: {e}")
            return None, None, None

    @staticmethod
    def _parse_version(version_str):
        try:
            version_str = version_str.strip()
            if version_str.startswith("v."):
                version_str = version_str[2:]
            elif version_str.startswith("v"):
                version_str = version_str[1:]
            parts = version_str.split(".")
            major = int(parts[0]) if len(parts) > 0 else 0
            minor = int(parts[1]) if len(parts) > 1 else 0
            patch = int(parts[2]) if len(parts) > 2 else 0
            return (major, minor, patch)
        except:
            return (0, 0, 0)


# =======================================
# INFO DIALOG
# =======================================


class InfoDialog(QDialog):
    """Dialog mit Versionsinfo, Copyright, License, Impressum."""

    VERSION = VersionManager.CURRENT_VERSION
    YEAR = "2026"
    AUTHOR = "BinhDiez"
    CONTACT = "https://github.com/BinhDiez"

    def __init__(self, parent=None):
        super().__init__(parent)
        LANG.add_listener(self.update_ui_language)
        self.setWindowTitle(tr("info_title"))
        self.setFixedSize(500, 600)  # Höhe etwas erhöht für Header

        self.setModal(True)

        self.setStyleSheet("""
            QDialog, QWidget {
                background-color: #000000;
            }
            QLabel {
                color: #ffffff;
                font-family: Helvetica, Arial, sans-serif;
            }
            QLabel#title_label {
                font-size: 24px;
                font-weight: bold;
                color: #007AFF;
                padding: 10px;
            }
            QLabel#subtitle_label {
                font-size: 14px;
                color: #888888;
            }
            QLabel#section_title {
                font-weight: bold;
                font-size: 13px;
                color: #007AFF;
                padding: 5px 0;
            }
            QLabel#content_label {
                font-size: 12px;
                color: #cccccc;
                padding: 2px 0;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px 16px;
                border-radius: 4px;
                border: 1px solid #333;
                background-color: #2a2a2a;
                color: white;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_close {
                background-color: #007AFF;
            }
            QPushButton#btn_close:hover {
                background-color: #0055CC;
            }
            QPushButton#btn_update {
                background-color: #4CAF50;
                font-size: 13px;
                padding: 8px 16px;
                min-width: 120px;
            }
            QPushButton#btn_update:hover {
                background-color: #388E3C;
            }
            QScrollArea {
                border: none;
                background: transparent;
            }
            QFrame#content_frame {
                background-color: #1a1a1a;
                border: 1px solid #333;
                border-radius: 5px;
                padding: 10px;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # ==========================================
        # HEADER mit Logo, Titel und Icon (wie Hauptfenster)
        # ==========================================

        header_layout = QHBoxLayout()
        header_layout.setSpacing(10)

        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Linkes Logo (BinhDiez.png)
        logo_path = os.path.join(script_dir, "BinhDiez.png")
        if os.path.exists(logo_path):
            try:
                pixmap = QPixmap(logo_path)
                if not pixmap.isNull():
                    logo_label = QLabel()
                    logo_label.setPixmap(
                        pixmap.scaled(
                            80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation
                        )
                    )
                    logo_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    header_layout.addStretch()
                    header_layout.addWidget(logo_label)
                    header_layout.addStretch()
            except:
                pass

        # Titel in der Mitte
        title_label = QLabel("AnyNasPy")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #ffffff;")
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label)

        # Rechtes Icon (AnyNasPy.png)
        icon_path = os.path.join(script_dir, "AnyNasPy.png")
        if os.path.exists(icon_path):
            try:
                pixmap = QPixmap(icon_path)
                if not pixmap.isNull():
                    icon_label = QLabel()
                    icon_label.setPixmap(
                        pixmap.scaled(
                            60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation
                        )
                    )
                    icon_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    header_layout.addStretch()
                    header_layout.addWidget(icon_label)
                    header_layout.addStretch()
            except:
                pass

        main_layout.addLayout(header_layout)

        # Untertitel (wie im Hauptfenster)
        subtitle_label = QLabel("NAS Management Tool")
        subtitle_label.setObjectName("subtitle_label")
        subtitle_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(subtitle_label)

        # Trennlinie
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: #333;")
        main_layout.addWidget(line)

        # ==========================================
        # Scrollbereich mit Inhalt
        # ==========================================
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_widget)
        self.scroll_layout.setSpacing(8)

        self.content_frame = QFrame()
        self.content_frame.setObjectName("content_frame")
        self.content_layout = QVBoxLayout(self.content_frame)
        self.content_layout.setSpacing(10)

        self._build_content()

        self.content_layout.addStretch()
        self.scroll_layout.addWidget(self.content_frame)
        self.scroll_layout.addStretch()
        scroll_area.setWidget(scroll_widget)
        main_layout.addWidget(scroll_area)

        # ==========================================
        # Buttons (Update prüfen + Schließen)
        # ==========================================
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        self.update_btn = QPushButton("🔄 Update prüfen")
        self.update_btn.setObjectName("btn_update")
        self.update_btn.clicked.connect(self.check_for_updates)
        btn_layout.addWidget(self.update_btn)

        close_btn = QPushButton(tr("btn_cancel"))
        close_btn.setObjectName("btn_close")
        close_btn.clicked.connect(self.accept)
        btn_layout.addWidget(close_btn)

        main_layout.addLayout(btn_layout)

        # Dialog zentrieren
        parent_widget = self.parent()
        if parent_widget and isinstance(parent_widget, QWidget):
            self.move(
                parent_widget.x() + (parent_widget.width() - self.width()) // 2,
                parent_widget.y() + (parent_widget.height() - self.height()) // 2,
            )

    # ------------------------------------------------
    # Hilfsmethoden mit EINGERÜCKTEN mehrzeiligen Strings
    # ---------------------------------------------------

    def _get_license_text(self):
        """Gibt den Lizenztext zurück (String ist eingerückt!)."""
        return textwrap.dedent("""\
            MIT License

            Copyright (c) 2026 BinhDiez

            Permission is hereby granted, free of charge, to any person obtaining a copy
            of this software and associated documentation files (the "Software"), to deal
            in the Software without restriction, including without limitation the rights
            to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
            copies of the Software, and to permit persons to whom the Software is
            furnished to do so, subject to the following conditions:

            The above copyright notice and this permission notice shall be included in all
            copies or substantial portions of the Software.

            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
            IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
            FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
            AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
            LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
            OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
            SOFTWARE.
        """)

    def _get_impressum_text(self):
        """Gibt den Impressumstext zurück (String ist eingerückt!)."""
        return textwrap.dedent(f"""\
            AnyNasPy NAS Management Tool

            Entwickler: {self.AUTHOR}
            Kontakt: {self.CONTACT}
            Version: {self.VERSION}

            Dieses Tool dient der Verwaltung von Synology NAS-Servern
            und wird unter der MIT License vertrieben.

            Die Nutzung erfolgt auf eigene Verantwortung.
        """)

    def _get_pyqt5_license_text(self):
        """Gibt den PyQt5-Lizenzhinweis zurück (String ist eingerückt!)."""
        return textwrap.dedent("""\
            Diese Anwendung verwendet PyQt5, das unter der GNU General Public License v3 (GPLv3) lizenziert ist.
            Copyright (c) Riverbank Computing Limited.

            Der vollständige Lizenztext kann unter https://www.gnu.org/licenses/gpl-3.0.html eingesehen werden.
        """)

    # --------------------------------
    # Kernmethoden
    # -------------------------------

    def _build_content(self):
        """Erstellt den Inhalt neu (wird bei Sprachwechsel aufgerufen)."""
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self._add_section(
            self.content_layout, "info_version", f"AnyNasPy v{self.VERSION}"
        )
        self._add_section(
            self.content_layout,
            "Multi-Server",
            "✅ Unterstützt mehrere Server-Profile\n✅ Beliebig viele NAS-Server verwaltbar",
        )
        # CHANGELOG VERSION
        self._add_section(
            self.content_layout,
            "Neu in v2.3.0",
            (
                "🌍 Universelle NAS-Unterstützung (13 Hersteller)\n"
                "🔧 Auto-Erkennung des Herstellers via SSH\n"
                "💻 Benutzerdefinierte Shutdown-Befehle\n"
                "📂 Hersteller-spezifische Volume-Erkennung\n"
                "🔍 MAC-Adresserkennung per Knopfdruck"
            ),
            multi_line=True,
            title_color="#4CAF50",
        )
        self._add_section(
            self.content_layout, "info_copyright", f"© {self.YEAR} {self.AUTHOR}"
        )
        self._add_section(self.content_layout, "info_developer", self.AUTHOR)
        self._add_section(self.content_layout, "info_contact", self.CONTACT)
        self._add_section(
            self.content_layout,
            "info_license",
            self._get_license_text(),
            multi_line=True,
        )
        # NEU: Drittanbieter-Bibliotheken (PyQt5)
        self._add_section(
            self.content_layout,
            "info_third_party",
            self._get_pyqt5_license_text(),
            multi_line=True,
        )
        self._add_section(
            self.content_layout,
            "info_impressum",
            self._get_impressum_text(),
            multi_line=True,
        )

        self.content_layout.addStretch()

    def _add_section(
        self, layout, title_key, content, multi_line=False, title_color="#007AFF"
    ):
        """Fügt einen Abschnitt zum Layout hinzu."""
        title_label = QLabel(tr(title_key))
        title_label.setObjectName("section_title")
        if title_color:
            title_label.setStyleSheet(
                f"font-weight: bold; font-size: 13px; color: {title_color}; padding: 5px 0;"
            )
        layout.addWidget(title_label)

        if multi_line:
            content_label = QLabel(content)
            content_label.setObjectName("content_label")
            content_label.setWordWrap(True)
            content_label.setTextFormat(Qt.PlainText)
            content_label.setStyleSheet(
                "font-size: 11px; color: #cccccc; padding: 2px 0; line-height: 1.5;"
            )
            layout.addWidget(content_label)
        else:
            content_label = QLabel(content)
            content_label.setObjectName("content_label")
            content_label.setStyleSheet(
                "font-size: 12px; color: #cccccc; padding: 2px 0;"
            )
            layout.addWidget(content_label)

    def update_ui_language(self):
        """Aktualisiert die UI-Texte bei Sprachwechsel."""
        self.setWindowTitle(tr("info_title"))
        self._build_content()

    def check_for_updates(self):
        """Manuelle Versionsprüfung."""
        self.update_btn.setEnabled(False)
        self.update_btn.setText("⏳ Prüfe...")
        QApplication.processEvents()

        try:
            VersionManager.check_for_updates(self, show_no_update=True)
        finally:
            self.update_btn.setEnabled(True)
            self.update_btn.setText("🔄 Update prüfen")

    def check_for_updates_background(self):
        """Automatische Hintergrundprüfung (ohne Benachrichtigung bei keinem Update)."""
        try:
            VersionManager.check_for_updates(self, show_no_update=False)
        except Exception as e:
            print(f"Fehler bei Hintergrund-Versionsprüfung: {e}")

    def closeEvent(self, event):
        """Listener entfernen."""
        LANG.remove_listener(self.update_ui_language)
        super().closeEvent(event)


# =====================================================
# ZEITGESTEUERTES HERUNTERFAHREN - DIALOG
# =====================================================


class ScheduledShutdownDialog(QDialog):
    """
    Dialog zum zeitgesteuerten Herunterfahren.
    Unabhängig von den Standard-Timeouts in den Settings.

    Layout:
      - ScrollArea enthält den kompletten Inhalt oben
      - Buttons (Abbrechen/Speichern) sind FIX außerhalb der ScrollArea
      - Fensterhöhe passt sich an Bildschirm an (max. 90% Bildschirmhöhe)
    """

    MAX_HOURS = 720          # 30 Tage
    MIN_SECONDS = 60         # mindestens 1 Minute
    MAX_HEIGHT_RATIO = 0.8   # max. 90 % der Bildschirmhöhe

    def __init__(self, parent=None, server_online: bool = True):
        super().__init__(parent)
        self.result_data = None
        self.server_online = server_online

        LANG.add_listener(self.update_ui_language)

        if parent and hasattr(parent, "logger"):
            self.logger = parent.logger
        else:
            self.logger = AppLogger()

        self.setWindowTitle(tr("sched_dialog_title"))
        self.setModal(True)

        # ─── Bildschirmgröße ermitteln (QApplication statt QDesktopWidget) ───
        try:
            screen = QApplication.primaryScreen()
            if screen is not None:
                screen_h = screen.availableGeometry().height()
                screen_w = screen.availableGeometry().width()
            else:
                screen_h, screen_w = 1080, 1920
        except Exception:
            screen_h, screen_w = 1080, 1920

        max_h = int(screen_h * self.MAX_HEIGHT_RATIO)
        desired_h = min(760, max_h)
        desired_w = min(600, int(screen_w * 0.8))

        self.setMinimumSize(600, 450)
        self.resize(desired_w, desired_h)

        self.setStyleSheet(self._get_stylesheet())

        try:
            self._build_ui()
        except Exception as e:
            self.logger.log_error("Fehler in ScheduledShutdownDialog._build_ui", str(e), e)
            raise

        # Dialog zentrieren – erst nachdem die Geometrie final ist
        self._center_on_parent(parent)


    # ─────────────────────────────────────────────────────────
    # Stylesheet als Methode (übersichtlicher als Inline-String)
    # ─────────────────────────────────────────────────────────

    def _get_stylesheet(self) -> str:
        return """
            QDialog, QWidget {
                background-color: #000000;
            }
            QLabel {
                color: #ffffff;
                font-family: Helvetica, Arial, sans-serif;
                font-size: 13px;
            }
            QLabel#sched_header {
                font-size: 20px;
                font-weight: bold;
                color: #ffffff;
                padding: 8px;
            }
            QLabel#sched_preview {
                background-color: #1a1a1a;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 14px;
                color: #4CAF50;
                font-size: 13px;
                font-weight: bold;
            }
            QLabel#sched_hint {
                background-color: #0d1b0d;
                border: 1px solid #1e3a1e;
                border-radius: 5px;
                padding: 10px;
                color: #a5d6a7;
                font-family: 'Courier New', monospace;
                font-size: 11px;
            }
            QLabel#sched_offline_hint {
                color: #FFA500;
                font-size: 12px;
                padding: 6px;
                font-style: italic;
                background-color: #2a1f00;
                border: 1px solid #554400;
                border-radius: 4px;
            }
            QLabel#field_label {
                color: #ffffff;
                font-size: 14px;
                font-weight: bold;
                padding: 4px 0;
            }
            QComboBox, QSpinBox {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #444;
                border-radius: 4px;
                padding: 8px;
                min-height: 30px;
                font-size: 13px;
                selection-background-color: #007AFF;
            }
            QComboBox:hover, QSpinBox:hover {
                border: 1px solid #007AFF;
            }
            QComboBox::drop-down {
                border: none;
                width: 24px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 6px solid #aaa;
                margin-right: 8px;
            }
            QComboBox QAbstractItemView {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #444;
                selection-background-color: #007AFF;
                padding: 4px;
                outline: none;
            }
            QComboBox QAbstractItemView::item {
                min-height: 28px;
                padding: 4px 8px;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #007AFF;
                color: #ffffff;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                background-color: #2a2a2a;
                border: 1px solid #444;
                width: 18px;
            }
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background-color: #007AFF;
            }
            QSpinBox::up-arrow {
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-bottom: 5px solid #fff;
            }
            QSpinBox::down-arrow {
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 5px solid #fff;
            }
            QPushButton {
                font-size: 14px;
                padding: 10px 22px;
                border-radius: 5px;
                border: 1px solid #444;
                background-color: #2a2a2a;
                color: white;
                min-width: 130px;
                min-height: 34px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_sched_start {
                background-color: #007AFF;
            }
            QPushButton#btn_sched_start:hover {
                background-color: #0055CC;
            }
            QPushButton#btn_sched_start:disabled {
                background-color: #333;
                color: #666;
                border: 1px solid #444;
            }
            QPushButton#btn_sched_cancel {
                background-color: #555;
            }
            QPushButton#btn_sched_cancel:hover {
                background-color: #666;
                border: 1px solid #ffffff;
            }
            QGroupBox {
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 6px;
                margin-top: 12px;
                padding-top: 22px;
                font-size: 13px;
                background-color: #0d0d0d;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 10px;
                color: #ffffff;
                font-size: 18px;
                font-weight: bold;
                background-color: #000000;
            }
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: #1a1a1a;
                width: 12px;
                margin: 0;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #444;
                min-height: 30px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background: #007AFF;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
                height: 0;
            }
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
            QFrame#btn_separator {
                background-color: #222;
                max-height: 1px;
                min-height: 1px;
                border: none;
            }
        """

    def _center_on_parent(self, parent):
        """Zentriert den Dialog über dem Parent-Fenster."""
        try:
            if parent and isinstance(parent, QWidget):
                parent_geom = parent.frameGeometry()
                target_x = parent_geom.x() + (parent_geom.width() - self.width()) // 2
                target_y = max(
                    20,
                    parent_geom.y() + (parent_geom.height() - self.height()) // 2,
                )
                self.move(target_x, target_y)
        except Exception as e:
            # Zentrierung ist nicht kritisch, daher nur loggen
            try:
                self.logger.log_error("Dialog-Zentrierung fehlgeschlagen", str(e), e)
            except Exception:
                pass

    def _build_ui(self):
        """Baut die Dialog-Oberfläche auf.

        Layout-Prinzip:
          - Header oben fixiert
          - Ziel / Zeit / caffeinate kompakt in einer ScrollArea
          - Offline-Hinweis direkt in der Ziel-Zeile integriert
          - Vorschau + Buttons unten fixiert
        """
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 12)
        outer_layout.setSpacing(0)

        # ═══════════════ HEADER (fixiert) ═══════════════
        header_container = QWidget()
        header_container.setStyleSheet("background-color: #000000;")
        header_layout = QHBoxLayout(header_container)
        header_layout.setContentsMargins(20, 14, 20, 6)
        header_layout.setSpacing(0)

        self.header_label = QLabel(f"⏰  {tr('sched_dialog_title')}")
        self.header_label.setObjectName("sched_header")
        self.header_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(self.header_label)

        outer_layout.setSpacing(20)
        outer_layout.addWidget(header_container)

        # ═══════════════ SCROLLBEREICH ═══════════════
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: #000000;")
        layout = QVBoxLayout(content_widget)
        layout.setSpacing(10)              # ⬅️ enger als vorher (18)
        layout.setContentsMargins(20, 4, 20, 4)

        # ══════════════ 🎯 ZIEL-ZEILE ══════════════
        target_row = QHBoxLayout()
        target_row.setSpacing(12)

        target_icon = QLabel("🎯")
        target_icon.setStyleSheet(
            "font-size: 36px; padding: 0; margin: 0; color: #FFFFFF;"
        )
        target_icon.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        target_icon.setFixedWidth(40)
        target_icon.setTextFormat(Qt.PlainText)
        target_row.addWidget(target_icon)

        self.target_combo = QComboBox()
        if self.server_online:
            self.target_combo.addItem(tr("sched_target_both"), "both")
            self.target_combo.addItem(tr("sched_target_nas"), "nas_only")
            self.target_combo.addItem(tr("sched_target_mac"), "mac_only")
            self.target_combo.addItem(tr("sched_target_coffee"), "coffee")
        else:
            self.target_combo.addItem(tr("sched_target_mac"), "mac_only")
            self.target_combo.addItem(tr("sched_target_coffee"), "coffee")

        self.target_combo.currentIndexChanged.connect(self._update_preview)
        target_row.addWidget(self.target_combo, stretch=1)

        layout.addLayout(target_row)

        # ── Offline-Hinweis direkt unter der ComboBox (eingerückt zur ComboBox) ──
        if not self.server_online:
            offline_row = QHBoxLayout()
            offline_row.setSpacing(10)
            offline_row.addSpacing(40)   # ⬅️ gleicher Einzug wie Icon-Breite

            offline_hint = QLabel("ⓘ  NAS ist offline – nur Mac-bezogene Optionen verfügbar.")
            offline_hint.setObjectName("sched_offline_hint")
            offline_hint.setWordWrap(True)
            offline_row.addWidget(offline_hint, stretch=1)

            layout.addLayout(offline_row)

        # ══════════════ 🕐 ZEIT-ZEILE ══════════════
        time_row = QHBoxLayout()
        time_row.setSpacing(12)

        time_icon = QLabel("🕐")
        time_icon.setStyleSheet(
            "font-size: 26px; padding: 0; margin: 0; color: #FFFFFF;"
        )
        time_icon.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        time_icon.setFixedWidth(40)
        time_icon.setTextFormat(Qt.PlainText)
        time_row.addWidget(time_icon)

        self.hours_spin = QSpinBox()
        self.hours_spin.setRange(0, self.MAX_HOURS)
        self.hours_spin.setValue(0)
        self.hours_spin.setSuffix(f"  {tr('sched_hours')}")
        self.hours_spin.setAlignment(Qt.AlignCenter)
        self.hours_spin.valueChanged.connect(self._update_preview)
        time_row.addWidget(self.hours_spin, stretch=1)

        self.minutes_spin = QSpinBox()
        self.minutes_spin.setRange(0, 59)
        self.minutes_spin.setValue(30)
        self.minutes_spin.setSuffix(f"  {tr('sched_minutes')}")
        self.minutes_spin.setAlignment(Qt.AlignCenter)
        self.minutes_spin.valueChanged.connect(self._update_preview)
        time_row.addWidget(self.minutes_spin, stretch=1)

        layout.addLayout(time_row)

        # ══════════════ ☕ CAFFEINATE-ZEILE ══════════════
        caff_row = QHBoxLayout()
        caff_row.setSpacing(12)

        caff_icon = QLabel("\u2615\uFE0E")   # HOT BEVERAGE (Text-Variante)
        caff_icon.setStyleSheet(
            "font-size: 52px; padding: 0; margin: 0; color: #FFFFFF;"
        )
        caff_icon.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        caff_icon.setFixedWidth(40)
        caff_icon.setTextFormat(Qt.PlainText)
        caff_row.addWidget(caff_icon)

        self.caffeinate_combo = QComboBox()
        self.caffeinate_combo.addItem(tr("sched_caffeinate_ims"), "-i -m -s")
        self.caffeinate_combo.addItem(tr("sched_caffeinate_im"), "-i -m")
        self.caffeinate_combo.addItem(tr("sched_caffeinate_d"), "-i -m -s -d")
        self.caffeinate_combo.addItem(tr("sched_caffeinate_u"), "-i -m -s -u")
        self.caffeinate_combo.addItem(tr("sched_caffeinate_full"), "-d -i -m -s -u")
        self.caffeinate_combo.addItem(tr("sched_caffeinate_off"), "off")
        self.caffeinate_combo.currentIndexChanged.connect(self._update_preview)
        caff_row.addWidget(self.caffeinate_combo, stretch=1)

        layout.addLayout(caff_row)

        # WICHTIG: Stretch am Ende sammelt überschüssigen Platz unten,
        #    damit die Zeilen oben kompakt zusammen bleiben.
        layout.addStretch(1)

        scroll_area.setWidget(content_widget)
        outer_layout.addWidget(scroll_area, stretch=1)

        # ═══════════════ TRENNLINIE ═══════════════
        separator = QFrame()
        separator.setObjectName("btn_separator")
        separator.setFrameShape(QFrame.HLine)
        outer_layout.addWidget(separator)

        # ═══════════════ VORSCHAU (fixiert) ═══════════════
        preview_container = QWidget()
        preview_container.setStyleSheet("background-color: #000000;")
        preview_layout = QVBoxLayout(preview_container)
        preview_layout.setContentsMargins(20, 8, 20, 6)
        preview_layout.setSpacing(6)

        preview_header = QLabel("Vorschau")
        preview_header.setObjectName("field_label")
        preview_layout.addWidget(preview_header)

        self.preview_label = QLabel("")
        self.preview_label.setObjectName("sched_preview")
        self.preview_label.setWordWrap(True)
        self.preview_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.preview_label.setMinimumHeight(80)
        preview_layout.addWidget(self.preview_label)

        outer_layout.addWidget(preview_container)

        # ═══════════════ FIXIERTE BUTTONS ═══════════════
        bottom_container = QWidget()
        bottom_container.setStyleSheet("background-color: #000000;")
        btn_layout = QHBoxLayout(bottom_container)
        btn_layout.setContentsMargins(20, 6, 20, 4)
        btn_layout.setSpacing(10)
        btn_layout.addStretch()

        self.cancel_btn = QPushButton("✕  " + tr("btn_cancel"))
        self.cancel_btn.setObjectName("btn_sched_cancel")
        self.cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(self.cancel_btn)

        self.start_btn = QPushButton("▶  " + tr("btn_save"))
        self.start_btn.setObjectName("btn_sched_start")
        self.start_btn.clicked.connect(self._on_start)
        btn_layout.addWidget(self.start_btn)

        btn_layout.addStretch()
        outer_layout.addWidget(bottom_container)

        # Initiale Vorschau
        self._update_preview()

    def _update_preview(self):
        """Aktualisiert die Vorschau mit berechneter Endzeit."""
        hours = self.hours_spin.value()
        minutes = self.minutes_spin.value()
        total_seconds = hours * 3600 + minutes * 60

        if total_seconds < self.MIN_SECONDS:
            self.preview_label.setText(f"⚠️   {tr('sched_invalid_time')}")
            self.preview_label.setStyleSheet(
                "background-color: #2a0a0a; border: 1px solid #d32f2f; "
                "border-radius: 6px; padding: 14px; color: #ff8080; "
                "font-size: 13px; font-weight: bold;"
            )
            self.start_btn.setEnabled(False)
            return

        if hours > self.MAX_HOURS:
            self.preview_label.setText(f"⚠️   {tr('sched_max_time')}")
            self.preview_label.setStyleSheet(
                "background-color: #2a0a0a; border: 1px solid #d32f2f; "
                "border-radius: 6px; padding: 14px; color: #ff8080; "
                "font-size: 13px; font-weight: bold;"
            )
            self.start_btn.setEnabled(False)
            return

        self.start_btn.setEnabled(True)

        from datetime import datetime, timedelta
        target_dt = datetime.now() + timedelta(seconds=total_seconds)

        if hours > 0:
            duration_str = f"{hours} h {minutes} min"
        else:
            duration_str = f"{minutes} min"

        target_str = target_dt.strftime("%d.%m.%Y  %H:%M:%S")
        target_name = self.target_combo.currentText()
        caff_flag = self.caffeinate_combo.currentData()

        if caff_flag == "off":
            caff_str = tr("sched_caffeinate_off")
        else:
            caff_str = f"caffeinate {caff_flag}"

        now = datetime.now()
        days_diff = (target_dt.date() - now.date()).days
        if days_diff == 0:
            day_hint = "heute"
        elif days_diff == 1:
            day_hint = "morgen"
        elif days_diff < 7:
            weekday = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"][target_dt.weekday()]
            day_hint = weekday
        else:
            day_hint = f"in {days_diff} Tagen"

        preview_text = (
            f"🕐   {tr('sched_info_scheduled').format(target_str)}   ({day_hint})\n\n"
            f"⏱️   Dauer:      {duration_str}\n"
            f"🎯   Ziel:        {target_name}\n"
            f" ☕   Energie:   {caff_str}"
        )
        self.preview_label.setText(preview_text)
        self.preview_label.setStyleSheet(
            "background-color: #0d1b0d; border: 1px solid #1e3a1e; "
            "border-radius: 6px; padding: 14px; color: #a5d6a7; "
            "font-size: 13px; font-weight: bold; line-height: 1.6;"
        )

    def _on_start(self):
        """Validiert und schließt mit Ergebnis."""
        hours = self.hours_spin.value()
        minutes = self.minutes_spin.value()
        total_seconds = hours * 3600 + minutes * 60

        if total_seconds < self.MIN_SECONDS:
            QMessageBox.warning(
                self, tr("sched_dialog_title"), tr("sched_invalid_time")
            )
            return

        self.result_data = {
            "target": self.target_combo.currentData(),
            "total_seconds": total_seconds,
            "caffeinate_option": self.caffeinate_combo.currentData(),
        }
        self.logger.log_action(
            "Zeitgeber konfiguriert",
            f"Ziel: {self.result_data['target']}, "
            f"Dauer: {total_seconds}s, "
            f"caffeinate: {self.result_data['caffeinate_option']}",
        )
        self.accept()

    def update_ui_language(self):
        """Aktualisiert Texte bei Sprachwechsel."""
        self.setWindowTitle(tr("sched_dialog_title"))

        # Header
        if hasattr(self, "header_label"):
            self.header_label.setText(f"⏰  {tr('sched_dialog_title')}")

        # Ziel-ComboBox
        self.target_combo.blockSignals(True)
        if self.server_online:
            self.target_combo.setItemText(0, tr("sched_target_both"))
            self.target_combo.setItemText(1, tr("sched_target_nas"))
            self.target_combo.setItemText(2, tr("sched_target_mac"))
            self.target_combo.setItemText(3, tr("sched_target_coffee"))
        else:
            self.target_combo.setItemText(0, tr("sched_target_mac"))
            self.target_combo.setItemText(1, tr("sched_target_coffee"))
        self.target_combo.blockSignals(False)

        # caffeinate-ComboBox
        self.caffeinate_combo.setItemText(0, tr("sched_caffeinate_ims"))
        self.caffeinate_combo.setItemText(1, tr("sched_caffeinate_im"))
        self.caffeinate_combo.setItemText(2, tr("sched_caffeinate_d"))
        self.caffeinate_combo.setItemText(3, tr("sched_caffeinate_u"))
        self.caffeinate_combo.setItemText(4, tr("sched_caffeinate_full"))
        self.caffeinate_combo.setItemText(5, tr("sched_caffeinate_off"))

        # Spinnbox-Suffixe (sprachabhängig)
        self.hours_spin.setSuffix(f"  {tr('sched_hours')}")
        self.minutes_spin.setSuffix(f"  {tr('sched_minutes')}")

        # Buttons
        self.cancel_btn.setText("✕  " + tr("btn_cancel"))
        self.start_btn.setText("▶  " + tr("btn_save"))

        self._update_preview()

    def closeEvent(self, event):
        LANG.remove_listener(self.update_ui_language)
        super().closeEvent(event)

# =======================================
# HAUPTKLASSE: AnyNasPy - Hauptfenster
# =======================================


class AnyNasPy(QMainWindow):
    def __init__(self):
        """Initialisiert die Hauptanwendung."""
        super().__init__()

        # Sprach-Listener registrieren
        LANG.add_listener(self.update_ui_language)

        self._auto_shutdown_allowed = False
        self._paused_timeout_counter = 0   # gemerkter Zählerstand bei Pause

        # 1. ZUERST Konfiguration laden
        self.config = Config()

        # 2. DANACH Logger initialisieren
        self.logger = AppLogger()
        self.logger.log_system_info()
        self.logger.log("AnyNasPy gestartet", "START")
        self.logger.log_config(self.config.config)
        self.logger.log_action(
            "Aktives Profil", self.config.get_active_profile_name() or "Kein Profil"
        )

        # Volumes mit Zuständen laden (statt nur Namen)
        volumes_with_state = self.config.get_volumes_with_state()
        self.all_volumes = [v["name"] for v in volumes_with_state]

        # 3. GUI initialisieren
        self.initUI()
        self.rebuild_volume_checkboxes()

        # 4. Timer und Counter initialisieren (NOCH NICHT STARTEN!)
        self.auto_timer = QTimer()
        self.auto_timer.timeout.connect(self.autoSelect)
        self.timeout_counter: int = 0

        # Stelle sicher, dass timeout_limit immer ein int ist
        shutdown_delay = self.config.get("auto_shutdown_delay")
        self.timeout_limit: int = (
            shutdown_delay if isinstance(shutdown_delay, int) else 120
        )

        # ═══════════════════════════════════════════════════════
        # NEU v2.2.0: Zeitgesteuertes Herunterfahren
        # ═══════════════════════════════════════════════════════
        self.scheduled_timer = QTimer()
        self.scheduled_timer.timeout.connect(self._scheduled_tick)
        self.scheduled_target_time = None      # datetime
        self.scheduled_target_action = None    # "both" / "nas_only" / "mac_only" / "coffee"
        self.scheduled_caffeinate_proc = None  # subprocess.Popen
        self.scheduled_voice_interval = 3600   # 60 min Sprachausgabe
        self.scheduled_last_voice_time = None
        self.scheduled_active = False
        # Verfügbare say-Stimmen prüfen
        self._check_say_voices()

        # Sicherheitsnetz: Attribute initialisieren, damit
        # checkServerStatus/handleOnline sie bereits nutzen können
        if not hasattr(self, "timer_paused"):
            self.timer_paused = False
        if not hasattr(self, "is_operation_running"):
            self.is_operation_running = False

        # 5. Serverstatus prüfen (HIER wird server_online gesetzt)
        self.checkServerStatus()

        # 5b. Zeitgeber-Button initial beschriften (abhängig vom Status)
        self._update_scheduled_button_text()
        self._refresh_all_tooltips()

        # 5c. Auto-Timer vorbereiten (NICHT starten!)
        #     Der Auto-Timer wird erst gestartet, wenn die Voraussetzungen
        #     für den Auto-Shutdown erfüllt sind (NOPASSWD oder Keychain-PW).
        #     Deshalb: Prüfung + Start erfolgt über einen kurzen Timer,
        #     damit die GUI zuerst sichtbar wird.
        QTimer.singleShot(500, self._check_shutdown_prerequisites_at_startup)

        # 6. Tastenkürzel für Einstellungen
        self.settings_action = QAction(tr("btn_settings"), self)
        self.settings_action.setShortcut("Ctrl+E")
        self.settings_action.triggered.connect(self.open_settings)
        self.addAction(self.settings_action)

        # 7. Log schreiben
        self.logger.flush()

        # 8. Update-Check nach kurzer Verzögerung
        self.last_check_file = (
            Path.home()
            / "Library/Application Support/AnyNasPy/last_update_check.txt"
        )
        QTimer.singleShot(10000, self.check_for_updates_auto)

        # 9. Timer-Pause und Operations-Status
        self.timer_paused = False
        self.is_operation_running = False

        # Wenn der Mac herunterfährt (durch sudo shutdown), beendet das System
        # alle Prozesse per SIGTERM. Damit die der scheduled_timer
        # sauber beendet werden können.
        signal.signal(signal.SIGTERM, self._sigterm_handler)
        signal.signal(signal.SIGINT, self._sigterm_handler)

    def initUI(self):
        """Initialisiert die Benutzeroberfläche."""
        self.setWindowTitle(tr("window_title"))
        self.setFixedSize(700, 620)

        # Stylesheet für modernes, dunkles Design
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #000000;
            }
            QLabel {
                color: #ffffff;
                font-family: Helvetica, Arial, sans-serif;
            }
            QLabel#status_label {
                font-size: 13px;
                font-weight: bold;
                padding: 8px;
                background-color: #1a1a1a;
                border-radius: 4px;
                margin: 5px;
                border: 1px solid #333;
                min-height: 44px;
                max-height: 44px;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px 12px;
                margin: 2px;
                border-radius: 4px;
                border: 1px solid #333;
                font-weight: bold;
                min-height: 24px;
                min-width: 86px;
                background-color: #2a2a2a;
                color: white;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_shutdown_both {
                background-color: #d32f2f;
            }
            QPushButton#btn_shutdown_nas {
                background-color: #f57c00;
                min-width: 60px;
            }
            QPushButton#btn_shutdown_mac_only {
                background-color: #7B1FA2;
                min-width: 60px;
            }
            QPushButton#btn_shutdown_mac_only:hover {
                background-color: #9C27B0;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_scheduled {
                background-color: #6A1B9A;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton#btn_scheduled:hover {
                background-color: #8E24AA;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_scheduled_active {
                background-color: #d32f2f;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton#btn_scheduled_active:hover {
                background-color: #f44336;
                border: 1px solid #ffffff;
            }
            QPushButton#btn_cancel {
                background-color: #555;
            }
            QPushButton#btn_select_all {
                background-color: #2a2a2a;
                font-size: 10px;
                padding: 4px 8px;
                min-height: 24px;
            }
            QPushButton#btn_start {
                background-color: #007AFF;
            }
            QPushButton#btn_pause {
                font-family: "Segoe UI Symbol", "Arial Unicode MS", "Helvetica Neue", sans-serif;
                font-size: 36px;
                min-width: 30px;
                max-width: 30px;
                min-height: 30px;
                max-height: 30px;
                padding: 0;
                background-color: #2a2a2a;
                color: white;
                border: 1px solid #333;
                border-radius: 4px;
            }
            QPushButton#btn_pause:hover {
                background-color: #3a3a3a;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_stop {
                font-family: "Segoe UI Symbol", "Arial Unicode MS", "Helvetica Neue", sans-serif;
                font-size: 36px;
                min-width: 30px;
                max-width: 30px;
                min-height: 30px;
                max-height: 30px;
                padding: 0;
                background-color: #2a2a2a;
                color: #888888;
                border: 1px solid #333;
                border-radius: 4px;
            }
            QPushButton#btn_stop:hover {
                background-color: #3a3a3a;
                border: 1px solid #007AFF;
            }
            QPushButton#btn_stop_active {
                font-family: "Segoe UI Symbol", "Arial Unicode MS", "Helvetica Neue", sans-serif;
                font-size: 36px;
                min-width: 30px;
                max-width: 30px;
                min-height: 30px;
                max-height: 30px;
                padding: 0;
                background-color: #d32f2f;
                color: #ffffff;
                border: 1px solid #b71c1c;
                border-radius: 4px;
            }
            QPushButton#btn_stop_active:hover {
                background-color: #f44336;
                border: 1px solid #ffffff;
            }
            QPushButton#btn_stop:disabled {
                background-color: #1a1a1a;
                color: #444444;
                border: 1px solid #222;
            }
            QPushButton#btn_settings {
                background-color: transparent;
                border: none;
                font-size: 20px;
                color: #666;
                min-width: 30px;
                padding: 0;
            }
            QPushButton#btn_settings:hover {
                color: #007AFF;
                background-color: transparent;
                border: none;
            }
            QPushButton#btn_info {
                background-color: transparent;
                border: none;
                font-size: 20px;
                color: #666;
                min-width: 30px;
                padding: 0;
            }
            QPushButton#btn_info:hover {
                color: #007AFF;
                background-color: transparent;
                border: none;
            }
            QProgressBar {
                border: 1px solid #333;
                border-radius: 3px;
                background-color: #1a1a1a;
                height: 18px;
                margin: 5px;
            }
            QProgressBar::chunk {
                background-color: #007AFF;
                border-radius: 3px;
            }
            QCheckBox {
                color: #ffffff;
                font-size: 11px;
                padding: 3px;
                spacing: 5px;
            }
            QCheckBox::indicator {
                width: 14px;
                height: 14px;
                border: 1px solid #555;
                border-radius: 2px;
                background-color: #1a1a1a;
            }
            QCheckBox::indicator:checked {
                background-color: #007AFF;
                border: 1px solid #007AFF;
            }
            QCheckBox::indicator:disabled {
                background-color: #333;
                border: 1px solid #444;
            }
            QFrame#volumes_frame {
                background-color: #1a1a1a;
                border: 1px solid #333;
                border-radius: 5px;
                margin: 8px;
            }
            QLabel#volumes_title {
                font-weight: bold;
                color: #cccccc;
            }
            QComboBox#profile_selector {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 4px;
                padding: 4px 8px;
                font-size: 12px;
                min-width: 120px;
            }
            QComboBox#profile_selector::drop-down {
                border: none;
            }
            QComboBox#profile_selector::down-arrow {
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid #888;
                margin-right: 6px;
            }
            QComboBox#profile_selector QAbstractItemView {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333;
                selection-background-color: #007AFF;
            }
        """)

        # Fenster auf dem Bildschirm zentrieren (verfügbare Fläche ohne Dock)
        # Position direkt mit verfügbarer Fläche berechnen
        try:
            screen = QApplication.primaryScreen()
            if screen is not None:
                avail = screen.availableGeometry()
                x = avail.x() + (avail.width() - self.width()) // 2
                y = avail.y() + (avail.height() - self.height()) // 2 - 30  # 30px höher
                self.move(x, y)
        except Exception:
            pass

        # Haupt-Widget und Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(15, 15, 15, 15)

        # ==================================
        # HEADER-Bereich mit Logo und Titel
        # ==================================

        header_layout = QHBoxLayout()
        header_layout.setSpacing(10)

        # Linkes Logo - DIREKTEN Pfad verwenden
        script_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(script_dir, "BinhDiez.png")

        if os.path.exists(logo_path):
            try:
                pixmap = QPixmap(logo_path)
                if not pixmap.isNull():
                    logo_label = QLabel()
                    logo_label.setPixmap(
                        pixmap.scaled(
                            80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation
                        )
                    )
                    header_layout.addStretch()
                    header_layout.addWidget(logo_label)
                    header_layout.addStretch()
                    self.logger.log_action("Logo geladen", "Erfolgreich")
                else:
                    self.logger.log_error(
                        "Logo konnte nicht geladen werden", "QPixmap ist null"
                    )
            except Exception as e:
                self.logger.log_error("Fehler beim Laden des Logos", str(e), e)
        else:
            self.logger.log_error("Logo nicht gefunden", f"Pfad: {logo_path}")

        # Titel in der Mitte
        title_label = QLabel("Synology NAS Management")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #ffffff;")
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label)

        # Rechtes Icon
        icon_path = os.path.join(script_dir, "AnyNasPy.png")

        if os.path.exists(icon_path):
            try:
                pixmap = QPixmap(icon_path)
                if not pixmap.isNull():
                    icon_label = QLabel()
                    icon_label.setPixmap(
                        pixmap.scaled(
                            60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation
                        )
                    )
                    icon_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    header_layout.addStretch()
                    header_layout.addWidget(icon_label)
                    header_layout.addStretch()
                    if hasattr(self, "logger"):
                        try:
                            self.logger.log_action("Icon geladen", "Erfolgreich")
                        except:
                            pass
                else:
                    if hasattr(self, "logger"):
                        try:
                            self.logger.log_error(
                                "Icon konnte nicht geladen werden", "QPixmap ist null"
                            )
                        except:
                            pass
            except Exception as e:
                if hasattr(self, "logger"):
                    try:
                        self.logger.log_error("Fehler beim Laden des Icon", str(e), e)
                    except:
                        pass
        else:
            if hasattr(self, "logger"):
                try:
                    self.logger.log_error("Icon nicht gefunden", f"Pfad: {logo_path}")
                except:
                    pass

        main_layout.addLayout(header_layout)

        # =====================================
        # PROFIL-AUSWAHL
        # =====================================
        profile_layout = QHBoxLayout()
        profile_layout.setSpacing(8)

        profile_label = QLabel("📌")
        profile_label.setStyleSheet("font-size: 16px;")
        profile_layout.addWidget(profile_label)

        self.profile_selector = QComboBox()
        self.profile_selector.setObjectName("profile_selector")
        self.profile_selector.currentIndexChanged.connect(self.on_profile_changed)
        profile_layout.addWidget(self.profile_selector)

        self.profile_selector.setSizePolicy(
            self.profile_selector.sizePolicy().horizontalPolicy(),
            self.profile_selector.sizePolicy().verticalPolicy(),
        )

        profile_manage_btn = QPushButton("⚙")
        profile_manage_btn.setObjectName("btn_settings")
        profile_manage_btn.setToolTip(tr("config_tab_profiles"))
        profile_manage_btn.setFixedSize(30, 30)
        profile_manage_btn.clicked.connect(self.open_profile_manager)
        profile_layout.addWidget(profile_manage_btn)

        profile_layout.addStretch()
        main_layout.addLayout(profile_layout)

        # =====================================
        # STATUS-Anzeige und Fortschrittsbalken
        # =====================================

        self.status_label = QLabel(tr("status_checking"))
        self.status_label.setObjectName("status_label")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)            #  : Zeilenumbruch
        self.status_label.setMinimumHeight(44)
        self.status_label.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed
        )                                               #  : Höhe fix, Breite flexibel
        main_layout.addWidget(self.status_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setFormat("%p%")  # Zeigt Prozent an
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #333;
                border-radius: 3px;
                background-color: #1a1a1a;
                height: 18px;
                margin: 5px;
                text-align: center;
                color: #ffffff;
                font-size: 11px;
            }
            QProgressBar::chunk {
                background-color: #007AFF;
                border-radius: 3px;
            }
        """)
        main_layout.addWidget(self.progress_bar)

        # ==========================
        # HAUPTBUTTONS für Aktionen
        # ==========================

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(6)

        self.button1 = QPushButton(f"⏼ {tr('btn_shutdown_both')}")
        self.button1.setObjectName("btn_shutdown_both")
        self.button1.setToolTip(tr("tooltip_shutdown_both"))

        self.button2 = QPushButton(f"⏼ {tr('btn_shutdown_nas')}")
        self.button2.setObjectName("btn_shutdown_nas")
        self.button2.setToolTip(tr("tooltip_shutdown_nas"))

        self.button3 = QPushButton(tr("btn_cancel"))
        self.button3.setObjectName("btn_cancel")
        self.button3.setToolTip(tr("tooltip_cancel"))

        self.button4 = QPushButton(f"⏻ {tr('btn_start_nas')}")
        self.button4.setObjectName("btn_start")
        self.button4.setToolTip(tr("tooltip_start_nas"))

        # NEU v2.2.0: Nur-Mac-Shutdown Button
        self.button_mac_only = QPushButton(f"⏼ {tr('btn_shutdown_mac_only')}")
        self.button_mac_only.setObjectName("btn_shutdown_mac_only")
        self.button_mac_only.setToolTip(tr("tooltip_shutdown_mac_only"))
        self.button_mac_only.clicked.connect(lambda: self.handleChoice("mac_only"))

        # NEU v2.2.0: Zeitgesteuert-Button
        self.button_scheduled = QPushButton(tr("btn_scheduled_shutdown"))
        self.button_scheduled.setObjectName("btn_scheduled")
        self.button_scheduled.setToolTip(tr("tooltip_scheduled_shutdown"))
        self.button_scheduled.clicked.connect(self.toggle_scheduled_shutdown)

        # Stop/Neustart-Button für Timer (links vom Pause-Button)
        self.stop_btn = QPushButton("⏹")
        self.stop_btn.setObjectName("btn_stop")
        self.stop_btn.setToolTip(tr("tooltip_stop_timer"))
        self.stop_btn.setFixedSize(30, 30)
        self.stop_btn.clicked.connect(self.stop_auto_timer)

        # Pause/Resume Button für Timer
        self.pause_btn = QPushButton("⏸")
        self.pause_btn.setObjectName("btn_pause")
        self.pause_btn.setToolTip(tr("tooltip_pause_timer"))
        self.pause_btn.setFixedSize(30, 30)

        self.pause_btn.clicked.connect(self.toggle_timer_pause)

        # Settings Button (Zahnrad)
        settings_btn = QPushButton("⚙")
        settings_btn.setStyleSheet(
            "font-size: 50px; font-weight: bold; color: #ffffff;"
        )
        settings_btn.setObjectName("btn_settings")
        settings_btn.setToolTip(tr("tooltip_settings"))
        settings_btn.clicked.connect(self.open_settings)

        # Info Button
        info_btn = QPushButton("ℹ")
        info_btn.setStyleSheet("font-size: 50px; font-weight: bold; color: #ffffff;")
        info_btn.setObjectName("btn_info")
        info_btn.setToolTip(tr("info_title"))
        info_btn.clicked.connect(self.open_info)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(6)

        # alle Buttons hinzufügen
        buttons_layout.addWidget(self.button1)          # Mac + NAS
        buttons_layout.addStretch(10)
        buttons_layout.addWidget(self.button2)          # Nur NAS
        buttons_layout.addStretch(10)
        buttons_layout.addWidget(self.button_mac_only)  # NEU: Nur Mac
        buttons_layout.addStretch(10)
        buttons_layout.addWidget(self.button4)          # Start NAS
        buttons_layout.addStretch(10)
        buttons_layout.addWidget(self.button3)          # Abbrechen
        buttons_layout.addStretch(10)
        buttons_layout.addWidget(self.stop_btn)         # ⏹ Stop/Neustart
        buttons_layout.addStretch(10)
        buttons_layout.addWidget(self.pause_btn)        # ⏸ Pause
        buttons_layout.addStretch(10)
        buttons_layout.addWidget(settings_btn)
        buttons_layout.addStretch(10)
        buttons_layout.addWidget(info_btn)
        buttons_layout.addStretch(10)

        main_layout.addLayout(buttons_layout)
        main_layout.addSpacing(6)

        # NEU v2.2.0: Zeitgesteuert-Button in eigener Zeile
        sched_row = QHBoxLayout()
        sched_row.addStretch()
        sched_row.addWidget(self.button_scheduled)
        sched_row.addStretch()
        main_layout.addLayout(sched_row)
        main_layout.addSpacing(8)

        # ======================
        # VOLUME-Auswahlbereich
        # ======================
        self.volumes_frame = QFrame()
        self.volumes_frame.setObjectName("volumes_frame")
        self.volumes_frame.setVisible(False)

        volumes_layout = QVBoxLayout(self.volumes_frame)
        volumes_layout.setSpacing(6)
        volumes_layout.setContentsMargins(12, 12, 12, 12)

        # Titelzeile mit "Alle"-Button
        title_layout = QHBoxLayout()
        self.volumes_title_label = QLabel(tr("volumes_title"))
        self.volumes_title_label.setObjectName("volumes_title")
        title_layout.addWidget(self.volumes_title_label)
        title_layout.addStretch()

        self.select_all_btn = QPushButton(tr("btn_select_all"))
        self.select_all_btn.setObjectName("btn_select_all")
        self.select_all_btn.setCheckable(True)
        title_layout.addWidget(self.select_all_btn)
        volumes_layout.addLayout(title_layout)

        # Scrollbarer Bereich für Volume-Checkboxen
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(
            "QScrollArea { border: none; background: transparent; }"
        )
        scroll_area.setMinimumHeight(120)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(3)

        # WICHTIG: volume_checkboxes VOR der Schleife initialisieren!
        self.volume_checkboxes = {}
        self.all_volumes = self.config.get_volumes()
        if not self.all_volumes:
            self.all_volumes = ["NAS Dokumente"]  # Sicherheitsfallback

        # Checkboxen für jedes Volume erstellen
        for i, volume_name in enumerate(self.all_volumes):
            checkbox = QCheckBox(volume_name)
            if i == 0:  # Erstes Volume ist das Haupt-Volume
                checkbox.setChecked(True)
                checkbox.setEnabled(False)
            self.volume_checkboxes[volume_name] = checkbox
            scroll_layout.addWidget(checkbox)

        scroll_layout.addStretch()
        scroll_area.setWidget(scroll_content)
        volumes_layout.addWidget(scroll_area)
        main_layout.addWidget(self.volumes_frame)

        # =========================
        # TIMER für Auto-Aktionen
        # =========================
        self.auto_timer = QTimer()
        self.auto_timer.timeout.connect(self.autoSelect)
        self.timeout_counter = 0
        self.timeout_limit = self.config.get("auto_shutdown_delay", 120)

        # ==========================
        # SIGNAL-SLOT Verbindungen
        # ==========================
        self.button1.clicked.connect(lambda: self.handleChoice("both"))
        self.button2.clicked.connect(lambda: self.handleChoice("nas_only"))
        self.button3.clicked.connect(lambda: self.handleChoice("cancel"))
        self.button4.clicked.connect(lambda: self.handleChoice("start_nas"))
        self.select_all_btn.clicked.connect(self.toggle_all_volumes)

        # Initial alle Buttons ausblenden
        self.hideAllButtons()

        # Profil-Selector befüllen
        self.update_profile_selector()

    def open_settings(self):
        """Öffnet den Einstellungsdialog."""
        # Timer stoppen, aber nur wenn keine Operation läuft
        timer_was_active = self.auto_timer.isActive()
        if timer_was_active:
            self.auto_timer.stop()
            self.logger.log_action("Timer gestoppt für Einstellungen")
            self.say_message(tr("say_settings_opened"))
            self.status_label.setText(tr("status_settings"))
            self.status_label.setStyleSheet(
                "color: #FF6B00; font-weight: bold; padding: 10px;"
            )
            self.timeout_counter = 0
            QApplication.processEvents()

        # Dialog öffnen
        dialog = ConfigDialog(self.config, self)
        if dialog.exec_() == QDialog.Accepted:
            # Konfiguration wurde geändert
            self.logger.log_action("Einstellungen gespeichert")
            self.refresh_ui()
            self.say_message(tr("say_settings_saved"))
            self.status_label.setText(tr("status_settings_saved"))
            self.logger.log_config(self.config.config)

            # Timer nur neu starten, wenn keine Operation läuft und nicht pausiert
            self.timeout_limit = self.config.get("auto_shutdown_delay", 120)
            if self._start_auto_timer_safe("nach Settings-Speichern"):
                self.say_timer_status()
            else:
                self.logger.log_action(
                    "Timer nicht neu gestartet (Operation läuft oder pausiert)"
                )

        else:
            # Dialog abgebrochen - Timer nur neu starten wenn keine Operation läuft und nicht pausiert
            self.logger.log_action("Einstellungen abgebrochen")
            if self._start_auto_timer_safe("nach Settings-Abbruch"):
                self.say_timer_status()
                self.auto_timer.start(1000)
                self.say_timer_status()
            else:
                self.logger.log_action(
                    "Timer nicht neu gestartet (Operation läuft oder pausiert)"
                )

        self.logger.flush()

    def open_info(self):
        """Öffnet den Info-Dialog."""
        dialog = InfoDialog(self)
        dialog.exec_()

    def update_profile_selector(self):
        """Aktualisiert die Profil-Auswahl-Combobox."""
        self.profile_selector.blockSignals(True)
        self.profile_selector.clear()

        active_id = self.config.get_active_profile_id()
        selected_index = 0

        for i, profile_info in enumerate(
            self.config.profile_manager.get_profile_list()
        ):
            name = profile_info["name"]
            if profile_info["is_active"]:
                name = f"⭐ {name}"
            self.profile_selector.addItem(name, profile_info["id"])
            if profile_info["id"] == active_id:
                selected_index = i

        if self.profile_selector.count() > 0:
            self.profile_selector.setCurrentIndex(selected_index)

        self.profile_selector.blockSignals(False)

    def on_profile_changed(self, index):
        """Wird aufgerufen, wenn ein anderes Profil ausgewählt wird."""
        if index < 0:
            return

        profile_id = self.profile_selector.itemData(index)
        if not profile_id:
            return

        current_active = self.config.get_active_profile_id()
        if profile_id == current_active:
            return

        # Profil wechseln
        self.logger.log_action("Profilwechsel", f"Zu ID: {profile_id}")
        self.status_label.setText(
            tr("status_switching").format(
                self.profile_selector.currentText().replace("⭐ ", "")
            )
        )
        QApplication.processEvents()

        if self.config.profile_manager.set_active_profile(profile_id):
            # Konfiguration neu laden
            self.config.load_config()
            self.logger.log_config(self.config.config)
            self.logger.log_action(
                "Profil gewechselt",
                self.config.get_active_profile_name() or "Unbekannt",
            )

            # GUI aktualisieren
            self.refresh_ui()

            # Sprachausgabe
            profile_name = self.config.get_active_profile_name() or "Unbekannt"
            self.say_message(tr("say_profile_changed").format(profile_name))
            self.status_label.setText(tr("status_profile_changed").format(profile_name))

            # Profil-Selector aktualisieren
            self.update_profile_selector()

    def open_profile_manager(self):
        """Öffnet den Profil-Manager."""
        dialog = ProfileDialog(self.config.profile_manager, self)
        dialog.exec_()
        # Nach Schließen aktualisieren
        self.update_profile_selector()
        self.refresh_ui()

    def update_ui_language(self):
        """Aktualisiert alle UI-Texte bei Sprachwechsel."""
        # Wenn ein Zeitgeber aktiv ist, im Log vermerken,
        # damit man im Nachhinein nachvollziehen kann, warum
        # manche Meldungen in einer anderen Sprache kamen.
        if getattr(self, "scheduled_active", False):
            try:
                self.logger.log_action(
                    "Sprachwechsel während aktivem Zeitgeber",
                    f"Neue Sprache: {LANG.current_language}. "
                    f"Bereits gesprochene Meldungen bleiben in alter Sprache, "
                    f"stündliche Updates nutzen die neue Sprache.",
                )
            except Exception:
                pass
        try:
            # Fenstertitel
            self.setWindowTitle(tr("window_title"))

            # Status-Label (wenn keine spezielle Nachricht angezeigt wird)
            current_text = self.status_label.text()
            status_keys = [
                "status_checking",
                "status_online",
                "status_offline",
                "status_settings",
                "status_settings_saved",
                "status_settings_cancelled",
            ]
            for key in status_keys:
                if current_text == tr(key) or current_text == key:
                    self.status_label.setText(tr(key))
                    break

            # Buttons
            self.button1.setText(f"⏼ {tr('btn_shutdown_both')}")
            self.button1.setToolTip(tr("tooltip_shutdown_both"))
            self.button2.setText(f"⏼ {tr('btn_shutdown_nas')}")
            self.button2.setToolTip(tr("tooltip_shutdown_nas"))
            self.button3.setText(tr("btn_cancel"))
            self.button3.setToolTip(tr("tooltip_cancel"))
            self.button4.setText(f"⏻ {tr('btn_start_nas')}")
            self.button4.setToolTip(tr("tooltip_start_nas"))
            self.select_all_btn.setText(tr("btn_select_all"))

            # Volume Titel
            if self.server_online:
                self.volumes_title_label.setText(tr("volumes_title"))
            else:
                self.volumes_title_label.setText(tr("volumes_title_offline"))

            # Tastenkürzel
            self.settings_action.setText(tr("btn_settings"))

            # Profil-Selector aktualisieren (Texte neu setzen)
            self.update_profile_selector()

            # Alle Tooltips neu setzen
            self._refresh_all_tooltips()

        except Exception as e:
            self.logger.log_error("Fehler bei Sprachaktualisierung", str(e), e)

    def refresh_ui(self):
        """Aktualisiert die GUI nach Konfigurationsänderungen oder Profilwechsel."""
        try:
            # Volumes mit Zuständen laden
            volumes_with_state = self.config.get_volumes_with_state()
            self.all_volumes = [v["name"] for v in volumes_with_state]
            self.rebuild_volume_checkboxes()

            # Timer-Limit aktualisieren
            self.timeout_limit = self.config.get("auto_shutdown_delay", 120)

            # Serverstatus neu prüfen
            self.checkServerStatus()

            # Profil-Selector aktualisieren
            self.update_profile_selector()

        except Exception as e:
            self.logger.log_error("Fehler beim Aktualisieren der GUI", str(e), e)

    def rebuild_volume_checkboxes(self):
        """Baut die Volume-Checkboxen neu auf und setzt die Zustände."""
        try:
            scroll_area = self.volumes_frame.findChild(QScrollArea)
            if not scroll_area:
                return

            scroll_content = scroll_area.widget()
            if not scroll_content:
                return

            # Alte Checkboxen entfernen
            for checkbox in self.volume_checkboxes.values():
                checkbox.deleteLater()
            self.volume_checkboxes.clear()

            # Layout leeren
            layout = scroll_content.layout()
            if layout:
                while layout.count():
                    item = layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()

            # Volumes mit Zuständen aus der Config holen
            volumes_with_state = self.config.get_volumes_with_state()
            # Sicherstellen, dass das erste Volume (Haupt-Volume) aktiv ist
            if volumes_with_state:
                volumes_with_state[0]["checked"] = True

            # Checkboxen erstellen
            for i, entry in enumerate(volumes_with_state):
                name = entry.get("name", "")
                checked = entry.get("checked", True)
                checkbox = QCheckBox(name)
                checkbox.setChecked(checked)
                if i == 0:  # Erstes Volume = Haupt-Volume
                    checkbox.setEnabled(False)
                    checkbox.setChecked(True)
                self.volume_checkboxes[name] = checkbox
                layout.addWidget(checkbox)

            layout.addStretch()

            # "Alle auswählen"-Button zurücksetzen
            self.select_all_btn.setChecked(False)

            # Aktualisierte Volumenliste speichern (für spätere Referenz)
            self.all_volumes = [v["name"] for v in volumes_with_state]

        except Exception as e:
            self.logger.log_error(
                "Fehler beim Neuerstellen der Volume-Checkboxen", str(e), e
            )

    # ======================
    # HILFSMETHODEN
    # ======================

    def hideAllButtons(self):
        """Blendet alle Aktionsbuttons aus und zeigt Fortschrittsbalken."""
        try:
            self.button1.setVisible(False)
            self.button2.setVisible(False)
            self.button_mac_only.setVisible(False)
            self.button3.setVisible(False)
            self.button4.setVisible(False)
            self.stop_btn.setVisible(False)
            self.button_scheduled.setVisible(False)

            self.progress_bar.setVisible(True)
            self.volumes_frame.setVisible(False)
            self.setFixedSize(500, 400)
        except Exception as e:
            self.logger.log_error("Fehler beim Ausblenden der Buttons", str(e), e)

    def showAllButtons(self):
        """Zeigt alle Buttons entsprechend dem Modus an."""
        try:
            if self.server_online:
                self.button1.setVisible(True)
                self.button2.setVisible(True)
                self.button_mac_only.setVisible(True)
                self.button3.setVisible(True)
                self.stop_btn.setVisible(True)
                self.pause_btn.setVisible(True)
                self.button4.setVisible(False)
                self.button_scheduled.setVisible(True)   # ⭐ immer an
                self.volumes_frame.setVisible(True)
                self.setFixedSize(640, 650)
                # Stop-Button-Zustand initial aktualisieren
                self.update_stop_button_state()
            else:
                self.button1.setVisible(False)
                self.button2.setVisible(False)
                self.button_mac_only.setVisible(False)
                self.button3.setVisible(True)
                self.stop_btn.setVisible(True)
                self.pause_btn.setVisible(True)
                self.button4.setVisible(True)
                self.button_scheduled.setVisible(True)   # ⭐ AUCH OFFLINE AN
                self.volumes_frame.setVisible(True)
                self.setFixedSize(500, 680) # 700 ???
                # Stop-Button-Zustand initial aktualisieren
                self.update_stop_button_state()
        except Exception as e:
            self.logger.log_error("Fehler beim Anzeigen der Buttons", str(e), e)

    def _check_say_voices(self):
        """Prüft beim Start, welche Stimmen für die aktuelle Sprache verfügbar sind."""
        try:
            result = subprocess.run(
                ["say", "-v", "?"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            available = result.stdout

            lang_code = LANG.get_language()
            voice_name = self._get_say_voice_for_language(lang_code)

            if voice_name and voice_name in available:
                self.logger.log_action(
                    "Say-Stimme gefunden", f"{lang_code} → {voice_name}"
                )
            elif voice_name:
                self.logger.log_error(
                    "Say-Stimme NICHT verfügbar",
                    f"{lang_code} → {voice_name}. "
                    f"Installiere sie in Systemeinstellungen → "
                    f"Bedienungshilfen → Gesprochene Inhalte."
                )
        except Exception as e:
            self.logger.log_error("Stimmen-Check fehlgeschlagen", str(e), e)

    def _get_say_voice_for_language(self, lang_code: str) -> str:
        """
        Gibt den Namen der macOS-say-Stimme für den übergebenen Sprachcode zurück.
        Fällt auf None zurück, wenn keine passende Stimme bekannt ist – dann
        verwendet say die Systemstandard-Stimme.
        """
        voice_map = {
            "de": "Anna",
            "en": "Samantha",
            "es": "Monica",
            "fr": "Thomas",
            "it": "Alice",
            "nl": "Ellen",
            "no": "Sara",
            "pl": "Zosia",
            "pt": "Luciana",
            "ru": "Milena",
            "fi": "Satu",
            "sv": "Alva",
            "tr": "Yelda",
            "vi": "Linh",
            "cs": "Zuzana",
            "el": "Melina",
            "ar": "Maged",
        }
        return voice_map.get(lang_code)

    def say_message(self, message, wait=False):
        """Spricht eine Nachricht über die macOS Text-to-Speech Funktion.

        Args:
            message: Der zu sprechende Text
            wait: Wenn True, wird synchron gesprochen (blockiert bis
                  `say` fertig ist, max. 4 s). Verhindert Überlagerungen
                  bei schnellen Serien (Mount/Unmount von Volumes).
        """
        # Sprachausgabe in den Einstellungen deaktivierbar
        if not self.config.get("speech_enabled", True):
            return
        try:
            if hasattr(self, "_last_say_time") and hasattr(self, "_last_say_message"):
                elapsed = time.time() - self._last_say_time
                if elapsed < 1.5 and message == self._last_say_message:
                    return

            clean_message = self._strip_emojis_for_speech(message)
            voice = self._get_say_voice_for_language(LANG.get_language())

            if voice:
                args = ["say", "-v", voice, clean_message]
            else:
                args = ["say", clean_message]

            if wait:
                # Synchron, aber mit Timeout, damit ein hängender
                # say-Prozess nicht alles blockiert.
                try:
                    subprocess.run(args, timeout=4)
                except subprocess.TimeoutExpired:
                    self.logger.log_action(
                        "Sprachausgabe Timeout", clean_message[:50]
                    )
            else:
                subprocess.Popen(args)

            self.logger.log_action(
                "Sprachausgabe",
                f"[{voice or 'Standard'}{' wait' if wait else ''}] {clean_message}",
            )
            self._last_say_time = time.time()
            self._last_say_message = message
        except Exception as e:
            self.logger.log_error("Fehler bei Sprachausgabe", str(e), e)

    def _strip_emojis_for_speech(self, text: str) -> str:
        """
        Entfernt Emojis und Symbole aus einem Text, damit die
        macOS-Sprachausgabe sie nicht vorliest.

        Beispiel:
            "⏳ Countdown: 2 h 15 min" → "Countdown: 2 h 15 min"
            "🎯 Ziel: Nur Mac" → "Ziel: Nur Mac"
        """
        import re

        if not text:
            return text

        # Emoji-Bereiche + Variation Selectors + Zero-Width-Joiner
        emoji_pattern = re.compile(
            "["
            "\U0001F300-\U0001F5FF"   # Symbole & Piktogramme
            "\U0001F600-\U0001F64F"   # Emoticons
            "\U0001F680-\U0001F6FF"   # Transport & Karten
            "\U0001F700-\U0001F77F"   # Alchemie
            "\U0001F780-\U0001F7FF"   # Geometrische Formen
            "\U0001F800-\U0001F8FF"   # Pfeile C
            "\U0001F900-\U0001F9FF"   # Supplemental Symbole
            "\U0001FA00-\U0001FAFF"   # Erweiterte Symbole
            "\U00002600-\U000026FF"   # Verschiedene Symbole (☕, ⏰, ⏳, ⏱)
            "\U00002700-\U000027BF"   # Dingbats (✂, ✈, etc.)
            "\U0001F000-\U0001F02F"   # Mahjong
            "\U0001F0A0-\U0001F0FF"   # Spielkarten
            "\U00002190-\U000021FF"   # Pfeile (→, ←, ▶, ◀)
            "\U00002B00-\U00002BFF"   # Weitere Pfeile & Symbole
            "\U0000FE00-\U0000FE0F"   # Variation Selectors
            "\U0001F3FB-\U0001F3FF"   # Hauttöne
            "\U00002000-\U0000206F"   # Typografie (Gedankenstriche etc.)
            "]+",
            flags=re.UNICODE,
        )

        cleaned = emoji_pattern.sub("", text)
        # Mehrfache Leerzeichen zusammenfassen
        cleaned = re.sub(r"\s+", " ", cleaned)
        return cleaned.strip()

    def say_timer_status(self):
        """Spricht den aktuellen Timer-Status mit Verzögerung."""
        if self.server_online:
            message = tr("say_timer_shutdown").format(self.timeout_limit)
        else:
            message = tr("say_timer_start").format(self.timeout_limit)

        # Warte 2 Sekunden und verwende die normale say_message Methode
        QTimer.singleShot(2000, lambda: self.say_message(message))

    def _msgbox_question(self, title: str, text: str,
                         default_no: bool = True) -> bool:
        """
        Zeigt eine übersetzte Ja/Nein-MessageBox.
        Rückgabe: True wenn Ja geklickt, False sonst.
        """
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Question)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No if default_no else QMessageBox.Yes)
        msg.button(QMessageBox.Yes).setText(tr("btn_yes"))
        msg.button(QMessageBox.No).setText(tr("btn_no"))
        return msg.exec_() == QMessageBox.Yes

    def _refresh_all_tooltips(self):
        """
        Setzt alle Tooltips und Accessible-Namen neu.
        Wird bei jedem Sprachwechsel aufgerufen, damit die
        macOS-Accessible-Metadata (Sprache) korrekt aktualisiert wird.
        """
        try:
            # ─── Hauptbuttons ───
            if hasattr(self, "button1"):
                self.button1.setToolTip(tr("tooltip_shutdown_both"))
            if hasattr(self, "button2"):
                self.button2.setToolTip(tr("tooltip_shutdown_nas"))
            if hasattr(self, "button_mac_only"):
                self.button_mac_only.setToolTip(tr("tooltip_shutdown_mac_only"))
            if hasattr(self, "button3"):
                self.button3.setToolTip(tr("tooltip_cancel"))
            if hasattr(self, "button4"):
                self.button4.setToolTip(tr("tooltip_start_nas"))

            # ─── Zeitgeber-Button (modus-abhängig) ───
            if hasattr(self, "button_scheduled"):
                self._update_scheduled_button_text()   # setzt auch Tooltip

            # ─── Pause-Button ───
            if hasattr(self, "pause_btn"):
                self.pause_btn.setToolTip(tr("tooltip_pause_timer"))

            # ─── Stop-Button ───
            if hasattr(self, "stop_btn"):
                # Tooltip abhängig vom Zustand
                if self.stop_btn.isEnabled():
                    self.stop_btn.setToolTip(tr("tooltip_stop_timer"))
                else:
                    self.stop_btn.setToolTip(tr("tooltip_stop_timer_inactive"))
                self.pause_btn.setToolTip(tr("tooltip_pause_timer"))

            # ─── Volume-Auswahl ───
            if hasattr(self, "select_all_btn"):
                self.select_all_btn.setToolTip(tr("volumes_mount_tooltip"))
            if hasattr(self, "volumes_title_label"):
                self.volumes_title_label.setToolTip(tr("volumes_mount_tooltip"))

            # ─── Profilverwaltung ───
            if hasattr(self, "profile_selector"):
                self.profile_selector.setToolTip(tr("config_tab_profiles"))

            # ─── Settings-Button (Zahnrad) ───
            # Der Button hat keine Instanz-Referenz, daher per findChild suchen
            for btn in self.findChildren(QPushButton):
                if btn.objectName() == "btn_settings":
                    btn.setToolTip(tr("tooltip_settings"))
                elif btn.objectName() == "btn_info":
                    btn.setToolTip(tr("info_title"))

            # ─── Accessible-Namen (macOS VoiceOver-Sprache) ───
            # Explizit nochmal setzen, damit die Sprachmetadata neu geschrieben wird
            if hasattr(self, "button1"):
                self.button1.setAccessibleName(tr("btn_shutdown_both"))
            if hasattr(self, "button2"):
                self.button2.setAccessibleName(tr("btn_shutdown_nas"))
            if hasattr(self, "button_mac_only"):
                self.button_mac_only.setAccessibleName(tr("btn_shutdown_mac_only"))
            if hasattr(self, "button_scheduled"):
                # Aktueller Text des Buttons ist bereits die Übersetzung
                self.button_scheduled.setAccessibleName(self.button_scheduled.text())

            # Kontext-Aktualisierung (macht Qt/Mac, dass die Änderungen sichtbar werden)
            self.update()
        except Exception as e:
            self.logger.log_error(
                "Fehler beim Aktualisieren der Tooltips", str(e), e
            )

    def update_stop_button_state(self):
        """
        Aktualisiert die Optik des Stop-Buttons basierend auf dem
        aktuellen Timer-Zustand.

        - Timer läuft oder pausiert → Button rot, aktiv, Icon ⏹
        - Timer gestoppt → Button grau, inaktiv, Icon ⏹
        """
        try:
            # Ist ein Auto-Timer aktiv? (entweder laufend oder pausiert)
            timer_active = (
                self.auto_timer.isActive()
                or getattr(self, "timer_paused", False)
                or self.timeout_counter > 0
            )

            if timer_active:
                # Rot + aktiv
                self.stop_btn.setObjectName("btn_stop_active")
                self.stop_btn.setEnabled(True)
                self.stop_btn.setToolTip(tr("tooltip_stop_timer"))
            else:
                # Grau + inaktiv
                self.stop_btn.setObjectName("btn_stop")
                self.stop_btn.setEnabled(False)
                self.stop_btn.setToolTip(tr("tooltip_stop_timer_inactive"))

            # Stylesheet neu anwenden (damit objectName-Wechsel wirkt)
            self.stop_btn.style().unpolish(self.stop_btn)
            self.stop_btn.style().polish(self.stop_btn)

        except Exception as e:
            self.logger.log_error(
                "Fehler beim Aktualisieren des Stop-Buttons", str(e), e
            )

    def stop_auto_timer(self):
        """
        Stoppt den Auto-Timer komplett.
        Setzt den Zähler auf 0, hebt Pause auf, aktualisiert Optik.
        """
        try:
            # Timer stoppen
            if self.auto_timer.isActive():
                self.auto_timer.stop()

            # Zustand zurücksetzen
            self.timeout_counter = 0
            self._paused_timeout_counter = 0
            self.timer_paused = False
            # Nach Stop zeigt der Button ▶ (Neustart-Symbol),
            # weil jetzt kein Timer läuft
            self.pause_btn.setText("▶")

            self.logger.log_action("Auto-Timer komplett gestoppt")

            # Status-Anzeige
            self.status_label.setText(tr("timer_stopped_notice"))
            self.status_label.setStyleSheet(
                "color: #888888; "
                "font-size: 13px; "
                "font-weight: bold; "
                "padding: 8px; "
                "background-color: #1a1a1a; "
                "border: 1px solid #333; "
                "border-radius: 4px; "
                "margin: 5px;"
            )

            # Sprachausgabe
            self.say_message(tr("say_timer_stopped"))

            # Stop-Button-Optik aktualisieren
            self.update_stop_button_state()

        except Exception as e:
            self.logger.log_error("Fehler beim Stoppen des Auto-Timers", str(e), e)

    def toggle_timer_pause(self):
        """
        Pausiert den Auto-Timer oder setzt ihn an der pausierten
        Sekunde fort.

        Drei Zustände:
          - Läuft → pausieren
          - Pausiert → an gemerkter Sekunde fortsetzen
          - Gestoppt → Neustart mit Settings-Zeit
        """
        # ─── Läuft → Pausieren ───
        if self.auto_timer.isActive() and not self.timer_paused:
            self._paused_timeout_counter = self.timeout_counter
            self.auto_timer.stop()
            self.timer_paused = True
            self.pause_btn.setText("▶")

            remaining = max(0, self.timeout_limit - self.timeout_counter)
            self.status_label.setText(tr("timer_paused").format(remaining))
            self.say_message(tr("say_timer_paused"))
            self.logger.log_action(
                "Timer pausiert",
                f"Bei Sekunde {self.timeout_counter} ({remaining}s verbleibend)",
            )
            self.update_stop_button_state()
            return

        # ─── Pausiert → Fortsetzen ───
        if self.timer_paused:
            self.timer_paused = False

            # Offline-Modus: WOL-Timer braucht kein Passwort
            if not self.server_online:
                self._auto_shutdown_allowed = True
                self.timeout_counter = self._paused_timeout_counter
                self.auto_timer.start(1000)
                self.pause_btn.setText("⏸")
                self.status_label.setText(tr("timer_resumed"))
                self.say_message(tr("say_timer_resumed"))
                self.logger.log_action(
                    "Timer fortgesetzt (Offline)",
                    f"Ab Sekunde {self._paused_timeout_counter}",
                )
                self.update_stop_button_state()
                return

            # Online-Modus: Guard-Prüfung
            if self._start_auto_timer_safe("Fortsetzen nach Pause"):
                self.timeout_counter = self._paused_timeout_counter
                self.pause_btn.setText("⏸")
                self.status_label.setText(tr("timer_resumed"))
                self.say_message(tr("say_timer_resumed"))
                self.logger.log_action(
                    "Timer fortgesetzt (Online)",
                    f"Ab Sekunde {self._paused_timeout_counter}",
                )
            else:
                # Konnte nicht starten (kein Passwort) → Pause beibehalten
                self.timer_paused = True
                self.pause_btn.setText("▶")
                self.status_label.setText(tr("auto_timer_disabled_no_pw"))
                self.logger.log_action(
                    "Timer konnte nicht fortgesetzt werden "
                    "(keine Voraussetzungen)"
                )
            self.update_stop_button_state()
            return

        # ─── Gestoppt → Neustart mit Settings-Zeit ───
        # (kein Timer läuft, keine Pause aktiv)
        self.logger.log_action(
            "Neustart Auto-Timer mit Settings-Zeit",
            f"Verzögerung: {self.timeout_limit}s",
        )

        # Auto-Timer starten (Guard prüft Voraussetzungen)
        if self._start_auto_timer_safe("Neustart aus gestopptem Zustand"):
            self.pause_btn.setText("⏸")
            self.say_timer_status()
            self.logger.log_action("Timer neu gestartet")
        else:
            # Konnte nicht starten (kein Passwort im Online-Modus)
            self.status_label.setText(tr("auto_timer_disabled_no_pw"))
            self.logger.log_action(
                "Neustart verweigert (keine Voraussetzungen)"
            )

        self.update_stop_button_state()

    # ═══════════════════════════════════════════════════════════
    # NEU v2.2.0: Zeitgesteuertes Herunterfahren
    # ═══════════════════════════════════════════════════════════

    # =====================================
    # PASSWORT (sudo / ABFRAGE / KEYCHAIN)
    # =====================================

    def _prompt_for_mac_password(self) -> bool:
        """
        Zeigt einen Dialog zur Eingabe des Administrator-Passworts.
        Speichert das Passwort im Keychain, wenn es gültig ist.
        """
        while True:
            password, ok = QInputDialog.getText(
                self,
                tr("mac_pw_dialog_title"),
                tr("mac_pw_dialog_message"),
                QLineEdit.Password,
                "",
            )

            if not ok or not password:
                # User hat abgebrochen
                self.logger.log_action(
                    "Passwort-Eingabe für Mac-Shutdown abgebrochen"
                )
                return False

            # Passwort testen
            try:
                result = subprocess.run(
                    ["sudo", "-S", "-k", "true"],
                    input=f"{password}\n",
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                if result.returncode == 0:
                    # Gültig → im Keychain speichern
                    if MacKeychainHelper.store_password(password):
                        self.logger.log_action(
                            "Mac-Shutdown: Passwort im Keychain gespeichert"
                        )
                    else:
                        self.logger.log_error(
                            "Keychain-Speicherung fehlgeschlagen",
                            "Passwort bleibt nur für diese Sitzung gültig",
                        )
                    return True
                else:
                    # Falsches Passwort → nochmal fragen
                    QMessageBox.warning(
                        self,
                        tr("mac_pw_dialog_title"),
                        tr("mac_pw_wrong_password"),
                    )
                    # Falsches Passwort → nochmal fragen
                    QMessageBox.warning(
                        self,
                        tr("mac_pw_dialog_title"),
                        tr("mac_pw_wrong_password"),
                    )
                    self.logger.log_action(
                        "Passwort-Eingabe fehlgeschlagen (falsches Passwort)"
                    )
                    # Schleife läuft weiter → erneut fragen
            except Exception as e:
                self.logger.log_error(
                    "Passwort-Test fehlgeschlagen", str(e), e
                )
                QMessageBox.warning(
                    self,
                    tr("mac_pw_dialog_title"),
                    tr("mac_pw_test_failed").format(str(e)),
                )
                return False

    def _has_nopasswd_sudo(self) -> bool:
        """
        Prüft still, ob die NOPASSWD-sudoers-Regel greift.
        Keine UI-Interaktion, kein Passwort.

        Rückgabe:
            True  → sudo -n true funktioniert (NOPASSWD-Regel aktiv)
            False → NOPASSWD greift nicht, oder sudo -n nicht verfügbar
        """
        ### =========================================================
        # return False # zum Testen ohne sudo simulieren return am Anfang # ???
        ### =========================================================
        try:
            result = subprocess.run(
                ["sudo", "-n", "true"],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception:
            return False

    def _can_auto_shutdown(self) -> bool:
        """
        Prüft ohne UI-Interaktion, ob die Voraussetzungen für einen
        Mac-Shutdown erfüllt sind.

        Rückgabe:
            True  → NOPASSWD-Regel oder Keychain-Passwort vorhanden
            False → Keines von beiden → Auto-Timer darf nicht starten
        """
        # 1. NOPASSWD-Regel prüfen
        if self._has_nopasswd_sudo():
            self.logger.log_action(
                "Auto-Shutdown-Check: NOPASSWD-Regel vorhanden"
            )
            return True

        # 2. Keychain-Passwort prüfen
        if MacKeychainHelper.has_password():
            self.logger.log_action(
                "Auto-Shutdown-Check: Keychain-Passwort vorhanden"
            )
            return True

        # 3. Keines von beiden
        self.logger.log_action(
            "Auto-Shutdown-Check: Keine Voraussetzungen erfüllt"
        )
        return False

    def _ensure_mac_shutdown_prerequisites(self) -> bool:
        """
        Stellt sicher, dass die App den Mac herunterfahren kann.
        Wird beim Einrichten eines Zeitgebers aufgerufen (nicht beim Auslösen!).

        Ablauf:
          1. NOPASSWD-Regel oder Keychain-Passwort vorhanden?
             → JA:  alles gut, keine Eingabe nötig
          2. Passwort-Dialog zeigen
             → Speichern im Keychain

        Rückgabe:
            True  → App kann herunterfahren
            False → User hat abgebrochen oder Passwort falsch
        """
        # ─── Schritt 1a: NOPASSWD-Regel prüfen (zentral) ───
        if self._has_nopasswd_sudo():
            self.logger.log_action(
                "Mac-Shutdown: NOPASSWD-Regel vorhanden, kein Passwort nötig"
            )
            return True

        # ─── Schritt 1b: Passwort im Keychain? ───
        existing_pw = MacKeychainHelper.get_password()
        if existing_pw:
            try:
                # Passwort testen
                result = subprocess.run(
                    ["sudo", "-S", "-k", "true"],
                    input=f"{existing_pw}\n",
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                if result.returncode == 0:
                    self.logger.log_action(
                        "Mac-Shutdown: Passwort im Keychain ist gültig"
                    )
                    return True
                else:
                    self.logger.log_action(
                        "Mac-Shutdown: Passwort im Keychain ist ungültig, "
                        "wird neu abgefragt"
                    )
                    MacKeychainHelper.delete_password()
            except Exception as e:
                self.logger.log_error(
                    "Keychain-Passwort-Test fehlgeschlagen", str(e), e
                )

        # ─── Schritt 2: Passwort-Dialog ───
        return self._prompt_for_mac_password()

    def _check_shutdown_prerequisites_at_startup(self):
        """
        Prüft beim App-Start die Voraussetzungen für den Auto-Timer.

        Wichtig:
          - ONLINE (NAS läuft):  Auto-Timer würde 'both' auslösen
                                 → Passwort nötig
          - OFFLINE (NAS aus):   Auto-Timer löst nur 'start_nas' aus (WOL)
                                 → Kein Passwort nötig, Timer startet direkt

        Im Offline-Modus wird die Passwort-Prüfung erst beim
        Öffnen des Zeitgeber-Dialogs oder bei einem tatsächlichen
        Shutdown-Versuch durchgeführt.
        """
        try:
            # ═══════════════════════════════════════════════════
            # OFFLINE-MODUS: Auto-Timer darf immer starten
            # ═══════════════════════════════════════════════════
            if not self.server_online:
                self.logger.log_action(
                    "Auto-Timer startet (Offline-Modus, WOL-Timer)"
                )
                self._start_auto_timer()
                return

            # ═══════════════════════════════════════════════════
            # ONLINE-MODUS: Auto-Timer braucht Passwort für Mac-Shutdown
            # ═══════════════════════════════════════════════════
            if self._can_auto_shutdown():
                self.logger.log_action(
                    "Auto-Shutdown aktiviert (Voraussetzungen erfüllt)"
                )
                self._start_auto_timer()
                return

            # Nichts vorhanden → User fragen
            self.logger.log_action(
                "Auto-Shutdown: Voraussetzungen fehlen, frage User"
            )

            # Startup Dialog
            if not self._msgbox_question(
                tr("startup_no_pw_title"),
                tr("startup_no_pw_message"),
                default_no=False,
            ):
                self.logger.log_action(
                    "Auto-Shutdown deaktiviert: User hat Einrichtung vertagt"
                )
                self._disable_auto_timer_with_notice()
                return

            # Passwort-Dialog
            if self._prompt_for_mac_password():
                self.logger.log_action(
                    "Auto-Shutdown aktiviert nach Passwort-Einrichtung"
                )
                self._start_auto_timer()
            else:
                self.logger.log_action(
                    "Auto-Shutdown deaktiviert: Passwort-Einrichtung abgebrochen"
                )
                self._disable_auto_timer_with_notice()

        except Exception as e:
            self.logger.log_error(
                "Fehler beim Start-Check der Shutdown-Voraussetzungen",
                str(e),
                e,
            )
            # Sicherheitshalber Auto-Timer nicht starten
            self._disable_auto_timer_with_notice()

    def _start_auto_timer_safe(self, reason: str = "") -> bool:
        """
        Zentrale Methode zum (Neu-)Start des Auto-Timers mit Guard-Prüfung.

        Startet den Auto-Timer nur, wenn:
          - kein Zeitgeber läuft
          - Auto-Shutdown erlaubt ist (NOPASSWD oder Keychain-PW)
          - nicht pausiert
          - keine Operation läuft

        Rückgabe:
            True  → Timer wurde gestartet
            False → Timer wurde NICHT gestartet (Guard hat blockiert)
        """
        # 1. Zeitgeber läuft? → Nicht starten
        if getattr(self, "scheduled_active", False):
            self.logger.log_action(
                "Auto-Timer nicht gestartet (Zeitgeber aktiv)",
                reason,
            )
            return False

        # 2. Pausiert oder Operation läuft? → Nicht starten
        if getattr(self, "timer_paused", False) or getattr(self, "is_operation_running", False):
            self.logger.log_action(
                "Auto-Timer nicht gestartet (pausiert oder Operation)",
                reason,
            )
            return False

        # 3. Voraussetzungen erfüllt? → Nur dann starten
        if not self._can_auto_shutdown():
            self.logger.log_action(
                "Auto-Timer nicht gestartet (Voraussetzungen fehlen)",
                reason,
            )
            return False

        # 4. Alles ok → starten
        self._auto_shutdown_allowed = True
        self.timeout_counter = 0
        self.auto_timer.start(1000)
        self.logger.log_action("Auto-Timer gestartet", reason)
        return True

    def _start_auto_timer(self):
        """Startet
         den Auto-Timer mit einem sicheren Hinweis im Status-Label."""
        try:
            self._auto_shutdown_allowed = True
            self.timeout_counter = 0
            self.timer_paused = False
            self.pause_btn.setText("⏸")
            self.auto_timer.start(1000)
            self.logger.log_action(
                "Auto-Timer gestartet",
                f"Verzögerung: {self.timeout_limit}s"
            )
            self.say_timer_status()

            # Stop-Button-Optik aktualisieren
            if hasattr(self, "stop_btn"):
                self.update_stop_button_state()
        except Exception as e:
            self.logger.log_error("Fehler beim Auto-Timer-Start", str(e), e)

    def _disable_auto_timer_with_notice(self):
        """Deaktiviert den Auto-Timer und zeigt einen Hinweis im Hauptfenster."""
        try:
            self._auto_shutdown_allowed = False
            if self.auto_timer.isActive():
                self.auto_timer.stop()
            self.timeout_counter = 0

            self.status_label.setText(tr("auto_timer_disabled_no_pw"))
            self.status_label.setStyleSheet(
                "color: #FFA500; "
                "font-size: 13px; "
                "font-weight: bold; "
                "padding: 10px; "
                "background-color: #2a1f00; "
                "border: 1px solid #554400; "
                "border-radius: 4px; "
                "margin: 5px;"
            )

            self.logger.log_action(
                "Auto-Timer deaktiviert - kein Passwort vorhanden"
            )

            # Stop-Button auf inaktiv setzen
            if hasattr(self, "stop_btn"):
                self.stop_btn.setObjectName("btn_stop")
                self.stop_btn.setEnabled(False)
                self.stop_btn.style().unpolish(self.stop_btn)
                self.stop_btn.style().polish(self.stop_btn)
        except Exception as e:
            self.logger.log_error(
                "Fehler beim Deaktivieren des Auto-Timers", str(e), e
            )

    def toggle_scheduled_shutdown(self):
        """Öffnet Dialog oder bricht aktiven Zeitgeber ab."""
        if self.scheduled_active:
            self._cancel_scheduled_shutdown()
        else:
            self._open_scheduled_dialog()

    def _open_scheduled_dialog(self):
        """Öffnet den Dialog für zeitgesteuertes Herunterfahren."""
        auto_timer_was_active = self.auto_timer.isActive()
        self.timeout_counter = 0   # ⬅️ Zähler sofort zurücksetzen
        if auto_timer_was_active:
            self.auto_timer.stop()
            self.timeout_counter = 0  # Zähler zurücksetzen
            self.logger.log_action("Auto-Timer zurückgesetzt für Zeitgeber-Dialog")

        try:
            # ⭐ server_online an den Dialog übergeben
            dialog = ScheduledShutdownDialog(self, server_online=self.server_online)
            if dialog.exec_() == QDialog.Accepted and dialog.result_data:
                self._start_scheduled_shutdown(
                    target=dialog.result_data["target"],
                    total_seconds=dialog.result_data["total_seconds"],
                    caffeinate_option=dialog.result_data["caffeinate_option"],
                )
            else:
                if auto_timer_was_active and not self.timer_paused:
                    self.timeout_counter = 0
                    self.auto_timer.start(1000)
                    self.logger.log_action(
                        "Auto-Timer nach Dialogabbruch wieder gestartet"
                    )
        except Exception as e:
            self.logger.log_error("Fehler im Zeitgeber-Dialog", str(e), e)
            if auto_timer_was_active and not self.timer_paused:
                self.auto_timer.start(1000)

    def _start_scheduled_shutdown(self, target: str, total_seconds: int,
                                  caffeinate_option: str):
        """Startet den zeitgesteuerten Shutdown."""
        from datetime import datetime, timedelta

       # Debug ???
        print(f"=== _start_scheduled_shutdown ===")
        print(f"target: {target}")
        print(f"server_online: {self.server_online}")
        print(f"target in (both, mac_only): {target in ('both', 'mac_only')}")
        print(f"_has_nopasswd_sudo(): {self._has_nopasswd_sudo()}")
        print(f"MacKeychainHelper.has_password(): {MacKeychainHelper.has_password()}")

        # ⭐ Sicherheitsnetz: NAS-Ziele im Offline-Modus auf "mac_only" umbiegen
        if not self.server_online and target in ("both", "nas_only"):
            self.logger.log_action(
                "Zeitgeber: NAS offline, Ziel umgebogen",
                f"{target} → mac_only",
            )
            target = "mac_only"

        # ⭐ Passwort-Vorbereitung für den Mac-Shutdown
        # Nur nötig, wenn der Mac tatsächlich heruntergefahren wird
        if target in ("both", "mac_only"):
            if not self._ensure_mac_shutdown_prerequisites():
                # User hat abgebrochen → Zeitgeber nicht starten
                self.logger.log_action(
                    "Zeitgeber abgebrochen: Passwort-Voraussetzung nicht erfüllt"
                )
                QMessageBox.information(
                    self,
                    tr("sched_dialog_title"),
                    tr("sched_cancelled_no_password"),
                )
                return

        self.scheduled_target_action = target
        self.scheduled_target_time = datetime.now() + timedelta(seconds=total_seconds)
        self.scheduled_active = True

        # ⭐ Auto-Timer deaktivieren, solange der Zeitgeber läuft
        self._auto_shutdown_allowed = False
        if self.auto_timer.isActive():
            self.auto_timer.stop()
        self.timeout_counter = 0
        self.logger.log_action(
            "Auto-Timer deaktiviert (Zeitgeber aktiv)",
            f"Ziel: {target}",
        )
        # Auto-Timer pausieren, solange der Zeitgeber läuft
        if self.auto_timer.isActive():
            self.auto_timer.stop()
        self.timeout_counter = 0
        # Pause- und Stop-Button ausblenden, solange Zeitgeber läuft
        self.pause_btn.setVisible(False)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setVisible(False)
        self.stop_btn.setEnabled(False)
        self.logger.log_action("Auto-Timer pausiert (Zeitgeber aktiv)")
        self.scheduled_last_voice_time = None

        # caffeinate starten
        if caffeinate_option and caffeinate_option != "off":
            self._start_scheduled_caffeinate(caffeinate_option)

        # Timer ticken lassen
        self.scheduled_timer.start(1000)

        # Button-Zustand ändern
        self.button_scheduled.setText(tr("btn_cancel_scheduled"))
        self.button_scheduled.setToolTip(tr("tooltip_cancel_scheduled"))
        self.button_scheduled.setObjectName("btn_scheduled_active")
        self.button_scheduled.style().unpolish(self.button_scheduled)
        self.button_scheduled.style().polish(self.button_scheduled)

        # Info an User
        duration_str = self._format_duration(total_seconds)
        end_time_str = self.scheduled_target_time.strftime("%d.%m.%Y %H:%M:%S")
        target_names = {
            "both": tr("sched_target_both"),
            "nas_only": tr("sched_target_nas"),
            "mac_only": tr("sched_target_mac"),
            "coffee": tr("sched_target_coffee"),
        }
        target_name = target_names.get(target, target)

        self.logger.log_action(
            "Zeitgeber gestartet",
            f"Ziel: {target}, Dauer: {duration_str}, "
            f"Ende: {end_time_str}, caffeinate: {caffeinate_option}",
        )

        # Für die Sprachausgabe: menschenlesbare Dauer
        duration_spoken = self._format_duration_spoken(total_seconds)

        # Ziel-spezifische Sprachausgabe
        if target == "coffee":
            # Bei "Nichts tun" hängt der Text von der caffeinate-Option ab
            voice_key_map = {
                "-i -m -s": "sched_voice_nothing_ims",
                "-i -m": "sched_voice_nothing_im",
                "-i -m -s -d": "sched_voice_nothing_d",
                "-i -m -s -u": "sched_voice_nothing_u",
                "-d -i -m -s -u": "sched_voice_nothing_full",
                "off": "sched_voice_nothing_off",
            }
            voice_key = voice_key_map.get(
                caffeinate_option, "sched_voice_nothing_off"
            )
            voice_text = tr(voice_key).format(duration_spoken)
        else:
            voice_map = {
                "both": "sched_voice_started_both",
                "nas_only": "sched_voice_started_nas",
                "mac_only": "sched_voice_started_mac",
            }
            voice_key = voice_map.get(target, "sched_voice_started_both")
            voice_text = tr(voice_key).format(duration_spoken)

        self.say_message(voice_text)

        QMessageBox.information(
            self,
            tr("sched_dialog_title"),
            tr("sched_started").format(target_name, duration_str, end_time_str),
        )

        self._update_scheduled_status_label()

    def _start_scheduled_caffeinate(self, option: str):
        """Startet caffeinate mit den gewählten Optionen."""
        try:
            args = ["caffeinate"] + option.split() + ["-w", str(os.getpid())]
            self.scheduled_caffeinate_proc = subprocess.Popen(
                args,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            self.logger.log_action(
                "caffeinate gestartet",
                f"Optionen: {option} (PID: {self.scheduled_caffeinate_proc.pid})",
            )
        except Exception as e:
            self.logger.log_error("caffeinate-Start fehlgeschlagen", str(e), e)
            QMessageBox.warning(
                self,
                tr("sched_dialog_title"),
                tr("sched_caffeinate_failed").format(str(e)),
            )

    def _stop_scheduled_caffeinate(self):
        """Beendet den caffeinate-Prozess, falls aktiv."""
        if self.scheduled_caffeinate_proc:
            try:
                self.scheduled_caffeinate_proc.terminate()
                try:
                    self.scheduled_caffeinate_proc.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    self.scheduled_caffeinate_proc.kill()
                self.logger.log_action("caffeinate beendet")
            except Exception as e:
                self.logger.log_error("caffeinate-Beenden fehlgeschlagen", str(e), e)
            finally:
                self.scheduled_caffeinate_proc = None

    def _cancel_scheduled_shutdown(self):
        """Bricht den aktiven Zeitgeber ab."""
        if not self.scheduled_active:
            return

        self.scheduled_timer.stop()
        self._stop_scheduled_caffeinate()

        self.scheduled_active = False

        # ⭐ Auto-Timer wieder erlauben
        # (Guard prüft Voraussetzungen und startet ggf.)
        if self._start_auto_timer_safe("Zeitgeber abgebrochen"):
            self.logger.log_action("Auto-Timer wieder aktiviert")
        else:
            self.logger.log_action(
                "Auto-Timer nicht reaktiviert (Voraussetzungen fehlen)"
            )

        # Pause- und Stop-Button wieder anzeigen
        self.pause_btn.setVisible(True)
        self.pause_btn.setEnabled(True)
        self.stop_btn.setVisible(True)
        self.stop_btn.setEnabled(True)
        self.update_stop_button_state()

        self.scheduled_target_time = None
        self.scheduled_target_action = None

        self.button_scheduled.setObjectName("btn_scheduled")
        self.button_scheduled.style().unpolish(self.button_scheduled)
        self.button_scheduled.style().polish(self.button_scheduled)
        self._update_scheduled_button_text()

        self.say_message(tr("sched_voice_cancelled"))
        self.logger.log_action("Zeitgeber abgebrochen")

        # Serverstatus neu prüfen — das ruft handleOnline/handleOffline auf
        # und setzt timeout_limit korrekt. Der Auto-Timer-Start erfolgt dann
        # über handleOnline/handleOffline.
        self.checkServerStatus()

    def _scheduled_tick(self):
        """Wird jede Sekunde aufgerufen, wenn ein Zeitgeber aktiv ist."""
        if not self.scheduled_active or not self.scheduled_target_time:
            return

        from datetime import datetime

        now = datetime.now()
        remaining_seconds = int((self.scheduled_target_time - now).total_seconds())

        if remaining_seconds <= 0:
            self._trigger_scheduled_shutdown()
            return

        self._update_scheduled_status_label(remaining_seconds)

        if self.scheduled_last_voice_time is None:
            self.scheduled_last_voice_time = now
        else:
            elapsed = (now - self.scheduled_last_voice_time).total_seconds()
            if elapsed >= self.scheduled_voice_interval:
                duration_str = self._format_duration(remaining_seconds)
                self.say_message(tr("status_scheduled_active").format(duration_str))
                self.scheduled_last_voice_time = now

    def _update_scheduled_status_label(self, remaining_seconds: int = None):
        """Aktualisiert das Status-Label mit dem Countdown."""
        if remaining_seconds is None and self.scheduled_target_time:
            from datetime import datetime
            remaining_seconds = int(
                (self.scheduled_target_time - datetime.now()).total_seconds()
            )
        if remaining_seconds is None:
            return

        duration_str = self._format_duration(remaining_seconds)
        end_str = (
            self.scheduled_target_time.strftime("%d.%m. %H:%M")
            if self.scheduled_target_time else "?"
        )

        target_names = {
            "both": tr("sched_target_both"),
            "nas_only": tr("sched_target_nas"),
            "mac_only": tr("sched_target_mac"),
            "coffee": tr("sched_target_coffee"),
        }
        target_name = target_names.get(self.scheduled_target_action, "?")

        # ⭐ Für "Nichts herunterfahren" einen anderen Text verwenden
        if self.scheduled_target_action == "coffee":
            label_text = tr("sched_countdown_coffee_label").format(
                duration_str, end_str
            )
        else:
            label_text = tr("sched_countdown_label").format(
                duration_str, end_str
            )

        self.status_label.setText(
            label_text + f"  •  {target_name}"
        )
        self.status_label.setStyleSheet(
            "color: #FFD700; "
            "font-size: 13px; "
            "font-weight: bold; "
            "padding: 8px; "
            "background-color: #2a1a00; "
            "border: 1px solid #FFD700; "
            "border-radius: 4px; "
            "margin: 5px;"
        )

    def _update_scheduled_button_text(self):
        """Aktualisiert den Text des Zeitgeber-Buttons je nach Modus und Status."""
        # Defensive Prüfung: Während der Initialisierung existieren die
        # Attribute noch nicht zwingend. In diesem Fall nichts tun –
        # der Aufruf erfolgt dann erneut in handleOnline/handleOffline.
        if not hasattr(self, "button_scheduled"):
            return
        if not hasattr(self, "scheduled_active"):
            return
        if not hasattr(self, "server_online"):
            # Server-Status noch nicht ermittelt: neutraler Standard-Text
            self.button_scheduled.setText(tr("btn_scheduled_shutdown"))
            self.button_scheduled.setToolTip(tr("tooltip_scheduled_shutdown"))
            return

        if self.scheduled_active:
            self.button_scheduled.setText(tr("btn_cancel_scheduled"))
            self.button_scheduled.setToolTip(tr("tooltip_cancel_scheduled"))
        elif self.server_online:
            self.button_scheduled.setText(tr("btn_scheduled_shutdown"))
            self.button_scheduled.setToolTip(tr("tooltip_scheduled_shutdown"))
        else:
            self.button_scheduled.setText(tr("btn_scheduled_shutdown_offline"))
            self.button_scheduled.setToolTip(tr("tooltip_scheduled_shutdown_offline"))

    def _update_scheduled_button_tooltip(self):
        """Aktualisiert nur den Tooltip des Zeitgeber-Buttons."""
        if self.scheduled_active:
            self.button_scheduled.setToolTip(tr("tooltip_cancel_scheduled"))
        elif self.server_online:
            self.button_scheduled.setToolTip(tr("tooltip_scheduled_shutdown"))
        else:
            self.button_scheduled.setToolTip(tr("tooltip_scheduled_shutdown_offline"))

    def _trigger_scheduled_shutdown(self):
        """Wird aufgerufen, wenn die Zeit abgelaufen ist."""
        self.scheduled_timer.stop()
        self._stop_scheduled_caffeinate()

        target = self.scheduled_target_action
        self.scheduled_active = False

        # ⭐ Auto-Timer wieder erlauben (Guard prüft Voraussetzungen)
        self._auto_shutdown_allowed = False  # Wird von _start_auto_timer_safe gesetzt

        # Pause- und Stop-Button wieder anzeigen
        self.pause_btn.setVisible(True)
        self.pause_btn.setEnabled(True)
        self.stop_btn.setVisible(True)
        self.stop_btn.setEnabled(True)
        self.update_stop_button_state()

        self.scheduled_target_time = None
        self.scheduled_target_action = None

        self.button_scheduled.setObjectName("btn_scheduled")
        self.button_scheduled.style().unpolish(self.button_scheduled)
        self.button_scheduled.style().polish(self.button_scheduled)
        self._update_scheduled_button_text()

        self.logger.log_action("Zeitgeber abgelaufen", f"Ziel: {target}")

        if target in ("both", "nas_only", "mac_only"):
            # Auto-Timer STOPPEN, damit handleChoice freie Bahn hat
            if self.auto_timer.isActive():
                self.auto_timer.stop()
            self.say_message(tr("status_scheduled_triggered").format(target))
            self.handleChoice(target)
        elif target == "coffee":
            # Kein Shutdown → Auto-Timer wieder starten (Guard-geprüft)
            self.logger.log_action(
                "Zeitgeber abgelaufen - nichts zu tun (Ziel: nothing)"
            )
            self._start_auto_timer_safe("Zeitgeber 'nothing' abgelaufen")
            self.checkServerStatus()

    def _format_duration(self, total_seconds: int) -> str:
        """Formatiert Sekunden in lesbare Form: '2 d 3 h 15 min'."""
        total_seconds = max(0, int(total_seconds))

        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        parts = []
        if days > 0:
            parts.append(f"{days} d")
        if hours > 0 or days > 0:
            parts.append(f"{hours} h")
        if minutes > 0 or hours > 0 or days > 0:
            parts.append(f"{minutes} min")
        if not parts or (seconds > 0 and not days and not hours):
            parts.append(f"{seconds} s")
        return " ".join(parts)

    def _format_duration_spoken(self, total_seconds: int) -> str:
        """
        Formatiert Sekunden in eine für die Sprachausgabe geeignete Form.
        Beispiel: 178200 -> "2 Tagen, 1 Stunde und 30 Minuten"
        """
        total_seconds = max(0, int(total_seconds))

        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60

        def unit(value, singular, plural):
            return f"{value} {singular if value == 1 else plural}"

        parts = []
        if days > 0:
            parts.append(f"{days} {tr('duration_day' if days == 1 else 'duration_days')}")
        if hours > 0:
            parts.append(f"{hour} {tr('duration_hour' if hours == 1 else 'duration_hours')}")
        if minutes > 0 or not parts:
            if minutes == 0 and not parts:
                minutes = max(1, total_seconds // 60)
            parts.append(f"{minutes} {tr('duration_minute' if minutes == 1 else 'duration_minutes')}")

        if len(parts) == 1:
            return parts[0]
        elif len(parts) == 2:
            return f"{parts[0]} und {parts[1]}"
        else:
            return f"{parts[0]}, {parts[1]} und {parts[2]}"

    # ==========================
    # SERVERSTATUS und GUI-MODI
    # ==========================

    def checkServerStatus(self):
        """Prüft, ob der NAS-Server erreichbar ist."""
        try:
            nas_ip = self.config.get("nas_ip")
            self.logger.log_action("Prüfe Serverstatus", f"IP: {nas_ip}")
            self.status_label.setText(tr("status_checking"))
            QApplication.processEvents()

            try:
                result = subprocess.run(
                    ["ping", "-c", "2", "-t", "2", nas_ip],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )

                if result.returncode == 0 and "bytes from" in result.stdout:
                    self.server_online = True
                    self.logger.log_action("Server online", f"IP: {nas_ip}")
                    self.handleOnline()
                else:
                    self.server_online = False
                    self.logger.log_action(
                        "Server offline", f"IP: {nas_ip} - kein Ping"
                    )
                    self.handleOffline()

            except Exception as e:
                self.server_online = False
                self.logger.log_error("Ping fehlgeschlagen", f"IP: {nas_ip}", e)
                self.handleOffline()

        except Exception as e:
            self.logger.log_error("Fehler bei Serverstatus-Prüfung", str(e), e)
            self.server_online = False
            self.handleOffline()

    def handleOnline(self):
        """Konfiguriert GUI für Online-Modus."""
        try:
            self.logger.log_action("Server online - Normalmodus aktiv")

            # 1. ZUERST die Statusmeldung
            self.say_message(tr("say_server_online"))
            self.status_label.setText(tr("status_online"))
            self.status_label.setStyleSheet(
                "color: #4CAF50; font-size: 14px; font-weight: bold; padding: 10px;"
            )

            # 2. GUI aktualisieren
            self.volumes_title_label.setText(tr("volumes_title"))
            self.volumes_title_label.setStyleSheet("font-weight: bold; color: #4CAF50;")

            main_vol = self.get_main_volume()
            for volume_name, checkbox in self.volume_checkboxes.items():
                if volume_name != main_vol:  # Dynamisch, nicht hartcodiert
                    checkbox.setEnabled(True)
                    checkbox.stateChanged.connect(
                        lambda state, v=volume_name: self.on_volume_checkbox_changed(
                            v, state
                        )
                    )

            self.select_all_btn.setEnabled(True)
            self.showAllButtons()
            self.button2.setFocus()
            self.update_checkbox_status()

            # 3. Timer-Limit für Auto-Shutdown setzen
            self.timeout_counter = 0
            self.timeout_limit = self.config.get("auto_shutdown_delay", 120)

            self.logger.log_action(
                "Auto-Shutdown Timer-Limit gesetzt",
                f"Verzögerung: {self.timeout_limit}s",
            )

            # 4. Auto-Timer starten, wenn Voraussetzungen erfüllt
            #    (Online: Braucht Passwort für Mac-Shutdown)
            if self._start_auto_timer_safe("handleOnline"):
                self.say_timer_status()
            else:
                self.logger.log_action(
                    "Auto-Timer nicht gestartet (handleOnline, keine Voraussetzungen)"
                )

            self._update_scheduled_button_tooltip()
            self._update_scheduled_button_text()

            # 5. JETZT die Timer-Sprachausgabe (NACH dem Setzen des Limits)
            # 5. Auto-Timer-Status nur ansagen, wenn kein Zeitgeber läuft
            if not getattr(self, "scheduled_active", False):
                self.say_timer_status()
            else:
                self.logger.log_action(
                    "Auto-Timer-Sprachausgabe übersprungen "
                    "(Zeitgeber aktiv)"
                )

        except Exception as e:
            self.logger.log_error("Fehler im Online-Modus", str(e), e)

    def handleOffline(self):
        """Konfiguriert GUI für Offline-Modus."""
        try:
            self.logger.log_action("Server offline")

            # 1. ZUERST die Statusmeldung
            self.say_message(tr("say_server_offline"))
            self.status_label.setText(tr("status_offline"))
            self.status_label.setStyleSheet(
                "color: #f44336; font-weight: bold; padding: 10px;"
            )

            # 2. GUI aktualisieren
            self.volumes_title_label.setText(tr("volumes_title_offline"))
            self.volumes_title_label.setStyleSheet("font-weight: bold; color: #888888;")

            main_vol = self.get_main_volume()  # Dynamisch, nicht hartcodiert
            for volume_name, checkbox in self.volume_checkboxes.items():
                checkbox.setEnabled(True)
                if volume_name != main_vol:  # Haupt-Volume wird nicht markiert
                    checkbox.setToolTip(tr("volumes_mount_tooltip"))

            self.select_all_btn.setEnabled(True)
            self.select_all_btn.setStyleSheet("")
            self.select_all_btn.setToolTip(tr("volumes_mount_tooltip"))

            self.showAllButtons()
            self.button4.setFocus()

            # 3. Timer-Limit für Auto-Start setzen
            self.timeout_counter = 0
            self.timeout_limit = self.config.get("auto_start_delay", 120)

            self.logger.log_action(
                "Auto-Start Timer-Limit gesetzt", f"Verzögerung: {self.timeout_limit}s"
            )

            # 4. Auto-Timer starten — im Offline-Modus (WOL) immer
            self._auto_shutdown_allowed = True
            self.timeout_counter = 0
            self.auto_timer.start(1000)
            self.logger.log_action(
                "Auto-Timer gestartet (Offline, WOL-Timer)"
            )

            # 5. Auto-Timer-Status nur ansagen, wenn kein Zeitgeber läuft
            if not getattr(self, "scheduled_active", False):
                self.say_timer_status()
            else:
                self.logger.log_action(
                    "Auto-Timer-Sprachausgabe übersprungen "
                    "(Zeitgeber aktiv)"
                )

            self._update_scheduled_button_tooltip()
            self._update_scheduled_button_text()


        except Exception as e:
            self.logger.log_error("Fehler im Offline-Modus", str(e), e)

    def autoSelect(self):
        """Wird jede Sekunde aufgerufen und löst Auto-Aktion nach Timeout aus."""
        # Nicht ausführen, wenn ein Zeitgeber läuft
        if getattr(self, "scheduled_active", False):
            return

        # Nicht ausführen, wenn Auto-Shutdown nicht erlaubt ist
        # (Default False = sicherer)
        if not getattr(self, "_auto_shutdown_allowed", False):
            return

        # Nicht ausführen, wenn pausiert
        if self.timer_paused:
            return

        try:
            self.timeout_counter += 1
            remaining = int(self.timeout_limit) - self.timeout_counter

            if self.server_online:
                self.status_label.setText(tr("timer_shutdown").format(remaining))
                if self.timeout_counter >= self.timeout_limit:
                    self.auto_timer.stop()
                    self.logger.log_action(
                        "Auto-Shutdown ausgelöst", "Timeout erreicht"
                    )
                    self.handleChoice("both")
            else:
                self.status_label.setText(tr("timer_start").format(remaining))
                if self.timeout_counter >= self.timeout_limit:
                    self.auto_timer.stop()
                    self.logger.log_action("Auto-Start ausgelöst", "Timeout erreicht")
                    self.handleChoice("start_nas")
                    self.pause_btn.setVisible(False)

            # Stop-Button-Zustand bei Bedarf aktualisieren
            # (nur einmal pro Sekunde, nicht bei jedem Tick neu zeichnen)
            if hasattr(self, "stop_btn"):
                self.update_stop_button_state()
                self.status_label.setText(tr("timer_start").format(remaining))
                if self.timeout_counter >= self.timeout_limit:
                    self.auto_timer.stop()
                    self.logger.log_action("Auto-Start ausgelöst", "Timeout erreicht")
                    self.handleChoice("start_nas")
                    self.pause_btn.setVisible(False)
        except Exception as e:
            self.logger.log_error("Fehler im Auto-Select Timer", str(e), e)

    def handleChoice(self, choice):
        """Verarbeitet Benutzeraktionen oder Auto-Aktionen."""
        try:
            self.logger.log_action(f"Benutzeraktion: {choice}")
            if hasattr(self, "auto_timer"):
                self.auto_timer.stop()
                self.timer_paused = False

            self.is_operation_running = True
            self.hideAllButtons()
            self.progress_bar.setVisible(True)
            self.progress_bar.setValue(10)

            # ═══════════════════════════════════════════════════════════
            # ZEITGEBER-KONFLIKT prüfen (für alle Shutdown-Ziele)
            # ═══════════════════════════════════════════════════════════
            # Wenn ein Zeitgeber läuft UND ein manueller Shutdown
            # ausgelöst wird (both / mac_only), muss der User warnen.
            if choice in ("both", "mac_only"):
                if getattr(self, "scheduled_active", False) and self.scheduled_target_time:
                    from datetime import datetime
                    remaining_seconds = int(
                        (self.scheduled_target_time - datetime.now()).total_seconds()
                    )
                    duration_str = self._format_duration(remaining_seconds)

                    # Ziel-Name des laufenden Timers (für die Meldung)
                    target_names = {
                        "both": tr("sched_target_both"),
                        "nas_only": tr("sched_target_nas"),
                        "mac_only": tr("sched_target_mac"),
                        "coffee": tr("sched_target_coffee"),
                    }
                    running_target_name = target_names.get(
                        self.scheduled_target_action, "?"
                    )

                    # ─── Ziel-spezifische Konfliktbehandlung ───
                    if self.scheduled_target_action == "coffee":
                        # Coffee-Timer → eigener Warntext
                        if not self._msgbox_question(
                            tr("coffee_conflict_title"),
                            tr("coffee_conflict_message").format(duration_str),
                        ):
                            self.logger.log_action(
                                "Shutdown abgebrochen: Coffee-Timer aktiv, "
                                "User hat abgelehnt"
                            )
                            self.is_operation_running = False
                            self.checkServerStatus()
                            return
                        self.logger.log_action(
                            "Shutdown trotz Coffee-Timer bestätigt – "
                            "breche Coffee-Timer ab"
                        )
                    else:
                        # Shutdown-Timer (both / nas_only / mac_only)
                        if not self._msgbox_question(
                            tr("shutdown_timer_conflict_title"),
                            tr("shutdown_timer_conflict_message").format(
                                running_target_name, duration_str
                            ),
                        ):
                            self.logger.log_action(
                                "Shutdown abgebrochen: Timer aktiv, "
                                "User hat abgelehnt"
                            )
                            self.is_operation_running = False
                            self.checkServerStatus()
                            return
                        self.logger.log_action(
                            "Shutdown trotz aktivem Timer bestätigt – "
                            "breche Timer ab"
                        )

                    # User hat bestätigt → laufenden Timer beenden
                    self._cancel_scheduled_shutdown()

            # ═══════════════════════════════════════════════════════════
            # ZIEL: "both" (Mac + NAS)
            # ═══════════════════════════════════════════════════════════
            if choice == "both":
                self.logger.log_action("Starte Shutdown (Mac + NAS)")

                # Passwort-Voraussetzungen prüfen
                if not self._ensure_mac_shutdown_prerequisites():
                    self.logger.log_action(
                        "Shutdown abgebrochen: Passwort-Voraussetzung nicht erfüllt"
                    )
                    QMessageBox.information(
                        self,
                        tr("sched_dialog_title"),
                        tr("shutdown_no_password_message"),
                    )
                    self.is_operation_running = False
                    self.checkServerStatus()
                    return

                self.say_message(tr("say_shutdown_started"))
                self.status_label.setText(tr("status_shutdown"))
                self.pause_btn.setVisible(False)

                # Volumes auswerfen und Erfolg prüfen
                self.progress_bar.setValue(25)
                eject_success = self.ejectNetworkDrives()

                if not eject_success:
                    if not self._msgbox_question(
                        tr("warning_title"),
                        tr("warning_eject_failed_continue"),
                    ):
                        self.logger.log_action(
                            "Shutdown abgebrochen nach Eject-Fehler"
                        )
                        self.is_operation_running = False
                        self.checkServerStatus()
                        return
                    self.logger.log_action(
                        "User hat Shutdown trotz Eject-Fehler bestätigt"
                    )
                else:
                    self.logger.log_action("Volumes erfolgreich ausgeworfen")

                self.progress_bar.setValue(50)

                # NAS-Shutdown senden
                self.logger.log_action("Sende NAS-Shutdown...")
                nas_success = self.shutdownNAS()
                self.progress_bar.setValue(70)

                if nas_success:
                    self.logger.log_action("NAS-Shutdown-Befehl gesendet")
                    self.status_label.setText(
                        tr("status_shutdown_nas_sent_mac_follows")
                    )
                else:
                    self.logger.log_action(
                        "NAS-Shutdown fehlgeschlagen, fahre trotzdem Mac herunter..."
                    )
                    self.status_label.setText(
                        tr("status_shutdown_nas_failed_mac_still")
                    )

                # Wartezeit aus Konfiguration
                delay = self.config.get("shutdown_mac_delay", 5)
                QTimer.singleShot(
                    delay * 1000,
                    lambda: [self.shutdownMac(), self.progress_bar.setValue(100)],
                )
                QTimer.singleShot((delay + 3) * 1000, self.close)

            # ═══════════════════════════════════════════════════════════
            # ZIEL: "nas_only" (Nur NAS)
            # ═══════════════════════════════════════════════════════════
            elif choice == "nas_only":
                self.logger.log_action("Starte Shutdown (nur NAS)")
                self.say_message(tr("say_nas_shutdown"))
                self.status_label.setText(tr("status_shutdown_nas"))
                self.pause_btn.setVisible(False)

                # Volumes auswerfen und Erfolg prüfen
                self.progress_bar.setValue(25)
                eject_success = self.ejectNetworkDrives()

                if not eject_success:
                    if not self._msgbox_question(
                        tr("warning_title"),
                        tr("warning_eject_failed_continue"),
                    ):
                        self.logger.log_action(
                            "NAS-Shutdown abgebrochen nach Eject-Fehler"
                        )
                        self.is_operation_running = False
                        self.checkServerStatus()
                        return
                    self.logger.log_action(
                        "User hat NAS-Shutdown trotz Eject-Fehler bestätigt"
                    )

                self.progress_bar.setValue(50)

                # NAS herunterfahren
                self.shutdownNAS()
                self.progress_bar.setValue(66)

                # Warten und schließen
                QTimer.singleShot(
                    5000, lambda: [self.progress_bar.setValue(100), self.close()]
                )

            # ═══════════════════════════════════════════════════════════
            # ZIEL: "mac_only" (Nur Mac)
            # ═══════════════════════════════════════════════════════════
            elif choice == "mac_only":
                self.logger.log_action("Starte Shutdown (nur Mac)")

                # Passwort-Voraussetzungen prüfen
                if not self._ensure_mac_shutdown_prerequisites():
                    self.logger.log_action(
                        "Mac-Shutdown abgebrochen: Passwort-Voraussetzung nicht erfüllt"
                    )
                    QMessageBox.information(
                        self,
                        tr("sched_dialog_title"),
                        tr("shutdown_no_password_message"),
                    )
                    self.is_operation_running = False
                    self.checkServerStatus()
                    return

                self.say_message(tr("say_shutdown_mac_only"))
                self.status_label.setText(tr("status_shutdown_mac_only"))
                self.pause_btn.setVisible(False)

                # WICHTIG: KEIN ejectNetworkDrives() - NAS bleibt an!
                # Netzwerk-Mounts bleiben bestehen.

                self.progress_bar.setValue(50)

                delay = self.config.get("shutdown_mac_delay", 5)
                QTimer.singleShot(
                    delay * 1000,
                    lambda: [self.shutdownMac(), self.progress_bar.setValue(100)],
                )
                QTimer.singleShot((delay + 3) * 1000, self.close)

            # ═══════════════════════════════════════════════════════════
            # ZIEL: "start_nas" (NAS hochfahren via WOL)
            # ═══════════════════════════════════════════════════════════
            elif choice == "start_nas":
                self.logger.log_action("Starte NAS via WOL")
                self.say_message(tr("say_starting_nas"))
                self.status_label.setText(tr("status_starting"))
                self.pause_btn.setVisible(False)
                self.progress_bar.setValue(20)
                self.startup_volumes = []
                for volume_name, checkbox in self.volume_checkboxes.items():
                    if checkbox.isChecked():
                        self.startup_volumes.append(volume_name)
                self.startNAS()

            # ═══════════════════════════════════════════════════════════
            # ZIEL: "cancel" (App schließen)
            # ═══════════════════════════════════════════════════════════
            elif choice == "cancel":
                # Zeitgeber läuft → warnen
                if getattr(self, "scheduled_active", False):
                    if not self._msgbox_question(
                        tr("close_blocked_title"),
                        tr("close_blocked_cancel_text"),
                    ):
                        self.logger.log_action(
                            tr("close_blocked_log_cancel_aborted")
                        )
                        self.is_operation_running = False
                        self.checkServerStatus()
                        return

                self.logger.log_action("Aktion abgebrochen")
                self.say_message(tr("say_cancelled"))
                self.status_label.setText(tr("status_cancelled"))
                self.progress_bar.setValue(100)
                QTimer.singleShot(1000, self.close)

            self.logger.flush()
        except Exception as e:
            self.logger.log_error("Fehler bei handleChoice", str(e), e)
            self.is_operation_running = False


    # ==============================
    # WAKE-ON-LAN FUNKTIONALITÄT
    # =============================

    def startNAS(self):
        """Startet den NAS-Server über Wake-on-LAN."""
        try:
            self.config.load_config()
            self.logger.log_action(
                "Starte NAS via WOL",
                f"MAC: {self.config.get('nas_mac')}, IP: {self.config.get('nas_ip')}",
            )
            self.status_label.setText(tr("status_wol_sending"))
            self.progress_bar.setVisible(True)
            self.progress_bar.setMaximum(100)
            self.progress_bar.setValue(10)

            nas_mac = self.config.get("nas_mac")
            nas_ip = self.config.get("nas_ip")

            success = False
            methods_tried = []

            # Methode 1: Python
            try:
                self.status_label.setText(tr("status_wol_sending"))
                QApplication.processEvents()
                self.send_wol_python(nas_mac, nas_ip)
                methods_tried.append("Python")
                success = True
                self.logger.log_action("WOL erfolgreich", "Python-Methode")
                self.status_label.setText(tr("status_wol_sent"))
            except Exception as e:
                methods_tried.append(f"Python fehlgeschlagen: {str(e)[:50]}...")
                self.logger.log_error("WOL Python-Methode fehlgeschlagen", str(e), e)
                self.status_label.setText(tr("status_wol_method_failed"))
                QApplication.processEvents()

            # Methode 2: wakeonlan
            if not success:
                try:
                    self.status_label.setText(tr("status_trying_wakeonlan"))
                    QApplication.processEvents()
                    result = subprocess.run(
                        ["which", "wakeonlan"],
                        capture_output=True,
                        text=True,
                        timeout=5,
                    )
                    if result.returncode == 0 and "wakeonlan" in result.stdout:
                        wol_result = subprocess.run(
                            ["wakeonlan", nas_mac],
                            capture_output=True,
                            text=True,
                            timeout=10,
                        )
                        if wol_result.returncode == 0:
                            methods_tried.append("wakeonlan")
                            success = True
                            self.logger.log_action(
                                "WOL erfolgreich", "wakeonlan-Befehl"
                            )
                            self.status_label.setText(tr("status_wol_sent"))
                        else:
                            methods_tried.append("wakeonlan Befehl fehlgeschlagen")
                            self.logger.log_error(
                                "WOL wakeonlan fehlgeschlagen", wol_result.stderr
                            )
                    else:
                        methods_tried.append("wakeonlan nicht installiert")
                        self.logger.log_action("wakeonlan nicht installiert")
                except Exception as e:
                    methods_tried.append(
                        f"wakeonlan Ausführung fehlgeschlagen: {str(e)[:50]}..."
                    )
                    self.logger.log_error("WOL wakeonlan Exception", str(e), e)
                    self.status_label.setText(tr("status_wol_method_failed"))
                    QApplication.processEvents()

            # Methode 3: etherwake
            if not success:
                try:
                    self.status_label.setText(tr("status_trying_etherwake"))
                    QApplication.processEvents()
                    interface = self.get_active_interface()
                    try:
                        ether_result = subprocess.run(
                            ["etherwake", "-i", interface, nas_mac],
                            capture_output=True,
                            text=True,
                            timeout=10,
                        )
                        if ether_result.returncode == 0:
                            methods_tried.append("etherwake ohne sudo")
                            success = True
                            self.logger.log_action(
                                "WOL erfolgreich", "etherwake ohne sudo"
                            )
                            self.status_label.setText(tr("status_wol_sent"))
                        else:
                            ether_result = subprocess.run(
                                ["sudo", "etherwake", "-i", interface, nas_mac],
                                capture_output=True,
                                text=True,
                                timeout=10,
                                input=f"{getpass.getuser()}\n",
                            )
                            if ether_result.returncode == 0:
                                methods_tried.append("etherwake mit sudo")
                                success = True
                                self.logger.log_action(
                                    "WOL erfolgreich", "etherwake mit sudo"
                                )
                                self.status_label.setText(tr("status_wol_sent"))
                            else:
                                methods_tried.append(
                                    "etherwake mit sudo fehlgeschlagen"
                                )
                                self.logger.log_error(
                                    "WOL etherwake mit sudo fehlgeschlagen",
                                    ether_result.stderr,
                                )
                    except Exception as e:
                        methods_tried.append(
                            f"etherwake Ausführung fehlgeschlagen: {str(e)[:50]}..."
                        )
                        self.logger.log_error("WOL etherwake Exception", str(e), e)
                except Exception as e:
                    methods_tried.append(f"etherwake Gesamtfehler: {str(e)[:50]}...")
                    self.logger.log_error("WOL etherwake Gesamtfehler", str(e), e)

            if success:
                self.logger.log_action(
                    "WOL erfolgreich", f"Methoden: {', '.join(methods_tried)}"
                )
                self.say_message(tr("say_waiting_server"))
                self.status_label.setText(tr("status_waiting"))
                self.progress_bar.setValue(30)
                self.waitForServerStart()
            else:
                self.logger.log_error(
                    "WOL komplett fehlgeschlagen",
                    f"Methoden: {', '.join(methods_tried)}",
                )
                self.say_message(tr("say_wol_failed"))
                self.status_label.setText(tr("status_wol_failed"))
                self.progress_bar.setValue(0)
                QTimer.singleShot(3000, self.close)

            self.logger.flush()
        except Exception as e:
            self.logger.log_error("Fehler bei startNAS", str(e), e)

    def send_wol_python(self, mac_address, nas_ip):
        """Sendet ein Wake-on-LAN Magic Packet über reine Python-Sockets."""
        try:
            mac_hex = mac_address.replace(":", "").replace("-", "")
            if len(mac_hex) != 12:
                raise ValueError(f"Ungültige MAC-Adresse: {mac_address}")

            mac_bytes = bytes.fromhex(mac_hex)
            magic_packet = b"\xff" * 6 + mac_bytes * 16

            broadcast_addresses = [
                "255.255.255.255",
                nas_ip.rsplit(".", 1)[0] + ".255",
                "192.168.1.255",
            ]

            wol_port = 9
            success = False

            for broadcast_addr in broadcast_addresses:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    sock.settimeout(2)
                    sock.sendto(magic_packet, (broadcast_addr, wol_port))
                    sock.close()
                    self.logger.log_action(
                        "WOL Python-Methode",
                        f"Packet an {broadcast_addr}:{wol_port} gesendet",
                    )
                    success = True
                    break
                except socket.error as e:
                    self.logger.log_error(
                        "WOL Python Socket-Fehler", f"{broadcast_addr}: {e}", e
                    )
                    continue

            if not success:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    sock.settimeout(2)
                    sock.sendto(magic_packet, (nas_ip, wol_port))
                    sock.close()
                    self.logger.log_action(
                        "WOL Python-Methode",
                        f"Packet direkt an {nas_ip}:{wol_port} gesendet",
                    )
                    success = True
                except socket.error as e:
                    self.logger.log_error(
                        "WOL Python direkter Socket-Fehler", str(e), e
                    )
                    raise Exception(f"WOL über Python-Sockets fehlgeschlagen: {e}")

            return success
        except Exception as e:
            self.logger.log_error("send_wol_python Fehler", str(e), e)
            raise

    def get_active_interface(self):
        """Ermittelt das aktive Netzwerkinterface für WOL."""
        try:
            result = subprocess.run(
                ["route", "get", "default"], capture_output=True, text=True
            )

            for line in result.stdout.splitlines():
                if "interface:" in line:
                    interface = line.split(":")[1].strip()
                    self.logger.log_action(
                        "Interface ermittelt", f"route get: {interface}"
                    )
                    return interface

        except Exception as e:
            self.logger.log_error(
                "Interface-Ermittlung route get fehlgeschlagen", str(e), e
            )

        try:
            result = subprocess.run(
                ["networksetup", "-listallhardwareports"],
                capture_output=True,
                text=True,
            )

            lines = result.stdout.splitlines()
            for i, line in enumerate(lines):
                if "Device:" in line and i + 1 < len(lines) and "en" in lines[i + 1]:
                    interface = lines[i + 1].split(":")[1].strip()
                    self.logger.log_action(
                        "Interface ermittelt", f"networksetup: {interface}"
                    )
                    return interface

        except Exception as e:
            self.logger.log_error(
                "Interface-Ermittlung networksetup fehlgeschlagen", str(e), e
            )

        self.logger.log_action("Interface default", "en0")
        return "en0"

    # ==============================
    # SERVERBEREITSCHAFT
    # ==============================

    def waitForServerStart(self):
        """Startet einen Thread, der auf Server-Start wartet."""
        self.wait_thread = threading.Thread(target=self._waitForServer)
        self.wait_thread.daemon = True
        self.wait_thread.start()

    def _waitForServer(self):
        """Thread-Funktion: Prüft regelmäßig, ob Server online ist."""
        try:
            nas_ip = self.config.get("nas_ip")
            total_wait = self.config.get("wol_wait_time", 180)
            check_interval = 10
            waited = 0

            self.logger.log_action("Warte auf Serverstart", f"Max: {total_wait}s")
            time.sleep(30)
            waited = 30
            QMetaObject.invokeMethod(
                self.progress_bar, "setValue", Qt.QueuedConnection, Q_ARG(int, 40)
            )

            while waited < total_wait:
                try:
                    result = subprocess.run(
                        ["ping", "-c", "2", "-t", "3", nas_ip],
                        capture_output=True,
                        text=True,
                        timeout=5,
                    )

                    if result.returncode == 0 and "bytes from" in result.stdout:
                        self.logger.log_action(
                            "Server startet", f"Erreichbar nach {waited}s"
                        )
                        QMetaObject.invokeMethod(
                            self, "serverIsUp", Qt.QueuedConnection
                        )
                        return
                except Exception as e:
                    self.logger.log_error(
                        "Ping während Wartezeit fehlgeschlagen", str(e), e
                    )

                progress = 40 + int((waited / total_wait) * 40)
                QMetaObject.invokeMethod(
                    self.progress_bar,
                    "setValue",
                    Qt.QueuedConnection,
                    Q_ARG(int, progress),
                )

                time.sleep(check_interval)
                waited += check_interval

            self.logger.log_error(
                "Serverstart timeout", f"Nach {total_wait}s nicht erreichbar"
            )
            QMetaObject.invokeMethod(self, "serverTimeout", Qt.QueuedConnection)
        except Exception as e:
            self.logger.log_error("Fehler im Wartethread", str(e), e)

    @pyqtSlot()
    def serverIsUp(self):
        """Wird aufgerufen, wenn Server erfolgreich gestartet wurde."""
        try:
            self.logger.log_action("Server erfolgreich gestartet")
            self.say_message(tr("say_server_reachable"))
            self.status_label.setText(tr("status_server_online"))

            if self.progress_bar:
                self.progress_bar.setValue(70)

            smb_wait = self.config.get("smb_wait_time", 30)
            QTimer.singleShot(smb_wait * 1000, self._mountVolumesAfterDelay)
        except Exception as e:
            self.is_operation_running = False
            self.logger.log_error("Fehler in serverIsUp", str(e), e)

    @pyqtSlot()
    def serverTimeout(self):
        """Wird aufgerufen, wenn Server-Start timeoutet."""
        try:
            self.logger.log_action("Serverstart timeout")
            self.say_message(tr("say_server_timeout"))
            self.status_label.setText(tr("status_timeout"))
            self.is_operation_running = False
            QTimer.singleShot(3000, self.close)
        except Exception as e:
            self.is_operation_running = False
            self.logger.log_error("Fehler in serverTimeout", str(e), e)

    # ========================================
    # VOLUME-MANAGEMENT
    # ========================================

    def on_volume_checkbox_changed(self, volume_name, state):
        """Wird aufgerufen, wenn Volume-Checkbox geändert wird."""
        try:
            if hasattr(self, "auto_timer"):
                self.auto_timer.stop()

            QTimer.singleShot(
                300, lambda: self.process_volume_change(volume_name, state)
            )
        except Exception as e:
            self.logger.log_error("Fehler in on_volume_checkbox_changed", str(e), e)

    def get_main_volume(self):
        """Gibt das erste Volume aus der Volume-Liste zurück (Haupt-Volume)."""
        if self.all_volumes:
            return self.all_volumes[0]
        return "NAS Dokumente"  # Fallback, falls Liste leer

    def process_volume_change(self, volume_name, state):
        """Verarbeitet Volume-Änderungen (Mounten/Auswerfen)."""
        try:
            if state:
                self.logger.log_action("Volume mounten", volume_name)
                self.status_label.setText(
                    tr("status_mounting_volume").format(volume_name)
                )
                success = self.mount_single_volume(volume_name)
                if not success:
                    self.volume_checkboxes[volume_name].setChecked(False)
                    self.logger.log_error("Volume mounten fehlgeschlagen", volume_name)
                    self.say_message(tr("say_mount_error"))
                    self.status_label.setText(tr("status_error").format(volume_name))
                else:
                    self.logger.log_action("Volume gemountet", volume_name)
                    self.say_message(tr("say_mount_volume").format(volume_name), wait=False)
                    self.status_label.setText(tr("status_mounted").format(volume_name))
            else:
                self.logger.log_action("Volume auswerfen", volume_name)
                self.say_message(tr("say_unmount_volume").format(volume_name))
                self.status_label.setText(tr("status_unmounting").format(volume_name))
                success = self.unmount_single_volume(volume_name)
                if not success:
                    self.volume_checkboxes[volume_name].setChecked(True)
                    self.logger.log_error(
                        "Volume auswerfen fehlgeschlagen", volume_name
                    )
                    self.say_message(tr("say_unmount_error"))
                    self.status_label.setText(
                        tr("status_error_unmount").format(volume_name)
                    )
                else:
                    self.logger.log_action("Volume ausgewerfen", volume_name)
                    self.status_label.setText(
                        tr("status_unmounted").format(volume_name)
                    )
        except Exception as e:
            self.logger.log_error("Fehler in process_volume_change", str(e), e)

    def toggle_all_volumes(self, checked):
        """Schaltet alle Volumes gleichzeitig um."""
        main_vol = self.get_main_volume()
        if checked:
            for volume_name, checkbox in self.volume_checkboxes.items():
                if volume_name != main_vol and not checkbox.isChecked():
                    checkbox.setChecked(True)
        else:
            for volume_name, checkbox in self.volume_checkboxes.items():
                if volume_name != main_vol and checkbox.isChecked():
                    checkbox.setChecked(False)

    def update_checkbox_status(self):
        """Aktualisiert Checkbox-Status basierend auf gemounteten Volumes."""
        try:
            mount_result = subprocess.run(["mount"], capture_output=True, text=True)
            mounted_text = mount_result.stdout

            main_vol = self.get_main_volume()
            for volume_name, checkbox in self.volume_checkboxes.items():
                if volume_name == main_vol:  # Dynamisch, nicht hartcodiert
                    continue

                is_mounted = volume_name in mounted_text
                checkbox.blockSignals(True)
                checkbox.setChecked(is_mounted)
                checkbox.blockSignals(False)

            self.logger.log_action("Checkbox-Status aktualisiert")
        except Exception as e:
            self.logger.log_error("Fehler in update_checkbox_status", str(e), e)

    def _mountVolumesAfterDelay(self):
        """Mountet Volumes nach Verzögerung."""
        try:
            self.logger.log_action("Starte Volume-Mounting")
            self.status_label.setText(tr("status_mounting"))

            main_vol = self.get_main_volume()
            volumes_to_mount = [main_vol]  # Haupt-Volume zuerst
            for volume_name in self.startup_volumes:
                if volume_name != main_vol and volume_name not in volumes_to_mount:
                    volumes_to_mount.append(volume_name)

            success_count = 0
            self.progress_bar.setValue(70)
            successfully_mounted = []

            mount_retries = self.config.get("mount_retries", 3)

            for i, volume_name in enumerate(volumes_to_mount):
                self.status_label.setText(
                    tr("status_mounting_volume").format(volume_name)
                )
                QApplication.processEvents()

                # Haupt-Volume bekommt etwas mehr Zeit
                if volume_name == main_vol:
                    time.sleep(5)

                success = self.mount_single_volume_with_retry(
                    volume_name, retries=mount_retries
                )
                if success:
                    success_count += 1
                    successfully_mounted.append(volume_name)
                    self.logger.log_action("Volume erfolgreich gemountet", volume_name)
                    self.say_message(tr("say_mount_volume").format(volume_name), wait=True)
                else:
                    self.logger.log_error("Volume mounten fehlgeschlagen", volume_name)

                progress = 70 + int(((i + 1) / len(volumes_to_mount)) * 30)
                self.progress_bar.setValue(progress)
                time.sleep(3)

            self.progress_bar.setValue(100)
            if success_count > 0:
                self.logger.log_action(
                    "Volume-Mounting abgeschlossen",
                    f"{success_count} von {len(volumes_to_mount)} erfolgreich",
                )
                self.status_label.setText(
                    f"{success_count} von {len(volumes_to_mount)} Volumes gemountet ✓"
                )
            else:
                self.logger.log_error("Volume-Mounting komplett fehlgeschlagen")
                self.say_message(tr("say_mount_failed"))
                self.status_label.setText(tr("status_mount_failed"))

            # Operation beendet
            self.is_operation_running = False
            QTimer.singleShot(2000, self.close)
        except Exception as e:
            self.logger.log_error("Fehler in _mountVolumesAfterDelay", str(e), e)
            self.is_operation_running = False

    def mount_single_volume(self, volume_name):
        """Mountet ein einzelnes Volume über SMB."""
        try:
            nas_user = self.config.get("nas_user")
            nas_ip = self.config.get("nas_ip")

            smb_url = f"smb://{nas_user}@{nas_ip}/{volume_name}"
            apple_script = f'try\n  mount volume "{smb_url}"\n  return "success"\non error err\n  return "error"\nend try'

            result = subprocess.run(
                ["osascript", "-e", apple_script],
                capture_output=True,
                text=True,
                timeout=30,
            )

            return "success" in result.stdout
        except Exception as e:
            self.logger.log_error(
                "mount_single_volume Fehler", f"{volume_name}: {e}", e
            )
            return False

    def mount_single_volume_with_retry(self, volume_name, retries=3):
        """Mountet ein Volume mit Wiederholungsversuchen."""
        nas_user = self.config.get("nas_user")
        nas_ip = self.config.get("nas_ip")

        for attempt in range(retries):
            try:
                if attempt > 0:
                    wait_time = 5 * attempt
                    self.logger.log_action(
                        "Volume-Mount Wiederholung",
                        f"{volume_name} Versuch {attempt+1}/{retries} nach {wait_time}s",
                    )
                    time.sleep(wait_time)

                smb_url = f"smb://{nas_user}@{nas_ip}/{volume_name}"
                apple_script = f'try\n  mount volume "{smb_url}"\n  return "success"\non error err\n  return "error"\nend try'

                result = subprocess.run(
                    ["osascript", "-e", apple_script],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )

                if "success" in result.stdout:
                    time.sleep(2)
                    mount_check = subprocess.run(
                        ["mount"], capture_output=True, text=True
                    )
                    if volume_name in mount_check.stdout:
                        return True
                    else:
                        self.logger.log_error(
                            "Volume gemeldet aber nicht in mount-Liste", volume_name
                        )
                        continue

            except Exception as e:
                self.logger.log_error(
                    "Volume-Mount Versuch fehlgeschlagen",
                    f"{volume_name} Versuch {attempt+1}: {e}",
                    e,
                )
                continue

        return False

    def unmount_single_volume(self, volume_name):
        """Wirft ein einzelnes Volume aus."""
        try:
            mount_check = subprocess.run(["mount"], capture_output=True, text=True)
            if volume_name not in mount_check.stdout:
                return True

            apple_script = f"""
            try
                tell application "Finder"
                    eject disk "{volume_name}"
                end tell
                return "success"
            on error errMsg
                try
                    do shell script "diskutil unmount '/Volumes/{volume_name}'"
                    return "success"
                on error
                    return "error"
                end try
            end try
            """

            result = subprocess.run(
                ["osascript", "-e", apple_script],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if "success" in result.stdout:
                time.sleep(1)
                mount_check = subprocess.run(["mount"], capture_output=True, text=True)
                return volume_name not in mount_check.stdout
            else:
                safe_name = volume_name.replace(" ", r"\ ")
                mount_point = f"/Volumes/{safe_name}"

                result = subprocess.run(
                    ["diskutil", "unmount", "force", mount_point],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )

                if result.returncode == 0:
                    time.sleep(1)
                    mount_check = subprocess.run(
                        ["mount"], capture_output=True, text=True
                    )
                    return volume_name not in mount_check.stdout
                else:
                    subprocess.run(
                        ["umount", "-f", mount_point],
                        stderr=subprocess.DEVNULL,
                        stdout=subprocess.DEVNULL,
                        timeout=5,
                    )
                    time.sleep(1)
                    mount_check = subprocess.run(
                        ["mount"], capture_output=True, text=True
                    )
                    return volume_name not in mount_check.stdout

        except Exception as e:
            self.logger.log_error(
                "unmount_single_volume Fehler", f"{volume_name}: {e}", e
            )
            return False

    # umfangreiche Logausgaben sind auskommentiert
    def ejectNetworkDrives(self) -> bool:
        """
        Wirft alle Netzwerklaufwerke aus.

        Wichtig:
          - `home` und `homes` sind System-Volumes. Ihr Auswurf wird
            versucht, aber ein Fehlschlag oder automatisches Remount
            durch macOS führt NICHT zu einem Fehler-Rückgabewert.
          - Andere Volumes müssen erfolgreich ausgeworfen werden, sonst
            gibt die Methode `False` zurück.
          - Kein blockierender Dialog – der NAS-Shutdown läuft trotzdem.

        Rückgabe:
            True  → alle wichtigen Volumes weg (home/homes dürfen bleiben)
            False → mindestens ein normales Volume ließ sich nicht auswerfen
        """
        # ═══════════════════════════════════════════════════════════════
        # Umfangreiches Debug (bei Bedarf einkommentieren)
        # ═══════════════════════════════════════════════════════════════
        # print("\n" + "=" * 70)
        # print("DEBUG ejectNetworkDrives() START")
        # print("=" * 70)

        self.logger.log_action("=== ejectNetworkDrives START ===")

        # System-Volumes, die nicht zwingend ausgeworfen werden müssen
        SYSTEM_VOLUMES_SOFT = {"home", "homes"}

        try:
            self.logger.log_action("Starte Auswerfen aller Netzwerklaufwerke")
            all_volumes = list(self.volume_checkboxes.keys())

            # Umfangreiches Debug (bei Bedarf einkommentieren)
            # print(f"DEBUG all_volumes ({len(all_volumes)}): {all_volumes}")

            # ─── Schritt 1: Welche Volumes sind gemountet? ───
            mount_check = subprocess.run(
                ["mount"], capture_output=True, text=True
            )
            mounted_volumes = []
            soft_volumes = []
            hard_volumes = []

            for volume_name in all_volumes:
                if volume_name in mount_check.stdout:
                    mounted_volumes.append(volume_name)
                    if volume_name in SYSTEM_VOLUMES_SOFT:
                        soft_volumes.append(volume_name)
                        self.logger.log_action(
                            "Volume ist gemountet (System-Volume)",
                            volume_name,
                        )
                    else:
                        hard_volumes.append(volume_name)
                        self.logger.log_action(
                            "Volume ist gemountet",
                            volume_name,
                        )

            self.logger.log_action(
                "Mounted-Volumes",
                f"{len(mounted_volumes)}: "
                f"{', '.join(mounted_volumes) if mounted_volumes else '(keine)'}",
            )

            # Umfangreiches Debug (bei Bedarf einkommentieren)
            # print(f"DEBUG mounted_volumes ({len(mounted_volumes)}): "
            #       f"{mounted_volumes}")
            # print(f"DEBUG soft_volumes ({len(soft_volumes)}): {soft_volumes}")
            # print(f"DEBUG hard_volumes ({len(hard_volumes)}): {hard_volumes}")
            # for line in mount_check.stdout.splitlines():
            #     if "smbfs" in line.lower():
            #         print(f"DEBUG   mount: {line.strip()[:140]}")

            if not mounted_volumes:
                self.logger.log_action("Keine Volumes zum Auswerfen gefunden")
                return True

            # ═══════════════════════════════════════════════════════════
            # Schritt 2: Massenauswurf per AppleScript
            # ═══════════════════════════════════════════════════════════
            self.status_label.setText(tr("status_unmount_all"))
            QApplication.processEvents()

            applescript_cmd = """
            tell application "Finder"
                set ejectedVolumes to {}
                try
            """
            for volume_name in mounted_volumes:
                applescript_cmd += f'\n        eject disk "{volume_name}"'
            applescript_cmd += """
                    set ejectedVolumes to "success"
                on error errMsg
                    set ejectedVolumes to "error: " & errMsg
                end try
                return ejectedVolumes
            end tell
            """

            try:
                result = subprocess.run(
                    ["osascript", "-e", applescript_cmd],
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                self.logger.log_action(
                    "AppleScript Massenauswurf",
                    f"rc={result.returncode}, "
                    f"stdout='{result.stdout.strip()[:80]}'",
                )
            except Exception as e:
                self.logger.log_error(
                    "AppleScript Auswerfen fehlgeschlagen", str(e), e
                )

            # Warte auf SMB-Teardown
            QApplication.processEvents()
            time.sleep(2)
            QApplication.processEvents()

            # ─── Schritt 3: Hängende Volumes einzeln nachbehandeln ───
            mount_check = subprocess.run(
                ["mount"], capture_output=True, text=True
            )
            remaining_volumes = [
                v for v in mounted_volumes if v in mount_check.stdout
            ]
            self.logger.log_action(
                "Nach AppleScript noch gemountet",
                f"{len(remaining_volumes)}: "
                f"{', '.join(remaining_volumes) if remaining_volumes else '(keine)'}",
            )

            # ═══════════════════════════════════════════════════════════
            # Nachbehandlung pro hängendem Volume – 3 Stufen
            # ═══════════════════════════════════════════════════════════
            for volume_name in remaining_volumes:
                try:
                    safe_name = volume_name.replace(" ", r"\ ")
                    mount_point = f"/Volumes/{safe_name}"

                    self.status_label.setText(
                        tr("status_unmounting").format(volume_name)
                    )
                    QApplication.processEvents()

                    self.logger.log_action(
                        f"Nachbehandlung: {volume_name}",
                        f"mount_point: {mount_point}",
                    )

                    # ─── Stufe 1: diskutil unmount (sanft) ───
                    result = subprocess.run(
                        ["diskutil", "unmount", mount_point],
                        capture_output=True,
                        text=True,
                        timeout=10,
                    )

                    # Umfangreiches Debug (bei Bedarf einkommentieren)
                    # print(f"DEBUG diskutil unmount {volume_name}: "
                    #       f"rc={result.returncode}")
                    # print(f"DEBUG   stdout: {result.stdout.strip()[:200]}")
                    # print(f"DEBUG   stderr: {result.stderr.strip()[:200]}")

                    if result.returncode == 0:
                        self.logger.log_action(
                            "Stufe 1 erfolgreich",
                            f"{volume_name} ausgeworfen (sanft)",
                        )
                        continue

                    # ─── Stufe 2: diskutil unmount force ───
                    result = subprocess.run(
                        ["diskutil", "unmount", "force", mount_point],
                        capture_output=True,
                        text=True,
                        timeout=10,
                    )

                    # Umfangreiches Debug (bei Bedarf einkommentieren)
                    # print(f"DEBUG diskutil unmount force {volume_name}: "
                    #       f"rc={result.returncode}")
                    # print(f"DEBUG   stdout: {result.stdout.strip()[:200]}")
                    # print(f"DEBUG   stderr: {result.stderr.strip()[:200]}")

                    if result.returncode == 0:
                        self.logger.log_action(
                            "Stufe 2 erfolgreich",
                            f"{volume_name} ausgeworfen (force)",
                        )
                        continue

                    # ─── Stufe 3: umount -f ───
                    result = subprocess.run(
                        ["umount", "-f", mount_point],
                        capture_output=True,
                        text=True,
                        timeout=5,
                    )

                    # Umfangreiches Debug (bei Bedarf einkommentieren)
                    # print(f"DEBUG umount -f {volume_name}: "
                    #       f"rc={result.returncode}")

                    if result.returncode == 0:
                        self.logger.log_action(
                            "Stufe 3 erfolgreich",
                            f"{volume_name} ausgeworfen (umount -f)",
                        )
                    else:
                        self.logger.log_action(
                            "Alle Stufen fehlgeschlagen",
                            f"{volume_name} konnte nicht ausgeworfen werden",
                        )

                except Exception as e:
                    self.logger.log_error(
                        "Fehler beim Auswerfen von Volume",
                        f"{volume_name}: {e}",
                        e,
                    )

                # Kurze Pause, damit Auto-Remounts erkannt werden
                QApplication.processEvents()
                time.sleep(1)
                QApplication.processEvents()

            # ═══════════════════════════════════════════════════════════
            # Schritt 4: Prüfen, was tatsächlich weg ist
            # ═══════════════════════════════════════════════════════════
            QApplication.processEvents()
            time.sleep(1)
            QApplication.processEvents()

            mount_check = subprocess.run(
                ["mount"], capture_output=True, text=True
            )

            ausgeworfen = []
            noch_da = []
            for volume_name in mounted_volumes:
                if volume_name in mount_check.stdout:
                    noch_da.append(volume_name)
                else:
                    ausgeworfen.append(volume_name)

            self.logger.log_action(
                "Zwischenstand",
                f"{len(ausgeworfen)} ausgeworfen, {len(noch_da)} noch gemountet",
            )

            # Merken, welche Volumes schon quittiert wurden
            bereits_quittiert = set(ausgeworfen.copy())

            # ═══════════════════════════════════════════════════════════
            # Schritt 5: Sprachquittung für erfolgreich ausgeworfene
            # ═══════════════════════════════════════════════════════════
            for volume_name in ausgeworfen:
                self.status_label.setText(
                    tr("status_unmounting").format(volume_name)
                )
                QApplication.processEvents()
                self.say_message(
                    tr("say_unmount_volume").format(volume_name), wait=True
                )
                QApplication.processEvents()

            # ═══════════════════════════════════════════════════════════
            # Schritt 6: Zweite Chance für noch hängende Volumes
            # ═══════════════════════════════════════════════════════════
            if noch_da:
                QApplication.processEvents()
                time.sleep(2)
                QApplication.processEvents()

                mount_check = subprocess.run(
                    ["mount"], capture_output=True, text=True
                )
                endgueltig_noch_da = []
                for volume_name in noch_da:
                    if volume_name in mount_check.stdout:
                        endgueltig_noch_da.append(volume_name)
                    else:
                        # Zwischenzeitlich weg → quittieren, falls nicht schon
                        if volume_name not in ausgeworfen:
                            ausgeworfen.append(volume_name)
                        if volume_name not in bereits_quittiert:
                            self.status_label.setText(
                                tr("status_unmounting").format(volume_name)
                            )
                            QApplication.processEvents()
                            self.say_message(
                                tr("say_unmount_volume").format(volume_name),
                                wait=True,
                            )
                            QApplication.processEvents()
                            bereits_quittiert.add(volume_name)
                noch_da = endgueltig_noch_da

            # ═══════════════════════════════════════════════════════════
            # Schritt 7: Auswertung
            # ═══════════════════════════════════════════════════════════
            hard_noch_da = [v for v in noch_da if v in hard_volumes]
            soft_noch_da = [v for v in noch_da if v in soft_volumes]

            # ─── Sonderfall: home bleibt systembedingt gemountet ───
            # macOS remountet den Home-Ordner automatisch (autofs, automounted).
            # Das ist unkritisch für den NAS-Shutdown.
            auto_remounted = []
            for v in soft_noch_da.copy():
                if v == "home":
                    auto_remounted.append(v)
                    soft_noch_da.remove(v)

            if auto_remounted:
                self.logger.log_action(
                    "home wurde von macOS automatisch neu gemountet",
                    "Auswurf nicht dauerhaft möglich – wird toleriert",
                )

            # ─── Auswertung loggen ───
            self.logger.log_action(
                "Auswertung",
                f"{len(ausgeworfen)} ausgeworfen, "
                f"{len(hard_noch_da)} normale Volumes hängen, "
                f"{len(soft_noch_da)} System-Volumes hängen, "
                f"{len(auto_remounted)} auto-remountet",
            )

            # ═══════════════════════════════════════════════════════════
            # Schritt 8: Ergebnis
            # ═══════════════════════════════════════════════════════════
            if hard_noch_da:
                # Normale Volumes konnten nicht ausgeworfen werden
                # → Warnung (aber kein Abbruch des Shutdowns hier —
                # das macht der Aufrufer in handleChoice)
                self.logger.log_error(
                    "Volumes konnten nicht ausgeworfen werden",
                    f"{len(hard_noch_da)}: {', '.join(hard_noch_da)}",
                )
                self.say_message(tr("say_unmount_error"))
                self.logger.log_action(
                    "=== ejectNetworkDrives ENDE (False) ==="
                )
                return False
            else:
                # Alle wichtigen Volumes weg
                if auto_remounted:
                    self.logger.log_action(
                        "Alle wichtigen Volumes ausgeworfen. "
                        "home wurde von macOS auto-remountet und toleriert.",
                    )
                elif soft_noch_da:
                    self.logger.log_action(
                        "Alle wichtigen Volumes ausgeworfen. "
                        "System-Volumes konnten nicht ausgeworfen werden.",
                        f"{', '.join(soft_noch_da)}",
                    )
                else:
                    self.logger.log_action(
                        "Alle Volumes erfolgreich ausgeworfen",
                        f"{len(ausgeworfen)} Volumes",
                    )

                self.logger.log_action(
                    "=== ejectNetworkDrives ENDE (True) ==="
                )
                return True

        except Exception as e:
            self.logger.log_error("ejectNetworkDrives Fehler", str(e), e)
            self.logger.log_action(
                "=== ejectNetworkDrives ENDE (Exception) ==="
            )
            return False

    def _is_volume_mounted(self, volume_name: str) -> bool:
        """Prüft, ob ein Volume aktuell gemountet ist."""
        try:
            result = subprocess.run(
                ["mount"], capture_output=True, text=True, timeout=5
            )
            return volume_name in result.stdout
        except Exception:
            return False

    # =====================================
    # HERUNTERFAHREN und SYSTEMOPERATIONEN
    # =====================================

    def detect_nas_vendor(self) -> tuple:
        """
        Erkennt den NAS-Hersteller per SSH.

        Liest aus:
          - /etc/os-release      (Linux-Standard)
          - /etc/synoinfo.conf   (Synology-spezifisch)
          - uname -a             (Fallback für alle Systeme)

        Rückgabe:
            (vendor_key: str or None, raw_output: str)
            vendor_key = None → Erkennung fehlgeschlagen
        """
        nas_user = self.config.get("nas_user", "")
        nas_ip = self.config.get("nas_ip", "")
        ssh_key = self.config.get("ssh_key_path", "")

        if not nas_user or not nas_ip or not ssh_key:
            self.logger.log_action(
                "Auto-Erkennung: Unvollständige SSH-Konfiguration"
            )
            return (None, "")

        expanded_key = os.path.expanduser(ssh_key)

        # Prüfen, ob der SSH-Key existiert
        if not os.path.exists(expanded_key):
            self.logger.log_error(
                "Auto-Erkennung: SSH-Key nicht gefunden",
                f"Pfad: {expanded_key}",
            )
            return (None, f"SSH-Key nicht gefunden: {expanded_key}")

        # ─── SSH-Befehl: OS-Info auslesen ───
        # Wir kombinieren mehrere Quellen — Linux, Synology, QNAP, macOS
        ssh_commands = (
            "cat /etc/os-release 2>/dev/null; "
            "echo '---SYNO---'; "
            "cat /etc/synoinfo.conf 2>/dev/null | head -20; "
            "echo '---QNAP---'; "
            "cat /etc/config/uLinux.conf 2>/dev/null | head -20; "
            "echo '---UNAME---'; "
            "uname -a 2>/dev/null"
        )

        cmd = [
            "ssh",
            "-i", expanded_key,   # ⬅️ KORREKT: expandierter Pfad
            "-o", "ConnectTimeout=5",
            "-o", "BatchMode=yes",
            "-o", "StrictHostKeyChecking=no",
            f"{nas_user}@{nas_ip}",
            ssh_commands,
        ]

        self.logger.log_action(
            "Auto-Erkennung gestartet",
            f"SSH zu {nas_user}@{nas_ip}",
        )

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=8,
            )

            if result.returncode != 0:
                error_text = result.stderr.strip()[:200]
                self.logger.log_error(
                    "SSH-Verbindung bei Auto-Erkennung fehlgeschlagen",
                    f"rc={result.returncode}, err={error_text}",
                )
                return (None, error_text)

            output = result.stdout
            self.logger.log_action(
                "SSH-Abfrage erfolgreich",
                f"Ausgabe-Länge: {len(output)} Zeichen",
            )

            # Umfangreiches Debug (bei Bedarf einkommentieren)
            # print("DEBUG Auto-Erkennung Ausgabe:")
            # print(output[:1000])

            # ─── Muster-Vergleich ───
            vendor_key = NasVendor.detect_vendor_from_os_info(output)

            if vendor_key:
                self.logger.log_action(
                    "Hersteller erkannt",
                    f"{vendor_key}",
                )
                return (vendor_key, output)
            else:
                self.logger.log_action(
                    "Hersteller konnte nicht erkannt werden",
                    f"Ausgabe: {output[:200]}",
                )
                return (None, output)

        except subprocess.TimeoutExpired:
            self.logger.log_error(
                "Auto-Erkennung Timeout",
                "SSH-Verbindung hat nicht innerhalb von 15 s geantwortet",
            )
            return (None, "Timeout")
        except Exception as e:
            self.logger.log_error(
                "Auto-Erkennung Fehler", str(e), e
            )
            return (None, str(e))

    def detect_nas_volumes(self) -> list:
        """
        Erkennt die verfügbaren Volume-Namen auf dem NAS.

        Strategie (hersteller-spezifisch mit Fallbacks):
          1. SSH: Hersteller-spezifische Pfade durchsuchen
             (z.B. /volume1, /share, /mnt)
             — Befehle werden in Häppchen aufgeteilt, damit die
               SSH-Argumentgrenze nicht überschritten wird.
             — Trennzeichen `@@@PATH:...@@@` statt `###`.
             — `; true` am Ende → Exit-Code immer 0.
          2. SSH: smbclient (Fallback für ältere NAS-Konfigurationen)
          3. Rückgabe: Liste von Volume-Namen (Strings)

        Rückgabe:
            Liste der gefundenen Volume-Namen oder leere Liste.
        """
        nas_user = self.config.get("nas_user", "")
        nas_ip = self.config.get("nas_ip", "")
        ssh_key = self.config.get("ssh_key_path", "")
        vendor_key = self.config.get("nas_vendor", "linux_generic")

        if not nas_user or not nas_ip or not ssh_key:
            self.logger.log_action(
                "Volume-Erkennung: Unvollständige SSH-Konfiguration"
            )
            return []

        expanded_key = os.path.expanduser(ssh_key)

        if not os.path.exists(expanded_key):
            self.logger.log_error(
                "Volume-Erkennung: SSH-Key nicht gefunden",
                f"Pfad: {expanded_key}",
            )
            return []

        # ─── SSH-Key in den Agent laden ───
        try:
            subprocess.run(
                ["ssh-add", expanded_key],
                capture_output=True,
                text=True,
                timeout=5,
            )
        except Exception:
            pass

        # ═══════════════════════════════════════════════════════════════
        # Methode 1: Hersteller-spezifische Pfade prüfen
        # ═══════════════════════════════════════════════════════════════
        vendor = NasVendor.get_vendor(vendor_key)
        if vendor and vendor.get("volume_paths"):
            paths = vendor["volume_paths"]
            self.logger.log_action(
                "Volume-Erkennung: Hersteller-spezifische Pfade",
                f"Hersteller: {vendor_key}, Pfade: {paths}",
            )

            # ─── Pfade in Häppchen aufteilen (SSH-Argumentgrenze) ───
            MAX_CMD_LENGTH = 4000
            chunks = []
            current_chunk = []
            current_length = 0

            for p in paths:
                cmd_part = f"printf '@@@PATH:{p}@@@\\n'; ls -1 {p} 2>/dev/null"
                part_length = len(cmd_part) + 2  # +2 für "; "
                if current_length + part_length > MAX_CMD_LENGTH and current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = [p]
                    current_length = part_length
                else:
                    current_chunk.append(p)
                    current_length += part_length

            if current_chunk:
                chunks.append(current_chunk)

            self.logger.log_action(
                "Volume-Erkennung: Pfad-Häppchen gebildet",
                f"{len(chunks)} Häppchen für {len(paths)} Pfade",
            )

            # ─── Jedes Häppchen per SSH abfragen ───
            all_output = []

            for chunk_idx, chunk_paths in enumerate(chunks, start=1):
                # ⭐ Wichtig: `; true` am Ende → Exit-Code immer 0,
                # auch wenn einzelne `ls` fehlschlagen (z.B. /volume4
                # existiert nicht).
                ls_commands = "; ".join(
                    f"printf '@@@PATH:{p}@@@\\n'; ls -1 {p} 2>/dev/null"
                    for p in chunk_paths
                ) + "; true"

                self.logger.log_action(
                    f"Volume-Erkennung: Häppchen {chunk_idx}/{len(chunks)}",
                    f"Pfade: {chunk_paths}, Befehl-Länge: {len(ls_commands)}",
                )

                cmd = [
                    "ssh",
                    "-i", expanded_key,
                    "-o", "ConnectTimeout=5",
                    "-o", "BatchMode=yes",
                    "-o", "StrictHostKeyChecking=no",
                    f"{nas_user}@{nas_ip}",
                    ls_commands,
                ]

                try:
                    result = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        timeout=15,
                    )

                    # ⭐ Ausgabe verwenden, WENN Daten vorhanden sind —
                    # unabhängig vom Exit-Code (weil `; true` eigentlich
                    # für rc=0 sorgt, aber wir sind defensiv).
                    if result.stdout and result.stdout.strip():
                        all_output.append(result.stdout)
                        self.logger.log_action(
                            f"Häppchen {chunk_idx}/{len(chunks)} OK",
                            f"rc={result.returncode}, "
                            f"stdout-Länge: {len(result.stdout)}",
                        )
                    else:
                        self.logger.log_action(
                            f"Häppchen {chunk_idx}/{len(chunks)}: "
                            f"keine Ausgabe",
                            f"rc={result.returncode}, "
                            f"stderr='{result.stderr.strip()[:150]}'",
                        )
                except subprocess.TimeoutExpired:
                    self.logger.log_error(
                        f"Häppchen {chunk_idx} Timeout", "SSH >15s"
                    )
                except Exception as e:
                    self.logger.log_error(
                        f"Häppchen {chunk_idx} Fehler", str(e), e
                    )

            # ─── Ausgabe parsen ───
            if all_output:
                output = "\n".join(all_output)
                volumes = self._parse_volume_ls_output(output)

                if volumes:
                    self.logger.log_action(
                        "Volume-Erkennung erfolgreich (Hersteller-Pfade)",
                        f"{len(volumes)} Volumes: "
                        f"{', '.join(volumes[:5])}"
                        + (
                            f" ... (+{len(volumes)-5})"
                            if len(volumes) > 5
                            else ""
                        ),
                    )
                    return volumes
                else:
                    self.logger.log_action(
                        "Volume-Erkennung: Keine Volumes in Hersteller-Pfaden",
                    )
            else:
                self.logger.log_action(
                    "Volume-Erkennung: Kein Häppchen lieferte Ausgabe",
                )

        # ═══════════════════════════════════════════════════════════════
        # Methode 2: Fallback via smbclient
        # ═══════════════════════════════════════════════════════════════
        self.logger.log_action("Volume-Erkennung: Fallback smbclient")

        cmd = [
            "ssh",
            "-i", expanded_key,
            "-o", "ConnectTimeout=5",
            "-o", "BatchMode=yes",
            "-o", "StrictHostKeyChecking=no",
            f"{nas_user}@{nas_ip}",
            "smbclient -L localhost -N 2>/dev/null | "
            "grep -E '^[A-Za-z0-9_]+[[:space:]]+Disk' | awk '{print $1}'",
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=15,
            )

            if result.returncode == 0 and result.stdout.strip():
                volumes = [
                    line.strip()
                    for line in result.stdout.splitlines()
                    if line.strip()
                ]
                if volumes:
                    self.logger.log_action(
                        "Volume-Erkennung erfolgreich (smbclient)",
                        f"{len(volumes)} Volumes",
                    )
                    return volumes
        except Exception as e:
            self.logger.log_error("Volume-Erkennung smbclient Fehler", str(e), e)

        # ═══════════════════════════════════════════════════════════════
        # Keine Volumes gefunden
        # ═══════════════════════════════════════════════════════════════
        self.logger.log_action("Volume-Erkennung: Keine Volumes gefunden")
        return []

    def _parse_volume_ls_output(self, output: str) -> list:
        """
        Parst die Ausgabe von `ls -1 <path>` für mehrere Pfade.

        Format:
            @@@PATH:/volume1@@@
            Dokumente
            Bilder
            @@@PATH:/volume2@@@
            Backup
            ...

        Filtert System-Dateien und -Ordner heraus.

        Rückgabe:
            Liste der Volume-Namen (ohne Duplikate).
        """
        volumes = []
        current_path = None

        # System-Dateien und -Ordner die ignoriert werden
        skip_prefixes = ("@", ".")
        skip_exact = {
            "aquota.group",
            "aquota.user",
            "synoquota.db",
            "lost+found",
            "#recycle",
        }
        skip_contains = ("quota",)   # .group, .user, .db mit "quota" im Namen

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # ⭐ @@@ statt ### (Shell-Kommentarzeichen!)
            if line.startswith("@@@PATH:") and line.endswith("@@@"):
                current_path = line[8:-3]
                continue

            if not current_path:
                continue

            # ─── Filter 1: beginnt mit @ oder . ───
            if line.startswith(skip_prefixes):
                continue

            # ─── Filter 2: exakte System-Dateien ───
            if line in skip_exact:
                continue

            # ─── Filter 3: enthält "quota" (aquota, synoquota, ...) ───
            line_lower = line.lower()
            if any(pat in line_lower for pat in skip_contains):
                continue

            # ─── Gültiges Volume ───
            if line not in volumes:
                volumes.append(line)

        return volumes

    def _get_vendor_shutdown_commands(self) -> list:
        """
        Gibt die Shutdown-Befehle für den aktuellen Hersteller zurück.

        Sonderfall `custom`: Der User hat einen eigenen Befehl
        (oder mehrere, durch `;` getrennt) eingetragen.
        """
        try:
            vendor_key = self.config.get("nas_vendor", "linux_generic")

            # ═══════════════════════════════════════════════════════
            # Sonderfall: Benutzerdefiniert
            # ═══════════════════════════════════════════════════════
            if vendor_key == "custom":
                custom_cmd = self.config.get(
                    "custom_shutdown_command", "sudo shutdown -h now"
                )
                # Mehrere Befehle durch `;` trennen
                commands = [
                    c.strip() for c in custom_cmd.split(";") if c.strip()
                ]
                if commands:
                    self.logger.log_action(
                        "Benutzerdefinierter Shutdown-Befehl",
                        f"{len(commands)} Befehl(e): {commands}",
                    )
                    return commands
                else:
                    # Fallback auf Default
                    self.logger.log_action(
                        "Benutzerdefinierter Befehl leer, "
                        "verwende Standard",
                    )
                    return ["sudo shutdown -h now"]

            # ═══════════════════════════════════════════════════════
            # Standard-Hersteller
            # ═══════════════════════════════════════════════════════
            vendor = NasVendor.get_vendor(vendor_key)

            if vendor and vendor.get("shutdown_commands"):
                return vendor["shutdown_commands"]

            # Fallback: Generische Linux-Befehle
            self.logger.log_action(
                "Kein Hersteller-Shutdown gefunden, verwende generische Linux-Befehle",
                f"Hersteller: {vendor_key}",
            )
            generic = NasVendor.get_vendor("linux_generic")
            return generic["shutdown_commands"]
        except Exception as e:
            self.logger.log_error(
                "Fehler beim Laden der Shutdown-Befehle", str(e), e
            )
            # Absolute Notfall-Liste
            return [
                "sudo shutdown -h now",
                "sudo poweroff",
            ]

    def _try_shutdown_commands(self) -> tuple:
        """
        Versucht die Shutdown-Befehle des gewählten Herstellers
        nacheinander, bis einer funktioniert.

        Hersteller Erster Befehl Falls der fehlschlägt
        Synology sudo shutdown -h now sudo synopoweroff, sudo poweroff
        QNAP sudo shutdown -h now sudo poweroff, poweroff
        TrueNAS sudo shutdown -h now sudo poweroff, /sbin/shutdown
        Unraid powerdown sudo powerdown, sudo shutdown
        Windows shutdown /s /t 0 powershell Stop-Computer

        Rückgabe:
            (success: bool, used_command: str)
        """
        nas_user = self.config.get("nas_user")
        nas_ip = self.config.get("nas_ip")
        ssh_key = self.config.get("ssh_key_path")

        commands = self._get_vendor_shutdown_commands()

        self.logger.log_action(
            "Shutdown-Befehlskette gestartet",
            f"Anzahl: {len(commands)}",
        )

        for idx, cmd_str in enumerate(commands, start=1):
            self.logger.log_action(
                f"Shutdown-Versuch {idx}/{len(commands)}",
                cmd_str,
            )

            # SSH-Verbindung mit Timeout aufbauen und Befehl senden
            cmd = [
                "ssh",
                "-i", ssh_key,
                "-o", "ConnectTimeout=5",
                "-o", "BatchMode=yes",
                "-o", "StrictHostKeyChecking=no",
                f"{nas_user}@{nas_ip}",
                cmd_str,
            ]

            try:
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.PIPE,
                )

                # 3 Sekunden warten — dann Status prüfen
                try:
                    _, stderr_output = process.communicate(timeout=3)
                    returncode = process.returncode
                except subprocess.TimeoutExpired:
                    # Prozess läuft noch → wahrscheinlich erfolgreich
                    # (weil NAS bereits herunterfährt, SSH-Verbindung bricht ab)
                    self.logger.log_action(
                        f"Shutdown-Versuch {idx} läuft noch – "
                        "interpretiere als Erfolg",
                        cmd_str,
                    )
                    return (True, cmd_str)

                # Prozess beendet → Rückgabewert prüfen
                if returncode == 0:
                    self.logger.log_action(
                        f"Shutdown-Versuch {idx} erfolgreich",
                        cmd_str,
                    )
                    return (True, cmd_str)
                else:
                    error_text = (
                        stderr_output.decode("utf-8", errors="replace")[:200]
                        if stderr_output else ""
                    )
                    self.logger.log_action(
                        f"Shutdown-Versuch {idx} fehlgeschlagen",
                        f"rc={returncode}, err={error_text}",
                    )
                    # Nächsten Befehl versuchen
                    continue

            except Exception as e:
                self.logger.log_error(
                    f"Shutdown-Versuch {idx} Ausnahme",
                    f"{cmd_str}: {e}",
                    e,
                )
                continue

        # Alle Befehle fehlgeschlagen
        self.logger.log_error(
            "Alle Shutdown-Befehle fehlgeschlagen",
            f"Hersteller: {self.config.get('nas_vendor')}, "
            f"Versuche: {len(commands)}",
        )
        return (False, "")

    def shutdownNAS(self):
        """
        Fährt den NAS-Server herunter.
        Nutzt die hersteller-spezifische Shutdown-Befehlskette.

        Gibt True zurück, wenn ein Befehl erfolgreich gesendet wurde.
        """
        try:
            nas_ip = self.config.get("nas_ip")
            ssh_key = self.config.get("ssh_key_path")

            self.logger.log_action(
                "Starte NAS-Shutdown",
                f"IP: {nas_ip}, Hersteller: {self.config.get('nas_vendor')}",
            )
            self.status_label.setText("Sende Shutdown-Befehl an NAS...")
            QApplication.processEvents()

            # SSH-Key zum Agent hinzufügen (einmalig)
            try:
                expanded_key = os.path.expanduser(ssh_key)
                self.logger.log_action("Lade SSH-Key in den Agent...")
                subprocess.run(
                    ["ssh-add", expanded_key],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
            except Exception as e:
                self.logger.log_error(
                    "Fehler beim Laden des SSH-Keys", str(e), e
                )

            # Befehlskette durchlaufen
            success, used_command = self._try_shutdown_commands()

            if success:
                self.logger.log_action(
                    "NAS-Shutdown erfolgreich",
                    f"Verwendeter Befehl: {used_command}",
                )
                self.status_label.setText(tr("status_shutdown_cmd"))
                return True
            else:
                self.logger.log_error(
                    "NAS-Shutdown komplett fehlgeschlagen",
                    "Kein Befehl hat funktioniert",
                )
                self.status_label.setText(
                    "❌ NAS-Shutdown fehlgeschlagen – siehe Log"
                )
                return False

        except Exception as e:
            self.logger.log_error("shutdownNAS Fehler", str(e), e)
            self.status_label.setText("❌ Fehler beim Senden des Shutdown-Befehls")
            return False

    def shutdownMac(self):
        """Fährt den lokalen Mac herunter.

        Startet einen 2-Sekunden-Timer, damit die GUI noch aktualisiert
        werden kann, und ruft dann die eigentliche Shutdown-Logik auf.
        """
        try:
            self.logger.log_action("Starte Mac-Shutdown")
            self.status_label.setText("Fahre Mac herunter...")
            QApplication.processEvents()
            # Warte 2 Sekunden, damit GUI aktualisiert wird,
            # dann eigentliche Shutdown-Logik ausführen
            QTimer.singleShot(2000, self._execute_mac_shutdown)
        except Exception as e:
            self.logger.log_error("shutdownMac Fehler", str(e), e)

    def _execute_mac_shutdown(self):
        """Führt den tatsächlichen Mac-Shutdown aus – mehrstufiger Ansatz.

        Versuch 1: sudo -n (NOPASSWD-Regel) – ohne Passwort
        Versuch 2: Keychain-Passwort + sudo -S
        Versuch 3: Fallback – bisheriges Verhalten
        """
        # ═══════════════════════════════════════════════════
        # Versuch 1: sudo -n (NOPASSWD-Regel, keine Eingabe)
        # ═══════════════════════════════════════════════════
        try:
            result = subprocess.run(
                ["sudo", "-n", "shutdown", "-h", "now"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0:
                self.logger.log_action(
                    "Mac-Shutdown via sudo -n erfolgreich"
                )
                return
            else:
                self.logger.log_action(
                    "sudo -n fehlgeschlagen – versuche Keychain-Passwort",
                    f"stderr: {result.stderr.strip()[:200]}",
                )
        except Exception as e:
            self.logger.log_error(
                "sudo -n Aufruf fehlgeschlagen", str(e), e
            )

        # ═══════════════════════════════════════════════════
        # Versuch 2: Passwort aus Keychain verwenden
        # ═══════════════════════════════════════════════════
        keychain_pw = MacKeychainHelper.get_password()
        if keychain_pw:
            try:
                # -S = Passwort von stdin lesen
                # -k = sudo-Cache löschen (erzwingt neue Auth)
                result = subprocess.run(
                    ["sudo", "-S", "-k", "shutdown", "-h", "now"],
                    input=f"{keychain_pw}\n",
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                if result.returncode == 0:
                    self.logger.log_action(
                        "Mac-Shutdown via Keychain-Passwort erfolgreich"
                    )
                    return
                else:
                    # Keychain-Passwort falsch → aus Keychain löschen,
                    # damit beim nächsten Timer neu gefragt wird
                    self.logger.log_error(
                        "Keychain-Passwort abgelehnt",
                        f"stderr: {result.stderr.strip()[:200]}",
                    )
                    MacKeychainHelper.delete_password()
                    self.logger.log_action(
                        "Ungültiges Keychain-Passwort gelöscht – "
                        "wird beim nächsten Timer neu abgefragt"
                    )
            except Exception as e:
                self.logger.log_error(
                    "Keychain-Shutdown fehlgeschlagen", str(e), e
                )

        # ═══════════════════════════════════════════════════
        # Versuch 3: Bisheriges Verhalten (Fallback, ohne Passwort)
        # ═══════════════════════════════════════════════════
        try:
            self.logger.log_action(
                "Mac-Shutdown: Fallback (sudo ohne Passwort)"
            )
            subprocess.run(
                ["sudo", "shutdown", "-h", "now"],
                capture_output=True,
                text=True,
                timeout=10,
            )
        except Exception as e:
            self.logger.log_error(
                "Mac-Shutdown Fallback fehlgeschlagen", str(e), e
            )

    """Notlösung wenn NAS Shutdown nicht mehr funktioniert:
        falls einmal der ssh key nicht mehr akzeptiert wird hilf u.U. folgendes im Terminal:
        # 1. Prüfen ob SSH-Key existiert und korrekte Berechtigungen hat
        ls -la ~/.ssh/id_rsa
        # Sollte sein: -rw------- (600)

        # 2. Prüfen ob der Key im SSH-Agent geladen ist
        # Sollte den Fingerprint des Keys anzeigen
        ssh-add -l

        # falls nicht
        # 3. SSH-Key zum SSH-Agent hinzufügen
        ssh-add ~/.ssh/id_rsa

        # 4. Prüfen ob der Key jetzt geladen ist
        ssh-add -l
        # Sollte jetzt den Fingerprint des Keys anzeigen
    """

    # =====================
    # TASTATUR-HANDLING
    # =====================

    def keyPressEvent(self, event):
        """Behandelt Tastaturengaben."""
        if event.key() == Qt.Key_Escape:
            self.logger.log_action("ESC gedrückt - App wird geschlossen")
            self.status_label.setText(tr("status_esc"))
            QTimer.singleShot(500, self.close)
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            focused_widget = self.focusWidget()
            if isinstance(focused_widget, QPushButton):
                focused_widget.click()
        else:
            super().keyPressEvent(event)

    def check_for_updates_auto(self):
        """Automatische Versionsprüfung beim Start (max. 1× pro 24 Stunden)."""
        try:
            # Prüfen ob heute schon erfolgreich geprüft wurde
            should_check = True
            try:
                if self.last_check_file.exists():
                    last = float(self.last_check_file.read_text().strip())
                    if time.time() - last < 86400:  # 24 h
                        should_check = False
            except Exception:
                should_check = True

            if not should_check:
                return

            # Prüfung durchführen
            result = VersionManager.check_for_updates(
                self, show_no_update=False
            )

            # Nur bei erfolgreicher Prüfung Zeitstempel setzen
            # None = Fehler → beim nächsten Start erneut versuchen
            if result is not None:
                try:
                    self.last_check_file.parent.mkdir(
                        parents=True, exist_ok=True
                    )
                    self.last_check_file.write_text(str(time.time()))
                except Exception as e:
                    self.logger.log_error(
                        "Update-Check Zeitstempel schreiben fehlgeschlagen",
                        str(e),
                        e,
                    )
        except Exception as e:
            print(f"Fehler bei automatischer Versionsprüfung: {e}")

    def _sigterm_handler(signum, frame):
        """Wird aufgerufen, wenn macOS die App beendet (z.B. beim Shutdown)."""
        try:
            if hasattr(self, "scheduled_caffeinate_proc") and self.scheduled_caffeinate_proc:
                self.scheduled_caffeinate_proc.terminate()
            if hasattr(self, "scheduled_timer") and self.scheduled_timer.isActive():
                self.scheduled_timer.stop()
            if hasattr(self, "auto_timer") and self.auto_timer.isActive():
                self.auto_timer.stop()
        except Exception:
            pass
        sys.exit(0)

    def closeEvent(self, event):
        """Wird beim Schließen der App aufgerufen.

        Wenn ein Countdown aktiv ist, wird der User gefragt, ob er
        wirklich schließen will.
        """
        try:
            if getattr(self, "scheduled_active", False) and self.scheduled_target_time:
                from datetime import datetime
                remaining_seconds = int(
                    (self.scheduled_target_time - datetime.now()).total_seconds()
                )
                duration_str = self._format_duration(remaining_seconds)

                target_names = {
                    "both": tr("sched_target_both"),
                    "nas_only": tr("sched_target_nas"),
                    "mac_only": tr("sched_target_mac"),
                    "coffee": tr("sched_target_coffee"),
                }
                target_name = target_names.get(self.scheduled_target_action, "?")
                end_time_str = self.scheduled_target_time.strftime(
                    "%d.%m.%Y %H:%M:%S"
                )

                msg = QMessageBox(self)
                msg.setWindowTitle(tr("close_blocked_title"))
                msg.setIcon(QMessageBox.Warning)
                msg.setText(
                    tr("close_blocked_text").format(
                        target_name, duration_str, end_time_str
                    )
                )
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg.setDefaultButton(QMessageBox.No)
                msg.button(QMessageBox.Yes).setText(tr("close_blocked_yes"))
                msg.button(QMessageBox.No).setText(tr("close_blocked_no"))

                # Dialog-Breite auf maximal 90% der Bildschirmbreite begrenzen
                try:
                    screen_w = QApplication.primaryScreen().availableGeometry().width()
                    max_box_w = int(screen_w * 0.9)
                    max_btn_w = max(160, min(280, max_box_w // 2 - 30))
                except Exception:
                    max_box_w = 520
                    max_btn_w = 200

                msg.setMinimumWidth(min(520, max_box_w))
                for btn in msg.buttons():
                    btn.setMinimumWidth(max_btn_w)
                    btn.setMinimumHeight(38)

                reply = msg.exec_()
                if reply != QMessageBox.Yes:
                    event.ignore()
                    self.logger.log_action(tr("close_blocked_log_aborted"))
                    return

                self.logger.log_action(tr("close_blocked_log_discarded"))
                self.scheduled_timer.stop()
                self._stop_scheduled_caffeinate()
                self.scheduled_active = False

            LANG.remove_listener(self.update_ui_language)

            if hasattr(self, "scheduled_timer") and self.scheduled_timer.isActive():
                self.scheduled_timer.stop()
            self._stop_scheduled_caffeinate()

            if hasattr(self, "auto_timer") and self.auto_timer.isActive():
                self.auto_timer.stop()

            if hasattr(self, "wait_thread") and self.wait_thread.is_alive():
                self.wait_thread.join(timeout=1)

            self.logger.log("=== SYNASPY BEENDET ===", "STOP")
            self.logger.flush()
            event.accept()
        except Exception as e:
            try:
                self.logger.log_error("Fehler im closeEvent", str(e), e)
            except Exception:
                pass
            event.accept()

# ======================
# HAUPTFUNKTION
# ======================


def main():
    """Hauptfunktion der Anwendung."""
    app = QApplication(sys.argv)

    # App-Icon setzen - DIREKT aus dem aktuellen Verzeichnis
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "AnyNasPy.png")

    if os.path.exists(icon_path):
        app_icon = QIcon(icon_path)
        app.setWindowIcon(app_icon)

    app.setStyle("Fusion")
    window = AnyNasPy()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
