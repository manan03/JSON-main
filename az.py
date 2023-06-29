from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()

subscription_id = "<7610b97a-a371-4329-86c2-a38755ea8c88>"
resource_client = ResourceManagementClient(credential, subscription_id)

resource_group_name = "<Manan>"
deployment_name = "<MANAN>"

deployment = resource_client.deployments.get(resource_group_name, deployment_name)
template = deployment.properties.template

output_directory = "<manparih@manparih-mac JSON-main>"
output_path = f"{output_directory}/{deployment_name}_template.json"

with open(output_path, "w") as file:
    file.write(template)
