from latex_protector import Protector


target_folder_root = [
    "./source/_posts/",
    "./source/about/"
]

protector = Protector(target_folder_root)

protector.protect()
