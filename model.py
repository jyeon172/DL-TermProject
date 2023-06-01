import requests
from youtube_transcript_api import YouTubeTranscriptApi


class Model():
    def __init__(self):
        self.url = ""
        self.input = ""
        self.output = ""
        self.question = ""
        self.answer = ""

    def setUrl(self, url):
        url = url.split('watch?v=')[1]
        self.url = url
        print(self.url)
        
    def subtitle(self):
        srt = YouTubeTranscriptApi.get_transcript(self.url,languages=['ko'])
        res = ''
        for line in srt :
            res = res + line['text'] + '\n'
            
        self.input = res
        print(res)
        
        return self.input
    
    def summarize_api(self, payload):
        API_URL = "https://api-inference.huggingface.co/models/eenzeenee/t5-base-korean-summarization"
        headers = {"Authorization": "Bearer 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"}
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    def summarize(self):
        output = self.summarize_api({
            "inputs": self.input
        })
        self.output = output[0]['summary_text']

        return self.output
    
    def setQuestion(self, question):
        self.question = question
        print(self.question)
    
    def QA_api(self, payload):
        API_URL = "https://api-inference.huggingface.co/models/monologg/koelectra-small-v2-distilled-korquad-384"
        headers = {"Authorization": "Bearer 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"}
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    
    def QA(self):
        output = self.QA_api({
            "inputs": {
                "question": self.question,
                "context": self.input
                },
            })
        self.answer = output['answer']
        
        return self.answer
        
