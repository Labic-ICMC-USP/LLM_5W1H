# LLM-5W1H
This project is an LLM-based System for extracting main events from news articles.

## Step-by-Step Tutorial on how to use LLM-5W1H API
### 1. Install the required libraries by running the following commands in your command line:

```
pip install openai
pip install llm5w1h
```

### 2. Import LLM-5W1H API classes.

```python
from llm5w1h import NewsArticle, NewsAnalyzer
```

### 3. Instantiate your NewsAnalyzer object.
```python
analyzer = NewsAnalyzer("your_llm_endpoint", "your_llm_key", "your_llm_model")
```
The first parameter (`"your_llm_endpoint"`) refers to the used LLM model's endpoint, necessary for the `NewsAnalyzer` to establish the connection. The second one (`"your_llm_key"`) is the key to be allowed to access the model. The last one (`"your_llm_model"`) is the name of the model that is going to be used, such as `"llama3.1"`, `"gemma2"`, etc.

### 4. Give an example article to the analyzer, with the following parameters: *title, description, text, date, url*.

```python
title = "Taliban attacks German consulate in northern Afghan city of Mazar-i-Sharif with truck bomb"

description = "The death toll from a powerful Taliban truck bombing at the German consulate in Afghanistan's Mazar-i-Sharif city rose to at least six Friday, with more than 100 others wounded in a major militant assault."

text = "The death toll from a powerful Taliban truck bombing at the German consulate in Afghanistan's Mazar-i-Sharif city rose to at least six Friday, with more than 100 others wounded in a major militant assault. The Taliban said the bombing late Thursday, which tore a massive crater in the road and overturned cars, was a \"revenge attack\" for US air strikes this month in the volatile province of Kunduz that left 32 civilians dead. The explosion, followed by sporadic gunfire, reverberated across the usually tranquil northern city, smashing windows of nearby shops and leaving terrified local residents fleeing for cover. \"The suicide attacker rammed his explosives-laden car into the wall of the German consulate,\" local police chief Sayed Kamal Sadat told AFP. All German staff from the consulate were unharmed, according to the foreign ministry in Berlin."

date = "2016-11-11 08:42:13"

url = "http://www.telegraph.co.uk/news/2016/11/10/taliban-attack-german-consulate-in-northern-afghan-city-of-mazar/"

article_example = NewsArticle(title, description, text, date, url)
```

### 5. Extract the article components by calling process_article(article) function in the created NewsAnalyzer object:
```python            
analyzer.process_article(article_example)
```
This function extracts all of the article components: *what, where, when, who, why, how* **(5W1H)**. It is also possible to extract each of them separately using `identify_component(component)` in the same `NewsAnalyzer` object, where the '`component`' parameter must be one of the components from 5W1H.

For example, the following line returns the 'What' component from the article as a result:

```python
analyzer.identify_component('What')
-> 'Truck bombing at the German consulate in Mazar-i-Sharif city, Afghanistan'
```