# Allow Multiple Emergency Access Requests

**Technical Name:** AllowMultipleEmergencyAccessRequests

**Category:** Workflow

**Default Value:** Not provided in the given code references.

**Impact Level:** Medium

**Description:**

The `AllowMultipleEmergencyAccessRequests` parameter determines whether users can submit multiple requests for emergency access simultaneously within the Pathlock Cloud GRC platform. This setting is crucial for managing urgent access requirements in a controlled and auditable manner.

**Business Impact:**

Enabling multiple emergency access requests can significantly enhance an organization's agility in responding to critical incidents or operational demands. By allowing more than one request at a time, businesses can ensure that necessary personnel have the required access to address emergencies promptly. However, it's essential to balance this flexibility with the need to maintain strict access controls and auditability to mitigate the risk of unauthorized access.

**Technical Impact when configured:**

- If enabled, users can initiate multiple emergency access requests without being limited to a single, outstanding request. This allows for greater flexibility during emergency situations.
- If disabled, users must wait for an existing emergency access request to be resolved (approved or denied) before submitting a new one, which could potentially delay response times to critical situations.

**Examples Scenario:**

- A cybersecurity incident requires several team members to gain immediate access to different systems for remediation. Enabling this parameter allows all affected personnel to request emergency access simultaneously, facilitating a swift response to the incident.
- During a high-priority project, multiple contractors may need urgent access to specific applications to meet a tight deadline. With this setting enabled, these requests can be processed in parallel, avoiding project delays.

**Related Settings:** EmergencyAccessRequestsEnabledForAnyone

**Best Practices:** 

- **Configure when:**
  - Your organization operates in a high-paced environment where rapid response to emergencies or critical incidents is often necessary.
  - You have a robust process for reviewing and approving access requests promptly to prevent bottlenecks.
- **Avoid when:**
  - Your organization lacks the administrative bandwidth to review multiple emergency access requests in a timely manner, which could lead to unmonitored access escalations.
  - You operate in a highly regulated industry where each access request must be meticulously documented and justified, potentially making the management of multiple simultaneous requests challenging.