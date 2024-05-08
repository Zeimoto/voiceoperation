from gliner import GLiNER
from resources import set_start, audit_elapsedtime, entity_labels

#Named-Entity Recognition model

def init_model_ner():
    print("Initiating NER model...")
    start = set_start()
    model = GLiNER.from_pretrained("urchade/gliner_multi")
    audit_elapsedtime(function="Initiating NER model", start=start)
    return model

def get_entity_labels(model: GLiNER, text: str): #-> Lead_labels:
    print("Initiating entity recognition...")
    start = set_start()
    
    labels = entity_labels
    entities = model.predict_entities(text, labels)
    audit_elapsedtime(function="Retreiving entity labels from text", start=start)

    for entity in entities:
        print(entity["text"], "=>", entity["label"])

    return entities