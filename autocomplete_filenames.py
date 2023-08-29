import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class FileTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_autocomplete(node, word)

    def _find_autocomplete(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append(prefix)
        for char, child_node in node.children.items():
            result.extend(self._find_autocomplete(child_node, prefix + char))
        return result

def build_file_trie(directory):
    file_trie = FileTrie()
    for _, _, files in os.walk(directory):
        for file in files:
            file_trie.insert(file)
    return file_trie

def convert_input(input_string):
    return "-".join(input_string.split())

class NewFileHandler(FileSystemEventHandler):
    def __init__(self, file_trie):
        super().__init__()
        self.file_trie = file_trie

    def on_created(self, event):
        if event.is_directory:
            return
        new_file_name = os.path.basename(event.src_path)
        self.file_trie.insert(new_file_name)

if __name__ == "__main__":
    current_directory = os.getcwd()
    file_trie = build_file_trie(current_directory)

    event_handler = NewFileHandler(file_trie)
    observer = Observer()
    observer.schedule(event_handler, path=current_directory, recursive=False)
    observer.start()

    try:
        while True:
            input_query = input("Enter a space-separated file name prefix to search (or 'exit' to quit): ")
            if input_query == "exit":
                break
            if input_query == "restart":
                print("Restarting the script...")
                subprocess.run(["python", __file__])
                exit()
            search_query = convert_input(input_query)
            _1920_autocomplete_options = file_trie.search("1920-"+search_query)
            _2400_autocomplete_options=file_trie.search("2400-"+search_query)
            
            if _1920_autocomplete_options or _2400_autocomplete_options:
                print("Autocomplete options:", _1920_autocomplete_options)
            else:
                print("No autocomplete options found.")

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
