import os


# must ends with '/'
ENTRIES_TO_PROTECT_UNDER_SOURCE_FOLDER = [
    'about/',
    '_posts/'
]

SKIP_ALL_SYNTAX = "<!--lp:skip-all-->"
SKIP_SOME_SYNTAX = "<!--lp:skip-some-->"

protected_count = 0

def protect(file_path):
    global protected_count

    state = "N"
    content = []

    # [index, context]
    insert_cmd = []

    with open(file_path, 'r', encoding='utf-8') as i_file:
        content = i_file.read().split('\n')

    for (i, line) in enumerate(content):
        if state == "N":
            if line.startswith("$$"):
                state = "S"
                
                if not content[i - 1].startswith("<p>"):
                    insert_cmd.append([i, "<p>"])

                if not (line.endswith("$$") and len(line) > 4):
                    continue
                
            elif line.startswith(SKIP_SOME_SYNTAX):
                state = "I"
            elif line.startswith(SKIP_ALL_SYNTAX):
                return

        if state == "S" and line.endswith("$$"):
            state = "N"
            
            if (i + 1) >= len(content) or not content[i + 1].startswith("</p>"):
                insert_cmd.append([i + 1, "</p>"])

        if state == "I" and line.startswith(SKIP_SOME_SYNTAX):
            state = "N"

    insert_cmd.reverse()

    for cmd in insert_cmd:
        content.insert(cmd[0], cmd[1])

    with open(file_path, 'w', encoding='utf-8') as o_file:
        o_file.write('\n'.join(content))

    print(f'[Protected] {file_path}')
    protected_count += 1


# root_path ended with '/'
def traverse_folder(root_path):
    for filename in os.listdir(root_path):
        if filename.endswith('.md'):
            protect(f'{root_path}{filename}')
        elif filename.find('.') == -1:
            traverse_folder(f'{root_path}{filename}/')

for entry in ENTRIES_TO_PROTECT_UNDER_SOURCE_FOLDER:
    traverse_folder(f'./source/{entry}')

print(f'\033[1;32m[LaTeX Protector] Protected {protected_count} files.\033[0m\n')
