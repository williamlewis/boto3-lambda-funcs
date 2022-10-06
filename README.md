# Mastering Boto3 and Lambda Functions Using Python
Hands-on projects using Boto3 Python SDK for AWS


Instructor:  Hari Kammana

Platform:  Udemy


--

## Course Outline

- Managing EC2 Services & EBS Snapshots
    - **Launching EC2 Instances**
        - create and launch new EC2 instances using `EC2.Client` class and `.run_instances()` method
        - provided inputs:  AMI ImageId, Min. / Max. number of instances

    - **Operations on EC2**
        - start, stop, and terminate existing EC2 isntances using `EC2.Client` class and `.start_instances()`, `.stop_instances()`, and `.terminate_instances()` methods
        - provided inputs:  InstanceId (list of Ids if multiple)

    - **Filtering & Describing EC2 Instances**
        - filter instances and display selected attributes using `EC2.Client` class and `.describe_instances()` method
        - provided inputs:  instance tag key/value pairs, attributes to describe

    - **Boto3 Collections**
        - find and stop instances in a "running" state using `EC2.ServiceResource` class and `.stop()` method
        - provided inputs:  current instance state
    
    - **Taking EBS Snapshots & Sending Email Notifications**
        - take a snapshot of EBS volumes for a filtered selection of EC2 instances, using `EC2.ServiceResource` class
        - publish an email message noting all Snapshot Ids using `SNS.Client` class and `.publish()` method
        - provided inputs:  instance tag key/value pairs, snapshot description, SNS message, SNS TopicArn, SNS email subject

    - **Deleting EBS Snapshots Older than X Days**
    - **Migrating AMIs to Different Regions Using Boto3 Waiters**








- AWS Lambda - Develop Real-Time Use Cases
- Boto3 & DynamoDB
- Operations on S3
- Cost Optimization


<br/>
<br/>
<br/>

---
- TEST Table Format

    |   SECTION (CODE SAMPLE)   |   ACTION  |   CLASSES USED    |   METHODS USED    |   INPUTS  |   PERFOMED VIA CONSOLE
    |---|---|---|---|---|---|
    |**Launching EC2 Instances**| create and launch new EC2 instances | `EC2.Client` | `.run_instances()` | AMI `ImageId`, Min. & Max. number of instances | None
    |**Operations on EC2**|
    |**Filtering & Describing EC2 Instances**|
    |**Boto3 Collections**|
    |**Taking EBS Snapshots & Sending Email Notifications**|
    |**Deleting EBS Snapshots Older than X Days**|
    |**Migrating AMIs to Different Regions Using Boto3 Waiters**|
