# Authorization Review Show User Or Employee By Process Definition

**Technical Name:** AuthorizationReviewShowUserOrEmployeeByProcessDefinition

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

Allows for the differentiation between User and Employee data during the review process based on specific process definitions.

**Business Impact:**

Facilitates targeted review processes by ensuring that reviewers can distinguish between users and employees, which is critical for maintaining accurate access rights and compliance levels within organizational roles and processes.

**Technical Impact when configured:**

Enables the system to adapt display outputs during authorization reviews, affecting both the efficiency and accuracy of the review process by ensuring pertinent information is presented in line with the process criteria.

**Examples Scenario:**

A scenario where this parameter is critical could involve a compliance officer reviewing access rights as part of a quarterly audit. By enabling this feature, the officer can quickly distinguish between a user (an account that might have system-wide access for administration purposes) and an employee (an individual with access tailored to their job functions), thereby streamlining the review process.

**Related Settings:**

- AuthorizationReviewByRolesShowActivitiesInRoleDetailsLink

**Applicable Workflows Actions:**

**Best Practices:** 

- **Configure when:** A clear understanding of the distinction between user and employee roles and their impact on the access review process is established.
  
- **Avoid when:** If the organization does not have a defined difference in access control policies or review processes between users and employees.