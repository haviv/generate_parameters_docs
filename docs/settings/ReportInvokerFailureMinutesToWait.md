# Report Invoker Failure Minutes To Wait

**Technical Name:** ReportInvokerFailureMinutesToWait

**Category:** Configuration

**Default Value:** 5

**Impact Level:** Medium

**Description:**

This parameter defines the number of minutes the system should wait before considering a report invocation as failed. It is crucial in scenarios where report generation might take longer due to data volume or complexity.

**Business Impact:**

Adjusting this parameter can minimize unnecessary report invocation retries, which could lead to system overload and negatively impact performance. It ensures that users receive their reports in a timely manner without jeopardizing system stability.

**Technical Impact when configured:**

Proper configuration of this parameter contributes to optimal application performance and efficient resource utilization. It helps in balancing the load on the system by avoiding premature report failure notifications and unnecessary retries.

**Examples Scenario:**

Scenario: During month-end financial close, the volume of data being processed is significantly higher, leading to longer report generation times. By increasing the `ReportInvokerFailureMinutesToWait`, the system accommodates the additional processing time required, avoiding premature failure notifications and unnecessary report generation attempts.

**Related Settings:**

- ReportInvokerFailureNumberOfRetries

**Best Practices:** 

- Configure this parameter to a higher value during known periods of high reporting demand to prevent unnecessary report invocation failures.
  
- Avoid setting this value too high during normal operation as it may delay the detection of genuine report generation issues, impacting user experience.