from sklearn.feature_extraction.text import CountVectorizer

'''
Textdatei lesen
Aufgabe Die Datei textdatei.txt lesen und den Text der Variablen text zuweisen.
'''

# Textdatei lesen
with open('textdatei.txt', 'r', encoding='utf-8') as file:
    text = file.read()

#CountVectorizer initialisieren
vectorizer = CountVectorizer()

# Bag-of-Words-Modell erstellen
X = vectorizer.fit_transform([text])

# Vokabelliste in eine Liste umwandeln
vocab_list = list(vectorizer.vocabulary_)

# Die Sparse Matrix in ein dichte Array umwandeln (für einfachere Darstellung)
sparse_matrix = X.toarray()

# Das resultierende Bag-of-Words-Modell anzeigen
print("Vokabular:", vectorizer.vocabulary_)
print("Bag-of-Words (Sparse Matrix):\n", X.toarray())
print("Form der Sparse Matrix:", X.shape)
print("Anzahl der Einträge in der Sparse Matrix:", X.nnz)

# Über das Vokabular iterieren, um Wort, Index und die entsprechende Spalte der Matrix anzuzeigen
for word, index in vectorizer.vocabulary_.items():
    # Zugriff auf die Anzahl des Wortes im Dokument
    word_count = sparse_matrix[0, index]  # Zugriff auf das spezifische Element in der Matrix
    # Ausgabe in einer Zeile
    print(f"Wort: {word}, Vokabular-Index: {index}, Anzahl des Wortes im Dokument: {word_count}")
