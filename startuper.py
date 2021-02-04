from builder import Builder


class StartUper:
    extractors = list()
    files = list()
    processor = None
    
    def _init_(self, file_names):
        assert isinstance(file_names, list)
        files = file_names[:]
    
    def start_up(self):
        for file in self.files:
            self.extractors.append(Builder().build_extractor(file))
            
        self.processor = Builder().build_processor()
        
        self.processor.process_files()
        