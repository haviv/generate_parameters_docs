# Workflow Employee Card

**Technical Name:** Workflow_EmployeeCard

**Category:** Workflow

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The Workflow Employee Card parameter is used within the Pathlock Cloud GRC platform to customize and manage visibility options and data bindings for employee-specific information in workflow-related interfaces and processes. It ensures that relevant employee data is accessible and can be dynamically included in workflow scenarios, particularly where user-specific information is crucial for decision-making or tracking purposes.

**Business Impact:**

Effectively configuring the Workflow Employee Card parameter impacts how organizations can monitor, manage, and report on employee-specific data within their governance, risk, and compliance activities. By enabling tailored visibility and interaction with employee data, businesses can ensure compliance with internal policies and external regulations, improve the accuracy of user role management, and enhance the efficiency of audit processes.

**Technical Impact when configured:**

When configured, this parameter enables dynamic data bindings and configurations within user management workflows, allowing employee-specific data to be displayed and interacted with. It impacts user experience by providing context-relevant data, supports compliance by ensuring correct data usage, and enhances security through precise access controls.

**Examples Scenario:**

An organization desires to streamline its user access review process by ensuring managers have all relevant employee information readily available during the workflow. By configuring the Workflow Employee Card parameter, they can include critical information like SAP user names or specific HR fields directly within the workflow interface, thus improving decision-making efficiency and accuracy.

**Related Settings:**

- UsersProfile
- UpdateUserRoleInFinish
- UseSapProfilesAsRoles

**Best Practices:** configure when necessary to provide essential employee information within workflows; avoid when excessive information could clutter the interface or when data privacy concerns are paramount.