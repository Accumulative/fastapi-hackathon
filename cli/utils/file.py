import os
from string import Template


def file_creator(app_dir: str, app_name: str, file_name: str):
    template_name = f"local_{file_name[:-3]}.tpl"
    
    with open(os.path.join(app_dir, file_name), "w") as fh:
        with open(os.path.join("cli/templates", template_name), "r") as template:
            src = Template(template.read())
            name = app_name[:-4]
            fh.write(src.substitute(name=name.lower(), name_upper=name.upper(), name_title=name.title()))