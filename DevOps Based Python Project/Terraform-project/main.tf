provider "aws" {
  region = var.aws_region
}

# VPC
resource "aws_vpc" "main_vpc" {

  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "Ravi-VPC"
  }
}

# Public Subnet
resource "aws_subnet" "public_subnet" {

  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "Ravi-Public-Subnet"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main_igw" {

  vpc_id = aws_vpc.main_vpc.id

  tags = {
    Name = "Ravi-IGW"
  }
}

# Route Table
resource "aws_route_table" "public_rt" {

  vpc_id = aws_vpc.main_vpc.id

  route {

    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main_igw.id
  }

  tags = {
    Name = "Ravi-Public-RT"
  }
}

# Route Table Association
resource "aws_route_table_association" "public_subnet_assoc" {

  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

# Security Group
resource "aws_security_group" "main_sg" {

  name   = "ravi-sg"
  vpc_id = aws_vpc.main_vpc.id

  ingress {

    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {

    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Key Pair
resource "aws_key_pair" "deployer" {

  key_name = "ravi-key"

  public_key = file("terraform-key.pub")
}

# EC2 Instance
resource "aws_instance" "my_ec2" {

  ami           = var.ami_id
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id

  vpc_security_group_ids = [
    aws_security_group.main_sg.id
  ]

  key_name = aws_key_pair.deployer.key_name

  tags = {
    Name = "Ravi-EC2"
  }
}
