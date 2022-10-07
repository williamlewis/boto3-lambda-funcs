import boto3

############################
## PART 1 - CREATE IMAGES ##
############################
source_region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=source_region)

instances = ec2.instances.filter(InstanceIds=['i-03842f098199c3f88'])

image_ids = []

# create an image for each instance in filtered list, then include in image_ids list
for instance in instances:
    image = instance.create_image(Name='Demo Boto3 ' + instance.id, Description='Demo Boto' + instance.id)
    image_ids.append(image.id)

print(f'Images to be copied {image_ids}')


##############################################
## PART 2 - WAIT FOR IMAGES TO BE AVAILABLE ##
##############################################

client = boto3.client('ec2', region_name=source_region)
waiter = client.get_waiter('image_available') # get waiter for image_available

# wait for images to be ready before proceeding
waiter.wait(Filters=[{
    'Name': 'image-id',
    'Values': image_ids
}])


###########################################
## PART 3 - COPY IMAGES TO OTHER REGIONS ##
###########################################

destination_region = 'eu-west-2' # define destination region
client = boto3.client('ec2', region_name=destination_region)

# copy each image in image_ids list to destination region
for image_id in image_ids:
    client.copy_image(
        Name=f'Boto3 Copy {image_id}',
        SourceImageId = image_id,
        SourceRegion = source_region
    )
