from django.test import TestCase


class HealthCheckTestCaseModule(TestCase):
    def test_health_check(self) -> None:
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
