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

        for k, v in schema.__dict__.items():
            setattr(self, k, ModelField(k))

    def create(self, **_document):
        apply_schema = self._schema.apply(_document)
        return document.Document(apply_schema, self._schema.pk, self._table)

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
