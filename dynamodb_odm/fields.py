import decimal
import uuid


class Field:
    auto = False

    def cast(self, value):
        return value


class PrimaryKeyField(Field):
    def __init__(self, keytype):
        if not isinstance(keytype, Field):
            raise TypeError(f'PrimaryKey keytype must be instance of Field.')

        self.keytype = keytype

        if keytype.auto:
            setattr(self, 'auto', True)

    def cast(self, value):
        try:
            return self.keytype.cast(value)
        except ValueError:
            return value


class StringField(Field):
    def cast(self, value):
        try:
            return str(value)
        except ValueError:
            return value


class IntegerField(Field):
    def cast(self, value):
        try:
            return int(value)
        except ValueError:
            return value


class UUID4Field(Field):
    auto = True

    def cast(self, _):
        return uuid.uuid4().hex
