import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

#Topic Modeling (LDA)

def categorize_tasks(tasks, processed_sentences):
    """Categorizes tasks using LDA topic modeling."""
    vectorizer = TfidfVectorizer(max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(processed_sentences)
    
    lda_model = LatentDirichletAllocation(n_components=4, random_state=42)
    lda_output = lda_model.fit_transform(tfidf_matrix)
    
    category_map = {0: 'Professional', 1: 'Personal', 2: 'Team', 3: 'Administrative'}
    
    for task, topic_dist in zip(tasks, lda_output):
        dominant_topic = np.argmax(topic_dist)
        task['category'] = category_map[dominant_topic]
    
    return tasks

# Word Embeddings + Clustering

    # def train_word_embeddings(self, processed_sentences: List[str]):
    #     """Train Word2Vec embeddings"""
    #     # Tokenize processed sentences
    #     tokenized_sentences = [sent.split() for sent in processed_sentences]
        
    #     # Train Word2Vec model
    #     model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)
    #     return model
    

    # def categorize_tasks(self, tasks: List[Dict], processed_sentences: List[str]):
    #     """Categorize tasks using Word2Vec embeddings and K-Means clustering"""

    #     # Train Word2Vec model
    #     model = self.train_word_embeddings(processed_sentences)

    #     # Convert sentences to embeddings
    #     embeddings = [np.mean([model.wv[word] for word in sent.split() if word in model.wv], axis=0)
    #                   if any(word in model.wv for word in sent.split()) else np.zeros(100)
    #                   for sent in processed_sentences]

    #     # Cluster embeddings using K-Means
    #     kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    #     task_clusters = kmeans.fit_predict(embeddings)

    #     # Define category names
    #     category_map = {
    #         0: 'Professional',
    #         1: 'Personal',
    #         2: 'Team',
    #         3: 'Administrative'
    #     }

    #     # Assign categories
    #     for task, cluster in zip(tasks, task_clusters):
    #         task['category'] = category_map[cluster]

    #     return tasks