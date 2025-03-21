# Direct Execution Of Programs Log Only High Risk Events

**Technical Name:** DirectExectionOfProgramsLogOnlyHighRiskEvents

**Category:** Security

**Default Value:** False

**Impact Level:** High

**Description:**

This setting controls whether only high-risk program execution events are logged by the system. When enabled, it filters the event logging to include only those executions considered critical based on a predefined list of programs. This is intended to reduce noise from less significant events and focus on ones that could signify a security threat.

**Business Impact:**

Enabling this feature will focus security and compliance efforts on high-risk activities, potentially reducing the overhead associated with analyzing logs and responding to security incidents. It can help organizations prioritize their responses and allocate resources more effectively to manage risks.

**Technical Impact when configured:**

- Log files will be smaller and more manageable because only high-risk event executions are recorded.
- The system might perform better due to reduced load from processing and storing extensive logs.
- Security personnel can respond more swiftly and effectively to critical threats without being overwhelmed by large volumes of event data.

**Examples Scenario:**

An organization faces challenges in managing vast amounts of log data, making it hard to identify genuine security threats among numerous low-risk events. By implementing this control, only high-risk events like execution of unauthorized or risky programs are logged. This change helps their security team to focus on investigating and mitigating potential threats, improving their overall security posture.

**Related Settings:** N/A

**Best Practices:** 
- Configure when a focused security monitoring approach is required, especially in high-risk environments where prioritizing threats is essential.
- Avoid when comprehensive logging of all program execution events is necessary for compliance or detailed security monitoring purposes.