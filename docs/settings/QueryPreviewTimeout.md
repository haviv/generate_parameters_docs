# Query Preview Timeout

**Technical Name:** QueryPreviewTimeout

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The Query Preview Timeout parameter is designed to manage the duration before a report preview operation times out in the Pathlock Cloud GRC platform. This setting is particularly crucial for optimizing the performance of the reporting feature within the platform, ensuring that report previews load efficiently without causing undue strain on system resources.

**Business Impact:**

Adjusting the Query Preview Timeout can significantly affect the user experience within the Pathlock GRC platform, specifically in how users interact with the reporting functionalities. A well-configured timeout ensures that reports are generated swiftly, enhancing user satisfaction and improving the decision-making process by providing timely insights. Conversely, an inadequately configured timeout may lead to prolonged waits for report previews or even timeout errors, potentially hindering the audit, risk, and compliance processes.

**Technical Impact when configured:**

When the Query Preview Timeout is configured appropriately, it leads to a harmonious balance between system performance and usability. It ensures that the system resources are not overburdened by lengthy report preview operations, thereby maintaining the overall efficiency and responsiveness of the Pathlock GRC platform.

**Examples Scenario:**

For instance, if an organization needs to generate compliance reports frequently and those reports include a substantial amount of data, setting an adequately high Query Preview Timeout can prevent the reports from failing to load. This is crucial during peak operational times when the quick availability of report previews is essential for meeting strict compliance deadlines.

**Related Settings:**

- DashboardSortingOrder

**Best Practices:** 

- **Configure when:** There is a need for balancing system performance with the prompt generation of report previews, especially when dealing with large datasets or complex reports.
  
- **Avoid when:** Default settings adequately meet the organization's reporting speed and system performance needs, or if adjusting the timeout could detrimentally impact the system's overall functionality.