# CheckProcessQueueEvery Parameter Documentation

## Category
- System Configuration

## Default Value
- `"m:10"` (Every 10 minutes)

## Impact Level
- Medium

## Description
The `CheckProcessQueueEvery` parameter is used to configure the frequency at which the system checks and processes its queue. This setting is critical for systems that require timely processing of queued tasks or events, such as job scheduling, event handling, and real-time data processing.

## Business Impact
Adjusting this parameter impacts how quickly the system can respond to queued events or tasks. A lower value will make the system more responsive to new events at the potential cost of higher resource consumption. Conversely, a higher value reduces the workload on the system at the risk of delayed processing.

## Technical Impact when Configured
- **Increased Responsiveness**: Lowering the time interval (`m:x`) makes the system check its queue more frequently, potentially leading to faster processing of tasks.
- **Resource Utilization**: More frequent checks may lead to higher CPU and memory usage, impacting the overall system performance especially in resource-constrained environments.
- **Throughput vs. Latency**: There's a trade-off between throughput (how much work is done over a period) and latency (how long it takes to respond to an event). Configuring this setting optimally requires balancing these two aspects based on the specific needs of the business.

## Example Scenario
- **Real-Time Data Processing**: For an application processing real-time data, reducing the `CheckProcessQueueEvery` parameter to `m:5` ensures that data is processed and made available to users more quickly.
- **Batch Jobs**: In contrast, for systems running batch jobs where immediate processing is not critical, increasing the parameter to `m:15` or higher reduces the system's load without significantly affecting user experience.

## Related Settings
- `InitTimerShortSampling`
- `InitTimerReadSapLog`
- Other scheduler-related settings that define specific task frequencies.

## Best Practices
- **Configure When**:
  - Immediate or near-real-time processing is necessary.
  - The system is underutilized, and resources are available for increased polling.
- **Avoid When**:
  - The system is resource-constrained.
  - Tasks do not require immediate processing, allowing for longer intervals between checks to conserve resources.

## Context
The `CheckProcessQueueEvery` parameter plays a pivotal role in determining how the backend processes and workflows within PathlockGRC's ProfileTailor service and application behave, directly impacting performance and responsiveness. Adjusting this setting requires an understanding of the current system load, resource availability, and the business's temporal requirements for task processing.