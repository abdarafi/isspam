from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Message(BaseModel):
    message: str

app = FastAPI()
model = tf.keras.models.load_model('isspam/model.h5')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*","*"],
    allow_credentials=True,
    allow_methods=["*","*"],
    allow_headers=["*","*"],
)

def tokenize_message(message):
    tokenizer = Tokenizer(num_words=1000, oov_token="<ASW>")
    tokenizer.fit_on_texts(message)
    word_index = tokenizer.word_index
    sample_sequences = tokenizer.texts_to_sequences(message)
    fakes_padded = pad_sequences(sample_sequences, padding="post", maxlen=200)
    return fakes_padded

def filter_message(message):
    filtered = []
    filtered.insert(0, message.replace('\n', ' ').replace('\r', ''))
    return filtered

@app.post("/api/check")
async def check_message(body: Message):
    if len(body.message) > 1000:
        raise HTTPException(status_code=400, detail="Only support up to 1000 chars")
    message = body.message
    filtered_message = filter_message(message)
    tokenized_message = tokenize_message(filtered_message)
    classes = model.predict(tokenized_message)
    result = classes.tolist()[0]
    max_value = max(result)
    max_index = result.index(max_value)    
    if max_index == 0:
        return {"result": "normal"}
    elif max_index == 1:
        return {"result": "spam"}
    elif max_index == 2:
        return {"result": "promotion"}
    else:
        raise HTTPException(status_code=400, detail="Something bad happened")