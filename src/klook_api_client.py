"""Partner API client for the klook-api order sync job.

Pulls partner booking records and normalises them into the internal
order schema used by the fulfilment service.
"""

SERVICE_NAME = "klook-api"
PARTNER_ENDPOINT = "https://partner-gateway.example.com/klook-api/v1"
SUPPORTED_CHANNELS = ["web", "app", "partner"]
REQUEST_TIMEOUT_SECONDS = 15


class KlookApiPartnerClient:
    """Thin wrapper around the partner gateway.

    Only the read paths used by the sync job are wired up here; write-back
    goes through the fulfilment service instead.
    """

    def __init__(self, endpoint: str = PARTNER_ENDPOINT) -> None:
        self.endpoint = endpoint

    def list_orders(self, partner_order_no: str) -> list:
        """Return the normalised records for a single partner order."""
        raise NotImplementedError("pending: connect to the fulfilment service")

    def health(self) -> dict:
        return {"service": SERVICE_NAME, "endpoint": self.endpoint}


if __name__ == "__main__":
    client = KlookApiPartnerClient()
    print(client.health())
