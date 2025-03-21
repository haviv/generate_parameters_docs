# Customer Statistics Post Url

**Technical Name:** CustomerStatistics_PostUrl

**Category:** Configuration

**Default Value:** http://usagestats.Pathlock.com/ServerMonitoring.ashx

**Impact Level:** Medium

**Description:**

This setting specifies the URL to which customer statistics and usage data are posted. It is utilized by the Pathlock Cloud GRC platform to monitor and analyze customer usage patterns to enhance system performance and user experience.

**Business Impact:**

Configuring this URL ensures that usage statistics are accurately sent to the specified endpoint, enabling Pathlock to provide insights and improvements based on real usage data. It plays a crucial role in the optimization of resource allocation and system enhancements.

**Technical Impact when configured:**

When properly configured, this URL allows for the seamless transmission of encrypted statistics data to Pathlock's monitoring servers, ensuring that usage patterns are captured without impacting the user experience or system performance.

**Examples Scenario:**

A company configures the CustomerStatistics_PostUrl to point to their specific monitoring endpoint. This enables the organization to track how their users interact with the Pathlock platform, identifying popular features and potential bottlenecks, which in turn assists in prioritizing system improvements and customizations.

**Related Settings:**

- SystemProductKey

**Best Practices:** 
- **Configure when:** Setting up the system for the first time or updating the monitoring server address.
- **Avoid when:** If the organization has strict policies against sending usage data externally.