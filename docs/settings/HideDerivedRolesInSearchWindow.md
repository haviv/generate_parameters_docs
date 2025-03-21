# Hide Derived Roles In Search Window

**Technical Name:** HideDerivedRolesInSearchWindow

**Category:** Configuration

**Default Value:** Not provided

**Impact Level:** Medium

**Description:** This parameter controls the visibility of derived roles within the search windows of the Pathlock Cloud GRC platform. When enabled, it hides derived roles from search results, streamlining the view for users by only displaying primary roles.

**Business Impact:** Enabling this feature can significantly enhance the usability of the Pathlock Cloud GRC platform for end users. It simplifies the search process by filtering out derived roles from the search results, allowing users to focus on primary roles. This can help in reducing confusion and improving the efficiency of role selection and assignment processes.

**Technical Impact when configured:** Once configured, this setting filters out any derived roles from appearing in the search results within role search operations. This ensures that users are presented with a simplified list, enhancing usability and reducing potential errors in role selection.

**Examples Scenario:** A company uses the Pathlock Cloud GRC platform to manage user roles within their ERP system. They have a large number of derived roles that are variations of a few primary roles. By enabling `HideDerivedRolesInSearchWindow`, they can make the user interface cleaner and more straightforward for administrators managing role assignments, as only the primary roles will be displayed in the search window.

**Related Settings:** Not provided

**Best Practices:** Configure when the presence of derived roles in search results is known to cause confusion or inefficiency in role assignment processes. Avoid when detailed visibility of all roles, including derived ones, is critical for the role management process.