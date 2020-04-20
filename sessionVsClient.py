#session vs client
# first need to import the boto3 lib before start working
import boto3

aws_mag_con_root = boto3.session.Session(profile_name="root") # first just create session first.
print (dir(aws_mag_con_root))   # list operation avalialble to the session object
# we can creat any object from the execution of the dir. any object, like get avaialble res
# client, resources,...
print("\n")
# the below will print out what we cah do only using rescources 
# iam_con_re=aws_mag_con_root.resource(service_name='iam',region_name="us-east-2")
# theses are the services ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
print (aws_mag_con_root.get_available_resources())
#Listiing iam users with resource object:
iam_con_re=aws_mag_con_root.resource(service_name='iam',region_name="us-east-2")
for each_user in iam_con_re.users.all():
    print(each_user.name)

########################################
# The client will have ability to perform as user on consoul fully not like the rescourse limitedt
# also resourse return object While client return the class/ dictionary

iam_con_client=aws_mag_con_root.client(service_name='iam',region_name="us-east-2")
print (iam_con_client.list_users())
#Listing iam users with client object:

print("\n here is the output from client")
for each in iam_con_client.list_users()['Users']:
    print(each['UserName'])

# if we want to use the default profile then we dont need to specfy the 
#aws_mag_con_root = boto3.session.Session(profile_name="root") # first just create session first.
# we can use directly the resource 
iam_con_re=boto3.resource(service_name="iam",region_name="us-east-1")


""" 
# by using the roow profile

iam_con_re=aws_mag_con_root.resource(service_name='iam',region_name="us-east-2")

iam_con_client=aws_mag_con_root.client(service_name='iam',region_name="us-east-2")

#Listiing iam users with resource object:

for each_user in iam_con_re.users.all():
    print(each_user.name)

#Listing iam users with client object:

for each in iam_con_client.list_users()['Users']:
   print(each['UserName'])


"""
