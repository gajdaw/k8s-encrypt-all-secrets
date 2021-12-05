# k8s encrypt all secrets

Install deps:

    pip3 install -r requirements.txt

Run:

    ./main.py

To fetch all secrets from K8s first authorize in k8s and then run:

    ./main.py fetch

The secrets are stored in `secret/` dir and can be encrypted with:

    ./main.py encrypt someone@example.net

To decrypt secrets type:

    ./main.py decrypt
