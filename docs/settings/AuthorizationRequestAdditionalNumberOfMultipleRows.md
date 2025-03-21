**Authorization Request Additional Number Of Multiple Rows**

**Technical Name:** AuthorizationRequestAdditionalNumberOfMultipleRows

**Category:** Authorization Review

**Default Value:** Not specified

**Impact Level:** Medium

**Description:** This parameter controls the additional number of rows that can be included in an authorization request when performing batch operations within the Pathlock Cloud GRC platform. It specifically applies to scenarios where multiple items or entities are being reviewed or authorized simultaneously.

**Business Impact:** Adjusting this parameter can significantly affect the efficiency and manageability of batch authorization requests. A higher number allows for more extensive reviews in a single operation, potentially reducing the time and effort required for authorization processes. However, setting the value too high may impact system performance or overwhelm reviewers with too much information at once.

**Technical Impact when configured:** When this parameter is configured to increase the number of rows, it allows users to handle larger datasets in a single authorization request. This can improve workflow efficiency but may also increase the load on the system, requiring careful configuration to balance performance with operational needs.

**Example Scenario:** An organization needs to regularly review and authorize hundreds of user role assignments due to frequent staffing changes. By adjusting this parameter to allow a higher number of rows per authorization request, the security team can review and process these changes more quickly and in fewer batches.

**Related Settings:**
- RoleAdvisorNumberOfRowsToCalculateSodViolation

**Best Practices:** 
- Configure when handling large datasets in authorization reviews to improve efficiency.
- Avoid setting the value too high to prevent system overload and reduce the risk of overwhelming reviewers. Aim for a balance that suits the size and capability of your organization.