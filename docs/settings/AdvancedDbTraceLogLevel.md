# Advanced Db Trace Log Level

**Technical Name:** AdvancedDbTraceLogLevel

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** High

**Description:**  
The Advanced Db Trace Log Level parameter allows users to set the verbosity of database trace logs within the Pathlock Cloud GRC platform. This affects how detailed the logs regarding database operations will be.

**Business Impact:**  
Adjusting this parameter can help organizations fine-tune the performance of their GRC activities by controlling the amount of logging detail, which is crucial for debugging and auditing purposes. High verbosity levels can provide deep insights during troubleshooting but may impact system performance due to the increased logging overhead.

**Technical Impact when configured:**  
- **Increased Verbosity:** Higher detail in logs, aiding in precise troubleshooting and debugging at the cost of potential performance degradation.
- **Reduced Verbosity:** Decreases the amount of detailed information logged, potentially improving overall system performance but at the risk of insufficient data for in-depth analysis.

**Examples Scenario:**  
- **Before an Audit:** Increase the Db Trace Log Level to ensure all actions are thoroughly logged, providing auditors with comprehensive data.
- **During Standard Operation:** Keep the Db Trace Log Level at a moderate setting to balance between having a detailed log for potential troubleshooting and maintaining system performance.

**Related Settings:**  
- `EnableExcelMatrixTextRotation`
- `UpdateActiveDirectoryPropertiesOnTerminateUserAction`

**Best Practices:** 
- **Configure when:** Detailed debugging is required, or prior to an audit to ensure all transactions are thoroughly logged.
- **Avoid when:** The system is under heavy load or during peak usage times to prevent additional performance impacts.