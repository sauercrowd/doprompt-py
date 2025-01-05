import re
import yaml

section_re = re.compile(r'^---\s*$', re.MULTILINE)

class DotPrompt:
    def __init__(self, fpath):
        with open(fpath, 'r') as f:
            content = f.read()

        sections = section_re.split(content)

        if len(sections) != 3:
            raise ValueError('Missing section separator')

        metadata_section = sections[1]
        prompt_section = sections[2]

        self.metadata = yaml.safe_load(metadata_section)
        if 'model' not in self.metadata:
            raise ValueError('Missing model in metadata')

        self.model = self.metadata['model']
        self.model_config = self.metadata.get('config', {})

        self.prompt_template = prompt_section.strip()

    def get_metadata(self):
        return self.metadata

    def render_prompt(self, **kwargs):
        template_engine = self.metadata.get('template_engine', 'handlebars')
        if template_engine == 'handlebars':
            return render_handlebars(self.prompt_template, **kwargs)
        elif template_engine == 'jinja2':
            return render_jinja(self.prompt_template, **kwargs)
        else:
            raise ValueError(f'Unknown template engine: {template_engine}')



def render_handlebars(content, **kwargs):
    from pybars import Compiler
    compiler = Compiler()

    template = compiler.compile(content)

    return template(kwargs)

def render_jinja(content, **kwargs):
    from jinja2 import Template
    template = Template(content)
    res =  template.render(**kwargs)
    return res
