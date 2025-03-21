# Run Synchronize Authorizations In Separate Queue

**Technical Name:** RunSyncronizeAuthorizationsInSeperateQueue

**Category:** Configuration

**Default Value:** 

**Impact Level:** High

**Description:**

Enables the execution of authorization synchronization processes in a separate queue, aiming to optimize performance and system resource allocation during bulk or intensive data processing scenarios.

**Business Impact:**

Effectively segregating authorization synchronization tasks improves system responsiveness and operational efficiency. It ensures critical application functions remain unaffected during heavy data processing, essential for maintaining compliance and security standards without hindering user experience or system performance.

**Technical Impact when configured:**

Configuring this parameter to utilize a separate queue for authorization synchronization can significantly reduce the load on the primary processing queue. This separation facilitates smoother execution of routine tasks and operations, particularly beneficial in environments with high transaction volumes or complex authorization schemes.

**Examples Scenario:**

- A financial institution processes thousands of role updates and permission changes daily. Enabling this parameter ensures these bulk updates do not impact the performance of other critical applications, such as real-time transaction processing or fraud detection systems.
  
**Related Settings:** 

- **RolesSplliterRolesChildRoleSingleRoleFlag**: Indicates settings related to role splitting and child role processing, which may interact with or influence how authorization synchronizations are handled when segregated into a separate queue.

**Best Practices:** configure when

- System experiences latency or performance degradation during large-scale authorization updates.
- There is a need to prioritize business-critical applications and processes while performing background synchronization tasks.

avoid when

- The system is underutilized, or the volume of authorization synchronization tasks does not justify the overhead of managing an additional queue.
- In environments with simple authorization structures and low rates of change, where the benefits do not outweigh the configuration and monitoring efforts.