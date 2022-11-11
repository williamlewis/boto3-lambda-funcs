## Hands-on projects to automate actions in AWS using Boto3 Python SDK
<br/>
<br/>

**Boto3 is the Python-based SDK for Amazon Web Services, enabling programmatic control services.**

*Course: Mastering Boto3 and Lambda Functions Using Python (Udemy)*

*Instructor: Hari Kammana*

<br/>
<br/>


# Part 1: Boto3 for Lambda Functions
Using Boto3 within Lambda Functions to manage S3, DynamoDB, CloudWatch, EC2, AMIs, SNS, & SES


<table>
    <thead>
        <tr>
            <th>Description</th>
            <th>Services Used</th>
            <th>Link ↗</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td width="60%">Find unused Elastic IPs and send alert email using SES and Lambda environmental variables</td>
            <td width="20%"><code>Lambda</code> <code>EC2</code> <code>SES</code></td>
            <td width="20%" ><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/find_and_email_unused_eips.py">find and email unused eips.py</a></td>
        </tr>
        <tr>
            <td width="60%">Detect unattached EBS volumes and send alert email using SNS</td>
            <td width="20%"><code>Lambda</code> <code>EC2</code> <code>SNS</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/unused_volumes.py">unused volumes.py</a></td>
        </tr>
        <tr>
            <td width="60%">Persist CSV data to DynamoDB when file is uploaded to an S3 bucket</td>
            <td width="20%"><code>Lambda</code> <code>S3</code> <code>DynamoDB</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/s3_csv_to_dynamodb.py">s3 csv to dynamodb.py</a></td>
        </tr>
        <tr>
            <td width="60%">Persist JSON data to DynamoDB when S3 file upload triggers a CloudWatch log event</td>
            <td width="20%"><code>Lambda</code> <code>S3</code> <code>DynamoDB</code> <code>CloudWatchLogs</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/s3_json_to_dynamodb.py">s3 json to dynamodb.py</a></td>
        </tr>
        <tr>
            <td width="60%">Send Slack message via webhook to alert when an instance has stopped</td>
            <td width="20%"><code>Lambda</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/slack_alert.py">slack alert.py</a></td>
        </tr>
    </tbody>
</table>

<br/>
<br/>

# Part 2: Boto3 Terminal Scripts
Using Boto3 Terminal Scripts to manage EC2 Instances, EBS Volumes, & AMIs


<table>
    <thead>
        <tr>
            <th>Description</th>
            <th>Services Used</th>
            <th>Link ↗</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td width="60%">Query contents of CSV file stored in S3</td>
            <td width="20%"><code>S3</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/s3_query_csv_select_object_content.py">s3 query csv select object content.py</a></td>
        </tr>
        <tr>
            <td width="60%">Batch write data to DynamoDB table</td>
            <td width="20%"><code>DynamoDB</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/dynamobd_batch_write.py">dynamobd batch write.py</a></td>
        </tr>
        <tr>
            <td width="60%">Get and delete items from DynamoDB table</td>
            <td width="20%"><code>DynamoDB</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/dynamobd_get_and_delete.py">dynamobd get and delete.py</a></td>
        </tr>
        <tr>
            <td width="60%">Email list of EBS Snapshots based on tags</td>
            <td width="20%"><code>EC2</code> <code>SNS</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/ebs_snapshots_email.py">ebs snapshots email.py</a></td>
        </tr>
        <tr>
            <td width="60%">Create AMI & copy to another region</td>
            <td width="20%"><code>EC2</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/create_image_copy_to_diff_region.py">create image copy to diff region.py</a></td>
        </tr>
        <tr>
            <td width="60%">Describe instances and related attributes</td>
            <td width="20%"><code>EC2</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/describe_instances.py">describe instances.py</a></td>
        </tr>
        <tr>
            <td width="60%">Filter & manage instances using EC2 resource collections</td>
            <td width="20%"><code>EC2</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/ec2_collections.py">ec2 collections.py</a></td>
        </tr>
        <tr>
            <td width="60%">Launch new intances based on AMI & instance type</td>
            <td width="20%"><code>EC2</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/launch_ec2.py">launch ec2.py</a></td>
        </tr>
        <tr>
            <td width="60%">Delete EBS snapshots older than 15 days</td>
            <td width="20%"><code>EC2</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/remove_old_ebs_snapshots.py">remove old ebs snapshots.py</a></td>
        </tr>
        <tr>
            <td width="60%">Deregister unused custom AMIs</td>
            <td width="20%"><code>EC2</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/remove_unused_amis.py">remove unused amis.py</a></td>
        </tr>
        <tr>
            <td width="60%">Start, stop, & terminate instances based in Id</td>
            <td width="20%"><code>EC2</code></td>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/sec_start_stop_terminate.py">sec start stop terminate.py</a></td>
        </tr>
    </tbody>
</table>
