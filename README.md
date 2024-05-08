# voiceoperation
Record your statement and it will be translated into an operation with classified labels.
Every model is using pre-trained data out-of-the-box.

ML Models:

Speech-to-Text -> openai/whisper-large-v3
Named Entity Recognition -> GLiNER
Translation (only valid for Portuguese-English) -> unicamp-dl/translation-pt-en-t5

After setting up your python virtual environment, you'll find all the required libraries in requirements.txt.

Future releases:
  º setup the entities you wish to classify your text with
  º allow more language translations
