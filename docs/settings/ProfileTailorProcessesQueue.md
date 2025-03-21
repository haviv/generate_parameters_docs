# Pathlock Processes Queue

**Technical Name:** ProfileTailorProcessesQueue

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:** 

The Pathlock Processes Queue parameter controls the management and prioritization of workflow processes in the Pathlock GRC platform. It ensures that processes are executed in an orderly manner, maintaining system efficiency and reliability.

**Business Impact:** 

By effectively managing the process queue, organizations can ensure that critical GRC tasks such as risk assessments, compliance checks, and audit Trails are performed efficiently, without unnecessary delays. This contributes to a more robust GRC strategy, directly impacting the organization's ability to comply with regulations and manage risks.

**Technical Impact when configured:** 

- Streamlines the execution of queued processes, optimizing system performance.
- Reduces the risk of process execution timeouts or failures due to system overload.
- Ensures that priority workflows are executed in a timely manner, enhancing compliance and risk management efforts.

**Examples Scenario:** 

A company uses the Pathlock GRC platform for managing their compliance with GDPR. The ProfileTailorProcessesQueue parameter is configured to prioritize GDPR risk assessment workflows. This ensures these critical processes are executed first, enhancing the company's ability to maintain compliance and reduce the risk of penalties.

**Related Settings:** 

- DatabaseConnectionSettings.Default.Cloud

**Best Practices:** configure when critical GRC processes must be prioritized to ensure compliance and effective risk management; avoid when all processes have equal priority and system resources are sufficient to manage the workload without prioritization.