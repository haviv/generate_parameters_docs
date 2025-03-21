# Show Open On On Workflow

**Technical Name:** ShowOpenOnOnWorkflow

**Category:** Workflow

**Default Value:** Not explicitly mentioned in provided code references

**Impact Level:** Medium

**Description:** This parameter controls the visibility of open workflow instances within the Pathlock Cloud GRC platform, specifically within certain user interfaces and reports. It determines whether workflow instances that are currently open should be displayed, enhancing the customization and flexibility of workflow management.

**Business Impact:** Proper configuration of this parameter can significantly improve the efficiency of workflow management by ensuring that users have visibility into relevant, active workflows. This can impact decision-making processes, audit readiness, and compliance management by providing clear insights into the operational status and approval processes within the organization.

**Technical Impact when configured:** When enabled, users can see open (active) workflow instances in applicable reports and user interfaces. This can aid in tracking progress, understanding current workloads, and identifying potential bottlenecks in the workflow process.

**Examples Scenario:** An organization is undergoing an audit for compliance with industry standards. The auditor requests a report of all currently open access requests to review workflow efficiency and compliance with approval processes. With ShowOpenOnOnWorkflow enabled, generating such a report directly from the Pathlock Cloud GRC platform becomes feasible, providing real-time data on all open workflows.

**Related Settings:** EnableOpenRequestByManager

**Best Practices:** Configure this parameter to be enabled in scenarios where real-time tracking of workflow statuses is crucial for operational efficiency or compliance. Avoid enabling this feature if there is a need to limit the visibility of open workflows due to security or confidentiality concerns.