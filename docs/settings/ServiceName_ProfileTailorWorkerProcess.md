# Service Name Pathlock Worker Process

**Technical Name:** ServiceName_ProfileTailorWorkerProcess

**Category:** Configuration

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

Configures the Pathlock Worker Process for Profile Tailor Dynamics, primarily responsible for processing server discrepancies and general notifications within the Pathlock Cloud GRC platform.

**Business Impact:**

Proper configuration of this parameter ensures timely and accurate handling of server discrepancies and essential communications via email, directly impacting the organization's ability to manage security, risk, and compliance effectively. It supports operational efficiency and ensures compliance functions are aware of and can react to system discrepancies in a timely manner.

**Technical Impact when configured:**

When correctly configured, it enables the Pathlock platform to process and manage server discrepancies and notifications efficiently. This ensures that all discrepancies are logged, tracked, and notified as per the organization’s policy, supporting compliance and risk management practices.

**Example Scenario:**

If an organization needs to ensure that any discrepancies detected by the system are quickly communicated to the compliance and IT team, the ServiceName_ProfileTailorWorkerProcess can be configured to manage these notifications efficiently. For instance, setting up this service to run at a specific interval could help with real-time detection and reporting of system discrepancies, supporting swift action.

**Related Settings:** 

- `ServerDiscrepancyNotInPTD`
- `NotifyAuthorizationReviewWillStartTemplateId`
- `ExistingStringPattern`

**Best Practices:** 

- **Configure When:** You need to ensure that system discrepancies and notifications are managed effectively, supporting your organization's compliance and risk management processes.
- **Avoid When:** If your organization does not use Profile Tailor Dynamics for managing compliance and server discrepancies, configuring this service might not be necessary.