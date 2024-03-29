import sys
import ruamel.yaml
from color import Colors


# settings
config_file_path = "./_config.yml"
#

yaml = ruamel.yaml.YAML()
yaml.indent = 2
yaml.preserve_quotes = True # type: ignore

def load_file():
    global config_file
    with open(config_file_path, 'r', encoding='utf-8') as file:
        config_file = yaml.load(file)

def save_file():
    global config_file
    with open(config_file_path, 'w', encoding='utf-8') as file:
        yaml.dump(config_file, file)


load_file()

config_file["deploy"]["message"] = sys.argv[1] if len(sys.argv) > 1 else None
save_file()


# checking
load_file()

print(
    f'{Colors.OKGREEN}[Deploy MSG Customizer]{Colors.ENDC}\n'
    f'Deploy message has been set to: '
    f'{Colors.OKCYAN}{config_file["deploy"]["message"]}{Colors.ENDC}'
)
