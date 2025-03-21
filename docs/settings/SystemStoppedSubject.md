# System Stopped Subject

**Technical Name:** SystemStoppedSubject

**Category:** Audit

**Default Value:** N/A

**Impact Level:** High

**Description:**

This parameter is used to monitor and control the state of the application in scenarios where continuous errors or problematic states are detected. When the configured conditions are met, indicating persistent issues, this triggers the application to halt. This mechanism is crucial for preventing further errors and ensuring the stability and integrity of the system.

**Business Impact:**

Implementing the SystemStoppedSubject parameter effectively helps in mitigating risks associated with system failures. When persistent issues are not promptly addressed, it can lead to system downtime, affecting productivity, data integrity, and potentially causing significant business disruptions. By enabling an automatic stoppage, it ensures that the affected areas can be addressed without incurring additional errors or data corruption.

**Technical Impact when configured:**

When this parameter is configured and activated, it immediately halts the application's processes upon detection of continuous issues, preventing the propagation of errors. This serves as a critical safeguard, ensuring that any underlying problems can be isolated and resolved without affecting the broader system or data integrity.

**Examples Scenario:**

1. *Security Breach Detection:* If the system detects ongoing unauthorized access attempts or security anomalies, the application is stopped to prevent further breach or data leakage.

2. *Data Integrity Issues:* Upon identifying recurring data corruption errors, the application stops to avoid widespread data loss or corruption.

3. *Operational Failures:* In cases of continuous operational failures, like process terminations or service disruptions, the application halts to stabilize the system for troubleshooting.

**Related Settings:**

- ErrorNotificationBody: Configures the content of notification messages sent out when the application is stopped, enabling timely intervention by IT support teams or administrators.

- SyncronizeEmployees: Ensures that operational data concerning employees is current and accurate, excluding terminated employees from active processes to prevent operational inconsistencies.

- SodMitigatedUsersGroupId: Used to maintain a list of user groups with mitigated Segregation of Duties (SoD) conflicts, relevant for audit trails and compliance checks before stopping the application.

**Best Practices:**

- **Timely Review of Logs:** Regularly review server and application logs for errors or warnings that could precede the stopping condition, allowing preemptive action.

- **Configure Sensible Thresholds:** Set up the condition thresholds for stopping the application based on historical data and risk assessment to avoid unnecessary disruptions.

- **Comprehensive Testing:** Ensure thorough testing of the parameter settings in a controlled environment to understand its impact on the application and to fine-tune its configuration.

- **Emergency Procedures:** Establish clear procedures for responding when the application is stopped automatically, including immediate investigation, notification protocols, and steps for recovery.