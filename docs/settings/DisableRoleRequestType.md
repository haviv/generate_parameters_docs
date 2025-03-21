# Disable Role Request Type

**Technical Name:** DisableRoleRequestType

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Disable Role Request Type parameter is configured to enable or disable role request types within the Pathlock Cloud GRC platform. This affects how users interact with role requests, potentially restricting or allowing certain types of requests based on organizational policy.

**Business Impact:**

Enabling or disabling specific role request types can directly influence the organization's security posture and compliance with internal or external policies. It determines the flexibility and restrictions placed on users requesting access to different system roles, impacting efficiency and access control.

**Technical Impact: when configured**

When this parameter is configured to disable certain role request types, users may be restricted from requesting access to specific roles within the system. This can be used as a control mechanism to ensure that access is granted based on necessity and compliance, reducing the risk of unauthorized access.

**Examples Scenario:**

An organization identifies that certain roles within their system should not be requested freely by users due to their sensitive nature. To mitigate the risk, they utilize the Disable Role Request Type parameter to prevent these roles from being requested, thus ensuring that only designated administrators can assign these roles directly.

**Related Settings:**

- DirectExectionOfProgramsLogOnlyHighRiskEvents
- DefaultReportRunMode

**Best Practices:** 

- **Configure when:** Specific roles require tight control and should not be available for open request due to their access level or sensitivity.
  
- **Avoid when:** Role request flexibility is essential for business operations, and all roles can safely be requested by users through the normal workflow process.