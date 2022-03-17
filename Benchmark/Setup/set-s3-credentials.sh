echo "Access Key:"
read -sr access_key

echo "Secret Key:"
read -sr secret_key

export AWS_ACCESS_KEY_ID="${access_key}"
export AWS_SECRET_ACCESS_KEY="${secret_key}"
export AWS_DEFAULT_REGION='fr-repl'
export RCLONE_S3_REGION="${AWS_DEFAULT_REGION}"
export RCLONE_S3_LOCATION_CONSTRAINT="${AWS_DEFAULT_REGION}"
alias aws='aws --endpoint-url https://s3.bwsfs.uni-freiburg.de/'

unset access_key
unset secret_key
