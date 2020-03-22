exclude = [
    'table'
]


class Document:
    def __init__(self, document, table):
        self.table = table

        for k, v in document.items():
            setattr(self, k, v)

    def save(self):
        item = self.__dict__

        for k in exclude:
            del item[k]

        self.table.put_item(Item=item)

    def delete(self):
        pass