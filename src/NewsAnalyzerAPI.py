from openai import OpenAI

class NewsArticle:
    def __init__(self, title, description, text, date, url):
        self.title = title
        self.description = description
        self.text = text
        self.date = date
        self.url = url

class LLMConnector:
    def __init__(self, endpoint, key, model):
        # Initialize the connection to the LLM endpoint
        self.endpoint = endpoint

        self.client = OpenAI(
            base_url = self.endpoint,
            api_key = key,
        )

        self.model = model

    def process_text(self, text):
        # Method to interact with the LLM endpoint for text processing
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [
                {"role": "user", "content": text},
            ]
        )
        return response.choices[0].message.content

class NewsAnalyzer:
    language = 'English'
    event_components = {}
    event_components['what'] = 'What events occur in the text? List and enumerate (in '+language+'):'
    event_components['where'] = 'Where (locations and places) did the events described in the text occur? Output format is [country,state,city]. List and enumerate (in '+language+')::'
    event_components['when'] = 'When (dates) did the events described in the text occur? Output format is [yyyy-mm-dd]. List and enumerate (in '+language+')::'
    event_components['who'] = 'Who are the people or organizations described in the text? List and enumerate (in '+language+')::'
    event_components['why'] = 'Why did the events described in the texts occur? List and enumerate (in '+language+')::'
    event_components['how'] = 'How did the events described in the texts occur? List and enumerate (in '+language+')::'

    def __init__(self, llm_connector):
        self.llm_connector = llm_connector

    # Method to process and analyze an article
    def process_article(self, article):
        for component in self.event_components:
            print(component)
            print(self.llm_connector.process_text(article.text + "\n\n" + self.event_components[component]))
            print("--------------\n\n")

    # Method to process a list of articles
    def process_articles(self, news_list):
        for article in news_list:
          print(f"Article title: {article.title}\n")
          self.process_article(article)

    # Method to identify the specified component of the news
    def identify_component(self, article, component):
        return self.llm_connector.process_text((article.text + '\n\n'+ self.event_components[component]))