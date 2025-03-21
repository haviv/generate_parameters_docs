# Check SoD For Employees

**Technical Name:** CheckSodForEmployees

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

The CheckSodForEmployees parameter is designed to automate the process of Segregation of Duties (SoD) validation for employee user accounts within the Pathlock Cloud GRC platform. This validation process identifies potential security risks associated with improper SoD, helping to maintain compliance and minimize risk.

**Business Impact:**

Improper segregation of duties can lead to fraud, errors, and compliance risks. By using CheckSodForEmployees, organizations can proactively detect and manage these risks, ensuring that no individual has conflicting responsibilities or excessive access rights within critical systems.

**Technical Impact when configured:**

- Automated scanning and validation of user roles and permissions for potential SoD conflicts.
- Dynamic update on user status based on SoD validation results, facilitating immediate corrective actions.
- Enhanced performance and efficiency in handling SoD checks through in-memory processing options.

**Examples Scenario:**

- **Before Implementation:** Manual reviews of user roles and permissions are conducted irregularly, leading to delayed detection of SoD violations and prolonged exposure to potential fraud.
  
- **After Implementation:** CheckSodForEmployees is configured to run daily, automatically identifying and reporting any SoD conflicts among employees. This allows for swift remediation, significantly reducing the organization’s risk exposure.

**Related Settings:** 

- `CommonSettings.Default.RunSoDInMemory` - Determines whether SoD checks are processed in-memory for performance optimization.

**Best Practices:** 

- **Configure when:** Regular monitoring and enforcement of SoD policies are required to meet compliance standards and minimize security risks.
- **Avoid when:** The organization operates under a minimal risk environment or when the performance impact of in-memory processing cannot be justified.