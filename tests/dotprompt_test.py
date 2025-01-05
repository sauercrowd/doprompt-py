from dotprompt.dotprompt import DotPrompt
def test_parser():
    prompt = DotPrompt("./tests/simple.prompt")
    result = prompt.render_prompt(location="New York").strip()
    assert result == "You are the world's most welcoming AI assistant and are currently working in New York."
    result = prompt.render_prompt(location="New York", is_true=True).strip()
    ## looks like pybars drops doesn't consider lines only with conditions as empty newlines, but jinja2 does.
    assert result == "You are the world's most welcoming AI assistant and are currently working in New York.\nThis is a true statement."


def test_jinja():
    prompt = DotPrompt("./tests/simple_jinja.prompt")
    result = prompt.render_prompt(location="London").strip()
    assert result == "You are the world's most welcoming AI assistant and are currently working in London."
    result = prompt.render_prompt(location="London", is_true=True).strip()
    assert result == "You are the world's most welcoming AI assistant and are currently working in London.\n\nThis is a true statement."
