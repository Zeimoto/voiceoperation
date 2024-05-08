from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch
from resources import set_start, audit_elapsedtime 

#Speech to text transcription model

def init_model_trans ():
    print("Initiating transcription model...")
    start = set_start()

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-large-v3"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        return_timestamps=True,
        torch_dtype=torch_dtype,
        device=device,
    )
    print(f'Init model successful')
    audit_elapsedtime(function="Init transc model", start=start)
    return pipe

def transcribe (audio_sample: bytes, pipe) -> str:
    print("Initiating transcription...")
    start = set_start()
    # dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
    # sample = dataset[0]["audio"]
    
    #result = pipe(audio_sample)
    result = pipe(audio_sample)

    audit_elapsedtime(function="Transcription", start=start)
    print("transcription result",result)

    #st.write('trancription: ', result["text"])
    return result["text"]

# def translate (audio_sample: bytes, pipe) -> str:
#     print("Initiating Translation...")
#     start = set_start()
#     # dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
#     # sample = dataset[0]["audio"]
    
#     #result = pipe(audio_sample)
#     result = pipe(audio_sample, generate_kwargs={"task": "translate"})

#     audit_elapsedtime(function="Translation", start=start)
#     print("Translation result",result)

#     #st.write('trancription: ', result["text"])
#     return result["text"]