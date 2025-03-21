# Custom Method External Command Timeout In Seconds

**Technical Name:** CustomMethodExternalCommandTimeoutInSeconds

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

Defines the maximum duration in seconds that the system waits for an external command executed by custom methods to complete. If the external command does not finish within this time frame, the process is automatically terminated. This setting is crucial for ensuring that long-running external commands do not hinder system performance or cause unintended timeouts in other areas of the application.

**Business Impact:**

Setting an appropriate timeout period helps maintain optimal system performance and prevents potential system lock-ups caused by external commands that run indefinitely. It also aids in managing the execution time of scripts and commands that are critical to compliance and risk calculation processes, ensuring they complete within expected timeframes.

**Technical Impact when configured:**

When this parameter is configured, any external command initiated by custom methods in the Pathlock Cloud GRC platform will be forced to terminate if it exceeds the specified timeout period. This can prevent hanging processes but may also interrupt commands that are legitimately taking longer to complete due to complex calculations or data processing requirements.

**Examples Scenario:**

- **Optimizing System Performance:** If certain external scripts used for compliance checks are known to hang or run for extended periods, setting a reasonable timeout can help in avoiding system slowdowns.
- **Preventing Process Hang-up:** In scenarios where third-party tools are executed for data retrieval or modification, ensuring they do not exceed a set time limit can prevent them from causing delays in automated workflows.

**Related Settings:**

- `RoleSearchProviderShowActivitiesIsRoleCount`: Although not directly related, understanding how role count settings are configured might also be valuable when considering overall system performance and timeout needs.

**Best Practices:** 

- **Configure when:** It is known that certain external commands may run indefinitely or significantly longer than expected, potentially impacting system resources or completing critical tasks.
- **Avoid when:** External commands are critical and vary significantly in execution time, where a timeout could interrupt important processes or lead to incomplete executions.