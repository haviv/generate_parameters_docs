# Set User Email By Company Employee

**Technical Name:** SetUserEmailByCompanyEmployee

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The `SetUserEmailByCompanyEmployee` parameter is designed to automate the process of defining user email addresses in the Pathlock Cloud GRC platform based on their employment status and details within the company. This parameter plays a crucial role in ensuring that users are correctly and efficiently assigned email addresses, thereby streamlining communication and access within the system.

**Business Impact:**

Setting user emails automatically by their company employee status can significantly enhance operational efficiency, reduce manual errors, and ensure that all communications are correctly directed. This capability is particularly useful in large organizations where user management is an ongoing process and email addresses are essential for access, notifications, and compliance purposes.

**Technical Impact when configured:**

When this parameter is enabled, the system automatically retrieves and assigns email addresses to users based on their associated company employee information. This automation can lead to a more streamlined user onboarding process, minimizes the need for manual intervention, and ensures that email-related fields are populated accurately and consistently across the platform.

**Examples Scenario:**

A user, John Doe, is onboarded to the Pathlock Cloud GRC platform. Upon setting the `SetUserEmailByCompanyEmployee` parameter to true, the system automatically retrieves John's company email address from the Active Directory or employee database and assigns it to his user profile, ensuring he receives all necessary communications and access rights through his official email address.

**Related Settings:**

- `GetEmployeeRolesByActiveDirectoryUser`

**Best Practices:** 

- Configure when: Automating user management processes is a priority, and there is a reliable source of employee information that includes up-to-date email addresses.
- Avoid when: User email addresses do not align with company employee records, or there are multiple sources of truth for email addresses that might lead to inconsistencies.