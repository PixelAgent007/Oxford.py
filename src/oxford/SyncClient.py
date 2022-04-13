import requests


class SyncClient:
    """Sync Wrapper for Oxford API"""
    def __init__(self, app_id: str, app_key: str, language: str = 'en-gb', debug: bool = False) -> None:
        self.app_id = app_id
        self.app_key = app_key
        self.language = language
        self.url = f"https://od-api.oxforddictionaries.com:443/api/v2/entries/{self.language}/"
        self.header = {"app_id": app_id, "app_key": app_key}
        self.debug = debug

    def api_request(self, word: str) -> dict:
        """
        Normal api requests returns a huge dict
        """
        res = requests.request("GET", f"{self.url}{word.lower()}", headers=self.header)
        return res.json()

    def get_word_definition(self, word: str) -> list[str]:
        """Returns list of definitions of the word"""
        data = self.api_request(word)

        definitions = []
        for i in data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
            try:
                for e in i['definitions']:
                    definitions.append(e)
            except KeyError:
                cross_reference = self.get_word_definition(i['crossReferences'][0]['text'])
                definitions.extend(cross_reference)

        return definitions

    def define(self, word: str) -> list[str]:
        return self.get_word_definition(word)

    def get_word_examples(self, word: str) -> list[str]:
        """Get word examples """
        data = self.api_request(word)
        examples = []
        for i in data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
            try:
                for e in i['examples']:
                    examples.append(e['text'])
            except KeyError:
                cross_reference = self.get_word_examples(i['crossReferences'][0]['text'])
                examples.extend(cross_reference)

        return examples

    def get_audio_file(self, word) -> str:
        """Get audio file which tells you how to pronounce the word"""
        data = self.api_request(word)
        return data['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    def get_synonyms(self, word):
        """Get synonyms for the word"""
        try:
            data = self.api_request(word)
            synonyms = []
            for i in data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']:
                synonyms.append(i['text'])

            return synonyms

        except Exception as e:
            if self.debug:
                print(e)
            return "No Synonyms Found!"
