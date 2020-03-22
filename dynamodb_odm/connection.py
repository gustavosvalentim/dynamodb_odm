import boto3


class DynamodbConnection:
    ddb = None

    @classmethod
    def use(cls, table_name):
        return cls.ddb.Table(table_name)

    @classmethod
    def factory(cls, profile_name=None, region_name=None, endpoint_url=None):
        session = boto3.Session(region_name=region_name, profile_name=profile_name)
        ddb = session.resource('dynamodb', endpoint_url=endpoint_url)

        cls.ddb = ddb

        return cls


dynamodb = DynamodbConnection.factory()