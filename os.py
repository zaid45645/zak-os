import os

class FileSystem():
    def __init__(self):
        pass  

    def create_file(self, filename):
        if filename in os.listdir('.'):
            print("File already exists!")
        else:
            with open(filename, "w") as f:
                f.write("") 
            print(f"File '{filename}' was created!")

    def delete_file(self, filename):
        if filename in os.listdir('.'):
            os.remove(filename)  
            print(f"File '{filename}' was deleted!")
        else:
            print("File not found.")

    def list_files(self):
        files = os.listdir(".")  
        if files:
            print("Files:", ", ".join(files))
        else:
            print("No files found")

    def edit_file(self, filename, content):
        if filename in os.listdir('.'):
            with open(filename, "w") as f:
                f.write(content)  
            print(f"File '{filename}' was edited!")
        else:
            print("File not found.")

    def read_file(self, filename):
        if filename in os.listdir('.'):
            with open(filename, "r") as f:
                content = f.read()  
            print(f"Content of '{filename}': \n{content}")
        else:
            print("File not found.")

    def create_process(self, process):
        os.system(process)

class OS():
    def __init__(self):
        self.file_system = FileSystem()
        self.welcome_mess = '''\n mmmmmm        #       mmmm   mmmm
     #"  mmm   #   m  m"  "m #"   "
   m#   "   #  # m"   #    # "#mmm
  m"    m"""#  #"#    #    #     "#
 ##mmmm "mm"#  #  "m   #mm#  "mmm#\n'''
        print(self.welcome_mess)
    
    def clear(self):
        os.system('cls' if os.name == "nt" else 'clear')
        print(self.welcome_mess)

    def cli(self):
        while True:
            command = input("\nZakOS:~$ ")
            if command == "exit":
                break
            elif command == "help":
                print("Available Commands \n 1. help \n 2. exit \n 3. clear \n 4. list files \n 5. create file <filename> \n 7. delete file <filename> \n 8. edit file <filename> \n 9. read file <filename> \n 10. create process <process>")
            elif command.startswith("create file "):
                filename = command.split("create file ")[1]
                self.file_system.create_file(filename)
            elif command.startswith("delete file "):
                filename = command.split("delete file ")[1]
                self.file_system.delete_file(filename)
            elif command == "list files":
                self.file_system.list_files()
            elif command.startswith("edit file "):
                parts = command.split("edit file ")[1].split(" ", 1)
                if len(parts) == 2:
                    filename = parts[0]
                    print("Enter content (type 'END' on a new line to finish):")
                    content_lines = []
                    while True:
                        line = input()
                        if line == "END":
                            break
                        content_lines.append(line)
                    content = "\n".join(content_lines)
                    self.file_system.edit_file(filename, content)
                else:
                    print("Usage: edit file <filename>")
            elif command.startswith("read file "):
                filename = command.split("read file ")[1]
                self.file_system.read_file(filename)
            elif command == "clear":
                self.clear()
            elif command.startswith("create process "):
                process = command.split("create process ")[1]
                self.file_system.create_process(process)

if __name__ == "__main__":
    zakos = OS()
    zakos.cli()