# Employees Not Saved Body

**Technical Name:** EmployeesNotSavedBody

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `EmployeesNotSavedBody` parameter is utilized within the synchronization workflows for organization employee data, especially in scenarios where discrepancies between newly created employees and existing employee records are checked. This parameter is key in managing the communication or handling actions when certain employee records do not meet the criteria to be added or updated in the system during the sync process.

**Business Impact:**

Improper configuration or understanding of this parameter could lead to missed notifications about synchronization issues, resulting in outdated or incorrect employee data being present in the system. This could have ramifications for compliance reporting, security permissions, and access rights management within the organization.

**Technical Impact when configured:**

Configuring `EmployeesNotSavedBody` effectively ensures that administrators or relevant stakeholders are alerted about synchronization discrepancies, enabling timely manual verification and update of employee records. This is paramount to maintaining the integrity, accuracy, and security of the employee data within the organization.

**Examples Scenario:**

- During the synchronization process, if new employee records from an HR system do not match existing records due to discrepancies in key fields, this parameter could trigger notifications to administrators to review and correct the discrepancies.
- If the system detects that the number of new employees being imported exceeds a predetermined threshold (as defined in `MaximumEmployeeRecordsDifference`), the `EmployeesNotSavedBody` parameter might be used to configure an alert to prevent bulk erroneous data import.

**Related Settings:**

- `MaximumEmployeeRecordsDifference`: This setting defines the threshold for the difference in employee records that triggers alerts or actions.

**Best Practices:** configure when, avoid when

- **Configure when**:
  - You are managing large volumes of employee data across systems that need to be kept in sync.
  - Regular audits and compliance checks for employee data accuracy and integrity are crucial.
  - You need to ensure that discrepancies in employee data are promptly addressed by responsible parties.
- **Avoid when**:
  - Employee data is rarely synchronized or updated, making real-time alerts and checks unnecessary.
  - The organization lacks the resources to manage the alerts or discrepancies highlighted by this parameter effectively.