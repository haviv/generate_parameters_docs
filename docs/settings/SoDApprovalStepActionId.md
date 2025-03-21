# SoD Approval Step Action

**Technical Name:** SoDApprovalStepActionId

**Category:** SOD

**Default Value:** None

**Impact Level:** High

**Description:** This parameter identifies the approval step action required within an SoD (Segregation of Duties) check step in workflows.

**Business Impact:** Appropriately configuring this parameter ensures that transactions or activities that could potentially violate segregation of duties policies are properly flagged and subjected to an approval process. This is crucial for maintaining compliance and preventing fraud.

**Technical Impact when configured:** When configured, this parameter triggers an approval workflow for actions identified as violating SoD rules, effectively mitigating risks associated with unauthorized or fraudulent activities.

**Examples Scenario:** If a user attempts to access both the roles of "Purchase Order Creation" and "Vendor Payment Approval" within the same system or schema, the SoDApprovalStepActionId parameter would ensure that this potential violation is flagged and subjected to an approval process before access is granted.

**Related Settings:** 
- System
- Schema
- CompanyCode

**Best Practices:** 
- **Configure when:** Setting up SoD controls within your organization to ensure compliance and mitigate risk.
- **Avoid when:** There are no explicit SoD policies or controls required for the business process in question.