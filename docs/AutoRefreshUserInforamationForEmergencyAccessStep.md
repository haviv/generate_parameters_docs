# Auto Refresh User Information For Emergency Access Step

**Technical Name:** AutoRefreshUserInforamationForEmergencyAccessStep

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter controls the functionality for automatically refreshing user information during the emergency access workflow step. It is essential in situations requiring immediate access under emergency conditions, ensuring that user information is up-to-date and accurate before access is granted.

**Business Impact:**

Implementing AutoRefreshUserInformationForEmergencyAccessStep significantly impacts how swiftly and securely emergency access is granted to users. In scenarios where access rights are critical, and time-sensitive, this feature ensures that the access provided is based on the latest user information, thereby mitigating potential security risks associated with outdated data.

**Technical Impact when configured:**

When enabled, this parameter automates the process of updating user data right before the emergency access step is executed. It interacts with the system connector to initiate a trace for emergency access, using updated information such as the user's SAP UserName and the specific details concerning the workflow instance. This automatic refresh process guarantees that any access rights assigned during the emergency step are accurately aligned with the user's current role and privileges.

**Examples Scenario:**

A scenario where this parameter is critical is during an operational incident requiring immediate system access by a support engineer. By ensuring that the user's information and access rights are updated automatically, the platform can quickly provide the necessary access without compromising security by relying on outdated data.

**Related Settings:** 

- StepAutomaticApprovalOn
- WorkflowInstanceId

**Best Practices:** 

- **Configure when:** Immediate and accurate user information is critical for granting emergency access, especially in scenarios where access rights and privileges might have changed recently.
- **Avoid when:** There is confidence that user information does not change frequently, or there are specific reasons to manually review and approve user information before emergency access is granted.
