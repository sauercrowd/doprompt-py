import unittest.mock
from unittest.mock import MagicMock
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


def test_expected_missing_param():
    prompt = DoPrompt("./tests/chat.prompt")

    try:
        rendered_messages = prompt.get_messages(values={})
    except ValueError as e:
        if 'value of userQuestion is not marked as optional but is None' in str(e):
            return 
    raise AssertionError('Expected ValueError not raised')
                                                


def test_expected_wrong_primitive_param():
    prompt = DoPrompt("./tests/chat.prompt")

    try:
        rendered_messages = prompt.get_messages(values={
            'userQuestion': 'What is the capital of France?',
            'location': 1
        })
    except ValueError as e:
        if 'value of "location" expected to be string but instead is <class \'int\'>' in str(e):
            return 
    raise AssertionError('Expected ValueError not raised')
                                                

def test_nested_array_param():
    prompt = DoPrompt("./tests/chat.prompt")

    rendered_messages = prompt.get_messages(values={
        'userQuestion': 'What is the capital of France?',
        'profiles': [
            {'username': 'johndoe', 'age': 30},
        ]
    })


def test_wrong_type_nested_array_param():
    prompt = DoPrompt("./tests/chat.prompt")

    try:
        rendered_messages = prompt.get_messages(values={
            'userQuestion': 'What is the capital of France?',
            'profiles': [
                {'username': 'johndoe', 'age': '30'},
            ]
        })
    except ValueError as e:
        if 'value of "profiles/age" expected to be integer but instead is <class \'str\'>' in str(e):
            return

## TODO: patch the openai client properly
#def test_execute_shortcut():
#    prompt = DoPrompt("./tests/chat.prompt")
#
#    mock_response = MagicMock()
#    mock_response.choices = [MagicMock()]
#    mock_response.choices[0].message.content = "Paris"
#
#    with unittest.mock.patch('openai.OpenAI.chat.completions.create', return_value=mock_response):
#        result = prompt.complete({
#            'userQuestion': 'What is the capital of France?',
#        })
#
#    assert result == "Paris"
