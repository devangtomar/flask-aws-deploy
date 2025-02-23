resource "aws_vpc" "flask_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "flask_subnet" {
  vpc_id            = aws_vpc.flask_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "ap-south-1a"
}

resource "aws_security_group" "flask_sg" {
  vpc_id = aws_vpc.flask_vpc.id

  ingress {
    from_port   = 8090
    to_port     = 8090
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
