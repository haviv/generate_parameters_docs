# PTDM Worker Process Path

**Technical Name:** PTDM_WorkerProcessPath

**Category:** Configuration

**Default Value:** net.pipe://127.0.0.1/Pipe/ServiceConfigurationTester

**Impact Level:** Medium

**Description:**

The PTDM_WorkerProcessPath parameter configures the communication endpoint for services and processes within the Pathlock GRC environment. It defines how automated processes and services, like those responsible for mass data uploads or integration tests, connect to and interact with other components of the Pathlock Cloud system.

**Business Impact:**

Proper configuration of this setting ensures efficient and secure communication between the platform's services, supporting the reliability and performance of the Pathlock system. Incorrect settings could lead to failures in automation, impacting compliance workflows, data integrity, and system audits.

**Technical Impact when configured:**

- **Correct Configuration:** Ensures seamless integration and communication between Pathlock services, supporting automation, testing, and operational processes without interruption.
- **Incorrect Configuration:** May lead to disconnection or communication failures among services, causing process interruptions, failures in automation execution, and potential data inconsistency.

**Examples Scenario:**

1. **Mass Data Upload:** An organization wishes to upload a large volume of compliance data. The PTDM_WorkerProcessPath is configured to ensure the mass upload service communicates efficiently with the Pathlock Cloud, ensuring data integrity and upload success.

2. **Integration Testing:** A developer is implementing new compliance checks and needs to run integration tests. Correctly configuring the PTDM_WorkerProcessPath ensures that the test services can properly communicate with the Cloud services, leading to successful test completion.

**Related Settings:** ServiceConfigurationTester

**Best Practices:** 

- **Configure when:** Setting up mass upload processes, integration testing, or any other service requiring inter-process communication within the Pathlock Cloud.
- **Avoid when:** The default communication paths or protocols are sufficient for the organization's operational needs and security requirements.