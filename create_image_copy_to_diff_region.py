from tkinter import image_names
import boto3

#### PART 1 - CREATE IMAGES
source_region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=source_region)

instances = ec2.instances.filter(InstanceIds=['i-03842f098199c3f88'])

image_ids = []

for instance in instances:
    image = instance.create_image(Name='Demo Boto3 - ' + instance.id, Description='Demo Boto' + instance.id)
    image_ids.append(image.id)

print(f'Images to be copied {image_ids}')


#### PART 2 - WAIT FOR IMAGES TO BE AVAILABLE



#### PART 3 - COPY IMAGES TO OTHER REGIONS
