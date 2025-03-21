# Include All Activity Mode

**Technical Name:** IncludeAllActivitiyMode

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The "Include All Activity Mode" parameter controls whether all organizational unit types are considered when importing manager information into workflows. This setting is pivotal in determining the scope of data processed and included in workflow-related decisions and reporting.

**Business Impact:**

Adjusting this parameter can significantly affect compliance and operational efficiency. For organizations under strict regulatory watch, ensuring accurate and comprehensive activity inclusion is crucial for audit and compliance purposes. It dictates the inclusivity of the workflow data, potentially impacting decision-making and reporting accuracy.

**Technical Impact when configured:**

When enabled, this mode ensures a complete set of data concerning managerial activities and related organizational units is imported into workflows, facilitating thorough analysis and reporting. Conversely, disabling it allows for a more streamlined, focused import process, beneficial in scenarios where not all activity data is relevant to the workflow’s intended purpose.

**Example Scenario:**

- **Scenario 1:** An organization needs to adhere to tight compliance requirements requiring comprehensive oversight of all managerial activities. By enabling "Include All Activity Mode," they can ensure that no piece of relevant information is omitted during the import process, enhancing the fidelity of compliance reporting.
  
- **Scenario 2:** A company seeks to streamline its internal audit processes by focusing only on specific departments due to resource constraints. By adjusting the "Include All Activity Mode" setting, they can exclude irrelevant organizational unit types, making the audit process more manageable and focused.

**Related Settings:** ImportManagersToWFIgnoreDepartmentTypes, ImportManagersToWFIncludePhoneNumberInDescription

**Best Practices:** 
- **Configure when:** Complete data inclusivity is required for compliance, audit, or in-depth analysis purposes.
- **Avoid when:** The workflow process should remain streamlined, focusing on specific departments or activities to save on processing time and resources.