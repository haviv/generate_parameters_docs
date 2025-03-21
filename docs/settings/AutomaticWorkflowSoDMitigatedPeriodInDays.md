# Automatic Workflow SoD Mitigated Period In Days

**Technical Name:** AutomaticWorkflowSoDMitigatedPeriodInDays

**Category:** Workflow

**Default Value:** (Not provided in the code references)

**Impact Level:** Medium

**Description:**

This parameter is designed to define the period, in days, during which segregation of duties (SoD) risks identified within the Pathlock Cloud GRC platform's automated workflows are considered mitigated after approval actions are taken. It sets a timeframe for how long the mitigation is valid before re-assessment is required.

**Business Impact:**

Setting an appropriate period for SoD risk mitigation is crucial for maintaining the balance between operational efficiency and security within the business processes. It impacts the organization's ability to comply with internal controls and external regulations, potentially affecting audit outcomes and the overall risk posture.

**Technical Impact when configured:**

Configuring this parameter helps in managing the lifecycle of approved SoD risk mitigations by specifying a time limit. It directly influences the workflow engine's handling of user roles and access rights, ensuring users are only permitted to perform roles free of SoD conflicts for a determined period.

**Examples Scenario:**

For instance, if the `AutomaticWorkflowSoDMitigatedPeriodInDays` is set to 90 days for a user's emergency access role granted through an approval process in the workflow, this access will automatically be considered for re-evaluation or revocation after the specified period, helping to prevent prolonged inappropriate access.

**Related Settings:**

- ProfileTailorRoleForApplyChangesInAuthorizationSimulationRoleToUser

**Best Practices:** 

- **Configure when:** There is a clear policy on the duration for which mitigated SoD risks are acceptable within your organization's GRC framework. This helps in automated management of access rights, ensuring they are kept within the policy's constraints without manual intervention.
  
- **Avoid when:** The organization lacks a clear SoD mitigation policy or when SoD risks require permanent or long-term resolutions that do not align with temporary mitigation periods.