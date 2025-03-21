# Pathlock Worker Process Server

**Technical Name:** ProfileTailorWorkerProcessServer

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter configures the server that will handle worker processes for the Pathlock platform, relating to the ProfileTailor suite.

**Business Impact:** Proper configuration ensures efficient processing of GRC tasks related to security, risk, and compliance. Misconfiguration could lead to delayed or unprocessed tasks, affecting the organization's ability to maintain desired security and compliance standards.

**Technical Impact when configured:** Determines the efficiency and reliability of background tasks processing, impacting the overall performance and responsiveness of the ProfileTailor functionalities within the Pathlock GRC platform.

**Example Scenario:** If an organization needs to prioritize high-efficiency processing for compliance checks and risk assessment tasks, configuring the `ProfileTailorWorkerProcessServer` to point to a high-capacity, low-latency server can significantly improve task processing times and system responsiveness.

**Related Settings:** RiskTypesKeywordsForRiskApprovalStep

**Best Practices:** Configure when a dedicated server is available for worker processes to ensure optimal processing times. Avoid when the server's resources are already stretched thin, as this can lead to performance bottlenecks.