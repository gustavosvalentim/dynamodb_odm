exclude = [
    'table',
    'pk'
]


class Document:
    def __init__(self, document, pk, table):
        self.table = table
        self.pk = pk

        for k, v in document.items():
            setattr(self, k, v)

    def save(self):
        item = dict([
            [k, v] for k, v in self.__dict__.items() if k not in exclude
        ])

        self.table.put_item(Item=item)

    def delete(self):
        self.table.delete_item(Key={
            self.pk: getattr(self, self.pk)
        })

        return True
