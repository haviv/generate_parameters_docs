# Hide Roles In Search Window By Attribute10 Values

**Technical Name:** HideRolesInSearchWindowByAttribute10Values

**Category:** User Management

**Default Value:** Not provided

**Impact Level:** Medium

**Description:** This parameter controls the visibility of roles in the search window based on the values of Attribute10. It allows for a more focused and efficient search experience by filtering out roles that do not meet certain criteria defined by Attribute10.

**Business Impact:** By enabling this feature, organizations can streamline the role search process, making it easier for administrators and users to find relevant roles. This is particularly useful in environments with a large number of roles, where finding the right role can be time-consuming and cumbersome.

**Technical Impact when configured:** When this parameter is configured, the role search functionality will filter the roles displayed in the search results according to the specified Attribute10 values. Roles that do not match the filter criteria will be hidden from the search results, reducing clutter and improving the efficiency of the role search process.

**Examples Scenario:** Suppose a company wants to restrict the display of certain roles in the search window that are not relevant for a particular audit or compliance process. By configuring this parameter, roles tagged with specific Attribute10 values that denote irrelevance to the process can be hidden from the search results, focusing the user's search on roles that are pertinent.

**Related Settings:** Not directly related to any provided settings.

**Best Practices:** Configure this parameter when you have a clear understanding of which roles need to be hidden based on Attribute10 values to avoid unintentionally hiding important roles. Avoid configuring this parameter without a strategy for role visibility, as it could lead to confusion or difficulty in finding certain roles when needed.