import botocore

class S3MediaStorage:
  
  def __init__(self, s3, git_name):
    self.s3 = s3
    self.git_name = git_name

  def save(self, path, to_be_uploaded):
    bucket = self.s3.Bucket(self.git_name)
    bucket.put_object(Key=path, Body=to_be_uploaded)
  
  def contains(self, path):
    try:
      s3.Object(self.git_name, path).load()
      return True
    except botocore.exceptions.ClientError as e:
      return False
