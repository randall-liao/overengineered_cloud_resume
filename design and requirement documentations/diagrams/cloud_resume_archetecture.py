from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront
from diagrams.aws.network import Route53
from diagrams.aws.security import CertificateManager

OUTPUT_FILE_PATH = "images/cloud_resume"

graph_attr = {
    "fontsize": "16",
}

node_attr = {
    "fontsize": "16",
}

cluster_attr = {
    "fontsize": "16",
    "margin": "20"
}

with Diagram("Cloud Resume", show=True, filename=OUTPUT_FILE_PATH, outformat="png", graph_attr=graph_attr,
             node_attr=node_attr, direction="TB"):
    with Cluster("AWS Cloud", graph_attr=cluster_attr):
        with Cluster("Management Tools", graph_attr=cluster_attr):
            ssl_certificate_manager = CertificateManager("Certificate Manager")
        with Cluster("Region: CA Central", graph_attr=cluster_attr):
            dns_server = Route53("DNS")
            cdn = CloudFront("CDN")
            with Cluster("VPC", graph_attr=cluster_attr):
                with Cluster("AZ 1", graph_attr=cluster_attr):
                    static_website_store = S3("Resume HTML File")
    dns_server >> cdn >> static_website_store
