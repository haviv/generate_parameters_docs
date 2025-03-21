# Show Transaction Status Column

**Technical Name:** ShowTransactionStatusColumn

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:** 

Enables the display of the transaction status column in reporting views. This setting allows users to include or exclude transaction status information in the generated reports. 

**Business Impact:**

Including the transaction status in reports enhances visibility into the workflow processes, allowing users to monitor and audit transactional activities effectively. It aids in identifying transactions that are pending, completed, or failed, thereby improving decision-making and operational efficiency.

**Technical Impact when configured:**

When enabled, this parameter adds an additional column to report views that display the status of transactions. It requires additional processing to fetch and display the transaction status, which might slightly affect performance depending on the volume of data being reported.

**Examples Scenario:**

- **Audit Reports:** In audit scenarios where understanding the status of transactions is crucial for compliance and monitoring, enabling this column would provide auditors with detailed insights into each transaction's current state.
- **Operational Reports:** For operational managers needing to oversee the day-to-day activities and ensure processes are running smoothly, including the transaction status enables quick identification of any transactions that may require further attention.

**Related Settings:** 

- AllowMultipleEmergencyAccessRequests

**Best Practices:** 

- **Configure when:** You require detailed reporting that includes the status of transactions to enhance visibility and control over business processes.
- **Avoid when:** Minimalist reporting is needed without the necessity to analyze transaction statuses, or when system performance is a primary concern due to high data volumes.