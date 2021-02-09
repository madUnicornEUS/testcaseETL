from tsv_file_crafter import TsvFileCrafter


class FileProcessor:
    processing_files = list()

    def __init__(self, extractors):
        assert isinstance(extractors, list)
        self.processing_files = extractors[:]
        self.file_crafter = TsvFileCrafter()
    
    def process_files(self):
        self.extract_file_structure()
        for extractor in self.processing_files:
            while True:
                new_values = extractor.get_value()
                if new_values is None:
                    break
                self.update_crafter_state(new_values)
    
    def craft_common_file(self):
        self.file_crafter.write_file()

    def state_sort(self):
        self.file_crafter.sort_inner_state()

    def update_crafter_state(self, new_values):
        self.file_crafter.update_state(new_values)

    def extract_file_structure(self):
        file_columns = list()
        for extractor in self.processing_files:
            file_columns += extractor.get_columns()
        self.file_crafter.set_structure(file_columns)
