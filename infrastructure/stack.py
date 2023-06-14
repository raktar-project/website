from aws_cdk import Stack
from pathlib import Path

from static_site import StaticSite


CONTENTS_PATH = Path.cwd().parent / "site"


class StaticWebsiteStack(Stack):
    def __init__(self, scope, _id):
        super().__init__(scope, _id)

        site_domain_name = "raktar.io"
        hosted_zone_id = "Z09595212ITJVLFTDQCA4"
        hosted_zone_name = "raktar.io"
        domain_certificate_arn = "arn:aws:acm:us-east-1:156105759311:certificate/e7cfbbac-1fe0-4021-b2e1-a3665af53cb1"

        site = StaticSite(
            scope=self,
            construct_id="StaticSite",
            site_domain_name=site_domain_name,
            hosted_zone_id=hosted_zone_id,
            hosted_zone_name=hosted_zone_name,
            domain_certificate_arn=domain_certificate_arn,
        )
        site.deploy(CONTENTS_PATH.as_posix())
