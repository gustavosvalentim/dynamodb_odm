# import dynamodb_odm.config as config
import dynamodb_odm.schema as schema
import dynamodb_odm.model as model
import dynamodb_odm.fields as fields


# # Map according to botosession config
# config.connection.update({
#     'endpoint_url': None,
#     'profile_name': None
# })


"""
    Default fields:
        created_at
        updated_at
"""
task_schema = schema.Schema(
    id=fields.PrimaryKeyField(fields.UUID4Field()),
    company_id=fields.StringField(),
    client=fields.StringField(),
    has_notes=fields.IntegerField(),
    type=fields.StringField()
)
Task = model.Model('DrumboTestingTasksTable', task_schema)

# Create new task
# task_doc = Task.create(
#     company_id='Westpoint',
#     client='Mariana',
#     has_notes=0,
#     type='VAT'
# )
# task_doc.save()

# # Get task
# Task.get('Someid')

# # Get all
# Task.scan()

# Filter values
tasks = Task.scan(Task.company_id.eq('Westpoint') & Task.client.contains('A'))
print(tasks)