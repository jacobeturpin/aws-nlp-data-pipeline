aws cloudformation create-stack --stack-name test \
    --template-body file://stack.yml \
    --parameters ParameterKey=LogBucketName,ParameterValue=mybucketname \
                 ParameterKey=ElasticsearchDomainName,ParameterValue=esdomainname \
                 ParameterKey=ElasticsearchIndexName,ParameterValue=test \
                 ParameterKey=FirehoseName,ParameterValue=myirehosename \
    --capabilities CAPABILITY_NAMED_IAM
