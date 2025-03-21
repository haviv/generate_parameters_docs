**Run User Process In Separate Queue**

**Technical Name:** RunUserProcessInSeperateQueue

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the execution of certain processes in a separate queue, ensuring that these processes do not interfere with the primary workflow execution or cause performance bottlenecks in the main system queue.

**Business Impact:**

This setting directly impacts the system's efficiency and user satisfaction by optimizing the performance of the Pathlock GRC platform. When activated, critical processes can run independently, reducing wait times and improving the responsiveness of the system for end-users.

**Technical Impact when configured:**

Configuring this parameter allows for better resource allocation and management within the Pathlock GRC platform. Processes designated to run in a separate queue may include synchronization tasks or authorization checks, which, due to their potentially heavy computational requirements, can benefit from isolation from the main processing queue.

**Examples Scenario:**

To illustrate, consider an organization needing to synchronize user authorizations from an external HR system routinely. By configuring the RunUserProcessInSeperateQueue parameter, this synchronization process can occur without slowing down other critical operations, such as risk assessments or compliance checks, ensuring that the system remains responsive during peak business hours.

**Related Settings:**

- RunSyncronizeAuthorizationsInSeperateQueue

**Best Practices:** Configure this parameter for processes known to consume significant system resources or during times of high system load to ensure that critical operations continue to run smoothly. Avoid using this for lightweight or infrequently run tasks to prevent unnecessary complexity in system configuration.