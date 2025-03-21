# Managers Groups In Active Directory

**Technical Name:** ImportManagersToWFActiveDirectoryManagersGroups

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the importation of manager groups from an organization's Active Directory (AD) into Pathlock's workflow systems. This setting is crucial for organizations looking to automate and synchronize manager roles and permissions based on their existing AD configurations.

**Business Impact:**

Improves efficiency in role management and ensures that managerial permissions and accesses are up-to-date and accurately reflected across the Pathlock platform. It minimizes manual work in updating manager groups within the system, reducing the risk of human error and enhancing overall security posture.

**Technical Impact when configured:**

- Dynamically updates workflow permissions and access based on AD manager groups.
- Ensures that only current managers have access to sensitive workflows and data, adhering to the principle of least privilege.
- Streamlines the process of updating manager roles across business units, reflecting real-time organizational changes.

**Examples Scenario:**

1. **Automating Role Assignments:** An organization restructures its management team, and several managerial positions are reassigned within the AD. Using this parameter, the Pathlock platform automatically updates the workflow permissions, ensuring that only the appropriate individuals have access to sensitive information, without manual intervention.

2. **Compliance and Auditing:** Ensuring that only currently assigned managers have access to specific workflows is essential for compliance. This setting automates the process, making it easier to audit permissions and demonstrate compliance with various regulations.

**Related Settings:**

- `SodResolver_MaxNoOfActivitiesToKeep`
- `ImportManagersToWFApprovalGroupInactiveText`

**Best Practices:** 

- **Configure when:** you have a dynamic organizational structure with frequent changes in management roles or when you aim to reduce manual workload in managing access permissions.
  
- **Avoid when:** your organization does not use Active Directory for managing user roles or if there is no clear mapping between AD groups and Pathlock manager roles.