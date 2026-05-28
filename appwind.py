import boto3

# Create EC2 client
ec2 = boto3.resource(
    'ec2',
    region_name='us-east-1'
)

# Launch EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-pair-name'
)

instance = instances[0]

print("Launching instance...")
print("Instance ID:", instance.id)

# Wait until running
instance.wait_until_running()

# Reload instance attributes
instance.reload()

print("Instance is running")
print("Public IP:", instance.public_ip_address) 