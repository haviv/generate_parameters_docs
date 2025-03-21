# Read Usage Keep Alive Interval In Seconds

**Technical Name:** ReadUsageKeepAliveIntervalInSeconds

**Category:** Configuration

**Default Value:** 300

**Impact Level:** Medium

**Description:**

The Read Usage Keep Alive Interval In Seconds parameter is designed to maintain active session status for system log reading processes. It specifies the maximum allowable delay in seconds for inactive log reading sessions before considering them as inactive. This setting plays a critical role in managing system resource utilization and ensuring the timely processing of system logs.

**Business Impact:**

Proper configuration of this parameter helps in balancing the load on system resources, preventing unnecessary strain from prolonged inactive sessions. It optimizes the performance of the system log reading process, which is crucial for maintaining the integrity and security of the system by ensuring all activities are logged and monitored efficiently.

**Technical Impact when configured:**

When configured, this parameter ensures that sessions reading system logs that have not shown activity for the specified interval are marked as inactive. This configuration helps in freeing up system resources taken up by idle sessions, thereby improving the overall performance and responsiveness of the Pathlock Cloud GRC platform.

**Examples Scenario:**

- **Scenario 1:** If the system is experiencing delays in processing system logs due to a high number of inactive log reading sessions, adjusting the Read Usage Keep Alive Interval In Seconds to a lower value can help in quicker identification and termination of inactive sessions, improving log processing times.
  
- **Scenario 2:** In a low-load environment where the immediate freeing up of resources is not critical, setting a higher value can reduce the number of checks performed on active sessions, slightly reducing the overhead on system resources.

**Related Settings:** ReadUsageMaxDelayInSecondsForInactiveRead

**Best Practices:** 

- **Configure when:** There is a need to optimize system resources and improve the efficiency of log processing by preventing systemlogs reading sessions from remaining indefinitely active without making progress.
  
- **Avoid when:** The default setting adequately supports the system's current load and operational efficiency, and changes might lead to unintended resource allocation issues.