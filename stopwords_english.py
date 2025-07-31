# importar la libreria NLTK
import nltk

# desde nltk descargar el paquete stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

lista_stopwords_english = stopwords.words('english')

# imprimir la lista de stopwords
print(lista_stopwords_english)