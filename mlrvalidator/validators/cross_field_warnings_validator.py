from .base_cross_field_validator import BaseCrossFieldValidator


class CrossFieldWarningsValidator(BaseCrossFieldValidator):
    def __init__(self):
        self._warnings = {}
        super().__init__()

    def _validate_drainage(self):
        keys = ['drainageArea', 'contributingDrainageArea']
        if self._any_fields_in_document(keys):
            try:
                cont_drainage_area, drainage_area = [float(self.merged_document.get(key, '').strip()) for key in keys]
            except ValueError:
                pass
            else:
                if cont_drainage_area == drainage_area:
                    self._warnings['drainage_areas'] = ["Contributing drainage area is equal to drainage area"]

    def validate(self, document, existing_document):
        super().validate(document, existing_document)
        self._validate_drainage()
        return self._warnings == {}

    @property
    def warnings(self):
        return self._warnings
