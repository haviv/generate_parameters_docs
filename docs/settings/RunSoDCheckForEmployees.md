# Run SoD Check For Employees

**Technical Name:** RunSoDCheckForEmployees

**Category:** SOD

**Default Value:** False

**Impact Level:** High

**Description:** Enables the execution of Segregation of Duties (SoD) checks specifically for employee roles within the organization's IT systems to identify potential conflicts in access rights that could lead to fraud or error.

**Business Impact:** Ensuring that SoD checks are run for employees minimizes the risk of fraud, prevents errors in financial reporting, and reinforces internal controls by highlighting areas where excessive permissions may breach policy or compliance requirements.

**Technical Impact when configured:** When enabled, this setting systematically scans and analyzes employee access within systems to detect and report any combinations of duties that should be segregated to prevent conflicts of interest, fraud, or errors.

**Example Scenario:**

- **Scenario 1:** An organization is preparing for a financial audit and must demonstrate compliance with internal controls standards. Enabling `RunSoDCheckForEmployees` would allow them to quickly identify and rectify any access combinations among employees that could compromise the integrity of financial processes.

**Related Settings:**

- `EnableJobFailedRead`
- `EnableTransportsRead`

**Best Practices:** 

- **Configure when:** You have clearly defined SoD policies and need to enforce them within your IT systems to comply with regulatory requirements, or when you wish to strengthen your internal controls against potential fraud or errors.
  
- **Avoid when:** Your organization lacks the necessary structure to define or enforce SoD policies, or if the potential impact on system performance outweighs the benefits of automated checks in your specific context.