**Technical Name:** Duration_Minutes

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `Duration_Minutes` parameter specifies the length of time, in minutes, for a particular operation or setting within the Pathlock Cloud GRC platform. This can be used to configure timeouts, durations of temporary permissions, or the length of time before an action is executed.

**Business Impact:**

Adjusting the `Duration_Minutes` parameter can directly impact the operational flow within an organization. For example, setting an appropriate duration for temporary access requests can help maintain a balance between operational efficiency and security. A shorter duration minimizes the risk of excessive access, while a longer duration can improve user convenience for longer tasks.

**Technical Impact when configured:**

Proper configuration of the `Duration_Minutes` parameter ensures that operations within the Pathlock GRC platform are executed within a reasonable timeframe, enhancing both security and user experience. Incorrect configuration might lead to either unnecessary restrictions, impacting user productivity, or overly lenient permissions, potentially increasing security risks.

**Examples Scenario:**

- **Temporary Access:** If a user needs temporary access to a sensitive system, the `Duration_Minutes` can be set to the exact time required to complete the job, reducing the risk window.
  
- **Scheduled Jobs:** For scheduled compliance checks that need to run longer due to a large volume of data, adjusting the `Duration_Minutes` ensures that the job completes successfully without timing out.

**Related Settings:** 

- `DailyEmailFooter`
- `DailyEmailFormatedHeader`

**Best Practices:** 

- **Configure when:** There is a clear requirement for the duration a particular operation or permission should last. Use organizational standards and compliance requirements as a guideline.
  
- **Avoid when:** The duration cannot be estimated with a reasonable level of confidence. It's better to use default settings or consult with Pathlock support for best practices.