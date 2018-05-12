import unittest
import os, boto3
from media.s3_storage import S3MediaStorage 
class TestS3Storage(unittest.TestCase):

  def test_it_allow_store_files(self):
    #Arrange
    storage = self.there_is_s3_storage()
    to_be_up = self.there_is_file()
    #Act
    storage.save(
      path="my/test/path.txt",
      to_be_uploaded = to_be_up 
    )
    #Assert
    assert False == storage.contains(path='not-ets')
    assert storage.contains(path='my/test/path.txt')
  
  def there_is_s3_storage(self):
    git_name = os.getenv('APP_BUCKET_NAME')
    s3 = boto3.resource('s3')
    return S3MediaStorage(s3, git_name)
  
  def there_is_file(self):
    pass
