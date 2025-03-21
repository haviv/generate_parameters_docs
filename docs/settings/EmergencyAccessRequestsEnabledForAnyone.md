# Emergency Access Requests Enabled For Anyone

**Technical Name:** EmergencyAccessRequestsEnabledForAnyone

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

Enables or disables the feature that allows any user to submit emergency access requests. This setting plays a crucial role in scenarios where immediate access is needed to sensitive or critical systems without going through the usual approval channels.

**Business Impact:**

Enabling this feature can significantly accelerate response times during urgent situations but also poses a security risk if not monitored and controlled properly. Organizations must balance the need for rapid access against the potential for abuse or unauthorized access.

**Technical Impact when configured:**

- If enabled, users can bypass standard access control procedures to gain emergency access, potentially increasing the risk of unauthorized or unintended access to sensitive information or systems.
- If disabled, all emergency access requests must follow predefined workflows, ensuring compliance with organizational policies and reducing the risk of security breaches.

**Examples Scenario:**

- **During an IT outage:** Key personnel might require immediate access to specific systems to resolve issues. Enabling this parameter allows quick response without waiting for manual approval processes.
- **Critical incident response:** In case of a security breach, certain users might need emergency access to investigative tools or systems that they don't usually have access to, enabling swift action to mitigate the incident.

**Related Settings:** 

- ApprovedByAdminAnnotation

**Best Practices:** 

- **Configure when:** There is a clear, immediate business or operational need for rapid emergency access that outweighs security concerns.
- **Avoid when:** The organizational risk profile cannot tolerate the potential for abuse or unauthorized access. In such cases, maintaining standard approval workflows for emergency access is advisable.