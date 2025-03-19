### CreateDerivedRolesBasedOnTemplateParentRoleAction

**Category:** User Management

**Description:**

The `CreateDerivedRolesBasedOnTemplateParentRoleAction` is designed to automate the creation of derived roles based on a specified template parent role within the Pathlock Cloud's identity and GRC platform. This action facilitates the dynamic generation of new roles, reducing manual setup processes and ensuring consistency in role-based access controls. Once initiated, the action fetches the template parent role specified by the user, and for each derived role found, it generates new roles based on the predefined conditions and mappings provided. The action is executed within the context of SAP role management, however, it's designed to be adaptable for different systems within the scope of identity management and governance.

**Parameters:**

*Basic Parameters:*

- Name: TemplateParentRole
  - Description: The name of the template parent role from which derived roles will be created. It acts as a base for generating new roles.
  - Default value: N/A
  - Mandatory: yes

- Name: NewParentRole
  - Description: Specifies the naming convention for the new parent role to be created from the template.
  - Default value: N/A
  - Mandatory: yes

*Advanced Parameters:*

- Name: RolesSplliterRolesIgnoreText_Replace
  - Description: Specifies text patterns to be ignored or replaced in the master role name during the role creation process.
  - Default value: N/A
  - Mandatory: no

- Name: IsTestRun
  - Description: A boolean parameter that determines whether the action is executed as a test run, preventing actual creation of roles.
  - Default value: false
  - Mandatory: no

**Business impact:**

Implementing `CreateDerivedRolesBasedOnTemplateParentRoleAction` significantly optimizes the role creation and management process within an organization. By automating the derivation of roles from a single template, it ensures consistency across user access management, mitigates risks associated with manual errors, and enhances audit and compliance capabilities by maintaining standardized role-based access controls.

**Example of usage:**

An administrator wishes to populate a set of derived roles from a master role "SAP_FINANCE_MANAGER" across different organizational units with specific adjustments in role names and permissions. They would specify "SAP_FINANCE_MANAGER" as the `TemplateParentRole`, define the naming guideline in `NewParentRole`, and run the action, resulting in the creation of new, customized roles derived from the template role, tailored to each unit's access needs.

**Prerequisites:**

- Administrative access to the Pathlock Cloud platform with permissions to execute workflow actions.
- A predefined template parent role must exist within the system.
- Knowledge of the existing roles and required access permissions to accurately setup the parameters.

**Error Handling and Troubleshooting:**

- **Issue:** Action fails to create any derived roles.
  - **Possible Cause:** The template parent role does not exist or is incorrectly named.
  - **Solution:** Verify the existence of the template parent role and check for typos in the `TemplateParentRole` parameter.

- **Issue:** Derived roles are not as expected.
  - **Possible Cause:** Incorrect setup of the `NewParentRole` or `RolesSplliterRolesIgnoreText_Replace` parameters.
  - **Solution:** Review the configurations and ensure they match the intended outcome. Conduct a test run using the `IsTestRun` parameter to validate configurations before executing the action.

By adhering to these guidelines, users can effectively utilize the `CreateDerivedRolesBasedOnTemplateParentRoleAction` to streamline role management processes within their identity and GRC framework.