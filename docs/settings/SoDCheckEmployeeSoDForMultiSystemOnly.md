# SoD Check Employee SoD For Multi System Only

**Technical Name:** SoDCheckEmployeeSoDForMultiSystemOnly

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:** 
This configuration parameter determines whether the Separation of Duties (SoD) check is applied exclusively for employees with access across multiple systems. It helps in identifying cross-system conflicts of interest by focusing on users who may have conflicting roles or permissions within different applications or systems, thus ensuring a more stringent compliance and security posture.

**Business Impact:**
Enabling this setting ensures that SoD policies are enforced more effectively by prioritizing checks on employees who have access to multiple systems. This targeted approach helps reduce the risk of fraud, errors, and unauthorized access, thereby enhancing the organization's internal controls and compliance with regulatory requirements.

**Technical Impact when configured:**
When configured, the system will filter and perform SoD analysis only for users that have permissions in more than one system. This is particularly useful in environments with complex IT landscapes, where users may hold roles across different platforms, increasing the risk of SoD violations.

**Examples Scenario:**
A scenario where this parameter might be particularly beneficial is in large organizations with diverse IT systems. For example, an employee with access to both the financial system and the HR information system might inadvertently be granted permissions that allow them to both create vendors and approve payments, constituting an SoD conflict. Enabling `SoDCheckEmployeeSoDForMultiSystemOnly` would ensure such configurations are flagged for review.

**Related Settings:**
- WorkflowActionsDisabledColor
- VerifyWorkflowActionsNotVerifiedText

**Best Practices:** 
- **configure when:** You operate in a multi-system environment where users have access across different platforms, and there's a need for stringent SoD controls.
- **avoid when:** Your organization operates a single system or if SoD controls across multiple systems are not a regulatory or compliance requirement.
