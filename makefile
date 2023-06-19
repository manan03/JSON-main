.PHONY: download-and-run

download-and-run:
	aws cloudformation get-template --stack-name EC2-STACK --output json > temp1.json && python main.py
