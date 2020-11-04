aws cloudformation create-stack --stack-name test \
    --template-body file://storage-stack.yml \
    --parameters ParameterKey=LogBucketName,ParameterValue=mybucketname \
                 ParameterKey=ElasticsearchDomainName,ParameterValue=esdomainname \
                 ParameterKey=ElasticsearchIndexName,ParameterValue=test \
                 ParameterKey=FirehoseName,ParameterValue=myirehosename \
    --capabilities CAPABILITY_NAMED_IAM
