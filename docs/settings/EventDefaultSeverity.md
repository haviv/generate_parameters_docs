# Default Event Severity

**Technical Name:** EventDefaultSeverity

**Category:** Security

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The `EventDefaultSeverity` parameter defines the baseline severity level for events within the Pathlock Cloud GRC platform. It's primarily used in the context of security events generation and handling, allocating a default severity level before any specific severity calculation logic is applied based on the event's nature or type.

**Business Impact:**

Setting an appropriate default event severity is crucial for ensuring that security teams prioritize threats effectively. A well-configured default severity helps in categorizing events properly, ensuring that high-risk events are escalated promptly, while lower-risk events are handled accordingly without overwhelming security teams with false positives.

**Technical Impact when configured:**

When set, the parameter affects the initial severity score assigned to security events, before any custom logic or further analysis is applied. This initial severity plays a key role in the event's lifecycle, including notification, investigation, and response workflows.

**Examples Scenario:**

- A low default severity might result in slower response times for significant security events that were not yet analyzed for custom severity, potentially putting the organization at risk.
  
- A high default severity could lead to alert fatigue, where security teams become overwhelmed by a high volume of high-severity alerts, many of which might not warrant such urgency.

**Related Settings:** Not specified due to lack of direct references in the provided code excerpts.

**Best Practices:** 

- **Configure when**: You have a clear understanding of your organization's security posture and typical event types. This understanding will guide you to set a default severity that reflects the general risk level appropriately.

- **Avoid when**: There's an absence of data on the common or expected security events within your organization. In such cases, it's better to analyze your security needs and event types before setting a default severity that might either overburden your security team or underrepresent serious threats.