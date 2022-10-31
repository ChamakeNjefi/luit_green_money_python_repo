#Create a list of AWS Services

# 1. The list should be empty initially

aws_services = []

# 2. Populate the list using append or insert

aws_services.append('EC2')
aws_services.append('ECS')
aws_services.append('EKS')
aws_services.append('ECR')
aws_services.append('S3')
aws_services.append('Lambda')
aws_services.append('DynamoDB')
aws_services.append('CloudFront')
aws_services.append('CloudFormation')
aws_services.append('SNS')

# 3. Print the list and the length of the list

print(aws_services)

print(len(aws_services))

# 4. Remove two specific services from the list by name or by index

del aws_services[5]
del aws_services[6]

# 5. Print the new list and the new length of the list

print(aws_services)

print(len(aws_services))







