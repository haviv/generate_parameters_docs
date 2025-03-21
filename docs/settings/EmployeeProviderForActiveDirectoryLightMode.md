# Employee Provider For Active Directory Light Mode

**Technical Name:** EmployeeProviderForActiveDirectoryLightMode

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter controls the integration mode for employee data synchronization between an Active Directory (AD) and the Pathlock platform in a lightweight manner. When enabled, it optimizes the sync process to handle essential employee data efficiently without overburdening system resources.

**Business Impact:** Enabling this feature can significantly reduce the load on system resources during synchronization processes, leading to improved system performance and user experience. It is particularly beneficial for organizations with large volumes of employee data in Active Directory that need to be managed efficiently.

**Technical Impact when configured:** When configured, the system will use a minimized data set for synchronization purposes, focusing on vital employee information necessary for GRC functionalities. This can result in faster sync times and lower system overhead, enhancing overall system responsiveness and reducing operational delays in managing compliance and security workflows.

**Examples Scenario:**

- **Scenario 1:** An organization experiences slow performance and high system load during the synchronization of employee data from Active Directory. Enabling the EmployeeProviderForActiveDirectoryLightMode can mitigate these performance issues by reducing the data load during synchronization processes.
  
- **Scenario 2:** A company is looking to optimize its Pathlock Cloud GRC platform without compromising on the timeliness and accuracy of employee data used in security, risk, and compliance workflows. By enabling this parameter, the company can achieve a balanced performance, ensuring that critical employee data is still synchronized efficiently.

**Related Settings:** 

- ShowEmployeeInfoInWorkflowForm
- NewPasswordRule_Enable_PasswordMustNotContainUsername

**Best Practices:** 

- **Configure when:** You're experiencing high latency or system resource strain during Active Directory synchronization, or when working with large AD datasets where only essential employee data is required for compliance and security purposes.
- **Avoid when:** Full detail synchronization is critical for your compliance, security requirements, or if the reduced data set does not suffice for organizational GRC needs.