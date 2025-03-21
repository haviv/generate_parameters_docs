# Custom TCodes For Direct Execution Of Programs

**Technical Name:** CustomTCodesForDirectExectionOfPrograms

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter enables the specification of custom transaction codes (TCodes) that are allowed for direct execution of programs. It is designed to help fine-tune the security and compliance settings related to direct program execution within the Pathlock environment.

**Business Impact:**

Configuring this parameter directly impacts an organization's ability to control and secure direct executions of reports or programs, thus affecting overall system security and compliance with internal or external regulations.

**Technical Impact when configured:**

When this parameter is properly configured, it ensures that only authorized transaction codes can be used to execute direct reports or programs, protecting against unauthorized access or potential misuse of the system's capabilities.

**Example Scenario:**

An organization needs to ensure that only certain users are able to execute direct programs for data analysis purposes. This parameter can be configured to include only the specific TCodes that these users are authorized to use, hence enforcing security policy and compliance requirements.

**Related Settings:**

- CustomReportSeperator
- CustomStoreProcedureForEmployeesData

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when:** You need to strictly control which reports or programs can be executed directly in the system to comply with security policies or regulations.
- **Avoid when:** Allowing broad direct execution rights aligns with the operational needs and security posture of the organization.