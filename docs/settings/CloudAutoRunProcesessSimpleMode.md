# Cloud Auto Run Processes Simple Mode

**Technical Name:** CloudAutoRunProcesessSimpleMode

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** The `CloudAutoRunProcesessSimpleMode` parameter controls the automated execution of processes in a simplified mode within the Pathlock Cloud GRC platform. This is particularly relevant for tasks that involve data file handling and processing in the background, ensuring a streamlined operation without extensive manual intervention.

**Business Impact:** Automating processes in a simple mode can significantly enhance operational efficiency by reducing the time and effort required for manual process execution. It ensures timely execution of critical workflows, thereby minimizing the risk of delays in compliance and reporting activities. This can have a direct impact on the organization's ability to maintain continuous compliance with regulatory standards and internal policies.

**Technical Impact when configured:** When activated, `CloudAutoRunProcesessSimpleMode` initiates automatic processing of tasks based on predefined criteria without manual triggers. This includes the automatic generation and processing of data files for system analysis, ensuring that the latest data is always used in compliance and risk assessment processes.

**Examples Scenario:** An organization requires frequent data analysis of user activities to comply with internal security policies. By enabling `CloudAutoRunProcesessSimpleMode`, data files are automatically generated and processed at scheduled intervals, reducing the need for IT staff to manually execute these processes. This ensures that the organization can continually monitor compliance status and address potential issues more swiftly.

**Related Settings:** WebSiteHostForValidation

**Best Practices:** Configure `CloudAutoRunProcesessSimpleMode` when your organization has clearly defined processes that can be automated without compromising the accuracy or integrity of the task outcomes. Avoid using this feature for complex workflows that require significant customization or manual oversight, as it may not offer the flexibility needed for such operations.