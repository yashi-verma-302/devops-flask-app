provider "local" {}

resource "local_file" "hello" {
  content  = "This is a placeholder for Terraform provisioning."
  filename = "${path.module}/hello.txt"
}
