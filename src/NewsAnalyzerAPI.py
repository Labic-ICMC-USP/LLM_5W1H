from openai import OpenAI

class NewsArticle:
    def __init__(self, title, description, text, date, url):
        self.title = title
        self.description = description
        self.text = text
        self.date = date
        self.url = url

class LLMConnector:
    def __init__(self, endpoint):
        # Initialize the connection to the LLM endpoint
        self.endpoint = endpoint

        self.client = OpenAI(
            base_url = self.endpoint,
            api_key = "dummykey",
        )

    def process_text(self, text):
        # Method to interact with the LLM endpoint for text processing
        response = self.client.chat.completions.create(
            model = "openchat_3.5",
            messages = [
                {"role": "user", "content": text},
            ]
        )
        return response.choices[0].message.content

class NewsAnalyzer:
    language = 'Portuguese'
    event_components = {}
    event_components['what'] = 'What events occur in the text? List and enumerate (in '+language+'):'
    event_components['where'] = 'Where (locations and places) did the events described in the text occur? Output format is [country,state,city]. List and enumerate (in '+language+')::'
    event_components['when'] = 'When (dates) did the events described in the text occur? Output format is [yyyy-mm-dd]. List and enumerate (in '+language+')::'
    event_components['who'] = 'Who are the people or organizations described in the text? List and enumerate (in '+language+')::'
    event_components['why'] = 'Why did the events described in the texts occur? List and enumerate (in '+language+')::'
    event_components['how'] = 'How did the events described in the texts occur? List and enumerate (in '+language+')::'

    def __init__(self, llm_connector):
        self.llm_connector = llm_connector

    def process_articles(self, news_list):
        # Method to process and analyze a list of news articles
        for article in news_list:
          print(f"Article title: {article.title}\n")
          for c in self.event_components:
            print(c)
            self.llm_connector.process_text(article.text + "\n\n" + self.event_components[c])
            print("--------------\n\n")

    def identify_component(self, article, component):
        # Method to identify the specified component of the news
        return self.llm_connector.process_text((article.text + '\n\n'+ self.event_components[component]))

    # -> manter as funções abaixo ou só esta de cima?

    def identify_what(self, article):
        # Method to identify the "what" component of the news
        return self.llm_connector.process_text((article.text + '\n\n'+ self.event_components['what']))

    def identify_where(self, article):
        # Method to identify the "where" component of the news
        return self.llm_connector.process_text((article.text + '\n\n'+ self.event_components['where']))

    def identify_when(self, article):
        # Method to identify the "when" component of the news
        return self.llm_connector.process_text((article.text + '\n\n'+ self.event_components['when']))

    def identify_who(self, article):
        # Method to identify the "who" component of the news
        return self.llm_connector.process_text((article.text + '\n\n'+ self.event_components['who']))

    def identify_why(self, article):
        # Method to identify the "why" component of the news
        return self.llm_connector.process_text((article.text + '\n\n'+ self.event_components['why']))

    def identify_how(self, article):
        # Method to identify the "how" component of the news
        return self.llm_connector.process_text((article.text + '\n\n'+ self.event_components['how']))