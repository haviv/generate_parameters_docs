# Max Role Size For Role Advisor Dialog

**Technical Name:** MaxRoleSizeForRoleAdvisorDialog

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** This parameter controls the maximum size of roles that can be processed or displayed in the Role Advisor Dialog within the Pathlock Cloud GRC platform.

**Business Impact:** Configuring this parameter helps in managing system performance and user experience by limiting the amount of data processed during role evaluation and selection tasks. This can especially impact large organizations with numerous roles, ensuring the Role Advisor Dialog remains responsive and efficient.

**Technical Impact when configured:** Adjusting this parameter impacts how roles are loaded and displayed within the Role Advisor Dialog. A lower value may lead to faster dialog performance but at the risk of excluding larger roles from evaluation, while a higher value can accommodate larger roles but may impact system performance and user experience due to increased loading times.

**Examples Scenario:** In an organization where there are thousands of roles, setting an appropriate value for MaxRoleSizeForRoleAdvisorDialog ensures the Role Advisor Dialog can efficiently display roles without overwhelming the system or the end-user, facilitating smoother role selection processes during audit or compliance workflows.

**Related Settings:** 

- EmployeeExtraAttributesAddEscape

**Applicable Workflows Actions:** 

- RolesSelectionList

**Best Practices:** 

- **configure when:** Adjust the parameter to accommodate the average size of roles in your organization, ensuring a balance between performance and usability. 

- **avoid when:** Do not set the value too low if your organization has complex roles that could be excluded from the selection process, nor too high where it might degrade performance and user experience.