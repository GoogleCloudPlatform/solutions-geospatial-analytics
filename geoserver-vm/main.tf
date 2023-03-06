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

module "gce-container" {
  source = "terraform-google-modules/container-vm/google"
  version = "~> 2.0"

  container = {
    image="gcr.io/bigquery-geotools/geoserver-vm"
  }
}

resource "google_compute_instance" "vm" {
  name = "geoserver-vm"
  machine_type = "e2-standard-4"
  boot_disk {
    initialize_params {
      image = module.gce-container.source_image
    }
  }
  network_interface {
    network = "default"
    access_config {}
  }
  
}
