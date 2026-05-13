# DevOps Based Python Project

This folder contains small DevOps-focused Python and Terraform projects for system monitoring, AWS S3 backups, a Flask monitoring dashboard, and AWS infrastructure automation.

## Projects

### DevOps System Monitoring Project

`DevOps System Monitoring Project/DevOpsSystemMonitoring.py`

Runs as a simple monitoring script that:

- Shows running processes.
- Tracks CPU, memory, and disk usage.
- Writes monitoring logs to `system_monitor.log`.
- Logs a warning when CPU usage is high.

Run it with:

```powershell
python "DevOps System Monitoring Project/DevOpsSystemMonitoring.py"
```

### System Monitoring Flask Application

`System Monitoring Flask Application/app.py`

Starts a Flask dashboard that displays:

- Hostname.
- Operating system and release.
- CPU usage.
- Memory usage.
- Disk usage.
- System boot time.

Run it with:

```powershell
pip install flask psutil
python "System Monitoring Flask Application/app.py"
```

Then open:

```text
http://127.0.0.1:5000
```

### AWS Python Project

`AWS python project/`

Contains scripts for working with AWS S3:

- `s3_backup.py`: lists, creates, and deletes S3 buckets.
- `monitor_and_backup_in_s3.py`: collects system metrics, saves a report, creates an S3 bucket if needed, and uploads the report.

Before running these scripts, configure AWS credentials locally using the AWS CLI, environment variables, or an AWS profile.

Install dependencies:

```powershell
pip install boto3 psutil
```

Run a script:

```powershell
python "AWS python project/s3_backup.py"
python "AWS python project/monitor_and_backup_in_s3.py"
```

### Terraform Project

`Terraform-project/`

Contains Terraform configuration for AWS infrastructure:

- VPC.
- Public subnet.
- Internet gateway.
- Route table and association.
- Security group.
- EC2 key pair.
- EC2 instance.

Create a local Terraform variables file from the example:

```powershell
Copy-Item "Terraform-project/terraform.tfvars.example" "Terraform-project/terraform.tfvars"
```

Edit `terraform.tfvars` with your own values, then run:

```powershell
cd "Terraform-project"
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

You can also use the Python automation script:

```powershell
python deploy.py
```

## What Not To Push

The `.gitignore` keeps local and sensitive files out of Git, including:

- Virtual environments such as `.venv/`.
- Python cache files such as `__pycache__/`.
- Log files and generated monitoring reports.
- Terraform state, plans, `.terraform/`, and real `terraform.tfvars`.
- Private keys and certificate files.

Keep secrets, AWS credentials, Terraform state, and generated files local only.
