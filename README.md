# EndToEndRAGApplication_AmazonBedrock

## How to run?

```bash
conda create -p bedrock python==3.10 -y
```

```bash
conda activate bedrock
```

```bash
pip install -r requirements.txt
```

### Install aws cli from following link
```bash
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```
### Add credentials by running below command
```bash
aws configure
```

### To run streamlit app
```bash
streamlit run bedrock_text.py
```

```bash
streamlit run rag_demo.py
```