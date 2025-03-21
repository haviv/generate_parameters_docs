# Customer Statistics Monitoring Post Url

**Technical Name:** CustomerStatistics_MonitoringPostUrl

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Customer Statistics Monitoring Post URL is a configuration parameter within the Pathlock Cloud GRC platform used to define the endpoint URL for posting system usage statistics. This setting enables the platform to send anonymized usage data to a specified URL for monitoring and analysis purposes.

**Business Impact:**

Configuring this parameter allows the organization to monitor the health and usage of their Pathlock Cloud GRC environment. It assists in understanding how the platform is utilized, which in turn can drive improvements in security, risk management, and compliance processes based on actual usage patterns.

**Technical Impact when configured:**

Once set, the system will automatically send usage statistics to the configured URL. This enables real-time monitoring and can be leveraged for analytics, identifying trends in system use, and potentially highlighting areas where additional training or optimization may be necessary.

**Examples Scenario:**

An organization wants to analyze how their teams are utilizing the Pathlock platform to ensure they are getting the most out of their investment. By configuring the Customer Statistics Monitoring Post URL, they can have detailed usage data sent to their analytics tools, where they can visualize usage patterns, identify popular or underutilized features, and plan targeted training or enhancements accordingly.

**Related Settings:**

- SystemProductKey

**Best Practices:** 

- Configure when: You have a dedicated tool or platform for analyzing usage statistics to make informed decisions based on system usage patterns.
- Avoid when: The destination for the data is not secured or has not been properly vetted, to prevent any potential data leaks or privacy concerns.