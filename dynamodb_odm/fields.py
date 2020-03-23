import decimal
import uuid


class Field:
    auto = False
    required = False
    default = None

    def __init__(self, auto=False, required=False, default=False):
        self.auto = auto
        self.required = required
        self.default = default

    def cast(self, value):
        return value


class PrimaryKeyField(Field):
    def __init__(self, keytype):
        if not isinstance(keytype, Field):
            raise TypeError(f'PrimaryKey keytype must be instance of Field.')

        self.keytype = keytype

        if keytype.auto:
            setattr(self, 'auto', True)

        super(PrimaryKeyField, self).__init__(
            auto=self.auto,
            required=keytype.required,
            default=keytype.default
        )

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
