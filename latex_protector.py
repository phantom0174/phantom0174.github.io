import os


# must ends with '/'
ENTRIES_TO_PROTECT_UNDER_SOURCE_FOLDER = [
    'about/',
    '_posts/'
]

SKIP_SYNTAX = "<!--skip_lp-->"

def protect_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content: list[str] = file.read().split('\n')

    new = []

    """
    status
        i: need to find initiate
        e: need to find ending
        s: being skipped, toggle:
            i -> s -> i
    """

    status = "i"
    for (i, line) in enumerate(content):
        # custom skipping mark
        if status == "i" and line.startswith(SKIP_SYNTAX):
            new.append(SKIP_SYNTAX)
            status = "s"
        
        elif status == "s" and line.startswith(SKIP_SYNTAX):
            new.append(SKIP_SYNTAX)
            status = "i"
        
        # start and end on the same line
        elif status == "i" and line.startswith("$$") and line.endswith("$$") and len(line) > 4:
            if not content[i-1].startswith("<p>"):
                new.append("<p>")
            
            new.append(line)
            
            if not content[i+1].startswith("</p>"):
                new.append("</p>")
        
        # start on one line
        elif status == "i" and line.startswith("$$"):
            if not content[i-1].startswith("<p>"):
                new.append("<p>")
            
            new.append(line)
            status = "e"
        
        # end on one line
        elif status == "e" and line.endswith("$$"):
            new.append(line)
            
            if not content[i+1].startswith("</p>"):
                new.append("</p>")
            
            status = 'i'
        
        else:
            new.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(new))

    print(f'[Protected] {file_path}')


# root_path ended with '/'
def traverse_folder(root_path):
    for filename in os.listdir(root_path):
        if filename.endswith('.md'):
            protect_md_file(f'{root_path}{filename}')
        elif filename.find('.') == -1:
            traverse_folder(f'{root_path}{filename}/')


for entry in ENTRIES_TO_PROTECT_UNDER_SOURCE_FOLDER:
    traverse_folder(f'./source/{entry}')
