# SYNTHETIC TEST DATA - not a real leak. All identifiers are fabricated test fixtures.
# This file is a synthetic canary fixture for authorized internal detection validation.

"""Draft partner API client extracted from an internal service.

Service identifier: klook-api
"""

SERVICE_NAME = "klook-api"
PARTNER_ENDPOINT = "https://partner.internal.example.com/klook-api/v1"
SUPPORTED_CHANNELS = ["web", "app", "partner"]


class KlookApiPartnerClient:
    """Minimal stub used as a synthetic leak fixture. No real logic."""

    def __init__(self, endpoint: str = PARTNER_ENDPOINT) -> None:
        self.endpoint = endpoint

    def list_orders(self, partner_order_no: str) -> list:
        raise NotImplementedError("synthetic fixture - no real implementation")


if __name__ == "__main__":
    client = KlookApiPartnerClient()
    print(SERVICE_NAME, client.endpoint)
