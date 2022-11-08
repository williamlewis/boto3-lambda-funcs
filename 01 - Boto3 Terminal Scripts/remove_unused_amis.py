import boto3
ec2 = boto3.client('ec2')

instances = ec2.describe_instances()
used_amis = []

# find images used by current EC2 instances
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])

# remove duplicate values from list of used_amis
unique_amis = list(set(used_amis))

# get custom AMIs from the account
custom_images = ec2.describe_instances(
    Filters=[{
        'Name': 'state',
        'Values': ['available']
    }],
    Onwers=['self']
)

custom_amis_list = []
for image in custom_images['Images']:
    custom_amis_list.append(image['ImageId'])


# compare list of custom amis to list of amis in use, to delete custom amis that are not in use
for ami_id in custom_amis_list:
    if ami_id not in unique_amis:
        print(f'Deleting image {ami_id}')
        ec2.deregister_image(ImageId=ami_id)
