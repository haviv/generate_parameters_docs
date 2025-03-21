# Role Advisor Number Of Rows To Calculate SoD Violation

**Technical Name:** RoleAdvisorNumberOfRowsToCalculateSodViolation

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

The RoleAdvisorNumberOfRowsToCalculateSodViolation parameter determines the maximum number of rows (entities) that the Pathlock Cloud GRC platform's Role Advisor will analyze to calculate potential Segregation of Duties (SoD) violations within an organization's roles. It impacts the scope of SoD violation reviews, ensuring that the analysis is manageable, precise, and within the system's performance thresholds.

**Business Impact:**

Configuring this parameter properly can significantly affect an organization's ability to efficiently manage risk and maintain compliance with regulatory standards. By setting an optimal number of rows for SoD analysis, organizations can ensure that critical violations are identified and addressed without overwhelming the system or administrators with excessive data.

**Technical Impact when configured:**

Proper configuration leads to optimized performance of the Role Advisor function within Pathlock Cloud GRC. It prevents system overload by limiting the number of rows analyzed for SoD violations, ensuring timely and relevant risk assessments.

**Examples Scenario:**

For an organization with thousands of roles, setting the RoleAdvisorNumberOfRowsToCalculateSodViolation to a reasonable limit, like 100, means the system will only evaluate potential SoD violations across the most recent or most critical 100 roles identified, optimizing review times and focusing efforts on areas with potentially higher risk exposure.

**Related Settings:** 

- WorkflowRemainderEmailTemplateId

**Best Practices:** configure when
- There is a need to focus the SoD analysis on a manageable subset of roles.
- The system experiences performance issues due to large datasets.

avoid when
- A comprehensive review of all roles is required without omitting any potential risk.