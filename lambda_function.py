import boto3

def upload_to_s3(local_file_path, s3_bucket, s3_file_path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3_bucket)
    with open(local_file_path, "rb") as f:
        bucket.put_object(Key=s3_file_path, Body=f)

# Exemplo de como chamar a função de upload
upload_to_s3('arquivo.txt', 'lambda-pythonn', 'lambda-pythonn/teste/arquivo.txt')
