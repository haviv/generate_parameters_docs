# Customer Statistics Enable Send

**Technical Name:** CustomerStatistics_EnableSend

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the sending of customer statistics data collected within the Pathlock Cloud GRC platform. This setting controls whether statistical data about customer usage is compiled and sent for further analysis.

**Business Impact:**

Activating this parameter allows for a deeper understanding and insights into how the software is used. This can drive improvements in user experience, detect underutilized features, and help in strategic planning for future enhancements. It can also assist in identifying potential areas of risk or non-compliance within user activities.

**Technical Impact when configured:**

When enabled, the system gathers various statistics and sends them to a centralized collection point for analysis. This may include usage patterns, system access times, and feature usage frequencies, among other metrics.

**Examples Scenario:**

A company wants to better understand how its employees are utilizing the Pathlock Cloud GRC platform. By enabling 'CustomerStatistics_EnableSend', administrators can receive reports detailing which features are most used, at what times the system experiences peak usage, and other relevant statistics. This data can then inform training programs, system improvements, or customization efforts to improve efficiency and compliance posture.

**Related Settings:**

- CustomerStatistics_LastSend

**Best Practices:** 

Enable this parameter to gain insights into application usage patterns and to help identify potential areas for system improvement or user training. Avoid enabling if there are significant concerns about data privacy or if the generation and sending of statistics could impact system performance.