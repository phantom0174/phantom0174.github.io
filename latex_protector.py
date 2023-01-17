import os


# must ends with '/'
ENTRIES_TO_PROTECT_UNDER_SOURCE_FOLDER = [
    './about/',
    './_posts/'
]


def protect_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content: list[str] = file.read().split('\n')

    new = []

    status = "i"
    for (i, line) in enumerate(content):
        if status == "i" and line.startswith("$$") and line.endswith("$$") and len(line) > 2:
            if not content[i-1].startswith("<p>"):
                new.append("<p>")
            
            new.append(line)
            
            if not content[i+1].startswith("</p>"):
                new.append("</p>")
            
        elif status == "i" and line.startswith("$$"):
            if not content[i-1].startswith("<p>"):
                new.append("<p>")
            
            new.append(line)
            status = "e"
        
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
    traverse_folder(entry)
