# Run Process Out Process

**Technical Name:** RunProccessOutProccess

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:**

The "Run Process Out Process" parameter is designed to control the execution of processes and workflows within the Pathlock Cloud GRC platform. It plays a critical role in managing how and when certain automated tasks are initiated, ensuring they are run efficiently and securely outside of the main system process.

**Business Impact:**

Proper configuration of this parameter can significantly impact the operational efficiency and security posture of an organization. It ensures that critical processes related to governance, risk management, and compliance (GRC) are executed in a controlled manner, minimizing risks associated with process failures or unauthorized access.

**Technical Impact when configured:**

- **Enhanced Performance:** Running processes outside the main system process can lead to better overall system performance and responsiveness.
- **Reduced Risk:** Isolates the execution of critical processes, reducing the risk of system-wide issues due to process failures.
- **Improved Security:** Limits the exposure of the main system to potential vulnerabilities by segregating the execution environment of sensitive processes.

**Examples Scenario:**

A financial institution utilizes the Run Process Out Process parameter to manage the execution of its quarterly risk assessment processes. By configuring this parameter, the institution can ensure that these critical processes are executed securely and efficiently outside the main system process, thereby minimizing the impact on system performance and enhancing the execution security.

**Related Settings:** 

- `ProfileTailorProcessesLogs`
- `RolesSplliterRolesChildRoleObjectsOnlyRoleFlag`
- `RequestApprovedTemplateId`

**Best Practices:** 

- **Configure when:** There is a need to improve system performance or when executing processes that require a high level of security and isolation.
- **Avoid when:** The system doesn't have the requisite resources to manage processes outside of the main system process efficiently.