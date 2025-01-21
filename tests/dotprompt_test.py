from doprompt.doprompt import DoPrompt
from openai import OpenAI
import os

#def test_parser():
#    prompt = DoPrompt("./tests/simple.prompt")
#    result = prompt.render_prompt(location="New York").strip()
#    assert result == "You are the world's most welcoming AI assistant and are currently working in New York."
#    result = prompt.render_prompt(location="New York", is_true=True).strip()
#    assert result == "You are the world's most welcoming AI assistant and are currently working in New York.\nThis is a true statement."


def test_execute_prompt():
    prompt = DoPrompt("./tests/chat.prompt")

    openai = OpenAI()

    chat_completion = openai.chat.completions.create(
        messages=prompt.get_messages(values={'userQuestion': 'What is the capital of France?',
                                             'authors': [{'hello': 1}]}),
        model=prompt.model_name
    )

    print(chat_completion.choices[0].message.content)

    raise ValueError('Test failed')



#def test_jinja():
#    prompt = DotPrompt("./tests/simple_jinja.prompt")
#    result = prompt.render_prompt(location="London").strip()
#    assert result == "You are the world's most welcoming AI assistant and are currently working in London."
#    result = prompt.render_prompt(location="London", is_true=True).strip()
#    assert result == "You are the world's most welcoming AI assistant and are currently working in London.\n\nThis is a true statement."
#
#def test_proxy():
#    prompt = DotPrompt("./tests/simple_proxy.prompt")
#
#    from openai import OpenAI
#
#    client = OpenAI(
#        api_key=os.environ.get("PROMPTKINS_API_KEY"),
#        base_url="http://localhost:8080",
#    )
#
#    chat_completion = client.chat.completions.create(
#        messages=[{"role": "user", "content": "Say this is a test!"}],
#        model="gpt-4o-mini",
#    )
