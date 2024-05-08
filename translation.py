from transformers import MarianMTModel, MarianTokenizer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from resources import set_start, audit_elapsedtime

def translate(text_to_translate: str) -> str:
    
    start = set_start()
    print("Initiating translation model...")
    text_size = len(text_to_translate)*2
    tokenizer = AutoTokenizer.from_pretrained("unicamp-dl/translation-pt-en-t5")
    model = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-pt-en-t5")
    pten_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)
    translated_text = pten_pipeline(text_to_translate, max_new_tokens= text_size)

    audit_elapsedtime(function="Finished translation", start=start)
    print("Translated text:", translated_text)
    return translated_text
