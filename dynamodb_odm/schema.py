import dynamodb_odm.fields as fields


class Schema:
    autokeys: list = []

    def __init__(self, **keyschema):
        for keyname, keytype in keyschema.items():
            if not isinstance(keytype, fields.Field):
                raise TypeError(f'{keyname} not instance of Field.')

            if keytype.auto:
                self.autokeys.append(keyname)

            setattr(self, keyname, keytype)