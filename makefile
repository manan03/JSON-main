.PHONY: download-and-run
    
download-and-run:
	aws cloudformation get-template --stack-name ELB-AS-STACK --output json > temp1.json
