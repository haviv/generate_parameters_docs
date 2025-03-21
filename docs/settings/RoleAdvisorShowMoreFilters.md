# Role Advisor Show More Filters

**Technical Name:** RoleAdvisorShowMoreFilters

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

The "Role Advisor Show More Filters" parameter allows users to expand or contract the filter options available within the Role Advisor feature on the Pathlock Cloud GRC platform. This parameter is designed to enhance user experience by providing flexibility in how much detail the users wish to see and use when searching for or analyzing roles.

**Business Impact:**

Enabling more filters can significantly streamline the process of finding specific roles based on finer details such as transaction codes, system IDs, or other criteria, thus improving efficiency in role management and compliance activities. This can lead to a more refined and efficient compliance process, making it easier for businesses to adhere to various compliance standards by ensuring the right roles are assigned to the right individuals.

**Technical Impact when configured:**

When this parameter is configured to show more filters, users will have the ability to apply more granular searches within the Role Advisor. This could lead to an increased load on the server due to more complex queries being processed, but it also means users can more accurately pinpoint roles that meet specific criteria, potentially reducing the time spent on role review and adjustment.

**Examples Scenario:**

Imagine a scenario where an organization is undergoing an audit and needs to quickly verify that roles are correctly assigned according to strict compliance requirements. By enabling more filters, auditors can quickly narrow down their search to specific transaction codes or system IDs, making the audit process more efficient.

**Related Settings:** 

- ReadRoleAssignmentChangeDocuments

**Best Practices:** configure when needing detailed role analysis and review for compliance or audit purposes; avoid when broad role searches are sufficient to meet organizational needs.