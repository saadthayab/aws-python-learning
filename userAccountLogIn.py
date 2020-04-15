#interacted with service as defalut and Dev 

# now since i do have a defualut user in .aws created i dont need to spicifed the profile
import boto3
iam_con_re = boto3.resource(service_name='iam',region_name="us-east-1")
for each_user in iam_con_re.users.all():
    print(each_user.name)

# now going to use a profile
print("\n")
print (" now using saad profile")
print("\n")

aws_mag_con_root = boto3.session.Session(profile_name="SaadLearningPython") # first just create session first.
iam_con_saadProfile = aws_mag_con_root.resource(service_name='iam',region_name="us-east-1")
for each_user in iam_con_saadProfile.users.all():
    print(each_user.name)
