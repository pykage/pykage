import pathlib
from command.base_cmd import BaseCommand 
from files.file import list_to_list_abspath
from files.toml_parse import PyProject

class AddCommand(BaseCommand):
    name = 'add'
    help = "add file to LIST_FILE"
    option = [{
        "name": ("-p", "--pyproject"),
        "option": {
            "type": str,
            "help": "the pkg.py path",

        }
    }]

    arguments = [{
        "name": "files",
        "option": {
            "type": str,
            "required": False,
            "nargs": -1
        }
    }]

    def main(self):
        path = self.pyproject if self.pyproject else (pathlib.Path() / "pkg.toml").resolve()
        list_file = list_to_list_abspath(self.files)
        toml = PyProject(path)
        for i in list_file:
            toml.append_file(i)
        toml.save()

        print('multiple file added to LIST_FILE: ', ' '.join(list_file))
