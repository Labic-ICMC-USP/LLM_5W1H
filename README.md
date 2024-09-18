# LLM-5W1H
This project is a LLM-based System for extracting main events from news articles.

## Step-by-Step Tutorial on how to use News Analyzer API
1. Ensure you have OpenAI's Python library installed by running the following command in the Python shell.
        
        pip install openai 

2. Import News Analyzer API.

```python
from src.NewsAnalyzerAPI import NewsArticle
from src.NewsAnalyzerAPI import LLMConnector
from src.NewsAnalyzerAPI import NewsAnalyzer
```


3. Instantiate your LLMConnector and NewsAnalyzer objects.
```python
connector = LLMConnector("your_llm_endpoint", "your_llm_key", "your_llm_model")
analyzer = NewsAnalyzer(connector)
```

4. Give an example article to the analyzer, with the following parameters: title, description, text, date, url.

```python
title = "Taliban attacks German consulate in northern Afghan city of Mazar-i-Sharif with truck bomb"

description = "The death toll from a powerful Taliban truck bombing at the German consulate in Afghanistan's Mazar-i-Sharif city rose to at least six Friday, with more than 100 others wounded in a major militant assault."

text = "The death toll from a powerful Taliban truck bombing at the German consulate in Afghanistan's Mazar-i-Sharif city rose to at least six Friday, with more than 100 others wounded in a major militant assault. The Taliban said the bombing late Thursday, which tore a massive crater in the road and overturned cars, was a \"revenge attack\" for US air strikes this month in the volatile province of Kunduz that left 32 civilians dead. The explosion, followed by sporadic gunfire, reverberated across the usually tranquil northern city, smashing windows of nearby shops and leaving terrified local residents fleeing for cover. \"The suicide attacker rammed his explosives-laden car into the wall of the German consulate,\" local police chief Sayed Kamal Sadat told AFP. All German staff from the consulate were unharmed, according to the foreign ministry in Berlin."

date = "2016-11-11 08:42:13"

url = "http://www.telegraph.co.uk/news/2016/11/10/taliban-attack-german-consulate-in-northern-afghan-city-of-mazar/"

article_example = NewsArticle(title, description, text, date, url)
```

4. Extract the article components by calling process_article(article) function (or process_articles(articles) for a list of articles) in the created NewsAnalyzer object:
```python            
analyzer.process_article(article_example)
```
This function extracts all of the article components: what, where, when, who, why, how (5W1H). It is also possible to extract each of them separately by calling the function identify_component(article, component) in the same NewsAnalyzer object, where the 'component' parameter must be one of the components from 5W1H. For example:

```python
analyzer.identify_component(article_example, 'what')
```
This line returns the 'what' component from the article as a result.