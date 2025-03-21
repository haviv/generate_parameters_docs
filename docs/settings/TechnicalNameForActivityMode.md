**Technical Name: TechnicalNameForActivityMode**

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `TechnicalNameForActivityMode` parameter is utilized within the Pathlock Cloud GRC platform to define or alter the behavior of activities as they are being added to a group or queried for in the context of folder permissions. It plays a crucial role in tailoring the platform's workflow actions to meet specific organizational security, risk, and compliance requirements.

**Business Impact:**

Properly setting this parameter can significantly affect how activities are categorized and accessed, influencing both the efficiency of workflow management and the security posture of the organization. Misconfiguration may lead to improper access permissions or inefficiencies in workflow operations.

**Technical Impact when configured:**

When the `TechnicalNameForActivityMode` is configured correctly:
- It ensures that activities are properly grouped, enhancing the organization and visibility of activities within the Pathlock platform.
- It facilitates the correct application of folder permissions, contributing to the secure and compliant management of data.

**Examples Scenario:**

In a scenario where an organization needs to categorize activities based on their sensitivity level, `TechnicalNameForActivityMode` could be configured to differentiate activities that have high, medium, or low sensitivity. This differentiation allows for applying distinct folder permissions for each category, ensuring users have access only to the activities pertinent to their role and compliance requirements.

**Related Settings:**

- `TechnicalNameForUserGroup`

**Applicable Workflows Actions:**

- AddActivityToGroup
- GetGroupsForFolderPermission

**Best Practices:** 

- **Configure when:** you need to customize how activities are grouped or how folder permissions are granted based on the organizational workflow and security requirements.
  
- **Avoid when:** default grouping and permission settings align with the organization's needs, or if there is insufficient information to categorize activities accurately.