import boto3

aws_mag_con = boto3.session.Session(profile_name="root")
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)

s3_con=aws_mag_con.resource('s3')

for each_user_bucket in  s3_con.buckets.all():
    print(each_user_bucket)
