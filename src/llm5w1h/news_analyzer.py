from ollama import Client
import json

# Class for storing the news article information
class NewsArticle:
    def __init__(self, title, description, text, date, url):
        self.title = title
        self.description = description
        self.text = text
        self.date = date
        self.url = url

# Class for connecting to the specified LLM
class LLMConnector:
    def __init__(self, endpoint, key, model, text, num_ctx=10240, temperature=0):

        self.llm_json_response = None
        self.system_prompt = """You are an AI designed to extract key event components (5W1H: Who, What, When, Where, Why, How) from news articles. Your task is to analyze the given article and return only the extracted components in a structured JSON format. Each component should be concise and informative, based on the details provided in the article. The components to extract are as follows:


        1. **Who**: Identify the individuals, groups, or organizations involved in the event. This may include specific people, roles, or organizations.
        2. **What**: Summarize the core event or action described in the article.
        3. **When**: Provide the exact time and/or date when the event occurred. If not explicitly stated, use the most relevant time frame mentioned.
        4. **Where**: Specify the location where the event took place (e.g., city, country, landmark, etc.).
        5. **Why**: If the article provides a reason or cause for the event, include it here. If not stated, leave this field blank or provide 'Not mentioned'.
        6. **How**: Describe the method or manner in which the event occurred. This could refer to processes, mechanisms, or circumstances leading to the event.

        Your output should be formatted as a JSON object. Below is an example of the expected output structure:

        ```json
        {
          "Who": "Name or group of individuals or organizations involved in the event",
          "What": "Description of the event or action that occurred",
          "When": "Exact date and/or time when the event occurred (format YYYY-MM-DD)",
          "Where": "Location where the event took place (city, country, or specific place)",
          "Why": "The reason or cause behind the event",
          "How": "The method or manner in which the event occurred"
        }
        ```"""

        self.user_prompt = """
        "Please read the following news article and extract the 5W1H components from the text. For each component, provide a brief and precise answer. Your response should be in the form of a JSON object with the following structure:

        ```json
        {
          "Who": "Name or group of individuals or organizations involved in the event",
          "What": "Description of the event or action that occurred",
          "When": "Exact date and/or time when the event occurred (format YYYY-MM-DD)",
          "Where": "Location where the event took place (city, country, or specific place)",
          "Why": "The reason or cause behind the event (if provided in the text)",
          "How": "The method or manner in which the event occurred (if specified in the text)"
        }
        ```

        ### Instructions for each component:
        1. **Who**: Identify the individuals, groups, or organizations involved in the event. This can include names or roles (e.g., "president", "police", "protesters").
        2. **What**: Summarize the core event or action described in the article. This is the primary event or situation that the article focuses on (e.g., "flood", "meeting", "discovery").
        3. **When**: Extract the exact time and/or date the event occurred. If multiple dates or times are mentioned, provide the most relevant one.
        4. **Where**: Identify the geographical location where the event took place. This could include cities, countries, or even specific buildings or landmarks.
        5. **Why**: If the reason or cause behind the event is given in the article, provide a clear explanation here (e.g., "due to a natural disaster", "as a result of a political decision").
        6. **How**: Describe the manner or method in which the event unfolded or occurred. This might be about the process, technique, or circumstances that led to the event (e.g., "due to a bomb explosion", "after negotiations").

        Important: Your output must be in JSON format only. No additional text, explanations, or comments are allowed. Do not include any other information outside of the JSON structure.

        Now, apply the same logic to the following news article.

        ### Text to analyze:
        {text}
        """


        client = Client(
          host=endpoint,
        )

        response = client.chat(model=model, messages=[
            {
              'role': 'system',
              'content': self.system_prompt,
            },
            {
              'role': 'user',
              'content': self.user_prompt.replace('{text}',text),
            },
          ],
          options= {
              'temperature': temperature,
              'num_ctx': num_ctx,
              'seed': 42
          }
        )
        llm_json_response =  response['message']['content'].strip()
        try:
          r = llm_json_response
          r = r.replace('```json', '')
          r = r.replace('```', '')
          json_obj = json.loads(r)
          self.llm_json_response = json_obj
        except Exception as error:
          print("An exception occurred:", error)
          self.llm_json_response = None

    def process_text(self):
        return self.llm_json_response

# Class for analyzing news articles and extracting its components
class NewsAnalyzer:
    def __init__(self, endpoint, key, model, num_ctx=10240, temperature=0):
        self.endpoint = endpoint
        self.key = key
        self.model = model
        self.num_ctx = num_ctx
        self.temperature = temperature

    # Method to process article, extracting its components
    def process_article(self, article):
        text = "Date: {article.date}\nTitle: {article.title}\nDescription: {article.description}\nText: {article.text}\nURL: {article.url}"
        text = text.format(article=article)
        print(text)
        self.llm_connector = LLMConnector(self.endpoint, self.key, self.model, text, self.num_ctx, self.temperature)
        return self.llm_connector.llm_json_response

    # Method to get the specified component from the text
    def identify_component(self, component):
        return self.llm_connector.llm_json_response[component]

    # Method to get all the previously extracted components
    def extract_components(self):
        what_pred = self.identify_component("What")
        where_pred = self.identify_component("Where")
        when_pred = self.identify_component("When")
        who_pred = self.identify_component("Who")
        why_pred = self.identify_component("Why")
        how_pred = self.identify_component("How")

        components = {
            "what_pred": what_pred,
            "where_pred": where_pred,
            "when_pred": when_pred,
            "who_pred": who_pred,
            "why_pred": why_pred,
            "how_pred": how_pred,
        }

        return components