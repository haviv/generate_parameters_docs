# Report Run Time Out In Seconds

**Technical Name:** ReportRunTimeOutInSeconds

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter specifies the maximum amount of time (in seconds) that a report can run before timing out. It is designed to prevent long-running reports from consuming excessive system resources, which could impact the performance of the Pathlock Cloud GRC platform.

**Business Impact:**

Setting an appropriate timeout for report execution helps in managing system performance and ensures that resources are available for other critical tasks. It prevents the system from being overwhelmed by reports that take too long to run, possibly due to complex queries or large volumes of data.

**Technical Impact** when configured:

- Helps in balancing system load by terminating long-running reports.
- Improves overall system response time by freeing up resources.
- Prevents potential timeouts that could occur at the database level due to overly complex report queries.

**Examples Scenario:**

- **Scenario:** An administrator notices that during end-of-month reporting, the system becomes sluggish, impacting other critical functions. By setting a reasonable `ReportRunTimeOutInSeconds`, reports that run longer than the specified time will be terminated, thus helping to manage the system load during peak times.

**Related Settings:**

- KpiChartQuery

**Best Practices:** 

- **Configure when** you observe report run times significantly impacting system performance, especially during peak business reporting periods.
- **Avoid when** reports are known to require more time due to complexity or volume of data but do not negatively impact overall system performance. Consider optimizing report queries or scheduling such reports during off-peak hours instead.