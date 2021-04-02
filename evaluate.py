import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
model = tf.keras.models.load_model('isspam/model.h5')

# Test Score: 0.48393920063972473
# Test Accuracy: 0.8384279608726501

# Initiate Hyperparameters
vocab_size = 1000
embedding_dim = 16
trunc_type='post'
oov = "<ASW>"

# Test

# Use the model to predict whether a message is spam
text_messages = ['Nasabah BRI Yth !!! Nomor Rek BRI Anda Mendapa DANA GIRO Rp.37.000.000', 'Halo gan, apakabar? hari ini bisa ke taman nggak', 'PROMO!! Kamu dapat 200 juta rupiah. Buruan kunjungi link kami di www.bandar.com', 'Konsumen yth, Anda dapat 125jt dari program s.h.o.p.e.3 thn,.2021 kode pin anda (25477BLW) Info klik: www.program1212.com', 'Selamat Kpd Anda Telah Mendapatkan Cek Tunai 175juta Dari ShopeCenter3.3 2021 PIN ID ( 25F4777 ) Chat WhatsApp https:/wa.me/6285283194456', 'ASS,, Punya Masala 3konomi Kmi Ml4yni  Kredit Rakyat  Mulai Pnj4m4n 5jt-500jt Wa;082259633599', 'Gampang Cari Uang Hanya Dengan D3pos1t 10rbu Bisa Dpt J4ckp0t Sampai Jut4an Hanya Di Situs QQ T3rb4ik Di http://bit.ly/cantikqq']

text_messages = ['Gampang Cari Uang Hanya Dengan D3pos1t 10rbu Bisa Dpt J4ckp0t Sampai Jut4an Hanya Di Situs QQ T3rb4ik Di http://bit.ly/cantikqq']

print(text_messages) 

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov)
tokenizer.fit_on_texts(text_messages)
word_index = tokenizer.word_index

# Create the sequences
padding_type = 'post'
max_length = 200
sample_sequences = tokenizer.texts_to_sequences(text_messages)
fakes_padded = pad_sequences(sample_sequences, padding=padding_type, maxlen=max_length)           

classes = model.predict(fakes_padded)

# The closer the class is to 1, the more likely that the message is spam
for x in range(len(text_messages)):
  print(text_messages[x])
  print(classes[x])
  print('\n')