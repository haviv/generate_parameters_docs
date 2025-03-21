# Show Has Change Filter

**Technical Name:** ShowHasChangeFilter

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:** Enables users to filter reporting views based on whether certain criteria or data points have changed.

**Business Impact:** Allows for more targeted reporting by highlighting changes in user access or risk levels, thus helping in identifying potential security risks or compliance issues more efficiently.

**Technical Impact when configured:** When enabled, this setting allows reports to include or exclude data based on changes, thereby improving the relevance and focus of compliance and security reporting.

**Examples Scenario:**
- An auditor wants to see all changes in user roles within the last quarter to ensure all modifications adhere to the compliance policy. Enabling the Show Has Change Filter would allow them to easily identify these changes.
- A security officer wishes to review all recent modifications to sensitive access permissions to ensure no unauthorized changes have occurred. This filter facilitates a focused review by highlighting these changes.

**Related Settings:** RoleSpliterCopyAlsoInactiveAuth

**Best Practices:** 
- Configure when timely identification of changes is critical to maintaining security and compliance standards.
- Avoid when comprehensive, unfiltered data analysis is required.