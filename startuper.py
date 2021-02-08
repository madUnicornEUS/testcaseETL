from builder import Builder


class StartUper:
    extractors = list()
    files = list()
    processor = None
    
    def __init__(self, file_names):
        assert isinstance(file_names, list)
        self.files = file_names[:]
    
    def run(self):
        for file in self.files:
            crafted_extractor = Builder().build_extractor(file)
            if crafted_extractor is not None:
                self.extractors.append(crafted_extractor)
        self.processor = Builder().build_processor(self.extractors)
        self.processor.process_files()
        self.processor.state_sort()
        self.processor.file_crafter.show_inner_state()
        self.processor.craft_common_file()
