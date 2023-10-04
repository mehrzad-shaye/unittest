import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble


class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in wisconsin")
        self.assertIsInstance(ents, dict)

    def  test_get_ents_give_spacy_PERSON_is_returned_serializes_to_Person(self):
         model = NerModelTestDouble('eng')
         doc_ents = [{'text': 'Laurent Fressinet', 'label_':'PERSON'}]
         model.returns_doc_ents(doc_ents)
         ner = NamedEntityClient(model)
         result = ner.get_ents('...')
         expected_result = {'ents': [{'ent': 'Laurent Fressinet', 'label':'Person'}], 'html': ""}
         self.assertListEqual(result['ents'], expected_result['ents'])
 