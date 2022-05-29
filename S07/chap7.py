import tensorflow as tf

def load_dataset():
    (trX,trY),(teX,teY) = tf.keras.datasets.imdb.load_data(num_words=20000)

    trX = tf.keras.preprocessing.sequence.pad_sequences(trX,maxlen=100,padding='pre')
    teX = tf.keras.preprocessing.sequence.pad_sequences(teX, maxlen=100, padding='pre')

    return trX, trY, teX, teY

def define_model():
    model = tf.keras.models.Sequential()

    model.add(tf.keras.layers.Embedding(20000,128))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32,return_sequences=True)))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)))
    model.add(tf.keras.layers.Dense(1,activation='sigmoid'))
    return model

trX, trY, teX, teY = load_dataset()
model = define_model()
opt = tf.keras.optimizers.Adam(0.0001)
model.compile(optimizer=opt,loss='binary_crossentropy',metrics=['accuracy'])
model.fit(trX,trY,epochs=5,batch_size=64,validation_data=(teX,teY))
sloss,acc = model.evaluate(teX,teY)
print(' > %.3f' % (acc * 100.0))


