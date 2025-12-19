import streamlit as st
from openai import OpenAI, APIConnectionError, APITimeoutError, AuthenticationError, BadRequestError, ConflictError, InternalServerError, NotFoundError, PermissionDeniedError, RateLimitError, UnprocessableEntityError
import json
from datetime import datetime

with open('config.json', 'r') as f:
    config = json.load(f)

st.title("Medizinische Transkript-Analyzer")

text_input = st.text_area("Fügen Sie hier das medizinische Transkript ein:", height=300)

client = OpenAI(
    api_key = st.secrets["API_KEY"],
    base_url="https://router.requesty.ai/v1"
)

if st.button("Analysieren"):
    if len(text_input.strip()) > 0:
        with st.spinner("Analyse läuft..."):
            try:
                response = client.chat.completions.create(
                model=config["model_catalogue"][config["selected_model"]],
                messages=[
                    {"role": "system", "content": config["prompts"]["prompt_1"]},
                    {"role": "user", "content": config["prompts"]["prompt_2"].format(text=text_input)},
                    {"role": "user", "content": config["prompts"]["prompt_3"]},
                    {"role": "user", "content": config["prompts"]["prompt_4"]}
                ]
                )
            
                result = response.choices[0].message.content
            except APIConnectionError as e:
                st.markdown(":red[Verbindungsfehler: Bitte überprüfen Sie Ihre Netzwerkverbindung.]") 
                st.stop()   
            except APITimeoutError as e:
                st.markdown(":red[Zeitüberschreitung der Anfrage: Der Server hat nicht rechtzeitig geantwortet.]")
                st.stop()
            except AuthenticationError as e:
                st.markdown(":red[Authentifizierungsfehler: Bitte überprüfen Sie Ihren API-Schlüssel.]")
                st.stop()
            except BadRequestError as e:
                st.markdown(":red[Fehlerhafte Anfrage: Bitte überprüfen Sie die übermittelten Daten.]")
                st.stop()
            except ConflictError as e:
                st.markdown(":red[Konfliktfehler: Es besteht ein Konflikt mit dem aktuellen Zustand der Ressource.]")
                st.stop()
            except InternalServerError as e:
                st.markdown(":red[Interner Serverfehler: Ein Fehler ist auf dem Server aufgetreten.]")
                st.stop()
            except NotFoundError as e:
                st.markdown(":red[Nicht gefunden: Die angeforderte Ressource wurde nicht gefunden.]")
                st.stop()
            except PermissionDeniedError as e:
                st.markdown(":red[Authentifizierungsfehler: Bitte überprüfen Sie Ihren API-Schlüssel.]")
                st.stop()
            except RateLimitError as e:
                st.markdown(":red[Rate-Limit-Überschreitung: Sie haben die zulässige Anzahl von Anfragen überschritten.]")  
                st.stop()
            except UnprocessableEntityError as e:
                st.markdown(":red[Nicht verarbeitbare Entität: Die Anfrage konnte aufgrund semantischer Fehler nicht verarbeitet werden.]")
                st.stop()
        st.success("Analyse abgeschlossen!")

        meta_data = {
            "date": datetime.now().isoformat(),
            "transcript": text_input.encode().decode("unicode_escape"),
            "prompts": config["prompts"],
            "analysis": result,
            "model": response.model,
            "prompt_tokens": response.usage.prompt_tokens,
            "total_tokens": response.usage.total_tokens,
            "cost": response.usage.cost
        }

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"meta_data/transcript_analysis_{timestamp}.json", "w") as outfile:
            json.dump(meta_data, outfile, indent=4)

        st.write(f"{result}")

    else:
        st.markdown(":red[Bitte geben Sie ein Transkript zur Analyse ein.]")
