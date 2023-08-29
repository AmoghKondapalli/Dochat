# Dochat
# A full solution for extracting valuable information from large documents using the power of LLMs.
### Has a complelete backend with login and register, and each user gets their own private database, need an OpenAI API key in order to deploy and run, example running in the following screenshots
# Fully Working
![login](https://github.com/AmoghKondapalli/Dochat/assets/90903421/a54b0dcb-b343-4aa0-99c0-59e43f5f75d9)
![register](https://github.com/AmoghKondapalli/Dochat/assets/90903421/f83b6c01-6954-4b9c-9026-462d276eb029)
![upload_files](https://github.com/AmoghKondapalli/Dochat/assets/90903421/24ea3af0-9797-4ed6-86a9-3ef06ab38d73)
![working](https://github.com/AmoghKondapalli/Dochat/assets/90903421/ff62659d-b284-481a-afe5-666bb10d16cf)
## You can add your OpenAI API key in the followning files:
### Dochat/django_chatgpt/chatclone/ingest.py
### Dochat/django_chatgpt/chatclone/func.py
## To Run
```pip3 install -r requirements.txt```

``` python3 manage.py runserver```
## Built using Django framework, Langchain, ChromaDB and OPENAI API
