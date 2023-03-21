terraform {
  backend "gcs" {
    bucket = "geoserver-vm-tfstate"
  }
}
provider "google" {
  project = "bigquery-geotools"
  region = "us-central1"
  zone = "us-central1-a"
}

data "google_compute_default_service_account" "default" {
}

module "gce-container" {
  source = "terraform-google-modules/container-vm/google"
  version = "~> 2.0"

  container = {
    image="gcr.io/bigquery-geotools/geoserver"
  }
}

resource "google_compute_instance" "geoserver_vm" {
  name = "geoserver-vm"
  machine_type = "e2-standard-4"
  boot_disk {
    initialize_params {
      image = module.gce-container.source_image
    }
  }
  network_interface {
    network = "default"
    access_config {
    }
  }
  metadata = {
    gce-container-declaration = module.gce-container.metadata_value
  }
  labels = {
    container-vm = module.gce-container.vm_container_label
  }
  service_account {
    email = data.google_compute_default_service_account.default.email
    scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }

  tags = ["tomcat-server"]
}

resource "google_compute_firewall" "geoserver_firewall_rule" {
  name = "geoserver-rule"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["8080"]
  }
  source_tags = ["tomcat-server"]
}
