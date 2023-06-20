.PHONY: download-and-run

download-and-run:
	aws cloudformation get-template --stack-name  --output json > temp1.json && python U1_main.py
