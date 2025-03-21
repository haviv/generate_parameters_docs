**Technical Name:** TechnicalInformation

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

The TechnicalInformation parameter is designed to capture and provide critical diagnostic and log information related to errors and system operations within the Pathlock Cloud GRC platform. This includes capturing specific error logs, statuses of processes, and notifications related to system anomalies or operational interruptions.

**Business Impact:**

Proper configuration and monitoring of TechnicalInformation are crucial for maintaining system integrity, ensuring compliance, and minimizing operational risks. It aids in quick identification and resolution of errors, which in turn reduces downtime and sustains business continuity. 

**Technical Impact when configured:**

When configured, TechnicalInformation enables administrators and compliance officers to track and diagnose system failures or abnormalities efficiently. It encompasses error logging, notifications of critical messages, and the administration of system-wide identifiers which are pivotal for audit trails and security monitoring.

**Examples Scenario:**

1. A critical system process is canceled unexpectedly, leading to potential security or operational risks. TechnicalInformation captures and logs this event, including details about the authorization objects affected, aiding in swift analysis and remediation.
   
2. An administrator receives a critical message notification indicating a system-wide failure. Utilizing the TechnicalInformation parameter, they can access detailed error logs and system notifications to pinpoint the issue and initiate corrective actions promptly.

**Related Settings:**

- ProfileTailor Dynamics -- Critical Message
- HR source system
- SystemStoppedSubject

**Best Practices:** 

- **Configure when:** Setting up the system for initial use or when modifying the system's operational scope. Regular updates are necessary to ensure all critical systems and processes are monitored.
  
- **Avoid when:** Unnecessary for non-critical informational logging, as excessive logger details may lead to storage and manageability issues.