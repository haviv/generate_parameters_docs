# Show Advanced User Group Filter Selection

**Technical Name:** ShowAdvancedUserGroupFilterSelection

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

Enables advanced filtering options for user groups outside the standard users filter. This parameter is intended to provide more granular control over the visibility and management of user groups within reports and analyses.

**Business Impact:**

Activating this feature can significantly improve the ability to segregate and manage user group data, enhancing compliance, audit readiness, and security posture by ensuring only relevant data is presented to the end-users based on their roles and permissions.

**Technical Impact when configured:**

When enabled, this setting allows for the application of more sophisticated filters to user groups, which may include filters based on specific attributes, membership criteria, or custom-defined parameters. This can lead to more efficient reporting and data analysis processes, as it reduces the volume of irrelevant information presented to users.

**Example Scenario:**

An organization needs to ensure that reports generated for department heads only include data relevant to their specific department's user groups. By enabling the Show Advanced User Group Filter Selection, the organization can configure the reports to filter out user groups that do not pertain to each department head, thus streamlining the information and making it more actionable.

**Related Settings:**

- ShowUserGroupFilterOutsideUsersFilter

**Best Practices:** 

- **Configure when:** There is a need to provide detailed and specific visibility over user groups within reports to meet compliance requirements or for detailed data analysis.
- **Avoid when:** The default filtering capabilities are sufficient for the reporting needs, or there are concerns about the complexity of managing the filters leading to potential misconfigurations.