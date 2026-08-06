from pathlib import Path

class LocalFolderConnector(KnowledgeSourceConnector):
    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)

        self.supported_extensions = {".pdf", ".docx", ".pptx", ".xlsx", ".txt", ".md"}

        self.is_connected = False
        self.is_running = False
        self.watcher = None

    def connect(self):
        dir_path = self.dataset_path
        if not dir_path.exists() or not dir_path.is_dir():
            self.is_connected = False
            raise FileNotFoundError(f"Directory does not exist: {dir_path}")

        can_read = dir_path.exists() and dir_path.is_dir() and dir_path.stat().st_mode & 0o400

        if can_read:
            self.is_connected = True
            return True
        else:
            self.is_connected = False
            raise PermissionError(f"Insufficient permissions to access the directory: {dir_path}")
    def discover_documents(self):
        if not self.is_connected:
            raise ConnectionError("Not connected to the knowledge source.")

        documents = []
        for file in self.dataset_path.rglob("*"):
            if file.is_file():
                if file.suffix in self.supported_extensions:
                    documents.append(file)
        return documents




    