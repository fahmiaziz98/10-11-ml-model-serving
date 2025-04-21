# Deploy ML Model to Production Grade
Buat Instance baru di EC2, bisa pilih t2.medium, namun karena keterbatasan sumber daya hanya pake t2.micro. Berikut spesifikasinya:

    - t2.micro
    - 30GB Storage
    - Image Ubuntu
    - Add S3 Policy to EC2

- Setup EC2 di video no 122
- Login via SSH dan Vscode
    - buat folder mlops-prods
    - buat SSH Baru
        - https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
        - https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
    - Clone repo via SSH
    - Ubah port untuk api ke 8502 dan client 8501 hostt ke 0.0.0.0
    - downgrade py ke 3.11

