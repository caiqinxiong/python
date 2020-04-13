from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDkKivthxfrwlKflCKo6AzYzC9rJbnwX5P'  # 替换为用户的 secretId
secret_key = 'HIepnWzGJ6d1PcZFiwvd7PTKwKUNG0Zu'  # 替换为用户的 secretKey

region = 'ap-chengdu'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.create_bucket(
    Bucket='test-1301483313',
    ACL="public-read"  #  private  /  public-read / public-read-write
)