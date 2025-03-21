# Check Process Queue Every

**Technical Name:** CheckProcessQueueEvery

**Category:** Configuration

**Default Value:** Not provided in the code references

**Impact Level:** Medium

**Description:**

The `CheckProcessQueueEvery` parameter is designed to define the frequency at which the system checks the process queue for new tasks or jobs to execute. This is crucial for ensuring timely execution and processing within the Pathlock Cloud GRC platform's operational framework.

**Business Impact:**

Setting this parameter optimally ensures that tasks are processed efficiently, reducing delays and potential bottlenecks in system operations. It directly affects the system's responsiveness to new or pending tasks, impacting overall system performance and user satisfaction.

**Technical Impact: when configured**

Properly configuring this parameter can help in balancing system load and improving the execution flow of tasks. A lower value might increase system responsiveness but could also lead to higher CPU usage, whereas a higher value might reduce system load at the cost of responsiveness.

**Examples Scenario:**

- **Scenario 1:** If the system is expected to handle a high volume of short, rapid tasks, setting a lower `CheckProcessQueueEvery` value could improve the throughput by reducing the wait time for each task to be picked up for processing.
  
- **Scenario 2:** In a less demanding environment, where tasks are less time-sensitive, setting a higher value could help in conserving system resources without significantly impacting user experience.

**Related Settings:** 

- `TimeSliceInHoursForReadLog`

**Best Practices:** 

- **configure when:** Adjust the `CheckProcessQueueEvery` parameter based on the operational workload and processing requirements of your organization to maintain an optimal balance between system responsiveness and resource utilization.
  
- **avoid when:** Avoid setting this parameter to an extremely low value in environments with low system resources or if the task queue is usually light, to prevent unnecessary system strain.