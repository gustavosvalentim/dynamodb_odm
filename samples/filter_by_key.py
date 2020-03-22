import dynamodb_odm.schema as schema
import dynamodb_odm.model as model
import dynamodb_odm.fields as fields


task_schema = schema.Schema(
    id=fields.PrimaryKeyField(fields.UUID4Field()),
    client=fields.StringField()
)
Task = model.Model('DrumboTestingTasksTable', task_schema)
collection = Task.collect()
cs_collection = collection.key('type').eq('CS')

print([doc.to_dict() for doc in cs_collection])