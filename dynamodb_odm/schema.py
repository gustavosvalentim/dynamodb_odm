import copy
import dynamodb_odm.fields as fields


exclude = ['pk']


class Schema:
    pk = None

    def __init__(self, **keyschema):
        for keyname, keytype in keyschema.items():
            if not isinstance(keytype, fields.Field):
                raise TypeError(f'{keyname} not instance of Field.')

            if isinstance(keytype, fields.PrimaryKeyField):
                self.pk = keyname

            setattr(self, keyname, keytype)

        if not self.pk:
            raise KeyError(f'Primary Key type not found.')

    def apply(self, document):
        doc_copy = copy.deepcopy(document)
        schema_keys = dict([
            [k, v] for k, v in self.__dict__.items() if k not in exclude
        ])

        for keyname, keytype in schema_keys:
            if keyname not in document:
                if keytype.required:
                    raise KeyError(f'Key {keyname} is required')
                
                if keytype.auto:
                    doc_copy[keyname] = keytype.cast(None)
                else:
                    doc_copy[keyname] = keytype.default

            else:
                doc_copy[keyname] = keytype.cast(document[keyname])

        return doc_copy
