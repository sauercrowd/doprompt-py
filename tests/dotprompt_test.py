from doprompt.doprompt import DoPrompt

def test_execute_prompt():
    prompt = DoPrompt("./tests/chat.prompt")

    rendered_messages = prompt.get_messages(values={
        'userQuestion': 'What is the capital of France?',
    })
                                                

    assert rendered_messages == [
        {'role': 'system', 'content': 'You are a helpful AI assistant that really loves to talk about food. Try to work\nfood items into all of your conversations.'},
        {'role': 'user', 'content': 'What is the capital of France?'}
    ]


    assert prompt.model_name == 'gpt-4o'


          

def test_execute_shortcut():
    prompt = DoPrompt("./tests/chat.prompt")

    prompt.complete({
        'userQuestion': 'What is the capital of France?',
    })
