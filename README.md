# Medizinischer Transkript-Analyzer

Ein Streamlit-basiertes Tool zur automatisierten Analyse von medizinischen Transkripten mit Hilfe eines Large Language Models (LLM).

## Features

- 📝 Einfache Benutzeroberfläche zum Hochladen von medizinischen Transkripten
- 🤖 KI-gestützte Analyse durch LLM (OpenAI kompatibel)
- 💾 Automatische Speicherung der Analyseergebnisse in JSON-Format
- ⚙️ Konfigurierbare Prompts und Modellauswahl
- 🛡️ Umfangreiche Fehlerbehandlung mit aussagekräftigen Fehlermeldungen
- 🌐 Unterstützung für externe API-Router

## Installation

### Voraussetzungen

- Python 3.7+
- pip (Python Package Manager)

### Schritt-für-Schritt-Anleitung

1. **Repository klonen oder Ordner herunterladen**
   ```bash
   cd "Medizinischer Transkript-Analyzer"
   ```

2. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

3. **Secrets konfigurieren**
   - Erstelle einen `.streamlit/secrets.toml` Ordner im Projektverzeichnis
   - Füge deinen API-Schlüssel hinzu:
   ```toml
   API_KEY = "dein-api-key-hier"
   ```

4. **Anwendung starten**
   ```bash
   streamlit run app.py
   ```

Die Anwendung öffnet sich dann im Browser unter `http://localhost:8501`

## Projektstruktur

```
Medizinischer Transkript-Analyzer/
├── app.py                          # Hauptanwendung
├── config.json                     # Konfiguration für Modelle und Prompts
├── README.md                       # Diese Datei
├── requirements.txt                # Python-Abhängigkeiten
└── meta_data/
    └── (generierte Analyseergebnisse)
```

## Konfiguration

### config.json

Die `config.json` Datei enthält:
- **model_catalogue**: Verfügbare LLM-Modelle
- **selected_model**: Das aktuell verwendete Modell
- **prompts**: Prompts, die dem Modell übergeben werden

Beispiel:
```json
{
  "model_catalogue": {
    "haiku": "policy/haiku-fallbacks",
    "gemini-fast": "policy/gemini-fast"
  },
  "selected_model": "haiku",
  "prompts": {
    "prompt_1": "Du bist ein medizinischer Analyst...",
    "prompt_2": "Bitte analysiere folgendes Transkript: {text}",
    "prompt_3": "Fasse die wichtigsten Erkenntnisse zusammen"
  }
}
```

## Verwendung

1. **Transkript eingeben**
   - Kopiere das medizinische Transkript in das Textfeld
   - Mindestlänge: 1 Zeichen (nach Whitespace-Trimmen)

2. **Analyse starten**
   - Klicke auf den Button "Analysieren"
   - Die Anwendung zeigt einen Ladeindikator während der Verarbeitung

3. **Ergebnisse anzeigen**
   - Die LLM-Analyse wird in der UI angezeigt
   - Automatisch wird ein JSON-Export erstellt und gespeichert

## Technologien

- **Streamlit**: Web-Framework für Python
- **OpenAI Python Client**: API-Integration
- **JSON**: Datenspeicherung
- **datetime**: Zeitstempel-Management

---

**Version**: 1.0  
**Letztes Update**: Dezember 2025
