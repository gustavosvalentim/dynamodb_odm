import copy

import boto3.dynamodb.conditions as conditions

import dynamodb_odm.document as document
import dynamodb_odm.connection as connection


class ModelField:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __getattr__(self, attr):
        expr = conditions.Attr(self.attribute_name)

        if not hasattr(expr, attr):
            raise KeyError(f'Condition {attr} not found.')

        return getattr(expr, attr)


class Model:
    def __init__(self, table_name, schema):
        self._table = connection.dynamodb.use(table_name)
        self._schema = schema
        self._expr = None

        for k, v in schema.__dict__.items():
            setattr(self, k, ModelField(k))

    def __call__(self, **_document):
        doc_copy = copy.deepcopy(_document)

        for k, v in _document.items():
            if hasattr(self._schema, k):
                keytype = getattr(self._schema, k)
                is_autokey = k in self._schema.autokeys
                doc_copy[k] = keytype.cast(v) if not is_autokey else v

            for ak in self._schema.autokeys:
                if ak not in doc_copy:
                    keytype = getattr(self._schema, ak)
                    doc_copy[ak] = keytype.cast(None)

        return document.Document(doc_copy, self._table)

    def get(self, value):
        item = self._table.get_item(Key={
            self._schema.pk: value
        })

        if 'Item' not in item:
            return None

        return item['Item']

    def scan(self, _filter=None):
        if not _filter:
            return self._table.scan()['Items']

        return self._table.scan(FilterExpression=_filter)['Items']
