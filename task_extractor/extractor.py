import spacy
import nltk
from logger import logger
import re
import csv
from typing import List, Dict
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from task_extractor.utils import extract_deadline
from task_extractor.models import categorize_tasks

class AdvancedTaskExtractor:
    def __init__(self):
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = set(stopwords.words('english'))
        
        self.task_indicators = {
            'imperative_verbs': ['buy', 'clean', 'review', 'prepare', 'submit', 'finalize',
                                 'complete', 'schedule', 'discuss', 'send', 'create', 'update',
                                 'resolve', 'go', 'finish', 'plan', 'organize'],
            'task_phrases': ['need to', 'has to', 'should', 'must', 'will', 'plan to', 'going to', 'wants to']
        }

    def preprocess_text(self, text: str) -> List[str]:
        """Preprocess text by tokenizing and lemmatizing."""
        text = re.sub(r'\s+', ' ', text).strip()
        sentences = sent_tokenize(text)
        
        processed_sentences = []
        for sentence in sentences:
            doc = self.nlp(sentence)
            processed_sentence = [
                token.lemma_.lower()
                for token in doc
                if token.text.lower() not in self.stop_words and not token.is_punct and token.pos_ in ['VERB', 'NOUN', 'PROPN']
            ]
            processed_sentences.append(' '.join(processed_sentence))
        
        return sentences, processed_sentences

    def identify_tasks(self, original_sentences: List[str], processed_sentences: List[str]) -> List[Dict]:
        """Identify tasks from processed sentences."""
        tasks = []

        for orig_sent, proc_sent in zip(original_sentences, processed_sentences):
            logger.info(f"Analyzing Sentence: {orig_sent}")
            logger.info(f"Processed Sentence: {proc_sent}")
            
            is_task = any(verb in proc_sent for verb in self.task_indicators['imperative_verbs']) or \
                      any(phrase in orig_sent.lower() for phrase in self.task_indicators['task_phrases'])

            if not is_task:
                logger.info("Not a task. Skipping.")
                continue
            
            doc = self.nlp(orig_sent)
            entities = [ent.text for ent in doc.ents if ent.label_ == "PERSON"] or \
                       [token.text for token in doc if token.dep_ in ["nsubj", "nsubjpass"]]

            deadline = extract_deadline(orig_sent)

            task_entry = {
                'task': orig_sent,
                'processed_task': proc_sent,
                'entity': entities[0] if entities else None,
                'deadline': deadline
            }

            logger.info(f"Task Identified: {task_entry}")
            tasks.append(task_entry)
        
        return tasks

    def extract_tasks(self, text: str) -> List[Dict]:
        """Main extraction pipeline."""
        original_sentences, processed_sentences = self.preprocess_text(text)
        tasks = self.identify_tasks(original_sentences, processed_sentences)
        categorized_tasks = categorize_tasks(tasks, processed_sentences)
        return categorized_tasks
