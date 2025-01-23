terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.17.0"
    }
  }
}


provider "google" {
  project = "data-experiments-448712"
  region  = "us-central1"
  
}

resource "google_storage_bucket" "experimental_terraform_bucket" {
  name          = "engineering_terraform_bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "Delete"
    }
  }
}

resource "google_bigquery_dataset" "terraform_dataset" {
  dataset_id = "terraform_dataset_example"

}