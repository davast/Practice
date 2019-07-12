import os


class Search:
    def __init__(self, path: str, is_recursive: bool):
        self.path = path
        self.recursive = is_recursive

    def search_in_file(self, path: str, keyword: str):
        with open(path, 'r') as fp:
            for ln, line in enumerate(fp, start=1):
                if keyword in line:
                    print('{}:{}  {}'.format(
                        path, ln, line.rstrip()))

    def scan_folder(self, path: str, keyword: str):
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                self.search_in_file(full_path, keyword)
            elif self.recursive:
                self.scan_folder(full_path, keyword)
                
    def run(self, keyword: str):
        if os.path.isfile(self.path):
            self.search_in_file(self.path, keyword)
        elif os.path.isdir(self.path):
            self.scan_folder(self.path, keyword)
        else:
            print('ERROR: Invalid path')


if __name__ == '__main__':
    crowler = Search('.\\', True)
    crowler.run('__main__')
