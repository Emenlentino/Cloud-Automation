provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "bucket" {
  bucket = "my-cloud-automation-bucket"
  acl    = "private"
}
