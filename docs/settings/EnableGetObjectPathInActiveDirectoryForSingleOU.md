# Enable Get Object Path In Active Directory For Single OU

**Technical Name:** EnableGetObjectPathInActiveDirectoryForSingleOU

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the Pathlock GRC platform will extract and store the full LDAP path for objects located in a single Organizational Unit (OU) within Active Directory. When enabled, it captures the complete path for better identification and management of the objects.

**Business Impact:**

Enabling this setting can significantly enhance security governance and administration by allowing for more precise tracking and control of Active Directory objects. It is particularly useful for organizations that require detailed auditing and monitoring capabilities to comply with internal policies or external regulations.

**Technical Impact when configured:**

Once enabled, any AD object belonging to a specified OU will have its entire LDAP path retrieved and stored. This could potentially increase the amount of data processed and stored, but it greatly aids in the precise management and identification of AD objects, enhancing granular security controls and compliance reporting.

**Examples Scenario:**

- *Enhanced Security Management*: With this parameter enabled, administrators can more easily trace the origins of AD objects, improving the organization's ability to monitor and manage access controls and security policies.
- *Improved Compliance*: For organizations subject to strict regulatory requirements, having detailed information about AD objects, including their full paths, can simplify compliance auditing processes.

**Related Settings:**

- `ForceWorkflowRoleUpdateDisplay`

**Best Practices:** 

- **Configure when**: 
  - Detailed tracking and management of Active Directory objects is a priority.
  - You need to enhance security and compliance measures by having more control and visibility over AD objects.
  
- **Avoid when**: 
  - Your organization does not require detailed tracking of objects within Active Directory, or such granularity might lead to unnecessary complexity and overhead.