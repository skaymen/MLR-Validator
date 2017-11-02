
from .base_cross_field_validator import BaseCrossFieldValidator

class CrossFieldWarningValidator(BaseCrossFieldValidator):

    def _validate_drainage_area(self):
        keys = ['drainageArea', 'contributingDrainageArea']
        if self._any_fields_in_document(keys):
            try:
                drainage_area, contributing_drainage_area = [float(self.merged_document.get(key, '').strip()) for key in keys]
            except ValueError:
                pass
            else:
                if (drainage_area and contributing_drainage_area) and contributing_drainage_area == drainage_area:
                    self._errors['drainageArea'] = ['contributingDrainageArea should not be equal to drainageArea']

    def validate(self, document, existing_document):
        '''
        After validate is called the error property will reflect the errors generated by the last call to validate
        :param dict document:
        :param dict existing_document:
        :return: boolean
        '''

        super().validate(document, existing_document)

        self._validate_drainage_area()

        return self._errors == {}