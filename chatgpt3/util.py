import requests

class ChatGPT3:
    """
    class untuk akses ChatGPT3 via API
    """
    def __init__(self, 
                 api_key,
                 model="text-davinci-003",
                 suffix="python",
                 max_tokens=1000,
                 temperature=0.1):

        self.url = "https://api.openai.com/v1/completions"
        self.model = model
        self.suffix = suffix
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.context = None
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            }

    
    def ngobrol(self, text):
        data = { 
            "model": self.model,
            "prompt": text,
            "suffix": self.suffix,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        output = response.json()['choices'][0]['text']
        print(output)

    def ngoding(self, text):
        if self.context is not None:
            text = f"dari kode : \n {self.context} \n " + text
        data = { 
            "model": self.model,
            "prompt": text,
            "suffix": self.suffix,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        output = response.json()['choices'][0]['text']
        self.context = output
        exec(output, globals())

    def tampilkan_kode_terakhir(self):
        print(self.context)

    def reset_context(self):
        self.context = None
    