import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

class Text:
    def __init__(self):
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.dtype = torch.float64 if torch.cuda.is_available() else torch.float32
        self.model_id = "openai/whisper-small"
        self.max_new_tokens = 128
        self.chunk_length_s = 30
        self.batch_size = 16



    def ConvertIntoText(self,filename,language = "en"):
        model = AutoModelForSpeechSeq2Seq.from_pretrained( self.model_id,torch_dtype = self.dtype, low_cpu_mem_usage = False,use_safetensors = True)
        tokenizer = AutoProcessor.from_pretrained(self.model_id)
        Pipeline = pipeline(task="automatic-speech-recognition",model = model, tokenizer=tokenizer.tokenizer,
               feature_extractor=tokenizer.feature_extractor, max_new_tokens = self.max_new_tokens, 
               chunk_length_s = self.chunk_length_s ,
                batch_size = self.batch_size, 
               return_timestamps = False, 
               torch_dtype = torch.types,
               device = self.device)
        text = Pipeline(filename, generate_kwargs = {"language": language})

        return text["text"]


    

if __name__ == "__main__":
    filename = "temp1.mp3" #input("Enter File Name : ")
    result = Text().ConvertIntoText(filename = filename)
    print(result)