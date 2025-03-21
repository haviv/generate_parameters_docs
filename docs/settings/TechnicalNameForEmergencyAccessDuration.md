**Technical Name: TechnicalNameForEmergencyAccessDuration**

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:** 

This parameter defines the duration for which emergency access is granted within the Pathlock Cloud GRC platform's workflow processes. It specifically applies to the StartStep action of a workflow, setting a time limit for temporary permissions or access rights granted in urgent scenarios.

**Business Impact:**

Setting an appropriate duration for emergency access is crucial for maintaining the integrity of security protocols within an organization. It ensures that temporary access rights are not left open indefinitely, reducing the potential for unauthorized access and compliance issues.

**Technical Impact when configured:**

When this parameter is configured, it directly influences the lifecycle of emergency access permissions. By defining a fixed timeframe, it ensures that elevated access rights automatically expire, reverting the user's permissions back to their standard level without manual intervention.

**Example Scenario:**

An organization needs to grant temporary access to a sensitive system for a contractor to perform an urgent fix. By using the TechnicalNameForEmergencyAccessDuration parameter, the organization can ensure that the contractor's access rights are automatically revoked once the specified duration elapses, without needing to manually remove the permissions.

**Related Settings:** N/A

**Best Practices:** 

- **Configure when:** Immediate, temporary access is required for a user or group to address an urgent issue within a secure environment. Setting a precise duration minimizes the risk associated with open-ended access.
  
- **Avoid when:** Standard, non-emergency processes and access management practices suffice. Emergency access durations should not be used as a workaround for regular access management procedures.