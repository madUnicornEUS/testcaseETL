
class FileProcessor:
    processing_files = list()
    inner_state = dict()
    
    def __init__(self, extractors):
        assert isinstance(extractors, list)
        self.processing_files = extractors[:]
    
    def process_files(self):
        file_columns = list()
        for extractor in self.processing_files:
            file_columns += extractor.get_columns()
    
    def craft_comon_file(self):
        pass