import json

# Dictionary mapping JSON attributes to OCI Terraform attributes
attribute_mapping = {
    'ami': 'image_id',
    'instance_type': 'shape',
    'tags': 'defined_tags',
    # Add more attribute mappings as needed
}

def transform_terraform_file(json_template, terraform_file):
    with open(json_template) as f:
        data = json.load(f)

    with open(terraform_file, 'w') as f:
        # Write OCI provider configuration
        f.write('provider "oci" {\n')
        f.write('  tenancy_ocid     = "YOUR_TENANCY_OCID"\n')
        f.write('  user_ocid        = "YOUR_USER_OCID"\n')
        f.write('  fingerprint      = "YOUR_API_KEY_FINGERPRINT"\n')
        f.write('  private_key_path = "PATH_TO_PRIVATE_KEY"\n')
        f.write('  region           = "YOUR_REGION"\n')
        f.write('}\n\n')

        for resource in data['resources']:
            resource_type = resource['type']
            resource_name = resource['name']
            resource_attributes = resource['attributes']

            # Transform the resource attributes
            transformed_attributes = {}

            for json_attr, oci_attr in attribute_mapping.items():
                if json_attr in resource_attributes:
                    transformed_attributes[oci_attr] = resource_attributes[json_attr]

            # Generate the transformed Terraform resource block
            f.write(f'resource "{resource_type}" "{resource_name}" {{\n')
            for attr, value in transformed_attributes.items():
                f.write(f'  {attr} = "{value}"\n')
            f.write('}\n\n')

# Usage
json_template = 'input.json'
terraform_file = 'output.tf'

transform_terraform_file(json_template, terraform_file)
