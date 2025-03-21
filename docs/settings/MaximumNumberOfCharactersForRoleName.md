# Maximum Number Of Characters For Role Name

**Technical Name:** MaximumNumberOfCharactersForRoleName

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** 

This parameter defines the maximum number of characters allowed in a role name within the Pathlock Cloud GRC platform. It ensures role names are kept within a manageable length for both display purposes and backend processing.

**Business Impact:** 

Setting an appropriate limit for the role name length helps in maintaining clarity and consistency across the organization's role-based access control. It prevents confusion that could arise from overly long or complex role names, thereby facilitating easier management and auditing of roles.

**Technical Impact when configured:** 

Once configured, this parameter enforces a limit on the number of characters that can be used in naming a role. Roles with names exceeding this limit cannot be created or renamed until they comply with the defined character count, ensuring uniformity and avoiding potential errors in role assignment or rights management.

**Examples Scenario:**

- **Scenario 1:** If the parameter is set to 20 characters, an admin attempting to create a role with the name "Senior Financial Analyst Role" (which is 27 characters long) will be prompted to shorten the name to comply with the maximum length requirement.
  
- **Scenario 2:** During a role-split operation where new roles are automatically generated, ensuring role names do not exceed the set limit will facilitate easier understanding and management of the newly created roles.

**Related Settings:** 

- `EventOnEmployeePositionCodeChangeIncludePositionTitleTexts`

**Best Practices:** 

- **Configure when:** Setting up the Pathlock platform for the organization to maintain concise and meaningful role names that are easily understandable.
- **Avoid when:** If there is no clear organizational policy on naming conventions or no issues have been faced due to long role names, adjusting this value might not be necessary. However, it is recommended to review this setting periodically as the organization scales.
