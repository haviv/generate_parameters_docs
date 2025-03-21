# Hide Derived Roles In Auto Complete

**Technical Name:** HideDerivedRolesInAutoComplete

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of derived roles in autocomplete fields throughout the Pathlock Cloud GRC platform. When activated, it aims to streamline the user experience by filtering out derived roles from the autocomplete suggestions, ensuring users have a more focused and relevant selection of roles to choose from. 

**Business Impact:**

The primary business impact lies in enhancing operational efficiency and user experience. By hiding derived roles in autocomplete fields, users can more easily and quickly find the specific roles they are looking for without sifting through potentially irrelevant suggestions. This can lead to more accurate role assignment and management, contributing positively to overall security and compliance postures.

**Technical Impact when configured:**

Configuring this parameter to hide derived roles impacts the role selection process in user management tasks. It directly influences how role data is queried and presented in the UI, especially in scenario-contributing functionalities such as system access requests, role delegation, and access reviews.

**Examples Scenario:**

For instance, in a scenario where an administrator is setting up access controls for a new employee, they might start typing in the role field to assign roles. With the "HideDerivedRolesInAutoComplete" parameter enabled, the autocomplete field will not show any derived roles, thereby simplifying the administrator's search for the appropriate primary roles. This ensures a more straightforward assignment process and helps in maintaining a cleaner and more manageable role structure.

**Related Settings:** 

- GridPageSize
- GroupChangeDocuemntResults
- EventsWorkflowOpenBy

**Best Practices:** configure when the role management process requires simplification, particularly in large or complex environments with numerous derived roles. Avoid when comprehensive visibility of all role types (including derived roles) is necessary during the role selection or management process.